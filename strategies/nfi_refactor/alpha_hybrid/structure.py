import talib.abstract as ta
from pandas import DataFrame


def populate_alpha_structure_indicators(
    dataframe: DataFrame,
    trend_ema_fast: int,
    trend_ema_slow: int,
    center_window: int,
    pullback_window: int,
    restart_window: int,
    triangle_window: int,
    compression_window: int,
    swing_window: int,
    pullback_depth: float,
    breakout_buffer: float,
    compression_limit: float,
    level_tolerance: float,
    level_proximity: float,
    volume_multiplier: float,
) -> DataFrame:
    """Add DoubleShun-style structure columns on top of the NFI base timeframe.

    The source strategy uses 1h as its base timeframe. This hybrid strategy runs
    on NFI's 5m timeframe, so these columns are explicitly prefixed with
    ``alpha_`` and treated as experimental entry context only.
    """

    half_window = max(2, triangle_window // 2)
    typical_price = (dataframe["high"] + dataframe["low"] + dataframe["close"]) / 3.0

    dataframe["alpha_ema_fast"] = ta.EMA(dataframe, timeperiod=trend_ema_fast)
    dataframe["alpha_ema_slow"] = ta.EMA(dataframe, timeperiod=trend_ema_slow)
    dataframe["alpha_rsi"] = ta.RSI(dataframe, timeperiod=14)
    dataframe["alpha_atr"] = ta.ATR(dataframe, timeperiod=14)
    dataframe["alpha_volume_mean"] = dataframe["volume"].rolling(max(5, triangle_window)).mean()

    dataframe["alpha_market_center"] = typical_price.rolling(center_window).mean()
    dataframe["alpha_center_up"] = dataframe["alpha_market_center"] > dataframe["alpha_market_center"].shift(2)
    dataframe["alpha_center_down"] = dataframe["alpha_market_center"] < dataframe["alpha_market_center"].shift(2)

    dataframe["alpha_uptrend"] = (
        (dataframe["close"] > dataframe["alpha_ema_slow"])
        & (dataframe["alpha_ema_fast"] > dataframe["alpha_ema_slow"])
        & dataframe["alpha_center_up"]
    )
    dataframe["alpha_downtrend"] = (
        (dataframe["close"] < dataframe["alpha_ema_slow"])
        & (dataframe["alpha_ema_fast"] < dataframe["alpha_ema_slow"])
        & dataframe["alpha_center_down"]
    )

    dataframe["alpha_recent_high"] = dataframe["high"].shift(1).rolling(triangle_window).max()
    dataframe["alpha_recent_low"] = dataframe["low"].shift(1).rolling(triangle_window).min()
    dataframe["alpha_recent_high_short"] = dataframe["high"].shift(1).rolling(half_window).max()
    dataframe["alpha_recent_low_short"] = dataframe["low"].shift(1).rolling(half_window).min()
    dataframe["alpha_prior_high_short"] = dataframe["high"].shift(half_window + 1).rolling(half_window).max()
    dataframe["alpha_prior_low_short"] = dataframe["low"].shift(half_window + 1).rolling(half_window).min()

    dataframe["alpha_rising_lows"] = dataframe["alpha_recent_low_short"] > dataframe["alpha_prior_low_short"]
    dataframe["alpha_falling_highs"] = dataframe["alpha_recent_high_short"] < dataframe["alpha_prior_high_short"]
    dataframe["alpha_flat_ceiling"] = (
        (dataframe["alpha_recent_high"] - dataframe["alpha_recent_high_short"]).abs() / dataframe["close"]
    ) < level_tolerance
    dataframe["alpha_flat_floor"] = (
        (dataframe["alpha_recent_low_short"] - dataframe["alpha_recent_low"]).abs() / dataframe["close"]
    ) < level_tolerance

    dataframe["alpha_range_width"] = (
        (
            dataframe["high"].shift(1).rolling(compression_window).max()
            - dataframe["low"].shift(1).rolling(compression_window).min()
        )
        / dataframe["close"]
    )
    dataframe["alpha_range_width_prev"] = dataframe["alpha_range_width"].shift(max(2, compression_window // 2))
    dataframe["alpha_range_tight"] = dataframe["alpha_range_width"] < compression_limit
    dataframe["alpha_range_contracting"] = dataframe["alpha_range_width"] < dataframe["alpha_range_width_prev"]
    dataframe["alpha_volume_expansion"] = dataframe["volume"] > dataframe["alpha_volume_mean"] * volume_multiplier

    dataframe["alpha_pullback_low"] = dataframe["low"].shift(1).rolling(pullback_window).min()
    dataframe["alpha_pullback_high"] = dataframe["high"].shift(1).rolling(pullback_window).max()
    dataframe["alpha_pullback_seen_long"] = dataframe["alpha_pullback_low"] <= (
        dataframe["alpha_ema_fast"] * (1 + pullback_depth)
    )
    dataframe["alpha_pullback_seen_short"] = dataframe["alpha_pullback_high"] >= (
        dataframe["alpha_ema_fast"] * (1 - pullback_depth)
    )
    dataframe["alpha_structure_intact_long"] = dataframe["alpha_pullback_low"] > (
        dataframe["alpha_ema_slow"] * (1 - pullback_depth * 2.0)
    )
    dataframe["alpha_structure_intact_short"] = dataframe["alpha_pullback_high"] < (
        dataframe["alpha_ema_slow"] * (1 + pullback_depth * 2.0)
    )

    dataframe["alpha_restart_ready_long"] = (
        dataframe["alpha_uptrend"]
        & dataframe["alpha_pullback_seen_long"]
        & dataframe["alpha_structure_intact_long"]
        & (dataframe["close"] > dataframe["alpha_ema_fast"])
        & (dataframe["alpha_rsi"] > dataframe["alpha_rsi"].shift(1))
    )
    dataframe["alpha_restart_ready_short"] = (
        dataframe["alpha_downtrend"]
        & dataframe["alpha_pullback_seen_short"]
        & dataframe["alpha_structure_intact_short"]
        & (dataframe["close"] < dataframe["alpha_ema_fast"])
        & (dataframe["alpha_rsi"] < dataframe["alpha_rsi"].shift(1))
    )

    dataframe["alpha_near_high_compression"] = (
        dataframe["close"].shift(1) >= dataframe["alpha_recent_high"] * (1 - level_proximity)
    )
    dataframe["alpha_near_low_compression"] = (
        dataframe["close"].shift(1) <= dataframe["alpha_recent_low"] * (1 + level_proximity)
    )
    dataframe["alpha_breakout_above_recent"] = (
        (dataframe["close"] > dataframe["alpha_recent_high"] * (1 + breakout_buffer))
        & (dataframe["close"].shift(1) <= dataframe["alpha_recent_high"].shift(1) * (1 + breakout_buffer))
    )
    dataframe["alpha_breakout_below_recent"] = (
        (dataframe["close"] < dataframe["alpha_recent_low"] * (1 - breakout_buffer))
        & (dataframe["close"].shift(1) >= dataframe["alpha_recent_low"].shift(1) * (1 - breakout_buffer))
    )
    dataframe["alpha_ema_slow_slope_up"] = dataframe["alpha_ema_slow"] > dataframe["alpha_ema_slow"].shift(3)
    dataframe["alpha_ema_slow_slope_down"] = dataframe["alpha_ema_slow"] < dataframe["alpha_ema_slow"].shift(3)

    dataframe["alpha_triangle_breakout_long"] = (
        dataframe["alpha_restart_ready_long"]
        & dataframe["alpha_rising_lows"]
        & dataframe["alpha_flat_ceiling"]
        & dataframe["alpha_range_contracting"]
        & dataframe["alpha_breakout_above_recent"]
        & dataframe["alpha_volume_expansion"]
    )
    dataframe["alpha_triangle_breakout_short"] = (
        dataframe["alpha_restart_ready_short"]
        & dataframe["alpha_falling_highs"]
        & dataframe["alpha_flat_floor"]
        & dataframe["alpha_range_contracting"]
        & dataframe["alpha_breakout_below_recent"]
        & dataframe["alpha_volume_expansion"]
    )

    dataframe["alpha_center_breakout_long"] = (
        dataframe["alpha_restart_ready_long"]
        & dataframe["alpha_center_up"]
        & dataframe["alpha_range_contracting"]
        & dataframe["alpha_near_high_compression"]
        & (dataframe["alpha_market_center"] > dataframe["alpha_market_center"].shift(1))
        & dataframe["alpha_breakout_above_recent"]
        & (dataframe["close"] > dataframe["alpha_market_center"])
        & dataframe["alpha_volume_expansion"]
    )
    dataframe["alpha_center_breakout_short"] = (
        dataframe["alpha_restart_ready_short"]
        & dataframe["alpha_center_down"]
        & dataframe["alpha_range_contracting"]
        & dataframe["alpha_near_low_compression"]
        & (dataframe["alpha_market_center"] < dataframe["alpha_market_center"].shift(1))
        & dataframe["alpha_breakout_below_recent"]
        & (dataframe["close"] < dataframe["alpha_market_center"])
        & dataframe["alpha_volume_expansion"]
    )

    dataframe["alpha_compression_breakout_short"] = (
        dataframe["alpha_restart_ready_short"]
        & dataframe["alpha_range_tight"]
        & dataframe["alpha_range_contracting"]
        & dataframe["alpha_near_low_compression"]
        & dataframe["alpha_breakout_below_recent"]
        & dataframe["alpha_volume_expansion"]
    )

    dataframe["alpha_structure_stop_long"] = dataframe["low"].shift(1).rolling(swing_window).min()
    dataframe["alpha_structure_stop_short"] = dataframe["high"].shift(1).rolling(swing_window).max()

    return dataframe
