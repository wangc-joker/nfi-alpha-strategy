from NFIRefactorStrategy import NFIRefactorStrategy
from nfi_refactor.alpha_hybrid.entry import (
    ALPHA_LONG_GRIND_TAGS,
    ALPHA_SHORT_GRIND_TAGS,
    apply_alpha_hybrid_entries,
    populate_alpha_hybrid_indicators,
)
from nfi_refactor.alpha_hybrid.risk import global_loss_exit


class NFIAlphaHybridStrategy(NFIRefactorStrategy):
    """Experimental strategy: NFI management plus DoubleShun-style entries."""

    alpha_hybrid_entries_enabled = True
    alpha_hybrid_long_entries_enabled = True
    alpha_hybrid_short_entries_enabled = False
    alpha_global_loss_stop_enabled = True
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
