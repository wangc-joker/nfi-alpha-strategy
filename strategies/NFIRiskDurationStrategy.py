from datetime import timedelta

from NFIRefactorStrategy import NFIRefactorStrategy


def _safe_ratio(value, fallback=0.0):
    try:
        if value != value:
            return fallback
        return float(value)
    except (TypeError, ValueError):
        return fallback


class NFIRiskDurationBalancedStrategy(NFIRefactorStrategy):
    """Risk-focused NFI variant keeping leverage unchanged while cutting deep/long holds."""

    risk_hard_stop_profit = -0.18
    risk_grind_timeout_days = 21
    risk_max_hold_days = 45
    risk_timeout_profit_ceiling = 0.02
    risk_blocked_tags = set()
    risk_blocked_pair_tags = set()
    risk_use_dynamic_entry_filter = False
    risk_dynamic_block_score = 2
    risk_dynamic_btc_dump_1h = -3.5
    risk_dynamic_btc_rsi_1h = 38.0
    risk_dynamic_recent_drop_48 = -8.0
    risk_dynamic_roc9 = -5.0
    risk_dynamic_bb_width = 12.0
    risk_dynamic_volume_spike = 3.0
    risk_dynamic_volume_dry = 0.35

    def populate_indicators(self, df, metadata: dict):
        df = super().populate_indicators(df, metadata)

        df["risk_volume_mean_288"] = df["volume"].rolling(288, min_periods=72).mean()
        df["risk_volume_ratio_288"] = df["volume"] / df["risk_volume_mean_288"]
        df["risk_drop_from_48_high"] = (df["close"] / df["close_max_48"] - 1.0) * 100.0
        df["risk_btc_dump"] = (
            (df.get("btc_ROC_9_1h", 0) <= self.risk_dynamic_btc_dump_1h)
            | (df.get("btc_RSI_14_1h", 50) <= self.risk_dynamic_btc_rsi_1h)
        )
        df["risk_pair_dump"] = (
            (df["risk_drop_from_48_high"] <= self.risk_dynamic_recent_drop_48)
            | (df["ROC_9"] <= self.risk_dynamic_roc9)
        )
        df["risk_high_volatility"] = (
            (df["BBB_40_2.0"] >= self.risk_dynamic_bb_width)
            | (df["risk_volume_ratio_288"] >= self.risk_dynamic_volume_spike)
        )
        df["risk_weak_volume"] = df["risk_volume_ratio_288"] <= self.risk_dynamic_volume_dry
        df["risk_dynamic_score"] = (
            df["risk_btc_dump"].astype(int)
            + df["risk_pair_dump"].astype(int)
            + df["risk_high_volatility"].astype(int)
            + df["risk_weak_volume"].astype(int)
        )
        return df

    def version(self) -> str:
        return "nfi-risk-duration-balanced-0.1.0"

    def _entry_tags(self, entry_tag) -> set[str]:
        return set(str(entry_tag or "").split())

    def _trade_age(self, trade, current_time):
        open_time = getattr(trade, "open_date_utc", None) or getattr(trade, "open_date", None)
        if open_time is None:
            return timedelta(0)
        if getattr(open_time, "tzinfo", None) is not None and getattr(current_time, "tzinfo", None) is None:
            open_time = open_time.replace(tzinfo=None)
        elif getattr(open_time, "tzinfo", None) is None and getattr(current_time, "tzinfo", None) is not None:
            current_time = current_time.replace(tzinfo=None)
        return current_time - open_time

    def _is_risk_blocked_entry(self, pair: str, entry_tag) -> bool:
        tags = self._entry_tags(entry_tag)
        if tags.intersection(self.risk_blocked_tags):
            return True

        for blocked_pair, blocked_tag in self.risk_blocked_pair_tags:
            if pair == blocked_pair and blocked_tag in tags:
                return True
        return False

    def _is_dynamic_risk_blocked(self, pair: str, current_time, side: str) -> bool:
        if not self.risk_use_dynamic_entry_filter or side == "short":
            return False

        dataframe, _ = self.dp.get_analyzed_dataframe(pair, self.timeframe)
        if dataframe is None or dataframe.empty:
            return False

        current_candle = dataframe.iloc[-1]
        risk_score = _safe_ratio(current_candle.get("risk_dynamic_score"), 0.0)
        if risk_score >= self.risk_dynamic_block_score:
            return True

        btc_dump = bool(current_candle.get("risk_btc_dump", False))
        pair_dump = bool(current_candle.get("risk_pair_dump", False))
        high_volatility = bool(current_candle.get("risk_high_volatility", False))
        weak_volume = bool(current_candle.get("risk_weak_volume", False))
        return btc_dump and (pair_dump or high_volatility or weak_volume)

    def _dynamic_risk_mask(self, dataframe):
        score_block = dataframe["risk_dynamic_score"] >= self.risk_dynamic_block_score
        combo_block = dataframe["risk_btc_dump"] & (
            dataframe["risk_pair_dump"]
            | dataframe["risk_high_volatility"]
            | dataframe["risk_weak_volume"]
        )
        return score_block | combo_block

    def populate_entry_trend(self, df, metadata: dict):
        df = super().populate_entry_trend(df, metadata)
        if not self.risk_use_dynamic_entry_filter:
            return df

        risk_mask = self._dynamic_risk_mask(df)
        if "enter_long" in df.columns:
            df.loc[risk_mask, "enter_long"] = 0
        return df

    def confirm_trade_entry(
        self,
        pair: str,
        order_type: str,
        amount: float,
        rate: float,
        time_in_force: str,
        current_time,
        entry_tag,
        side: str,
        **kwargs,
    ) -> bool:
        if self._is_risk_blocked_entry(pair, entry_tag):
            return False
        if self._is_dynamic_risk_blocked(pair, current_time, side):
            return False

        return super().confirm_trade_entry(
            pair,
            order_type,
            amount,
            rate,
            time_in_force,
            current_time,
            entry_tag,
            side,
            **kwargs,
        )

    def custom_exit(
        self,
        pair: str,
        trade,
        current_time,
        current_rate: float,
        current_profit: float,
        **kwargs,
    ):
        age = self._trade_age(trade, current_time)
        tags = self._entry_tags(getattr(trade, "enter_tag", None))

        if current_profit <= self.risk_hard_stop_profit:
            return "risk_hard_stop"

        if "120" in tags and age >= timedelta(days=self.risk_grind_timeout_days):
            if current_profit <= self.risk_timeout_profit_ceiling:
                return "risk_grind_timeout"

        if age >= timedelta(days=self.risk_max_hold_days):
            return "risk_max_hold"

        return super().custom_exit(
            pair,
            trade,
            current_time,
            current_rate,
            current_profit,
            **kwargs,
        )


