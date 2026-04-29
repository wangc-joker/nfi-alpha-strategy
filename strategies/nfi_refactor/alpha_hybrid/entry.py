from pandas import DataFrame
import pandas as pd

from nfi_refactor.alpha_hybrid.structure import populate_alpha_structure_indicators


ALPHA_LONG_GRIND_TAGS = [
    "alpha_long_1h_triangle",
    "alpha_long_1d_triangle",
    "alpha_long_1d_center",
]
ALPHA_SHORT_GRIND_TAGS = [
    "alpha_short_1h_center",
    "alpha_short_1h_compression",
    "alpha_short_1d_center",
]


def _as_bool(dataframe: DataFrame, column: str):
    if column not in dataframe.columns:
        return False
    return dataframe[column].fillna(False).eq(True)


def _no_open_signal(dataframe: DataFrame):
    long_signal = pd.to_numeric(dataframe.get("enter_long", 0), errors="coerce").fillna(0)
    short_signal = pd.to_numeric(dataframe.get("enter_short", 0), errors="coerce").fillna(0)
    return (
        long_signal.astype(int).ne(1)
        & short_signal.astype(int).ne(1)
    )


def populate_alpha_hybrid_indicators(strategy, dataframe: DataFrame, metadata: dict) -> DataFrame:
    return populate_alpha_structure_indicators(
        dataframe=dataframe,
        trend_ema_fast=strategy.alpha_trend_ema_fast,
        trend_ema_slow=strategy.alpha_trend_ema_slow,
        center_window=strategy.alpha_center_window,
        pullback_window=strategy.alpha_pullback_window,
        restart_window=strategy.alpha_restart_window,
        triangle_window=strategy.alpha_triangle_window,
        compression_window=strategy.alpha_compression_window,
        swing_window=strategy.alpha_swing_window,
        pullback_depth=strategy.alpha_pullback_depth,
        breakout_buffer=strategy.alpha_breakout_buffer,
        compression_limit=strategy.alpha_compression_limit,
        level_tolerance=strategy.alpha_level_tolerance,
        level_proximity=strategy.alpha_level_proximity,
        volume_multiplier=strategy.alpha_volume_multiplier,
    )


def apply_alpha_hybrid_entries(strategy, dataframe: DataFrame, metadata: dict) -> DataFrame:
    if metadata["pair"].split("/")[0] not in strategy.alpha_allowed_coins:
        return dataframe

    if not strategy.alpha_hybrid_entries_enabled:
        return dataframe

    no_signal = _no_open_signal(dataframe)
    daily_long_ok = dataframe["RSI_14_1d"] > strategy.alpha_daily_long_rsi
    hourly_long_ok = dataframe["RSI_14_1h"] > strategy.alpha_hourly_long_rsi
    daily_short_ok = dataframe["RSI_14_1d"] < strategy.alpha_daily_short_rsi

    long_context = (
        _as_bool(dataframe, "alpha_restart_ready_long")
        & _as_bool(dataframe, "alpha_ema_slow_slope_up")
        & hourly_long_ok
        & daily_long_ok
    )
    short_context = (
        _as_bool(dataframe, "alpha_restart_ready_short")
        & _as_bool(dataframe, "alpha_ema_slow_slope_down")
        & daily_short_ok
    )

    long_triangle = (
        long_context
        & _as_bool(dataframe, "alpha_triangle_breakout_long")
        & _as_bool(dataframe, "alpha_range_tight")
    )
    long_center = long_context & _as_bool(dataframe, "alpha_center_breakout_long")
    short_center = short_context & _as_bool(dataframe, "alpha_center_breakout_short")
    short_compression = short_context & _as_bool(dataframe, "alpha_compression_breakout_short")

    if strategy.alpha_hybrid_long_entries_enabled:
        dataframe.loc[no_signal & long_triangle, ["enter_long", "enter_tag"]] = (
            1,
            "alpha_long_1h_triangle",
        )
        dataframe.loc[no_signal & long_center, ["enter_long", "enter_tag"]] = (
            1,
            "alpha_long_1d_center",
        )

    if strategy.alpha_hybrid_short_entries_enabled:
        dataframe.loc[no_signal & short_center, ["enter_short", "enter_tag"]] = (
            1,
            "alpha_short_1h_center",
        )
        dataframe.loc[no_signal & short_compression, ["enter_short", "enter_tag"]] = (
            1,
            "alpha_short_1h_compression",
        )

    return dataframe
