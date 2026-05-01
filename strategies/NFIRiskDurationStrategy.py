from datetime import timedelta

from NFIRefactorStrategy import NFIRefactorStrategy


class NFIRiskDurationBalancedStrategy(NFIRefactorStrategy):
    """Risk-focused NFI variant keeping leverage unchanged while cutting deep/long holds."""

    risk_hard_stop_profit = -0.18
    risk_grind_timeout_days = 21
    risk_max_hold_days = 45
    risk_timeout_profit_ceiling = 0.02
    risk_blocked_tags = set()
    risk_blocked_pair_tags = set()

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
