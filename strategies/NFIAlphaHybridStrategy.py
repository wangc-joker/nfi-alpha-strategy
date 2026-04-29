from NFIRefactorStrategy import NFIRefactorStrategy
from nfi_refactor.alpha_hybrid.entry import (
    ALPHA_LONG_GRIND_TAGS,
    ALPHA_SHORT_GRIND_TAGS,
    apply_alpha_hybrid_entries,
    populate_alpha_hybrid_indicators,
)
from nfi_refactor.alpha_hybrid.risk import global_loss_exit


class _RiskEntryFilterMixin:
    risk_blocked_base_coins = set()
    risk_blocked_pair_tags = set()

    def _is_risk_blocked_entry(self, pair: str, entry_tag) -> bool:
        base_coin = pair.split("/")[0]
        if base_coin in self.risk_blocked_base_coins:
            return True

        tags = set(str(entry_tag or "").split())
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


class NFIRefactorLowLeverageStrategy(NFIRefactorStrategy):
    """Experimental NFI variant using 1x leverage to reduce floating-loss severity."""

    futures_mode_leverage = 1.0
    futures_mode_leverage_rebuy_mode = 1.0
    futures_mode_leverage_grind_mode = 1.0

    def version(self) -> str:
        return "nfi-refactor-low-leverage-0.1.0"


class NFIRefactorRiskBalancedStrategy(_RiskEntryFilterMixin, NFIRefactorLowLeverageStrategy):
    """Experimental NFI 1x variant filtering historically deep floating-loss entries."""

    risk_blocked_base_coins = {"ZEC"}
    risk_blocked_pair_tags = {("CRV/USDT:USDT", "120")}

    def version(self) -> str:
        return "nfi-refactor-risk-balanced-0.1.0"


class NFIRefactorRiskStrictStrategy(NFIRefactorRiskBalancedStrategy):
    """Experimental NFI 1x variant targeting sub-15% estimated max floating loss."""

    risk_blocked_pair_tags = {
        ("CRV/USDT:USDT", "120"),
        ("UNI/USDT:USDT", "120"),
        ("HYPE/USDT:USDT", "120"),
    }

    def version(self) -> str:
        return "nfi-refactor-risk-strict-0.1.0"


class NFIAlphaHybridStrategy(NFIRefactorStrategy):
    """Experimental strategy: NFI management plus DoubleShun-style entries."""

    alpha_hybrid_entries_enabled = True
    alpha_hybrid_long_entries_enabled = True
    alpha_hybrid_short_entries_enabled = False
    alpha_global_loss_stop_enabled = False
    alpha_global_loss_ratio = 0.05

    alpha_allowed_coins = {
        "BTC",
        "ETH",
        "SOL",
        "XRP",
        "ZEC",
        "DOGE",
        "TAO",
        "HYPE",
        "BNB",
    }

    alpha_trend_ema_fast = 6
    alpha_trend_ema_slow = 46
    alpha_center_window = 5
    alpha_pullback_window = 6
    alpha_restart_window = 4
    alpha_triangle_window = 5
    alpha_compression_window = 11
    alpha_swing_window = 3
    alpha_pullback_depth = 0.009
    alpha_breakout_buffer = 0.009
    alpha_compression_limit = 0.006
    alpha_level_tolerance = 0.016
    alpha_level_proximity = 0.015
    alpha_volume_multiplier = 1.13
    alpha_hourly_long_rsi = 54
    alpha_daily_long_rsi = 55
    alpha_daily_short_rsi = 46

    def __init__(self, config: dict) -> None:
        super().__init__(config)
        self.long_grind_mode_tags = list(self.long_grind_mode_tags) + ALPHA_LONG_GRIND_TAGS
        self.short_grind_mode_tags = list(self.short_grind_mode_tags) + ALPHA_SHORT_GRIND_TAGS

    def version(self) -> str:
        return "nfi-alpha-hybrid-0.1.0"

    def populate_indicators(self, df, metadata: dict):
        df = super().populate_indicators(df, metadata)
        return populate_alpha_hybrid_indicators(self, df, metadata)

    def populate_entry_trend(self, df, metadata: dict):
        df = super().populate_entry_trend(df, metadata)
        return apply_alpha_hybrid_entries(self, df, metadata)

    def custom_exit(
        self,
        pair: str,
        trade,
        current_time,
        current_rate: float,
        current_profit: float,
        **kwargs,
    ):
        loss_exit = global_loss_exit(self, trade, current_profit)
        if loss_exit is not None:
            return loss_exit

        return super().custom_exit(
            pair,
            trade,
            current_time,
            current_rate,
            current_profit,
            **kwargs,
        )


class NFIAlphaHybridLowLeverageStrategy(NFIAlphaHybridStrategy):
    """Experimental NFI+alpha variant using 1x leverage to reduce floating loss."""

    futures_mode_leverage = 1.0
    futures_mode_leverage_rebuy_mode = 1.0
    futures_mode_leverage_grind_mode = 1.0

    def version(self) -> str:
        return "nfi-alpha-hybrid-low-leverage-0.1.0"


class NFIAlphaHybridRiskBalancedStrategy(_RiskEntryFilterMixin, NFIAlphaHybridLowLeverageStrategy):
    """Experimental NFI+alpha 1x variant filtering historically deep floating-loss entries."""

    risk_blocked_base_coins = {"ZEC"}

    def version(self) -> str:
        return "nfi-alpha-hybrid-risk-balanced-0.1.0"