class NFIRiskDurationStrictStrategy(NFIRiskDurationBalancedStrategy):
    risk_hard_stop_profit = -0.12
    risk_grind_timeout_days = 10
    risk_max_hold_days = 21
    risk_timeout_profit_ceiling = 0.03

    def version(self) -> str:
        return "nfi-risk-duration-strict-0.1.0"


class NFIRiskDurationFilteredStrategy(NFIRiskDurationBalancedStrategy):
    risk_hard_stop_profit = -0.16
    risk_grind_timeout_days = 14
    risk_max_hold_days = 30
    risk_timeout_profit_ceiling = 0.03
    risk_blocked_pair_tags = {
        ("ZEC/USDT:USDT", "120"),
        ("CRV/USDT:USDT", "120"),
        ("ETH/USDT:USDT", "120"),
    }

    def version(self) -> str:
        return "nfi-risk-duration-filtered-0.1.0"


class NFIRiskDurationNoGrind120Strategy(NFIRiskDurationBalancedStrategy):
    """Remove the historically deepest drawdown grind entry while preserving other NFI logic."""

    risk_hard_stop_profit = -0.14
    risk_grind_timeout_days = 14
    risk_max_hold_days = 21
    risk_timeout_profit_ceiling = 0.03
    risk_blocked_tags = {"120"}

    def version(self) -> str:
        return "nfi-risk-duration-no-grind-120-0.1.0"


class NFIRiskDurationLowMaeStrategy(NFIRiskDurationNoGrind120Strategy):
    """More defensive variant targeting lower maximum adverse excursion."""

    risk_hard_stop_profit = -0.12
    risk_max_hold_days = 14
    risk_blocked_pair_tags = {
        ("RIVER/USDT:USDT", "61"),
        ("RIVER/USDT:USDT", "62"),
        ("RIVER/USDT:USDT", "63"),
        ("UNI/USDT:USDT", "62"),
    }

    def version(self) -> str:
        return "nfi-risk-duration-low-mae-0.1.0"


class NFIRiskDurationSelectiveStrategy(NFIRiskDurationLowMaeStrategy):
    """Selective filter removing the concentrated loss clusters found in the low-MAE run."""

    risk_blocked_pair_tags = NFIRiskDurationLowMaeStrategy.risk_blocked_pair_tags | {
        ("ZEC/USDT:USDT", "6"),
        ("ZEC/USDT:USDT", "104"),
        ("ZEC/USDT:USDT", "143"),
        ("APT/USDT:USDT", "141"),
        ("UNI/USDT:USDT", "143"),
        ("UNI/USDT:USDT", "145"),
        ("ARB/USDT:USDT", "163"),
    }

    def version(self) -> str:
        return "nfi-risk-duration-selective-0.1.0"


class NFIRiskDurationDynamicGuardStrategy(NFIRiskDurationBalancedStrategy):
    """General risk filter without pair-specific blacklists."""

    risk_hard_stop_profit = -0.14
    risk_grind_timeout_days = 14
    risk_max_hold_days = 21
    risk_timeout_profit_ceiling = 0.03
    risk_use_dynamic_entry_filter = True
    risk_dynamic_block_score = 2

    def version(self) -> str:
        return "nfi-risk-duration-dynamic-guard-0.1.0"


class NFIRiskDurationDynamicGuardLooseStrategy(NFIRiskDurationDynamicGuardStrategy):
    """Looser market-state filter, intended to keep more upside while avoiding obvious stress."""

    risk_hard_stop_profit = -0.16
    risk_max_hold_days = 30
    risk_dynamic_block_score = 3
    risk_dynamic_btc_dump_1h = -5.0
    risk_dynamic_btc_rsi_1h = 34.0
    risk_dynamic_recent_drop_48 = -11.0
    risk_dynamic_roc9 = -7.0
    risk_dynamic_bb_width = 16.0
    risk_dynamic_volume_spike = 4.5
    risk_dynamic_volume_dry = 0.25

    def version(self) -> str:
        return "nfi-risk-duration-dynamic-guard-loose-0.1.0"


class NFIRiskDurationDynamicGuardStrictStrategy(NFIRiskDurationDynamicGuardStrategy):
    """Stricter market-state filter targeting lower MAE over raw return."""

    risk_hard_stop_profit = -0.12
    risk_max_hold_days = 14
    risk_dynamic_block_score = 2
    risk_dynamic_btc_dump_1h = -2.5
    risk_dynamic_btc_rsi_1h = 42.0
    risk_dynamic_recent_drop_48 = -6.5
    risk_dynamic_roc9 = -4.0
    risk_dynamic_bb_width = 10.0
    risk_dynamic_volume_spike = 2.5
    risk_dynamic_volume_dry = 0.45

    def version(self) -> str:
        return "nfi-risk-duration-dynamic-guard-strict-0.1.0"


class NFIRiskDurationSignalGuardStrategy(NFIRiskDurationDynamicGuardStrategy):
    """Non-coin-specific guard: remove high-risk grind signal and use market stress filter."""

    risk_blocked_tags = {"120"}

    def version(self) -> str:
        return "nfi-risk-duration-signal-guard-0.1.0"


class NFIRiskDurationSignalGuardLooseStrategy(NFIRiskDurationDynamicGuardLooseStrategy):
    """Looser signal-level guard without pair-specific overrides."""

    risk_blocked_tags = {"120"}

    def version(self) -> str:
        return "nfi-risk-duration-signal-guard-loose-0.1.0"


class NFIRiskDurationSignalGuardStrictStrategy(NFIRiskDurationDynamicGuardStrictStrategy):
    """Stricter signal-level guard without pair-specific overrides."""

    risk_blocked_tags = {"120"}

    def version(self) -> str:
        return "nfi-risk-duration-signal-guard-strict-0.1.0"
