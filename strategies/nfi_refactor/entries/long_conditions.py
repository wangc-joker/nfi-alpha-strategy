import numpy as np

def append_long_120(
    strategy,
    df,
    long_entry_logic,
    num_open_long_grind_mode,
    is_pair_long_grind_mode,
) -> None:
    """Append NFI long condition #120, the grind-mode long entry."""
    # Protections
    long_entry_logic.append(num_open_long_grind_mode < strategy.grind_mode_max_slots)
    long_entry_logic.append(df["protections_long_global"] == True)
    long_entry_logic.append(is_pair_long_grind_mode)
    long_entry_logic.append(df["RSI_3"] <= 50.0)
    long_entry_logic.append(df["RSI_3_15m"] >= 20.0)
    long_entry_logic.append(df["RSI_3_1h"] >= 10.0)
    long_entry_logic.append(df["RSI_3_4h"] >= 10.0)
    long_entry_logic.append(df["RSI_14_1h"] < 80.0)
    long_entry_logic.append(df["RSI_14_4h"] < 80.0)
    long_entry_logic.append(df["RSI_14_1d"] < 80.0)
    long_entry_logic.append(df["AROONU_14_1d"] < 100.0)
    long_entry_logic.append(df["STOCHRSIk_14_14_3_3_1d"] < 90.0)

    # Logic
    long_entry_logic.append(
        (df["STOCHRSIk_14_14_3_3"] < 20.0)
        & (df["WILLR_14"] < -80.0)
        & (df["AROONU_14"] < 25.0)
        & (df["close"] < (df["EMA_20"] * 0.978))
    )

def append_long_141(df, long_entry_logic, allowed_empty_candles_288, is_pair_long_top_coins_mode) -> None:
    """Append NFI long condition #141, a top-coins long entry."""
    long_entry_logic.append(is_pair_long_top_coins_mode)
    long_entry_logic.append(df["num_empty_288"] <= allowed_empty_candles_288)
    long_entry_logic.append(df["protections_long_global"] == True)

    long_entry_logic.append(
      # 5m & 15m down move, 15m high
      ((df["RSI_3"] > 3.0) | (df["RSI_3_15m"] > 15.0) | (df["AROONU_14_15m"] < 70.0))
      # 5m & 15m down move, 4h still high
      & ((df["RSI_3"] > 3.0) | (df["RSI_3_15m"] > 15.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 50.0))
      # 5m & 15m down move, 15m high
      & ((df["RSI_3"] > 3.0) | (df["RSI_3_15m"] > 20.0) | (df["AROONU_14_15m"] < 70.0))
      # 5m & 1h down move, 15m still high
      & ((df["RSI_3"] > 3.0) | (df["RSI_3_1h"] > 15.0) | (df["AROONU_14_15m"] < 40.0))
      # 5m & 1h down move, 1h high
      & ((df["RSI_3"] > 3.0) | (df["RSI_3_1h"] > 45.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 80.0))
      # 5m & 4h down move, 15m still high
      & ((df["RSI_3"] > 3.0) | (df["RSI_3_4h"] > 5.0) | (df["AROONU_14_15m"] < 40.0))
      # 5m & 4h down move, 15m still high
      & ((df["RSI_3"] > 3.0) | (df["RSI_3_4h"] > 5.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 40.0))
      # 5m & 4h down move, 15m still high
      & ((df["RSI_3"] > 3.0) | (df["RSI_3_4h"] > 20.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 50.0))
      # 5m & 4h down move, 1h high
      & ((df["RSI_3"] > 3.0) | (df["RSI_3_4h"] > 45.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 80.0))
      # 5m & 1d down move, 15m high
      & ((df["RSI_3"] > 3.0) | (df["RSI_3_1d"] > 10.0) | (df["AROONU_14_15m"] < 70.0))
      # 5m & 1d down move, 15m stil high
      & ((df["RSI_3"] > 3.0) | (df["RSI_3_1d"] > 10.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 40.0))
      # 5m & 1d down move, 4h still high
      & ((df["RSI_3"] > 3.0) | (df["RSI_3_1d"] > 10.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 40.0))
      # 5m down move, 1h high
      & ((df["RSI_3"] > 3.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 90.0))
      # 5m down move, 15m & 1d high
      & ((df["RSI_3"] > 5.0) | (df["AROONU_14_15m"] < 60.0) | (df["AROONU_14_1d"] < 100.0))
      # 5m down move, 1h & 1d high
      & ((df["RSI_3"] > 10.0) | (df["AROONU_14_1h"] < 80.0) | (df["AROONU_14_1d"] < 100.0))
      # 15m & 1h down move, 1d overbought
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_1h"] > 10.0) | (df["ROC_9_1d"] < 100.0))
      # 15m & 1h down move, 1h still not low enough
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_1h"] > 10.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 20.0))
      # 15m & 1h down move, 1d overbought
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_1h"] > 10.0) | (df["ROC_9_1d"] < 60.0))
      # 15m & 1h down move, 4h still high
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_1h"] > 15.0) | (df["AROONU_14_4h"] < 40.0))
      # 15m & 1h down move, 4h high
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_1h"] > 15.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 90.0))
      # 15m & 1h down move, 1d still high
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_1h"] > 20.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 50.0))
      # 15m & 1h down move, 15m high
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_1h"] > 30.0) | (df["AROONU_14_15m"] < 70.0))
      # 15m & 1h down move, 1d high
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_1h"] > 30.0) | (df["AROONU_14_1d"] < 80.0))
      # 15m & 1h down move, 4h high
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_1h"] > 40.0) | (df["AROONU_14_1h"] < 85.0))
      # 15m & 1h down move, 1h high
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_1h"] > 40.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 80.0))
      # 15m & 1h down move, 1h high
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_1h"] > 45.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 80.0))
      # 15m & 1h down move, 1d high
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_1h"] > 45.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 80.0))
      # 15m & 4h down move, 15m downtrend
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_4h"] > 3.0) | (df["CMF_20_15m"] > -0.30))
      # 15m & 4h down move, 4h still high
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_4h"] > 25.0) | (df["AROONU_14_4h"] < 40.0))
      # 15m down move, 1h high, 4h overbought
      & ((df["RSI_3_15m"] > 3.0) | (df["AROONU_14_1h"] < 70.0) | (df["ROC_9_4h"] < 10.0))
      # 15m down move, 1d high & overbought
      & ((df["RSI_3_15m"] > 3.0) | (df["AROONU_14_1d"] < 70.0) | (df["ROC_9_1d"] < 10.0))
      # 15m & 1h down move, 4h still high
      & ((df["RSI_3_15m"] > 5.0) | (df["RSI_3_1h"] > 10.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 50.0))
      # 15m & 1h down move, 1h still high
      & ((df["RSI_3_15m"] > 5.0) | (df["RSI_3_1h"] > 25.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 50.0))
      # 15m & 1h down move, 1h high
      & ((df["RSI_3_15m"] > 5.0) | (df["RSI_3_1h"] > 30.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 80.0))
      # 15m & 4h down move, 1d high
      & ((df["RSI_3_15m"] > 5.0) | (df["RSI_3_4h"] > 15.0) | (df["AROONU_14_1d"] < 70.0))
      # 15m & 4h down move, 1d high
      & ((df["RSI_3_15m"] > 5.0) | (df["RSI_3_4h"] > 20.0) | (df["AROONU_14_1d"] < 80.0))
      # 15m & 1d down move, 1d still high
      & ((df["RSI_3_15m"] > 5.0) | (df["RSI_3_1d"] > 10.0) | (df["AROONU_14_1d"] < 40.0))
      # 15m down move, 15m downtrend, 1d high
      & ((df["RSI_3_15m"] > 5.0) | (df["CMF_20_15m"] > -0.40) | (df["AROONU_14_1d"] < 100.0))
      # 15m down move, 4h high, 1h overbought
      & ((df["RSI_3_15m"] > 5.0) | (df["AROONU_14_4h"] < 100.0) | (df["ROC_9_1h"] < 10.0))
      # 15m & 1h down move, 4h high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1h"] > 10.0) | (df["AROONU_14_4h"] < 85.0))
      # 15m & 1h down move, 1d high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1h"] > 10.0) | (df["AROONU_14_1d"] < 85.0))
      # 15m & 1h down move, 15m still high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1h"] > 15.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 50.0))
      # 15m & 1h down move, 1h still high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1h"] > 15.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 50.0))
      # 15m & 1h down move, 1d still high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1h"] > 15.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 50.0))
      # 15m & 1h down move, 15m high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1h"] > 20.0) | (df["AROONU_14_15m"] < 60.0))
      # 15m & 1h down move, 1h high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1h"] > 20.0) | (df["AROONU_14_1h"] < 80.0))
      # 15m & 1h down move, 1h high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1h"] > 30.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 70.0))
      # 15m & 1h down move, 1d overbought
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1h"] > 30.0) | (df["ROC_9_1d"] < 60.0))
      # 15m & 4h down move, 15m still high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_4h"] > 10.0) | (df["AROONU_14_15m"] < 40.0))
      # 15m & 4h down move, 1d high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_4h"] > 10.0) | (df["AROONU_14_1d"] < 80.0))
      # 15m & 4h down move, 1d downtrend
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_4h"] > 10.0) | (df["ROC_9_1d"] > -20.0))
      # 15m & 4h down move, 1d overbought
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_4h"] > 15.0) | (df["ROC_9_1d"] < 20.0))
      # 15m & 4h down move, 1d high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_4h"] > 20.0) | (df["RSI_14_1d"] < 70.0))
      # 15m & 4h down move, 15m high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_4h"] > 20.0) | (df["AROONU_14_15m"] < 60.0))
      # 15m & 4h down move, 4h still high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_4h"] > 20.0) | (df["AROONU_14_4h"] < 50.0))
      # 15m & 4h down move, 1d high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_4h"] > 20.0) | (df["AROONU_14_1d"] < 80.0))
      # 15m & 4h down move, 1h high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_4h"] > 20.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 70.0))
      # 15m & 4h down move, 1d high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_4h"] > 20.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 80.0))
      # 15m & 4h down move, 1d overbought
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_4h"] > 20.0) | (df["ROC_9_1d"] < 50.0))
      # 15m & 4h down move, 1d high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_4h"] > 30.0) | (df["ROC_9_1d"] < 30.0))
      # 15m & 4h down move, 15m high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_4h"] > 40.0) | (df["AROONU_14_15m"] < 70.0))
      # 15m & 4h down move, 4h high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_4h"] > 45.0) | (df["AROONU_14_4h"] < 70.0))
      # 15m down move, 1h high
      & ((df["RSI_3_15m"] > 10.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 90.0))
      # 15m & 1d down move, 1h still high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1d"] > 10.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 50.0))
      # 15m & 1d down move, 1d high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1d"] > 30.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 60.0))
      # 15m down move, 15m & 1h high
      & ((df["RSI_3_15m"] > 10.0) | (df["AROONU_14_15m"] < 60.0) | (df["AROONU_14_1h"] < 100.0))
      # 15m down move, 15m & 4h high
      & ((df["RSI_3_15m"] > 10.0) | (df["AROONU_14_15m"] < 60.0) | (df["AROONU_14_4h"] < 70.0))
      # 15m down move, 15m high, 1h high
      & ((df["RSI_3_15m"] > 10.0) | (df["AROONU_14_15m"] < 70.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 80.0))
      # 15m down move, 4h high, 1d overbought
      & ((df["RSI_3_15m"] > 10.0) | (df["AROONU_14_4h"] < 70.0) | (df["ROC_9_1d"] < 100.0))
      # 15m down move, 1d high & overbought
      & ((df["RSI_3_15m"] > 10.0) | (df["AROONU_14_1d"] < 85.0) | (df["ROC_9_1d"] < 20.0))
      # 15m down move, 1h high, 1d overbought
      & ((df["RSI_3_15m"] > 10.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 50.0) | (df["ROC_9_1d"] < 40.0))
      # 15m & 1h down move, 1h high
      & ((df["RSI_3_15m"] > 15.0) | (df["RSI_3_1h"] > 15.0) | (df["AROONU_14_1h"] < 70.0))
      # 15m & 1h down move, 4h high
      & ((df["RSI_3_15m"] > 15.0) | (df["RSI_3_1h"] > 15.0) | (df["AROONU_14_4h"] < 80.0))
      # 15m & 1h down move, 1h high
      & ((df["RSI_3_15m"] > 15.0) | (df["RSI_3_1h"] > 40.0) | (df["AROONU_14_1h"] < 90.0))
      # 15m & 4h down move, 15m high
      & ((df["RSI_3_15m"] > 15.0) | (df["RSI_3_4h"] > 15.0) | (df["AROONU_14_15m"] < 50.0))
      # 15m & 4h down move, 1h high
      & ((df["RSI_3_15m"] > 15.0) | (df["RSI_3_4h"] > 15.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 70.0))
      # 15m & 4h down move, 15m high
      & ((df["RSI_3_15m"] > 15.0) | (df["RSI_3_4h"] > 20.0) | (df["AROONU_14_15m"] < 70.0))
      # 15m & 4h down move, 4h high
      & ((df["RSI_3_15m"] > 15.0) | (df["RSI_3_4h"] > 25.0) | (df["AROONU_14_4h"] < 60.0))
      # 15m & 4h down move, 4h still high
      & ((df["RSI_3_15m"] > 15.0) | (df["RSI_3_4h"] > 25.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 40.0))
      # 15m & 4h down move, 1h high
      & ((df["RSI_3_15m"] > 15.0) | (df["RSI_3_4h"] > 35.0) | (df["AROONU_14_1h"] < 90.0))
      # 15m & 1d down move, 1h still high
      & ((df["RSI_3_15m"] > 15.0) | (df["RSI_3_1d"] > 15.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 30.0))
      # 15m down move, 15m downtrend, 1h high
      & ((df["RSI_3_15m"] > 15.0) | (df["CMF_20_15m"] > -0.40) | (df["AROONU_14_1h"] < 60.0))
      # 15m down move, 15m still high, 4h high
      & ((df["RSI_3_15m"] > 15.0) | (df["AROONU_14_15m"] < 50.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 80.0))
      # 15m down move, 15m high, 1d overbought
      & ((df["RSI_3_15m"] > 15.0) | (df["AROONU_14_15m"] < 70.0) | (df["ROC_9_1d"] < 20.0))
      # 15m down move, 1h & 4h high
      & ((df["RSI_3_15m"] > 15.0) | (df["AROONU_14_1h"] < 100.0) | (df["AROONU_14_4h"] < 100.0))
      # 15m down move, 4h & 1d overbought
      & ((df["RSI_3_15m"] > 15.0) | (df["ROC_9_4h"] < 20.0) | (df["ROC_9_1d"] < 80.0))
      # 15m down move, 1h high, 1d overbought
      & ((df["RSI_3_15m"] > 20.0) | (df["AROONU_14_1h"] < 80.0) | (df["ROC_9_1d"] < 10.0))
      # 15m down move, 1h high, 1d downtrend
      & ((df["RSI_3_15m"] > 20.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 80.0) | (df["ROC_9_1d"] > -20.0))
      # 15m down move, 4h high, 1d downtrend
      & ((df["RSI_3_15m"] > 20.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 80.0) | (df["ROC_9_1d"] > -30.0))
      # 15m & 4h down move, 15m high
      & ((df["RSI_3_15m"] > 25.0) | (df["RSI_3_4h"] > 30.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 70.0))
      # 15m down move, 15m & 1h high
      & ((df["RSI_3_15m"] > 25.0) | (df["AROONU_14_15m"] < 70.0) | (df["AROONU_14_1h"] < 100.0))
      # 15m & 4h down mve, 1h high
      & ((df["RSI_3_15m"] > 30.0) | (df["RSI_3_4h"] > 30.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 80.0))
      # 15m & 4h down move, 4h high
      & ((df["RSI_3_15m"] > 30.0) | (df["RSI_3_4h"] > 45.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 80.0))
      # 15m down move, 15m & 1h high
      & ((df["RSI_3_15m"] > 30.0) | (df["AROONU_14_15m"] < 70.0) | (df["AROONU_14_1h"] < 90.0))
      # 15m down move, 1h high, 1d downtrend
      & ((df["RSI_3_15m"] > 30.0) | (df["AROONU_14_1h"] < 90.0) | (df["ROC_9_1d"] > -10.0))
      # 15m down move, 15m high, 4h high
      & ((df["RSI_3_15m"] > 35.0) | (df["AROONU_14_15m"] < 70.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 80.0))
      # 15m down move, 15m & 4h high
      & ((df["RSI_3_15m"] > 35.0) | (df["AROONU_14_15m"] < 70.0) | (df["AROONU_14_4h"] < 90.0))
      # 1h & 4h down move, 4h still not low enough
      & ((df["RSI_3_1h"] > 3.0) | (df["RSI_3_4h"] > 10.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 10.0))
      # 1h & 4h down move, 1d overbought
      & ((df["RSI_3_1h"] > 3.0) | (df["RSI_3_4h"] > 25.0) | (df["ROC_9_1d"] < 10.0))
      # 1h & 1d down move, 1d still high
      & ((df["RSI_3_1h"] > 3.0) | (df["RSI_3_1d"] > 25.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 40.0))
      # 1h & 4h down move, 15m still not low enough
      & ((df["RSI_3_1h"] > 5.0) | (df["RSI_3_4h"] > 5.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 20.0))
      # 1h & 4h down move, 4h downtrend
      & ((df["RSI_3_1h"] > 5.0) | (df["RSI_3_4h"] > 10.0) | (df["ROC_9_4h"] > -10.0))
      # 1h & 4h down move, 15m high
      & ((df["RSI_3_1h"] > 5.0) | (df["RSI_3_4h"] > 25.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 60.0))
      # 1h & 4h down move, 1d still high
      & ((df["RSI_3_1h"] > 10.0) | (df["RSI_3_4h"] > 10.0) | (df["AROONU_14_1d"] < 50.0))
      # 1h & 4h down move, 15m still high
      & ((df["RSI_3_1h"] > 10.0) | (df["RSI_3_4h"] > 10.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 70.0))
      # 1h & 4h down move, 4h still not low enough
      & ((df["RSI_3_1h"] > 10.0) | (df["RSI_3_4h"] > 15.0) | (df["AROONU_14_4h"] < 30.0))
      # 1h & 4h down move, 4h still high
      & ((df["RSI_3_1h"] > 10.0) | (df["RSI_3_4h"] > 20.0) | (df["AROONU_14_4h"] < 40.0))
      # 1h & 4h down move, 4h high
      & ((df["RSI_3_1h"] > 10.0) | (df["RSI_3_4h"] > 25.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 60.0))
      # 1h & 4h down move, 4h high
      & ((df["RSI_3_1h"] > 10.0) | (df["RSI_3_4h"] > 40.0) | (df["AROONU_14_4h"] < 70.0))
      # 1h & 1d down move, 1h still not low enough
      & ((df["RSI_3_1h"] > 10.0) | (df["RSI_3_1d"] > 15.0) | (df["AROONU_14_1h"] < 20.0))
      # 1h & 1d down move, 1h still not low enough
      & ((df["RSI_3_1h"] > 10.0) | (df["RSI_3_1d"] > 20.0) | (df["AROONU_14_1h"] < 30.0))
      # 1h down move, 15m downtrend, 1d high
      & ((df["RSI_3_1h"] > 10.0) | (df["CMF_20_15m"] > -0.40) | (df["AROONU_14_1d"] < 70.0))
      # 1h down move, 1h high, 4h high
      & ((df["RSI_3_1h"] > 10.0) | (df["AROONU_14_1h"] < 70.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 80.0))
      # 1h & 4h down move, 1h still high
      & ((df["RSI_3_1h"] > 15.0) | (df["RSI_3_4h"] > 15.0) | (df["AROONU_14_1h"] < 40.0))
      # 1h & 4h down move, 1h still high
      & ((df["RSI_3_1h"] > 15.0) | (df["RSI_3_4h"] > 15.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 50.0))
      # 1h & 4h down move, 1d downtrend
      & ((df["RSI_3_1h"] > 15.0) | (df["RSI_3_4h"] > 15.0) | (df["ROC_9_1d"] > -30.0))
      # 1h & 1d down move, 4h downtrend
      & ((df["RSI_3_1h"] > 15.0) | (df["RSI_3_1d"] > 15.0) | (df["ROC_9_4h"] > -30.0))
      # 1h & 1d down move, 1d still high
      & ((df["RSI_3_1h"] > 15.0) | (df["RSI_3_1d"] > 25.0) | (df["AROONU_14_1d"] < 50.0))
      # 1h & 1d down move, 1d high
      & ((df["RSI_3_1h"] > 15.0) | (df["RSI_3_1d"] > 35.0) | (df["AROONU_14_1d"] < 70.0))
      # 1h down move, 1h still high, 1d high
      & ((df["RSI_3_1h"] > 15.0) | (df["AROONU_14_1h"] < 50.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 80.0))
      # 1h down move, 1h still high, 4h overbought
      & ((df["RSI_3_1h"] > 15.0) | (df["AROONU_14_1h"] < 50.0) | (df["ROC_9_4h"] < 10.0))
      # 1h down move, 1h still high, 1d downtrend
      & ((df["RSI_3_1h"] > 15.0) | (df["AROONU_14_1h"] < 50.0) | (df["ROC_9_1d"] > -30.0))
      # 1h down move, 4h still high, 1d overbought
      & ((df["RSI_3_1h"] > 15.0) | (df["AROONU_14_4h"] < 50.0) | (df["ROC_9_1d"] < 40.0))
      # 1h down move, 1d high, 4h downtrend
      & ((df["RSI_3_1h"] > 15.0) | (df["AROONU_14_1d"] < 70.0) | (df["ROC_9_4h"] > -20.0))
      # 1h & 4h down move, 1d high
      & ((df["RSI_3_1h"] > 20.0) | (df["RSI_3_4h"] > 25.0) | (df["AROONU_14_1d"] < 80.0))
      # 1h & 4h down move, 1d overbought
      & ((df["RSI_3_1h"] > 20.0) | (df["RSI_3_4h"] > 30.0) | (df["ROC_9_1d"] < 100.0))
      # 1h & 4h down move, 1h high
      & ((df["RSI_3_1h"] > 20.0) | (df["RSI_3_4h"] > 35.0) | (df["AROONU_14_1h"] < 70.0))
      # 1h & 4h down move, 4h high
      & ((df["RSI_3_1h"] > 20.0) | (df["RSI_3_4h"] > 50.0) | (df["AROONU_14_4h"] < 100.0))
      # 1h & 4h down move, 1d downtrend
      & ((df["RSI_3_1h"] > 20.0) | (df["RSI_3_1d"] > 25.0) | (df["ROC_9_1d"] > -30.0))
      # 1h down move, 15m still high, 1d high
      & ((df["RSI_3_1h"] > 20.0) | (df["AROONU_14_15m"] < 40.0) | (df["AROONU_14_1d"] < 90.0))
      # 1h down move, 1h high, 1d overbought
      & ((df["RSI_3_1h"] > 20.0) | (df["AROONU_14_1h"] < 60.0) | (df["ROC_9_1d"] < 10.0))
      # 1h & 4h down move, 15m high
      & ((df["RSI_3_1h"] > 25.0) | (df["RSI_3_4h"] > 25.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 70.0))
      # 1h & 4h down move, 1h high
      & ((df["RSI_3_1h"] > 25.0) | (df["RSI_3_4h"] > 30.0) | (df["AROONU_14_1h"] < 80.0))
      # 1h & 4h down move, 4h high
      & ((df["RSI_3_1h"] > 25.0) | (df["RSI_3_4h"] > 30.0) | (df["AROONU_14_4h"] < 60.0))
      # 1h & 4h down move, 1d high
      & ((df["RSI_3_1h"] > 30.0) | (df["RSI_3_4h"] > 35.0) | (df["RSI_14_1d"] < 80.0))
      # 1h down move, 1d high & overbought
      & ((df["RSI_3_1h"] > 30.0) | (df["AROONU_14_1d"] < 85.0) | (df["ROC_9_1d"] < 40.0))
      # 1h down move, 1d high & overbought
      & ((df["RSI_3_1h"] > 30.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 80.0) | (df["ROC_9_1d"] < 20.0))
      # 1h down move, 15m still high, 1h high
      & ((df["RSI_3_1h"] > 30.0) | (df["AROONU_14_15m"] < 50.0) | (df["AROONU_14_1h"] < 85.0))
      # 1h down move, 4h high, 1d overbought
      & ((df["RSI_3_1h"] > 30.0) | (df["AROONU_14_4h"] < 90.0) | (df["ROC_9_1d"] < 40.0))
      # 1h & 4h down move, 1h still high
      & ((df["RSI_3_1h"] > 35.0) | (df["RSI_3_4h"] > 35.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 50.0))
      # 1h & 4h down move, 4h high
      & ((df["RSI_3_1h"] > 35.0) | (df["RSI_3_4h"] > 50.0) | (df["AROONU_14_4h"] < 80.0))
      # 1h down move, 1h high , 1d overbought
      & ((df["RSI_3_1h"] > 35.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 80.0) | (df["ROC_9_1d"] < 30.0))
      # 1h down move, 4h high, 1d overbought
      & ((df["RSI_3_1h"] > 35.0) | (df["AROONU_14_4h"] < 70.0) | (df["ROC_9_1d"] < 100.0))
      # 1h & 1d down move, 1h high
      & ((df["RSI_3_1h"] > 45.0) | (df["RSI_3_1d"] > 45.0) | (df["AROONU_14_1h"] < 80.0))
      # 1h down move, 1h & 4h high
      & ((df["RSI_3_1h"] > 45.0) | (df["AROONU_14_1h"] < 80.0) | (df["AROONU_14_4h"] < 100.0))
      # 1h down move, 4h high & overbought
      & ((df["RSI_3_1h"] > 50.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 90.0) | (df["ROC_9_4h"] < 25.0))
      # 1h & 1d down move, 1h high
      & ((df["RSI_3_1h"] > 60.0) | (df["RSI_3_1d"] > 60.0) | (df["AROONU_14_1h"] < 70.0))
      # 4h & 1d down move, 1d still high
      & ((df["RSI_3_4h"] > 3.0) | (df["RSI_3_1d"] > 20.0) | (df["RSI_14_1d"] < 40.0))
      # 4h down move, 1h still not low enough, 4h downtrend
      & ((df["RSI_3_4h"] > 3.0) | (df["AROONU_14_1h"] < 20.0) | (df["ROC_9_4h"] > -10.0))
      # 4h & 1d down move, 1d still high
      & ((df["RSI_3_4h"] > 5.0) | (df["RSI_3_1d"] > 30.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 40.0))
      # 4h down move, 1h high
      & ((df["RSI_3_4h"] > 5.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 90.0))
      # 4h down move, 4h & 1d downtrend
      & ((df["RSI_3_4h"] > 5.0) | (df["ROC_9_4h"] > -10.0) | (df["ROC_9_1d"] > -10.0))
      # 4h & 1d down move, 1h high
      & ((df["RSI_3_4h"] > 10.0) | (df["RSI_3_1d"] > 10.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 60.0))
      # 4h & 1d down move, 4h downtrend
      & ((df["RSI_3_4h"] > 10.0) | (df["RSI_3_1d"] > 10.0) | (df["ROC_9_4h"] > -20.0))
      # 4h & 1d down move, 1d still high
      & ((df["RSI_3_4h"] > 10.0) | (df["RSI_3_1d"] > 15.0) | (df["AROONU_14_1d"] < 40.0))
      # 4h & 1d down move, 1d downtrend
      & ((df["RSI_3_4h"] > 10.0) | (df["RSI_3_1d"] > 15.0) | (df["ROC_9_1d"] > -30.0))
      # 4h & 1d down move, 1h high
      & ((df["RSI_3_4h"] > 10.0) | (df["RSI_3_1d"] > 30.0) | (df["AROONU_14_1h"] < 100.0))
      # 4h down move, 15m still high, 1h still high
      & ((df["RSI_3_4h"] > 10.0) | (df["AROONU_14_15m"] < 40.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 50.0))
      # 4h down move, 4h still high, 4h downtrend
      & ((df["RSI_3_4h"] > 10.0) | (df["AROONU_14_4h"] < 40.0) | (df["ROC_9_4h"] > -20.0))
      # 4h down move, 15m high
      & ((df["RSI_3_4h"] > 10.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 80.0))
      # 4h down move, 1h still not low enough, 4h downtrend
      & ((df["RSI_3_4h"] > 10.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 20.0) | (df["ROC_9_4h"] > -20.0))
      # 4h & 1d down move, 15m still high
      & ((df["RSI_3_4h"] > 15.0) | (df["RSI_3_1d"] > 15.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 50.0))
      # 4h & 1d down move, 1h still high
      & ((df["RSI_3_4h"] > 15.0) | (df["RSI_3_1d"] > 15.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 40.0))
      # 4h & 1d down move, 1d high
      & ((df["RSI_3_4h"] > 15.0) | (df["RSI_3_1d"] > 20.0) | (df["AROONU_14_1d"] < 60.0))
      # 4h & 1d down move, 4h high
      & ((df["RSI_3_4h"] > 15.0) | (df["RSI_3_1d"] > 25.0) | (df["AROONU_14_4h"] < 70.0))
      # 4h & 1d down move, 4h still high
      & ((df["RSI_3_4h"] > 15.0) | (df["RSI_3_1d"] > 30.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 50.0))
      # 4h & 1d down move, 1d high
      & ((df["RSI_3_4h"] > 15.0) | (df["RSI_3_1d"] > 40.0) | (df["AROONU_14_1d"] < 70.0))
      # 4h & 1d down move, 4h still high
      & ((df["RSI_3_4h"] > 15.0) | (df["RSI_3_1d"] > 50.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 40.0))
      # 4h down move, 4h still high, 4h downtrend
      & ((df["RSI_3_4h"] > 15.0) | (df["AROONU_14_4h"] < 50.0) | (df["ROC_9_4h"] > -10.0))
      # 4h down move, 1d still high, 1d downtrend
      & ((df["RSI_3_4h"] > 15.0) | (df["AROONU_14_1d"] < 50.0) | (df["ROC_9_1d"] > -20.0))
      # 4h down move, 4h still not low enough, 1d downtrend
      & ((df["RSI_3_4h"] > 15.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 20.0) | (df["ROC_9_1d"] > -20.0))
      # 4h down move, 1h downtrend, 1d overbought
      & ((df["RSI_3_4h"] > 15.0) | (df["ROC_9_1h"] > -10.0) | (df["ROC_9_1d"] < 200.0))
      # 4h down move, 4h high, 4h downtrend
      & ((df["RSI_3_4h"] > 20.0) | (df["AROONU_14_4h"] < 60.0) | (df["ROC_9_4h"] > -20.0))
      # 4h down move, 1d high & overbought
      & ((df["RSI_3_4h"] > 20.0) | (df["AROONU_14_1d"] < 80.0) | (df["ROC_9_1d"] < 70.0))
      # 4h down move, 4h & 1d downtrend
      & ((df["RSI_3_4h"] > 25.0) | (df["ROC_9_4h"] > -10.0) | (df["ROC_9_1d"] > -10.0))
      # 1h down move, 4h still not low enough, 1d downtrend
      & ((df["RSI_3_4h"] > 20.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 30.0) | (df["ROC_9_1d"] > -20.0))
      # 4h & 1d down move, 1h high
      & ((df["RSI_3_4h"] > 25.0) | (df["RSI_3_1d"] > 25.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 80.0))
      # 4h down move, 1h high
      & ((df["RSI_3_4h"] > 25.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 70.0))
      # 4h & 1d down move, 1d overbought
      & ((df["RSI_3_4h"] > 25.0) | (df["RSI_3_1d"] > 40.0) | (df["ROC_9_1d"] < 30.0))
      # 4h & 1d down move, 4h still high
      & ((df["RSI_3_4h"] > 30.0) | (df["RSI_3_1d"] > 30.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 50.0))
      # 4h & 1d down move, 1d high
      & ((df["RSI_3_4h"] > 30.0) | (df["RSI_3_1d"] > 60.0) | (df["AROONU_14_1d"] < 90.0))
      # 4h down move, 15m & 4h high
      & ((df["RSI_3_4h"] > 30.0) | (df["AROONU_14_15m"] < 70.0) | (df["AROONU_14_4h"] < 70.0))
      # 4h down move, 1h high, 1d downtrend
      & ((df["RSI_3_4h"] > 30.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 80.0) | (df["ROC_9_1d"] > -40.0))
      # 4h down move, 4h & 1d downtrend
      & ((df["RSI_3_4h"] > 30.0) | (df["ROC_9_4h"] > -20.0) | (df["ROC_9_1d"] > -40.0))
      # 4h down move, 4h still high, 1d downtrend
      & ((df["RSI_3_4h"] > 35.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 40.0) | (df["ROC_9_1d"] > -30.0))
      # 4h down move, 1d high & overbought
      & ((df["RSI_3_4h"] > 35.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 80.0) | (df["ROC_9_1d"] < 20.0))
      # 4h down move, 15m still high, 1h high
      & ((df["RSI_3_4h"] > 35.0) | (df["AROONU_14_15m"] < 50.0) | (df["AROONU_14_1h"] < 100.0))
      # 4h down move, 1d high & overbought
      & ((df["RSI_3_4h"] > 45.0) | (df["AROONU_14_1d"] < 70.0) | (df["ROC_9_1d"] < 20.0))
      # 4h down move, 1d high & overbought
      & ((df["RSI_3_4h"] > 55.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 90.0) | (df["ROC_9_1d"] < 100.0))
      # 1d down move, 1d high, 4h downtrend
      & ((df["RSI_3_1d"] > 15.0) | (df["AROONU_14_1d"] < 70.0) | (df["ROC_9_4h"] > -40.0))
      # 1d down move, 1h & 4h high
      & ((df["RSI_3_1d"] > 30.0) | (df["AROONU_14_1h"] < 70.0) | (df["AROONU_14_4h"] < 100.0))
      # 1d down move, 4h high, 1d overbought
      & ((df["RSI_3_1d"] > 45.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 90.0) | (df["ROC_9_1d"] < 10.0))
      # 1d down move, 1d high & overbought
      & ((df["RSI_3_1d"] > 55.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 80.0) | (df["ROC_9_1d"] < 10.0))
      # 1d down move, 1d overbought
      & ((df["RSI_3_1d"] > 60.0) | (df["ROC_9_1d"] < 200.0))
      # 15m & 1h high, 4h overbought
      & ((df["AROONU_14_15m"] < 70.0) | (df["AROONU_14_1h"] < 100.0) | (df["ROC_9_4h"] < 15.0))
      # 15m & 1h high, 1d overbought
      & ((df["AROONU_14_15m"] < 70.0) | (df["AROONU_14_1h"] < 100.0) | (df["ROC_9_1d"] < 100.0))
      # 15m & 1h high, 1d downtrend
      & ((df["AROONU_14_15m"] < 70.0) | (df["AROONU_14_1h"] < 100.0) | (df["ROC_9_1d"] > -10.0))
      # 15m high, 1d high & overbought
      & ((df["AROONU_14_15m"] < 70.0) | (df["AROONU_14_1d"] < 90.0) | (df["ROC_9_1d"] < 30.0))
      # 15m high, 1d high & overbought
      & ((df["AROONU_14_15m"] < 70.0) | (df["AROONU_14_1d"] < 100.0) | (df["ROC_9_1d"] < 20.0))
      # 15m high, 1h high, 1d downtrend
      & ((df["AROONU_14_15m"] < 70.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 80.0) | (df["ROC_9_1d"] > -20.0))
      # 1h & 4h high, 4h overbought
      & ((df["AROONU_14_1h"] < 90.0) | (df["AROONU_14_4h"] < 90.0) | (df["ROC_9_4h"] < 10.0))
      # 1h & 4h high, 1d overbought
      & ((df["AROONU_14_1h"] < 90.0) | (df["AROONU_14_4h"] < 100.0) | (df["ROC_9_1d"] < 50.0))
      # 1h & 1d high, 1d overbought
      & ((df["AROONU_14_1h"] < 100.0) | (df["AROONU_14_1d"] < 100.0) | (df["ROC_9_1d"] < 40.0))
      # 4h & 1d high, 4h overbought
      & ((df["AROONU_14_4h"] < 100.0) | (df["AROONU_14_1d"] < 100.0) | (df["ROC_9_4h"] < 50.0))
      # 4h & 1d high, 1d overbought
      & ((df["AROONU_14_4h"] < 90.0) | (df["AROONU_14_1d"] < 100.0) | (df["ROC_9_1d"] < 50.0))
      # 4h & 1d overbought
      & ((df["ROC_9_4h"] < 100.0) | (df["ROC_9_1d"] < 200.0))
    )

    # Logic
    long_entry_logic.append(
      (df["RSI_20"] < df["RSI_20"].shift(1))
      & (df["RSI_3"] < 30.0)
      & (df["AROONU_14"] < 25.0)
      & (df["close"] < df["SMA_16"] * 0.960)
    )


def append_long_142(df, long_entry_logic, allowed_empty_candles_288, is_pair_long_top_coins_mode) -> None:
    """Append NFI long condition #142, a top-coins long entry."""
    long_entry_logic.append(is_pair_long_top_coins_mode)
    long_entry_logic.append(df["num_empty_288"] <= allowed_empty_candles_288)
    long_entry_logic.append(df["protections_long_global"] == True)

    long_entry_logic.append(
      # 5m & 4h down move, 15m high
      ((df["RSI_3"] > 10.0) | (df["RSI_3_4h"] > 10.0) | (df["AROONU_14_15m"] < 40.0))
      # 5m & 1d down move, 15m high
      & ((df["RSI_3"] > 10.0) | (df["RSI_3_1d"] > 30.0) | (df["AROONU_14_15m"] < 80.0))
      # 5m down move, 1h & 1d high
      & ((df["RSI_3"] > 10.0) | (df["AROONU_14_1h"] < 80.0) | (df["AROONU_14_1d"] < 100.0))
      # 5m down move, 15m & 1h high
      & ((df["RSI_3"] > 10.0) | (df["AROONU_14_15m"] < 85.0) | (df["AROONU_14_1h"] < 100.0))
      # 15m & 1h & 4h down move
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_1h"] > 3.0) | (df["RSI_3_4h"] > 15.0))
      # 15m & 1h down move, 1d high
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_1h"] > 10.0) | (df["AROONU_14_1d"] < 70.0))
      # 15m & 1h down move, 1h still high
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_1h"] > 10.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 40.0))
      # 15m & 1h down move, 1d overbought
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_1h"] > 10.0) | (df["ROC_9_1d"] < 60.0))
      # 15m & 1h down move, 1h still high
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_1h"] > 15.0) | (df["AROONU_14_1h"] < 50.0))
      # 15m & 1h down move, 4h still high
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_1h"] > 15.0) | (df["AROONU_14_4h"] < 40.0))
      # 15m & 1h down move, 4h high
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_1h"] > 15.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 90.0))
      # 15m & 1h down move, 15m high
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_1h"] > 30.0) | (df["AROONU_14_15m"] < 70.0))
      # 15m & 1h down move, 1h high
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_1h"] > 40.0) | (df["AROONU_14_1h"] < 75.0))
      # 15m & 4h down move, 1d downtrend
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_4h"] > 10.0) | (df["ROC_9_1d"] > -20.0))
      # 15m & 4h down move, 4h still high
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_4h"] > 25.0) | (df["AROONU_14_4h"] < 40.0))
      # 15m down move, 1h high, 4h overbought
      & ((df["RSI_3_15m"] > 3.0) | (df["AROONU_14_1h"] < 70.0) | (df["ROC_9_4h"] < 10.0))
      # 15m down move, 4h high
      & ((df["RSI_3_15m"] > 3.0) | (df["AROONU_14_4h"] < 90.0))
      # 15m down move, 1h high, 1d overbought
      & ((df["RSI_3_15m"] > 3.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 60.0) | (df["ROC_9_1d"] < 20.0))
      # 15m down move, 4h high
      & ((df["RSI_3_15m"] > 3.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 80.0))
      # 15m & 1h down move, 15m still not low enough
      & ((df["RSI_3_15m"] > 5.0) | (df["RSI_3_1h"] > 5.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 30.0))
      # 15m & 1h down move, 4h still high
      & ((df["RSI_3_15m"] > 5.0) | (df["RSI_3_1h"] > 10.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 50.0))
      # 15m & 4h down move, 1d high
      & ((df["RSI_3_15m"] > 5.0) | (df["RSI_3_4h"] > 15.0) | (df["AROONU_14_1d"] < 70.0))
      # 15m & 4h down move, 15m high
      & ((df["RSI_3_15m"] > 5.0) | (df["RSI_3_4h"] > 20.0) | (df["AROONU_14_15m"] < 60.0))
      # 15m & 1h down move, 4h high
      & ((df["RSI_3_15m"] > 5.0) | (df["RSI_3_1h"] > 15.0) | (df["AROONU_14_4h"] < 85.0))
      # 15m & 1h down move, 4h high
      & ((df["RSI_3_15m"] > 5.0) | (df["RSI_3_1h"] > 15.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 60.0))
      # 15m & 4h down move, 1d high
      & ((df["RSI_3_15m"] > 5.0) | (df["RSI_3_4h"] > 20.0) | (df["AROONU_14_1d"] < 80.0))
      # 15m down move, 4h high, 1h overbought
      & ((df["RSI_3_15m"] > 5.0) | (df["AROONU_14_4h"] < 100.0) | (df["ROC_9_1h"] < 10.0))
      # 15m & 1h down move, 4h high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1h"] > 10.0) | (df["AROONU_14_4h"] < 85.0))
      # 15m & 1h down move, 1h still high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1h"] > 10.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 40.0))
      # 15m & 1h down move, 4h high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1h"] > 10.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 60.0))
      # 15m & 1h down move, 1h still high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1h"] > 15.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 50.0))
      # 15m & 1h down move, 15m high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1h"] > 20.0) | (df["AROONU_14_15m"] < 60.0))
      # 15m & 1h down move, 15m still high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1h"] > 25.0) | (df["AROONU_14_15m"] < 40.0))
      # 15m & 1h down move, 1h high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1h"] > 30.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 70.0))
      # 15m & 1h down move, 1d overbought
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1h"] > 30.0) | (df["ROC_9_1d"] < 60.0))
      # 15m & 4h down move, 1d still high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_4h"] > 10.0) | (df["AROONU_14_1d"] < 50.0))
      # 15m & 4h down move, 15m still high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_4h"] > 15.0) | (df["AROONU_14_15m"] < 50.0))
      # 15m & 4h down move, 1d high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_4h"] > 15.0) | (df["AROONU_14_1d"] < 80.0))
      # 15m & 4h down move, 1d overbought
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_4h"] > 15.0) | (df["ROC_9_1d"] < 20.0))
      # 15m & 4h down move, 1d high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_4h"] > 20.0) | (df["RSI_14_1d"] < 70.0))
      # 15m & 4h down move, 4h still high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_4h"] > 20.0) | (df["AROONU_14_4h"] < 50.0))
      # 14m & 4h down move, 1d high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_4h"] > 20.0) | (df["AROONU_14_1d"] < 80.0))
      # 15m & 4h down move, 1h high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_4h"] > 20.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 70.0))
      # 15m & 4h down move, 1d high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_4h"] > 20.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 80.0))
      # 15m & 4h down move, 1d overbought
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_4h"] > 20.0) | (df["ROC_9_1d"] < 50.0))
      # 15m & 4h down move, 15m high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_4h"] > 30.0) | (df["AROONU_14_15m"] < 70.0))
      # 15m & 4h down move, 1d high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_4h"] > 30.0) | (df["ROC_9_1d"] < 30.0))
      # 15m & 4h down move, 1h high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_4h"] > 35.0) | (df["AROONU_14_1h"] < 90.0))
      # 15m & 4h down move, 4h overbought
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_4h"] > 35.0) | (df["ROC_9_4h"] < 10.0))
      # 15m & 4h down move, 15m high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_4h"] > 40.0) | (df["AROONU_14_15m"] < 70.0))
      # 15m & 1d down move, 1h still high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1d"] > 10.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 50.0))
      # 15m down move, 15m high, 1h high
      & ((df["RSI_3_15m"] > 10.0) | (df["AROONU_14_15m"] < 70.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 80.0))
      # 15m down move, 4h high, 1d overbought
      & ((df["RSI_3_15m"] > 10.0) | (df["AROONU_14_4h"] < 70.0) | (df["ROC_9_1d"] < 100.0))
      # 15m down move, 1d high & overbought
      & ((df["RSI_3_15m"] > 10.0) | (df["AROONU_14_1d"] < 85.0) | (df["ROC_9_1d"] < 20.0))
      # 15m down move, 1h high, 1d overbought
      & ((df["RSI_3_15m"] > 10.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 50.0) | (df["ROC_9_1d"] < 40.0))
      # 15m & 1h down move, 1h high
      & ((df["RSI_3_15m"] > 15.0) | (df["RSI_3_1h"] > 15.0) | (df["AROONU_14_1h"] < 70.0))
      # 15m & 1h down move, 4h high
      & ((df["RSI_3_15m"] > 15.0) | (df["RSI_3_1h"] > 25.0) | (df["AROONU_14_4h"] < 100.0))
      # 15m & 1h down move, 1h high
      & ((df["RSI_3_15m"] > 15.0) | (df["RSI_3_1h"] > 40.0) | (df["AROONU_14_1h"] < 90.0))
      # 15m & 4h down move, 15m high
      & ((df["RSI_3_15m"] > 15.0) | (df["RSI_3_4h"] > 15.0) | (df["AROONU_14_15m"] < 70.0))
      # 15m & 4h down move, 1d downtrend
      & ((df["RSI_3_15m"] > 15.0) | (df["RSI_3_4h"] > 15.0) | (df["ROC_9_1d"] > -20.0))
      # 15m & 4h down move, 1d overbought
      & ((df["RSI_3_15m"] > 15.0) | (df["RSI_3_4h"] > 20.0) | (df["ROC_9_1d"] < 50.0))
      # 15m & 4h down move, 1h high
      & ((df["RSI_3_15m"] > 15.0) | (df["RSI_3_4h"] > 35.0) | (df["AROONU_14_1h"] < 90.0))
      # 15m & 1d down move, 4h high
      & ((df["RSI_3_15m"] > 15.0) | (df["RSI_3_1d"] > 20.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 80.0))
      # 15m down move, 15m downtrend, 1h high
      & ((df["RSI_3_15m"] > 15.0) | (df["CMF_20_15m"] > -0.40) | (df["AROONU_14_1h"] < 60.0))
      # 15m down move, 15m still high, 4h high
      & ((df["RSI_3_15m"] > 15.0) | (df["AROONU_14_15m"] < 50.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 80.0))
      # 15m down move, 15m high, 1d overbought
      & ((df["RSI_3_15m"] > 15.0) | (df["AROONU_14_15m"] < 70.0) | (df["ROC_9_1d"] < 10.0))
      # 15m down move, 1h & 4h high
      & ((df["RSI_3_15m"] > 15.0) | (df["AROONU_14_1h"] < 100.0) | (df["AROONU_14_4h"] < 100.0))
      # 15m down move, 15m high, 1d overbought
      & ((df["RSI_3_15m"] > 15.0) | (df["AROONU_14_15m"] < 70.0) | (df["ROC_9_1d"] < 50.0))
      # 15m & 1h down move, 1h high
      & ((df["RSI_3_15m"] > 20.0) | (df["RSI_3_1h"] > 20.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 60.0))
      # 15m & 4h down move, 15m high
      & ((df["RSI_3_15m"] > 20.0) | (df["RSI_3_4h"] > 20.0) | (df["AROONU_14_15m"] < 70.0))
      # 15m & 4h down move, 15m still high
      & ((df["RSI_3_15m"] > 20.0) | (df["RSI_3_4h"] > 20.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 50.0))
      # 15m down move, 15m & 1h high
      & ((df["RSI_3_15m"] > 20.0) | (df["AROONU_14_15m"] < 70.0) | (df["AROONU_14_1h"] < 100.0))
      # 15m down move, 15m high, 1d high
      & ((df["RSI_3_15m"] > 20.0) | (df["AROONU_14_15m"] < 90.0) | (df["AROONU_14_1d"] < 100.0))
      # 15m down move, 1h high, 1d downtrend
      & ((df["RSI_3_15m"] > 20.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 80.0) | (df["ROC_9_1d"] > -20.0))
      # 15m down move, 1h high & overbought
      & ((df["RSI_3_15m"] > 20.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 90.0) | (df["ROC_9_1h"] < 10.0))
      # 15m & 4h down mve, 1h high
      & ((df["RSI_3_15m"] > 30.0) | (df["RSI_3_4h"] > 30.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 80.0))
      # 15m & 4h down move, 4h high
      & ((df["RSI_3_15m"] > 30.0) | (df["RSI_3_4h"] > 45.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 80.0))
      # 15m down move, 1h high, 1d downtrend
      & ((df["RSI_3_15m"] > 30.0) | (df["AROONU_14_1h"] < 90.0) | (df["ROC_9_1d"] > -10.0))
      # 15m down move, 15m high, 4h high
      & ((df["RSI_3_15m"] > 35.0) | (df["AROONU_14_15m"] < 70.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 80.0))
      # 15m down move, 15m & 4h high
      & ((df["RSI_3_15m"] > 35.0) | (df["AROONU_14_15m"] < 70.0) | (df["AROONU_14_4h"] < 90.0))
      # 15m down move, 15m high, 1d overbought
      & ((df["RSI_3_15m"] > 35.0) | (df["AROONU_14_15m"] < 80.0) | (df["ROC_9_1d"] < 50.0))
      # 15m down move, 1d high, 1h overbought
      & ((df["RSI_3_15m"] > 40.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 80.0) | (df["ROC_9_1h"] < 20.0))
      # 1h & 4h down move, 1d still high
      & ((df["RSI_3_1h"] > 3.0) | (df["RSI_3_4h"] > 10.0) | (df["AROONU_14_1d"] < 50.0))
      # 1h & 4h down move, 1d overbought
      & ((df["RSI_3_1h"] > 3.0) | (df["RSI_3_4h"] > 25.0) | (df["ROC_9_1d"] < 10.0))
      # 1h & 4h down move, 1d still high
      & ((df["RSI_3_1h"] > 5.0) | (df["RSI_3_4h"] > 15.0) | (df["AROONU_14_1d"] < 40.0))
      # 1h & 4h & 1d down move
      & ((df["RSI_3_1h"] > 5.0) | (df["RSI_3_4h"] > 20.0) | (df["RSI_3_1d"] > 25.0))
      # 1h & 4h down move, 15m high
      & ((df["RSI_3_1h"] > 5.0) | (df["RSI_3_4h"] > 25.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 60.0))
      # 1h & 4h & 1d down move
      & ((df["RSI_3_1h"] > 10.0) | (df["RSI_3_4h"] > 10.0) | (df["RSI_3_1d"] > 15.0))
      # 1h & 4h down move, 1d still not low enough
      & ((df["RSI_3_1h"] > 10.0) | (df["RSI_3_4h"] > 10.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 20.0))
      # 1h & 4h down move, 15m still high
      & ((df["RSI_3_1h"] > 10.0) | (df["RSI_3_4h"] > 15.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 50.0))
      # 1h & 4h down move, 1h still not low enough
      & ((df["RSI_3_1h"] > 10.0) | (df["RSI_3_4h"] > 20.0) | (df["AROONU_14_1h"] < 30.0))
      # 1h & 4h down move, 1d overbought
      & ((df["RSI_3_1h"] > 10.0) | (df["RSI_3_4h"] > 20.0) | (df["ROC_9_1d"] < 100.0))
      # 1h & 1d downtrend, 1d high
      & ((df["RSI_3_1h"] > 10.0) | (df["RSI_3_1d"] > 45.0) | (df["AROONU_14_1d"] < 70.0))
      # 1h & 4h down move, 1h still not low enough
      & ((df["RSI_3_1h"] > 15.0) | (df["RSI_3_4h"] > 15.0) | (df["AROONU_14_1h"] < 20.0))
      # 1h & 4h down move. 4h high
      & ((df["RSI_3_1h"] > 15.0) | (df["RSI_3_4h"] > 15.0) | (df["AROONU_14_4h"] < 60.0))
      # 1h & 4h down move, 1d still high
      & ((df["RSI_3_1h"] > 15.0) | (df["RSI_3_4h"] > 15.0) | (df["AROONU_14_1d"] < 50.0))
      # 1h & 4h down move, 1h still not low enough
      & ((df["RSI_3_1h"] > 15.0) | (df["RSI_3_4h"] > 15.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 30.0))
      # 1h & 4h down move, 15m still not low enough
      & ((df["RSI_3_1h"] > 15.0) | (df["RSI_3_4h"] > 15.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 30.0))
      # 1h & 4h down move, 4h still high
      & ((df["RSI_3_1h"] > 15.0) | (df["RSI_3_4h"] > 20.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 40.0))
      # 1h & 1d down move, 1d still high
      & ((df["RSI_3_1h"] > 15.0) | (df["RSI_3_1d"] > 20.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 40.0))
      # 1h & 1d down move, 1d high
      & ((df["RSI_3_1h"] > 15.0) | (df["RSI_3_1d"] > 35.0) | (df["AROONU_14_1d"] < 70.0))
      # 1h down move, 15m & 1d high
      & ((df["RSI_3_1h"] > 15.0) | (df["AROONU_14_15m"] < 70.0) | (df["AROONU_14_1d"] < 100.0))
      # 1h down move, 1h still high, 4h overbought
      & ((df["RSI_3_1h"] > 15.0) | (df["AROONU_14_1h"] < 50.0) | (df["ROC_9_4h"] < 10.0))
      # 1h down move, 1h still high, 1d downtrend
      & ((df["RSI_3_1h"] > 15.0) | (df["AROONU_14_1h"] < 50.0) | (df["ROC_9_1d"] > -30.0))
      # 1h down move, 4h & 1d overbought
      & ((df["RSI_3_1h"] > 15.0) | (df["ROC_9_4h"] < 30.0) | (df["ROC_9_1d"] < 50.0))
      # 1h & 4h down move, 1h still high
      & ((df["RSI_3_1h"] > 20.0) | (df["RSI_3_4h"] > 20.0) | (df["AROONU_14_1h"] < 50.0))
      # 1h & 4h down move, 1d high
      & ((df["RSI_3_1h"] > 20.0) | (df["RSI_3_4h"] > 25.0) | (df["AROONU_14_1d"] < 80.0))
      # 1h & 4h down move, 1d overbought
      & ((df["RSI_3_1h"] > 20.0) | (df["RSI_3_4h"] > 30.0) | (df["ROC_9_1d"] < 100.0))
      # 1h & 4h down move, 1h high
      & ((df["RSI_3_1h"] > 20.0) | (df["RSI_3_4h"] > 35.0) | (df["AROONU_14_1h"] < 70.0))
      # 1h & 4h down move, 4h high
      & ((df["RSI_3_1h"] > 20.0) | (df["RSI_3_4h"] > 50.0) | (df["AROONU_14_4h"] < 100.0))
      # 1h & 4h down move, 15m high
      & ((df["RSI_3_1h"] > 25.0) | (df["RSI_3_4h"] > 25.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 70.0))
      # 1h & 4h down move, 4h high
      & ((df["RSI_3_1h"] > 25.0) | (df["RSI_3_4h"] > 30.0) | (df["AROONU_14_4h"] < 60.0))
      # 1h down move, 4h & 1d overbought
      & ((df["RSI_3_1h"] > 25.0) | (df["ROC_9_4h"] < 30.0) | (df["ROC_9_1d"] < 60.0))
      # 1h & 4h down move, 1h high
      & ((df["RSI_3_1h"] > 30.0) | (df["RSI_3_4h"] > 30.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 60.0))
      # 1h & 4g down move, 4h still high
      & ((df["RSI_3_1h"] > 30.0) | (df["RSI_3_4h"] > 30.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 50.0))
      # 1h down move, 15m still high, 1h high
      & ((df["RSI_3_1h"] > 30.0) | (df["AROONU_14_15m"] < 50.0) | (df["AROONU_14_1h"] < 85.0))
      # 1h down move, 4h high, 1d overbought
      & ((df["RSI_3_1h"] > 35.0) | (df["AROONU_14_4h"] < 70.0) | (df["ROC_9_1d"] < 100.0))
      # 1h down move, 4h & 1d high
      & ((df["RSI_3_1h"] > 35.0) | (df["AROONU_14_4h"] < 100.0) | (df["AROONU_14_1d"] < 100.0))
      # 1h down move, 1h still high, 1d downtrend
      & ((df["RSI_3_1h"] > 35.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 50.0) | (df["ROC_9_1d"] > -30.0))
      # 1h & 1d down move, 1h high
      & ((df["RSI_3_1h"] > 45.0) | (df["RSI_3_1d"] > 45.0) | (df["AROONU_14_1h"] < 80.0))
      # 1h down move, 1h & 4h high
      & ((df["RSI_3_1h"] > 45.0) | (df["AROONU_14_1h"] < 80.0) | (df["AROONU_14_4h"] < 100.0))
      # 1h down move, 4h high & overbought
      & ((df["RSI_3_1h"] > 50.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 90.0) | (df["ROC_9_4h"] < 25.0))
      # 4h & 1d down move, 1d downtrend
      & ((df["RSI_3_4h"] > 3.0) | (df["RSI_3_1d"] > 10.0) | (df["ROC_9_1d"] > -20.0))
      # 4h & 1d down move, 1d still high
      & ((df["RSI_3_4h"] > 3.0) | (df["RSI_3_1d"] > 20.0) | (df["RSI_14_1d"] < 40.0))
      # 4h & 1d down move, 1d high
      & ((df["RSI_3_4h"] > 5.0) | (df["RSI_3_1d"] > 45.0) | (df["AROONU_14_1d"] < 70.0))
      # 4h down move, 4h still high, 4h downtrend
      & ((df["RSI_3_4h"] > 5.0) | (df["AROONU_14_4h"] < 40.0) | (df["ROC_9_4h"] > -10.0))
      # 4h down move, 1h high
      & ((df["RSI_3_4h"] > 5.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 90.0))
      # 4h & 1d down move, 1h still high
      & ((df["RSI_3_4h"] > 10.0) | (df["RSI_3_1d"] > 10.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 50.0))
      # 4h & 1d down move, 1h high
      & ((df["RSI_3_4h"] > 10.0) | (df["RSI_3_1d"] > 15.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 70.0))
      # 4h down move, 15m still high, 1h still high
      & ((df["RSI_3_4h"] > 10.0) | (df["AROONU_14_15m"] < 40.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 50.0))
      # 4h down move, 1d still high, 1d downtrend
      & ((df["RSI_3_4h"] > 10.0) | (df["AROONU_14_1d"] < 50.0) | (df["ROC_9_1d"] > -30.0))
      # 4h down move, 15m high
      & ((df["RSI_3_4h"] > 10.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 80.0))
      # 4h down move, 15m still high, 1d downtrend
      & ((df["RSI_3_4h"] > 10.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 50.0) | (df["ROC_9_1d"] > -30.0))
      # 4h down move, 1h still high, 1d downtrend
      & ((df["RSI_3_4h"] > 10.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 50.0) | (df["ROC_9_1d"] > -30.0))
      # 4h down move, 1h high, 4h downtrend
      & ((df["RSI_3_4h"] > 10.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 70.0) | (df["ROC_9_4h"] > -20.0))
      # 4h down move, 4h & 1d downtrend
      & ((df["RSI_3_4h"] > 10.0) | (df["ROC_9_4h"] > -15.0) | (df["ROC_9_1d"] > -20.0))
      # 4h & 1d down move, 4h still high
      & ((df["RSI_3_4h"] > 15.0) | (df["RSI_3_1d"] > 20.0) | (df["AROONU_14_4h"] < 40.0))
      # 4h & 1d down move, 4h high
      & ((df["RSI_3_4h"] > 15.0) | (df["RSI_3_1d"] > 25.0) | (df["AROONU_14_4h"] < 70.0))
      # 4h & 1d down move, 15m high
      & ((df["RSI_3_4h"] > 15.0) | (df["RSI_3_1d"] > 30.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 80.0))
      # 4h & 1d down move, 4h still high
      & ((df["RSI_3_4h"] > 15.0) | (df["RSI_3_1d"] > 50.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 40.0))
      # 4h down move, 15m still not low enough, 1d high
      & ((df["RSI_3_4h"] > 15.0) | (df["AROONU_14_15m"] < 30.0) | (df["AROONU_14_1d"] < 70.0))
      # 4h down move, 4h still high, 4h downtrend
      & ((df["RSI_3_4h"] > 15.0) | (df["AROONU_14_4h"] < 50.0) | (df["ROC_9_4h"] > -10.0))
      # 4h down move, 4h still not low enough, 1d downtrend
      & ((df["RSI_3_4h"] > 15.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 20.0) | (df["ROC_9_1d"] > -20.0))
      # 4h down move, 4h & 1d high
      & ((df["RSI_3_4h"] > 20.0) | (df["AROONU_14_4h"] < 70.0) | (df["AROONU_14_1d"] < 70.0))
      # 4h down move, 4h high
      & ((df["RSI_3_4h"] > 20.0) | (df["AROONU_14_4h"] < 80.0))
      # 4h down move, 1d high & overbought
      & ((df["RSI_3_4h"] > 20.0) | (df["AROONU_14_1d"] < 80.0) | (df["ROC_9_1d"] < 70.0))
      # 4h down move, 4h still high, 4h downtrend
      & ((df["RSI_3_4h"] > 20.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 50.0) | (df["ROC_9_4h"] > -20.0))
      # 4h down move, 4h high, 1d downtrend
      & ((df["RSI_3_4h"] > 20.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 70.0) | (df["ROC_9_1d"] > -20.0))
      # 4h & 1d down move, 4h overbought
      & ((df["RSI_3_4h"] > 25.0) | (df["RSI_3_1d"] > 45.0) | (df["ROC_9_4h"] < 5.0))
      # 4h & 1d down move, 1d overbought
      & ((df["RSI_3_4h"] > 25.0) | (df["RSI_3_1d"] > 45.0) | (df["ROC_9_1d"] < 10.0))
      # 4h down move, 15m still not low enough, 4h still high
      & ((df["RSI_3_4h"] > 25.0) | (df["AROONU_14_15m"] < 30.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 40.0))
      # 4h down move, 1d high, 4h overbought
      & ((df["RSI_3_4h"] > 25.0) | (df["AROONU_14_1d"] < 80.0) | (df["ROC_9_4h"] < 5.0))
      # 4h & 1d down move, 4h still high
      & ((df["RSI_3_4h"] > 30.0) | (df["RSI_3_1d"] > 30.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 50.0))
      # 4h & 1d down move, 1d high
      & ((df["RSI_3_4h"] > 30.0) | (df["RSI_3_1d"] > 60.0) | (df["AROONU_14_1d"] < 90.0))
      # 4h down move, 4h high, 1d high
      & ((df["RSI_3_4h"] > 30.0) | (df["AROONU_14_4h"] < 70.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 80.0))
      # 4h down move, 1d stil high, 1d downtrend
      & ((df["RSI_3_4h"] > 30.0) | (df["AROONU_14_1d"] < 40.0) | (df["ROC_9_1d"] > -30.0))
      # 4h down move, 1h high, 1d downtrend
      & ((df["RSI_3_4h"] > 30.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 80.0) | (df["ROC_9_1d"] > -40.0))
      # 4h down move, 15m still high, 1h high
      & ((df["RSI_3_4h"] > 35.0) | (df["AROONU_14_15m"] < 50.0) | (df["AROONU_14_1h"] < 100.0))
      # 4h down move, 4h still high, 1d downtrend
      & ((df["RSI_3_4h"] > 35.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 40.0) | (df["ROC_9_1d"] > -30.0))
      # 4h down move, 1d high & overbought
      & ((df["RSI_3_4h"] > 35.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 80.0) | (df["ROC_9_1d"] < 20.0))
      # 4h down move, 1d high & overbought
      & ((df["RSI_3_4h"] > 45.0) | (df["AROONU_14_1d"] < 70.0) | (df["ROC_9_1d"] < 20.0))
      # 4h down move, 4h high, 1d downtrend
      & ((df["RSI_3_4h"] > 45.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 40.0) | (df["ROC_9_1d"] > -25.0))
      # 4h down move, 1d high & overbought
      & ((df["RSI_3_4h"] > 50.0) | (df["AROONU_14_1d"] < 85.0) | (df["ROC_9_1d"] < 200.0))
      # 4h down move, 4h high & overbought
      & ((df["RSI_3_4h"] > 50.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 70.0) | (df["ROC_9_4h"] < 10.0))
      # 4h down move, 4h still high, 1d downtrend
      & ((df["RSI_3_4h"] > 50.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 50.0) | (df["ROC_9_1d"] > -40.0))
      # 4h down move, 4h & 1d overbought
      & ((df["RSI_3_4h"] > 50.0) | (df["ROC_9_4h"] < 10.0) | (df["ROC_9_1d"] < 50.0))
      # 4h down move, 1d high & overbought
      & ((df["RSI_3_4h"] > 55.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 90.0) | (df["ROC_9_1d"] < 100.0))
      # 1d down move, 1d high, 4h downtrend
      & ((df["RSI_3_1d"] > 15.0) | (df["AROONU_14_1d"] < 70.0) | (df["ROC_9_4h"] > -40.0))
      # 1d down move, 1d high, 1d downtrend
      & ((df["RSI_3_1d"] > 15.0) | (df["AROONU_14_1d"] < 70.0) | (df["ROC_9_1d"] > -20.0))
      # 1d down move, 1h & 4h high
      & ((df["RSI_3_1d"] > 30.0) | (df["AROONU_14_1h"] < 70.0) | (df["AROONU_14_4h"] < 100.0))
      # 15m & 1h high, 4h overbought
      & ((df["AROONU_14_15m"] < 70.0) | (df["AROONU_14_1h"] < 100.0) | (df["ROC_9_4h"] < 15.0))
      # 15m & 1h high, 1d overbought
      & ((df["AROONU_14_15m"] < 70.0) | (df["AROONU_14_1h"] < 100.0) | (df["ROC_9_1d"] < 100.0))
      # 15m & 1h high, 1d downtrend
      & ((df["AROONU_14_15m"] < 70.0) | (df["AROONU_14_1h"] < 100.0) | (df["ROC_9_1d"] > -10.0))
      # 15m & 4h & 1d high
      & ((df["AROONU_14_15m"] < 70.0) | (df["AROONU_14_4h"] < 90.0) | (df["AROONU_14_1d"] < 100.0))
      # 15m high, 1d high & overbought
      & ((df["AROONU_14_15m"] < 70.0) | (df["AROONU_14_1d"] < 100.0) | (df["ROC_9_1d"] < 20.0))
      # 15m high, 1h & 4h overbought
      & ((df["AROONU_14_15m"] < 70.0) | (df["ROC_9_1h"] < 10.0) | (df["ROC_9_4h"] < 10.0))
      # 15m high, 4h overbought, 1d downtrend
      & ((df["AROONU_14_15m"] < 80.0) | (df["ROC_9_4h"] < 20.0) | (df["ROC_9_1d"] > -30.0))
      # 15m & 1h high
      & ((df["AROONU_14_15m"] < 90.0) | (df["AROONU_14_1h"] < 100.0))
      # 15m & 4h high
      & ((df["AROONU_14_15m"] < 90.0) | (df["AROONU_14_4h"] < 100.0))
      # 1h & 1d high, 1d overbought
      & ((df["AROONU_14_1h"] < 100.0) | (df["AROONU_14_1d"] < 100.0) | (df["ROC_9_1d"] < 10.0))
      # 1h & 4h high, 1h overbought
      & ((df["AROONU_14_1h"] < 100.0) | (df["AROONU_14_4h"] < 100.0) | (df["ROC_9_1h"] < 10.0))
      # 1h & 4h high, 4h overbought
      & ((df["AROONU_14_1h"] < 100.0) | (df["AROONU_14_4h"] < 100.0) | (df["ROC_9_4h"] < 10.0))
      # 4h & 1d high, 4h overbought
      & ((df["AROONU_14_4h"] < 100.0) | (df["AROONU_14_1d"] < 100.0) | (df["ROC_9_4h"] < 40.0))
      # 4h & 1d high, 1d overbought
      & ((df["AROONU_14_4h"] < 100.0) | (df["AROONU_14_1d"] < 100.0) | (df["ROC_9_1d"] < 60.0))
      # 4h high, 1h & 4h overbought
      & ((df["AROONU_14_4h"] < 100.0) | (df["ROC_9_1h"] < 20.0) | (df["ROC_9_4h"] < 40.0))
      # 1d high, 4h & 1d downtrend
      & ((df["AROONU_14_1d"] < 60.0) | (df["ROC_9_4h"] > -20.0) | (df["ROC_9_1d"] > -30.0))
      # 1d high, 4h & 1d overbought
      & ((df["AROONU_14_1d"] < 100.0) | (df["ROC_9_4h"] < 60.0) | (df["ROC_9_1d"] < 100.0))
      # 15m high, 4h & 1d overbought
      & ((df["STOCHRSIk_14_14_3_3_15m"] < 70.0) | (df["ROC_9_4h"] < 20.0) | (df["ROC_9_1d"] < 20.0))
      # 1h high, 1h & 1d overbought
      & ((df["STOCHRSIk_14_14_3_3_1h"] < 80.0) | (df["ROC_9_1h"] < 20.0) | (df["ROC_9_1d"] < 100.0))
      # 4h high, 4h overbought, 1d downtrend
      & ((df["STOCHRSIk_14_14_3_3_4h"] < 90.0) | (df["ROC_9_4h"] < 20.0) | (df["ROC_9_1d"] > -20.0))
      # 1d high, 1h & 4h overbought
      & ((df["STOCHRSIk_14_14_3_3_1d"] < 80.0) | (df["ROC_9_1h"] < 20.0) | (df["ROC_9_4h"] < 20.0))
    )

    # Logic
    long_entry_logic.append(
      (df["RSI_3"] > 5.0)
      & (df["RSI_4"] < 46.0)
      # & (df["STOCHRSIk_14_14_3_3"] < 20.0)
      & (df["RSI_20"] < df["RSI_20"].shift(1))
      & (df["close"] < df["SMA_16"] * 0.960)
    )


def append_long_143(df, long_entry_logic, allowed_empty_candles_288, is_pair_long_top_coins_mode) -> None:
    """Append NFI long condition #143, a top-coins long entry."""
    long_entry_logic.append(is_pair_long_top_coins_mode)
    long_entry_logic.append(df["num_empty_288"] <= allowed_empty_candles_288)
    long_entry_logic.append(df["protections_long_global"] == True)

    long_entry_logic.append(
      # 5m & 4h & 1d down move
      ((df["RSI_3"] > 3.0) | (df["RSI_3_4h"] > 10.0) | (df["RSI_3_1d"] > 10.0))
      # 5m & 4h down move, 4h still high
      & ((df["RSI_3"] > 3.0) | (df["RSI_3_4h"] > 10.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 50.0))
      # 15m & 1h down move, 1h still not low enough
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_1h"] > 3.0) | (df["AROONU_14_1h"] < 25.0))
      # 15m & 1h & 4h down move
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_1h"] > 5.0) | (df["RSI_3_4h"] > 10.0))
      # 15m & 1h down move, 15m still high
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_1h"] > 15.0) | (df["AROONU_14_15m"] < 40.0))
      # 15m & 1h down move, 4h still high
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_1h"] > 15.0) | (df["AROONU_14_4h"] < 40.0))
      # 15m & 1h down move, 1h still high
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_1h"] > 15.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 50.0))
      # 15m & 1h down move, 4h high
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_1h"] > 15.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 90.0))
      # 15m & 1h down move, 15m high
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_1h"] > 30.0) | (df["AROONU_14_15m"] < 70.0))
      # 15m & 1h down move, 1d downtrend
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_1h"] > 35.0) | (df["ROC_9_1d"] > -30.0))
      # 15m & 1h down move, 4h high
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_1h"] > 40.0) | (df["AROONU_14_1h"] < 85.0))
      # 15m & 4h down move, 4h still high
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_4h"] > 15.0) | (df["AROONU_14_4h"] < 50.0))
      # 15m & 4h down move, 15m still high
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_4h"] > 20.0) | (df["AROONU_14_15m"] < 50.0))
      # 15m & 1d down move, 4h still high
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_1d"] > 20.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 50.0))
      # 15m & 4h down move, 1d still high
      & ((df["RSI_3_15m"] > 5.0) | (df["RSI_3_4h"] > 5.0) | (df["RSI_14_1d"] < 40.0))
      # 15m & 1h down move, 4h still high
      & ((df["RSI_3_15m"] > 5.0) | (df["RSI_3_1h"] > 10.0) | (df["RSI_14_4h"] < 40.0))
      # 15m & 1h down move, 1d high
      & ((df["RSI_3_15m"] > 5.0) | (df["RSI_3_1h"] > 15.0) | (df["AROONU_14_1d"] < 100.0))
      # 15m & 4h down move, 15m still not low enough
      & ((df["RSI_3_15m"] > 5.0) | (df["RSI_3_4h"] > 10.0) | (df["AROONU_14_15m"] < 30.0))
      # 15m & 4h down move, 4h high
      & ((df["RSI_3_15m"] > 5.0) | (df["RSI_3_4h"] > 10.0) | (df["AROONU_14_4h"] < 80.0))
      # 15m & 4h down move, 1h still high
      & ((df["RSI_3_15m"] > 5.0) | (df["RSI_3_4h"] > 10.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 40.0))
      # 15m & 4h down move, 1d downtrend
      & ((df["RSI_3_15m"] > 5.0) | (df["RSI_3_4h"] > 10.0) | (df["ROC_9_1d"] > -20.0))
      # 15m & 1d down move, 1h still high
      & ((df["RSI_3_15m"] > 5.0) | (df["RSI_3_1d"] > 10.0) | (df["AROONU_14_1h"] < 50.0))
      # 15m & 1d down move, 1h still high
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_1d"] > 25.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 50.0))
      # 15m down move, 1h high, 4h overbought
      & ((df["RSI_3_15m"] > 3.0) | (df["AROONU_14_1h"] < 70.0) | (df["ROC_9_4h"] < 10.0))
      # 15m down move, 4h high, 1d downtrend
      & ((df["RSI_3_15m"] > 3.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 70.0) | (df["ROC_9_1d"] > -20.0))
      # 15m down move, 15m still high, 1d downtrend
      & ((df["RSI_3_15m"] > 5.0) | (df["AROONU_14_15m"] < 50.0) | (df["ROC_9_1d"] > -20.0))
      # 15m down move, 1h high, 1d overbought
      & ((df["RSI_3_15m"] > 5.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 50.0) | (df["ROC_9_1d"] < 40.0))
      # 15m & 1h down move, 1h high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1h"] > 10.0) | (df["AROONU_14_1h"] < 60.0))
      # 15m & 1h down move, 4h high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1h"] > 10.0) | (df["AROONU_14_4h"] < 60.0))
      # 15m & 1h down move, 1h high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1h"] > 20.0) | (df["AROONU_14_1h"] < 80.0))
      # 15m & 1h down move, 1h high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1h"] > 25.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 70.0))
      # 15m & 1h down move, 1h high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1h"] > 30.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 70.0))
      # 15m & 4h down move, 1h still high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_4h"] > 10.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 50.0))
      # 15m & 4h down move, 1h high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_4h"] > 20.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 70.0))
      # 15m & 4h down move, 4h overbought
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_4h"] > 35.0) | (df["ROC_9_4h"] < 10.0))
      # 15m & 1d down move, 1h high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1d"] > 10.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 70.0))
      # 15m & 1d down move, 4h still high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1d"] > 10.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 40.0))
      # 15m & 4h down move, 15m high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_4h"] > 40.0) | (df["AROONU_14_15m"] < 70.0))
      # 15m down move, 15m high, 1d high
      & ((df["RSI_3_15m"] > 10.0) | (df["AROONU_14_15m"] < 60.0) | (df["AROONU_14_1d"] < 100.0))
      # 15m down move, 1h & 1d high
      & ((df["RSI_3_15m"] > 10.0) | (df["AROONU_14_1h"] < 90.0) | (df["AROONU_14_1d"] < 100.0))
      # 15m down move, 4h high, 1d overbought
      & ((df["RSI_3_15m"] > 10.0) | (df["AROONU_14_4h"] < 70.0) | (df["ROC_9_1d"] < 100.0))
      # 15m down move, 1h still high, 1d downtrend
      & ((df["RSI_3_15m"] > 10.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 50.0) | (df["ROC_9_1d"] > -20.0))
      # 15m & 4h down move, 1h high
      & ((df["RSI_3_15m"] > 15.0) | (df["RSI_3_4h"] > 35.0) | (df["AROONU_14_1h"] < 90.0))
      # 1h & 1d down move, 1d still high
      & ((df["RSI_3_1h"] > 3.0) | (df["RSI_3_1d"] > 25.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 40.0))
      # 1h & 4h down move, 1d downtrend
      & ((df["RSI_3_1h"] > 5.0) | (df["RSI_3_4h"] > 5.0) | (df["ROC_9_1d"] > -30.0))
      # 1h & 4h down move, 1d still high
      & ((df["RSI_3_1h"] > 5.0) | (df["RSI_3_4h"] > 10.0) | (df["AROONU_14_1d"] < 50.0))
      # 1h & 4h & 1d down move
      & ((df["RSI_3_1h"] > 5.0) | (df["RSI_3_4h"] > 10.0) | (df["RSI_3_1d"] > 20.0))
      # 1h & 4h down move, 4h still not low enough
      & ((df["RSI_3_1h"] > 5.0) | (df["RSI_3_4h"] > 15.0) | (df["AROONU_14_4h"] < 30.0))
      # 1h down move, 4h & 1d downtrend
      & ((df["RSI_3_1h"] > 5.0) | (df["ROC_9_4h"] > -10.0) | (df["ROC_9_1d"] > -20.0))
      # 1h & 4h down move, 1d still not low enough
      & ((df["RSI_3_1h"] > 10.0) | (df["RSI_3_4h"] > 10.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 20.0))
      # 1h & 4h down move, 15m still not low enough
      & ((df["RSI_3_1h"] > 15.0) | (df["RSI_3_4h"] > 3.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 30.0))
      # 1h & 4h down move, 4h high
      & ((df["RSI_3_1h"] > 15.0) | (df["RSI_3_4h"] > 15.0) | (df["AROONU_14_4h"] < 60.0))
      # 1h down move, 1h still not low enough, 1d overbought
      & ((df["RSI_3_1h"] > 15.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 30.0) | (df["ROC_9_1d"] < 50.0))
      # 1h down move, 1h still high, 1d downtrend
      & ((df["RSI_3_1h"] > 15.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 40.0) | (df["ROC_9_1d"] > -20.0))
      # 1h down move, 1d high & overbought
      & ((df["RSI_3_1h"] > 15.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 90.0) | (df["ROC_9_1d"] < 40.0))
      # 1h & 4h down move, 1h high
      & ((df["RSI_3_1h"] > 20.0) | (df["RSI_3_4h"] > 20.0) | (df["AROONU_14_1h"] < 70.0))
      # 1h & 4h down move, 1d high
      & ((df["RSI_3_1h"] > 20.0) | (df["RSI_3_4h"] > 25.0) | (df["AROONU_14_1d"] < 80.0))
      # 1h & 4h down move, 4h high
      & ((df["RSI_3_1h"] > 20.0) | (df["RSI_3_4h"] > 35.0) | (df["AROONU_14_4h"] < 70.0))
      # 1h & 4h down move, 4h high
      & ((df["RSI_3_1h"] > 20.0) | (df["RSI_3_4h"] > 50.0) | (df["AROONU_14_4h"] < 100.0))
      # 1h & 1d down move, 1d overbought
      & ((df["RSI_3_1h"] > 20.0) | (df["RSI_3_1d"] > 40.0) | (df["ROC_9_1d"] < 30.0))
      # 1h down move, 1h & 4h high
      & ((df["RSI_3_1h"] > 25.0) | (df["AROONU_14_1h"] < 80.0) | (df["AROONU_14_4h"] < 100.0))
      # 1h down move, 4h & 1d overbought
      & ((df["RSI_3_1h"] > 25.0) | (df["ROC_9_4h"] < 20.0) | (df["ROC_9_1d"] < 30.0))
      # 1h & 4h down move, 1h high
      & ((df["RSI_3_1h"] > 30.0) | (df["RSI_3_4h"] > 30.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 60.0))
      # 1h down move, 15m still high, 1h high
      & ((df["RSI_3_1h"] > 30.0) | (df["AROONU_14_15m"] < 50.0) | (df["AROONU_14_1h"] < 85.0))
      # 1h & 1d down move, 1h high
      & ((df["RSI_3_1h"] > 45.0) | (df["RSI_3_1d"] > 45.0) | (df["AROONU_14_1h"] < 80.0))
      # 4h & 1d down move, 15m still not low enough
      & ((df["RSI_3_4h"] > 3.0) | (df["RSI_3_1d"] > 15.0) | (df["AROONU_14_15m"] < 20.0))
      # 4h & 1d down move, 1d high
      & ((df["RSI_3_4h"] > 3.0) | (df["RSI_3_1d"] > 25.0) | (df["AROONU_14_1d"] < 70.0))
      # 4h & 1d down move, 1d downtrend
      & ((df["RSI_3_4h"] > 5.0) | (df["RSI_3_1d"] > 5.0) | (df["ROC_9_1d"] > -30.0))
      # 4h & 1d down move, 1h still high
      & ((df["RSI_3_4h"] > 5.0) | (df["RSI_3_1d"] > 10.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 50.0))
      # 4h down move, 4h still high, 1d downtrend
      & ((df["RSI_3_4h"] > 5.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 40.0) | (df["ROC_9_1d"] > -20.0))
      # 4h & 1d down move, 1d high
      & ((df["RSI_3_4h"] > 10.0) | (df["RSI_3_1d"] > 15.0) | (df["AROONU_14_1d"] < 70.0))
      # 4h & 1d down move, 15m still high
      & ((df["RSI_3_4h"] > 10.0) | (df["RSI_3_1d"] > 20.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 40.0))
      # 4h down move, 1d high & overbought
      & ((df["RSI_3_4h"] > 10.0) | (df["AROONU_14_1d"] < 100.0) | (df["ROC_9_1d"] < 10.0))
      # 4h down move, 1h high, 1d downtrend
      & ((df["RSI_3_4h"] > 10.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 50.0) | (df["ROC_9_1d"] > -30.0))
      # 4h down move, 4h & 1d downtrend
      & ((df["RSI_3_4h"] > 10.0) | (df["ROC_9_4h"] > -20.0) | (df["ROC_9_1d"] > -40.0))
      # 4h & 1d down move, 1d high
      & ((df["RSI_3_4h"] > 15.0) | (df["RSI_3_1d"] > 20.0) | (df["AROONU_14_1d"] < 60.0))
      # 4h & 1d down move, 4h high
      & ((df["RSI_3_4h"] > 15.0) | (df["RSI_3_1d"] > 30.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 60.0))
      # 1h down move, 1h still high, 1d downtrend
      & ((df["RSI_3_1h"] > 15.0) | (df["AROONU_14_1h"] < 50.0) | (df["ROC_9_1d"] > -30.0))
      # 4h down move, 4h & 1d high
      & ((df["RSI_3_4h"] > 15.0) | (df["AROONU_14_4h"] < 70.0) | (df["AROONU_14_1d"] < 70.0))
      # 4h down move, 1h still not low enough, 1d downtrend
      & ((df["RSI_3_4h"] > 15.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 20.0) | (df["ROC_9_1d"] > -20.0))
      # 4h down move, 1h high
      & ((df["RSI_3_4h"] > 15.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 80.0))
      # 4h down move, 1h downtrend, 1d overbought
      & ((df["RSI_3_4h"] > 15.0) | (df["ROC_9_1h"] > -10.0) | (df["ROC_9_1d"] < 200.0))
      # 4h & 1d down move, 1d still high
      & ((df["RSI_3_4h"] > 20.0) | (df["RSI_3_1d"] > 20.0) | (df["AROONU_14_1d"] < 50.0))
      # 4h down move, 4h & 1d high
      & ((df["RSI_3_4h"] > 20.0) | (df["AROONU_14_4h"] < 70.0) | (df["AROONU_14_1d"] < 70.0))
      # 4h down move, 1d high & overbought
      & ((df["RSI_3_4h"] > 20.0) | (df["AROONU_14_1d"] < 80.0) | (df["ROC_9_1d"] < 70.0))
      # 4h down move, 4h high, 1d downtrend
      & ((df["RSI_3_4h"] > 20.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 60.0) | (df["ROC_9_1d"] > -20.0))
      # 4h & 1d down move, 1d overbought
      & ((df["RSI_3_4h"] > 25.0) | (df["RSI_3_1d"] > 40.0) | (df["ROC_9_1d"] < 30.0))
      # 4h down move, 1h high, 1d downtrend
      & ((df["RSI_3_4h"] > 25.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 60.0) | (df["ROC_9_1d"] > -20.0))
      # 4h down move, 15m still high, 1h high
      & ((df["RSI_3_4h"] > 35.0) | (df["AROONU_14_15m"] < 50.0) | (df["AROONU_14_1h"] < 100.0))
      # 4h down move, 4h high, 1d downtrend
      & ((df["RSI_3_4h"] > 45.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 80.0) | (df["ROC_9_1d"] > -20.0))
      # 1h & 4h high, 1d overbought
      & ((df["AROONU_14_1h"] < 85.0) | (df["AROONU_14_4h"] < 100.0) | (df["ROC_9_1d"] < 40.0))
      # 1d high, 4h & 1d downtrend
      & ((df["AROONU_14_1d"] < 60.0) | (df["ROC_9_4h"] > -20.0) | (df["ROC_9_1d"] > -30.0))
      # 4h high, 4h & 1d overbought
      & ((df["STOCHRSIk_14_14_3_3_4h"] < 90.0) | (df["ROC_9_4h"] < 20.0) | (df["ROC_9_1d"] < 20.0))
    )

    # Logic
    long_entry_logic.append(
      (df["RSI_3"] < 40.0)
      & (df["STOCHRSIk_14_14_3_3"] < 20.0)
      & (df["EMA_26"] > df["EMA_12"])
      & ((df["EMA_26"] - df["EMA_12"]) > (df["open"] * 0.020))
      & ((df["EMA_26"].shift() - df["EMA_12"].shift()) > (df["open"] / 100.0))
    )


def append_long_144(df, long_entry_logic, allowed_empty_candles_288, is_pair_long_top_coins_mode) -> None:
    """Append NFI long condition #144, a top-coins long entry."""
    long_entry_logic.append(is_pair_long_top_coins_mode)
    long_entry_logic.append(df["num_empty_288"] <= allowed_empty_candles_288)
    long_entry_logic.append(df["protections_long_global"] == True)

    long_entry_logic.append(
      # 5m & 1h down move, 1h still not low enough
      ((df["RSI_3"] > 3.0) | (df["RSI_3_1h"] > 10.0) | (df["AROONU_14_1h"] < 30.0))
      # 5m & 4h down move, 15m still high
      & ((df["RSI_3"] > 3.0) | (df["RSI_3_4h"] > 5.0) | (df["AROONU_14_15m"] < 40.0))
      # 5m & 4h & 1d down move
      & ((df["RSI_3"] > 3.0) | (df["RSI_3_4h"] > 10.0) | (df["RSI_3_1d"] > 10.0))
      # 5m & 4h down move, 1d downtrend
      & ((df["RSI_3"] > 3.0) | (df["RSI_3_4h"] > 10.0) | (df["ROC_9_1d"] > -10.0))
      # 5m & 4h down move, 15m high
      & ((df["RSI_3"] > 10.0) | (df["RSI_3_4h"] > 10.0) | (df["AROONU_14_15m"] < 40.0))
      # 15m & 1h down move, 1h still not low enough
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_1h"] > 3.0) | (df["AROONU_14_1h"] < 25.0))
      # 15m & 1h down move, 1d high
      & ((df["RSI_3_15m"] > 5.0) | (df["RSI_3_1h"] > 5.0) | (df["AROONU_14_1d"] < 70.0))
      # 15m & 1h down move, 1d high
      & ((df["RSI_3_15m"] > 5.0) | (df["RSI_3_1h"] > 10.0) | (df["AROONU_14_1d"] < 100.0))
      # 15m & 1h down move, 1d overbought
      & ((df["RSI_3_15m"] > 5.0) | (df["RSI_3_1h"] > 30.0) | (df["ROC_9_1d"] < 30.0))
      # 15m & 4h down move, 4h downtrend
      & ((df["RSI_3_15m"] > 5.0) | (df["RSI_3_4h"] > 5.0) | (df["ROC_9_4h"] > -20.0))
      # 15m down move, 1d high & overbought
      & ((df["RSI_3_15m"] > 5.0) | (df["AROONU_14_1d"] < 100.0) | (df["ROC_9_1d"] < 40.0))
      # 15m & 4h down move, 4h still not low enough
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_4h"] > 10.0) | (df["RSI_14_4h"] < 20.0))
      # 15m & 4h down move, 4h high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_4h"] > 45.0) | (df["AROONU_14_4h"] < 70.0))
      # 15m down move, 4h high, 1d overbought
      & ((df["RSI_3_15m"] > 10.0) | (df["AROONU_14_4h"] < 80.0) | (df["ROC_9_1d"] < 50.0))
      # 15m & 1h down move, 15m still high
      & ((df["RSI_3_15m"] > 15.0) | (df["RSI_3_1h"] > 15.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 50.0))
      # 15m & 1h down move, 1d overbought
      & ((df["RSI_3_15m"] > 15.0) | (df["RSI_3_1h"] > 20.0) | (df["ROC_9_1d"] < 30.0))
      # 15m & 4h down move, 15m still high
      & ((df["RSI_3_15m"] > 15.0) | (df["RSI_3_4h"] > 15.0) | (df["AROONU_14_15m"] < 40.0))
      # 15m down move, 4h & 1d overbought
      & ((df["RSI_3_15m"] > 15.0) | (df["ROC_9_4h"] < 20.0) | (df["ROC_9_1d"] < 200.0))
      # 15m & 1h down move, 4h high
      & ((df["RSI_3_15m"] > 25.0) | (df["RSI_3_1h"] > 30.0) | (df["AROONU_14_4h"] < 100.0))
      # 15m & 1h down move, 4h high
      & ((df["RSI_3_15m"] > 25.0) | (df["RSI_3_1h"] > 40.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 90.0))
      # 15m down move, 4h high, 1d downtrend
      & ((df["RSI_3_15m"] > 25.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 80.0) | (df["ROC_9_1d"] > -30.0))
      # 15m & 1h down move, 15m high
      & ((df["RSI_3_15m"] > 45.0) | (df["RSI_3_1h"] > 45.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 70.0))
      # 15m down move, 4h high, 1d overbought
      & ((df["RSI_3_15m"] > 10.0) | (df["AROONU_14_4h"] < 70.0) | (df["ROC_9_1d"] < 100.0))
      # 15m & 4h down move, 1d downtrend
      & ((df["RSI_3_15m"] > 15.0) | (df["RSI_3_4h"] > 15.0) | (df["ROC_9_1d"] > -20.0))
      # 15m & 1h down move, 4h high
      & ((df["RSI_3_15m"] > 15.0) | (df["RSI_3_1h"] > 30.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 80.0))
      # 15m down move, 4h high & overbought
      & ((df["RSI_3_15m"] > 20.0) | (df["AROONU_14_4h"] < 100.0) | (df["ROC_9_4h"] < 30.0))
      # 15m down move, 4h high, 1d downtrend
      & ((df["RSI_3_15m"] > 25.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 90.0) | (df["ROC_9_1d"] > -30.0))
      # 15m down move, 1h & 4h overbought
      & ((df["RSI_3_15m"] > 25.0) | (df["ROC_9_1h"] < 10.0) | (df["ROC_9_4h"] < 30.0))
      # 15m down move, 1h & 4h high
      & ((df["RSI_3_15m"] > 30.0) | (df["AROONU_14_1h"] < 80.0) | (df["AROONU_14_4h"] < 100.0))
      # 15m down move, 15m & 4h high
      & ((df["RSI_3_15m"] > 35.0) | (df["AROONU_14_15m"] < 70.0) | (df["AROONU_14_4h"] < 90.0))
      # 1h & 4h down move, 1h downtrend
      & ((df["RSI_3_1h"] > 3.0) | (df["RSI_3_4h"] > 10.0) | (df["CMF_20_1h"] > -0.20))
      # 1h & 4h down move, 4h still high
      & ((df["RSI_3_1h"] > 3.0) | (df["RSI_3_4h"] > 20.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 40.0))
      # 1h & 4h down move, 15m still high
      & ((df["RSI_3_1h"] > 3.0) | (df["RSI_3_4h"] > 30.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 50.0))
      # 1h & 4h down move, 15m still not low enough
      & ((df["RSI_3_1h"] > 5.0) | (df["RSI_3_4h"] > 5.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 20.0))
      # 1h & 4h down move, 1d still high
      & ((df["RSI_3_1h"] > 5.0) | (df["RSI_3_4h"] > 20.0) | (df["AROONU_14_1d"] < 50.0))
      # 1h & 4h down move, 4h still not low enough
      & ((df["RSI_3_1h"] > 5.0) | (df["RSI_3_4h"] > 20.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 30.0))
      # 1h & 1d down move, 1h still high
      & ((df["RSI_3_1h"] > 5.0) | (df["RSI_3_1d"] > 5.0) | (df["AROONU_14_1h"] < 40.0))
      # 1h down move, 1d high & overbought
      & ((df["RSI_3_1h"] > 5.0) | (df["AROONU_14_1d"] < 90.0) | (df["ROC_9_1d"] < 20.0))
      # 1h & 4h down move, 4h still not low enough
      & ((df["RSI_3_1h"] > 10.0) | (df["RSI_3_4h"] > 15.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 30.0))
      # 1h & 4h down move, 15m still high
      & ((df["RSI_3_1h"] > 10.0) | (df["RSI_3_4h"] > 15.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 50.0))
      # 1h & 4h down move, 1d downtrend
      & ((df["RSI_3_1h"] > 10.0) | (df["RSI_3_4h"] > 15.0) | (df["ROC_9_1d"] > -20.0))
      # 1h & 4h down move, 4h still high
      & ((df["RSI_3_1h"] > 10.0) | (df["RSI_3_4h"] > 25.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 50.0))
      # 1h & 1d down move, 4h high
      & ((df["RSI_3_1h"] > 10.0) | (df["RSI_3_1d"] > 10.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 70.0))
      # 1h & 1d down move, 1d high
      & ((df["RSI_3_1h"] > 10.0) | (df["RSI_3_1d"] > 20.0) | (df["AROONU_14_1d"] < 70.0))
      # 1h down move, 1d high, 1h downtrend
      & ((df["RSI_3_1h"] > 10.0) | (df["AROONU_14_1d"] < 70.0) | (df["ROC_9_1h"] > -10.0))
      # 1h & 4h down move, 15m still not low enough
      & ((df["RSI_3_1h"] > 15.0) | (df["RSI_3_4h"] > 3.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 30.0))
      # 1h & 4h down move, 1h high
      & ((df["RSI_3_1h"] > 15.0) | (df["RSI_3_4h"] > 25.0) | (df["AROONU_14_1h"] < 70.0))
      # 1h & 4h down move, 4h high
      & ((df["RSI_3_1h"] > 15.0) | (df["RSI_3_4h"] > 30.0) | (df["AROONU_14_4h"] < 70.0))
      # 1h & 4h down move, 1d downtrend
      & ((df["RSI_3_1h"] > 15.0) | (df["RSI_3_4h"] > 30.0) | (df["ROC_9_1d"] > -40.0))
      # 1h & 1d down move, 1d high
      & ((df["RSI_3_1h"] > 15.0) | (df["RSI_3_1d"] > 25.0) | (df["AROONU_14_1d"] < 80.0))
      # 1h down move, 4h still high, 1d overbought
      & ((df["RSI_3_1h"] > 15.0) | (df["AROONU_14_4h"] < 50.0) | (df["ROC_9_1d"] < 40.0))
      # 1h down move, 1d high, 4h downtrend
      & ((df["RSI_3_1h"] > 15.0) | (df["AROONU_14_1d"] < 70.0) | (df["ROC_9_4h"] > -20.0))
      # 1h down move, 1d high & overbought
      & ((df["RSI_3_1h"] > 15.0) | (df["AROONU_14_1d"] < 80.0) | (df["ROC_9_1d"] < 10.0))
      # 1h down move, 4h high & overbought
      & ((df["RSI_3_1h"] > 15.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 80.0) | (df["ROC_9_4h"] < 20.0))
      # 1h down move, 4h high, 1d downtrend
      & ((df["RSI_3_1h"] > 15.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 80.0) | (df["ROC_9_1d"] > -30.0))
      # 1h & 4h down move, 4h still high
      & ((df["RSI_3_1h"] > 20.0) | (df["RSI_3_4h"] > 20.0) | (df["AROONU_14_4h"] < 40.0))
      # 1h & 4h down move, 1d high
      & ((df["RSI_3_1h"] > 20.0) | (df["RSI_3_4h"] > 25.0) | (df["AROONU_14_1d"] < 100.0))
      # 1h & 4h down move, 4h high
      & ((df["RSI_3_1h"] > 20.0) | (df["RSI_3_4h"] > 35.0) | (df["AROONU_14_4h"] < 80.0))
      # 1h & 4h down move, 4h overbought
      & ((df["RSI_3_1h"] > 20.0) | (df["RSI_3_4h"] > 35.0) | (df["ROC_9_4h"] < 10.0))
      # 1h & 1d down move, 1h still high
      & ((df["RSI_3_1h"] > 20.0) | (df["RSI_3_1d"] > 25.0) | (df["AROONU_14_1h"] < 50.0))
      # 1h down move, 4h high & overbought
      & ((df["RSI_3_1h"] > 20.0) | (df["AROONU_14_4h"] < 80.0) | (df["ROC_9_4h"] < 70.0))
      # 1h down move, 1h high, 1h still not low enough
      & ((df["RSI_3_1h"] > 20.0) | (df["AROONU_14_1d"] < 80.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 20.0))
      # 1h down move, 1d high & overbought
      & ((df["RSI_3_1h"] > 20.0) | (df["AROONU_14_1d"] < 100.0) | (df["ROC_9_1d"] < 20.0))
      # 1h down move, 4h still high, 1d downtrend
      & ((df["RSI_3_1h"] > 20.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 40.0) | (df["ROC_9_1d"] > -40.0))
      # 1h & 4h down move, 15m high
      & ((df["RSI_3_1h"] > 25.0) | (df["RSI_3_4h"] > 25.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 70.0))
      # 1h & 4h down move, 4h high
      & ((df["RSI_3_1h"] > 25.0) | (df["RSI_3_4h"] > 25.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 70.0))
      # 1h & 4h down move, 1d overbought
      & ((df["RSI_3_1h"] > 25.0) | (df["RSI_3_4h"] > 25.0) | (df["ROC_9_1d"] < 100.0))
      # 1h & 4h down move, 4h high
      & ((df["RSI_3_1h"] > 25.0) | (df["RSI_3_4h"] > 30.0) | (df["AROONU_14_4h"] < 60.0))
      # 1h & 1d down move, 1d high
      & ((df["RSI_3_1h"] > 25.0) | (df["RSI_3_1d"] > 25.0) | (df["AROONU_14_1d"] < 70.0))
      # 1h down move, 4h & 1d high
      & ((df["RSI_3_1h"] > 25.0) | (df["AROONU_14_4h"] < 70.0) | (df["AROONU_14_1d"] < 100.0))
      # 1h & 4h down move, 1d high
      & ((df["RSI_3_1h"] > 30.0) | (df["RSI_3_4h"] > 35.0) | (df["RSI_14_1d"] < 80.0))
      # 1h down move, 1h & 4h high
      & ((df["RSI_3_1h"] > 30.0) | (df["AROONU_14_1h"] < 70.0) | (df["AROONU_14_4h"] < 100.0))
      # 1h down move, 1h high, 4h high
      & ((df["RSI_3_1h"] > 30.0) | (df["AROONU_14_1h"] < 80.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 80.0))
      # 1h down move, 4h high, 1h overbought
      & ((df["RSI_3_1h"] > 40.0) | (df["AROONU_14_4h"] < 80.0) | (df["ROC_9_1h"] < 10.0))
      # 1h down move, 1h high, 15m high
      & ((df["RSI_3_1h"] > 50.0) | (df["AROONU_14_1h"] < 70.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 70.0))
      # 4h & 1d down move, 15m still not low enough
      & ((df["RSI_3_4h"] > 3.0) | (df["RSI_3_1d"] > 15.0) | (df["AROONU_14_15m"] < 20.0))
      # 4h & 1d down move, 1d still high
      & ((df["RSI_3_4h"] > 3.0) | (df["RSI_3_1d"] > 20.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 40.0))
      # 4h & 1d down move, 1d high
      & ((df["RSI_3_4h"] > 3.0) | (df["RSI_3_1d"] > 25.0) | (df["AROONU_14_1d"] < 70.0))
      # 4h down move, 15m high
      & ((df["RSI_3_4h"] > 3.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 60.0))
      # 4h down move, 15m still high, 4h still not low enough
      & ((df["RSI_3_4h"] > 5.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 50.0) | (df["AROONU_14_4h"] < 30.0))
      # 4h & 1d down move, 15m still high
      & ((df["RSI_3_4h"] > 10.0) | (df["RSI_3_1d"] > 15.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 40.0))
      # 4h down move, 4h still not low enough, 1d downtrend
      & ((df["RSI_3_4h"] > 10.0) | (df["AROONU_14_4h"] < 20.0) | (df["ROC_9_1d"] > -10.0))
      # 4h down move, 4h still high, 4h downtrend
      & ((df["RSI_3_4h"] > 10.0) | (df["AROONU_14_4h"] < 40.0) | (df["ROC_9_4h"] > -20.0))
      # 4h down move, 1d still high, 1d downtrend
      & ((df["RSI_3_4h"] > 10.0) | (df["AROONU_14_1d"] < 40.0) | (df["ROC_9_1d"] > -30.0))
      # 4h down move, 1d high, 4h downtrend
      & ((df["RSI_3_4h"] > 10.0) | (df["AROONU_14_1d"] < 100.0) | (df["ROC_9_4h"] > -10.0))
      # 4h down move, 4h & 1d downtrend
      & ((df["RSI_3_4h"] > 10.0) | (df["ROC_9_4h"] > -10.0) | (df["ROC_9_1d"] > -20.0))
      # 4h & 1d down move, 4h still high
      & ((df["RSI_3_4h"] > 15.0) | (df["RSI_3_1d"] > 30.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 50.0))
      # 4h & 1d down move, 4h still high
      & ((df["RSI_3_4h"] > 15.0) | (df["RSI_3_1d"] > 45.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 40.0))
      # 4h down move, 4h still not low enough, 1d high
      & ((df["RSI_3_4h"] > 15.0) | (df["AROONU_14_4h"] < 30.0) | (df["AROONU_14_1d"] < 70.0))
      # 4h down move, 1d high & overbought
      & ((df["RSI_3_4h"] > 15.0) | (df["AROONU_14_1d"] < 100.0) | (df["ROC_9_1d"] < 30.0))
      # 4h down move, 15m high
      & ((df["RSI_3_4h"] > 15.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 70.0))
      # 4h & 1d down move, 1d downtrend
      & ((df["RSI_3_4h"] > 20.0) | (df["RSI_3_1d"] > 25.0) | (df["ROC_9_1d"] > -30.0))
      # 4h down move, 1d high & overbought
      & ((df["RSI_3_4h"] > 20.0) | (df["AROONU_14_1d"] < 80.0) | (df["ROC_9_1d"] < 70.0))
      # 4h & 1d down move, 1d overbought
      & ((df["RSI_3_4h"] > 25.0) | (df["RSI_3_1d"] > 45.0) | (df["ROC_9_1d"] < 10.0))
      # 4h & 1d down move, 1d overbought
      & ((df["RSI_3_4h"] > 30.0) | (df["RSI_3_1d"] > 70.0) | (df["ROC_9_1d"] < 20.0))
      # 4h down move, 4h high, 1d high
      & ((df["RSI_3_4h"] > 30.0) | (df["AROONU_14_4h"] < 70.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 80.0))
      # 4h down move, 1d stil high, 1d downtrend
      & ((df["RSI_3_4h"] > 30.0) | (df["AROONU_14_1d"] < 40.0) | (df["ROC_9_1d"] > -30.0))
      # 4h down move, 4h still high, 4h downtrend
      & ((df["RSI_3_4h"] > 30.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 40.0) | (df["ROC_9_4h"] > -15.0))
      # 4h down move, 4h still high, 1d downtrend
      & ((df["RSI_3_4h"] > 35.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 40.0) | (df["ROC_9_1d"] > -20.0))
      # 4h down move, 1d high & overbought
      & ((df["RSI_3_4h"] > 55.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 90.0) | (df["ROC_9_1d"] < 100.0))
      # 1d down move, 4h still not low enough, 4h downtrend
      & ((df["RSI_3_1d"] > 10.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 30.0) | (df["ROC_9_4h"] > -15.0))
      # 1d down move, 4h & 1d downtrend
      & ((df["RSI_3_1d"] > 10.0) | (df["ROC_9_4h"] > -20.0) | (df["ROC_9_1d"] > -20.0))
      # 1d down move, 1d high, 4h downtrend
      & ((df["RSI_3_1d"] > 15.0) | (df["AROONU_14_1d"] < 70.0) | (df["ROC_9_4h"] > -20.0))
      # 4h & 1d down move, 4h overbought
      & ((df["RSI_3_4h"] > 25.0) | (df["RSI_3_1d"] > 45.0) | (df["ROC_9_4h"] < 5.0))
      # 1d down move, 1h & 4h high
      & ((df["RSI_3_1d"] > 25.0) | (df["AROONU_14_1h"] < 70.0) | (df["AROONU_14_4h"] < 100.0))
      # 1d down move, 1h & 4h high
      & ((df["RSI_3_1d"] > 30.0) | (df["AROONU_14_1h"] < 70.0) | (df["AROONU_14_4h"] < 100.0))
      # 4h & 1d high, 1h overbought
      & ((df["AROONU_14_4h"] < 85.0) | (df["AROONU_14_1d"] < 100.0) | (df["ROC_9_1h"] < 10.0))
      # 4h high, 4h & 1d overbought
      & ((df["AROONU_14_4h"] < 90.0) | (df["ROC_9_4h"] < 30.0) | (df["ROC_9_1d"] < 60.0))
      # 15m high, 4h & 1d overbought
      & ((df["STOCHRSIk_14_14_3_3_15m"] < 80.0) | (df["ROC_9_4h"] < 20.0) | (df["ROC_9_1d"] < 20.0))
      # 15m still high, 4h & 1d overbought
      & ((df["STOCHRSIk_14_14_3_3_15m"] < 50.0) | (df["ROC_9_4h"] < 40.0) | (df["ROC_9_1d"] < 100.0))
      # 1d high, 4h & 1d overbought
      & ((df["STOCHRSIk_14_14_3_3_1d"] < 90.0) | (df["ROC_9_4h"] < 30.0) | (df["ROC_9_1d"] < 100.0))
      # 4h & 1d overbought
      & ((df["ROC_9_4h"] < 100.0) | (df["ROC_9_1d"] < 200.0))
      # 1d P&D, 4h overbought
      & ((df["change_pct_1d"] > -10.0) | (df["change_pct_1d"].shift(288) < 50.0) | (df["ROC_9_4h"] < 30.0))
    )

    # Logic
    long_entry_logic.append(
      (df["WILLR_14"] < -50.0)
      & (df["STOCHRSIk_14_14_3_3"] < 30.0)
      # & (df["STOCHRSIk_14_14_3_3_15m"] < 40.0)
      & (df["STOCHRSIk_14_14_3_3_1h"] < 40.0)
      & (df["BBB_20_2.0_1h"] > 12.0)
      & (df["close_max_48"] >= (df["close"] * 1.10))
    )


def append_long_145(df, long_entry_logic, allowed_empty_candles_288, is_pair_long_top_coins_mode) -> None:
    """Append NFI long condition #145, a top-coins long entry."""
    long_entry_logic.append(is_pair_long_top_coins_mode)
    long_entry_logic.append(df["num_empty_288"] <= allowed_empty_candles_288)
    long_entry_logic.append(df["protections_long_global"] == True)

    long_entry_logic.append(
      # 5m & 4h down move, 1d downtrend
      ((df["RSI_3"] > 3.0) | (df["RSI_3_4h"] > 3.0) | (df["ROC_9_1d"] > -20.0))
      # 5m down move, 15m & 1h high
      & ((df["RSI_3"] > 10.0) | (df["AROONU_14_15m"] < 85.0) | (df["AROONU_14_1h"] < 100.0))
      # 15m & 1h & 4h down move
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_1h"] > 3.0) | (df["RSI_3_4h"] > 5.0))
      # 15m & 1h down move, 1h downtrend
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_1h"] > 3.0) | (df["ROC_9_1h"] > -20.0))
      # 15m & 1h down move, 1h still not low enough
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_1h"] > 10.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 20.0))
      # 15m & 1h down move, 4h high
      & ((df["RSI_3_15m"] > 5.0) | (df["RSI_3_1h"] > 10.0) | (df["AROONU_14_4h"] < 70.0))
      # 15m & 1h down move, 1h high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1h"] > 35.0) | (df["AROONU_14_1h"] < 70.0))
      # 15m & 4h down move, 4h still not low enough
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_4h"] > 10.0) | (df["AROONU_14_4h"] < 30.0))
      # 15m & 1h down move, 1h high
      & ((df["RSI_3_15m"] > 15.0) | (df["RSI_3_1h"] > 15.0) | (df["AROONU_14_1h"] < 70.0))
      # 15m & 1h down move, 1h high
      & ((df["RSI_3_15m"] > 15.0) | (df["RSI_3_1h"] > 40.0) | (df["AROONU_14_1h"] < 90.0))
      # 15m & 4h down move, 1d high
      & ((df["RSI_3_15m"] > 15.0) | (df["RSI_3_4h"] > 15.0) | (df["AROONU_14_1d"] < 90.0))
      # 15m & 4h down move, 1h high
      & ((df["RSI_3_15m"] > 15.0) | (df["RSI_3_4h"] > 35.0) | (df["AROONU_14_1h"] < 90.0))
      # 15m down move, 15m downtrend, 1h high
      & ((df["RSI_3_15m"] > 15.0) | (df["CMF_20_15m"] > -0.40) | (df["AROONU_14_1h"] < 60.0))
      # 15m down move, 15m still high, 4h high
      & ((df["RSI_3_15m"] > 15.0) | (df["AROONU_14_15m"] < 40.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 60.0))
      # 15m down move, 1h high, 1d downtrend
      & ((df["RSI_3_15m"] > 15.0) | (df["AROONU_14_1h"] < 90.0) | (df["ROC_9_1d"] > -30.0))
      # 15m & 1h down move, 1d downtrend
      & ((df["RSI_3_15m"] > 20.0) | (df["RSI_3_1h"] > 20.0) | (df["ROC_9_1d"] > -30.0))
      # 15m & 4h down move, 15m still high
      & ((df["RSI_3_15m"] > 20.0) | (df["RSI_3_4h"] > 20.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 50.0))
      # 15m down move, 15m & 1h high
      & ((df["RSI_3_15m"] > 20.0) | (df["AROONU_14_15m"] < 70.0) | (df["AROONU_14_1h"] < 100.0))
      # 15m down move, 15m still high, 1d overbought
      & ((df["RSI_3_15m"] > 25.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 50.0) | (df["ROC_9_1d"] < 30.0))
      # 15m & 4h down move, 1h high
      & ((df["RSI_3_15m"] > 30.0) | (df["RSI_3_4h"] > 30.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 70.0))
      # 15m down move, 15m & 4h high
      & ((df["RSI_3_15m"] > 30.0) | (df["AROONU_14_15m"] < 70.0) | (df["AROONU_14_4h"] < 70.0))
      # 15m down move, 15m high, 1h high
      & ((df["RSI_3_15m"] > 30.0) | (df["AROONU_14_15m"] < 70.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 70.0))
      # 15m down move, 15m high, 4h high
      & ((df["RSI_3_15m"] > 30.0) | (df["AROONU_14_15m"] < 70.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 80.0))
      # 15m down move, 1h high, 1d overbought
      & ((df["RSI_3_15m"] > 30.0) | (df["AROONU_14_1h"] < 80.0) | (df["ROC_9_1d"] < 20.0))
      # 15m down move, 4h & 1d overbought
      & ((df["RSI_3_15m"] > 35.0) | (df["ROC_9_4h"] < 30.0) | (df["ROC_9_1d"] < 80.0))
      # 1h & 4h down move, 4h still high
      & ((df["RSI_3_1h"] > 3.0) | (df["RSI_3_4h"] > 20.0) | (df["AROONU_14_4h"] < 40.0))
      # 1h down move, 4h still high, 1d high
      & ((df["RSI_3_1h"] > 3.0) | (df["AROONU_14_4h"] < 50.0) | (df["AROONU_14_1d"] < 90.0))
      # 1h & 1d down move, 1d still high
      & ((df["RSI_3_1h"] > 5.0) | (df["RSI_3_1d"] > 20.0) | (df["AROONU_14_1d"] < 40.0))
      # 1h & 4h & 1d down move
      & ((df["RSI_3_1h"] > 10.0) | (df["RSI_3_4h"] > 10.0) | (df["RSI_3_1d"] > 15.0))
      # 1h & 4h down move, 4h still high
      & ((df["RSI_3_1h"] > 10.0) | (df["RSI_3_4h"] > 10.0) | (df["AROONU_14_4h"] < 40.0))
      # 1h & 4h down move, 4h downtrend
      & ((df["RSI_3_1h"] > 10.0) | (df["RSI_3_4h"] > 10.0) | (df["ROC_9_4h"] > -10.0))
      # 1h & 4h down move, 1d downtrend
      & ((df["RSI_3_1h"] > 10.0) | (df["RSI_3_4h"] > 10.0) | (df["ROC_9_1d"] > -30.0))
      # 1h & 4h down move, 15m high
      & ((df["RSI_3_1h"] > 10.0) | (df["RSI_3_4h"] > 20.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 80.0))
      # 1h & 4h down move, 1d downtrend
      & ((df["RSI_3_1h"] > 10.0) | (df["RSI_3_4h"] > 25.0) | (df["ROC_9_1d"] > -50.0))
      # 1h & 4h down move, 4h high
      & ((df["RSI_3_1h"] > 10.0) | (df["RSI_3_4h"] > 35.0) | (df["AROONU_14_4h"] < 90.0))
      # 1h & 1d down move, 1h still not low enough
      & ((df["RSI_3_1h"] > 10.0) | (df["RSI_3_1d"] > 20.0) | (df["AROONU_14_1h"] < 30.0))
      # 1h down move, 15m downtrend, 1d high
      & ((df["RSI_3_1h"] > 10.0) | (df["CMF_20_15m"] > -0.40) | (df["AROONU_14_1d"] < 70.0))
      # 1h down move, 4h still high, 1d overbought
      & ((df["RSI_3_1h"] > 10.0) | (df["AROONU_14_4h"] < 40.0) | (df["ROC_9_1d"] < 40.0))
      # 1h down move, 1d still high, 1d downtrend
      & ((df["RSI_3_1h"] > 10.0) | (df["AROONU_14_1d"] < 50.0) | (df["ROC_9_1d"] > -20.0))
      # 1h & 4h & 1d down move
      & ((df["RSI_3_1h"] > 15.0) | (df["RSI_3_4h"] > 15.0) | (df["RSI_3_1d"] > 20.0))
      # 1h & 4h down move, 15m still not low enough
      & ((df["RSI_3_1h"] > 15.0) | (df["RSI_3_4h"] > 15.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 30.0))
      # 1h & 4h down move, 15m still high
      & ((df["RSI_3_1h"] > 15.0) | (df["RSI_3_4h"] > 15.0) | (df["AROONU_14_15m"] < 50.0))
      # 1h & 4h down move, 4h high
      & ((df["RSI_3_1h"] > 15.0) | (df["RSI_3_4h"] > 25.0) | (df["AROONU_14_4h"] < 60.0))
      # 1h & 4h down move, 1d downtrend
      & ((df["RSI_3_1h"] > 15.0) | (df["RSI_3_4h"] > 30.0) | (df["ROC_9_1d"] > -40.0))
      # 1h down move, 1h still high, 4h high
      & ((df["RSI_3_1h"] > 15.0) | (df["AROONU_14_1h"] < 40.0) | (df["AROONU_14_4h"] < 60.0))
      # 1h down move, 1h still high, 4h overbought
      & ((df["RSI_3_1h"] > 15.0) | (df["AROONU_14_1h"] < 50.0) | (df["ROC_9_4h"] < 10.0))
      # 1h down move, 1h high, 1d downtrend
      & ((df["RSI_3_1h"] > 15.0) | (df["AROONU_14_1h"] < 60.0) | (df["ROC_9_1d"] > -30.0))
      # 1h down move, 4h & 1d overbought
      & ((df["RSI_3_1h"] > 15.0) | (df["ROC_9_4h"] < 30.0) | (df["ROC_9_1d"] < 50.0))
      # 1h & 4h down move, 4h high
      & ((df["RSI_3_1h"] > 20.0) | (df["RSI_3_4h"] > 35.0) | (df["AROONU_14_4h"] < 70.0))
      # 1h & 4h down move, 4h high
      & ((df["RSI_3_1h"] > 20.0) | (df["RSI_3_4h"] > 45.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 80.0))
      # 1h & 1d down move, 4h still high
      & ((df["RSI_3_1h"] > 20.0) | (df["RSI_3_1d"] > 20.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 50.0))
      # 1h & 1d down move, 1h still high
      & ((df["RSI_3_1h"] > 20.0) | (df["RSI_3_1d"] > 25.0) | (df["AROONU_14_1h"] < 50.0))
      # 1h down move, 15m still high, 1h high
      & ((df["RSI_3_1h"] > 20.0) | (df["AROONU_14_15m"] < 40.0) | (df["AROONU_14_1h"] < 80.0))
      # 1h down move, 1h still high, 4h high
      & ((df["RSI_3_1h"] > 20.0) | (df["AROONU_14_1h"] < 50.0) | (df["AROONU_14_4h"] < 85.0))
      # 1h down move, 1h high, 1d overbought
      & ((df["RSI_3_1h"] > 20.0) | (df["AROONU_14_1h"] < 70.0) | (df["ROC_9_1d"] < 20.0))
      # 1h down move, 4h high & overbought
      & ((df["RSI_3_1h"] > 20.0) | (df["AROONU_14_4h"] < 80.0) | (df["ROC_9_4h"] < 60.0))
      # 1h down move, 1h still not low enough, 1d downtrend
      & ((df["RSI_3_1h"] > 20.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 30.0) | (df["ROC_9_1d"] > -30.0))
      # 1h & 4h down move, 1h high
      & ((df["RSI_3_1h"] > 25.0) | (df["RSI_3_4h"] > 35.0) | (df["AROONU_14_1h"] < 70.0))
      # 1h & 4h down move, 1d overbought
      & ((df["RSI_3_1h"] > 25.0) | (df["RSI_3_4h"] > 35.0) | (df["ROC_9_1d"] < 20.0))
      # 1h down move, 1h high, 1d overbought
      & ((df["RSI_3_1h"] > 25.0) | (df["AROONU_14_1h"] < 80.0) | (df["ROC_9_1d"] < 30.0))
      # 1h down move, 1h still high, 4h downtrend
      & ((df["RSI_3_1h"] > 25.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 50.0) | (df["ROC_9_4h"] > -20.0))
      # 1h down move, 1d overbought
      & ((df["RSI_3_1h"] > 25.0) | (df["ROC_9_1d"] < 80.0))
      # 1h down move, 1h high, 1d overbought
      & ((df["RSI_3_1h"] > 30.0) | (df["AROONU_14_1h"] < 70.0) | (df["ROC_9_1d"] < 40.0))
      # 1h & 4h down move, 4h high
      & ((df["RSI_3_1h"] > 35.0) | (df["RSI_3_4h"] > 40.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 80.0))
      # 1h down move, 1h still high, 1d overbought
      & ((df["RSI_3_1h"] > 35.0) | (df["AROONU_14_1h"] < 40.0) | (df["ROC_9_1d"] < 40.0))
      # 1h down move, 4h high & overbought
      & ((df["RSI_3_1h"] > 35.0) | (df["AROONU_14_4h"] < 90.0) | (df["ROC_9_4h"] < 60.0))
      # 1h down move, 4h high, 1d downtrend
      & ((df["RSI_3_1h"] > 35.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 90.0) | (df["ROC_9_1d"] > -20.0))
      # 1h down move, 1h high, 1d downtrend
      & ((df["RSI_3_1h"] > 40.0) | (df["AROONU_14_1h"] < 70.0) | (df["ROC_9_1d"] > -30.0))
      # 1h down move, 1h high, 1d downtrend
      & ((df["RSI_3_1h"] > 40.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 70.0) | (df["ROC_9_1d"] > -30.0))
      # 1h down move, 1h & 4h high
      & ((df["RSI_3_1h"] > 45.0) | (df["AROONU_14_1h"] < 80.0) | (df["AROONU_14_4h"] < 100.0))
      # 1h down move, 4h high & overbought
      & ((df["RSI_3_1h"] > 50.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 90.0) | (df["ROC_9_4h"] < 25.0))
      # 4h down move, 4h & 1d downtrend
      & ((df["RSI_3_4h"] > 5.0) | (df["ROC_9_4h"] > -15.0) | (df["ROC_9_1d"] > -20.0))
      # 4h & 1d down move, 1d still high
      & ((df["RSI_3_4h"] > 10.0) | (df["RSI_3_1d"] > 30.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 50.0))
      # 4h down move, 4h & 1d high
      & ((df["RSI_3_4h"] > 10.0) | (df["AROONU_14_4h"] < 60.0) | (df["AROONU_14_1d"] < 70.0))
      # 4h down move, 1d still high, 1d downtrend
      & ((df["RSI_3_4h"] > 10.0) | (df["AROONU_14_1d"] < 50.0) | (df["ROC_9_1d"] > -30.0))
      # 4h down move, 15m & 1h still not low enough
      & (
        (df["RSI_3_4h"] > 10.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 30.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 30.0)
      )
      # 4h down move, 15m stil high, 4h downtrend
      & ((df["RSI_3_4h"] > 10.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 50.0) | (df["ROC_9_4h"] > -20.0))
      # 4h & 1d down move, 1d downtrend
      & ((df["RSI_3_4h"] > 15.0) | (df["RSI_3_1d"] > 25.0) | (df["ROC_9_1d"] > -30.0))
      # 4h & 1d down move, 1h still high
      & ((df["RSI_3_4h"] > 15.0) | (df["RSI_3_1d"] > 30.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 50.0))
      # 4h & 1d down move, 4h high
      & ((df["RSI_3_4h"] > 15.0) | (df["RSI_3_1d"] > 35.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 70.0))
      # 4h down move, 4h & 1d high
      & ((df["RSI_3_4h"] > 20.0) | (df["AROONU_14_4h"] < 70.0) | (df["AROONU_14_1d"] < 70.0))
      # 4h down move, 15m high
      & ((df["RSI_3_4h"] > 20.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 90.0))
      # 4h down move, 1d high & overbought
      & ((df["RSI_3_4h"] > 20.0) | (df["AROONU_14_1d"] < 90.0) | (df["ROC_9_1d"] < 30.0))
      # 4h & 1d down move, 1d overbought
      & ((df["RSI_3_4h"] > 25.0) | (df["RSI_3_1d"] > 40.0) | (df["ROC_9_1d"] < 10.0))
      # 4h & 1d down move, 1d high
      & ((df["RSI_3_4h"] > 25.0) | (df["RSI_3_1d"] > 45.0) | (df["AROONU_14_1d"] < 80.0))
      # 4h down move, 15m high, 1d overbought
      & ((df["RSI_3_4h"] > 30.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 90.0) | (df["ROC_9_1d"] < 10.0))
      # 4h down move, 4h still high, 1d downtrend
      & ((df["RSI_3_4h"] > 35.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 40.0) | (df["ROC_9_1d"] > -30.0))
      # 4h down move, 4h high, 1d overbought
      & ((df["RSI_3_4h"] > 40.0) | (df["AROONU_14_4h"] < 60.0) | (df["ROC_9_1d"] < 40.0))
      # 4h down move, 1d high & overbought
      & ((df["RSI_3_4h"] > 55.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 90.0) | (df["ROC_9_1d"] < 100.0))
      # 1d down move, 1d high, 1d downtrend
      & ((df["RSI_3_1d"] > 15.0) | (df["AROONU_14_1d"] < 70.0) | (df["ROC_9_1d"] > -20.0))
      # 1d down move, 1h high, 1d downtrend
      & ((df["RSI_3_1d"] > 25.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 60.0) | (df["ROC_9_1d"] > -30.0))
      # 1d down move, 1d high, 4h downtrend
      & ((df["RSI_3_1d"] > 35.0) | (df["AROONU_14_1d"] < 70.0) | (df["ROC_9_4h"] > -10.0))
      # 1d down move, 4h high, 1d overbought
      & ((df["RSI_3_1d"] > 60.0) | (df["AROONU_14_4h"] < 70.0) | (df["ROC_9_1d"] < 40.0))
      # 15m high, 1d high & overbought
      & ((df["AROONU_14_15m"] < 70.0) | (df["AROONU_14_1d"] < 100.0) | (df["ROC_9_1d"] < 100.0))
      # 15m high, 4h overbought, 1d downtrend
      & ((df["AROONU_14_15m"] < 80.0) | (df["ROC_9_4h"] < 20.0) | (df["ROC_9_1d"] > -30.0))
      # 1h & 4h high, 4h overbought
      & ((df["AROONU_14_1h"] < 70.0) | (df["AROONU_14_4h"] < 100.0) | (df["ROC_9_4h"] < 10.0))
      # 1h high, 1d overbought
      & ((df["AROONU_14_1h"] < 85.0) | (df["ROC_9_1d"] < 80.0))
      # 1h high, 4h & 1d downtrend
      & ((df["AROONU_14_1h"] < 100.0) | (df["ROC_9_4h"] > -10.0) | (df["ROC_9_1d"] > -25.0))
      # 4h & 1d high, 1d overbought
      & ((df["AROONU_14_4h"] < 100.0) | (df["AROONU_14_1d"] < 100.0) | (df["ROC_9_1d"] < 60.0))
      # 1h high, 4h & 1d downtrend
      & ((df["STOCHRSIk_14_14_3_3_1h"] < 80.0) | (df["ROC_9_4h"] > -10.0) | (df["ROC_9_1d"] > -25.0))
    )

    # Logic
    long_entry_logic.append(
      (df["RSI_14"] < 36.0)
      & (df["BBD_40_2.0"].gt(df["close"] * 0.020))
      & (df["close_delta"].gt(df["close"] * 0.02))
      & (df["BBT_40_2.0"].lt(df["BBD_40_2.0"] * 0.3))
      & (df["close"].lt(df["BBL_40_2.0"].shift()))
      & (df["close"].le(df["close"].shift()))
    )

def append_long_61(df, long_entry_logic, allowed_empty_candles_288) -> None:
    """Append NFI long condition #61, a scalp-mode long entry."""
    long_entry_logic.append(df["num_empty_288"] <= allowed_empty_candles_288)
    long_entry_logic.append(df["protections_long_global"] == True)

    long_entry_logic.append(
      # 5m & 1h down move, 1h still not low enough
      ((df["RSI_3"] > 3.0) | (df["RSI_3_1h"] > 10.0) | (df["AROONU_14_1h"] < 30.0))
      # 5m & 1h down move, 1d high
      & ((df["RSI_3"] > 3.0) | (df["RSI_3_1h"] > 20.0) | (df["AROONU_14_1d"] < 100.0))
      # 5m & 4h down move, 4h high
      & ((df["RSI_3"] > 3.0) | (df["RSI_3_4h"] > 25.0) | (df["AROONU_14_4h"] < 70.0))
      # 5m down move, 1d high & overbought
      & ((df["RSI_3"] > 3.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 90.0) | (df["ROC_9_1d"] < 20.0))
      # 15m & 1h & 4h down move
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_1h"] > 3.0) | (df["RSI_3_4h"] > 10.0))
      # 15m & 1h down move, 4h still high
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_1h"] > 3.0) | (df["RSI_14_4h"] < 40.0))
      # 15m & 1h down move, 4h still high
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_1h"] > 3.0) | (df["AROONU_14_4h"] < 40.0))
      # 15m & 1h down move, 4h still not low enough
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_1h"] > 5.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 20.0))
      # 15m & 1h & 4h down move
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_1h"] > 10.0) | (df["RSI_3_4h"] > 3.0))
      # 15m & 1h down move, 1d still high
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_1h"] > 10.0) | (df["RSI_14_1d"] < 50.0))
      # 15m & 1h down move, 4h downtrend
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_1h"] > 10.0) | (df["CMF_20_4h"] > -0.30))
      # 15m & 1h down move, 1d still high
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_1h"] > 10.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 50.0))
      # 15m & 1h down move, 1d overbought
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_1h"] > 10.0) | (df["ROC_9_1d"] < 40.0))
      # 15m & 1h down move, 1d overbought
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_1h"] > 20.0) | (df["ROC_9_1d"] < 50.0))
      # 15m & 1h down move, 1d high
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_1h"] > 30.0) | (df["AROONU_14_1d"] < 80.0))
      # 15m & 1h down move, 1h still high
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_1h"] > 30.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 40.0))
      # 15m & 1h down move, 1h high
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_1h"] > 45.0) | (df["AROONU_14_1h"] < 80.0))
      # 15m & 1h down move, 1h high
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_1h"] > 60.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 80.0))
      # 15m & 4h down move, 4h still high
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_4h"] > 40.0) | (df["RSI_14_4h"] < 40.0))
      # 15m down move, 15m downtrend. 4h high
      & ((df["RSI_3_15m"] > 3.0) | (df["CMF_20_15m"] > -0.50) | (df["AROONU_14_4h"] < 60.0))
      # 15m down move, 15m still not low enough
      & ((df["RSI_3_15m"] > 3.0) | (df["AROONU_14_15m"] < 30.0))
      # 15m down move, 4h high
      & ((df["RSI_3_15m"] > 3.0) | (df["AROONU_14_4h"] < 80.0))
      # 15m down move, 4h & 1d downtrend
      & ((df["RSI_3_15m"] > 3.0) | (df["ROC_9_4h"] > -20.0) | (df["ROC_9_1d"] > -20.0))
      # 15m & 1h down move, 1h still high
      & ((df["RSI_3_15m"] > 5.0) | (df["RSI_3_1h"] > 20.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 40.0))
      # 15m & 1h down move, 1h high
      & ((df["RSI_3_15m"] > 5.0) | (df["RSI_3_1h"] > 30.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 80.0))
      # 15m & 4h down move, 1h downtrend
      & ((df["RSI_3_15m"] > 5.0) | (df["RSI_3_4h"] > 10.0) | (df["ROC_9_1h"] > -20.0))
      # 15m & 4h down move, 1d overbought
      & ((df["RSI_3_15m"] > 5.0) | (df["RSI_3_4h"] > 15.0) | (df["ROC_9_1d"] < 70.0))
      # 15m & 4h down move, 1h high
      & ((df["RSI_3_15m"] > 5.0) | (df["RSI_3_4h"] > 20.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 80.0))
      # 15m down move, 15m still low, 4h still high
      & ((df["RSI_3_15m"] > 5.0) | (df["AROONU_14_15m"] < 20.0) | (df["AROONU_14_4h"] < 50.0))
      # 15m down move, 15m still high
      & ((df["RSI_3_15m"] > 5.0) | (df["AROONU_14_15m"] < 50.0))
      # 15m & 1h down move, 1d high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1h"] > 10.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 70.0))
      # 15m & 1h down move, 4h downtrend
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1h"] > 10.0) | (df["ROC_9_4h"] > -50.0))
      # 15m & 1h down move, 15m still high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1h"] > 30.0) | (df["AROONU_14_15m"] < 50.0))
      # 15m & 1h down move, 4h overbought
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1h"] > 30.0) | (df["ROC_9_4h"] < 50.0))
      # 15m & 4h down move, 4h still not low enough
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_4h"] > 10.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 30.0))
      # 15m & 4h down move, 4h high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_4h"] > 25.0) | (df["AROONU_14_4h"] < 70.0))
      # 15m & 4h down move, 4h overbought
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_4h"] > 55.0) | (df["ROC_9_4h"] < 50.0))
      # 15m down move, 15m still not low enough, 1d downtrend
      & ((df["RSI_3_15m"] > 10.0) | (df["AROONU_14_15m"] < 30.0) | (df["ROC_9_1d"] > -30.0))
      # 15m down move, 15m still high, 1d overbought
      & ((df["RSI_3_15m"] > 10.0) | (df["AROONU_14_15m"] < 50.0) | (df["ROC_9_1d"] < 30.0))
      # 15m down move, 4h & 1d high
      & ((df["RSI_3_15m"] > 10.0) | (df["AROONU_14_4h"] < 60.0) | (df["AROONU_14_1d"] < 100.0))
      # 15m down move, 1d high, 1d downtrend
      & ((df["RSI_3_15m"] > 10.0) | (df["AROONU_14_1d"] < 85.0) | (df["CMF_20_1d"] > -0.40))
      # 15m down move, 1h high & overbought
      & ((df["RSI_3_15m"] > 10.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 90.0) | (df["ROC_9_1h"] < 20.0))
      # 15m down move, 4h high
      & ((df["RSI_3_15m"] > 10.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 70.0))
      # 15m down move, 4h & 1d overbought
      & ((df["RSI_3_15m"] > 10.0) | (df["ROC_9_4h"] < 10.0) | (df["ROC_9_1d"] < 40.0))
      # 15m & 1h down move, 15m high
      & ((df["RSI_3_15m"] > 15.0) | (df["RSI_3_1h"] > 15.0) | (df["AROONU_14_15m"] < 60.0))
      # 15m & 1h down move, 1h still high
      & ((df["RSI_3_15m"] > 15.0) | (df["RSI_3_1h"] > 15.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 50.0))
      # 15m & 1h down move, 1h high
      & ((df["RSI_3_15m"] > 15.0) | (df["RSI_3_1h"] > 25.0) | (df["AROONU_14_1h"] < 80.0))
      # 15m & 1h down move, 1h high
      & ((df["RSI_3_15m"] > 15.0) | (df["RSI_3_1h"] > 35.0) | (df["AROONU_14_1h"] < 80.0))
      # 15m down move, 15m still high, 1h high
      & ((df["RSI_3_15m"] > 15.0) | (df["AROONU_14_15m"] < 50.0) | (df["AROONU_14_1h"] < 80.0))
      # 15m down move, 4h high, 4h downtrend
      & ((df["RSI_3_15m"] > 15.0) | (df["AROONU_14_4h"] < 60.0) | (df["ROC_9_4h"] > -20.0))
      # 15m down move, 1d high, 4h overbought
      & ((df["RSI_3_15m"] > 15.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 90.0) | (df["ROC_9_4h"] < 40.0))
      # 15m down move, 1h & 4h overbought
      & ((df["RSI_3_15m"] > 15.0) | (df["ROC_9_1h"] < 20.0) | (df["ROC_9_4h"] < 40.0))
      # 15m down move, 4h & 1d downtrend
      & ((df["RSI_3_15m"] > 15.0) | (df["ROC_9_4h"] > -10.0) | (df["ROC_9_1d"] > -40.0))
      # 15m down move, 4h & 1d overbought
      & ((df["RSI_3_15m"] > 15.0) | (df["ROC_9_4h"] < 20.0) | (df["ROC_9_1d"] < 60.0))
      # 15m & 1h down move, 15m high
      & ((df["RSI_3_15m"] > 20.0) | (df["RSI_3_1h"] > 20.0) | (df["AROONU_14_15m"] < 60.0))
      # 15m & 1h down move, 1h high
      & ((df["RSI_3_15m"] > 20.0) | (df["RSI_3_1h"] > 20.0) | (df["AROONU_14_1h"] < 70.0))
      # 15m & 1h down move, 4h high
      & ((df["RSI_3_15m"] > 20.0) | (df["RSI_3_1h"] > 25.0) | (df["AROONU_14_4h"] < 90.0))
      # 15m down move, 1h high
      & ((df["RSI_3_15m"] > 20.0) | (df["AROONU_14_1h"] < 90.0))
      # 15m down move, 4h high & overbought
      & ((df["RSI_3_15m"] > 20.0) | (df["AROONU_14_4h"] < 70.0) | (df["ROC_9_4h"] < 20.0))
      # 15m down move, 1h high
      & ((df["RSI_3_15m"] > 20.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 80.0))
      # 15m down move, 4h high
      & ((df["RSI_3_15m"] > 20.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 90.0))
      # 15m down move, 1h high, 1d overbought
      & ((df["RSI_3_15m"] > 25.0) | (df["AROONU_14_1h"] < 100.0) | (df["ROC_9_1d"] < 20.0))
      # 15m & 1h down move, 1h high
      & ((df["RSI_3_15m"] > 30.0) | (df["RSI_3_1h"] > 50.0) | (df["AROONU_14_1h"] < 100.0))
      # 15m & 1h down move, 4h high
      & ((df["RSI_3_15m"] > 30.0) | (df["RSI_3_1h"] > 50.0) | (df["AROONU_14_4h"] < 100.0))
      # 15m down move, 15m high, 4h high
      & ((df["RSI_3_15m"] > 30.0) | (df["AROONU_14_15m"] < 60.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 70.0))
      # 15m down move, 1h & 4h high
      & (
        (df["RSI_3_15m"] > 30.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 70.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 80.0)
      )
      # 1h & 4h down move, 4h still not low enough
      & ((df["RSI_3_1h"] > 3.0) | (df["RSI_3_4h"] > 5.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 20.0))
      # 1h & 4h down move, 15m stil high
      & ((df["RSI_3_1h"] > 3.0) | (df["RSI_3_4h"] > 10.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 50.0))
      # 1h down move, 1h still not low enough
      & ((df["RSI_3_1h"] > 3.0) | (df["AROONU_14_1h"] < 20.0))
      # 1h & 4h down move, 1d downtrend
      & ((df["RSI_3_1h"] > 5.0) | (df["RSI_3_4h"] > 10.0) | (df["ROC_9_1d"] > -40.0))
      # 1h & 4h down move, 4h still not low enough
      & ((df["RSI_3_1h"] > 5.0) | (df["RSI_3_4h"] > 15.0) | (df["AROONU_14_4h"] < 30.0))
      # 1h & 4h down move, 1d high
      & ((df["RSI_3_1h"] > 5.0) | (df["RSI_3_4h"] > 15.0) | (df["ROC_9_1d"] < 40.0))
      # 1h & 4h down move, 4h still not low enough
      & ((df["RSI_3_1h"] > 5.0) | (df["RSI_3_4h"] > 20.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 30.0))
      # 1h down move, 4h high, 1d overbought
      & ((df["RSI_3_1h"] > 5.0) | (df["AROONU_14_4h"] < 60.0) | (df["ROC_9_1d"] < 10.0))
      # 1h down move, 1d high, 4h downtrend
      & ((df["RSI_3_1h"] > 5.0) | (df["AROONU_14_1d"] < 90.0) | (df["ROC_9_4h"] > -30.0))
      # 1h down move, 1d high, 1d downtrend
      & ((df["RSI_3_1h"] > 5.0) | (df["AROONU_14_1d"] < 100.0) | (df["ROC_9_1d"] > -20.0))
      # 1h & 4h down move, 1h still not low enough
      & ((df["RSI_3_1h"] > 10.0) | (df["RSI_3_4h"] > 10.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 20.0))
      # 1h & 4h down move, 15m downtrend
      & ((df["RSI_3_1h"] > 10.0) | (df["RSI_3_4h"] > 10.0) | (df["ROC_9_15m"] > -15.0))
      # 1h & 4h down move, 4h still high
      & ((df["RSI_3_1h"] > 10.0) | (df["RSI_3_4h"] > 15.0) | (df["RSI_14_4h"] < 40.0))
      # 1h & 4h down move, 1d overbought
      & ((df["RSI_3_1h"] > 10.0) | (df["RSI_3_4h"] > 30.0) | (df["ROC_9_1d"] < 80.0))
      # 1h down move, 15m still high, 4h high
      & ((df["RSI_3_1h"] > 10.0) | (df["AROONU_14_15m"] < 40.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 90.0))
      # 1h down move, 1d high & overbought
      & ((df["RSI_3_1h"] > 10.0) | (df["AROONU_14_1d"] < 100.0) | (df["ROC_9_1d"] < 10.0))
      # 1h down move, 4h still high, 4d downtrend
      & ((df["RSI_3_1h"] > 10.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 50.0) | (df["ROC_9_1d"] > -50.0))
      # 1h down move, 4h downtrend, 1d overbought
      & ((df["RSI_3_1h"] > 10.0) | (df["ROC_9_4h"] > -10.0) | (df["ROC_9_1d"] < 40.0))
      # 1h & 4h down move, 4h high
      & ((df["RSI_3_1h"] > 15.0) | (df["RSI_3_4h"] > 40.0) | (df["AROONU_14_4h"] < 80.0))
      # 1h down move, 1d downtrend, 1d high
      & ((df["RSI_3_1h"] > 15.0) | (df["CMF_20_1d"] > -0.30) | (df["STOCHRSIk_14_14_3_3_1d"] < 80.0))
      # 1h down move, 1h still high
      & ((df["RSI_3_1h"] > 15.0) | (df["AROONU_14_1h"] < 50.0))
      # 1h down move, 4h high, 1d overbought
      & ((df["RSI_3_1h"] > 15.0) | (df["AROONU_14_4h"] < 60.0) | (df["ROC_9_1d"] < 50.0))
      # 1h down move, 4h & 1d high
      & ((df["RSI_3_1h"] > 15.0) | (df["AROONU_14_4h"] < 70.0) | (df["AROONU_14_1d"] < 90.0))
      # 1h & 4h down move, 1d overbought
      & ((df["RSI_3_1h"] > 20.0) | (df["RSI_3_4h"] > 20.0) | (df["ROC_9_1d"] < 20.0))
      # 1h & 4h down move, 4h high
      & ((df["RSI_3_1h"] > 20.0) | (df["RSI_3_4h"] > 30.0) | (df["AROONU_14_4h"] < 80.0))
      # 1h down move, 1h high, 4h overbought
      & ((df["RSI_3_1h"] > 20.0) | (df["AROONU_14_1h"] < 70.0) | (df["ROC_9_4h"] < 10.0))
      # 1h & 4h down move, 1d overbought
      & ((df["RSI_3_1h"] > 25.0) | (df["RSI_3_4h"] > 40.0) | (df["ROC_9_1d"] < 100.0))
      # 1h down move, 1h & 1d high
      & ((df["RSI_3_1h"] > 25.0) | (df["AROONU_14_1h"] < 70.0) | (df["AROONU_14_1d"] < 90.0))
      # 1h down move, 1h still high, 1d overbought
      & ((df["RSI_3_1h"] > 25.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 50.0) | (df["ROC_9_1d"] < 40.0))
      # 1h down move, 4h high, 1d downtrend
      & ((df["RSI_3_1h"] > 25.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 80.0) | (df["ROC_9_1d"] > -40.0))
      # 1h & 4h down move, 1h high
      & ((df["RSI_3_1h"] > 30.0) | (df["RSI_3_4h"] > 35.0) | (df["AROONU_14_1h"] < 75.0))
      # 1h down move, 1h high, 4h downtrend
      & ((df["RSI_3_1h"] > 35.0) | (df["AROONU_14_1h"] < 80.0) | (df["ROC_9_4h"] > -40.0))
      # 1h down move, 1h still high, 1d overbought
      & ((df["RSI_3_1h"] > 35.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 50.0) | (df["ROC_9_1d"] < 200.0))
      # 1h down move, 1h & 4h high
      & ((df["RSI_3_1h"] > 40.0) | (df["AROONU_14_1h"] < 70.0) | (df["AROONU_14_4h"] < 90.0))
      # 1h down move, 1h high, 1d overbought
      & ((df["RSI_3_1h"] > 40.0) | (df["AROONU_14_1h"] < 85.0) | (df["ROC_9_1d"] < 80.0))
      # 1h down move, 1h high, 4h downtrend
      & ((df["RSI_3_1h"] > 40.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 80.0) | (df["ROC_9_4h"] > -20.0))
      # 1h down move, 1h high, 1h overbought
      & ((df["RSI_3_1h"] > 50.0) | (df["AROONU_14_1h"] < 70.0) | (df["ROC_9_1h"] < 25.0))
      # 1h down move, 4h high, 1d downtrend
      & ((df["RSI_3_1h"] > 50.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 60.0) | (df["ROC_9_1d"] > -60.0))
      # 1h down move, 4h & 1d overbought
      & ((df["RSI_3_1h"] > 60.0) | (df["ROC_9_4h"] < 30.0) | (df["ROC_9_1d"] < 60.0))
      # 4h & 1d down move, 15m still high
      & ((df["RSI_3_4h"] > 3.0) | (df["RSI_3_1d"] > 15.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 40.0))
      # 4h & 1d down move, 1h still not low enough
      & ((df["RSI_3_4h"] > 3.0) | (df["RSI_3_1d"] > 15.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 30.0))
      # 4h & 1d down move, 1d still not low enough
      & ((df["RSI_3_4h"] > 3.0) | (df["RSI_3_1d"] > 30.0) | (df["AROONU_14_1d"] < 30.0))
      # 4h down move, 1d high
      & ((df["RSI_3_4h"] > 3.0) | (df["AROONU_14_1d"] < 90.0))
      # 4h down move, 1h still high, 4h downtrend
      & ((df["RSI_3_4h"] > 3.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 50.0) | (df["ROC_9_4h"] > -30.0))
      # 4h down move, 1d high
      & ((df["RSI_3_4h"] > 3.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 90.0))
      # 4h down move, 1h & 4h downtrend
      & ((df["RSI_3_4h"] > 3.0) | (df["ROC_9_1h"] > -30.0) | (df["ROC_9_4h"] > -30.0))
      # 4h down move, 1d overbought
      & ((df["RSI_3_4h"] > 3.0) | (df["ROC_9_1d"] < 40.0))
      # 4h & 1d down move, 1d still high
      & ((df["RSI_3_4h"] > 5.0) | (df["RSI_3_1d"] > 30.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 40.0))
      # 4h down move, 4h downtrend, 4h still high
      & ((df["RSI_3_4h"] > 5.0) | (df["CMF_20_4h"] > -0.20) | (df["AROONU_14_4h"] < 40.0))
      # 4h & 1d down move, 1d downtrend
      & ((df["RSI_3_4h"] > 10.0) | (df["RSI_3_1d"] > 10.0) | (df["ROC_9_1d"] > -40.0))
      # 4h down move, 1h high, 1d downtrend
      & ((df["RSI_3_4h"] > 10.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 60.0) | (df["ROC_9_1d"] > -40.0))
      # 4h & 1d down move, 1d high
      & ((df["RSI_3_4h"] > 15.0) | (df["RSI_3_1d"] > 20.0) | (df["AROONU_14_1d"] < 60.0))
      # 4h down move, 4h high, 1h downtrend
      & ((df["RSI_3_4h"] > 15.0) | (df["AROONU_14_4h"] < 60.0) | (df["ROC_9_1h"] > -20.0))
      # 4h down move, 4h & 1d high
      & ((df["RSI_3_4h"] > 15.0) | (df["AROONU_14_4h"] < 70.0) | (df["AROONU_14_1d"] < 70.0))
      # 4h down move, 1d high & overbought
      & ((df["RSI_3_4h"] > 20.0) | (df["AROONU_14_1d"] < 80.0) | (df["ROC_9_1d"] < 80.0))
      # 4h down move, 1h still not low enough, 1d downtrend
      & ((df["RSI_3_4h"] > 15.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 20.0) | (df["ROC_9_1d"] > -20.0))
      # 4h down move, 4h still high, 1d downtrend
      & ((df["RSI_3_4h"] > 20.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 40.0) | (df["ROC_9_1d"] > -20.0))
      # 4h down move, 4h still high, 1d downtrend
      & ((df["RSI_3_4h"] > 25.0) | (df["AROONU_14_4h"] < 50.0) | (df["ROC_9_1d"] > -40.0))
      # 4h down move, 4h still high, 1d downtrend
      & ((df["RSI_3_4h"] > 30.0) | (df["AROONU_14_4h"] < 50.0) | (df["ROC_9_1d"] > -40.0))
      # 4h down move, 4h high, 1d overbought
      & ((df["RSI_3_4h"] > 30.0) | (df["AROONU_14_4h"] < 80.0) | (df["ROC_9_1d"] < 50.0))
      # 4h down move, 4h & 1d overbought
      & ((df["RSI_3_4h"] > 40.0) | (df["ROC_9_4h"] < 10.0) | (df["ROC_9_1d"] < 50.0))
      # 4h down move, 1h high, 1d overbought
      & ((df["RSI_3_4h"] > 45.0) | (df["AROONU_14_1h"] < 85.0) | (df["ROC_9_1d"] < 50.0))
      # 4h down move, 4h still high, 1d downtrend
      & ((df["RSI_3_4h"] > 50.0) | (df["RSI_14_4h"] < 40.0) | (df["ROC_9_1d"] > -30.0))
      # 4h down move, 4h still high, 1d downtrend
      & ((df["RSI_3_4h"] > 50.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 50.0) | (df["ROC_9_1d"] > -30.0))
      # 1d down move, 1h still high, 1d downtrend
      & ((df["RSI_3_1d"] > 5.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 50.0) | (df["ROC_9_1d"] > -30.0))
      # 1d down move, 1h high, 1d downtrend
      & ((df["RSI_3_1d"] > 10.0) | (df["AROONU_14_1h"] < 80.0) | (df["ROC_9_1d"] > -10.0))
      # 1d down move, 1d high, 1d downtrend
      & ((df["RSI_3_1d"] > 10.0) | (df["AROONU_14_1d"] < 70.0) | (df["ROC_9_1d"] > -40.0))
      # 1d down move, 1h high & overbought
      & ((df["RSI_3_1d"] > 35.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 90.0) | (df["ROC_9_1h"] < 10.0))
      # 1d downtrend, 1d high & overbought
      & ((df["CMF_20_1d"] > -0.30) | (df["AROONU_14_1d"] < 85.0) | (df["ROC_9_1d"] < 100.0))
      # 15m high, 1h high & overbought
      & ((df["AROONU_14_15m"] < 60.0) | (df["AROONU_14_1h"] < 85.0) | (df["ROC_9_1h"] < 10.0))
      # 1h high, 4h high, 1h overbought
      & ((df["AROONU_14_1h"] < 70.0) | (df["AROONU_14_4h"] < 100.0) | (df["ROC_9_1h"] < 20.0))
      # 1h & 1d high, 1h overbought
      & ((df["AROONU_14_1h"] < 70.0) | (df["AROONU_14_1d"] < 70.0) | (df["ROC_9_1h"] < 20.0))
      # 1h & 4h high, 1d downtrend
      & ((df["AROONU_14_1h"] < 85.0) | (df["AROONU_14_4h"] < 100.0) | (df["ROC_9_1d"] > -80.0))
      # 4h still high, 5m downtrend
      & ((df["AROONU_14_4h"] < 40.0) | (df["ROC_9"] > -40.0))
      # 4h high, 4h & 1d overbought
      & ((df["AROONU_14_4h"] < 60.0) | (df["ROC_9_4h"] < 30.0) | (df["ROC_9_1d"] < 60.0))
      # 4h & 1d high, 4h overbought
      & ((df["AROONU_14_4h"] < 80.0) | (df["AROONU_14_1d"] < 100.0) | (df["ROC_9_4h"] < 30.0))
      # 4h & 1d high, 1d overbought
      & ((df["AROONU_14_4h"] < 80.0) | (df["AROONU_14_1d"] < 100.0) | (df["ROC_9_1d"] < 50.0))
      # 4h high, 4h & 1d overbought
      & ((df["AROONU_14_4h"] < 80.0) | (df["ROC_9_4h"] < 20.0) | (df["ROC_9_1d"] < 20.0))
      # 1d high, 1h & 4h downtrend
      & ((df["AROONU_14_1d"] < 85.0) | (df["ROC_9_1h"] > -30.0) | (df["ROC_9_4h"] > -50.0))
      # 1d high, 1h & 1d overbought
      & ((df["AROONU_14_1d"] < 85.0) | (df["ROC_9_1h"] < 20.0) | (df["ROC_9_1d"] < 100.0))
      # 1d high, 4h & 1d overbought
      & ((df["AROONU_14_1d"] < 90.0) | (df["ROC_9_4h"] < 30.0) | (df["ROC_9_1d"] < 60.0))
      # 1h high, 1d overbought
      & ((df["STOCHRSIk_14_14_3_3_1h"] < 70.0) | (df["ROC_9_1d"] < 40.0))
      # 4h high, 1h overbought, 1d downtrend
      & ((df["STOCHRSIk_14_14_3_3_4h"] < 80.0) | (df["ROC_9_1h"] < 40.0) | (df["ROC_9_1d"] > -70.0))
      # 4h high, 1h & 4h overbought
      & ((df["STOCHRSIk_14_14_3_3_4h"] < 90.0) | (df["ROC_9_1h"] < 20.0) | (df["ROC_9_4h"] < 50.0))
      # 1h & 4h overbought
      & ((df["ROC_9_1h"] < 100.0) | (df["ROC_9_4h"] < 100.0))
      # big drop in the last 20 days, 1d high, 1d downtrend
      & (
        (df["close"] > (df["high_max_20_1d"] * 0.20))
        | (df["STOCHRSIk_14_14_3_3_1d"] < 70.0)
        | (df["ROC_9_1d"] > -15.0)
      )
    )

    # Logic
    long_entry_logic.append(
      (df["RSI_3"] < 50.0)
      & (df["AROONU_14"] < 25.0)
      & (df["STOCHRSIk_14_14_3_3"] < 30.0)
      & (df["EMA_26"] > df["EMA_12"])
      & ((df["EMA_26"] - df["EMA_12"]) > (df["open"] * 0.030))
      & ((df["EMA_26"].shift() - df["EMA_12"].shift()) > (df["open"] / 100.0))
    )


def append_long_62(df, long_entry_logic, allowed_empty_candles_288) -> None:
    """Append NFI long condition #62, a scalp-mode long entry."""
    long_entry_logic.append(df["num_empty_288"] <= allowed_empty_candles_288)
    long_entry_logic.append(df["protections_long_global"] == True)

    long_entry_logic.append(
      # 5m & 4h down move, 1d high
      ((df["RSI_3"] > 3.0) | (df["RSI_3_4h"] > 10.0) | (df["AROONU_14_1d"] < 90.0))
      # 5m & 1d down move, 15m still high
      & ((df["RSI_3"] > 3.0) | (df["RSI_3_1d"] > 20.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 40.0))
      # 5m & 4h down move, 15m still high
      & ((df["RSI_3"] > 5.0) | (df["RSI_3_4h"] > 25.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 50.0))
      # 5m & 4h down move, 4h still not low enough
      & ((df["RSI_3"] > 5.0) | (df["RSI_3_4h"] > 15.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 20.0))
      # 15m & 1h down move, 1h still not low enough
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_1h"] > 10.0) | (df["AROONU_14_1h"] < 20.0))
      # 15m & 1h down move, 4h still not low enough
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_1h"] > 10.0) | (df["RSI_14_4h"] < 30.0))
      # 15m & 1h down move, 4h still high
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_1h"] > 15.0) | (df["RSI_14_4h"] < 50.0))
      # 15m & 1h down move, 4h still high
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_1h"] > 20.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 40.0))
      # 15m & 1h down move, 4h still high
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_1h"] > 25.0) | (df["AROONU_14_4h"] < 50.0))
      # 15m & 4h down move, 4h still not low enough
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_4h"] > 3.0) | (df["AROONU_14_4h"] < 20.0))
      # 15m & 4h down move, 4h still high
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_4h"] > 20.0) | (df["AROONU_14_4h"] < 40.0))
      # 15m & 1h down move, 1h still not low enough
      & ((df["RSI_3_15m"] > 5.0) | (df["RSI_3_1h"] > 10.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 20.0))
      # 15m & 1h down move, 15m still not low enough
      & ((df["RSI_3_15m"] > 5.0) | (df["RSI_3_1h"] > 10.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 20.0))
      # 15m & 1h down move, 4h still high
      & ((df["RSI_3_15m"] > 5.0) | (df["RSI_3_1h"] > 10.0) | (df["AROONU_14_4h"] < 40.0))
      # 15m & 4h down move, 15m still not low enough
      & ((df["RSI_3_15m"] > 5.0) | (df["RSI_3_4h"] > 10.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 30.0))
      # 15m & 4h down move, 1h downtrend
      & ((df["RSI_3_15m"] > 5.0) | (df["RSI_3_4h"] > 10.0) | (df["ROC_9_1h"] > -20.0))
      # 15m & 4h down move, 1d overbought
      & ((df["RSI_3_15m"] > 5.0) | (df["RSI_3_4h"] > 10.0) | (df["ROC_9_1d"] < 20.0))
      # 15m & 4h down move, 4h still high
      & ((df["RSI_3_15m"] > 5.0) | (df["RSI_3_4h"] > 15.0) | (df["RSI_14_4h"] < 40.0))
      # 15m & 1h down move, 4h still high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1h"] > 10.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 40.0))
      # 15m & 1h down move, 1d downtrend
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1h"] > 10.0) | (df["ROC_9_1d"] > -20.0))
      # 15m & 1h down move, 15m high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1h"] > 10.0) | (df["AROONU_14_15m"] < 70.0))
      # 15m & 1h down move, 1h still not low enough
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1h"] > 10.0) | (df["AROONU_14_1h"] < 30.0))
      # 15m & 1h down move, 1h still high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1h"] > 15.0) | (df["AROONU_14_1h"] < 40.0))
      # 15m & 1h down move, 1d high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1h"] > 10.0) | (df["AROONU_14_1d"] < 100.0))
      # 15m & 1h down move, 4h high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1h"] > 15.0) | (df["AROONU_14_4h"] < 60.0))
      # 15m & 1h down move, 4h high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1h"] > 35.0) | (df["AROONU_14_4h"] < 90.0))
      # 15m & 4h down move, 15m still not low enough
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_4h"] > 15.0) | (df["AROONU_14_15m"] < 20.0))
      # 15m & 4h down move, 1d high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_4h"] > 20.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 90.0))
      # 15m & 4h down move, 4h still not low enough
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_4h"] > 20.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 30.0))
      # 15m & 4h down move, 1d high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_4h"] > 20.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 70.0))
      # 15m & 4h down move, 4h downtrend
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_4h"] > 25.0) | (df["CMF_20_4h"] > -0.30))
      # 15m & 4h down move, 1d high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_4h"] > 30.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 90.0))
      # 15m & 4h down move, 1d overbought
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_4h"] > 40.0) | (df["ROC_9_1d"] < 200.0))
      # 15m & 1d down move, 1d high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1d"] > 20.0) | (df["AROONU_14_1d"] < 75.0))
      # 15m down move, 4h high, 1d downtrend
      & ((df["RSI_3_15m"] > 10.0) | (df["AROONU_14_4h"] < 70.0) | (df["ROC_9_1d"] > -25.0))
      # 15m & 1h down move, 4h high
      & ((df["RSI_3_15m"] > 15.0) | (df["RSI_3_1h"] > 15.0) | (df["AROONU_14_4h"] < 75.0))
      # 15m & 4h down move, 4h high
      & ((df["RSI_3_15m"] > 15.0) | (df["RSI_3_4h"] > 20.0) | (df["AROONU_14_4h"] < 60.0))
      # 15m & 4h down move, 4h still high
      & ((df["RSI_3_15m"] > 15.0) | (df["RSI_3_4h"] > 25.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 40.0))
      # 15m down move, 15m downtrend, 4h high
      & ((df["RSI_3_15m"] > 15.0) | (df["CMF_20_15m"] > -0.30) | (df["AROONU_14_4h"] < 50.0))
      # 15m down move, 15m still high, 4h overbought
      & ((df["RSI_3_15m"] > 15.0) | (df["AROONU_14_15m"] < 40.0) | (df["ROC_9_4h"] < 40.0))
      # 15m down move, 4h & 1d high
      & ((df["RSI_3_15m"] > 15.0) | (df["AROONU_14_4h"] < 80.0) | (df["AROONU_14_1d"] < 100.0))
      # 15m down move, 1h & 4h high
      & ((df["RSI_3_15m"] > 20.0) | (df["AROONU_14_1h"] < 70.0) | (df["AROONU_14_4h"] < 100.0))
      # 15m down move, 15m still not low enough, 1d overbought
      & ((df["RSI_3_15m"] > 20.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 30.0) | (df["ROC_9_1d"] < 80.0))
      # 15m & 4h down move, 15m stil high
      & ((df["RSI_3_15m"] > 25.0) | (df["RSI_3_4h"] > 30.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 40.0))
      # 15m down move, 15m still not low enough, 1d downtrend
      & ((df["RSI_3_15m"] > 25.0) | (df["AROONU_14_15m"] < 25.0) | (df["ROC_9_1d"] > -50.0))
      # 15m down move, 15m still high, 4h high
      & ((df["RSI_3_15m"] > 25.0) | (df["AROONU_14_15m"] < 50.0) | (df["AROONU_14_4h"] < 80.0))
      # 15m & 1h down move, 1h high
      & ((df["RSI_3_15m"] > 30.0) | (df["RSI_3_1h"] > 40.0) | (df["AROONU_14_1h"] < 50.0))
      # 15m & 4h down move, 4h high
      & ((df["RSI_3_15m"] > 30.0) | (df["RSI_3_4h"] > 35.0) | (df["AROONU_14_4h"] < 70.0))
      # 15m down move, 15m still high, 4h high
      & ((df["RSI_3_15m"] > 35.0) | (df["AROONU_14_15m"] < 50.0) | (df["AROONU_14_4h"] < 80.0))
      # 1h & 4h down move, 4h still high
      & ((df["RSI_3_1h"] > 3.0) | (df["RSI_3_4h"] > 40.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 50.0))
      # 1h & 4h down move, 4h high
      & ((df["RSI_3_1h"] > 3.0) | (df["RSI_3_4h"] > 50.0) | (df["AROONU_14_4h"] < 70.0))
      # 1h down move, 15m still not low enough
      & ((df["RSI_3_1h"] > 3.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 20.0))
      # 1h down move, 4h still high, 1d downtrend
      & ((df["RSI_3_1h"] > 3.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 50.0) | (df["ROC_9_1d"] > -20.0))
      # 1h & 4h down move, 15m still not low enough
      & ((df["RSI_3_1h"] > 5.0) | (df["RSI_3_4h"] > 5.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 30.0))
      # 1h & 4h down move, 4h still not low enough
      & ((df["RSI_3_1h"] > 5.0) | (df["RSI_3_4h"] > 5.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 30.0))
      # 1h & 4h down move, 4h still not low enough
      & ((df["RSI_3_1h"] > 5.0) | (df["RSI_3_4h"] > 10.0) | (df["AROONU_14_4h"] < 20.0))
      # 1h & 4h down move, 4h downtrend
      & ((df["RSI_3_1h"] > 5.0) | (df["RSI_3_4h"] > 15.0) | (df["ROC_9_4h"] > -30.0))
      # 1h & 4h down move, 4h still not low enough
      & ((df["RSI_3_1h"] > 5.0) | (df["RSI_3_4h"] > 20.0) | (df["RSI_14_4h"] < 30.0))
      # 1h & 4h down move, 4h still high
      & ((df["RSI_3_1h"] > 5.0) | (df["RSI_3_4h"] > 30.0) | (df["AROONU_14_4h"] < 40.0))
      # 1h & 4h & 1d down move
      & ((df["RSI_3_1h"] > 10.0) | (df["RSI_3_4h"] > 10.0) | (df["RSI_3_1d"] > 15.0))
      # 1h & 4h down move, 15m high
      & ((df["RSI_3_1h"] > 10.0) | (df["RSI_3_4h"] > 10.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 60.0))
      # 1h & 4h down move, 4h still not low enough
      & ((df["RSI_3_1h"] > 10.0) | (df["RSI_3_4h"] > 10.0) | (df["AROONU_14_4h"] < 30.0))
      # 1h & 4h down move, 1h downtrend
      & ((df["RSI_3_1h"] > 10.0) | (df["RSI_3_4h"] > 10.0) | (df["ROC_9_1h"] > -20.0))
      # 1h & 4h down move, 1d downtrend
      & ((df["RSI_3_1h"] > 10.0) | (df["RSI_3_4h"] > 10.0) | (df["ROC_9_1d"] > -20.0))
      # 1h & 4h down move, 1d overbought
      & ((df["RSI_3_1h"] > 10.0) | (df["RSI_3_4h"] > 10.0) | (df["ROC_9_1d"] < 10.0))
      # 1h & 4h down move, 4h still high
      & ((df["RSI_3_1h"] > 10.0) | (df["RSI_3_4h"] > 20.0) | (df["AROONU_14_4h"] < 40.0))
      # 1h & 4h down move, 4h high
      & ((df["RSI_3_1h"] > 10.0) | (df["RSI_3_4h"] > 25.0) | (df["AROONU_14_4h"] < 60.0))
      # 1h & 4h down move, 4h still high
      & ((df["RSI_3_1h"] > 10.0) | (df["RSI_3_4h"] > 25.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 40.0))
      # 1h & 4h down move, 1h still not low enough
      & ((df["RSI_3_1h"] > 10.0) | (df["RSI_3_4h"] > 35.0) | (df["AROONU_14_1h"] < 30.0))
      # 1h& 1d down move, 1h still high
      & ((df["RSI_3_1h"] > 10.0) | (df["RSI_3_1d"] > 25.0) | (df["AROONU_14_1h"] < 40.0))
      # 1h & 1d down move, 1d high
      & ((df["RSI_3_1h"] > 10.0) | (df["RSI_3_1d"] > 60.0) | (df["AROONU_14_1d"] < 80.0))
      # 1h & 4h down move, 1d high
      & ((df["RSI_3_1h"] > 15.0) | (df["RSI_3_4h"] > 15.0) | (df["RSI_14_1d"] < 60.0))
      # 1h & 4h down move, 4h still high
      & ((df["RSI_3_1h"] > 15.0) | (df["RSI_3_4h"] > 15.0) | (df["AROONU_14_4h"] < 40.0))
      # 1h & 4h down move, 1d high
      & ((df["RSI_3_1h"] > 15.0) | (df["RSI_3_4h"] > 15.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 70.0))
      # 1h & 4h down move, 4h still high
      & ((df["RSI_3_1h"] > 15.0) | (df["RSI_3_4h"] > 20.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 40.0))
      # 1h & 4h down move, 1d high
      & ((df["RSI_3_1h"] > 15.0) | (df["RSI_3_4h"] > 20.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 90.0))
      # 1h & 4h down move, 1d downtrend
      & ((df["RSI_3_1h"] > 15.0) | (df["RSI_3_4h"] > 25.0) | (df["ROC_9_1d"] > -40.0))
      # 1h & 4h down move, 1d high
      & ((df["RSI_3_1h"] > 15.0) | (df["RSI_3_4h"] > 30.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 80.0))
      # 1h & 1d down move, 4h high
      & ((df["RSI_3_1h"] > 15.0) | (df["RSI_3_1d"] > 15.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 80.0))
      # 1h down move, 4h high, 1d overbought
      & ((df["RSI_3_1h"] > 15.0) | (df["AROONU_14_4h"] < 70.0) | (df["ROC_9_1d"] < 100.0))
      # 1h down move, 1d high, 4h downtrend
      & ((df["RSI_3_1h"] > 15.0) | (df["AROONU_14_1d"] < 90.0) | (df["ROC_9_4h"] > -20.0))
      # 1h & 4h down move, 1d high
      & ((df["RSI_3_1h"] > 20.0) | (df["RSI_3_4h"] > 25.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 70.0))
      # 1h & 4h down move, 4h high
      & ((df["RSI_3_1h"] > 20.0) | (df["RSI_3_4h"] > 40.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 70.0))
      # 1h & 4h down move, 4h overbought
      & ((df["RSI_3_1h"] > 20.0) | (df["RSI_3_4h"] > 40.0) | (df["ROC_9_4h"] < 10.0))
      # 1h & 4h down move, 1d high
      & ((df["RSI_3_1h"] > 20.0) | (df["RSI_3_4h"] > 45.0) | (df["AROONU_14_1d"] < 100.0))
      # 1h & 4h down move, 4h high
      & ((df["RSI_3_1h"] > 20.0) | (df["RSI_3_4h"] > 50.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 80.0))
      # 1h down move, 1h high
      & ((df["RSI_3_1h"] > 20.0) | (df["AROONU_14_1h"] < 70.0))
      # 1h down move, 4h still high, 1d downtrend
      & ((df["RSI_3_1h"] > 20.0) | (df["AROONU_14_4h"] < 40.0) | (df["ROC_9_1d"] > -20.0))
      # 1h down move, 4h high
      & ((df["RSI_3_1h"] > 20.0) | (df["AROONU_14_4h"] < 85.0))
      # 1h down move, 1h still not low enough, 4h stil high
      & ((df["RSI_3_1h"] > 20.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 20.0) | (df["AROONU_14_4h"] < 40.0))
      # 1h down move, 4h still high, 1d downtrend
      & ((df["RSI_3_1h"] > 20.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 40.0) | (df["ROC_9_1d"] > -40.0))
      # 1h down move, 1d high, 4h downtrend
      & ((df["RSI_3_1h"] > 20.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 80.0) | (df["ROC_9_4h"] > -20.0))
      # 1h down move, 4h high
      & ((df["RSI_3_1h"] > 20.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 80.0))
      # 1h & 4h down move, 1h still not low enough
      & ((df["RSI_3_1h"] > 25.0) | (df["RSI_3_4h"] > 25.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 20.0))
      # 1h & 4h down move, 1d overbought
      & ((df["RSI_3_1h"] > 25.0) | (df["RSI_3_4h"] > 25.0) | (df["ROC_9_1d"] < 50.0))
      # 1h & 4h down move, 4h high
      & ((df["RSI_3_1h"] > 25.0) | (df["RSI_3_4h"] > 30.0) | (df["AROONU_14_4h"] < 60.0))
      # 1h down move, 4h & 1d high
      & ((df["RSI_3_1h"] > 25.0) | (df["AROONU_14_4h"] < 60.0) | (df["AROONU_14_1d"] < 100.0))
      # 1h down move, 4h high, 4h downtrend
      & ((df["RSI_3_1h"] > 25.0) | (df["AROONU_14_4h"] < 70.0) | (df["CMF_20_4h"] > -0.50))
      # 1h down move, 4h high & overbought
      & ((df["RSI_3_1h"] > 25.0) | (df["AROONU_14_4h"] < 70.0) | (df["ROC_9_4h"] < 10.0))
      # 1h down move, 15m still high, 1d overbought
      & ((df["RSI_3_1h"] > 25.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 50.0) | (df["ROC_9_1d"] < 30.0))
      # 1h & 4h down move, 4h still high
      & ((df["RSI_3_1h"] > 30.0) | (df["RSI_3_4h"] > 30.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 50.0))
      # 1h & 4h down move, 1d overbought
      & ((df["RSI_3_1h"] > 30.0) | (df["RSI_3_4h"] > 30.0) | (df["ROC_9_1d"] < 100.0))
      # 1h & dh down move, 4h high
      & ((df["RSI_3_1h"] > 30.0) | (df["RSI_3_4h"] > 50.0) | (df["AROONU_14_4h"] < 85.0))
      # 1h down move, 4h & 1d downtrend
      & ((df["RSI_3_1h"] > 30.0) | (df["ROC_9_4h"] > -25.0) | (df["ROC_9_1d"] > -60.0))
      # 1h down move, 4h & 1h overbought
      & ((df["RSI_3_1h"] > 30.0) | (df["ROC_9_4h"] < 30.0) | (df["ROC_9_1d"] < 40.0))
      # 1h down move, 4h high, 4h downtrend
      & ((df["RSI_3_1h"] > 30.0) | (df["AROONU_14_4h"] < 70.0) | (df["CMF_20_4h"] > -0.40))
      # 1h down move, 1d high, 4h downtrend
      & ((df["RSI_3_1h"] > 30.0) | (df["AROONU_14_1d"] < 80.0) | (df["ROC_9_4h"] > -30.0))
      # 1h down move, 1d high, 4h overbought
      & ((df["RSI_3_1h"] > 30.0) | (df["AROONU_14_1d"] < 100.0) | (df["ROC_9_4h"] < 20.0))
      # 1h down move, 4h still high, 1d downtrend
      & ((df["RSI_3_1h"] > 30.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 40.0) | (df["ROC_9_1d"] > -80.0))
      # 1h down move, 4h high & overbought
      & ((df["RSI_3_1h"] > 30.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 90.0) | (df["ROC_9_4h"] < 20.0))
      # 1h down move, 4h & 1d overbought
      & ((df["RSI_3_1h"] > 30.0) | (df["ROC_9_4h"] < 10.0) | (df["ROC_9_1d"] < 30.0))
      # 1h & 4h down move, 1h still high
      & ((df["RSI_3_1h"] > 35.0) | (df["RSI_3_4h"] > 35.0) | (df["AROONU_14_1h"] < 50.0))
      # 1h & 4h down move, 4h high
      & ((df["RSI_3_1h"] > 35.0) | (df["RSI_3_4h"] > 40.0) | (df["AROONU_14_4h"] < 80.0))
      # 1h down move, 1h & 4h high
      & ((df["RSI_3_1h"] > 35.0) | (df["AROONU_14_1h"] < 70.0) | (df["AROONU_14_4h"] < 100.0))
      # 1h down move, 1d high, 4h overbought
      & ((df["RSI_3_1h"] > 35.0) | (df["AROONU_14_1d"] < 90.0) | (df["ROC_9_4h"] < 40.0))
      # 1h down move, 4h high & overbought
      & ((df["RSI_3_1h"] > 40.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 70.0) | (df["ROC_9_4h"] < 30.0))
      # 1h down move, 4h high & overbought
      & ((df["RSI_3_1h"] > 45.0) | (df["AROONU_14_4h"] < 80.0) | (df["ROC_9_4h"] < 100.0))
      # 1h down move, 1h overbought
      & ((df["RSI_3_1h"] > 50.0) | (df["ROC_9_1h"] < 40.0))
      # 1h down move, 4h & 1d overbought
      & ((df["RSI_3_1h"] > 60.0) | (df["ROC_9_4h"] < 30.0) | (df["ROC_9_1d"] < 100.0))
      # 4h & 1d down move, 1d still high
      & ((df["RSI_3_4h"] > 5.0) | (df["RSI_3_1d"] > 20.0) | (df["AROONU_14_1d"] < 40.0))
      # 4h & 1d down move, 4h still not low enough
      & ((df["RSI_3_4h"] > 5.0) | (df["RSI_3_1d"] > 30.0) | (df["AROONU_14_4h"] < 20.0))
      # 4h & 1d down move, 1d high
      & ((df["RSI_3_4h"] > 5.0) | (df["RSI_3_1d"] > 30.0) | (df["AROONU_14_1d"] < 70.0))
      # 4h down move, 1h high, 4h downtrend
      & ((df["RSI_3_4h"] > 5.0) | (df["AROONU_14_1h"] < 70.0) | (df["ROC_9_4h"] > -20.0))
      # 4h down move, 4h high
      & ((df["RSI_3_4h"] > 5.0) | (df["AROONU_14_4h"] < 60.0))
      # 4h & 1d down move, 1d still not low enough
      & ((df["RSI_3_4h"] > 10.0) | (df["RSI_3_1d"] > 15.0) | (df["AROONU_14_1d"] < 30.0))
      # 4h down move, 15m still high
      & ((df["RSI_3_4h"] > 10.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 40.0))
      # 4h down move, 1h downtrend, 1d downtrend
      & ((df["RSI_3_4h"] > 15.0) | (df["CMF_20_1h"] > -0.40) | (df["ROC_9_1d"] > -20.0))
      # 4h down move, 15m high, 1d overbought
      & ((df["RSI_3_4h"] > 15.0) | (df["AROONU_14_15m"] < 70.0) | (df["ROC_9_1d"] < 100.0))
      # 4h down move, 4h still high, 4h downtrend
      & ((df["RSI_3_4h"] > 15.0) | (df["AROONU_14_4h"] < 40.0) | (df["ROC_9_4h"] > -20.0))
      # 4h down move, 15m still not low enough, 1d downtrend
      & ((df["RSI_3_4h"] > 15.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 30.0) | (df["ROC_9_1d"] > -20.0))
      # 4h down move, 1d high & overbought
      & ((df["RSI_3_4h"] > 15.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 90.0) | (df["ROC_9_1d"] < 20.0))
      # 4h & 1d down move, 1d overbought
      & ((df["RSI_3_4h"] > 20.0) | (df["RSI_3_1d"] > 45.0) | (df["ROC_9_1d"] < 40.0))
      # 4h down move, 15m high, 4h downtrend
      & ((df["RSI_3_4h"] > 20.0) | (df["AROONU_14_15m"] < 70.0) | (df["ROC_9_4h"] > -30.0))
      # 4h down move, 1d high & overbought
      & ((df["RSI_3_4h"] > 20.0) | (df["AROONU_14_1d"] < 80.0) | (df["ROC_9_1d"] < 30.0))
      # 4h & 1d down move, 1d overbought
      & ((df["RSI_3_4h"] > 25.0) | (df["RSI_3_1d"] > 45.0) | (df["ROC_9_1d"] < 10.0))
      # 4h down move, 15m high, 4h high
      & ((df["RSI_3_4h"] > 25.0) | (df["AROONU_14_15m"] < 70.0) | (df["AROONU_14_4h"] < 80.0))
      # 4h down move, 4h still high, 1d downtrend
      & ((df["RSI_3_4h"] > 25.0) | (df["AROONU_14_4h"] < 40.0) | (df["ROC_9_1d"] > -20.0))
      # 4h down move, 4h still high, 4h downtrend
      & ((df["RSI_3_4h"] > 25.0) | (df["AROONU_14_4h"] < 50.0) | (df["CMF_20_4h"] > -0.40))
      # 4h down move, 4h high, 1d high
      & ((df["RSI_3_4h"] > 30.0) | (df["AROONU_14_4h"] < 70.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 80.0))
      # 4h down move, 1d still high, 1d downtrend
      & ((df["RSI_3_4h"] > 30.0) | (df["AROONU_14_1d"] < 40.0) | (df["ROC_9_1d"] > -20.0))
      # 4h down move, 1d high & overbought
      & ((df["RSI_3_4h"] > 30.0) | (df["AROONU_14_1d"] < 100.0) | (df["ROC_9_1d"] < 20.0))
      # 4h down move, 4h still not low enough, 1d overbought
      & ((df["RSI_3_4h"] > 30.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 20.0) | (df["ROC_9_1d"] < 40.0))
      # 4h down move, 1h high
      & ((df["RSI_3_4h"] > 35.0) | (df["AROONU_14_1h"] < 70.0))
      # 4h down move, 15m & 4h still high
      & (
        (df["RSI_3_4h"] > 40.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 50.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 50.0)
      )
      # 4h down move, 1d high & overbought
      & ((df["RSI_3_4h"] > 40.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 90.0) | (df["ROC_9_1d"] < 200.0))
      # 4h down move, 4h high
      & ((df["RSI_3_4h"] > 40.0) | (df["AROONU_14_4h"] < 100.0))
      # 4h down move, 4h still high, 1d downtrend
      & ((df["RSI_3_4h"] > 50.0) | (df["RSI_14_4h"] < 40.0) | (df["ROC_9_1d"] > -30.0))
      # 4h down move, 4h still high, 1d downtrend
      & ((df["RSI_3_4h"] > 50.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 50.0) | (df["ROC_9_1d"] > -30.0))
      # 4h down move, 4h overbought
      & ((df["RSI_3_4h"] > 55.0) | (df["ROC_9_4h"] < 30.0))
      # 4h down move, 4h overbought
      & ((df["RSI_3_4h"] > 60.0) | (df["ROC_9_4h"] < 40.0))
      # 1d down move, 4h & 1d downtrend
      & ((df["RSI_3_1d"] > 10.0) | (df["ROC_9_4h"] > -20.0) | (df["ROC_9_1d"] > -30.0))
      # 1d down move, 1d high, 1d downtrend
      & ((df["RSI_3_1d"] > 15.0) | (df["AROONU_14_1d"] < 70.0) | (df["ROC_9_1d"] > -20.0))
      # 1d down move, 4h & 1d downtrend
      & ((df["RSI_3_1d"] > 15.0) | (df["ROC_9_4h"] > -10.0) | (df["ROC_9_1d"] > -40.0))
      # 4h & 1d downtrend, 1d high
      & ((df["CMF_20_4h"] > -0.50) | (df["CMF_20_1d"] > -0.50) | (df["AROONU_14_1d"] < 85.0))
      # 4h still not low enough, 4h & 1d downtrend
      & ((df["AROONU_14_4h"] < 30.0) | (df["ROC_9_4h"] > -20.0) | (df["ROC_9_1d"] > -25.0))
      # 4h & 1d high, 4h overbought
      & ((df["AROONU_14_4h"] < 70.0) | (df["AROONU_14_1d"] < 100.0) | (df["ROC_9_4h"] < 30.0))
      # 4h & 1d high, 1d overbought
      & ((df["AROONU_14_4h"] < 70.0) | (df["AROONU_14_1d"] < 100.0) | (df["ROC_9_1d"] < 80.0))
      # 4h high, 1h & 4h overbought
      & ((df["AROONU_14_4h"] < 80.0) | (df["ROC_9_1h"] < 40.0) | (df["ROC_9_4h"] < 40.0))
      # 1d high, 4h downtrend, 1d overbought
      & ((df["AROONU_14_1d"] < 85.0) | (df["ROC_9_4h"] > -20.0) | (df["ROC_9_1d"] < 200.0))
      # 1d high, 4h & 1d overbought
      & ((df["AROONU_14_1d"] < 90.0) | (df["ROC_9_4h"] < 30.0) | (df["ROC_9_1d"] < 60.0))
      # 4h high, 1h & 4h overbought
      & ((df["STOCHRSIk_14_14_3_3_4h"] < 70.0) | (df["ROC_9_1h"] < 40.0) | (df["ROC_9_4h"] < 40.0))
      # 4h high, 4h & 1d overbought
      & ((df["STOCHRSIk_14_14_3_3_4h"] < 80.0) | (df["ROC_9_4h"] < 20.0) | (df["ROC_9_1d"] < 20.0))
      # 1d green, 4h down move, 4h still high
      & ((df["change_pct_1d"] < 40.0) | (df["RSI_3_4h"] > 35.0) | (df["AROONU_14_4h"] < 40.0))
    )

    # Logic
    long_entry_logic.append(
      (df["RSI_3"] < 40.0)
      & (df["AROONU_14"] < 30.0)
      & (df["STOCHRSIk_14_14_3_3"] < 20.0)
      & (df["STOCHRSIk_14_14_3_3_15m"] < 70.0)
      & (df["WILLR_84_1h"] < -70.0)
      & (df["STOCHRSIk_14_14_3_3_1h"] < 30.0)
      & (df["BBB_20_2.0_1h"] > 12.0)
      & (df["close_max_48"] >= (df["close"] * 1.10))
    )


def append_long_63(df, long_entry_logic, allowed_empty_candles_288) -> None:
    """Append NFI long condition #63, a scalp-mode long entry."""
    long_entry_logic.append(df["num_empty_288"] <= allowed_empty_candles_288)
    long_entry_logic.append(df["protections_long_global"] == True)

    long_entry_logic.append(
      (df["RSI_3_15m"] > 5.0)
      # 5m & 1h down move, 1h still not low enough
      & ((df["RSI_3"] > 3.0) | (df["RSI_3_1h"] > 10.0) | (df["AROONU_14_1h"] < 30.0))
      # 5m & 1d down move, 1d downtrend
      & ((df["RSI_3"] > 3.0) | (df["RSI_3_1d"] > 15.0) | (df["CMF_20_1d"] > -0.25))
      # 5m down move, 1d high & overbought
      & ((df["RSI_3"] > 3.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 90.0) | (df["ROC_9_1d"] < 20.0))
      # 15m & 1h down move, 1h still not low enough
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1h"] > 15.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 30.0))
      # 15m & 1h down move, 4h still high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1h"] > 20.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 50.0))
      # 15m & 1h down move 1h still high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1h"] > 25.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 40.0))
      # 15m & 1h down move, 15m still high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1h"] > 30.0) | (df["AROONU_14_15m"] < 50.0))
      # 15m & 1h down move 1h still high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1h"] > 30.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 50.0))
      # 15m & 1h down move, 4h overbought
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1h"] > 30.0) | (df["ROC_9_4h"] < 10.0))
      # 15m & 1h down move, 1h high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1h"] > 50.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 90.0))
      # 15m & 4h down move, 4h still not low enough
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_4h"] > 10.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 30.0))
      # 15m & 4h down move, 1d high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_4h"] > 10.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 80.0))
      # 15m & 4h down move, 1d downtrend
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_4h"] > 15.0) | (df["ROC_9_1d"] > -20.0))
      # 1h & 4h down move, 15m still high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_4h"] > 30.0) | (df["AROONU_14_15m"] < 50.0))
      # 15m & 4h down move, 4h high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_4h"] > 40.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 80.0))
      # 15m & 1d down move, 1d high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1d"] > 10.0) | (df["AROONU_14_1d"] < 70.0))
      # 15m & 1d down move, 1d high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1d"] > 20.0) | (df["AROONU_14_1d"] < 75.0))
      # 15m down move, 15m still high, 4h high
      & ((df["RSI_3_15m"] > 10.0) | (df["AROONU_14_15m"] < 50.0) | (df["AROONU_14_4h"] < 80.0))
      # 15m down move, 1h still high, 1d overbought
      & ((df["RSI_3_15m"] > 10.0) | (df["AROONU_14_1h"] < 50.0) | (df["ROC_9_1d"] < 60.0))
      # 15m down move, 4h high, 1d overbought
      & ((df["RSI_3_15m"] > 10.0) | (df["AROONU_14_4h"] < 60.0) | (df["ROC_9_1d"] < 60.0))
      # 15m down move, 1d high & overbought
      & ((df["RSI_3_15m"] > 10.0) | (df["AROONU_14_1d"] < 90.0) | (df["ROC_9_1d"] < 20.0))
      # 15m down move, 1d high, 4h overbought
      & ((df["RSI_3_15m"] > 10.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 90.0) | (df["ROC_9_4h"] < 10.0))
      # 15m & 1h & 4h down move
      & ((df["RSI_3_15m"] > 15.0) | (df["RSI_3_1h"] > 15.0) | (df["RSI_3_4h"] > 15.0))
      # 15m & 1h down move, 1h high
      & ((df["RSI_3_15m"] > 15.0) | (df["RSI_3_1h"] > 25.0) | (df["AROONU_14_1h"] < 70.0))
      # 15m & 4h down move, 15m still high
      & ((df["RSI_3_15m"] > 15.0) | (df["RSI_3_4h"] > 25.0) | (df["AROONU_14_15m"] < 40.0))
      # 15m & 4h down move, 1d high
      & ((df["RSI_3_15m"] > 15.0) | (df["RSI_3_4h"] > 35.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 90.0))
      # 15m & 4h down move, 15m high
      & ((df["RSI_3_15m"] > 15.0) | (df["RSI_3_4h"] > 35.0) | (df["AROONU_14_15m"] < 60.0))
      # 15m & 4h down move, 4h high
      & ((df["RSI_3_15m"] > 15.0) | (df["RSI_3_4h"] > 35.0) | (df["AROONU_14_4h"] < 60.0))
      # 15m & 1d down move, 4h high
      & ((df["RSI_3_15m"] > 15.0) | (df["RSI_3_1d"] > 25.0) | (df["AROONU_14_4h"] < 100.0))
      # 15m down move, 15m still high, 4h high
      & ((df["RSI_3_15m"] > 15.0) | (df["AROONU_14_15m"] < 50.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 80.0))
      # 15m down move, 4h high, 4h downtrend
      & ((df["RSI_3_15m"] > 15.0) | (df["AROONU_14_4h"] < 60.0) | (df["ROC_9_4h"] > -20.0))
      # 15m down move, 4h & 1d high
      & ((df["RSI_3_15m"] > 15.0) | (df["AROONU_14_4h"] < 75.0) | (df["AROONU_14_1d"] < 100.0))
      # 15m down move, 15m still not low enough, 1h still high
      & (
        (df["RSI_3_15m"] > 15.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 30.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 50.0)
      )
      # 15m down move, 4h & 1d overbought
      & ((df["RSI_3_15m"] > 15.0) | (df["ROC_9_4h"] < 20.0) | (df["ROC_9_1d"] < 60.0))
      # 15m & 1h down move, 1h high
      & ((df["RSI_3_15m"] > 20.0) | (df["RSI_3_1h"] > 20.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 70.0))
      # 15m & 4h down move, 4h high
      & ((df["RSI_3_15m"] > 20.0) | (df["RSI_3_4h"] > 50.0) | (df["AROONU_14_4h"] < 85.0))
      # 15m down move, 1h high
      & ((df["RSI_3_15m"] > 20.0) | (df["AROONU_14_1h"] < 75.0))
      # 15m down move, 1d high & overbought
      & ((df["RSI_3_15m"] > 20.0) | (df["AROONU_14_1d"] < 90.0) | (df["ROC_9_1d"] < 80.0))
      # 15m down move, 15m high, 4h downtrend
      & ((df["RSI_3_15m"] > 20.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 60.0) | (df["ROC_9_4h"] > -50.0))
      # 15m down move, 4h overbought
      & ((df["RSI_3_15m"] > 20.0) | (df["ROC_9_4h"] < 40.0))
      # 15m & 1h down move, 1h high
      & ((df["RSI_3_15m"] > 25.0) | (df["RSI_3_1h"] > 25.0) | (df["AROONU_14_1h"] < 70.0))
      # 15m & 4h down move, 4h high
      & ((df["RSI_3_15m"] > 25.0) | (df["RSI_3_4h"] > 25.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 60.0))
      # 15m down move, 1d high, 4h overbought
      & ((df["RSI_3_15m"] > 25.0) | (df["AROONU_14_1d"] < 80.0) | (df["ROC_9_4h"] < 10.0))
      # 15m down move, 4h & 1d overbought
      & ((df["RSI_3_15m"] > 25.0) | (df["ROC_9_4h"] < 10.0) | (df["ROC_9_1d"] < 50.0))
      # 15m & 1h down move, 1h high
      & ((df["RSI_3_15m"] > 30.0) | (df["RSI_3_1h"] > 40.0) | (df["AROONU_14_1h"] < 80.0))
      # 15m & 1h down move, 1h high
      & ((df["RSI_3_15m"] > 30.0) | (df["RSI_3_1h"] > 45.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 80.0))
      # 15m down move, 15m downtrend, 4h high
      & ((df["RSI_3_15m"] > 30.0) | (df["CMF_20_15m"] > -0.30) | (df["AROONU_14_4h"] < 100.0))
      # 15m down move, 15m still high, 1d high
      & ((df["RSI_3_15m"] > 30.0) | (df["AROONU_14_15m"] < 50.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 70.0))
      # 15m down move, 15m high, 4h high
      & ((df["RSI_3_15m"] > 30.0) | (df["AROONU_14_15m"] < 60.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 70.0))
      # 15m down move, 4h high, 1h downtrend
      & ((df["RSI_3_15m"] < 30.0) | (df["AROONU_14_4h"] < 85.0) | (df["ROC_9_1h"] > -40.0))
      # 15m down move, 4h high
      & ((df["RSI_3_15m"] > 30.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 90.0))
      # 15m & 1h down move, 15m high
      & ((df["RSI_3_15m"] > 35.0) | (df["RSI_3_1h"] > 45.0) | (df["AROONU_14_15m"] < 70.0))
      # 15m & 4h down move, 4h high
      & ((df["RSI_3_15m"] > 35.0) | (df["RSI_3_4h"] > 35.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 80.0))
      # 15m down move, 15m still high, 4h overbought
      & ((df["RSI_3_15m"] > 35.0) | (df["AROONU_14_15m"] < 40.0) | (df["ROC_9_4h"] < 20.0))
      # 15m down move, 15m still high, 1d overbought
      & ((df["RSI_3_15m"] > 35.0) | (df["AROONU_14_15m"] < 40.0) | (df["ROC_9_1d"] < 30.0))
      # 15m down move, 4h high & overbought
      & ((df["RSI_3_15m"] > 35.0) | (df["AROONU_14_4h"] < 60.0) | (df["ROC_9_4h"] < 20.0))
      # 15m down move, 4h high & overbought
      & ((df["RSI_3_15m"] > 35.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 70.0) | (df["ROC_9_4h"] < 20.0))
      # 15m still high, 4h high
      & ((df["RSI_3_15m"] < 40.0) | (df["AROONU_14_4h"] < 85.0))
      # 1h & 4h down move, 4h still not low enough
      & ((df["RSI_3_1h"] > 2.0) | (df["RSI_3_4h"] > 15.0) | (df["RSI_14_4h"] < 30.0))
      # 1h & 4h down move, 15m still not low enough
      & ((df["RSI_3_1h"] > 3.0) | (df["RSI_3_4h"] > 3.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 30.0))
      # 1h & 4h down move, 15m downtrend
      & ((df["RSI_3_1h"] > 3.0) | (df["RSI_3_4h"] > 3.0) | (df["ROC_9_15m"] > -30.0))
      # 1h & 4h down move, 4h still high
      & ((df["RSI_3_1h"] > 3.0) | (df["RSI_3_4h"] > 10.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 40.0))
      # 1h & 4h down move, 4h stil high
      & ((df["RSI_3_1h"] > 3.0) | (df["RSI_3_4h"] > 20.0) | (df["RSI_14_4h"] < 40.0))
      # 1h ^ 4h down move, 1d downtrend
      & ((df["RSI_3_1h"] > 3.0) | (df["RSI_3_4h"] > 25.0) | (df["ROC_9_1d"] > -50.0))
      # 1h & 1d down move, 4h still high
      & ((df["RSI_3_1h"] > 3.0) | (df["RSI_3_1d"] > 10.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 40.0))
      # 1h & 1d down move, 1h downtrend
      & ((df["RSI_3_1h"] > 3.0) | (df["RSI_3_1d"] > 15.0) | (df["ROC_9_1h"] > -40.0))
      # 1h down move, 15m downtrend, 1h still high
      & ((df["RSI_3_1h"] > 3.0) | (df["CMF_20_15m"] > -0.40) | (df["AROONU_14_1h"] < 40.0))
      # 1h down move, 15m still not low enough, 4h still high
      & ((df["RSI_3_1h"] > 3.0) | (df["AROONU_14_15m"] < 30.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 40.0))
      # 1h down move, 1h still not low enough
      & ((df["RSI_3_1h"] > 3.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 30.0))
      # 1h down move, 4h still high, 1d downtrend
      & ((df["RSI_3_1h"] > 3.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 50.0) | (df["ROC_9_1d"] > -20.0))
      # 1h down move, 4h high
      & ((df["RSI_3_1h"] > 3.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 70.0))
      # 1h & 4h down move, 1d high
      & ((df["RSI_3_1h"] > 5.0) | (df["RSI_3_4h"] > 5.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 60.0))
      # 1h & 4h down move, 4h still not low enough
      & ((df["RSI_3_1h"] > 5.0) | (df["RSI_3_4h"] > 10.0) | (df["AROONU_14_4h"] < 20.0))
      # 1h & 4h down move, 4h downtrend
      & ((df["RSI_3_1h"] > 5.0) | (df["RSI_3_4h"] > 10.0) | (df["ROC_9_4h"] > -20.0))
      # 1h & 4h down move, 4h still not low enough
      & ((df["RSI_3_1h"] > 5.0) | (df["RSI_3_4h"] > 15.0) | (df["AROONU_14_4h"] < 30.0))
      # 1h & 4h down move, 4h still high
      & ((df["RSI_3_1h"] > 5.0) | (df["RSI_3_4h"] > 35.0) | (df["RSI_14_4h"] < 40.0))
      # 1h down move, 1d high, 4h downtrend
      & ((df["RSI_3_1h"] > 5.0) | (df["AROONU_14_1d"] < 90.0) | (df["ROC_9_4h"] > -30.0))
      # 1h down move, 4h downtrend
      & ((df["RSI_3_1h"] > 5.0) | (df["ROC_9_4h"] > -20.0))
      # 1h, 1d downtrend
      & ((df["RSI_3_1h"] > 5.0) | (df["ROC_9_1d"] > -50.0))
      # 1h & 4h down move, 4h still not low enough
      & ((df["RSI_3_1h"] > 10.0) | (df["RSI_3_4h"] > 10.0) | (df["RSI_14_4h"] < 30.0))
      # 1h & 4h down move, 4h still not low enough
      & ((df["RSI_3_1h"] > 10.0) | (df["RSI_3_4h"] > 10.0) | (df["AROONU_14_4h"] < 30.0))
      # 1h & 4h down move, 15m still high
      & ((df["RSI_3_1h"] > 10.0) | (df["RSI_3_4h"] > 10.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 50.0))
      # 1h & 4h down move, 15m still not low enough
      & ((df["RSI_3_1h"] > 10.0) | (df["RSI_3_4h"] > 15.0) | (df["AROONU_14_15m"] < 30.0))
      # 1h & 4h down move, 1h still not low enough
      & ((df["RSI_3_1h"] > 10.0) | (df["RSI_3_4h"] > 15.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 20.0))
      # 1h & 4h down move, 1d high
      & ((df["RSI_3_1h"] > 10.0) | (df["RSI_3_4h"] > 25.0) | (df["AROONU_14_1d"] < 80.0))
      # 1h & 4h down move, 1d downtrend
      & ((df["RSI_3_1h"] > 10.0) | (df["RSI_3_4h"] > 25.0) | (df["ROC_9_1d"] > -40.0))
      # 1h & 4h down move, 4h still high
      & ((df["RSI_3_1h"] > 10.0) | (df["RSI_3_4h"] > 30.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 50.0))
      # 1h & 4h down move, 1d overbought
      & ((df["RSI_3_1h"] > 10.0) | (df["RSI_3_4h"] > 35.0) | (df["ROC_9_1d"] < 70.0))
      # 1h & 1d down move, 1h still high
      & ((df["RSI_3_1h"] > 10.0) | (df["RSI_3_1d"] > 10.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 40.0))
      # 1h & 1d down move, 4h high
      & ((df["RSI_3_1h"] > 10.0) | (df["RSI_3_1d"] > 15.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 70.0))
      # 1h & 1d downtrend, 1d overbought
      & ((df["RSI_3_1h"] > 10.0) | (df["RSI_3_1d"] > 45.0) | (df["ROC_9_1d"] < 10.0))
      # 1h down move, 1h downtrend, 1h still not low enough
      & ((df["RSI_3_1h"] > 10.0) | (df["CMF_20_1h"] > -0.20) | (df["AROONU_14_1h"] < 30.0))
      # 1h down move, 1h downtrend, 1h still not low enough
      & ((df["RSI_3_1h"] > 10.0) | (df["CMF_20_1h"] > -0.20) | (df["STOCHRSIk_14_14_3_3_1h"] < 30.0))
      # 1h down move, 1h downtrend
      & ((df["RSI_3_1h"] > 10.0) | (df["CMF_20_1h"] > -0.30))
      # 1h down move, 1d high & overbought
      & ((df["RSI_3_1h"] > 10.0) | (df["AROONU_14_1d"] < 70.0) | (df["ROC_9_1d"] < 50.0))
      # 1h & 4h down move, 4h still not low enough
      & ((df["RSI_3_1h"] > 10.0) | (df["RSI_3_4h"] > 10.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 20.0))
      # 1h down move, 1d overbought
      & ((df["RSI_3_1h"] > 10.0) | (df["ROC_9_1d"] < 200.0))
      # 1h & 4h down move, 1h still not low enough
      & ((df["RSI_3_1h"] > 15.0) | (df["RSI_3_4h"] > 15.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 30.0))
      # 1h & 4h down move, 15m high
      & ((df["RSI_3_1h"] > 15.0) | (df["RSI_3_4h"] > 20.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 90.0))
      # 1h & 4h down move, 1d downtrend
      & ((df["RSI_3_1h"] > 15.0) | (df["RSI_3_4h"] > 20.0) | (df["ROC_9_1d"] > -40.0))
      # 1h & 4h down mov, 1d overbought
      & ((df["RSI_3_1h"] > 15.0) | (df["RSI_3_4h"] > 30.0) | (df["ROC_9_1d"] < 100.0))
      # 1h down move, 1d downtrend, 1d high
      & ((df["RSI_3_1h"] > 15.0) | (df["CMF_20_1d"] > -0.30) | (df["STOCHRSIk_14_14_3_3_1d"] < 80.0))
      # 1h down move, 1h still high
      & ((df["RSI_3_1h"] > 15.0) | (df["AROONU_14_1h"] < 50.0))
      # 1h down move, 1d high, 4h downtrend
      & ((df["RSI_3_1h"] > 15.0) | (df["AROONU_14_1d"] < 70.0) | (df["ROC_9_4h"] > -20.0))
      # 1h down move, 1d high, 1d downtrend
      & ((df["RSI_3_1h"] > 15.0) | (df["AROONU_14_1d"] < 70.0) | (df["ROC_9_1d"] > -20.0))
      # 1h down move, 1d high & overbought
      & ((df["RSI_3_1h"] > 15.0) | (df["AROONU_14_1d"] < 90.0) | (df["ROC_9_1d"] < 30.0))
      # 1h down move, 1h still high
      & ((df["RSI_3_1h"] > 15.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 40.0))
      # 1h & 4h down move, 1d high
      & ((df["RSI_3_1h"] > 20.0) | (df["RSI_3_4h"] > 25.0) | (df["AROONU_14_1d"] < 80.0))
      # 1h & 4h down move, 1h high
      & ((df["RSI_3_1h"] > 20.0) | (df["RSI_3_4h"] > 45.0) | (df["AROONU_14_1h"] < 60.0))
      # 1h down move, 1h high, 1d overbought
      & ((df["RSI_3_1h"] > 20.0) | (df["AROONU_14_1h"] < 70.0) | (df["ROC_9_1d"] < 100.0))
      # 1h down move, 4h still high
      & ((df["RSI_3_1h"] > 20.0) | (df["AROONU_14_4h"] < 40.0))
      # 1h down move, 4h still high, 1d downtrend
      & ((df["RSI_3_1h"] > 20.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 40.0) | (df["ROC_9_1d"] > -25.0))
      # 1h down move, 4h high & overbought
      & ((df["RSI_3_1h"] > 20.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 70.0) | (df["ROC_9_4h"] < 10.0))
      # 1h down move, 1h & 1d high
      & ((df["RSI_3_1h"] > 25.0) | (df["AROONU_14_1h"] < 70.0) | (df["AROONU_14_1d"] < 90.0))
      # 1h & 4h down move, 4h high
      & ((df["RSI_3_1h"] > 25.0) | (df["RSI_3_4h"] > 50.0) | (df["AROONU_14_4h"] < 85.0))
      # 1h & 4h down move, 1d overbought
      & ((df["RSI_3_1h"] > 25.0) | (df["RSI_3_4h"] > 50.0) | (df["ROC_9_1d"] < 100.0))
      # 1h down move, 1h still not low enough, 4h still high
      & ((df["RSI_3_1h"] > 25.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 30.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 50.0))
      # 1h down move, 4h high, 1d downtrend
      & ((df["RSI_3_1h"] > 25.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 80.0) | (df["ROC_9_1d"] > -40.0))
      # 1h down move, 1h still high, 1h downtrend
      & ((df["RSI_3_1h"] > 25.0) | (df["AROONU_14_1h"] < 40.0) | (df["ROC_9_1h"] > -50.0))
      # 1h down move, 4h high & overbought
      & ((df["RSI_3_1h"] > 25.0) | (df["AROONU_14_4h"] < 90.0) | (df["ROC_9_4h"] < 20.0))
      # 1h down move, 1h still high, 1d overbought
      & ((df["RSI_3_1h"] > 25.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 50.0) | (df["ROC_9_1d"] < 40.0))
      # 1h down move, 4h high & overbought
      & ((df["RSI_3_1h"] > 25.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 80.0) | (df["ROC_9_4h"] < 20.0))
      # 1h down move, 4h high, 1d overbought
      & ((df["RSI_3_1h"] > 25.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 80.0) | (df["ROC_9_1d"] < 70.0))
      # 1h & 4h down move, 1h high
      & ((df["RSI_3_1h"] > 30.0) | (df["RSI_3_4h"] > 30.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 60.0))
      # 1h & 4h down move, 4h still high
      & ((df["RSI_3_1h"] > 30.0) | (df["RSI_3_4h"] > 30.0) | (df["AROONU_14_4h"] < 50.0))
      # 1h & 4h down move, 1h high
      & ((df["RSI_3_1h"] > 30.0) | (df["RSI_3_4h"] > 50.0) | (df["AROONU_14_1h"] < 70.0))
      # 1h & 4h down move, 4h high
      & ((df["RSI_3_1h"] > 30.0) | (df["RSI_3_4h"] > 50.0) | (df["AROONU_14_4h"] < 90.0))
      # 1h down move, 1h high, 4h overbought
      & ((df["RSI_3_1h"] > 30.0) | (df["AROONU_14_1h"] < 70.0) | (df["ROC_9_4h"] < 30.0))
      # 1h down move, 1h high
      & ((df["RSI_3_1h"] > 30.0) | (df["AROONU_14_1h"] < 80.0))
      # 1h down move, 4h high & overbought
      & ((df["RSI_3_1h"] > 30.0) | (df["AROONU_14_4h"] < 90.0) | (df["ROC_9_4h"] < 20.0))
      # 1h down move, 1d high & overbought
      & ((df["RSI_3_1h"] > 30.0) | (df["AROONU_14_1d"] < 80.0) | (df["ROC_9_1d"] < 200.0))
      # 1h down move, 1d high, 4h downtrend
      & ((df["RSI_3_1h"] > 30.0) | (df["AROONU_14_1d"] < 90.0) | (df["ROC_9_4h"] > -40.0))
      # 1h down move, 1d high, 4h overbought
      & ((df["RSI_3_1h"] > 30.0) | (df["AROONU_14_1d"] < 100.0) | (df["ROC_9_4h"] < 80.0))
      # 1h down move, 1h & 4h still high
      & ((df["RSI_3_1h"] > 30.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 40.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 50.0))
      # 1h down move, 1h highm 1d overbought
      & ((df["RSI_3_1h"] > 30.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 60.0) | (df["ROC_9_1d"] < 30.0))
      # 1h down move, 4h overbought
      & ((df["RSI_3_1h"] > 30.0) | (df["ROC_9_4h"] < 50.0))
      # 4h down move, 1d downtrend
      & ((df["RSI_3_4h"] > 30.0) | (df["ROC_9_1d"] > -50.0))
      # 1h down move, 1h high, 4h overbought
      & ((df["RSI_3_1h"] > 35.0) | (df["AROONU_14_1h"] < 70.0) | (df["ROC_9_4h"] < 40.0))
      # 1h down move, 1h high, 1d downtrend
      & ((df["RSI_3_1h"] > 35.0) | (df["AROONU_14_1h"] < 70.0) | (df["ROC_9_1d"] > -25.0))
      # 1h down move, 4h high & overbought
      & ((df["RSI_3_1h"] > 35.0) | (df["AROONU_14_4h"] < 85.0) | (df["ROC_9_4h"] < 100.0))
      # 1h down move, 4h high & overbought
      & ((df["RSI_3_1h"] > 35.0) | (df["AROONU_14_4h"] < 100.0) | (df["ROC_9_4h"] < 20.0))
      # 1h down move, 4h high & overbought
      & ((df["RSI_3_1h"] > 35.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 70.0) | (df["ROC_9_4h"] < 10.0))
      # 1h down move, 1d high & overbought
      & ((df["RSI_3_1h"] > 35.0) | (df["AROONU_14_1d"] < 100.0) | (df["ROC_9_1d"] < 100.0))
      # 1h down move, 1h still high, 1d overbought
      & ((df["RSI_3_1h"] > 35.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 50.0) | (df["ROC_9_1d"] < 200.0))
      # 1h down move, 15m high, 1h high
      & ((df["RSI_3_1h"] > 40.0) | (df["AROONU_14_15m"] < 60.0) | (df["AROONU_14_1h"] < 70.0))
      # 1h down move, 1h high, 1d overbought
      & ((df["RSI_3_1h"] > 40.0) | (df["AROONU_14_1h"] < 80.0) | (df["ROC_9_1d"] < 80.0))
      # 1h down move, 1h & 4h overbought
      & ((df["RSI_3_1h"] > 40.0) | (df["ROC_9_1h"] < 10.0) | (df["ROC_9_4h"] < 10.0))
      # 1h & 4h down move, 1d overbought
      & ((df["RSI_3_1h"] > 45.0) | (df["RSI_3_4h"] > 65.0) | (df["ROC_9_1d"] < 200.0))
      # 1h down move, 1h high & overbought
      & ((df["RSI_3_1h"] > 45.0) | (df["AROONU_14_1h"] < 70.0) | (df["ROC_9_1h"] < 10.0))
      # 1h down move, 4h high & overbought
      & ((df["RSI_3_1h"] > 45.0) | (df["AROONU_14_4h"] < 100.0) | (df["ROC_9_4h"] < 40.0))
      # 1h down move, 1h high, 1d downtrend
      & ((df["RSI_3_1h"] > 50.0) | (df["AROONU_14_1h"] < 90.0) | (df["ROC_9_1d"] > -30.0))
      # 1h down move, 4h high & overbought
      & ((df["RSI_3_1h"] > 50.0) | (df["AROONU_14_4h"] < 100.0) | (df["ROC_9_4h"] < 100.0))
      # 1h down move, 4h high, 1d downtrend
      & ((df["RSI_3_1h"] > 50.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 60.0) | (df["ROC_9_1d"] > -60.0))
      # 1h down move, 15m high, 1h high
      & ((df["RSI_3_1h"] > 55.0) | (df["AROONU_14_15m"] < 60.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 80.0))
      # 1h down move, 1h high & overbought
      & ((df["RSI_3_1h"] > 55.0) | (df["AROONU_14_1h"] < 90.0) | (df["ROC_9_1h"] < 10.0))
      # 4h down move, 1h still not low enough, 4h downtrend
      & ((df["RSI_3_4h"] > 3.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 20.0) | (df["ROC_9_4h"] > -30.0))
      # 4h down move, 1h & 4h downtrend
      & ((df["RSI_3_4h"] > 3.0) | (df["ROC_9_1h"] > -30.0) | (df["ROC_9_4h"] > -30.0))
      # 4h down move, 1d high, 4h downtrend
      & ((df["RSI_3_4h"] > 5.0) | (df["AROONU_14_1d"] < 80.0) | (df["ROC_9_4h"] > -10.0))
      # 4h down move, 1h still high
      & ((df["RSI_3_4h"] > 5.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 50.0))
      # 4h down move, 4h & 1d downtrend
      & ((df["RSI_3_4h"] > 5.0) | (df["ROC_9_4h"] > -15.0) | (df["ROC_9_1d"] > -20.0))
      # 4h & 1d down move, 1d overbought
      & ((df["RSI_3_4h"] > 10.0) | (df["RSI_3_1d"] > 45.0) | (df["ROC_9_1d"] < 10.0))
      # 4h down move, 1d still high, 1d downtrend
      & ((df["RSI_3_4h"] > 10.0) | (df["AROONU_14_1d"] < 50.0) | (df["ROC_9_1d"] > -30.0))
      # 4h down move, 1d high, 4h downtrend
      & ((df["RSI_3_4h"] > 10.0) | (df["AROONU_14_1d"] < 85.0) | (df["ROC_9_4h"] > -20.0))
      # 4h down move, 15m high, 15m downtrend
      & ((df["RSI_3_4h"] > 10.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 60.0) | (df["ROC_9_15m"] > -10.0))
      # 4h down move, 1h still high, 1d downtrend
      & ((df["RSI_3_4h"] > 10.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 40.0) | (df["ROC_9_1d"] > -20.0))
      # 4h down move, 1h high
      & ((df["RSI_3_4h"] > 10.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 70.0))
      # 4h down move, 4h still high, 1d downtrend
      & ((df["RSI_3_4h"] > 10.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 40.0) | (df["ROC_9_1d"] > -20.0))
      # 4h down move, 4h downtrend, 1d overbought
      & ((df["RSI_3_4h"] > 10.0) | (df["ROC_9_4h"] > -30.0) | (df["ROC_9_1d"] < 40.0))
      # 4h & 1d down move, 1d high
      & ((df["RSI_3_4h"] > 15.0) | (df["RSI_3_1d"] > 20.0) | (df["AROONU_14_1d"] < 60.0))
      # 4h & 1d down move, 1d high
      & ((df["RSI_3_4h"] > 15.0) | (df["RSI_3_1d"] > 40.0) | (df["AROONU_14_1d"] < 80.0))
      # 4h down move, 1h high
      & ((df["RSI_3_4h"] > 15.0) | (df["AROONU_14_1h"] < 50.0))
      # 4h down move, 1h still high, 1d downtrend
      & ((df["RSI_3_4h"] > 15.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 50.0) | (df["ROC_9_1d"] > -30.0))
      # 4h down move, 1d high & overbought
      & ((df["RSI_3_4h"] > 15.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 90.0) | (df["ROC_9_1d"] < 20.0))
      # 4h down move, 15m still high
      & ((df["RSI_3_4h"] > 20.0) | (df["AROONU_14_15m"] < 45.0))
      # 4h down move, 1h still not low enough, 1d downtrend
      & ((df["RSI_3_4h"] > 20.0) | (df["AROONU_14_1h"] < 30.0) | (df["ROC_9_1d"] > -20.0))
      # 4h down move, 4h still high, 1d high
      & ((df["RSI_3_4h"] > 20.0) | (df["AROONU_14_4h"] < 50.0) | (df["AROONU_14_1d"] < 100.0))
      # 4h down move, 1d high & overbought
      & ((df["RSI_3_4h"] > 20.0) | (df["AROONU_14_1d"] < 80.0) | (df["ROC_9_1d"] < 80.0))
      # 4h down move, 15m still high, 4h high
      & ((df["RSI_3_4h"] > 25.0) | (df["AROONU_14_15m"] < 40.0) | (df["AROONU_14_4h"] < 70.0))
      # 4h down move, 1h & 4h still high
      & ((df["RSI_3_4h"] > 25.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 40.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 40.0))
      # 4h dowqn move, 4h still high, 1d downtrend
      & ((df["RSI_3_4h"] > 25.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 30.0) | (df["ROC_9_1d"] > -30.0))
      # 4h down move, 4h high, 1d overbought
      & ((df["RSI_3_4h"] > 30.0) | (df["AROONU_14_4h"] < 80.0) | (df["ROC_9_1d"] < 50.0))
      # 4h down move, 1h high, 4h downtrend
      & ((df["RSI_3_4h"] > 30.0) | (df["AROONU_14_1h"] < 70.0) | (df["ROC_9_4h"] > -10.0))
      # 4h down move, 4h & 1d downtrend
      & ((df["RSI_3_4h"] > 40.0) | (df["AROONU_14_4h"] < 70.0) | (df["AROONU_14_1d"] < 100.0))
      # 4h down move, 1d high & overbought
      & ((df["RSI_3_4h"] > 40.0) | (df["AROONU_14_1d"] < 90.0) | (df["ROC_9_1d"] < 80.0))
      # 4h down move, 1h high, 1d downtrend
      & ((df["RSI_3_4h"] > 40.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 80.0) | (df["ROC_9_1d"] > -20.0))
      # 4h down move, 4h & 1d overbought
      & ((df["RSI_3_4h"] > 40.0) | (df["ROC_9_4h"] < 10.0) | (df["ROC_9_1d"] < 50.0))
      # 4h down move, 4h still high, 1d downtrend
      & ((df["RSI_3_4h"] > 50.0) | (df["RSI_14_4h"] < 40.0) | (df["ROC_9_1d"] > -30.0))
      # 4h down move, 4h high, 1d overbought
      & ((df["RSI_3_4h"] > 50.0) | (df["AROONU_14_4h"] < 70.0) | (df["ROC_9_1d"] < 40.0))
      # 4h down move, 4h still high, 1d downtrend
      & ((df["RSI_3_4h"] > 50.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 50.0) | (df["ROC_9_1d"] > -30.0))
      # 4h down move, 1h high, 1d overbought
      & ((df["RSI_3_4h"] > 60.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 90.0) | (df["ROC_9_1d"] < 30.0))
      # 4h down move, 4h high & overbought
      & ((df["RSI_3_4h"] > 60.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 70.0) | (df["ROC_9_4h"] < 20.0))
      # 1d down move, 1h high & overbought
      & ((df["RSI_3_1d"] > 35.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 90.0) | (df["ROC_9_1h"] < 10.0))
      # 1d down move, 1h high & overbought
      & ((df["RSI_3_1d"] > 40.0) | (df["AROONU_14_1d"] < 70.0) | (df["ROC_9_1d"] < 80.0))
      # 1d down move, 4h high & overbought
      & ((df["RSI_3_1d"] > 45.0) | (df["AROONU_14_4h"] < 80.0) | (df["ROC_9_4h"] < 30.0))
      # 1h downtrend, 1h high
      & ((df["CMF_20_1h"] > -0.20) | (df["AROONU_14_1h"] < 80.0))
      # 4h & 1d downtrend, 1d high
      & ((df["CMF_20_4h"] > -0.30) | (df["CMF_20_1d"] > -0.30) | (df["STOCHRSIk_14_14_3_3_1d"] < 60.0))
      # 1d downtrend, 1d high & overbought
      & ((df["CMF_20_1d"] > -0.30) | (df["AROONU_14_1d"] < 85.0) | (df["ROC_9_1d"] < 100.0))
      # 1d downtrend, 1d high & overbought
      & ((df["CMF_20_1d"] > -0.40) | (df["AROONU_14_1d"] < 85.0) | (df["ROC_9_1d"] < 20.0))
      # 15m still high, 1h overbought
      & ((df["AROONU_14_15m"] < 40.0) | (df["ROC_9_1h"] < 40.0))
      # 15m still high, 4h overbought
      & ((df["AROONU_14_15m"] < 40.0) | (df["ROC_9_4h"] < 80.0))
      # 15m still high, 1h high
      & ((df["AROONU_14_15m"] < 50.0) | (df["AROONU_14_1h"] < 85.0))
      # 15m still high, 4h high & overbought
      & ((df["AROONU_14_15m"] < 50.0) | (df["AROONU_14_4h"] < 70.0) | (df["ROC_9_4h"] < 30.0))
      # 15m still high, 4h downtrend, 1d overbought
      & ((df["AROONU_14_15m"] < 50.0) | (df["ROC_9_4h"] > -20.0) | (df["ROC_9_1d"] < 40.0))
      # 1h still high, 4h & 1d downtrend
      & ((df["AROONU_14_1h"] < 40.0) | (df["ROC_9_4h"] > -20.0) | (df["ROC_9_1d"] > -40.0))
      # 1h high, 4h high, 1h overbought
      & ((df["AROONU_14_1h"] < 70.0) | (df["AROONU_14_4h"] < 100.0) | (df["ROC_9_1h"] < 20.0))
      # 1h & 4h high, 4h overbought
      & ((df["AROONU_14_1h"] < 70.0) | (df["AROONU_14_4h"] < 100.0) | (df["ROC_9_4h"] < 40.0))
      # 1h & 1d high, 1h overbought
      & ((df["AROONU_14_1h"] < 70.0) | (df["AROONU_14_1d"] < 70.0) | (df["ROC_9_1h"] < 20.0))
      # 1h high, 1h & 4h overbought
      & ((df["AROONU_14_1h"] < 70.0) | (df["ROC_9_1h"] < 10.0) | (df["ROC_9_4h"] < 40.0))
      # 1h high, 1d downtrend
      & ((df["AROONU_14_1h"] < 80.0) | (df["ROC_9_1d"] > -40.0))
      # 4h still not low enough, 4h & 1d downtrend
      & ((df["AROONU_14_4h"] < 30.0) | (df["ROC_9_4h"] > -20.0) | (df["ROC_9_1d"] > -25.0))
      # 4h still high, 1d high, 4h downtrend
      & ((df["AROONU_14_4h"] < 50.0) | (df["AROONU_14_1d"] < 100.0) | (df["ROC_9_4h"] > -30.0))
      # 4h high, 1h & 1d downtrend
      & ((df["AROONU_14_4h"] < 70.0) | (df["ROC_9_1h"] > -20.0) | (df["ROC_9_1d"] > -20.0))
      # 4h & 1d high, 1d overbought
      & ((df["AROONU_14_4h"] < 80.0) | (df["AROONU_14_1d"] < 100.0) | (df["ROC_9_1d"] < 50.0))
      # 4h & 1d high, 4h overbought
      & ((df["AROONU_14_4h"] < 100.0) | (df["AROONU_14_1d"] < 100.0) | (df["ROC_9_4h"] < 10.0))
      # 4h high, 1h & 4h overbought
      & ((df["AROONU_14_4h"] < 100.0) | (df["ROC_9_1h"] < 10.0) | (df["ROC_9_4h"] < 40.0))
      # 1d high, 4h & 1d downtrend
      & ((df["AROONU_14_1d"] < 80.0) | (df["ROC_9_4h"] > -20.0) | (df["ROC_9_1d"] > -20.0))
      # 1d high, 1h & 4h downtrend
      & ((df["AROONU_14_1d"] < 85.0) | (df["ROC_9_1h"] > -30.0) | (df["ROC_9_4h"] > -50.0))
      # 1d high, 1h & 1d overbought
      & ((df["AROONU_14_1d"] < 85.0) | (df["ROC_9_1h"] < 20.0) | (df["ROC_9_1d"] < 100.0))
      # 1d high, 1h & 4h down move
      & ((df["AROONU_14_1d"] < 100.0) | (df["ROC_9_1h"] < 25.0) | (df["ROC_9_4h"] < 60.0))
      # 1d high, 4h & 1d overbought
      & ((df["AROONU_14_1d"] < 100.0) | (df["ROC_9_4h"] < 20.0) | (df["ROC_9_1d"] < 30.0))
      # 1h high, 4h & 1d overbought
      & ((df["STOCHRSIk_14_14_3_3_1h"] < 90.0) | (df["ROC_9_4h"] < 20.0) | (df["ROC_9_1d"] < 100.0))
      # 4h still high, 4h & 1d downtrend
      & ((df["STOCHRSIk_14_14_3_3_4h"] < 40.0) | (df["ROC_9_4h"] > -20.0) | (df["ROC_9_1d"] > -40.0))
      # 4h high, 1h & 1d downtrend
      & ((df["STOCHRSIk_14_14_3_3_4h"] < 70.0) | (df["ROC_9_1h"] > -20.0) | (df["ROC_9_1d"] > -20.0))
      # 4h high, 4h & 1d overbought
      & ((df["STOCHRSIk_14_14_3_3_4h"] < 70.0) | (df["ROC_9_4h"] < 20.0) | (df["ROC_9_1d"] < 30.0))
      # 4h high, 1h overbought, 1d downtrend
      & ((df["STOCHRSIk_14_14_3_3_4h"] < 80.0) | (df["ROC_9_1h"] < 40.0) | (df["ROC_9_1d"] > -70.0))
      # 4h high, 4h overbought
      & ((df["STOCHRSIk_14_14_3_3_4h"] < 80.0) | (df["ROC_9_4h"] < 10.0))
      # 4h high, 1h & 4h overbought
      & ((df["STOCHRSIk_14_14_3_3_4h"] < 90.0) | (df["ROC_9_1h"] < 20.0) | (df["ROC_9_4h"] < 50.0))
      # 1d high, 4h & 1d overbought
      & ((df["STOCHRSIk_14_14_3_3_1d"] < 90.0) | (df["ROC_9_4h"] < 40.0) | (df["ROC_9_1d"] < 100.0))
      # 1h & 4h overbought
      & ((df["ROC_9_1h"] < 30.0) | (df["ROC_9_4h"] < 80.0))
      # 1d green with top wick, 4h high
      & ((df["change_pct_1d"] < 30.0) | (df["top_wick_pct_1d"] < 20.0) | (df["AROONU_14_4h"] < 80.0))
      # 1d top wick, 4h down move, 1d overbought
      & ((df["top_wick_pct_1d"] < 50.0) | (df["RSI_3_4h"] > 35.0) | (df["ROC_9_1d"] < 60.0))
      # drop in last 20 days, 4h high
      & ((df["close"] > (df["high_max_20_1d"] * 0.10)) | (df["STOCHRSIk_14_14_3_3_4h"] < 90.0))
      # drop in last 20 days, 1h high, 1d downtrend
      & ((df["close"] > (df["high_max_20_1d"] * 0.20)) | (df["AROONU_14_1h"] < 70.0) | (df["ROC_9_1d"] > -70.0))
      # drop in last 20 days, 1d high, 1d downtrend
      & (
        (df["close"] > (df["high_max_20_1d"] * 0.20))
        | (df["STOCHRSIk_14_14_3_3_1d"] < 70.0)
        | (df["ROC_9_1d"] > -15.0)
      )
    )

    # Logic
    long_entry_logic.append(
      (df["RSI_3"] > 0.0)
      & (df["RSI_3"] < 50.0)
      & (df["AROONU_14"] < 25.0)
      & (df["EMA_26"] > df["EMA_12"])
      & ((df["EMA_26"] - df["EMA_12"]) > (df["open"] * 0.022))
      & ((df["EMA_26"].shift() - df["EMA_12"].shift()) > (df["open"] / 100.0))
    )

def append_long_41(df, long_entry_logic, allowed_empty_candles_288) -> None:
    """Append NFI long condition #41, a quick-mode long entry."""
    long_entry_logic.append(df["num_empty_288"] <= allowed_empty_candles_288)
    # long_entry_logic.append(df["protections_long_global"] == True)

    long_entry_logic.append(
      # 5m & 1d down move, 4h still high
      ((df["RSI_3"] > 15.0) | (df["RSI_3_1d"] > 30.0) | (df["AROONU_14_4h"] < 40.0))
      # 15m & 1h down move, 1d still high
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_1h"] > 3.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 50.0))
      # 15m & 1h down move, 1h still not low enough
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_1h"] > 5.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 30.0))
      # 15m & 1h down move, 15m downtrend
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_1h"] > 10.0) | (df["CMF_20_15m"] > -0.40))
      # 15m & 1h down move, 4h high
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_1h"] > 10.0) | (df["AROONU_14_4h"] < 80.0))
      # 15m & 1h down move, 1h still high
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_1h"] > 10.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 40.0))
      # 15m & 1h down move, 4h high
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_1h"] > 10.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 60.0))
      # 15m & 1h down move, 1d downtrend
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_1h"] > 15.0) | (df["ROC_9_1d"] > -20.0))
      # 15m & 1h down move, 1h still high
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_1h"] > 20.0) | (df["AROONU_14_1h"] < 50.0))
      # 15m & 1h down move, 1h high
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_1h"] > 25.0) | (df["AROONU_14_1h"] < 60.0))
      # 15m & 1h down move, 1d still high
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_1h"] > 30.0) | (df["AROONU_14_1d"] < 50.0))
      # 15m & 1h down move, 1h high
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_1h"] > 30.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 70.0))
      # 15m & 1h down move, 1h still high
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_1h"] > 30.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 50.0))
      # 15m & 1h down move, 1d high
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_1h"] > 30.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 90.0))
      # 15m & 1h down move, 1h high
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_1h"] > 45.0) | (df["AROONU_14_1h"] < 85.0))
      # 15m & 1h down move, 1h high
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_1h"] > 45.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 75.0))
      # 15m & 4h down move, 4h high
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_4h"] > 5.0) | (df["AROONU_14_4h"] < 80.0))
      # 15m & 4h down move, 4h still high
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_4h"] > 40.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 50.0))
      # 15m down move, 15m still high, 1d downtrend
      & ((df["RSI_3_15m"] > 3.0) | (df["AROONU_14_15m"] < 50.0) | (df["ROC_9_1d"] > -20.0))
      # 15m down move, 1h still high, 1d high
      & ((df["RSI_3_15m"] > 3.0) | (df["AROONU_14_1h"] < 50.0) | (df["AROONU_14_1d"] < 70.0))
      # 15m down move, 1h & 4h high
      & ((df["RSI_3_15m"] > 3.0) | (df["AROONU_14_1h"] < 80.0) | (df["AROONU_14_4h"] < 80.0))
      # 15m down move, 4h & 1d high
      & ((df["RSI_3_15m"] > 3.0) | (df["AROONU_14_4h"] < 80.0) | (df["AROONU_14_1d"] < 100.0))
      # 15m down move, 1h & 4h high
      & ((df["RSI_3_15m"] > 3.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 80.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 80.0))
      # 15m down move, 1h high, 4h overbought
      & ((df["RSI_3_15m"] > 3.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 90.0) | (df["ROC_9_4h"] < 10.0))
      # 15m down move, 4h high & overbought
      & ((df["RSI_3_15m"] > 3.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 80.0) | (df["ROC_9_4h"] < 10.0))
      # 15m down move, 4h & 1d downtrend
      & ((df["RSI_3_15m"] > 3.0) | (df["ROC_9_4h"] > -20.0) | (df["ROC_9_1d"] > -20.0))
      # 15m & 1h down move, 1d downtrend
      & ((df["RSI_3_15m"] > 5.0) | (df["RSI_3_1h"] > 5.0) | (df["ROC_9_1d"] > -10.0))
      # 15m & 1h down move, 1d high
      & ((df["RSI_3_15m"] > 5.0) | (df["RSI_3_1h"] > 10.0) | (df["AROONU_14_1d"] < 80.0))
      # 15m & 1h down move, 4h high
      & ((df["RSI_3_15m"] > 5.0) | (df["RSI_3_1h"] > 10.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 80.0))
      # 15m & 1h down move, 1h high
      & ((df["RSI_3_15m"] > 5.0) | (df["RSI_3_1h"] > 30.0) | (df["AROONU_14_1h"] < 70.0))
      # 15m & 1h down move, 4h high
      & ((df["RSI_3_15m"] > 5.0) | (df["RSI_3_1h"] > 30.0) | (df["AROONU_14_4h"] < 70.0))
      # 15m & 4h down move, 1h still high
      & ((df["RSI_3_15m"] > 5.0) | (df["RSI_3_4h"] > 5.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 50.0))
      # 15m & 4h down move, 1d downtrend
      & ((df["RSI_3_15m"] > 5.0) | (df["RSI_3_4h"] > 10.0) | (df["ROC_9_1d"] > -20.0))
      # 15m & 4h down move, 1h high
      & ((df["RSI_3_15m"] > 5.0) | (df["RSI_3_4h"] > 20.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 80.0))
      # 15m & 4h down move, 1d downtrend
      & ((df["RSI_3_15m"] > 5.0) | (df["RSI_3_4h"] > 25.0) | (df["ROC_9_1d"] > -70.0))
      # 15m down move, 1h & 4h high
      & ((df["RSI_3_15m"] > 5.0) | (df["AROONU_14_1h"] < 100.0) | (df["AROONU_14_4h"] < 100.0))
      # 15m down move, 1h still high, 1d downtrend
      & ((df["RSI_3_15m"] > 5.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 50.0) | (df["ROC_9_1d"] > -40.0))
      # 5m down move, 4h high, 1d downtrend
      & ((df["RSI_3_15m"] > 5.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 80.0) | (df["ROC_9_1d"] > -40.0))
      # 15m down move, 1h & 4h overbought
      & ((df["RSI_3_15m"] > 5.0) | (df["ROC_9_1h"] < 25.0) | (df["ROC_9_4h"] < 25.0))
      # 15m down move, 4h & 1d overbought
      & ((df["RSI_3_15m"] > 5.0) | (df["ROC_9_4h"] < 30.0) | (df["ROC_9_1d"] < 100.0))
      # 15m & 1h down move, 1h high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1h"] > 10.0) | (df["AROONU_14_1h"] < 70.0))
      # 15m & 1h down move, 1d high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1h"] > 10.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 70.0))
      # 15m & 1h down move, 1d downtrend
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1h"] > 10.0) | (df["ROC_9_1d"] > -30.0))
      # 15m & 1h down move, 1h high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1h"] > 15.0) | (df["AROONU_14_1h"] < 80.0))
      # 15m & 1h down move, 4h high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1h"] > 15.0) | (df["AROONU_14_4h"] < 100.0))
      # 15m & 1h down move, 4h high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1h"] > 15.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 70.0))
      # 15m & 1h down move, 1h still high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1h"] > 20.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 50.0))
      # 15m & 1h down move, 1d overbought
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1h"] > 25.0) | (df["ROC_9_1d"] < 20.0))
      # 15m & 1h down move, 1d overbought
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1h"] > 30.0) | (df["ROC_9_1d"] < 30.0))
      # 15m & 1h down move, 1h high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1h"] > 40.0) | (df["AROONU_14_1h"] < 90.0))
      # 15m & 1d down move, 4h high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1d"] > 25.0) | (df["AROONU_14_4h"] < 100.0))
      # 15m & 1d down move, 4h high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1d"] > 25.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 80.0))
      # 15m down move, 15m still high, 1d overbought
      & ((df["RSI_3_15m"] > 10.0) | (df["AROONU_14_15m"] < 50.0) | (df["ROC_9_1d"] < 30.0))
      # 15m down move, 15m high
      & ((df["RSI_3_15m"] > 10.0) | (df["AROONU_14_15m"] < 70.0))
      # 15m down move, 1h high, 15m downtrend
      & ((df["RSI_3_15m"] > 10.0) | (df["AROONU_14_1h"] < 80.0) | (df["ROC_9_15m"] > -10.0))
      # 15m down move, 1h high, 1d downtrend
      & ((df["RSI_3_15m"] > 10.0) | (df["AROONU_14_1h"] < 80.0) | (df["ROC_9_1d"] > -30.0))
      # 15m down move, 1h high, 1d overbought
      & ((df["RSI_3_15m"] > 10.0) | (df["AROONU_14_1h"] < 85.0) | (df["ROC_9_1d"] < 40.0))
      # 15m down move, 1h & 1d high
      & ((df["RSI_3_15m"] > 10.0) | (df["AROONU_14_1h"] < 90.0) | (df["AROONU_14_1d"] < 100.0))
      # 15m down move, 1h & 4h high
      & ((df["RSI_3_15m"] > 10.0) | (df["AROONU_14_1h"] < 100.0) | (df["AROONU_14_4h"] < 100.0))
      # 15m down move, 4h high, 1h downtrend
      & ((df["RSI_3_15m"] > 10.0) | (df["AROONU_14_4h"] < 85.0) | (df["ROC_9_1h"] > -25.0))
      # 15m down move, 4h & 1d high
      & ((df["RSI_3_15m"] > 10.0) | (df["AROONU_14_4h"] < 90.0) | (df["AROONU_14_1d"] < 100.0))
      # 15m down move, 4h high, 15m downtrend
      & ((df["RSI_3_15m"] > 10.0) | (df["AROONU_14_4h"] < 100.00) | (df["ROC_9_15m"] > -30.0))
      # 15m down move, 1h high & overbought
      & ((df["RSI_3_15m"] > 10.0) | (df["AROONU_14_1d"] < 100.0) | (df["ROC_9_1d"] < 60.0))
      # 15m down move, 1d high, 1d downtrend
      & ((df["RSI_3_15m"] > 10.0) | (df["AROONU_14_1d"] < 85.0) | (df["CMF_20_1d"] > -0.40))
      # 15m down move, 1h high, 15m downtrend
      & ((df["RSI_3_15m"] > 10.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 80.0) | (df["ROC_9_15m"] > -10.0))
      # 15m down move, 1h high, 1d downtrend
      & ((df["RSI_3_15m"] > 10.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 90.0) | (df["ROC_9_1d"] > -30.0))
      # 15m down move, 1h high, 1d overbought
      & ((df["RSI_3_15m"] > 10.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 90.0) | (df["ROC_9_1d"] < 30.0))
      # 15m down move, 4h high & overbought
      & ((df["RSI_3_15m"] > 10.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 90.0) | (df["ROC_9_4h"] < 20.0))
      # 15m & 1h down move, 1d overbought
      & ((df["RSI_3_15m"] > 15.0) | (df["RSI_3_1h"] > 15.0) | (df["ROC_9_1d"] < 30.0))
      # 15m & 1h down move, 1d high
      & ((df["RSI_3_15m"] > 15.0) | (df["RSI_3_1h"] > 20.0) | (df["AROONU_14_1d"] < 90.0))
      # 15m & 1h down move, 1h high
      & ((df["RSI_3_15m"] > 15.0) | (df["RSI_3_1h"] > 35.0) | (df["AROONU_14_1h"] < 80.0))
      # 15m & 1d down move, 4h high
      & ((df["RSI_3_15m"] > 15.0) | (df["RSI_3_1d"] > 20.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 90.0))
      # 15m & 1d down move, 4h high
      & ((df["RSI_3_15m"] > 15.0) | (df["RSI_3_1d"] > 25.0) | (df["AROONU_14_4h"] < 100.0))
      # 15m & 1d down move, 1d high
      & ((df["RSI_3_15m"] > 15.0) | (df["RSI_3_1d"] > 50.0) | (df["AROONU_14_1d"] < 80.0))
      # 15m down move, 15m still high, 1h high
      & ((df["RSI_3_15m"] > 15.0) | (df["AROONU_14_15m"] < 50.0) | (df["AROONU_14_1h"] < 90.0))
      # 15m down move, 15m still high, 1h high
      & ((df["RSI_3_15m"] > 15.0) | (df["AROONU_14_15m"] < 50.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 80.0))
      # 15m down move, 1h & 4h high
      & ((df["RSI_3_15m"] > 15.0) | (df["AROONU_14_1h"] < 80.0) | (df["AROONU_14_4h"] < 100.0))
      # 15m down move, 4h high, 4h downtrend
      & ((df["RSI_3_15m"] > 15.0) | (df["AROONU_14_4h"] < 60.0) | (df["ROC_9_4h"] > -20.0))
      # 15m down move, 4h & 1d high
      & ((df["RSI_3_15m"] > 15.0) | (df["AROONU_14_4h"] < 80.0) | (df["AROONU_14_1d"] < 100.0))
      # 15m down move, 1h high, 4h downtrend
      & ((df["RSI_3_15m"] > 15.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 70.0) | (df["ROC_9_4h"] > -30.0))
      # 15m down move, 4h high & overbought
      & ((df["RSI_3_15m"] > 15.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 80.0) | (df["ROC_9_4h"] < 10.0))
      # 15m down move, 4h high, 1d downtrend
      & ((df["RSI_3_15m"] > 15.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 80.0) | (df["ROC_9_1d"] > -50.0))
      # 15m down move, 1d high, 4h overbought
      & ((df["RSI_3_15m"] > 15.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 90.0) | (df["ROC_9_4h"] < 40.0))
      # 15m down move, 1h downtrend, 4h overbought
      & ((df["RSI_3_15m"] > 15.0) | (df["ROC_9_1h"] > -20.0) | (df["ROC_9_4h"] < 80.0))
      # 15m down move, 4h & 1d downtrend
      & ((df["RSI_3_15m"] > 15.0) | (df["ROC_9_4h"] > -10.0) | (df["ROC_9_1d"] > -40.0))
      # 15m & 1h down move, 1h high
      & ((df["RSI_3_15m"] > 20.0) | (df["RSI_3_1h"] > 20.0) | (df["AROONU_14_1h"] < 70.0))
      # 15m & 1h down move, 1d overbought
      & ((df["RSI_3_15m"] > 20.0) | (df["RSI_3_1h"] > 20.0) | (df["ROC_9_1d"] < 50.0))
      # 15m & 1h down move, 1d high
      & ((df["RSI_3_15m"] > 20.0) | (df["RSI_3_1h"] > 25.0) | (df["AROONU_14_1d"] < 100.0))
      # 15m &4h down move, 4h still high
      & ((df["RSI_3_15m"] > 20.0) | (df["RSI_3_4h"] > 20.0) | (df["AROONU_14_4h"] < 50.0))
      # 15m & 4h down move, 1d overbought
      & ((df["RSI_3_15m"] > 20.0) | (df["RSI_3_4h"] > 30.0) | (df["ROC_9_1d"] < 50.0))
      # 15m down move, 15m high, 1d overbought
      & ((df["RSI_3_15m"] > 20.0) | (df["AROONU_14_15m"] < 70.0) | (df["ROC_9_1d"] < 40.0))
      # 15m down move, 1h high, 4h downtrend
      & ((df["RSI_3_15m"] > 20.0) | (df["AROONU_14_1h"] < 80.0) | (df["ROC_9_4h"] > -15.0))
      # 15m down move, 1h high & overbought
      & ((df["RSI_3_15m"] > 20.0) | (df["AROONU_14_1h"] < 100.0) | (df["ROC_9_1h"] < 50.0))
      # 15m down move, 4h high & overbought
      & ((df["RSI_3_15m"] > 20.0) | (df["AROONU_14_4h"] < 70.0) | (df["ROC_9_4h"] < 20.0))
      # 15m down move, 4h high, 1d overbought
      & ((df["RSI_3_15m"] > 20.0) | (df["AROONU_14_4h"] < 80.0) | (df["ROC_9_1d"] < 60.0))
      # 15m & 4h down move, 4h high
      & ((df["RSI_3_15m"] > 25.0) | (df["RSI_3_4h"] > 25.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 60.0))
      # 15m & 1d down move, 1h high
      & ((df["RSI_3_15m"] > 25.0) | (df["RSI_3_1d"] > 25.0) | (df["AROONU_14_1h"] < 90.0))
      # 15m down move, 15m high, 1h high
      & ((df["RSI_3_15m"] > 30.0) | (df["AROONU_14_15m"] < 60.0) | (df["AROONU_14_1h"] < 90.0))
      # 15m down move, 15m high, 4h downtrend
      & ((df["RSI_3_15m"] > 25.0) | (df["AROONU_14_15m"] < 60.0) | (df["ROC_9_4h"] > -20.0))
      # 15m down move, 1h high, 4h overbought
      & ((df["RSI_3_15m"] > 25.0) | (df["AROONU_14_1h"] < 90.0) | (df["ROC_9_4h"] < 30.0))
      # 15m down move, 1h high, 4h overbought
      & ((df["RSI_3_15m"] > 25.0) | (df["AROONU_14_1h"] < 100.0) | (df["ROC_9_4h"] < 15.0))
      # 15m down move, 1h high, 1d overbought
      & ((df["RSI_3_15m"] > 25.0) | (df["AROONU_14_1h"] < 100.0) | (df["ROC_9_1d"] < 20.0))
      # 15m down move, 1h & 4h high
      & ((df["RSI_3_15m"] > 30.0) | (df["AROONU_14_1h"] < 90.0) | (df["AROONU_14_4h"] < 90.0))
      # 1h & 4h down move, 1d still high
      & ((df["RSI_3_1h"] > 3.0) | (df["RSI_3_4h"] > 3.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 50.0))
      # 1h & 4h down move, 1h still high
      & ((df["RSI_3_1h"] > 3.0) | (df["RSI_3_4h"] > 25.0) | (df["AROONU_14_1h"] < 40.0))
      # 1h & 4h down move, 4h high
      & ((df["RSI_3_1h"] > 3.0) | (df["RSI_3_4h"] > 45.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 70.0))
      # 1h down move, 15m & 1h downtrend
      & ((df["RSI_3_1h"] > 3.0) | (df["CMF_20_15m"] > -0.30) | (df["CMF_20_1h"] > -0.30))
      # 1h down move, 1h still high, 1h downtrend
      & ((df["RSI_3_1h"] > 3.0) | (df["AROONU_14_1h"] < 50.0) | (df["ROC_9_1h"] > -20.0))
      # 1h down move, 1h high
      & ((df["RSI_3_1h"] > 3.0) | (df["AROONU_14_1h"] < 70.0))
      # 1h down move, 4h high
      & ((df["RSI_3_1h"] > 3.0) | (df["AROONU_14_4h"] < 70.0))
      # 1h down move, 1d high
      & ((df["RSI_3_1h"] > 3.0) | (df["AROONU_14_1d"] < 70.0))
      # 1h down move, 4h still high, 1d downtrend
      & ((df["RSI_3_1h"] > 3.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 50.0) | (df["ROC_9_1h"] > -20.0))
      # 1h down move, 1d high & overbought
      & ((df["RSI_3_1h"] > 3.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 60.0) | (df["ROC_9_1d"] < 20.0))
      # 1h & 4h & 1d down move
      & ((df["RSI_3_1h"] > 5.0) | (df["RSI_3_4h"] > 10.0) | (df["RSI_3_1d"] > 20.0))
      # 1h & 4h down move, 1d overbought
      & ((df["RSI_3_1h"] > 5.0) | (df["RSI_3_4h"] > 10.0) | (df["ROC_9_1d"] < 100.0))
      # 1h & 4h down move, 4h still not low enough
      & ((df["RSI_3_1h"] > 5.0) | (df["RSI_3_4h"] > 15.0) | (df["AROONU_14_4h"] < 20.0))
      # 1h & 4h down move, 4h still high
      & ((df["RSI_3_1h"] > 5.0) | (df["RSI_3_4h"] > 30.0) | (df["RSI_14_4h"] < 40.0))
      # 1h & 4h down move, 1h downtrend
      & ((df["RSI_3_1h"] > 5.0) | (df["RSI_3_4h"] > 30.0) | (df["CMF_20_1h"] > -0.30))
      # 1h & 4h down move, 4h high
      & ((df["RSI_3_1h"] > 5.0) | (df["RSI_3_4h"] > 50.0) | (df["AROONU_14_4h"] < 70.0))
      # 1h & 1d down move, 1h still high
      & ((df["RSI_3_1h"] > 5.0) | (df["RSI_3_1d"] > 10.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 50.0))
      # 1h down move, 1d high, 1h downtrend
      & ((df["RSI_3_1h"] > 5.0) | (df["AROONU_14_1d"] < 85.0) | (df["ROC_9_1h"] > -50.0))
      # 1h down move, 1d high, 4h downtrend
      & ((df["RSI_3_1h"] > 5.0) | (df["AROONU_14_1d"] < 90.0) | (df["ROC_9_4h"] > -30.0))
      # 1h down move, 1d high, 1d downtrend
      & ((df["RSI_3_1h"] > 5.0) | (df["AROONU_14_1d"] < 100.0) | (df["ROC_9_1d"] > -20.0))
      # 1h down move, 1d high & overbought
      & ((df["RSI_3_1h"] > 5.0) | (df["AROONU_14_1d"] < 100.0) | (df["ROC_9_1d"] < 20.0))
      # 1h down move, 4h still high, 1d downtrend
      & ((df["RSI_3_1h"] > 5.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 50.0) | (df["ROC_9_1d"] > -50.0))
      # 1h down move, 4h & 1d downtrend
      & ((df["RSI_3_1h"] > 5.0) | (df["ROC_9_4h"] > -25.0) | (df["ROC_9_1d"] > -50.0))
      # 1h & 4h & 1d down move
      & ((df["RSI_3_1h"] > 10.0) | (df["RSI_3_4h"] > 10.0) | (df["RSI_3_1d"] > 15.0))
      # 1h & 4h down move, 1h high
      & ((df["RSI_3_1h"] > 10.0) | (df["RSI_3_4h"] > 10.0) | (df["AROONU_14_1h"] < 80.0))
      # 1h & 4h down move, 1d high
      & ((df["RSI_3_1h"] > 10.0) | (df["RSI_3_4h"] > 10.0) | (df["AROONU_14_1d"] < 80.0))
      # 1h & 4h down move, 4h still high
      & ((df["RSI_3_1h"] > 10.0) | (df["RSI_3_4h"] > 10.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 50.0))
      # 1h & 4h down move, 1d still not low enough
      & ((df["RSI_3_1h"] > 10.0) | (df["RSI_3_4h"] > 10.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 20.0))
      # 1h & 4h down move, 4h downtrend
      & ((df["RSI_3_1h"] > 10.0) | (df["RSI_3_4h"] > 10.0) | (df["ROC_9_4h"] > -35.0))
      # 1h & 4h down move, 1d downtrend
      & ((df["RSI_3_1h"] > 10.0) | (df["RSI_3_4h"] > 10.0) | (df["ROC_9_1d"] > -20.0))
      # 1h & 4h down move, 15m downtrend
      & ((df["RSI_3_1h"] > 10.0) | (df["RSI_3_4h"] > 15.0) | (df["ROC_9_15m"] > -20.0))
      # 1h & 4h down move, 4h still high
      & ((df["RSI_3_1h"] > 10.0) | (df["RSI_3_4h"] > 20.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 50.0))
      # 1h & 4h down move, 1d downtrend
      & ((df["RSI_3_1h"] > 10.0) | (df["RSI_3_4h"] > 20.0) | (df["ROC_9_1d"] > -30.0))
      # 1h & 4h down move, 4h high
      & ((df["RSI_3_1h"] > 10.0) | (df["RSI_3_4h"] > 25.0) | (df["AROONU_14_4h"] < 90.0))
      # 1h & 1d down move, 1d downtrend
      & ((df["RSI_3_1h"] > 10.0) | (df["RSI_3_1d"] > 10.0) | (df["ROC_9_1d"] > -30.0))
      # 1h & 1d down move, 4h still high
      & ((df["RSI_3_1h"] > 10.0) | (df["RSI_3_1d"] > 10.0) | (df["AROONU_14_4h"] < 40.0))
      # 1h & 1d down move, 4h high
      & ((df["RSI_3_1h"] > 10.0) | (df["RSI_3_1d"] > 15.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 70.0))
      # 1h & 1d down move, 1h still not low enough
      & ((df["RSI_3_1h"] > 10.0) | (df["RSI_3_1d"] > 20.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 20.0))
      # 1h & 1d down move, 1h high
      & ((df["RSI_3_1h"] > 10.0) | (df["RSI_3_1d"] > 25.0) | (df["AROONU_14_1h"] < 70.0))
      # 1h & 1d down move, 1h downtrend
      & ((df["RSI_3_1h"] > 10.0) | (df["RSI_3_1d"] > 30.0) | (df["CMF_20_1h"] > -0.40))
      # 1h down move, 1d downtrend, 4h high
      & ((df["RSI_3_1h"] > 10.0) | (df["CMF_20_1d"] > -0.30) | (df["STOCHRSIk_14_14_3_3_4h"] < 90.0))
      # 1h down move, 1h still high, 4h overbought
      & ((df["RSI_3_1h"] > 10.0) | (df["AROONU_14_1h"] < 50.0) | (df["ROC_9_4h"] < 20.0))
      # 1h down move, 1h & 4h high
      & ((df["RSI_3_1h"] > 10.0) | (df["AROONU_14_1h"] < 60.0) | (df["AROONU_14_4h"] < 60.0))
      # 1h down move, 1h high, 1d high
      & ((df["RSI_3_1h"] > 10.0) | (df["AROONU_14_1h"] < 60.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 90.0))
      # 1h down move, 1d overbought
      & ((df["RSI_3_1h"] > 10.0) | (df["ROC_9_1d"] < 50.0))
      # 1h & 4h down move, 1h downtrend
      & ((df["RSI_3_1h"] > 15.0) | (df["RSI_3_4h"] > 15.0) | (df["ROC_9_1h"] > -15.0))
      # 1h & 4h down move, 4h downtrend
      & ((df["RSI_3_1h"] > 15.0) | (df["RSI_3_4h"] > 15.0) | (df["ROC_9_4h"] > -25.0))
      # 1h & 4h down move, 1d downtrend
      & ((df["RSI_3_1h"] > 15.0) | (df["RSI_3_4h"] > 15.0) | (df["ROC_9_1d"] > -70.0))
      # 1h & 4h down move, 4h still high
      & ((df["RSI_3_1h"] > 15.0) | (df["RSI_3_4h"] > 20.0) | (df["RSI_14_4h"] < 40.0))
      # 1h & 4h down move, 4h high
      & ((df["RSI_3_1h"] > 15.0) | (df["RSI_3_4h"] > 20.0) | (df["AROONU_14_4h"] < 70.0))
      # 1h & 4h down move, 1d high
      & ((df["RSI_3_1h"] > 15.0) | (df["RSI_3_4h"] > 20.0) | (df["AROONU_14_1d"] < 100.0))
      # 1h & 1d down move, 1h still high
      & ((df["RSI_3_1h"] > 15.0) | (df["RSI_3_1d"] > 30.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 40.0))
      # 1h & 1d down move, 1h high
      & ((df["RSI_3_1h"] > 15.0) | (df["RSI_3_1d"] > 30.0) | (df["AROONU_14_1h"] < 80.0))
      # 1h down move, 1h downtrend, 1h still high
      & ((df["RSI_3_1h"] > 15.0) | (df["CMF_20_1h"] > -0.30) | (df["STOCHRSIk_14_14_3_3_1h"] < 40.0))
      # 1h down move, 1d downtrend, 1d high
      & ((df["RSI_3_1h"] > 15.0) | (df["CMF_20_1d"] > -0.30) | (df["STOCHRSIk_14_14_3_3_1d"] < 80.0))
      # 1h down move, 1h & 1d high
      & ((df["RSI_3_1h"] > 15.0) | (df["AROONU_14_1h"] < 70.0) | (df["AROONU_14_1d"] < 90.0))
      # 1h down move, 1h high, 1d overbought
      & ((df["RSI_3_1h"] > 15.0) | (df["AROONU_14_1h"] < 70.0) | (df["ROC_9_1d"] < 40.0))
      # 1h down move, 1h high, 1h downtrend
      & ((df["RSI_3_1h"] > 15.0) | (df["AROONU_14_1h"] < 80.0) | (df["CMF_20_1h"] > -0.25))
      # 1h down move, 1h high, 4h downtrend
      & ((df["RSI_3_1h"] > 15.0) | (df["AROONU_14_1h"] < 80.0) | (df["ROC_9_4h"] > -30.0))
      # 1h down move, 4h still high, 1d overbought
      & ((df["RSI_3_1h"] > 15.0) | (df["AROONU_14_4h"] < 50.0) | (df["ROC_9_1d"] < 60.0))
      # 1h down move, 4h high, 15m downtrend
      & ((df["RSI_3_1h"] > 15.0) | (df["AROONU_14_4h"] < 85.0) | (df["ROC_9_15m"] > -15.0))
      # 1h down move, 4h high, 1h downtrend
      & ((df["RSI_3_1h"] > 15.0) | (df["AROONU_14_4h"] < 85.0) | (df["ROC_9_1h"] > -30.0))
      # 1h down move, 1d high, 4h overbought
      & ((df["RSI_3_1h"] > 15.0) | (df["AROONU_14_1d"] < 100.0) | (df["ROC_9_4h"] < 10.0))
      # 1h down move, 4h still not low enough, 1d downtrend
      & ((df["RSI_3_1h"] > 15.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 30.0) | (df["ROC_9_1d"] > -30.0))
      # 1h down move, 4h high & overbought
      & ((df["RSI_3_1h"] > 15.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 80.0) | (df["ROC_9_4h"] < 100.0))
      # 1h down move, 1h downtrend, 1d overbought
      & ((df["RSI_3_1h"] > 15.0) | (df["ROC_9_1h"] > -30.0) | (df["ROC_9_1d"] < 35.0))
      # 1h down move, 4h downtrend, 1d overbought
      & ((df["RSI_3_1h"] > 15.0) | (df["ROC_9_4h"] > -25.0) | (df["ROC_9_1d"] < 100.0))
      # 1h & 4h down move, 1d high
      & ((df["RSI_3_1h"] > 20.0) | (df["RSI_3_4h"] > 20.0) | (df["AROONU_14_1d"] < 80.0))
      # 1h & 4h down move, 4h high
      & ((df["RSI_3_1h"] > 20.0) | (df["RSI_3_4h"] > 50.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 70.0))
      # 1h & 1d down move, 4h high
      & ((df["RSI_3_1h"] > 20.0) | (df["RSI_3_1d"] > 20.0) | (df["AROONU_14_4h"] < 90.0))
      # 1h & 1d down move, 1h high
      & ((df["RSI_3_1h"] > 20.0) | (df["RSI_3_1d"] > 25.0) | (df["AROONU_14_1h"] < 70.0))
      # 1h & 1d down move, 4h overbought
      & ((df["RSI_3_1h"] > 20.0) | (df["RSI_3_1d"] > 30.0) | (df["ROC_9_4h"] < 30.0))
      # 1h down move, 1h still high, 4h high
      & ((df["RSI_3_1h"] > 20.0) | (df["AROONU_14_1h"] < 50.0) | (df["AROONU_14_4h"] < 90.0))
      # 1h down move, 1h high, 1d overbought
      & ((df["RSI_3_1h"] > 20.0) | (df["AROONU_14_1h"] < 70.0) | (df["ROC_9_1d"] < 100.0))
      # 1h down move, 1d high & overbought
      & ((df["RSI_3_1h"] > 20.0) | (df["AROONU_14_1d"] < 100.0) | (df["ROC_9_1d"] < 60.0))
      # 1h down move, 1h high, 4h overbought
      & ((df["RSI_3_1h"] > 20.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 70.0) | (df["ROC_9_4h"] < 10.0))
      # 1h down move, 1d high, 1d downtrend
      & ((df["RSI_3_1h"] > 20.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 80.0) | (df["ROC_9_1d"] > -50.0))
      # 1h down move, 1d high & overbought
      & ((df["RSI_3_1h"] > 20.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 90.0) | (df["ROC_9_1d"] < 40.0))
      # 1h down move, 1h & 4h overbought
      & ((df["RSI_3_1h"] > 20.0) | (df["ROC_9_1h"] < 20.0) | (df["ROC_9_4h"] < 40.0))
      # 1h down move, 4h & 1d downtrend
      & ((df["RSI_3_1h"] > 20.0) | (df["ROC_9_4h"] > -30.0) | (df["ROC_9_1d"] > -40.0))
      # 1h & 4h down move, 1d overbought
      & ((df["RSI_3_1h"] > 25.0) | (df["RSI_3_4h"] > 40.0) | (df["ROC_9_1d"] < 100.0))
      # 1h down move, 15m still high, 1h high
      & ((df["RSI_3_1h"] > 25.0) | (df["AROONU_14_15m"] < 50.0) | (df["AROONU_14_1h"] < 90.0))
      # 1h down move, 1h high, 1d overbought
      & ((df["RSI_3_1h"] > 25.0) | (df["AROONU_14_1h"] < 70.0) | (df["ROC_9_1d"] < 200.0))
      # 1h down move, 1h & 1d high
      & ((df["RSI_3_1h"] > 25.0) | (df["AROONU_14_1h"] < 70.0) | (df["AROONU_14_1d"] < 90.0))
      # 1h down move, 1h high, 4h overbought
      & ((df["RSI_3_1h"] > 25.0) | (df["AROONU_14_1h"] < 80.0) | (df["ROC_9_4h"] < 20.0))
      # 1h down move, 1h high, 1d overbought
      & ((df["RSI_3_1h"] > 25.0) | (df["AROONU_14_1h"] < 85.0) | (df["ROC_9_1d"] < 50.0))
      # 1h down move, 4h high
      & ((df["RSI_3_1h"] > 25.0) | (df["AROONU_14_4h"] < 90.0))
      # 1h down move, 1h still high, 1d overbought
      & ((df["RSI_3_1h"] > 25.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 50.0) | (df["ROC_9_1d"] < 40.0))
      # 1h down move, 4h high, 1d downtrend
      & ((df["RSI_3_1h"] > 25.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 80.0) | (df["ROC_9_1d"] > -40.0))
      # 1h down move, 15m downtrend, 4h overbought
      & ((df["RSI_3_1h"] > 25.0) | (df["ROC_9_15m"] > -25.0) | (df["ROC_9_4h"] < 30.0))
      # 1h down move, 1h & 1d downtrend
      & ((df["RSI_3_1h"] > 25.0) | (df["ROC_9_1h"] > -50.0) | (df["ROC_9_1d"] > -50.0))
      # 1h down move, 1h downtrend, 4h overbought
      & ((df["RSI_3_1h"] > 25.0) | (df["ROC_9_1h"] > -25.0) | (df["ROC_9_4h"] < 50.0))
      # 1h down move, 1h & 4h overbought
      & ((df["RSI_3_1h"] > 25.0) | (df["ROC_9_1h"] < 30.0) | (df["ROC_9_4h"] < 100.0))
      # 1h & 4h down move, 1h high
      & ((df["RSI_3_1h"] > 30.0) | (df["RSI_3_4h"] > 30.0) | (df["AROONU_14_1h"] < 90.0))
      # 1h down move, 1h downtrend, 1h high
      & ((df["RSI_3_1h"] > 30.0) | (df["CMF_20_1h"] > -0.25) | (df["STOCHRSIk_14_14_3_3_1h"] < 70.0))
      # 1h down move, 4h downtrend, 4h high
      & ((df["RSI_3_1h"] > 30.0) | (df["CMF_20_4h"] > -0.50) | (df["AROONU_14_4h"] < 100.0))
      # 1h down move, 1h high & overbought
      & ((df["RSI_3_1h"] > 30.0) | (df["AROONU_14_1h"] < 70.0) | (df["ROC_9_1h"] < 10.0))
      # 1h down move, 1h high, 1d downtrend
      & ((df["RSI_3_1h"] > 30.0) | (df["AROONU_14_1h"] < 70.0) | (df["ROC_9_1d"] > -60.0))
      # 1h down move, 4h high, 1h overbought
      & ((df["RSI_3_1h"] > 30.0) | (df["AROONU_14_4h"] < 80.0) | (df["ROC_9_1h"] < 50.0))
      # 1h down move, 4h high, 1d downtrend
      & ((df["RSI_3_1h"] > 30.0) | (df["AROONU_14_4h"] < 90.0) | (df["ROC_9_1d"] > -30.0))
      # 1h down move, 4h high, 1d overbought
      & ((df["RSI_3_1h"] > 30.0) | (df["AROONU_14_4h"] < 100.0) | (df["ROC_9_1d"] < 20.0))
      # 1h down move, 4h & 1d overbought
      & ((df["RSI_3_1h"] > 30.0) | (df["ROC_9_4h"] < 10.0) | (df["ROC_9_1d"] < 50.0))
      # 1h down move, 15m & 1h high
      & ((df["RSI_3_1h"] > 35.0) | (df["AROONU_14_15m"] < 70.0) | (df["AROONU_14_1h"] < 100.0))
      # 1h down move, 1h high, 4h downtrend
      & ((df["RSI_3_1h"] > 35.0) | (df["AROONU_14_1h"] < 70.0) | (df["ROC_9_4h"] > -40.0))
      # 1h down move, 1h & 4h high
      & ((df["RSI_3_1h"] > 35.0) | (df["AROONU_14_1h"] < 80.0) | (df["AROONU_14_4h"] < 100.0))
      # 1h down move, 1h high, 1d downtrend
      & ((df["RSI_3_1h"] > 35.0) | (df["AROONU_14_1h"] < 80.0) | (df["ROC_9_1d"] > -40.0))
      # 1h down move, 1h high, 4h overbought
      & ((df["RSI_3_1h"] > 35.0) | (df["AROONU_14_1h"] < 90.0) | (df["ROC_9_4h"] < 10.0))
      # 1h down move, 4h high, 1d overbought
      & ((df["RSI_3_1h"] > 35.0) | (df["AROONU_14_4h"] < 70.0) | (df["ROC_9_1d"] < 200.0))
      # 1h down move, 4h high & overbought
      & ((df["RSI_3_1h"] > 35.0) | (df["AROONU_14_4h"] < 100.0) | (df["ROC_9_4h"] < 20.0))
      # 1h down move, 4h high & overbought
      & ((df["RSI_3_1h"] > 35.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 80.0) | (df["ROC_9_4h"] < 30.0))
      # 1h down move, 1h downtrend, 4h overbought
      & ((df["RSI_3_1h"] > 35.0) | (df["ROC_9_1h"] > -30.0) | (df["ROC_9_4h"] < 100.0))
      # 1h down move, 4h & 1d overbought
      & ((df["RSI_3_1h"] > 35.0) | (df["ROC_9_4h"] < 20.0) | (df["ROC_9_1d"] < 70.0))
      # 1h down move, 1h & 4h high
      & ((df["RSI_3_1h"] > 40.0) | (df["AROONU_14_1h"] < 70.0) | (df["AROONU_14_4h"] < 100.0))
      # 1h down move, 1h high & overbought
      & ((df["RSI_3_1h"] > 40.0) | (df["AROONU_14_1h"] < 80.0) | (df["ROC_9_1h"] < 10.0))
      # 1h down move, 1h high, 1d high
      & ((df["RSI_3_1h"] > 40.0) | (df["AROONU_14_1h"] < 85.0) | (df["ROC_9_1d"] < 80.0))
      # 1h down move, 1h high, 15m downtrend
      & ((df["RSI_3_1h"] > 40.0) | (df["AROONU_14_1h"] < 90.0) | (df["ROC_9_15m"] > -10.0))
      # 1h down move, 1h  high & overbought
      & ((df["RSI_3_1h"] > 40.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 80.0) | (df["ROC_9_1h"] < 10.0))
      # 1h down move, 4h & 1d overbought
      & ((df["RSI_3_1h"] > 40.0) | (df["ROC_9_4h"] < 20.0) | (df["ROC_9_1d"] < 100.0))
      # 1h down move, 4h & 1d overbought
      & ((df["RSI_3_1h"] > 40.0) | (df["ROC_9_4h"] < 30.0) | (df["ROC_9_1d"] < 40.0))
      # 1h down move, 1h high, 1d overbought
      & ((df["RSI_3_1h"] > 45.0) | (df["AROONU_14_1h"] < 100.0) | (df["ROC_9_1d"] < 200.0))
      # 1h down move, 4h high & overbought
      & ((df["RSI_3_1h"] > 45.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 80.0) | (df["ROC_9_4h"] < 100.0))
      # 1h down move, 1h high, 1d downtrend
      & ((df["RSI_3_1h"] > 50.0) | (df["AROONU_14_1h"] < 60.0) | (df["ROC_9_1d"] > -70.0))
      # 1h down move, 1h high, 1d overbought
      & ((df["RSI_3_1h"] > 50.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 70.0) | (df["ROC_9_1d"] < 100.0))
      # 1h down move, 4h high, 1d downtrend
      & ((df["RSI_3_1h"] > 50.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 60.0) | (df["ROC_9_1d"] > -60.0))
      # 1h down move, 1h high
      & ((df["RSI_3_1h"] > 60.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 80.0))
      # 1h down move, 1h overbought
      & ((df["RSI_3_1h"] > 60.0) | (df["ROC_9_1h"] < 30.0))
      # 1h down move, 4h & 1d overbought
      & ((df["RSI_3_1h"] > 60.0) | (df["ROC_9_4h"] < 30.0) | (df["ROC_9_1d"] < 60.0))
      # 4h & 1d down move, 1d still not low enough
      & ((df["RSI_3_4h"] > 3.0) | (df["RSI_3_1d"] > 30.0) | (df["AROONU_14_1d"] < 30.0))
      # 4h down move, 4h high, 1h downtrend
      & ((df["RSI_3_4h"] > 3.0) | (df["AROONU_14_4h"] < 70.0) | (df["ROC_9_1h"] > -40.0))
      # 4h down move, 1h still high, 4h downtrend
      & ((df["RSI_3_4h"] > 3.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 50.0) | (df["ROC_9_4h"] > -30.0))
      # 4h & 1d down move, 1d still high
      & ((df["RSI_3_4h"] > 5.0) | (df["RSI_3_1d"] > 20.0) | (df["AROONU_14_1d"] < 50.0))
      # 4h down move, 15m still high, 1d downtrend
      & ((df["RSI_3_4h"] > 5.0) | (df["AROONU_14_15m"] < 50.0) | (df["ROC_9_1d"] > -30.0))
      # 4h & 1d down move, 1d downtrend
      & ((df["RSI_3_4h"] > 10.0) | (df["RSI_3_1d"] > 25.0) | (df["ROC_9_1d"] > -50.0))
      # 4h down move, 1d high & overbought
      & ((df["RSI_3_4h"] > 10.0) | (df["AROONU_14_1d"] < 80.0) | (df["ROC_9_1d"] < 80.0))
      # 4h down move, 1h & 4h downtrend
      & ((df["RSI_3_4h"] > 10.0) | (df["ROC_9_1h"] > -30.0) | (df["ROC_9_4h"] > -30.0))
      # 4h down move, 1d high & overbought
      & ((df["RSI_3_4h"] > 10.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 70.0) | (df["ROC_9_1d"] < 35.0))
      # 4h down move, 4h & 1d downtrend
      & ((df["RSI_3_4h"] > 10.0) | (df["ROC_9_4h"] > -15.0) | (df["ROC_9_1d"] > -35.0))
      # 4h down move, 4h still high, 1d overbought
      & ((df["RSI_3_4h"] > 15.0) | (df["AROONU_14_4h"] < 40.0) | (df["ROC_9_1d"] < 40.0))
      # 4h down move, 1h still not low enough, 1d downtrend
      & ((df["RSI_3_4h"] > 15.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 20.0) | (df["ROC_9_1d"] > -20.0))
      # 4h & 1d down move, 1d high
      & ((df["RSI_3_4h"] > 20.0) | (df["RSI_3_1d"] > 20.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 70.0))
      # 4h down move, 1d high & overbought
      & ((df["RSI_3_4h"] > 20.0) | (df["AROONU_14_1d"] < 80.0) | (df["ROC_9_1d"] < 200.0))
      # 4h down move, 4h & 1d downtrend
      & ((df["RSI_3_4h"] > 20.0) | (df["ROC_9_4h"] > -20.0) | (df["ROC_9_1d"] > -30.0))
      # 4h down move, 15m high, 1d overbought
      & ((df["RSI_3_4h"] > 25.0) | (df["AROONU_14_15m"] < 70.0) | (df["ROC_9_1d"] < 100.0))
      # 4h down move, 4h high
      & ((df["RSI_3_4h"] > 25.0) | (df["AROONU_14_4h"] < 80.0))
      # 4h down move, 1d high, 1h downtrend
      & ((df["RSI_3_4h"] > 25.0) | (df["AROONU_14_1d"] < 100.0) | (df["ROC_9_1h"] > -40.0))
      # 4h down move, 4h still high, 1d downtrend
      & ((df["RSI_3_4h"] > 30.0) | (df["AROONU_14_4h"] < 50.0) | (df["ROC_9_1d"] > -40.0))
      # 4h down move, 4h still high, 1d overbought
      & ((df["RSI_3_4h"] > 30.0) | (df["AROONU_14_4h"] < 50.0) | (df["ROC_9_1d"] < 200.0))
      # 4h down move, 4h still not low enough, 1d overbought
      & ((df["RSI_3_4h"] > 30.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 20.0) | (df["ROC_9_1d"] < 60.0))
      # 4h down move, 1d high, 1d downtrend
      & ((df["RSI_3_4h"] > 35.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 60.0) | (df["ROC_9_1d"] > -30.0))
      # 4h down move, 1h high, 1d overbought
      & ((df["RSI_3_4h"] > 45.0) | (df["AROONU_14_1h"] < 85.0) | (df["ROC_9_1d"] < 50.0))
      # 4h down move, 1d high, 1d downtrend
      & ((df["RSI_3_4h"] > 45.0) | (df["AROONU_14_1d"] < 80.0) | (df["ROC_9_1d"] > -15.0))
      # 4h down move, 1d high & overbought
      & ((df["RSI_3_4h"] > 45.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 90.0) | (df["ROC_9_1d"] < 25.0))
      # 4h down move, 4h & 1d overbought
      & ((df["RSI_3_4h"] > 50.0) | (df["ROC_9_4h"] < 10.0) | (df["ROC_9_1d"] < 40.0))
      # 4h down move, 4h still high, 1d downtrend
      & ((df["RSI_3_4h"] > 50.0) | (df["RSI_14_4h"] < 40.0) | (df["ROC_9_1d"] > -30.0))
      # 4h down move, 4h still high, 1d downtrend
      & ((df["RSI_3_4h"] > 50.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 50.0) | (df["ROC_9_1d"] > -30.0))
      # 1d down move, 4h still high, 1d downtrend
      & ((df["RSI_3_1d"] > 3.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 40.0) | (df["ROC_9_1d"] > -25.0))
      # 1d down move, 1h & 4h high
      & ((df["RSI_3_1d"] > 10.0) | (df["AROONU_14_1h"] < 50.0) | (df["AROONU_14_4h"] < 90.0))
      # 1d down move, 1d high, 1d downtrend
      & ((df["RSI_3_1d"] > 10.0) | (df["AROONU_14_1d"] < 70.0) | (df["ROC_9_1d"] > -40.0))
      # 1d down move, 4h high, 1d downtrend
      & ((df["RSI_3_1d"] > 10.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 90.0) | (df["ROC_9_1d"] > -80.0))
      # 1d down move, 1h & 4h high
      & ((df["RSI_3_1d"] > 15.0) | (df["AROONU_14_1h"] < 90.0) | (df["AROONU_14_4h"] < 100.0))
      # 1d down move, 1h high, 1d downtrend
      & ((df["RSI_3_1d"] > 20.0) | (df["AROONU_14_1h"] < 100.0) | (df["ROC_9_1d"] > -30.0))
      # 1d down move, 1h still high, 4h downtrend
      & ((df["RSI_3_1d"] > 25.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 50.0) | (df["ROC_9_4h"] > -30.0))
      # 1d down move, 1h high & overbought
      & ((df["RSI_3_1d"] > 35.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 90.0) | (df["ROC_9_1h"] < 10.0))
      # 15m downtrend, 4h & 1d high
      & ((df["CMF_20_15m"] > -0.30) | (df["AROONU_14_4h"] < 80.0) | (df["AROONU_14_1d"] < 100.0))
      # 15m & 1h high, 1h overbought
      & ((df["AROONU_14_15m"] < 70.0) | (df["AROONU_14_1h"] < 100.0) | (df["ROC_9_1h"] < 50.0))
      # 15m & 1d high, 1d overbought
      & ((df["AROONU_14_15m"] < 70.0) | (df["AROONU_14_1d"] < 90.0) | (df["ROC_9_1d"] < 30.0))
      # 1h & 4h high, 1h downtrend
      & ((df["AROONU_14_1h"] < 70.0) | (df["AROONU_14_4h"] < 100.0) | (df["CMF_20_1h"] > -0.30))
      # 1h high, 4h high, 1h overbought
      & ((df["AROONU_14_1h"] < 70.0) | (df["AROONU_14_4h"] < 100.0) | (df["ROC_9_1h"] < 20.0))
      # 1h & 1d high, 1h overbought
      & ((df["AROONU_14_1h"] < 70.0) | (df["AROONU_14_1d"] < 70.0) | (df["ROC_9_1h"] < 20.0))
      # 1h high, 1d high & overbought
      & ((df["AROONU_14_1h"] < 70.0) | (df["AROONU_14_1d"] < 100.0) | (df["ROC_9_1d"] < 200.0))
      # 1h high, 1h & 1d overbought
      & ((df["AROONU_14_1h"] < 70.0) | (df["ROC_9_1h"] < 20.0) | (df["ROC_9_1d"] < 200.0))
      # 1h high, 4h downtrend, 1d overbought
      & ((df["AROONU_14_1h"] < 70.0) | (df["ROC_9_4h"] > -40.0) | (df["ROC_9_1d"] < 100.0))
      # 1h high, 1h & 1d overbought
      & ((df["AROONU_14_1h"] < 80.0) | (df["ROC_9_1h"] < 20.0) | (df["ROC_9_1d"] < 20.0))
      # 1h high, 1h overbought, 1d downtrend
      & ((df["AROONU_14_1h"] < 80.0) | (df["ROC_9_1h"] < 30.0) | (df["ROC_9_1d"] > -40.0))
      # 1h high, 4h & 1d overbought
      & ((df["AROONU_14_1h"] < 80.0) | (df["ROC_9_4h"] < 10.0) | (df["ROC_9_1d"] < 40.0))
      # 1h high, 4h & 1d downtrend
      & ((df["AROONU_14_1h"] < 85.0) | (df["ROC_9_4h"] > -20.0) | (df["ROC_9_1d"] > -50.0))
      # 1h & 4h high, 1h overbought
      & ((df["AROONU_14_1h"] < 100.0) | (df["AROONU_14_4h"] < 100.0) | (df["ROC_9_1h"] < 10.0))
      # 4h high, 4h & 1d overbought
      & ((df["AROONU_14_4h"] < 60.0) | (df["ROC_9_4h"] < 30.0) | (df["ROC_9_1d"] < 60.0))
      # 4h & 1d high, 4h overbought
      & ((df["AROONU_14_4h"] < 80.0) | (df["AROONU_14_1d"] < 100.0) | (df["ROC_9_4h"] < 30.0))
      # 4h high, 4h & 1d overbought
      & ((df["AROONU_14_4h"] < 80.0) | (df["ROC_9_4h"] < 20.0) | (df["ROC_9_1d"] < 20.0))
      # 4h high, 15m downtrend, 4h overbought
      & ((df["AROONU_14_4h"] < 100.0) | (df["ROC_9_15m"] > -30.0) | (df["ROC_9_4h"] < 30.0))
      # 4h high, 1h & 4h overbought
      & ((df["AROONU_14_4h"] < 100.0) | (df["ROC_9_1h"] < 30.0) | (df["ROC_9_4h"] < 70.0))
      # 4h & 1d high, 1h overbought
      & ((df["AROONU_14_4h"] < 100.0) | (df["AROONU_14_1d"] < 100.0) | (df["ROC_9_1h"] < 50.0))
      # 1d still high, 4h & 1d downtrend
      & ((df["AROONU_14_1d"] < 50.0) | (df["ROC_9_4h"] > -50.0) | (df["ROC_9_1d"] > -50.0))
      # 1d high, 1h & 4h downtrend
      & ((df["AROONU_14_1d"] < 85.0) | (df["ROC_9_1h"] > -30.0) | (df["ROC_9_4h"] > -50.0))
      # 1d high, 4h downtrend, 1d overbought
      & ((df["AROONU_14_1d"] < 85.0) | (df["ROC_9_4h"] > -25.0) | (df["ROC_9_1d"] < 50.0))
      # 1d high, 4h & 1d overbought
      & ((df["AROONU_14_1d"] < 90.0) | (df["ROC_9_4h"] < 10.0) | (df["ROC_9_1d"] < 50.0))
      # 1h high, 1d overbought
      & ((df["STOCHRSIk_14_14_3_3_1h"] < 70.0) | (df["ROC_9_1d"] < 40.0))
      # 1h high, 4h overbought
      & ((df["STOCHRSIk_14_14_3_3_1h"] < 80.0) | (df["ROC_9_4h"] < 80.0))
      # 1h high, 1h overbought, 4h downtrend
      & ((df["STOCHRSIk_14_14_3_3_1h"] < 90.0) | (df["ROC_9_1h"] < 10.0) | (df["ROC_9_4h"] > -15.0))
      # 4h high, 1h & 4h overbought
      & ((df["STOCHRSIk_14_14_3_3_4h"] < 90.0) | (df["ROC_9_1h"] < 20.0) | (df["ROC_9_4h"] < 50.0))
      # 1d high, 4h & 1d overbought
      & ((df["STOCHRSIk_14_14_3_3_1d"] < 90.0) | (df["ROC_9_4h"] < 100.0) | (df["ROC_9_1d"] < 100.0))
      # 1d P&D, 4h overbought
      & ((df["change_pct_1d"] > -10.0) | (df["change_pct_1d"].shift(288) < 30.0) | (df["ROC_9_4h"] < 10.0))
      # big drop in the last 20 days, 1d high, 1d downtrend
      & (
        (df["close"] > (df["high_max_20_1d"] * 0.20))
        | (df["STOCHRSIk_14_14_3_3_1d"] < 70.0)
        | (df["ROC_9_1d"] > -15.0)
      )
    )

    # Logic
    long_entry_logic.append(
      (df["RSI_3"] > 5.0)
      & (df["RSI_14"] < 36.0)
      & (df["AROONU_14"] < 25.0)
      & (df["AROOND_14"] > 75.0)
      & (df["EMA_9"] < (df["EMA_26"] * 0.960))
    )


def append_long_42(df, long_entry_logic, allowed_empty_candles_288) -> None:
    """Append NFI long condition #42, a quick-mode long entry."""
    long_entry_logic.append(df["num_empty_288"] <= allowed_empty_candles_288)
    # long_entry_logic.append(df["protections_long_global"] == True)

    long_entry_logic.append(
      # 5m & 1h down move, 1d still high
      ((df["RSI_3"] > 3.0) | (df["RSI_3_1h"] > 3.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 40.0))
      # 5m & 1h down move, 1d high
      & ((df["RSI_3"] > 3.0) | (df["RSI_3_1h"] > 25.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 70.0))
      # 15m & 1h down move, 4h high
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_1h"] > 3.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 70.0))
      # 15m & 1h down move, 1h downtrend
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_1h"] > 3.0) | (df["ROC_9_1h"] > -50.0))
      # 15m & 1h down move, 1d still not low enough
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_1h"] > 5.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 30.0))
      # 15m & 1h down move, 4h still high
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_1h"] > 10.0) | (df["AROONU_14_4h"] < 50.0))
      # 15m & 1h down move, 1d high
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_1h"] > 10.0) | (df["AROONU_14_1d"] < 60.0))
      # 15m & 1h down move, 1h high
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_1h"] > 15.0) | (df["AROONU_14_1h"] < 60.0))
      # 15m & 4h down move, 4h still high
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_4h"] > 30.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 40.0))
      # 15m & 4h down move, 1d still high
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_4h"] > 15.0) | (df["AROONU_14_1d"] < 40.0))
      # 15m & 1h down move, 1d downtrend
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_1h"] > 15.0) | (df["ROC_9_1d"] > -30.0))
      # 15m down move, 4h still high, 1d downtrend
      & ((df["RSI_3_15m"] > 3.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 40.0) | (df["ROC_9_1d"] > -40.0))
      # 15m & 1h & 4h down move
      & ((df["RSI_3_15m"] > 5.0) | (df["RSI_3_1h"] > 5.0) | (df["RSI_3_4h"] > 20.0))
      # 15m & 1h down move, 1h still high
      & ((df["RSI_3_15m"] > 5.0) | (df["RSI_3_1h"] > 5.0) | (df["AROONU_14_1h"] < 40.0))
      # 15m & 1h down move, 1d high
      & ((df["RSI_3_15m"] > 5.0) | (df["RSI_3_1h"] > 5.0) | (df["AROONU_14_1d"] < 70.0))
      # 15m & 1h & 4h down move
      & ((df["RSI_3_15m"] > 5.0) | (df["RSI_3_1h"] > 10.0) | (df["RSI_3_4h"] > 15.0))
      # 15m & 4h down move, 1h downtrend
      & ((df["RSI_3_15m"] > 5.0) | (df["RSI_3_4h"] > 10.0) | (df["ROC_9_1h"] > -20.0))
      # 15m & 4h down move, 1d downtrend
      & ((df["RSI_3_15m"] > 5.0) | (df["RSI_3_4h"] > 10.0) | (df["ROC_9_1d"] > -30.0))
      # 15m & 4h down move, 4h still high
      & ((df["RSI_3_15m"] > 5.0) | (df["RSI_3_4h"] > 30.0) | (df["AROONU_14_4h"] < 40.0))
      # 15m & 1h down move, 4h high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1h"] > 10.0) | (df["AROONU_14_4h"] < 70.0))
      # 15m & 1h down move, 1d high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1h"] > 10.0) | (df["AROONU_14_1d"] < 100.0))
      # 15m & 1h down move, 4h still high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1h"] > 10.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 40.0))
      # 15m & 1h down move, 1d high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1h"] > 10.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 90.0))
      # 15m & 1h down move, 4h high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1h"] > 15.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 60.0))
      # 15m & 1h down move, 1d downtrend
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1h"] > 15.0) | (df["ROC_9_1d"] > -30.0))
      # 15m & 1h down move, 4h high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1h"] > 20.0) | (df["AROONU_14_4h"] < 100.0))
      # 15m & 1h down move, 1d overbought
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1h"] > 20.0) | (df["ROC_9_1d"] < 10.0))
      # 15m & 4h down move, 1d high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_4h"] > 30.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 90.0))
      # 15m & 1d down move, 4h still high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1d"] > 10.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 40.0))
      # 15m & 4h down move, 4h still high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_4h"] > 10.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 40.0))
      # 15m & 4h down move, 1d high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_4h"] > 20.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 70.0))
      # 15m & 4h down move, 4h still not low enough
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_4h"] > 20.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 30.0))
      # 15m & 4h down move, 1d high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_4h"] > 20.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 80.0))
      # 15m & 1h down move, 1h high
      & ((df["RSI_3_15m"] > 15.0) | (df["RSI_3_1h"] > 15.0) | (df["AROONU_14_1h"] < 70.0))
      # 15m & 1h down move, 15m still high
      & ((df["RSI_3_15m"] > 15.0) | (df["RSI_3_1h"] > 20.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 50.0))
      # 15m & 4h down move, 15m still high
      & ((df["RSI_3_15m"] > 15.0) | (df["RSI_3_4h"] > 15.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 50.0))
      # 15m & 4h down move, 4h high
      & ((df["RSI_3_15m"] > 15.0) | (df["RSI_3_4h"] > 20.0) | (df["AROONU_14_4h"] < 60.0))
      # 15m & 1d down move, 1d high
      & ((df["RSI_3_15m"] > 15.0) | (df["RSI_3_1d"] > 40.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 70.0))
      # 15m down move, 15m high
      & ((df["RSI_3_15m"] > 15.0) | (df["AROONU_14_15m"] < 70.0))
      # 15m & 4h down move, 4h high
      & ((df["RSI_3_15m"] > 20.0) | (df["RSI_3_4h"] > 25.0) | (df["AROONU_14_4h"] < 70.0))
      # 15m down move, 1h & 4h high
      & ((df["RSI_3_15m"] > 20.0) | (df["AROONU_14_1h"] < 70.0) | (df["AROONU_14_4h"] < 100.0))
      # 15m down move, 15m still not low enough, 1d downtrend
      & ((df["RSI_3_15m"] > 25.0) | (df["AROONU_14_15m"] < 25.0) | (df["ROC_9_1d"] > -50.0))
      # 15m down move, 15m still high, 4h high
      & ((df["RSI_3_15m"] > 25.0) | (df["AROONU_14_15m"] < 50.0) | (df["AROONU_14_4h"] < 80.0))
      # 15m down move, 4h high, 1d downtrend
      & ((df["RSI_3_15m"] > 25.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 80.0) | (df["ROC_9_1d"] > -40.0))
      # 15m down move, 4h high, 1d downtrend
      & ((df["RSI_3_15m"] > 25.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 90.0) | (df["ROC_9_1d"] > -10.0))
      # 15m down move, 15m still high, 4h high
      & ((df["RSI_3_15m"] > 35.0) | (df["AROONU_14_15m"] < 50.0) | (df["AROONU_14_4h"] < 80.0))
      # 1h & 4h down move
      & ((df["RSI_3_1h"] > 3.0) | (df["RSI_3_4h"] > 3.0))
      # 1h & 4h down move, 1d still high
      & ((df["RSI_3_1h"] > 3.0) | (df["RSI_3_4h"] > 15.0) | (df["AROONU_14_1d"] < 50.0))
      # 1h & 4h down move, 1d still high
      & ((df["RSI_3_1h"] > 3.0) | (df["RSI_3_4h"] > 15.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 50.0))
      # 1h & 4h down move, 1h still high
      & ((df["RSI_3_1h"] > 3.0) | (df["RSI_3_4h"] > 20.0) | (df["AROONU_14_1h"] < 40.0))
      # 1h & 4h down move, 4h still not low enough
      & ((df["RSI_3_1h"] > 3.0) | (df["RSI_3_4h"] > 20.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 30.0))
      # 1h & 4h down move, 4h high
      & ((df["RSI_3_1h"] > 3.0) | (df["RSI_3_4h"] > 25.0) | (df["AROONU_14_4h"] < 70.0))
      # 1h & 4h down move, 1d high
      & ((df["RSI_3_1h"] > 3.0) | (df["RSI_3_4h"] > 25.0) | (df["AROONU_14_1d"] < 70.0))
      # 1h & 4h down move, 4h high
      & ((df["RSI_3_1h"] > 3.0) | (df["RSI_3_4h"] > 25.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 60.0))
      # 1h down move, 1d high, 1d downtrend
      & ((df["RSI_3_1h"] > 3.0) | (df["AROONU_14_1d"] < 70.0) | (df["ROC_9_1h"] > -50.0))
      # 1h & 4h down move, 15m still not low enough
      & ((df["RSI_3_1h"] > 5.0) | (df["RSI_3_4h"] > 5.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 20.0))
      # 1h & 4h down move, 1d downtrend
      & ((df["RSI_3_1h"] > 5.0) | (df["RSI_3_4h"] > 5.0) | (df["ROC_9_1d"] > -30.0))
      # 1h & 4h down move, 1d still high
      & ((df["RSI_3_1h"] > 5.0) | (df["RSI_3_4h"] > 15.0) | (df["AROONU_14_1d"] < 40.0))
      # 1h & 4h down move, 1h high
      & ((df["RSI_3_1h"] > 5.0) | (df["RSI_3_4h"] > 25.0) | (df["AROONU_14_1h"] < 70.0))
      # 1h & 4h down move, 1d high
      & ((df["RSI_3_1h"] > 5.0) | (df["RSI_3_4h"] > 25.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 80.0))
      # 1h & 4h down move, 1d overbought
      & ((df["RSI_3_1h"] > 5.0) | (df["RSI_3_4h"] > 35.0) | (df["ROC_9_1d"] < 40.0))
      # 1h & 1d down move, 1h still high
      & ((df["RSI_3_1h"] > 5.0) | (df["RSI_3_1d"] > 5.0) | (df["AROONU_14_1h"] < 50.0))
      # 1h down move, 4h high
      & ((df["RSI_3_1h"] > 5.0) | (df["AROONU_14_4h"] < 90.0))
      # 1h & 4h down move, 1d high
      & ((df["RSI_3_1h"] > 10.0) | (df["RSI_3_4h"] > 10.0) | (df["AROONU_14_1d"] < 75.0))
      # 1h & 4h down move, 1d high
      & ((df["RSI_3_1h"] > 10.0) | (df["RSI_3_4h"] > 10.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 80.0))
      # 1h & 4h down move, 4h downtrend
      & ((df["RSI_3_1h"] > 10.0) | (df["RSI_3_4h"] > 10.0) | (df["ROC_9_4h"] > -20.0))
      # 1h & 4h down move, 1d downtrend
      & ((df["RSI_3_1h"] > 10.0) | (df["RSI_3_4h"] > 10.0) | (df["ROC_9_1d"] > -20.0))
      # 1h & 4h down move, 1d overbought
      & ((df["RSI_3_1h"] > 10.0) | (df["RSI_3_4h"] > 10.0) | (df["ROC_9_1d"] < 10.0))
      # 1h & 4h down move, 1d high
      & ((df["RSI_3_1h"] > 10.0) | (df["RSI_3_4h"] > 15.0) | (df["AROONU_14_1d"] < 80.0))
      # 1h & 4h down move, 4h still not low enough
      & ((df["RSI_3_1h"] > 10.0) | (df["RSI_3_4h"] > 15.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 20.0))
      # 1h & 4h down move, 1d downtrend
      & ((df["RSI_3_1h"] > 10.0) | (df["RSI_3_4h"] > 15.0) | (df["ROC_9_1d"] > -40.0))
      # 1h & 4h down move, 1h still high
      & ((df["RSI_3_1h"] > 10.0) | (df["RSI_3_4h"] > 20.0) | (df["AROONU_14_1h"] < 40.0))
      # 1h & 4h down move, 4h high
      & ((df["RSI_3_1h"] > 10.0) | (df["RSI_3_4h"] > 20.0) | (df["AROONU_14_4h"] < 70.0))
      # 1h & 4h down move, 1d high
      & ((df["RSI_3_1h"] > 10.0) | (df["RSI_3_4h"] > 20.0) | (df["AROONU_14_1d"] < 90.0))
      # 1h & 4h down move, 1d overbought
      & ((df["RSI_3_1h"] > 10.0) | (df["RSI_3_4h"] > 25.0) | (df["ROC_9_1d"] < 40.0))
      # 1h & 4h down move, 1d high
      & ((df["RSI_3_1h"] > 10.0) | (df["RSI_3_4h"] > 35.0) | (df["AROONU_14_1d"] < 100.0))
      # 1h & 4h down move, 4h high
      & ((df["RSI_3_1h"] > 10.0) | (df["RSI_3_4h"] > 35.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 70.0))
      # 1h & 1d down move, 1d still high
      & ((df["RSI_3_1h"] > 10.0) | (df["RSI_3_1d"] > 10.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 50.0))
      # 1h & 1d down move, 1d still high
      & ((df["RSI_3_1h"] > 10.0) | (df["RSI_3_1d"] > 25.0) | (df["RSI_14_1d"] < 50.0))
      # 1h & 1d down move, 1h high
      & ((df["RSI_3_1h"] > 10.0) | (df["RSI_3_1d"] > 25.0) | (df["AROONU_14_1h"] < 70.0))
      # 1h & 1d down move, 1d high
      & ((df["RSI_3_1h"] > 10.0) | (df["RSI_3_1d"] > 35.0) | (df["AROONU_14_1d"] < 70.0))
      # 1h down move, 1h downtrend, 1h high
      & ((df["RSI_3_1h"] > 10.0) | (df["CMF_20_1h"] > -0.30) | (df["AROONU_14_1h"] < 70.0))
      # 1h down move, 1h high, 1d downtrend
      & ((df["RSI_3_1h"] > 10.0) | (df["AROONU_14_1h"] < 40.0) | (df["ROC_9_1d"] > -20.0))
      # 1h down move, 1h & 4h high
      & ((df["RSI_3_1h"] > 10.0) | (df["AROONU_14_1h"] < 60.0) | (df["AROONU_14_4h"] < 70.0))
      # 1h down move, 1h high, 1d overbought
      & ((df["RSI_3_1h"] > 10.0) | (df["AROONU_14_1h"] < 60.0) | (df["ROC_9_1d"] < 20.0))
      # 1h down move, 4h still high, 1d downtrend
      & ((df["RSI_3_1h"] > 10.0) | (df["AROONU_14_4h"] < 40.0) | (df["ROC_9_1d"] > -40.0))
      # 1h down move, 4h high, 1d downtrend
      & ((df["RSI_3_1h"] > 10.0) | (df["AROONU_14_4h"] < 70.0) | (df["ROC_9_1d"] > -20.0))
      # 1h down move, 1d still high, 1d downtrend
      & ((df["RSI_3_1h"] > 10.0) | (df["AROONU_14_1d"] < 40.0) | (df["ROC_9_1d"] > -20.0))
      # 1h down move, 1d high & overbought
      & ((df["RSI_3_1h"] > 10.0) | (df["AROONU_14_1d"] < 90.0) | (df["ROC_9_1d"] < 30.0))
      # 1h down move, 15m high
      & ((df["RSI_3_1h"] > 10.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 80.0))
      # 1h down move, 4h & 1d downtrend
      & ((df["RSI_3_1h"] > 10.0) | (df["ROC_9_4h"] > -20.0) | (df["ROC_9_1d"] > -40.0))
      # 1h & 4h down move, 4h still high
      & ((df["RSI_3_1h"] > 15.0) | (df["RSI_3_4h"] > 15.0) | (df["AROONU_14_4h"] < 50.0))
      # 1h & 4h down move, 15m still high
      & ((df["RSI_3_1h"] > 15.0) | (df["RSI_3_4h"] > 15.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 40.0))
      # 1h & 4h down move, 4h still not low enough
      & ((df["RSI_3_1h"] > 15.0) | (df["RSI_3_4h"] > 15.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 20.0))
      # 1h & 4h down move, 1d high
      & ((df["RSI_3_1h"] > 15.0) | (df["RSI_3_4h"] > 15.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 70.0))
      # 1h & 4h down move, 4h high
      & ((df["RSI_3_1h"] > 15.0) | (df["RSI_3_4h"] > 20.0) | (df["AROONU_14_4h"] < 70.0))
      # 1h & 4h down move, 1d downtrend
      & ((df["RSI_3_1h"] > 15.0) | (df["RSI_3_4h"] > 25.0) | (df["ROC_9_1d"] > -40.0))
      # 1h & 4h down move, 1d high
      & ((df["RSI_3_1h"] > 15.0) | (df["RSI_3_4h"] > 30.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 80.0))
      # 1h & 4h down move, 4h overbought
      & ((df["RSI_3_1h"] > 15.0) | (df["RSI_3_4h"] > 35.0) | (df["ROC_9_4h"] < 10.0))
      # 1h & 1d down move, 4h high
      & ((df["RSI_3_1h"] > 15.0) | (df["RSI_3_1d"] > 20.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 60.0))
      # 1h & 1d down move, 1d overbought
      & ((df["RSI_3_1h"] > 15.0) | (df["RSI_3_1d"] > 35.0) | (df["ROC_9_1d"] < 10.0))
      # 1h down move, 1h downtrend, 1h high
      & ((df["RSI_3_1h"] > 15.0) | (df["CMF_20_1h"] > -0.30) | (df["AROONU_14_1h"] < 70.0))
      # 1h down move, 1h still high, 4h downtrend
      & ((df["RSI_3_1h"] > 15.0) | (df["AROONU_14_1h"] < 40.0) | (df["ROC_9_4h"] > -30.0))
      # 1h down move, 1h still high, 1d downtrend
      & ((df["RSI_3_1h"] > 15.0) | (df["AROONU_14_1h"] < 50.0) | (df["ROC_9_1d"] > -40.0))
      # 1h down move, 1d still high, 4h downtrend
      & ((df["RSI_3_1h"] > 15.0) | (df["AROONU_14_1d"] < 50.0) | (df["ROC_9_4h"] > -20.0))
      # 1h down move, 1d high, 1d downtrend
      & ((df["RSI_3_1h"] > 15.0) | (df["AROONU_14_1d"] < 80.0) | (df["ROC_9_1d"] > -20.0))
      # 1h down move, 1d high & overbought
      & ((df["RSI_3_1h"] > 15.0) | (df["AROONU_14_1d"] < 80.0) | (df["ROC_9_1d"] < 30.0))
      # 1h down move, 4h still high, 1d downtrend
      & ((df["RSI_3_1h"] > 15.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 50.0) | (df["ROC_9_1d"] > -30.0))
      # 1h down move, 4h & 1d downtrend
      & ((df["RSI_3_1h"] > 15.0) | (df["ROC_9_4h"] > -20.0) | (df["ROC_9_1d"] > -20.0))
      # 1h & 4h down move, 1h high
      & ((df["RSI_3_1h"] > 20.0) | (df["RSI_3_4h"] > 20.0) | (df["AROONU_14_1h"] < 70.0))
      # 1h & 4h down move, 1d overbought
      & ((df["RSI_3_1h"] > 20.0) | (df["RSI_3_4h"] > 20.0) | (df["AROONU_14_1d"] < 100.0))
      # 1h & 4h down move, 15m high
      & ((df["RSI_3_1h"] > 20.0) | (df["RSI_3_4h"] > 20.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 60.0))
      # 1h & 4h down move, 1d overbought
      & ((df["RSI_3_1h"] > 20.0) | (df["RSI_3_4h"] > 20.0) | (df["ROC_9_1d"] < 30.0))
      # 1h & 4h down move, 4h high
      & ((df["RSI_3_1h"] > 20.0) | (df["RSI_3_4h"] > 50.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 80.0))
      # 1h & 1d down move, 1d high
      & ((df["RSI_3_1h"] > 20.0) | (df["RSI_3_1d"] > 20.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 60.0))
      # 1h & 1d down move, 1d high
      & ((df["RSI_3_1h"] > 20.0) | (df["RSI_3_1d"] > 30.0) | (df["AROONU_14_1d"] < 100.0))
      # 1h & 1d down move, 1d overbought
      & ((df["RSI_3_1h"] > 20.0) | (df["RSI_3_1d"] > 45.0) | (df["ROC_9_1d"] < 20.0))
      # 1h down move, 1h high, 1d overbought
      & ((df["RSI_3_1h"] > 20.0) | (df["AROONU_14_1h"] < 60.0) | (df["ROC_9_1d"] < 30.0))
      # 1h down move, 1h high, 4h downtrend
      & ((df["RSI_3_1h"] > 20.0) | (df["AROONU_14_1h"] < 70.0) | (df["ROC_9_4h"] > -20.0))
      # 1h down move, 1d high & overbought
      & ((df["RSI_3_1h"] > 20.0) | (df["AROONU_14_1d"] < 100.0) | (df["ROC_9_1d"] < 30.0))
      # 1h down move, 1d high, 4h downtrend
      & ((df["RSI_3_1h"] > 20.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 80.0) | (df["ROC_9_4h"] > -20.0))
      # 1h & 4h down move, 15m high
      & ((df["RSI_3_1h"] > 25.0) | (df["RSI_3_4h"] > 25.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 70.0))
      # 1h & 4h down move, 4h high
      & ((df["RSI_3_1h"] > 25.0) | (df["RSI_3_4h"] > 40.0) | (df["AROONU_14_4h"] < 70.0))
      # 1h & 1d down move, 1h high
      & ((df["RSI_3_1h"] > 25.0) | (df["RSI_3_1d"] > 25.0) | (df["AROONU_14_1h"] < 80.0))
      # 1h & 1d down move, 1d high
      & ((df["RSI_3_1h"] > 25.0) | (df["RSI_3_1d"] > 45.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 80.0))
      # 1h down move, 4h downtrend, 4h high
      & ((df["RSI_3_1h"] > 25.0) | (df["CMF_20_4h"] > -0.50) | (df["AROONU_14_4h"] < 70.0))
      # 1h down move, 1h high, 1d overbought
      & ((df["RSI_3_1h"] > 25.0) | (df["AROONU_14_1h"] < 60.0) | (df["ROC_9_1d"] < 50.0))
      # 1h down move, 1h high, 1d downtrend
      & ((df["RSI_3_1h"] > 25.0) | (df["AROONU_14_1h"] < 60.0) | (df["ROC_9_1d"] > -40.0))
      # 1h down move, 4h high & overbought
      & ((df["RSI_3_1h"] > 25.0) | (df["AROONU_14_4h"] < 70.0) | (df["ROC_9_4h"] < 10.0))
      # 1h down move, 1d high & overbought
      & ((df["RSI_3_1h"] > 25.0) | (df["AROONU_14_1d"] < 80.0) | (df["ROC_9_1d"] < 200.0))
      # 1h down move, 1d high, 4h overbought
      & ((df["RSI_3_1h"] > 25.0) | (df["AROONU_14_1d"] < 100.0) | (df["ROC_9_4h"] < 10.0))
      # 1h down move, 1h high & overbought
      & ((df["RSI_3_1h"] > 25.0) | (df["AROONU_14_1d"] < 100.0) | (df["ROC_9_1d"] < 20.0))
      # 1h down move, 4h high & overbought
      & ((df["RSI_3_1h"] > 25.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 80.0) | (df["ROC_9_4h"] < 20.0))
      # 1h & 4h down move, 1d downtrend
      & ((df["RSI_3_1h"] > 30.0) | (df["RSI_3_4h"] > 30.0) | (df["ROC_9_1d"] > -50.0))
      # 1h & 4h down move, 15m high
      & ((df["RSI_3_1h"] > 30.0) | (df["RSI_3_4h"] > 35.0) | (df["AROONU_14_15m"] < 80.0))
      # 1h & 4h down move, 4h high
      & ((df["RSI_3_1h"] > 30.0) | (df["RSI_3_4h"] > 40.0) | (df["AROONU_14_4h"] < 75.0))
      # 1h & 4h down move, 15m high
      & ((df["RSI_3_1h"] > 30.0) | (df["RSI_3_4h"] > 40.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 80.0))
      # 1h & 4h down move, 4h high
      & ((df["RSI_3_1h"] > 30.0) | (df["RSI_3_4h"] > 50.0) | (df["AROONU_14_4h"] < 80.0))
      # 1h & 1d down move, 1d high
      & ((df["RSI_3_1h"] > 30.0) | (df["RSI_3_1d"] > 30.0) | (df["AROONU_14_1d"] < 80.0))
      # 1h & 1d down move, 1d overbought
      & ((df["RSI_3_1h"] > 30.0) | (df["RSI_3_1d"] > 40.0) | (df["ROC_9_1d"] < 50.0))
      # 1h down move, 4h high, 4h downtrend
      & ((df["RSI_3_1h"] > 30.0) | (df["AROONU_14_4h"] < 70.0) | (df["CMF_20_4h"] > -0.40))
      # 1h down move, 4h high & overbought
      & ((df["RSI_3_1h"] > 30.0) | (df["AROONU_14_4h"] < 80.0) | (df["ROC_9_4h"] < 30.0))
      # 1h down move, 1d high, 4h overbought
      & ((df["RSI_3_1h"] > 30.0) | (df["AROONU_14_1d"] < 100.0) | (df["ROC_9_4h"] < 10.0))
      # 1h down move, 4h still high, 1d downtrend
      & ((df["RSI_3_1h"] > 30.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 40.0) | (df["ROC_9_1d"] > -80.0))
      # 1h down move, 4h & 1d overbought
      & ((df["RSI_3_1h"] > 30.0) | (df["ROC_9_4h"] < 10.0) | (df["ROC_9_1d"] < 30.0))
      # 1h & 4h down move, 15m high
      & ((df["RSI_3_1h"] > 35.0) | (df["RSI_3_4h"] > 45.0) | (df["AROONU_14_15m"] < 90.0))
      # 1h & 4h down move, 4h high
      & ((df["RSI_3_1h"] > 35.0) | (df["RSI_3_4h"] > 45.0) | (df["AROONU_14_4h"] < 90.0))
      # 1h down move, 15m high, 1d downtrend
      & ((df["RSI_3_1h"] > 35.0) | (df["AROONU_14_15m"] < 60.0) | (df["ROC_9_1d"] > -40.0))
      # 1h down move, 1h still high, 1d high
      & ((df["RSI_3_1h"] > 35.0) | (df["AROONU_14_1h"] < 50.0) | (df["AROONU_14_1d"] < 90.0))
      # 1h down move, 1h & 4h high
      & ((df["RSI_3_1h"] > 35.0) | (df["AROONU_14_1h"] < 70.0) | (df["AROONU_14_4h"] < 100.0))
      # 1h down move, 1h & 1d high
      & ((df["RSI_3_1h"] > 35.0) | (df["AROONU_14_1h"] < 70.0) | (df["AROONU_14_1d"] < 100.0))
      # 1h down move, 4h high, 1d downtrend
      & ((df["RSI_3_1h"] > 35.0) | (df["AROONU_14_4h"] < 90.0) | (df["ROC_9_1d"] > -20.0))
      # 1h down move, 4h high & overbought
      & ((df["RSI_3_1h"] > 35.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 90.0) | (df["ROC_9_4h"] < 10.0))
      # 1h down move, 4h & 1d downtrend
      & ((df["RSI_3_1h"] > 35.0) | (df["ROC_9_4h"] > -10.0) | (df["ROC_9_1d"] > -60.0))
      # 1h down move, 4h high & overbought
      & ((df["RSI_3_1h"] > 40.0) | (df["AROONU_14_4h"] < 90.0) | (df["ROC_9_4h"] < 20.0))
      # 1h down move, 4h high, 1d downtrend
      & ((df["RSI_3_1h"] > 40.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 60.0) | (df["ROC_9_1d"] > -50.0))
      # 1h down move, 4h high & overbought
      & ((df["RSI_3_1h"] > 40.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 70.0) | (df["ROC_9_4h"] < 40.0))
      # 1h down move, 4h high & overbought
      & ((df["RSI_3_1h"] > 45.0) | (df["AROONU_14_4h"] < 80.0) | (df["ROC_9_4h"] < 100.0))
      # 1h down move, 4h high & overbought
      & ((df["RSI_3_1h"] > 50.0) | (df["AROONU_14_4h"] < 100.0) | (df["ROC_9_4h"] < 40.0))
      # 1h down move, 1d high & overbought
      & ((df["RSI_3_1h"] > 50.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 90.0) | (df["ROC_9_1d"] < 20.0))
      # 1h down move, 4h & 1d overbought
      & ((df["RSI_3_1h"] > 60.0) | (df["ROC_9_4h"] < 30.0) | (df["ROC_9_1d"] < 100.0))
      # 4h & 1d down move
      & ((df["RSI_3_4h"] > 3.0) | (df["RSI_3_1d"] > 15.0))
      # 4h & 1d down move, 1d high
      & ((df["RSI_3_4h"] > 3.0) | (df["RSI_3_1d"] > 25.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 60.0))
      # 4h down move, 1h downtrend, 4h still high
      & ((df["RSI_3_4h"] > 3.0) | (df["CMF_20_1h"] > -0.30) | (df["AROONU_14_4h"] < 40.0))
      # 4h & 1d down move, 4h downtrend
      & ((df["RSI_3_4h"] > 5.0) | (df["RSI_3_1d"] > 15.0) | (df["ROC_9_4h"] > -10.0))
      # 4h & 1d down move, 1d downtrend
      & ((df["RSI_3_4h"] > 5.0) | (df["RSI_3_1d"] > 15.0) | (df["ROC_9_1d"] > -20.0))
      # 4h & 1d down move, 1d still high
      & ((df["RSI_3_4h"] > 5.0) | (df["RSI_3_1d"] > 20.0) | (df["AROONU_14_1d"] < 40.0))
      # 4h & 1d down move, 1d still high
      & ((df["RSI_3_4h"] > 5.0) | (df["RSI_3_1d"] > 20.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 50.0))
      # 4h & 1d down move, 4h still not low enough
      & ((df["RSI_3_4h"] > 5.0) | (df["RSI_3_1d"] > 30.0) | (df["AROONU_14_4h"] < 20.0))
      # 4h & 1d down move, 1d high
      & ((df["RSI_3_4h"] > 5.0) | (df["RSI_3_1d"] > 30.0) | (df["AROONU_14_1d"] < 70.0))
      # 4h down move, 1h & 4h downtrend
      & ((df["RSI_3_4h"] > 5.0) | (df["ROC_9_1h"] > -15.0) | (df["ROC_9_4h"] > -20.0))
      # 4h down move, 4h & 1d downtrend
      & ((df["RSI_3_4h"] > 5.0) | (df["ROC_9_4h"] > -20.0) | (df["ROC_9_1d"] > -20.0))
      # 4h & 1d down move, 15m still not low enough
      & ((df["RSI_3_4h"] > 10.0) | (df["RSI_3_1d"] > 10.0) | (df["AROONU_14_15m"] < 30.0))
      # 4h & 1d down move, 1d downtrend
      & ((df["RSI_3_4h"] > 10.0) | (df["RSI_3_1d"] > 10.0) | (df["ROC_9_1d"] > -20.0))
      # 15m & 1d down move, 15m still high
      & ((df["RSI_3_4h"] > 10.0) | (df["RSI_3_1d"] > 15.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 50.0))
      # 4h & 1d down move, 4h downtrend
      & ((df["RSI_3_4h"] > 10.0) | (df["RSI_3_1d"] > 30.0) | (df["ROC_9_4h"] > -20.0))
      # 4h & 1d down move, 1d overbought
      & ((df["RSI_3_4h"] > 10.0) | (df["RSI_3_1d"] > 45.0) | (df["ROC_9_1d"] < 10.0))
      # 4h down move, 15m high, 1h downtrend
      & ((df["RSI_3_4h"] > 10.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 60.0) | (df["ROC_9_1h"] > -10.0))
      # 4h down move, 15m high
      & ((df["RSI_3_4h"] > 10.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 80.0))
      # 4h down move, 4h still not low e nough, 1d downtrend
      & ((df["RSI_3_4h"] > 10.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 30.0) | (df["ROC_9_1d"] > -20.0))
      # 4h down move, 4h & 1d downtrend
      & ((df["RSI_3_4h"] > 10.0) | (df["ROC_9_4h"] > -20.0) | (df["ROC_9_1d"] > -40.0))
      # 4h & 1d down move, 1d downtrend
      & ((df["RSI_3_4h"] > 15.0) | (df["RSI_3_1d"] > 15.0) | (df["ROC_9_1d"] > -30.0))
      # 4h & 1d down move, 1d still high
      & ((df["RSI_3_4h"] > 15.0) | (df["RSI_3_1d"] > 25.0) | (df["AROONU_14_1d"] < 40.0))
      # 15m & 1d down move, 15m high
      & ((df["RSI_3_4h"] > 15.0) | (df["RSI_3_1d"] > 30.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 70.0))
      # 4h & 1d down move, 4h still high
      & ((df["RSI_3_4h"] > 15.0) | (df["RSI_3_1d"] > 30.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 50.0))
      # 4h & 1d down move, 1d still high
      & ((df["RSI_3_4h"] > 15.0) | (df["RSI_3_1d"] > 35.0) | (df["RSI_14_1d"] < 50.0))
      # 4h down move, 1h still high, 1d downtrend
      & ((df["RSI_3_4h"] > 15.0) | (df["AROONU_14_1h"] < 40.0) | (df["ROC_9_1d"] > -50.0))
      # 4h down move, 1h high, 1d downtrend
      & ((df["RSI_3_4h"] > 15.0) | (df["AROONU_14_1h"] < 90.0) | (df["ROC_9_1d"] > -30.0))
      # 4h down move, 4h still high, 4h downtrend
      & ((df["RSI_3_4h"] > 15.0) | (df["AROONU_14_4h"] < 40.0) | (df["ROC_9_4h"] > -20.0))
      # 4h down move, 4h still high, 1d high
      & ((df["RSI_3_4h"] > 15.0) | (df["AROONU_14_4h"] < 50.0) | (df["AROONU_14_1d"] < 70.0))
      # 4h down move, 4h still high, 1d downtrend
      & ((df["RSI_3_4h"] > 15.0) | (df["AROONU_14_4h"] < 50.0) | (df["ROC_9_1d"] > -20.0))
      # 4h down move, 1h & 4h downtrend
      & ((df["RSI_3_4h"] > 15.0) | (df["ROC_9_1h"] > -40.0) | (df["ROC_9_4h"] > -40.0))
      # 4h & 1d down move, 1d high
      & ((df["RSI_3_4h"] > 20.0) | (df["RSI_3_1d"] > 20.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 80.0))
      # 4h & 1d down move, 15m high
      & ((df["RSI_3_4h"] > 20.0) | (df["RSI_3_1d"] > 30.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 80.0))
      # 4h & 1d down move, 1d high
      & ((df["RSI_3_4h"] > 20.0) | (df["RSI_3_1d"] > 50.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 90.0))
      # 4h down move, 15m high, 4h downtrend
      & ((df["RSI_3_4h"] > 20.0) | (df["AROONU_14_15m"] < 70.0) | (df["ROC_9_4h"] > -30.0))
      # 4h down move, 4h high
      & ((df["RSI_3_4h"] > 20.0) | (df["AROONU_14_4h"] < 100.0))
      # 4h down move, 1d high & overbought
      & ((df["RSI_3_4h"] > 20.0) | (df["AROONU_14_1d"] < 70.0) | (df["ROC_9_1d"] < 70.0))
      # 4h down move, 1d high, 4h downtrend
      & ((df["RSI_3_4h"] > 20.0) | (df["AROONU_14_1d"] < 90.0) | (df["ROC_9_4h"] > -50.0))
      # 4h down move, 1d high & overbought
      & ((df["RSI_3_4h"] > 20.0) | (df["AROONU_14_1d"] < 90.0) | (df["ROC_9_1d"] < 40.0))
      # 4h down move, 15m high
      & ((df["RSI_3_4h"] > 20.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 70.0))
      # 4h down move, 4h still not low enough, 1d downtrend
      & ((df["RSI_3_4h"] > 20.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 30.0) | (df["ROC_9_1d"] > -20.0))
      # 4h down move, 4h & 1d downtrend
      & ((df["RSI_3_4h"] > 20.0) | (df["ROC_9_4h"] > -20.0) | (df["ROC_9_1d"] > -20.0))
      # 4h down move, 1d high, 4h downtrend
      & ((df["RSI_3_4h"] > 20.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 80.0) | (df["ROC_9_4h"] > -20.0))
      # 4h & 1d down move, 1h high
      & ((df["RSI_3_4h"] > 25.0) | (df["RSI_3_1d"] > 25.0) | (df["AROONU_14_1h"] < 90.0))
      # 4h & 1d down move, 1d high
      & ((df["RSI_3_4h"] > 25.0) | (df["RSI_3_1d"] > 25.0) | (df["AROONU_14_1d"] < 90.0))
      # 4h down move, 4h still high, 1d downtrend
      & ((df["RSI_3_4h"] > 25.0) | (df["AROONU_14_4h"] < 40.0) | (df["ROC_9_1d"] > -20.0))
      # 4h down move, 4h high, 1h downtrend
      & ((df["RSI_3_4h"] > 25.0) | (df["AROONU_14_4h"] < 60.0) | (df["ROC_9_1h"] > -10.0))
      # 4h down move, 1d high & overbought
      & ((df["RSI_3_4h"] > 25.0) | (df["AROONU_14_1d"] < 80.0) | (df["ROC_9_1d"] < 30.0))
      # 4h down move, 1d high, 4h downtrend
      & ((df["RSI_3_4h"] > 25.0) | (df["AROONU_14_1d"] < 100.0) | (df["ROC_9_4h"] > -20.0))
      # 4h down move, 4h still high, 1d downtrend
      & ((df["RSI_3_4h"] > 25.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 40.0) | (df["ROC_9_1d"] > -30.0))
      # 4h down move, 4h high, 1d downtrend
      & ((df["RSI_3_4h"] > 25.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 70.0) | (df["ROC_9_1d"] > -20.0))
      # 4h down move, 1d overbought
      & ((df["RSI_3_4h"] > 25.0) | (df["ROC_9_1d"] < 100.0))
      # 4h down move, 1h high, 4h downtrend
      & ((df["RSI_3_4h"] > 30.0) | (df["AROONU_14_1h"] < 60.0) | (df["ROC_9_4h"] > -10.0))
      # 4h down move, 4h still high, 1d high
      & ((df["RSI_3_4h"] > 30.0) | (df["AROONU_14_4h"] < 50.0) | (df["AROONU_14_1d"] < 100.0))
      # 4h down move, 4h high, 1h downtrend
      & ((df["RSI_3_4h"] > 30.0) | (df["AROONU_14_4h"] < 80.0) | (df["ROC_9_1h"] > -40.0))
      # 4h down move, 4h high
      & ((df["RSI_3_4h"] > 30.0) | (df["AROONU_14_4h"] < 100.0))
      # 4h down move, 1d high & overbought
      & ((df["RSI_3_4h"] > 30.0) | (df["AROONU_14_1d"] < 70.0) | (df["ROC_9_1d"] < 60.0))
      # 4h down move, 15m still high, 4h high
      & ((df["RSI_3_4h"] > 35.0) | (df["AROONU_14_15m"] < 50.0) | (df["AROONU_14_4h"] < 80.0))
      # 4h down move, 1h high
      & ((df["RSI_3_4h"] > 35.0) | (df["AROONU_14_1h"] < 70.0))
      # 4h down move, 4h high, 1d downtrend
      & ((df["RSI_3_4h"] > 35.0) | (df["AROONU_14_4h"] < 80.0) | (df["ROC_9_1d"] > -20.0))
      # 4h down move, 4h high, 1d overbought
      & ((df["RSI_3_4h"] > 35.0) | (df["AROONU_14_4h"] < 80.0) | (df["ROC_9_1d"] < 30.0))
      # 4h down move, 1d high & overbought
      & ((df["RSI_3_4h"] > 35.0) | (df["AROONU_14_1d"] < 100.0) | (df["ROC_9_1d"] < 20.0))
      # 4h down move, 4h still high, 1d overbought
      & ((df["RSI_3_4h"] > 35.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 50.0) | (df["ROC_9_1d"] < 200.0))
      # 4h down move, 4h & 1d high
      & ((df["RSI_3_4h"] > 40.0) | (df["AROONU_14_4h"] < 70.0) | (df["AROONU_14_1d"] < 100.0))
      # 4h down move, 4h high, 1d overbought
      & ((df["RSI_3_4h"] > 40.0) | (df["AROONU_14_4h"] < 70.0) | (df["ROC_9_1d"] < 20.0))
      # 4h down move, 4h still high, 1d downtrend
      & ((df["RSI_3_4h"] > 40.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 50.0) | (df["ROC_9_1d"] > -40.0))
      # 4h down move, 4h overbought, 1d downtrend
      & ((df["RSI_3_4h"] > 40.0) | (df["ROC_9_4h"] < 10.0) | (df["ROC_9_1d"] > -40.0))
      # 4h down move, 4h & 1d overbought
      & ((df["RSI_3_4h"] > 40.0) | (df["ROC_9_4h"] < 60.0) | (df["ROC_9_1d"] < 80.0))
      # 4h down move, 4h & 1d high
      & ((df["RSI_3_4h"] > 45.0) | (df["AROONU_14_4h"] < 80.0) | (df["AROONU_14_1d"] < 100.0))
      # 4h down move, 4h overbought
      & ((df["RSI_3_4h"] > 55.0) | (df["ROC_9_4h"] < 30.0))
      # 4h down move, 4h high & overbought
      & ((df["RSI_3_4h"] > 60.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 80.0) | (df["ROC_9_4h"] < 10.0))
      # 1d down move, 1d high, 1d downtrend
      & ((df["RSI_3_1d"] > 15.0) | (df["AROONU_14_1d"] < 70.0) | (df["ROC_9_1d"] > -20.0))
      # 1d down move, 1d still high
      & ((df["RSI_3_1d"] > 15.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 40.0))
      # 1d down move, 4h & 1d downtrend
      & ((df["RSI_3_1d"] > 15.0) | (df["ROC_9_4h"] > -10.0) | (df["ROC_9_1d"] > -40.0))
      # 1d down move, 15m high
      & ((df["RSI_3_1d"] > 20.0) | (df["AROONU_14_15m"] < 80.0))
      # 1d down move, 4h high, 4h downtrend
      & ((df["RSI_3_1d"] > 20.0) | (df["AROONU_14_4h"] < 50.0) | (df["ROC_9_4h"] > -40.0))
      # 1d down move, 1d high, 1d downtrend
      & ((df["RSI_3_1d"] > 25.0) | (df["AROONU_14_1d"] < 80.0) | (df["ROC_9_1d"] > -30.0))
      # 1d down move, 1d still high, 1d downtrend
      & ((df["RSI_3_1d"] > 25.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 50.0) | (df["ROC_9_1d"] > -20.0))
      # 1d down move, 4h & 1d high
      & ((df["RSI_3_1d"] > 30.0) | (df["AROONU_14_4h"] < 90.0) | (df["AROONU_14_1d"] < 90.0))
      # 1h & 4h downtrend, 4h high
      & ((df["CMF_20_1h"] > -0.40) | (df["CMF_20_4h"] > -0.40) | (df["AROONU_14_4h"] < 80.0))
      # 4h & 1d downtrend, 1d high
      & ((df["CMF_20_4h"] > -0.50) | (df["CMF_20_1d"] > -0.50) | (df["AROONU_14_1d"] < 85.0))
      # 15m & 1d high, 4h overbought
      & ((df["AROONU_14_15m"] < 70.0) | (df["AROONU_14_1d"] < 100.0) | (df["ROC_9_4h"] < 20.0))
      # 15m & 4h high, 1d downtrend
      & ((df["AROONU_14_15m"] < 85.0) | (df["AROONU_14_4h"] < 85.0) | (df["ROC_9_1d"] > -20.0))
      # 1h still high, 1h & 4h downtrend
      & ((df["AROONU_14_1h"] < 50.0) | (df["ROC_9_1h"] > -20.0) | (df["ROC_9_4h"] > -30.0))
      # 1h & 4h high, 4h overbought
      & ((df["AROONU_14_1h"] < 80.0) | (df["AROONU_14_4h"] < 100.0) | (df["ROC_9_4h"] < 10.0))
      # 4h high, 4h & 1d downtrend
      & ((df["AROONU_14_4h"] < 60.0) | (df["ROC_9_4h"] > -30.0) | (df["ROC_9_1d"] > -30.0))
      # 4h & 1d high, 4h overbought
      & ((df["AROONU_14_4h"] < 70.0) | (df["AROONU_14_1d"] < 100.0) | (df["ROC_9_4h"] < 30.0))
      # 4h & 1d high, 1d overbought
      & ((df["AROONU_14_4h"] < 70.0) | (df["AROONU_14_1d"] < 100.0) | (df["ROC_9_1d"] < 80.0))
      # 4h high, 4h & 1d overbought
      & ((df["AROONU_14_4h"] < 90.0) | (df["ROC_9_4h"] < 10.0) | (df["ROC_9_1d"] < 10.0))
      # 1d high, 4h & 1d overbought
      & ((df["AROONU_14_1d"] < 70.0) | (df["ROC_9_4h"] < 30.0) | (df["ROC_9_1d"] < 200.0))
      # 1d high, 4h downtrend, 1d overbought
      & ((df["AROONU_14_1d"] < 85.0) | (df["ROC_9_4h"] > -20.0) | (df["ROC_9_1d"] < 200.0))
      # 1d high, 1h & 4h downtrend
      & ((df["AROONU_14_1d"] < 100.0) | (df["ROC_9_1h"] > -30.0) | (df["ROC_9_4h"] > -30.0))
      # 1d high, 1h & 1d overbought
      & ((df["AROONU_14_1d"] < 100.0) | (df["ROC_9_1h"] < 10.0) | (df["ROC_9_1d"] < 30.0))
      # 1d high, 4h & 1d overbought
      & ((df["AROONU_14_1d"] < 100.0) | (df["ROC_9_4h"] < 30.0) | (df["ROC_9_1d"] < 60.0))
      # 15m still high, 1h & 4h downtrend
      & ((df["STOCHRSIk_14_14_3_3_15m"] < 50.0) | (df["ROC_9_1h"] > -20.0) | (df["ROC_9_4h"] > -20.0))
      # 4h high, 1h & 4h overbought
      & ((df["STOCHRSIk_14_14_3_3_4h"] < 90.0) | (df["ROC_9_1h"] < 20.0) | (df["ROC_9_4h"] < 30.0))
      # 4h high, 4h & 1d overbought
      & ((df["STOCHRSIk_14_14_3_3_4h"] < 90.0) | (df["ROC_9_4h"] < 20.0) | (df["ROC_9_1d"] < 80.0))
      # 1d still high, 4h & 1d downtrend
      & ((df["STOCHRSIk_14_14_3_3_1d"] < 50.0) | (df["ROC_9_4h"] > -30.0) | (df["ROC_9_1d"] > -30.0))
      # big drop in the last 20 days, 1d high, 1d downtrend
      & (
        (df["close"] > (df["high_max_20_1d"] * 0.20))
        | (df["STOCHRSIk_14_14_3_3_1d"] < 70.0)
        | (df["ROC_9_1d"] > -15.0)
      )
    )

    # Logic
    long_entry_logic.append(
      (df["WILLR_14"] < -50.0)
      & (df["STOCHRSIk_14_14_3_3"] < 20.0)
      & (df["WILLR_84_1h"] < -70.0)
      & (df["STOCHRSIk_14_14_3_3_1h"] < 20.0)
      & (df["BBB_20_2.0_1h"] > 16.0)
      & (df["close_max_48"] >= (df["close"] * 1.10))
    )


def append_long_43(df, long_entry_logic, allowed_empty_candles_288) -> None:
    """Append NFI long condition #43, a quick-mode long entry."""
    long_entry_logic.append(df["num_empty_288"] <= allowed_empty_candles_288)
    # long_entry_logic.append(df["protections_long_global"] == True)

    long_entry_logic.append(
      # 5m & 15m down move, 15m still high
      ((df["RSI_3"] > 3.0) | (df["RSI_3_15m"] > 5.0) | (df["AROONU_14_15m"] < 40.0))
      # 5m & 1h down move, 1h still not low enough
      & ((df["RSI_3"] > 3.0) | (df["RSI_3_1h"] > 10.0) | (df["AROONU_14_1h"] < 30.0))
      # 5m & 1h down move, 1h still not low enough
      & ((df["RSI_3"] > 3.0) | (df["RSI_3_1h"] > 15.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 30.0))
      # 5m & 1h down move, 4h high
      & ((df["RSI_3"] > 3.0) | (df["RSI_3_1h"] > 50.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 60.0))
      # 5m & 1d down move, 1d still not low enough
      & ((df["RSI_3"] > 3.0) | (df["RSI_3_1d"] > 15.0) | (df["AROONU_14_1d"] < 30.0))
      # 5m down move, 1h & 4h high
      & ((df["RSI_3"] > 3.0) | (df["AROONU_14_1h"] < 80.0) | (df["AROONU_14_4h"] < 100.0))
      # 5m down move, 4h high & overbought
      & ((df["RSI_3"] > 3.0) | (df["AROONU_14_4h"] < 100.0) | (df["ROC_9_4h"] < 20.0))
      # 5m down move, 1d high & overbought
      & ((df["RSI_3"] > 3.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 90.0) | (df["ROC_9_1d"] < 20.0))
      # 5m & 1h down move, 1d overbought
      & ((df["RSI_3"] > 5.0) | (df["RSI_3_1h"] > 25.0) | (df["ROC_9_1d"] < 100.0))
      # 5m & 1d down move, 1h high
      & ((df["RSI_3"] > 5.0) | (df["RSI_3_1d"] > 20.0) | (df["AROONU_14_1h"] < 90.0))
      # 5m & 1h down move, 1h high
      & ((df["RSI_3"] > 10.0) | (df["RSI_3_1h"] > 15.0) | (df["AROONU_14_1h"] < 85.0))
      # 15m & 1h down move
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_1h"] > 3.0))
      # 15m & 1h & 4h down move
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_1h"] > 5.0) | (df["RSI_3_4h"] > 10.0))
      # 15m & 1h & 1d down move
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_1h"] > 10.0) | (df["RSI_3_1d"] > 25.0))
      # 15m & 1h down move, 1d still high
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_1h"] > 10.0) | (df["RSI_14_1d"] < 50.0))
      # 15m & 1h down move, 15m still high
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_1h"] > 10.0) | (df["AROONU_14_15m"] < 50.0))
      # 15m & 1h down move, 1d high
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_1h"] > 10.0) | (df["AROONU_14_1d"] < 70.0))
      # 15m & 1d down move, 1d overbought
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_1h"] > 10.0) | (df["ROC_9_1d"] < 10.0))
      # 15m & 1h down move, 1h still high
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_1h"] > 15.0) | (df["AROONU_14_1h"] < 40.0))
      # 15m & 1h down move, 1d high
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_1h"] > 15.0) | (df["AROONU_14_1d"] < 90.0))
      # 15m & 1h down move, 4h high
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_1h"] > 15.0) | (df["AROONU_14_4h"] < 70.0))
      # 15m & 1h down move, 1d downtrend
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_1h"] > 15.0) | (df["ROC_9_1d"] > -30.0))
      # 15m & 1h down move, 15m high
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_1h"] > 20.0) | (df["AROONU_14_15m"] < 70.0))
      # 15m & 1h down move, 1h high
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_1h"] > 30.0) | (df["AROONU_14_1h"] < 100.0))
      # 15m & 1h down move, 1d high
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_1h"] > 30.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 90.0))
      # 15m & 1h down move, 1d overbought
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_1h"] > 30.0) | (df["ROC_9_1d"] < 200.0))
      # 15m & 1h down move, 1h still high
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_1h"] > 35.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 40.0))
      # 15m & 1h down move, 4h high
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_1h"] > 45.0) | (df["AROONU_14_4h"] < 90.0))
      # 15m & 4h down move, 1d high
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_4h"] > 15.0) | (df["AROONU_14_1d"] < 50.0))
      # 15m & 4h down move, 15m high
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_4h"] > 20.0) | (df["AROONU_14_15m"] < 70.0))
      # 15m & 4h down move, 1d overbought
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_4h"] > 35.0) | (df["ROC_9_1d"] < 60.0))
      # 15m & 1d down move, 1d still high
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_1d"] > 10.0) | (df["AROONU_14_1d"] < 40.0))
      # 15m & 1d down move, 4h still high
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_1d"] > 20.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 50.0))
      # 15m & 1d down move, 1d high
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_1d"] > 45.0) | (df["AROONU_14_1d"] < 70.0))
      # 15m down move, 4h high & overbought
      & ((df["RSI_3_15m"] > 3.0) | (df["AROONU_14_4h"] < 90.0) | (df["ROC_9_4h"] < 100.0))
      # 15m down move, 1d high & overbought
      & ((df["RSI_3_15m"] > 3.0) | (df["AROONU_14_1d"] < 100.0) | (df["ROC_9_1d"] < 40.0))
      # 15m down move, 1h high, 1d downtrend
      & ((df["RSI_3_15m"] > 3.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 80.0) | (df["ROC_9_1d"] > -20.0))
      # 15m down move, 4h high & overbought
      & ((df["RSI_3_15m"] > 3.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 80.0) | (df["ROC_9_4h"] < 40.0))
      # 15m down move, 4h high, 1d overbought
      & ((df["RSI_3_15m"] > 3.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 80.0) | (df["ROC_9_1d"] < 10.0))
      # 15m down move, 1h downtrend, 4h overbought
      & ((df["RSI_3_15m"] > 3.0) | (df["ROC_9_1h"] > -30.0) | (df["ROC_9_4h"] < 100.0))
      # 15m down move, 4h & 1d downtrend
      & ((df["RSI_3_15m"] > 3.0) | (df["ROC_9_4h"] > -70.0) | (df["ROC_9_1d"] > -70.0))
      # 15m & 1h down move, 4h still high
      & ((df["RSI_3_15m"] > 5.0) | (df["RSI_3_1h"] > 5.0) | (df["RSI_14_4h"] < 40.0))
      # 15m & 1h down move, 1h still not low enough
      & ((df["RSI_3_15m"] > 5.0) | (df["RSI_3_1h"] > 15.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 20.0))
      # 15m & 1h down move, 1d still high
      & ((df["RSI_3_15m"] > 5.0) | (df["RSI_3_1h"] > 20.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 50.0))
      # 15m & 1h down move, 1d overbought
      & ((df["RSI_3_15m"] > 5.0) | (df["RSI_3_1h"] > 25.0) | (df["ROC_9_1d"] < 70.0))
      # 15m & 1h down move, 4h high
      & ((df["RSI_3_15m"] > 5.0) | (df["RSI_3_1h"] > 30.0) | (df["AROONU_14_4h"] < 70.0))
      # 15m & 1h down move, 1h high
      & ((df["RSI_3_15m"] > 5.0) | (df["RSI_3_1h"] > 45.0) | (df["AROONU_14_1h"] < 80.0))
      # 15m & 4h down move, 1h still high
      & ((df["RSI_3_15m"] > 5.0) | (df["RSI_3_4h"] > 10.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 50.0))
      # 15m & 4h down move, 1h downtrend
      & ((df["RSI_3_15m"] > 5.0) | (df["RSI_3_4h"] > 10.0) | (df["ROC_9_1h"] > -20.0))
      # 15m & 4h down move, 15m still high
      & ((df["RSI_3_15m"] > 5.0) | (df["RSI_3_4h"] > 15.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 50.0))
      # 15m & 4h down move, 4h still high
      & ((df["RSI_3_15m"] > 5.0) | (df["RSI_3_4h"] > 20.0) | (df["AROONU_14_4h"] < 50.0))
      # 15m & 4h down move, 1d high
      & ((df["RSI_3_15m"] > 5.0) | (df["RSI_3_4h"] > 20.0) | (df["AROONU_14_1d"] < 70.0))
      # 15m & 1d down move, 1h still high
      & ((df["RSI_3_15m"] > 5.0) | (df["RSI_3_1d"] > 20.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 50.0))
      # 15m down move, 15m & 1h still high
      & ((df["RSI_3_15m"] > 5.0) | (df["AROONU_14_15m"] < 40.0) | (df["AROONU_14_1h"] < 50.0))
      # 15m down move, 1h & 4h high
      & ((df["RSI_3_15m"] > 5.0) | (df["AROONU_14_1h"] < 80.0) | (df["AROONU_14_4h"] < 100.0))
      # 15m down move, 1h high, 4h overbought
      & ((df["RSI_3_15m"] > 5.0) | (df["AROONU_14_1h"] < 80.0) | (df["ROC_9_4h"] < 10.0))
      # 15m down move, 4h high & overbought
      & ((df["RSI_3_15m"] > 5.0) | (df["AROONU_14_4h"] < 80.0) | (df["ROC_9_4h"] < 50.0))
      # 15m down move, 1d still high, 1d downtrend
      & ((df["RSI_3_15m"] > 5.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 50.0) | (df["ROC_9_1d"] > -20.0))
      # 15m down move, 1d downtrend
      & ((df["RSI_3_15m"] > 5.0) | (df["ROC_9_1d"] > -60.0))
      # 15m & 1h down move, 15m high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1h"] > 10.0) | (df["AROONU_14_15m"] < 70.0))
      # 15m & 1h down move, 1h still high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1h"] > 15.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 40.0))
      # 15m & 1h down move, 1d high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1h"] > 15.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 90.0))
      # 15m & 1h down move, 4h downtrend
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1h"] > 15.0) | (df["ROC_9_4h"] > -20.0))
      # 15m & 1h down move, 1d downtrend
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1h"] > 15.0) | (df["ROC_9_1d"] > -40.0))
      # 15m & 1h down move, 15m still high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1h"] > 20.0) | (df["AROONU_14_15m"] < 50.0))
      # 15m & 1h down move, 1h high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1h"] > 20.0) | (df["AROONU_14_1h"] < 70.0))
      # 15m & 1h down move, 1d high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1h"] > 20.0) | (df["AROONU_14_1d"] < 80.0))
      # 15m & 1h down move, 1d overbought
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1h"] > 20.0) | (df["ROC_9_1d"] < 80.0))
      # 15m & 1h down move, 4h high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1h"] > 25.0) | (df["AROONU_14_4h"] < 90.0))
      # 15m & 1h down move, 4h high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1h"] > 25.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 80.0))
      # 15m & 1h down move, 4h overbought
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1h"] > 25.0) | (df["ROC_9_4h"] < 20.0))
      # 15m & 1h down move, 1h high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1h"] > 30.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 60.0))
      # 15m & 1h down move, 1d high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1h"] > 40.0) | (df["AROONU_14_1d"] < 90.0))
      # 15m & 1h down move, 1h high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1h"] > 40.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 90.0))
      # 15m & 1h down move, 4h high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1h"] > 50.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 90.0))
      # 15m & 4h down move, 15m still high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_4h"] > 10.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 40.0))
      # 15m & 4h down move, 4h still high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_4h"] > 10.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 40.0))
      # 15m & 4h down move, 1h high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_4h"] > 15.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 90.0))
      # 15m & 4h down move, 1d downtrend
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_4h"] > 15.0) | (df["ROC_9_1d"] > -20.0))
      # 15m & 4h down move, 4h still high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_4h"] > 40.0) | (df["AROONU_14_4h"] < 50.0))
      # 15m & 4h down move, 4h high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_4h"] > 50.0) | (df["AROONU_14_4h"] < 70.0))
      # 15m & 1d down move, 4h high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1d"] > 20.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 70.0))
      # 15m down move, 15m still high, 1d downtrend
      & ((df["RSI_3_15m"] > 10.0) | (df["AROONU_14_15m"] < 40.0) | (df["ROC_9_1d"] > -30.0))
      # 15m down move, 15m still high, 1d overbought
      & ((df["RSI_3_15m"] > 10.0) | (df["AROONU_14_15m"] < 50.0) | (df["ROC_9_1d"] < 30.0))
      # 15m down move, 15m high, 1h high
      & ((df["RSI_3_15m"] > 10.0) | (df["AROONU_14_15m"] < 60.0) | (df["AROONU_14_1h"] < 80.0))
      # 15m down move, 15m high, 4h downtrend
      & ((df["RSI_3_15m"] > 10.0) | (df["AROONU_14_15m"] < 60.0) | (df["ROC_9_4h"] > -10.0))
      # 15m down move, 1h & 4h high
      & ((df["RSI_3_15m"] > 10.0) | (df["AROONU_14_1h"] < 90.0) | (df["AROONU_14_4h"] < 100.0))
      # 15m down move, 1h high, 1d downtrend
      & ((df["RSI_3_15m"] > 10.0) | (df["AROONU_14_1h"] < 90.0) | (df["ROC_9_1d"] > -40.0))
      # 15m down move, 4h & 1d high
      & ((df["RSI_3_15m"] > 10.0) | (df["AROONU_14_4h"] < 90.0) | (df["AROONU_14_1d"] < 100.0))
      # 15m down move, 1d high & overbought
      & ((df["RSI_3_15m"] > 10.0) | (df["AROONU_14_1d"] < 100.0) | (df["ROC_9_1d"] < 100.0))
      # 15m down move, 4h still high, 1d overbought
      & ((df["RSI_3_15m"] > 10.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 50.0) | (df["ROC_9_1d"] < 30.0))
      # 15m down move, 4h & 1d overbought
      & ((df["RSI_3_15m"] > 10.0) | (df["ROC_9_4h"] < 10.0) | (df["ROC_9_1d"] < 200.0))
      # 15m & 1h down move, 1h high
      & ((df["RSI_3_15m"] > 15.0) | (df["RSI_3_1h"] > 15.0) | (df["AROONU_14_1h"] < 90.0))
      # 15m & 1h down move, 1d high
      & ((df["RSI_3_15m"] > 15.0) | (df["RSI_3_1h"] > 15.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 90.0))
      # 15m & 1h down move, 1h high
      & ((df["RSI_3_15m"] > 15.0) | (df["RSI_3_1h"] > 20.0) | (df["AROONU_14_1h"] < 100.0))
      # 15m & 1h down move, 4h high
      & ((df["RSI_3_15m"] > 15.0) | (df["RSI_3_1h"] > 20.0) | (df["AROONU_14_4h"] < 100.0))
      # 15m & 4h down move, 4h high
      & ((df["RSI_3_15m"] > 15.0) | (df["RSI_3_4h"] > 40.0) | (df["AROONU_14_4h"] < 70.0))
      # 15m down move. 15m still high, 1h high
      & ((df["RSI_3_15m"] > 15.0) | (df["AROONU_14_15m"] < 50.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 80.0))
      # 15m down move, 15m & 4h high
      & ((df["RSI_3_15m"] > 15.0) | (df["AROONU_14_15m"] < 70.0) | (df["AROONU_14_4h"] < 100.0))
      # 15m down move, 1h high, 1d overbought
      & ((df["RSI_3_15m"] > 15.0) | (df["AROONU_14_1h"] < 80.0) | (df["ROC_9_1d"] < 40.0))
      # 15m down move, 4h high & overbought
      & ((df["RSI_3_15m"] > 15.0) | (df["AROONU_14_4h"] < 60.0) | (df["ROC_9_4h"] < 30.0))
      # 15m down move, 4h high, 1d overbought
      & ((df["RSI_3_15m"] > 15.0) | (df["AROONU_14_4h"] < 70.0) | (df["ROC_9_1d"] < 200.0))
      # 15m down move, 4h high, 1d overbought
      & ((df["RSI_3_15m"] > 15.0) | (df["AROONU_14_4h"] < 100.0) | (df["ROC_9_1d"] < 100.0))
      # 15m down move, 1h high, 4h downtrend
      & ((df["RSI_3_15m"] > 15.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 70.0) | (df["ROC_9_4h"] > -30.0))
      # 15m down move, 4h high & overbought
      & ((df["RSI_3_15m"] > 15.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 90.0) | (df["ROC_9_4h"] < 25.0))
      # 15m down move, 4h high, 1d downtrend
      & ((df["RSI_3_15m"] > 15.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 90.0) | (df["ROC_9_1d"] > -40.0))
      # 15m down move, 4h high, 1d overbought
      & ((df["RSI_3_15m"] > 15.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 90.0) | (df["ROC_9_1d"] < 30.0))
      # 15m down move, 1d high & overbought
      & ((df["RSI_3_15m"] > 15.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 90.0) | (df["ROC_9_1d"] < 100.0))
      # 15m down move, 4h & 1d downtrend
      & ((df["RSI_3_15m"] > 15.0) | (df["ROC_9_4h"] > -10.0) | (df["ROC_9_1d"] > -40.0))
      # 15m & 1h down move, 4h high
      & ((df["RSI_3_15m"] > 20.0) | (df["RSI_3_1h"] > 20.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 80.0))
      # 15m & 1h down move, 1d overbought
      & ((df["RSI_3_15m"] > 20.0) | (df["RSI_3_1h"] > 25.0) | (df["ROC_9_1d"] < 100.0))
      # 15m & 1d down move, 4h high
      & ((df["RSI_3_15m"] > 20.0) | (df["RSI_3_1d"] > 20.0) | (df["AROONU_14_4h"] < 90.0))
      # 15m down move, 15m & 1h high
      & ((df["RSI_3_15m"] > 20.0) | (df["AROONU_14_15m"] < 70.0) | (df["AROONU_14_1h"] < 100.0))
      # 15m down move, 1h high, 4h overbought
      & ((df["RSI_3_15m"] > 20.0) | (df["AROONU_14_1h"] < 80.0) | (df["ROC_9_4h"] < 10.0))
      # 15m down move, 1h high, 1d overbought
      & ((df["RSI_3_15m"] > 20.0) | (df["AROONU_14_1h"] < 80.0) | (df["ROC_9_1d"] < 10.0))
      # 15m down move, 4h high & overbought
      & ((df["RSI_3_15m"] > 20.0) | (df["AROONU_14_4h"] < 80.0) | (df["ROC_9_4h"] < 10.0))
      # 15m down move, 1d high & overbought
      & ((df["RSI_3_15m"] > 30.0) | (df["AROONU_14_1d"] < 100.0) | (df["ROC_9_1d"] < 50.0))
      # 1h & 4h down move, 1d still high
      & ((df["RSI_3_1h"] > 3.0) | (df["RSI_3_4h"] > 10.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 50.0))
      # 1h & 4h down move, 1d still high
      & ((df["RSI_3_1h"] > 3.0) | (df["RSI_3_4h"] > 15.0) | (df["AROONU_14_1d"] < 40.0))
      # 1h & 4h down move, 1d high
      & ((df["RSI_3_1h"] > 3.0) | (df["RSI_3_4h"] > 20.0) | (df["AROONU_14_1d"] < 60.0))
      # 1h & 4h down move, 1d high
      & ((df["RSI_3_1h"] > 3.0) | (df["RSI_3_4h"] > 25.0) | (df["AROONU_14_1d"] < 70.0))
      # 1h & 4h down move, 1d overbought
      & ((df["RSI_3_1h"] > 3.0) | (df["RSI_3_4h"] > 25.0) | (df["ROC_9_1d"] < 20.0))
      # 1h down move, 4h still high, 1d downtrend
      & ((df["RSI_3_1h"] > 3.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 50.0) | (df["ROC_9_1d"] > -20.0))
      # 1h & 4h down move, 1h still high
      & ((df["RSI_3_1h"] > 5.0) | (df["RSI_3_4h"] > 10.0) | (df["AROONU_14_1h"] < 50.0))
      # 1h & 4h down move, 1d high
      & ((df["RSI_3_1h"] > 5.0) | (df["RSI_3_4h"] > 15.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 90.0))
      # 1h & 4h down move, 1d high
      & ((df["RSI_3_1h"] > 5.0) | (df["RSI_3_4h"] > 20.0) | (df["AROONU_14_1d"] < 100.0))
      # 1h & 4h down move, 4h still high
      & ((df["RSI_3_1h"] > 5.0) | (df["RSI_3_4h"] > 35.0) | (df["RSI_14_4h"] < 40.0))
      # 1h down move, 4h high, 1d downtrend
      & ((df["RSI_3_1h"] > 5.0) | (df["AROONU_14_4h"] < 70.0) | (df["ROC_9_1d"] > -30.0))
      # 1h down move, 1d high, 1h downtrend
      & ((df["RSI_3_1h"] > 5.0) | (df["AROONU_14_1d"] < 90.0) | (df["ROC_9_1h"] > -40.0))
      # 1h down move, 4h & 1d downtrend
      & ((df["RSI_3_1h"] > 5.0) | (df["ROC_9_4h"] > -20.0) | (df["ROC_9_1d"] > -20.0))
      # 1h & 4h & 1d down move
      & ((df["RSI_3_1h"] > 10.0) | (df["RSI_3_4h"] > 10.0) | (df["RSI_3_1d"] > 15.0))
      # 1h & 4h down move, 1d downtrend
      & ((df["RSI_3_1h"] > 10.0) | (df["RSI_3_4h"] > 10.0) | (df["ROC_9_1d"] > -20.0))
      # 1h & 4h down move, 1h high
      & ((df["RSI_3_1h"] > 10.0) | (df["RSI_3_4h"] > 15.0) | (df["AROONU_14_1h"] < 60.0))
      # 1h & 4h down move, 1d high
      & ((df["RSI_3_1h"] > 10.0) | (df["RSI_3_4h"] > 15.0) | (df["AROONU_14_1d"] < 90.0))
      # 1h & 4h down move, 1d downtrend
      & ((df["RSI_3_1h"] > 10.0) | (df["RSI_3_4h"] > 15.0) | (df["ROC_9_1d"] > -30.0))
      # 1h & 1d down move, 4h high
      & ((df["RSI_3_1h"] > 10.0) | (df["RSI_3_1d"] > 15.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 70.0))
      # 1h & 1d down move, 1d still high
      & ((df["RSI_3_1h"] > 10.0) | (df["RSI_3_1d"] > 30.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 50.0))
      # 1h down move, 15m downtrend, 1d high
      & ((df["RSI_3_1h"] > 10.0) | (df["CMF_20_15m"] > -0.40) | (df["AROONU_14_1d"] < 70.0))
      # 1h down move, 1h high, 4h overbought
      & ((df["RSI_3_1h"] > 10.0) | (df["AROONU_14_1h"] < 80.0) | (df["ROC_9_4h"] < 10.0))
      # 1h down move, 1d high, 1d downtrend
      & ((df["RSI_3_1h"] > 10.0) | (df["AROONU_14_1d"] < 70.0) | (df["ROC_9_1d"] > -20.0))
      # 1h down move, 4h high, 1d downtrend
      & ((df["RSI_3_1h"] > 10.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 60.0) | (df["ROC_9_1d"] > -30.0))
      # 1h & 4h down move, 1h still not low enough
      & ((df["RSI_3_1h"] > 15.0) | (df["RSI_3_4h"] > 15.0) | (df["AROONU_14_1h"] < 20.0))
      # 1h & 4h down move, 4h high
      & ((df["RSI_3_1h"] > 15.0) | (df["RSI_3_4h"] > 15.0) | (df["AROONU_14_4h"] < 60.0))
      # 1h & 4h down move, 1h downtrend
      & ((df["RSI_3_1h"] > 15.0) | (df["RSI_3_4h"] > 15.0) | (df["ROC_9_1h"] > -15.0))
      # 1h & 4h down move, 1d overbought
      & ((df["RSI_3_1h"] > 15.0) | (df["RSI_3_4h"] > 15.0) | (df["ROC_9_1d"] < 10.0))
      # 1h & 4h down move, 4h still high
      & ((df["RSI_3_1h"] > 15.0) | (df["RSI_3_4h"] > 20.0) | (df["RSI_14_4h"] < 40.0))
      # 1h & 4h down move, 1h high
      & ((df["RSI_3_1h"] > 15.0) | (df["RSI_3_4h"] > 30.0) | (df["AROONU_14_1h"] < 70.0))
      # 1h & 4h down move, 1d high
      & ((df["RSI_3_1h"] > 15.0) | (df["RSI_3_4h"] > 40.0) | (df["AROONU_14_1d"] < 70.0))
      # 1h & 1d down move, 1d still high
      & ((df["RSI_3_1h"] > 15.0) | (df["RSI_3_1d"] > 25.0) | (df["AROONU_14_1d"] < 50.0))
      # 1h down move, 1h still high, 1d downtrend
      & ((df["RSI_3_1h"] > 15.0) | (df["AROONU_14_1h"] < 30.0) | (df["ROC_9_1d"] > -30.0))
      # 1h down move, 1h still high, 4h downtrend
      & ((df["RSI_3_1h"] > 15.0) | (df["AROONU_14_1h"] < 40.0) | (df["ROC_9_4h"] > -30.0))
      # 1h down move, 4h high & overbought
      & ((df["RSI_3_1h"] > 15.0) | (df["AROONU_14_4h"] < 80.0) | (df["ROC_9_4h"] < 10.0))
      # 1h & 4h down move, 1h still high
      & ((df["RSI_3_1h"] > 20.0) | (df["RSI_3_4h"] > 20.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 50.0))
      # 1h & 4h down move, 4h high
      & ((df["RSI_3_1h"] > 20.0) | (df["RSI_3_4h"] > 50.0) | (df["AROONU_14_4h"] < 75.0))
      # 1h down move, 1h high, 4h overbought
      & ((df["RSI_3_1h"] > 20.0) | (df["AROONU_14_1h"] < 70.0) | (df["ROC_9_4h"] < 10.0))
      # 1h down move, 1h high & overbought
      & ((df["RSI_3_1h"] > 20.0) | (df["AROONU_14_1d"] < 100.0) | (df["ROC_9_1d"] < 100.0))
      # 1h down move, 4h downtrend, 1d overbought
      & ((df["RSI_3_1h"] > 20.0) | (df["ROC_9_4h"] > -40.0) | (df["ROC_9_1d"] < 50.0))
      # 1h & 1d down move, 1h high
      & ((df["RSI_3_1h"] > 25.0) | (df["RSI_3_1d"] > 25.0) | (df["AROONU_14_1h"] < 80.0))
      # 1h down move, 1h high, 1d downtrend
      & ((df["RSI_3_1h"] > 25.0) | (df["AROONU_14_1h"] < 60.0) | (df["ROC_9_1d"] > -40.0))
      # 1h down move, 1h & 1d high
      & ((df["RSI_3_1h"] > 25.0) | (df["AROONU_14_1h"] < 70.0) | (df["AROONU_14_1d"] < 90.0))
      # 1h down move, 1h high & overbought
      & ((df["RSI_3_1h"] > 25.0) | (df["AROONU_14_1h"] < 80.0) | (df["ROC_9_1h"] < 10.0))
      # 1h down move, 1h high, 4h overbought
      & ((df["RSI_3_1h"] > 25.0) | (df["AROONU_14_1h"] < 80.0) | (df["ROC_9_4h"] < 50.0))
      # 1h down move, 4h & 1d high
      & ((df["RSI_3_1h"] > 25.0) | (df["AROONU_14_4h"] < 90.0) | (df["AROONU_14_1d"] < 100.0))
      # 1h down move, 1d high, 4h downtrend
      & ((df["RSI_3_1h"] > 25.0) | (df["AROONU_14_1d"] < 80.0) | (df["ROC_9_4h"] > -70.0))
      # 1h down move, 4h high, 1d downtrend
      & ((df["RSI_3_1h"] > 25.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 80.0) | (df["ROC_9_1d"] > -30.0))
      # 1h down move, 4h & 1d downtrend
      & ((df["RSI_3_1h"] > 25.0) | (df["ROC_9_4h"] > -30.0) | (df["ROC_9_1d"] > -60.0))
      # 1h & 4h down move, 1h high
      & ((df["RSI_3_1h"] > 30.0) | (df["RSI_3_4h"] > 40.0) | (df["AROONU_14_1h"] < 70.0))
      # 1h down move, 1h high, 1d overbought
      & ((df["RSI_3_1h"] > 30.0) | (df["AROONU_14_1h"] < 80.0) | (df["ROC_9_1d"] < 10.0))
      # 1h down move, 4h high, 1d overbought
      & ((df["RSI_3_1h"] > 30.0) | (df["AROONU_14_4h"] < 70.0) | (df["ROC_9_1d"] < 40.0))
      # 1h down move, 4h high & overbought
      & ((df["RSI_3_1h"] > 30.0) | (df["AROONU_14_4h"] < 80.0) | (df["ROC_9_4h"] < 30.0))
      # 1h down move, 1d high, 4h downtrend
      & ((df["RSI_3_1h"] > 30.0) | (df["AROONU_14_1d"] < 90.0) | (df["ROC_9_4h"] > -40.0))
      # 1h down move, 1d high, 4h overbought
      & ((df["RSI_3_1h"] > 30.0) | (df["AROONU_14_1d"] < 100.0) | (df["ROC_9_4h"] < 30.0))
      # 1h down move, 4h & 1d overbought
      & ((df["RSI_3_1h"] > 30.0) | (df["ROC_9_4h"] < 30.0) | (df["ROC_9_1d"] < 200.0))
      # 1h & 4h down move, 1d high
      & ((df["RSI_3_1h"] > 35.0) | (df["RSI_3_4h"] > 35.0) | (df["AROONU_14_1d"] < 90.0))
      # 1h down move, 1h high, 1d overbought
      & ((df["RSI_3_1h"] > 35.0) | (df["AROONU_14_1h"] < 90.0) | (df["ROC_9_1d"] < 80.0))
      # 1h down move, 1h & 4h high
      & ((df["RSI_3_1h"] > 35.0) | (df["AROONU_14_1h"] < 100.0) | (df["AROONU_14_4h"] < 100.0))
      # 1h down move, 1d high & overbought
      & ((df["RSI_3_1h"] > 35.0) | (df["AROONU_14_1d"] < 100.0) | (df["ROC_9_1d"] < 200.0))
      # 1h & 1d down move, 1h high
      & ((df["RSI_3_1h"] > 40.0) | (df["RSI_3_1d"] > 40.0) | (df["AROONU_14_1h"] < 90.0))
      # 1h down move, 1h high, 1d downtrend
      & ((df["RSI_3_1h"] > 40.0) | (df["AROONU_14_1h"] < 80.0) | (df["ROC_9_1d"] > -30.0))
      # 1h down move, 4h high, 1d overbought
      & ((df["RSI_3_1h"] > 40.0) | (df["AROONU_14_4h"] < 80.0) | (df["ROC_9_1d"] < 40.0))
      # 1h down move, 4h high & overbought
      & ((df["RSI_3_1h"] > 40.0) | (df["AROONU_14_4h"] < 90.0) | (df["ROC_9_4h"] < 20.0))
      # 1h down move, 4h high & overbought
      & ((df["RSI_3_1h"] > 40.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 80.0) | (df["ROC_9_4h"] < 20.0))
      # 1h down move, 1d high, 4h overbought
      & ((df["RSI_3_1h"] > 45.0) | (df["AROONU_14_1d"] < 100.0) | (df["ROC_9_4h"] < 40.0))
      # 1h down move, 1h high, 1d downtrend
      & ((df["RSI_3_1h"] > 50.0) | (df["AROONU_14_1h"] < 60.0) | (df["ROC_9_1d"] > -70.0))
      # 1h down move, 1h & 1d high
      & ((df["RSI_3_1h"] > 50.0) | (df["AROONU_14_1h"] < 80.0) | (df["AROONU_14_1d"] < 100.0))
      # 4h & 1d down move, 15m still high
      & ((df["RSI_3_4h"] > 3.0) | (df["RSI_3_1d"] > 15.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 40.0))
      # 4h & 1d down move, 1h still not low enough
      & ((df["RSI_3_4h"] > 3.0) | (df["RSI_3_1d"] > 15.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 30.0))
      # 4h down move, 4h still high
      & ((df["RSI_3_4h"] > 3.0) | (df["AROONU_14_4h"] < 50.0))
      # 4h down move, 1h still high, 4h downtrend
      & ((df["RSI_3_4h"] > 3.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 50.0) | (df["ROC_9_4h"] > -30.0))
      # 4h & 1d down move, 1d still high
      & ((df["RSI_3_4h"] > 5.0) | (df["RSI_3_1d"] > 30.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 40.0))
      # 4h down move, 1h & 4h downtrend
      & ((df["RSI_3_4h"] > 5.0) | (df["ROC_9_1h"] > -10.0) | (df["ROC_9_4h"] > -10.0))
      # 4h & 1d down move, 4h downtrend
      & ((df["RSI_3_4h"] > 10.0) | (df["RSI_3_1d"] > 10.0) | (df["ROC_9_4h"] > -20.0))
      # 4h & 1d down move, 1d downtrend
      & ((df["RSI_3_4h"] > 10.0) | (df["RSI_3_1d"] > 10.0) | (df["ROC_9_1d"] > -30.0))
      # 4h down move, 4h still high
      & ((df["RSI_3_4h"] > 10.0) | (df["AROONU_14_4h"] < 50.0))
      # 4h down move, 1d still high, 1d downtrend
      & ((df["RSI_3_4h"] > 10.0) | (df["AROONU_14_1d"] < 50.0) | (df["ROC_9_1d"] > -30.0))
      # 4h down move, 4h still not low enough, 1d downtrend
      & ((df["RSI_3_4h"] > 10.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 30.0) | (df["ROC_9_1d"] > -20.0))
      # 4h down move, 4h & 1d  downtrend
      & ((df["RSI_3_4h"] > 10.0) | (df["ROC_9_4h"] > -20.0) | (df["ROC_9_1d"] > -30.0))
      # 4h down move, 1h still high
      & ((df["RSI_3_4h"] > 15.0) | (df["AROONU_14_1h"] < 50.0))
      # 4h down move, 1h still high, 1d downtrend
      & ((df["RSI_3_4h"] > 15.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 50.0) | (df["ROC_9_1d"] > -30.0))
      # 4h down move, 4h still high, 1d downtrend
      & ((df["RSI_3_4h"] > 15.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 50.0) | (df["ROC_9_1d"] > -20.0))
      # 4h down move, 4h still high, 1d downtrend
      & ((df["RSI_3_4h"] > 20.0) | (df["AROONU_14_4h"] < 50.0) | (df["ROC_9_1d"] > -40.0))
      # 4h down move, 1d high & overbought
      & ((df["RSI_3_4h"] > 20.0) | (df["AROONU_14_1d"] < 70.0) | (df["ROC_9_1d"] < 50.0))
      # 4h & 1d down move, 1h high
      & ((df["RSI_3_4h"] > 25.0) | (df["RSI_3_1d"] > 25.0) | (df["AROONU_14_1h"] < 90.0))
      # 4h down move, 4h still high, 1d downtrend
      & ((df["RSI_3_4h"] > 30.0) | (df["AROONU_14_4h"] < 50.0) | (df["ROC_9_1d"] > -40.0))
      # 4h down move, 1d high, 1d downtrend
      & ((df["RSI_3_4h"] > 35.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 60.0) | (df["ROC_9_1d"] > -30.0))
      # 4h down move, 1d high, 1d downtrend
      & ((df["RSI_3_4h"] > 45.0) | (df["AROONU_14_1d"] < 80.0) | (df["ROC_9_1d"] > -15.0))
      # 4h down move, 4h still high, 1d downtrend
      & ((df["RSI_3_4h"] > 50.0) | (df["RSI_14_4h"] < 40.0) | (df["ROC_9_1d"] > -30.0))
      # 1d down move, 4h high, 1d downtrend
      & ((df["RSI_3_1d"] > 15.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 70.0) | (df["ROC_9_1d"] > -70.0))
      # 1d down move, 1h high & overbought
      & ((df["RSI_3_1d"] > 35.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 90.0) | (df["ROC_9_1h"] < 10.0))
      # 1d down move, 1h high & overbought
      & ((df["RSI_3_1d"] > 40.0) | (df["AROONU_14_1d"] < 70.0) | (df["ROC_9_1d"] < 80.0))
      # 4h downtrend, 1h & 4h high
      & ((df["CMF_20_4h"] > -0.30) | (df["AROONU_14_1h"] < 70.0) | (df["AROONU_14_4h"] < 100.0))
      # 15m still high, 1h & 4h overbought
      & ((df["AROONU_14_15m"] < 50.0) | (df["ROC_9_1h"] < 100.0) | (df["ROC_9_4h"] < 100.0))
      # 15m & 1d high, 1d overbought
      & ((df["AROONU_14_15m"] < 70.0) | (df["AROONU_14_1d"] < 90.0) | (df["ROC_9_1d"] < 30.0))
      # 1h still high, 4h & 1d downtrend
      & ((df["AROONU_14_1h"] < 40.0) | (df["ROC_9_4h"] > -20.0) | (df["ROC_9_1d"] > -40.0))
      # 1h & 4h high, 1d downtrend
      & ((df["AROONU_14_1h"] < 70.0) | (df["AROONU_14_4h"] < 100.0) | (df["ROC_9_1d"] > -20.0))
      # 1h & 4h high, 1d overbought
      & ((df["AROONU_14_1h"] < 70.0) | (df["AROONU_14_4h"] < 100.0) | (df["ROC_9_1d"] < 20.0))
      # 1h & 1d high, 1d overbought
      & ((df["AROONU_14_1h"] < 70.0) | (df["AROONU_14_1d"] < 90.0) | (df["ROC_9_1d"] < 200.0))
      # 1h high, 4h downtrend, 1d overbought
      & ((df["AROONU_14_1h"] < 70.0) | (df["ROC_9_4h"] > -40.0) | (df["ROC_9_1d"] < 100.0))
      # 1h & 4h high, 4h overbought
      & ((df["AROONU_14_1h"] < 80.0) | (df["AROONU_14_4h"] < 100.0) | (df["ROC_9_4h"] < 30.0))
      # 1h high, 1d downtrend
      & ((df["AROONU_14_1h"] < 80.0) | (df["ROC_9_1d"] > -60.0))
      # 1h high, 1h & 4h overbought
      & ((df["AROONU_14_1h"] < 100.0) | (df["ROC_9_1h"] < 100.0) | (df["ROC_9_4h"] < 100.0))
      # 4h & 1d high, 1d overbought
      & ((df["AROONU_14_4h"] < 60.0) | (df["AROONU_14_1d"] < 100.0) | (df["ROC_9_1d"] < 70.0))
      # 4h high, 1h & 4h overbought
      & ((df["AROONU_14_4h"] < 85.0) | (df["ROC_9_1h"] < 80.0) | (df["ROC_9_4h"] < 80.0))
      # 4h high, 1h downtrend, 4h overbought
      & ((df["AROONU_14_4h"] < 90.0) | (df["ROC_9_1h"] > -40.0) | (df["ROC_9_4h"] < 100.0))
      # 4h & 1d high, 4h overbought
      & ((df["AROONU_14_4h"] < 90.0) | (df["AROONU_14_1d"] < 100.0) | (df["ROC_9_4h"] < 100.0))
      # 4h high, 1h & 4h overbought
      & ((df["AROONU_14_4h"] < 90.0) | (df["ROC_9_1h"] < 10.0) | (df["ROC_9_4h"] < 20.0))
      # 4h & 1d high, 4h overbought
      & ((df["AROONU_14_4h"] < 100.0) | (df["AROONU_14_1d"] < 100.0) | (df["ROC_9_4h"] < 30.0))
      # 4h & 1d high, 1d overbought
      & ((df["AROONU_14_4h"] < 100.0) | (df["AROONU_14_1d"] < 100.0) | (df["ROC_9_1d"] < 40.0))
      # 1d high, 1h & 4h downtrend
      & ((df["AROONU_14_1d"] < 100.0) | (df["ROC_9_1h"] > -30.0) | (df["ROC_9_4h"] > -30.0))
      # 1d high, 4h & 1d overbought
      & ((df["AROONU_14_1d"] < 100.0) | (df["ROC_9_4h"] < 20.0) | (df["ROC_9_1d"] < 100.0))
      # 1h high, 1d overbought
      & ((df["STOCHRSIk_14_14_3_3_1h"] < 70.0) | (df["ROC_9_1d"] < 40.0))
      # 1h high, 4h overbought
      & ((df["STOCHRSIk_14_14_3_3_1h"] < 80.0) | (df["ROC_9_4h"] < 80.0))
      # 1h high, 4h & 1d downtrend
      & ((df["STOCHRSIk_14_14_3_3_1h"] < 85.0) | (df["ROC_9_4h"] > -70.0) | (df["ROC_9_1d"] > -70.0))
      # 4h high, 1h & 4h overbought
      & ((df["STOCHRSIk_14_14_3_3_4h"] < 80.0) | (df["ROC_9_1h"] < 40.0) | (df["ROC_9_4h"] < 100.0))
      # 1d high, 4h & 1d overbought
      & ((df["STOCHRSIk_14_14_3_3_1d"] < 90.0) | (df["ROC_9_4h"] < 20.0) | (df["ROC_9_1d"] < 100.0))
      # 1h & 4h overbought, 1d downtrend
      & ((df["ROC_9_1h"] < 40.0) | (df["ROC_9_4h"] < 50.0) | (df["ROC_9_1d"] > -30.0))
      # big drop in the last 20 days, 1d high, 1d downtrend
      & (
        (df["close"] > (df["high_max_20_1d"] * 0.20))
        | (df["STOCHRSIk_14_14_3_3_1d"] < 70.0)
        | (df["ROC_9_1d"] > -15.0)
      )
    )

    # Logic
    long_entry_logic.append(
      (df["RSI_14"] < 40.0)
      & (df["MFI_14"] < 40.0)
      & (df["AROONU_14"] < 25.0)
      & (df["EMA_26"] > df["EMA_12"])
      & ((df["EMA_26"] - df["EMA_12"]) > (df["open"] * 0.024))
      & ((df["EMA_26"].shift() - df["EMA_12"].shift()) > (df["open"] / 100.0))
      & (df["close"] < (df["EMA_20"] * 0.960))
      & (df["close"] < (df["BBL_20_2.0"] * 0.999))
    )


def append_long_44(df, long_entry_logic, allowed_empty_candles_288) -> None:
    """Append NFI long condition #44, a quick-mode long entry."""
    long_entry_logic.append(df["num_empty_288"] <= allowed_empty_candles_288)
    # long_entry_logic.append(df["protections_long_global"] == True)

    long_entry_logic.append(
      # 5m & 1h & 4h down move
      ((df["RSI_3"] > 3.0) | (df["RSI_3_1h"] > 15.0) | (df["RSI_3_4h"] > 15.0))
      # 15m & 1h & 4h down move
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_1h"] > 3.0) | (df["RSI_3_4h"] > 10.0))
      # 15m & 1h down move, 1h high
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_1h"] > 3.0) | (df["AROONU_14_1h"] < 60.0))
      # 15m & 1h & 4h down move
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_1h"] > 5.0) | (df["RSI_3_4h"] > 10.0))
      # 15m & 1h down move, 1d downtrend
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_1h"] > 5.0) | (df["ROC_9_1d"] > -30.0))
      # 15m & 1h down move, 1d high
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_1h"] > 10.0) | (df["AROONU_14_1d"] < 100.0))
      # 15m & 1h down move, 1h high
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_1h"] > 20.0) | (df["AROONU_14_1h"] < 80.0))
      # 15m & 4h down move, 4h still high
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_4h"] > 10.0) | (df["AROONU_14_4h"] < 40.0))
      # 15m & 4h down move, 15m downtrend
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_4h"] > 10.0) | (df["ROC_9_15m"] > -30.0))
      # 15m & 4h down move, 1h downtrend
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_4h"] > 10.0) | (df["ROC_9_1h"] > -20.0))
      # 15m & 4h down move, 1h still high
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_4h"] > 15.0) | (df["AROONU_14_1h"] < 50.0))
      # 15m & 4h down move, 1h still high
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_4h"] > 40.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 40.0))
      # 15m down move, 1h still high, 1d overbought
      & ((df["RSI_3_15m"] > 3.0) | (df["AROONU_14_1h"] < 40.0) | (df["ROC_9_1d"] < 70.0))
      # 15m down move, 4h high & overbought
      & ((df["RSI_3_15m"] > 3.0) | (df["AROONU_14_4h"] < 100.0) | (df["ROC_9_4h"] < 100.0))
      # 15m down move, 1h high
      & ((df["RSI_3_15m"] > 3.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 70.0))
      # 15m down move, 4h high, 15m downtrend
      & ((df["RSI_3_15m"] > 3.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 70.0) | (df["ROC_9_15m"] > -30.0))
      # 15m & 1h down move, 1h high
      & ((df["RSI_3_15m"] > 5.0) | (df["RSI_3_1h"] > 15.0) | (df["AROONU_14_1h"] < 70.0))
      # 15m & 1h down move, 1h downtrend
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1h"] > 10.0) | (df["ROC_9_1h"] > -20.0))
      # 15m & 4h down move, 1h still not low enough
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_4h"] > 10.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 30.0))
      # 15m down move, 4h overbought
      & ((df["RSI_3_15m"] > 10.0) | (df["ROC_9_4h"] < 30.0))
      # 15m & 4h down move, 4h high
      & ((df["RSI_3_15m"] > 15.0) | (df["RSI_3_4h"] > 25.0) | (df["AROONU_14_4h"] < 70.0))
      # 15m & 4h down move, 4h high
      & ((df["RSI_3_15m"] > 15.0) | (df["RSI_3_4h"] > 40.0) | (df["AROONU_14_4h"] < 75.0))
      # 15m & 4h down move, 4h high
      & ((df["RSI_3_15m"] > 15.0) | (df["RSI_3_4h"] > 45.0) | (df["AROONU_14_4h"] < 90.0))
      # 15m down move, 4h & 1d downtrend
      & ((df["RSI_3_15m"] > 15.0) | (df["ROC_9_4h"] > -10.0) | (df["ROC_9_1d"] > -40.0))
      # 15m down move, 1h high & overbought
      & ((df["RSI_3_15m"] > 25.0) | (df["AROONU_14_1d"] < 90.0) | (df["ROC_9_1d"] < 100.0))
      # 1h & 4h down move, 1h still not low enough
      & ((df["RSI_3_1h"] > 3.0) | (df["RSI_3_4h"] > 3.0) | (df["AROONU_14_1h"] < 20.0))
      # 1h & 4h down move
      & ((df["RSI_3_1h"] > 3.0) | (df["RSI_3_4h"] > 5.0))
      # 1h & 4h down move, 1d still high
      & ((df["RSI_3_1h"] > 3.0) | (df["RSI_3_4h"] > 10.0) | (df["AROONU_14_1d"] < 50.0))
      # 1h & 4h down move, 1d high
      & ((df["RSI_3_1h"] > 3.0) | (df["RSI_3_4h"] > 10.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 60.0))
      # 1h & 4h down move, 1d high
      & ((df["RSI_3_1h"] > 3.0) | (df["RSI_3_4h"] > 20.0) | (df["AROONU_14_1d"] < 60.0))
      # 1h & 4h down move, 4h high
      & ((df["RSI_3_1h"] > 3.0) | (df["RSI_3_4h"] > 20.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 60.0))
      # 1h down move, 1h & 4h still high
      & ((df["RSI_3_1h"] > 3.0) | (df["AROONU_14_1h"] < 50.0) | (df["AROONU_14_4h"] < 50.0))
      # 1h down move, 1h still high, 1h downtrend
      & ((df["RSI_3_1h"] > 3.0) | (df["AROONU_14_1h"] < 50.0) | (df["ROC_9_1h"] > -20.0))
      # 1h down move, 4h still high, 1d downtrend
      & ((df["RSI_3_1h"] > 3.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 50.0) | (df["ROC_9_1h"] > -15.0))
      # 1h downtrend, 4h high
      & ((df["RSI_3_1h"] > 3.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 70.0))
      # 1h down move, 1h & 4h downtrend
      & ((df["RSI_3_1h"] > 3.0) | (df["ROC_9_1h"] > -20.0) | (df["ROC_9_4h"] > -20.0))
      # 1h & 4h down move, 4h still high
      & ((df["RSI_3_1h"] > 5.0) | (df["RSI_3_4h"] > 10.0) | (df["AROONU_14_4h"] < 50.0))
      # 1h & 4h down move, 1d high
      & ((df["RSI_3_1h"] > 5.0) | (df["RSI_3_4h"] > 10.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 90.0))
      # 1h & 4h down move, 4h still high
      & ((df["RSI_3_1h"] > 5.0) | (df["RSI_3_4h"] > 30.0) | (df["RSI_14_4h"] < 40.0))
      # 1h & 1d down move, 1d downtrend
      & ((df["RSI_3_1h"] > 5.0) | (df["RSI_3_1d"] > 5.0) | (df["ROC_9_1d"] > -20.0))
      # 1h down move, 1h high
      & ((df["RSI_3_1h"] > 5.0) | (df["AROONU_14_1h"] < 60.0))
      # 1h down move, 4h high
      & ((df["RSI_3_1h"] > 5.0) | (df["AROONU_14_4h"] < 70.0))
      # 1h down move, 1d high & overbought
      & ((df["RSI_3_1h"] > 5.0) | (df["AROONU_14_1d"] < 90.0) | (df["ROC_9_1d"] < 30.0))
      # 1h down move, 4h & 1d downtrend
      & ((df["RSI_3_1h"] > 5.0) | (df["ROC_9_4h"] > -20.0) | (df["ROC_9_1d"] > -25.0))
      # 1h down move, 1d overbought
      & ((df["RSI_3_1h"] > 5.0) | (df["ROC_9_1d"] < 100.0))
      # 1h & 4h down move, 1d downtrend
      & ((df["RSI_3_1h"] > 10.0) | (df["RSI_3_4h"] > 10.0) | (df["ROC_9_1d"] > -20.0))
      # 1h & 4h down move, 4h still high
      & ((df["RSI_3_1h"] > 10.0) | (df["RSI_3_4h"] > 15.0) | (df["RSI_14_4h"] < 40.0))
      # 1h & 4h down move, 1h still high
      & ((df["RSI_3_1h"] > 10.0) | (df["RSI_3_4h"] > 15.0) | (df["AROONU_14_1h"] < 50.0))
      # 1h & 4h down move, 4h still high
      & ((df["RSI_3_1h"] > 10.0) | (df["RSI_3_4h"] > 20.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 50.0))
      # 1h & 4h down move, 1d downtrend
      & ((df["RSI_3_1h"] > 10.0) | (df["RSI_3_4h"] > 20.0) | (df["ROC_9_1d"] > -40.0))
      # 1h & 4h down move, 1h downtrend
      & ((df["RSI_3_1h"] > 10.0) | (df["RSI_3_4h"] > 20.0) | (df["ROC_9_1h"] > -25.0))
      # 1h & 4h down move, 4h high
      & ((df["RSI_3_1h"] > 10.0) | (df["RSI_3_4h"] > 25.0) | (df["AROONU_14_4h"] < 70.0))
      # 1h & 4h down move, 1h high
      & ((df["RSI_3_1h"] > 10.0) | (df["RSI_3_4h"] > 60.0) | (df["AROONU_14_1h"] < 70.0))
      # 1h & 1d down move, 4h still high
      & ((df["RSI_3_1h"] > 10.0) | (df["RSI_3_1d"] > 10.0) | (df["AROONU_14_4h"] < 40.0))
      # 1h & 1d down move, 1h still high
      & ((df["RSI_3_1h"] > 10.0) | (df["RSI_3_1d"] > 15.0) | (df["AROONU_14_1h"] < 50.0))
      # 1h & 1d down move, 1h high
      & ((df["RSI_3_1h"] > 10.0) | (df["RSI_3_1d"] > 40.0) | (df["AROONU_14_1h"] < 70.0))
      # 1h down move, 1h still high, 4h downtrend
      & ((df["RSI_3_1h"] > 10.0) | (df["AROONU_14_1h"] < 40.0) | (df["ROC_9_4h"] > -30.0))
      # 1h down move, 1h still high, 1d high
      & ((df["RSI_3_1h"] > 10.0) | (df["AROONU_14_1h"] < 50.0) | (df["AROONU_14_1d"] < 90.0))
      # 1h down move, 1h high, 1h downtrend
      & ((df["RSI_3_1h"] > 10.0) | (df["AROONU_14_1h"] < 60.0) | (df["ROC_9_1h"] > -10.0))
      # 1h down move, 1h high, 1d downtrend
      & ((df["RSI_3_1h"] > 10.0) | (df["AROONU_14_1h"] < 70.0) | (df["ROC_9_1d"] > -30.0))
      # 1h down move, 1h high
      & ((df["RSI_3_1h"] > 10.0) | (df["AROONU_14_1h"] < 80.0))
      # 1h down move, 4h still high, 15m downtrend
      & ((df["RSI_3_1h"] > 10.0) | (df["AROONU_14_4h"] < 50.0) | (df["CMF_20_15m"] > -0.40))
      # 1h down move, 4h still high, 4h downtrend
      & ((df["RSI_3_1h"] > 10.0) | (df["AROONU_14_4h"] < 50.0) | (df["ROC_9_4h"] > -30.0))
      # 1h down move, 4h still high, 1d downtrend
      & ((df["RSI_3_1h"] > 10.0) | (df["AROONU_14_4h"] < 50.0) | (df["ROC_9_1d"] > -30.0))
      # 1h down move, 4h & 1d high
      & ((df["RSI_3_1h"] > 10.0) | (df["AROONU_14_4h"] < 60.0) | (df["AROONU_14_1d"] < 100.0))
      # 1h down move, 4h high, 1d overbought
      & ((df["RSI_3_1h"] > 10.0) | (df["AROONU_14_4h"] < 90.0) | (df["ROC_9_1d"] < 100.0))
      # 1h down move, 4h high
      & ((df["RSI_3_1h"] > 10.0) | (df["AROONU_14_4h"] < 100.0))
      # 1h down move, 1d high & overbought
      & ((df["RSI_3_1h"] > 10.0) | (df["AROONU_14_1d"] < 100.0) | (df["ROC_9_1d"] < 60.0))
      # 1h down move, 4h overbought
      & ((df["RSI_3_1h"] > 10.0) | (df["ROC_9_4h"] < 10.0))
      # 1h down move, 4h high & overbought
      & ((df["RSI_3_1h"] > 10.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 80.0) | (df["ROC_9_4h"] < 20.0))
      # 1h down move, 4h & 1d downtrend
      & ((df["RSI_3_1h"] > 10.0) | (df["ROC_9_4h"] > -30.0) | (df["ROC_9_1d"] > -50.0))
      # 1h & 4h down move, 4h high
      & ((df["RSI_3_1h"] > 15.0) | (df["RSI_3_4h"] > 45.0) | (df["AROONU_14_4h"] < 80.0))
      # 1h down move, 1h high, 1d downtrend
      & ((df["RSI_3_1h"] > 15.0) | (df["AROONU_14_1h"] < 50.0) | (df["ROC_9_1d"] > -40.0))
      # 1h down move, 1h & 1d high
      & ((df["RSI_3_1h"] > 15.0) | (df["AROONU_14_1h"] < 60.0) | (df["AROONU_14_1d"] < 85.0))
      # 1h down move, 1h high, 1d downtrend
      & ((df["RSI_3_1h"] > 15.0) | (df["AROONU_14_1h"] < 60.0) | (df["ROC_9_1d"] > -30.0))
      # 1h down move, 1h high, 1d overbought
      & ((df["RSI_3_1h"] > 15.0) | (df["AROONU_14_1h"] < 60.0) | (df["ROC_9_1d"] < 50.0))
      # 1h down move, 1h high, 4h downtrend
      & ((df["RSI_3_1h"] > 15.0) | (df["AROONU_14_1h"] < 70.0) | (df["ROC_9_4h"] > -10.0))
      # 1h down move, 4h high & overbought
      & ((df["RSI_3_1h"] > 15.0) | (df["AROONU_14_4h"] < 80.0) | (df["ROC_9_4h"] < 100.0))
      # 1h down move, 1d high & overbought
      & ((df["RSI_3_1h"] > 15.0) | (df["AROONU_14_1d"] < 80.0) | (df["ROC_9_1d"] < 100.0))
      # 1h down move, 1h & 4h downtrend
      & ((df["RSI_3_1h"] > 15.0) | (df["ROC_9_1h"] > -30.0) | (df["ROC_9_4h"] > -30.0))
      # 1h down move, 1h & 4h overbought
      & ((df["RSI_3_1h"] > 15.0) | (df["ROC_9_4h"] < 10.0) | (df["ROC_9_1d"] < 50.0))
      # 1h down move, 1h & 4h overbought
      & ((df["RSI_3_1h"] > 15.0) | (df["ROC_9_4h"] < 20.0) | (df["ROC_9_1d"] < 20.0))
      # 1h & 4h down move, 4h high
      & ((df["RSI_3_1h"] > 20.0) | (df["RSI_3_4h"] > 50.0) | (df["AROONU_14_4h"] < 90.0))
      # 1h down move, 1h still high, 4h downtrend
      & ((df["RSI_3_1h"] > 20.0) | (df["AROONU_14_1h"] < 40.0) | (df["ROC_9_4h"] > -30.0))
      # 1h down move, 4h high, 1d downtrend
      & ((df["RSI_3_1h"] > 20.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 80.0) | (df["ROC_9_1d"] > -40.0))
      # 1h down move, 4h & 1d downtrend
      & ((df["RSI_3_1h"] > 20.0) | (df["ROC_9_4h"] > -30.0) | (df["ROC_9_1d"] > -40.0))
      # 1h & 4h down ove, 4h high
      & ((df["RSI_3_1h"] > 25.0) | (df["RSI_3_4h"] > 45.0) | (df["AROONU_14_4h"] < 90.0))
      # 1h down move, 1h & 1d high
      & ((df["RSI_3_1h"] > 25.0) | (df["AROONU_14_1h"] < 70.0) | (df["AROONU_14_1d"] < 80.0))
      # 1h down move, 4h high, 1d downtrend
      & ((df["RSI_3_1h"] > 25.0) | (df["AROONU_14_4h"] < 80.0) | (df["ROC_9_1d"] > -20.0))
      # 1h down move, 1d high & overbought
      & ((df["RSI_3_1h"] > 25.0) | (df["AROONU_14_1d"] < 90.0) | (df["ROC_9_1d"] < 100.0))
      # 1h down move, 1h still high, 1d overbought
      & ((df["RSI_3_1h"] > 25.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 50.0) | (df["ROC_9_1d"] < 40.0))
      # 1h down move, 1h downtrend, 4h overbought
      & ((df["RSI_3_1h"] > 25.0) | (df["ROC_9_1h"] > -20.0) | (df["ROC_9_4h"] < 20.0))
      # 1h down move, 1d overbought
      & ((df["RSI_3_1h"] > 25.0) | (df["ROC_9_1d"] < 200.0))
      # 1h down move, 4h high
      & ((df["RSI_3_1h"] > 30.0) | (df["AROONU_14_4h"] < 100.0))
      # 1h down move, 4h high & overbought
      & ((df["RSI_3_1h"] > 30.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 80.0) | (df["ROC_9_4h"] < 10.0))
      # 4h down move, 4h still high, 1d high
      & ((df["RSI_3_4h"] > 3.0) | (df["AROONU_14_4h"] < 50.0) | (df["AROONU_14_1d"] < 100.0))
      # 4h down move, 1d still high, 4h downtrend
      & ((df["RSI_3_4h"] > 3.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 50.0) | (df["ROC_9_4h"] > -30.0))
      # 4h down move, 1d overbought
      & ((df["RSI_3_4h"] > 3.0) | (df["ROC_9_1d"] < 200.0))
      # 4h down move, 1h still high
      & ((df["RSI_3_4h"] > 5.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 40.0))
      # 4h down move, 1h & 4h downtrend
      & ((df["RSI_3_4h"] > 5.0) | (df["ROC_9_1h"] > -15.0) | (df["ROC_9_4h"] > -20.0))
      # 4h down move, 4h downtrend
      & ((df["RSI_3_4h"] > 5.0) | (df["ROC_9_4h"] > -40.0))
      # 4h & 1d down move, 1d high
      & ((df["RSI_3_4h"] > 10.0) | (df["RSI_3_1d"] > 20.0) | (df["AROONU_14_1d"] < 80.0))
      # 4h down move, 1d high, 4h downtrend
      & ((df["RSI_3_4h"] > 10.0) | (df["AROONU_14_1d"] < 90.0) | (df["ROC_9_4h"] > -20.0))
      # 4h down move, 1h & 4h downtrend
      & ((df["RSI_3_4h"] > 10.0) | (df["ROC_9_1h"] > -30.0) | (df["ROC_9_4h"] > -30.0))
      # 4h down move, 4h still not low enough, 1d overbought
      & ((df["RSI_3_4h"] > 15.0) | (df["AROONU_14_4h"] < 30.0) | (df["ROC_9_1d"] < 50.0))
      # 4h down move, 4h high
      & ((df["RSI_3_4h"] > 15.0) | (df["AROONU_14_4h"] < 60.0))
      # 4h down move, 4h still high, 1d overbought
      & ((df["RSI_3_4h"] > 15.0) | (df["AROONU_14_4h"] < 40.0) | (df["ROC_9_1d"] < 40.0))
      # 15m down move, 4h still high, 1d downtrend
      & ((df["RSI_3_4h"] > 15.0) | (df["AROONU_14_4h"] < 50.0) | (df["ROC_9_1d"] > -40.0))
      # 4h down move, 1d high & overbought
      & ((df["RSI_3_4h"] > 15.0) | (df["AROONU_14_1d"] < 80.0) | (df["ROC_9_1d"] < 80.0))
      # 4h down move, 4h still high, 1d downtrend
      & ((df["RSI_3_4h"] > 30.0) | (df["AROONU_14_4h"] < 50.0) | (df["ROC_9_1d"] > -40.0))
      # 4h down move, 4h & 1d high
      & ((df["RSI_3_4h"] > 30.0) | (df["AROONU_14_4h"] < 80.0) | (df["AROONU_14_1d"] < 100.0))
      # 4h down move, 1d high & overbought
      & ((df["RSI_3_4h"] > 30.0) | (df["AROONU_14_1d"] < 100.0) | (df["ROC_9_1d"] < 30.0))
      # 4h down move, 1h high & overbought
      & ((df["RSI_3_4h"] > 35.0) | (df["AROONU_14_1d"] < 90.0) | (df["ROC_9_1d"] < 100.0))
      # 4h down move, 4h still high, 1d downtrend
      & ((df["RSI_3_4h"] > 50.0) | (df["RSI_14_4h"] < 40.0) | (df["ROC_9_1d"] > -30.0))
      # 4h down move, 4h high, 1d overbought
      & ((df["RSI_3_4h"] > 50.0) | (df["AROONU_14_4h"] < 70.0) | (df["ROC_9_1d"] < 40.0))
      # 4h down move, 4h high
      & ((df["RSI_3_4h"] > 50.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 70.0))
      # 4h down move, 4h overbought
      & ((df["RSI_3_4h"] > 50.0) | (df["ROC_9_4h"] < 60.0))
      # 4h downtrend, 4h high
      & ((df["CMF_20_4h"] > -0.50) | (df["AROONU_14_4h"] < 70.0))
      # 1h & 1d high, 4h downtrend
      & ((df["AROONU_14_1h"] < 40.0) | (df["AROONU_14_1d"] < 70.0) | (df["ROC_9_4h"] > -20.0))
      # 1h still high, 1h & 4h downtrend
      & ((df["AROONU_14_1h"] < 40.0) | (df["ROC_9_1h"] > -20.0) | (df["ROC_9_4h"] > -30.0))
      # 1h & 4h high, 1d overbought
      & ((df["AROONU_14_1h"] < 70.0) | (df["AROONU_14_4h"] < 100.0) | (df["ROC_9_1d"] < 20.0))
      # 1h high, 4h & 1d downtrend
      & ((df["AROONU_14_1h"] < 70.0) | (df["ROC_9_4h"] > -20.0) | (df["ROC_9_1d"] > -50.0))
      # 1h high, 4h downtrend
      & ((df["AROONU_14_1h"] < 70.0) | (df["ROC_9_4h"] > -40.0))
      # 1h & 1d high, 1d overbought
      & ((df["AROONU_14_1h"] < 80.0) | (df["AROONU_14_1d"] < 90.0) | (df["ROC_9_1d"] < 80.0))
      # 1h & 1d high, 1h downtrend
      & ((df["AROONU_14_1h"] < 80.0) | (df["AROONU_14_1d"] < 100.0) | (df["ROC_9_1h"] > -20.0))
      # 4h & 1d high, 1h downtrend
      & ((df["AROONU_14_4h"] < 80.0) | (df["AROONU_14_1d"] < 100.0) | (df["ROC_9_1h"] > -30.0))
      # 4h & 1d high, 4h overbought
      & ((df["AROONU_14_4h"] < 80.0) | (df["AROONU_14_1d"] < 100.0) | (df["ROC_9_4h"] < 40.0))
      # 4h high, 1h downtrend
      & ((df["AROONU_14_4h"] < 80.0) | (df["ROC_9_1h"] > -40.0))
      # 4h high & overbought
      & ((df["AROONU_14_4h"] < 80.0) | (df["ROC_9_4h"] < 100.0))
      # 4h high, 1d downtrend
      & ((df["AROONU_14_4h"] < 80.0) | (df["ROC_9_1d"] > -30.0))
      # 1d still high, 1d downtrend
      & ((df["AROONU_14_1d"] < 50.0) | (df["ROC_9_1d"] > -30.0))
      # 1d high, 15m downtrend
      & ((df["AROONU_14_1d"] < 70.0) | (df["ROC_9_15m"] > -50.0))
      # 1d high, 1h downtrend
      & ((df["AROONU_14_1d"] < 70.0) | (df["ROC_9_1h"] > -70.0))
      # 1d high, 4h downtrend
      & ((df["AROONU_14_1d"] < 80.0) | (df["ROC_9_4h"] > -70.0))
      # 1d high, 4h downtrend
      & ((df["AROONU_14_1d"] < 90.0) | (df["ROC_9_4h"] > -40.0))
      # 1d high & overbought
      & ((df["AROONU_14_1d"] < 90.0) | (df["ROC_9_1d"] < 200.0))
      # 1d high, 4h & 1d overbought
      & ((df["AROONU_14_1d"] < 100.0) | (df["ROC_9_4h"] < 20.0) | (df["ROC_9_1d"] < 80.0))
      # 1h still high, 4h & 1d downtrend
      & ((df["STOCHRSIk_14_14_3_3_1h"] < 50.0) | (df["ROC_9_4h"] > -20.0) | (df["ROC_9_1d"] > -50.0))
      # 1h high, 15m downtrend
      & ((df["STOCHRSIk_14_14_3_3_1h"] < 70.0) | (df["ROC_9_15m"] > -30.0))
      # 4h high, 1d downtrend
      & ((df["STOCHRSIk_14_14_3_3_4h"] < 70.0) | (df["ROC_9_1d"] > -70.0))
      # 1d high, 1h downtrend
      & ((df["STOCHRSIk_14_14_3_3_1d"] < 90.0) | (df["ROC_9_1h"] > -20.0))
      # 1d high, 1d downtrend
      & ((df["STOCHRSIk_14_14_3_3_1d"] < 60.0) | (df["ROC_9_1d"] > -30.0))
      # 15m downtrend, 1d overbought
      & ((df["ROC_9_15m"] > -60.0) | (df["ROC_9_1d"] < 200.0))
      # 1h downtrend, 1d overbought
      & ((df["ROC_9_1h"] > -60.0) | (df["ROC_9_1d"] < 200.0))
      # big drop in the last 20 days, 1d high, 1d downtrend
      & (
        (df["close"] > (df["high_max_20_1d"] * 0.20))
        | (df["STOCHRSIk_14_14_3_3_1d"] < 70.0)
        | (df["ROC_9_1d"] > -15.0)
      )
    )

    # Logic
    long_entry_logic.append(
      (df["RSI_3"] < 40.0)
      & (df["RSI_3_15m"] < 50.0)
      & (df["AROONU_14_15m"] < 25.0)
      & (df["STOCHRSIk_14_14_3_3_15m"] < 20.0)
      & (df["EMA_26_15m"] > df["EMA_12_15m"])
      & ((df["EMA_26_15m"] - df["EMA_12_15m"]) > (df["open_15m"] * 0.050))
      & ((df["EMA_26_15m"].shift() - df["EMA_12_15m"].shift()) > (df["open_15m"] / 100.0))
    )


def append_long_45(df, long_entry_logic, allowed_empty_candles_288) -> None:
    """Append NFI long condition #45, a quick-mode long entry."""
    long_entry_logic.append(df["num_empty_288"] <= allowed_empty_candles_288)
    long_entry_logic.append(df["protections_long_global"] == True)

    # 5m & 15m down move, 4h still high
    long_entry_logic.append(
      (df["RSI_3"] > 3.0) | (df["RSI_3_15m"] > 15.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 50.0)
    )
    # 15m & 1h down move, 1h still high
    long_entry_logic.append(
      (df["RSI_3_15m"] > 3.0) | (df["RSI_3_1h"] > 25.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 40.0)
    )
    # 5m & 4h & 1d down move
    long_entry_logic.append((df["RSI_3"] > 3.0) | (df["RSI_3_4h"] > 20.0) | (df["RSI_3_1d"] > 20.0))
    # 15m & 1h down move, 4h high
    long_entry_logic.append(
      (df["RSI_3_15m"] > 3.0) | (df["RSI_3_1h"] > 30.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 60.0)
    )
    # 15m & 4h down move
    long_entry_logic.append((df["RSI_3_15m"] > 3.0) | (df["RSI_3_4h"] > 10.0))
    # 15m & 4h down move, 4h still not low enough
    long_entry_logic.append((df["RSI_3_15m"] > 3.0) | (df["RSI_3_4h"] > 30.0) | (df["RSI_14_4h"] < 35.0))
    # 15m down move, 4h still high, 15m downtrend
    long_entry_logic.append((df["RSI_3_15m"] > 3.0) | (df["AROONU_14_4h"] < 40.0) | (df["CMF_20_15m"] > -0.35))
    # 15m & 1h down move
    long_entry_logic.append((df["RSI_3_15m"] > 5.0) | (df["RSI_3_1h"] > 15.0))
    # 15m & 1h down move, 4h high
    long_entry_logic.append(
      (df["RSI_3_15m"] > 5.0) | (df["RSI_3_1h"] > 40.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 80.0)
    )
    # 15m down move, 1h still not low enough
    long_entry_logic.append((df["RSI_3_15m"] > 5.0) | (df["AROONU_14_1h"] < 30.0))
    # 15m down move, 4h high
    long_entry_logic.append((df["RSI_3_15m"] > 5.0) | (df["AROONU_14_4h"] < 90.0))
    # 15m & 1h & 1d down move
    long_entry_logic.append((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1h"] > 10.0) | (df["RSI_3_1d"] > 10.0))
    # 15m & 1h down move, 1d overbought
    long_entry_logic.append((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1h"] > 20.0) | (df["ROC_9_1d"] < 30.0))
    # 15m & 1h down move, 1h high
    long_entry_logic.append((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1h"] > 45.0) | (df["AROONU_14_1h"] < 80.0))
    # 15m & 1h down move, 1h high
    long_entry_logic.append(
      (df["RSI_3_15m"] > 10.0) | (df["RSI_3_1h"] > 65.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 80.0)
    )
    # 15m & 4h down move, 4h still not low enough
    long_entry_logic.append(
      (df["RSI_3_15m"] > 10.0) | (df["RSI_3_4h"] > 10.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 30.0)
    )
    # 15m & 4h down move, 1d high
    long_entry_logic.append(
      (df["RSI_3_15m"] > 10.0) | (df["RSI_3_4h"] > 10.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 80.0)
    )
    # 15m & 4h down move, 4h still high
    long_entry_logic.append(
      (df["RSI_3_15m"] > 10.0) | (df["RSI_3_4h"] > 30.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 40.0)
    )
    # 15m down move, 1h & 4h high
    long_entry_logic.append(
      (df["RSI_3_15m"] > 10.0) | (df["AROONU_14_1h"] < 70.0) | (df["AROONU_14_4h"] < 100.0)
    )
    # 15m down move, 1h high & overbought
    long_entry_logic.append((df["RSI_3_15m"] > 10.0) | (df["AROONU_14_1h"] < 70.0) | (df["ROC_9_1h"] < 10.0))
    # 15m down move, 1h high, 4h overbought
    long_entry_logic.append((df["RSI_3_15m"] > 10.0) | (df["AROONU_14_1h"] < 70.0) | (df["ROC_9_4h"] < 20.0))
    # 15m down move, 4h & 1d high
    long_entry_logic.append(
      (df["RSI_3_15m"] > 10.0) | (df["AROONU_14_4h"] < 75.0) | (df["AROONU_14_1d"] < 100.0)
    )
    # 15m down move, 4h high, 1h overbought
    long_entry_logic.append((df["RSI_3_15m"] > 10.0) | (df["AROONU_14_4h"] < 100.0) | (df["ROC_9_1h"] < 10.0))
    # 15m down move, 4h high & overbought
    long_entry_logic.append((df["RSI_3_15m"] > 10.0) | (df["AROONU_14_4h"] < 100.0) | (df["ROC_9_4h"] < 20.0))
    # 15m & 1h down move, 4h high
    long_entry_logic.append((df["RSI_3_15m"] > 15.0) | (df["RSI_3_1h"] > 15.0) | (df["AROONU_14_4h"] < 70.0))
    # 15m down move, 1h & 4h high
    long_entry_logic.append(
      (df["RSI_3_15m"] > 15.0) | (df["AROONU_14_1h"] < 70.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 90.0)
    )
    # 15m down move, 4h high, 1d overbought
    long_entry_logic.append((df["RSI_3_15m"] > 15.0) | (df["AROONU_14_4h"] < 70.0) | (df["ROC_9_1d"] < 50.0))
    # 15m & 1h down move, 1h high
    long_entry_logic.append((df["RSI_3_15m"] > 30.0) | (df["RSI_3_1h"] > 30.0) | (df["AROONU_14_1h"] < 70.0))
    # 1h down move, 4h still not low enough
    long_entry_logic.append((df["RSI_3_1h"] > 3.0) | (df["AROONU_14_4h"] < 30.0))
    # 1h & 4h down move, 1h still not low enough
    long_entry_logic.append((df["RSI_3_1h"] > 5.0) | (df["RSI_3_4h"] > 30.0) | (df["AROONU_14_1h"] < 20.0))
    # 1h down move, 1h still not low enough
    long_entry_logic.append((df["RSI_3_1h"] > 5.0) | (df["AROONU_14_1h"] < 30.0))
    # 1h down move, 1h still not low enough
    long_entry_logic.append((df["RSI_3_1h"] > 5.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 25.0))
    # 1h & 4h down move
    long_entry_logic.append((df["RSI_3_1h"] > 10.0) | (df["RSI_3_4h"] > 15.0))
    # 1h & 4h down move, 4h still not low enough
    long_entry_logic.append(
      (df["RSI_3_1h"] > 10.0) | (df["RSI_3_4h"] > 20.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 30.0)
    )
    # 1h & 4h down move, 4h still high
    long_entry_logic.append((df["RSI_3_1h"] > 10.0) | (df["RSI_3_4h"] > 25.0) | (df["AROONU_14_4h"] < 50.0))
    # 1h & 4h down move, 4h still not low enough
    long_entry_logic.append((df["RSI_3_1h"] > 10.0) | (df["RSI_3_4h"] > 30.0) | (df["RSI_14_4h"] < 40.0))
    # 1h & 4h down move, 4h high
    long_entry_logic.append((df["RSI_3_1h"] > 10.0) | (df["RSI_3_4h"] > 40.0) | (df["AROONU_14_4h"] < 60.0))
    # 1h & 1d down move, 4h still high
    long_entry_logic.append((df["RSI_3_1h"] > 10.0) | (df["RSI_3_1d"] > 10.0) | (df["AROONU_14_4h"] < 40.0))
    # 1h & 1d down move, 5m moving down
    long_entry_logic.append((df["RSI_3_1h"] > 10.0) | (df["RSI_3_1d"] > 15.0) | (df["ROC_2"] > -0.0))
    # 1h & 1d down move, 4h still high
    long_entry_logic.append((df["RSI_3_1h"] > 10.0) | (df["RSI_3_1d"] > 30.0) | (df["AROONU_14_4h"] < 50.0))
    # 15m & 1d down move, 1d high
    long_entry_logic.append(
      (df["RSI_3_15m"] > 10.0) | (df["RSI_3_1d"] > 30.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 70.0)
    )
    # 1h & 4h down move, 4h still not low enough
    long_entry_logic.append(
      (df["RSI_3_1h"] > 3.0) | (df["RSI_3_4h"] > 25.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 30.0)
    )
    # 1h down move, 1h still not low enough, 1d high
    long_entry_logic.append(
      (df["RSI_3_1h"] > 10.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 20.0) | (df["AROONU_14_1d"] < 85.0)
    )
    # 1h down move, 1h still not low enough
    long_entry_logic.append((df["RSI_3_1h"] > 10.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 25.0))
    # 1h down move, 4h high
    long_entry_logic.append((df["RSI_3_1h"] > 10.0) | (df["AROONU_14_4h"] < 85.0))
    # 1h down move, 1d high & overbought
    long_entry_logic.append((df["RSI_3_1h"] > 10.0) | (df["AROONU_14_1d"] < 70.0) | (df["ROC_9_1d"] < 50.0))
    # 1h & 4h down move, 4h still high
    long_entry_logic.append((df["RSI_3_1h"] > 15.0) | (df["RSI_3_4h"] > 15.0) | (df["AROONU_14_4h"] < 40.0))
    # 1h & 4h down move, 1d high
    long_entry_logic.append(
      (df["RSI_3_1h"] > 15.0) | (df["RSI_3_4h"] > 20.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 70.0)
    )
    # 1h & 4h & 1d down move
    long_entry_logic.append((df["RSI_3_1h"] > 15.0) | (df["RSI_3_4h"] > 20.0) | (df["RSI_3_1d"] > 30.0))
    # 1h & 4h down move, 1d high
    long_entry_logic.append((df["RSI_3_1h"] > 15.0) | (df["RSI_3_4h"] > 30.0) | (df["AROONU_14_1d"] < 100.0))
    # 1h down move, 1h still high
    long_entry_logic.append((df["RSI_3_1h"] > 15.0) | (df["AROONU_14_1h"] < 50.0))
    # 1h down move, 1d high, 4h downtrend
    long_entry_logic.append((df["RSI_3_1h"] > 15.0) | (df["AROONU_14_1d"] < 70.0) | (df["ROC_9_4h"] > -20.0))
    # 1h down move, 1h still high
    long_entry_logic.append((df["RSI_3_1h"] > 15.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 30.0))
    # 1h & 4h down move, 1d overbought
    long_entry_logic.append((df["RSI_3_1h"] > 20.0) | (df["RSI_3_4h"] > 20.0) | (df["ROC_9_1d"] < 20.0))
    # 1h down move, 4h high
    long_entry_logic.append((df["RSI_3_1h"] > 20.0) | (df["AROONU_14_4h"] < 90.0))
    # 1h down move, 4h still high
    long_entry_logic.append((df["RSI_3_1h"] > 20.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 50.0))
    # 1h & 4h down move, 1h high
    long_entry_logic.append(
      (df["RSI_3_1h"] > 25.0) | (df["RSI_3_4h"] > 30.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 60.0)
    )
    # 1h & 4h down move, 4h high
    long_entry_logic.append((df["RSI_3_1h"] > 25.0) | (df["RSI_3_4h"] > 40.0) | (df["AROONU_14_4h"] < 70.0))
    # 1h down move, 1h high
    long_entry_logic.append((df["RSI_3_1h"] > 25.0) | (df["AROONU_14_1h"] < 70.0))
    # 1h down move, 4h high
    long_entry_logic.append((df["RSI_3_1h"] > 25.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 80.0))
    # 1h & 1d down move, 1h still high
    long_entry_logic.append(
      (df["RSI_3_1h"] > 30.0) | (df["RSI_3_1d"] > 50.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 50.0)
    )
    # 1h down move, 4h high
    long_entry_logic.append((df["RSI_3_1h"] > 30.0) | (df["RSI_14_4h"] < 80.0))
    # 14 down move, 1h high
    long_entry_logic.append((df["RSI_3_1h"] > 30.0) | (df["AROONU_14_1h"] < 80.0))
    # 1h down move, 4h high
    long_entry_logic.append((df["RSI_3_1h"] > 30.0) | (df["AROONU_14_4h"] < 80.0))
    # 1h down move, 4h high
    long_entry_logic.append((df["RSI_3_1h"] > 30.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 80.0))
    # 1h down move, 4h & 1d high
    long_entry_logic.append(
      (df["RSI_3_1h"] > 35.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 80.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 80.0)
    )
    # 1h down move, 1h still high, 1d overbought
    long_entry_logic.append((df["RSI_3_1h"] > 40.0) | (df["AROONU_14_1h"] < 50.0) | (df["ROC_9_1d"] < 50.0))
    # 1h down move, 1h & 4h high
    long_entry_logic.append((df["RSI_3_1h"] > 45.0) | (df["AROONU_14_1h"] < 70.0) | (df["AROONU_14_4h"] < 90.0))
    # 1h down move, 1h & 4h high
    long_entry_logic.append(
      (df["RSI_3_1h"] > 60.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 70.0) | (df["AROONU_14_4h"] < 90.0)
    )
    # 4h down move, 1d high
    long_entry_logic.append((df["RSI_3_4h"] > 5.0) | (df["AROONU_14_1d"] < 100.0))
    # 4h & 1d down move, 1d still high
    long_entry_logic.append(
      (df["RSI_3_4h"] > 10.0) | (df["RSI_3_1d"] > 25.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 50.0)
    )
    # 4h downmove, 4h still high
    long_entry_logic.append((df["RSI_3_4h"] > 10.0) | (df["AROONU_14_4h"] < 40.0))
    # 4h down move, 1h still high, 1d downtrend
    long_entry_logic.append(
      (df["RSI_3_4h"] > 10.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 40.0) | (df["ROC_9_1d"] > -20.0)
    )
    # 4h down move, 1h & 1d downtrend
    long_entry_logic.append((df["RSI_3_4h"] > 10.0) | (df["ROC_9_1h"] > -20.0) | (df["ROC_9_1d"] > -20.0))
    # 4h & 1d down move, 1d still high
    long_entry_logic.append((df["RSI_3_4h"] > 15.0) | (df["RSI_3_1d"] > 35.0) | (df["RSI_14_1d"] < 50.0))
    # 4h down move, 1h still not low enough
    long_entry_logic.append((df["RSI_3_4h"] > 15.0) | (df["AROONU_14_1h"] < 30.0))
    # 4h & 1d down move, 1d high
    long_entry_logic.append((df["RSI_3_4h"] > 20.0) | (df["RSI_3_1d"] > 20.0) | (df["AROONU_14_1d"] < 80.0))
    # 4h down move, 4h still high, 1d high
    long_entry_logic.append((df["RSI_3_4h"] > 20.0) | (df["AROONU_14_4h"] < 50.0) | (df["AROONU_14_1d"] < 100.0))
    # 4h down move, 1d high
    long_entry_logic.append((df["RSI_3_4h"] > 25.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 90.0))
    # 4h down move, 4h & 1d downtrend
    long_entry_logic.append((df["RSI_3_4h"] > 25.0) | (df["ROC_9_4h"] > -20.0) | (df["ROC_9_1d"] > -20.0))
    # 4h down move, 4h & 1d high
    long_entry_logic.append((df["RSI_3_4h"] > 30.0) | (df["AROONU_14_4h"] < 80.0) | (df["AROONU_14_1d"] < 100.0))
    # 4h down move, 1h high
    long_entry_logic.append((df["RSI_3_4h"] > 40.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 70.0))
    # 4h down move, 4h still high
    long_entry_logic.append((df["RSI_3_4h"] > 50.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 50.0))
    # 4h down move, 1h high
    long_entry_logic.append((df["RSI_3_4h"] > 60.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 80.0))
    # 4h down move, 4h high
    long_entry_logic.append((df["RSI_3_4h"] > 60.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 80.0))
    # 1d down move, 1h still not low enough
    long_entry_logic.append((df["RSI_3_1d"] > 5.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 30.0))
    # 1d down move, 1h still not low enough
    long_entry_logic.append((df["RSI_3_1d"] > 15.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 30.0))
    # 1d down move, 4h still high
    long_entry_logic.append((df["RSI_3_1d"] > 15.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 50.0))
    # 1d down move, 1h high & overbought
    long_entry_logic.append(
      (df["RSI_3_1d"] > 35.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 90.0) | (df["ROC_9_1h"] < 10.0)
    )
    # 15m still high, 1h & 4h high
    long_entry_logic.append(
      (df["RSI_14_15m"] < 40.0) | (df["AROONU_14_1h"] < 80.0) | (df["AROONU_14_4h"] < 90.0)
    )
    # 1h & 4h high, 4h overbought
    long_entry_logic.append((df["AROONU_14_1h"] < 70.0) | (df["AROONU_14_4h"] < 100.0) | (df["ROC_9_4h"] < 20.0))
    # 4h high, 1d overbought
    long_entry_logic.append((df["AROONU_14_4h"] < 70.0) | (df["ROC_9_1d"] < 80.0))
    # 4h high, 1h & 1d downtrend
    long_entry_logic.append((df["AROONU_14_4h"] < 70.0) | (df["ROC_9_1h"] > -20.0) | (df["ROC_9_1d"] > -20.0))
    # 4h high, 1h & 4h overbought
    long_entry_logic.append((df["AROONU_14_4h"] < 80.0) | (df["ROC_9_1h"] < 10.0) | (df["ROC_9_4h"] < 10.0))
    # 4h high & overbought
    long_entry_logic.append((df["AROONU_14_4h"] < 90.0) | (df["ROC_9_4h"] < 80.0))
    # 1d high, 4h & 1d downtrend
    long_entry_logic.append((df["AROONU_14_1d"] < 80.0) | (df["ROC_9_4h"] > -20.0) | (df["ROC_9_1d"] > -20.0))
    # 1h high, 4h overbought
    long_entry_logic.append((df["STOCHRSIk_14_14_3_3_1h"] < 80.0) | (df["ROC_9_4h"] < 80.0))
    # 4h high, 1h & 1d downtrend
    long_entry_logic.append(
      (df["STOCHRSIk_14_14_3_3_4h"] < 70.0) | (df["ROC_9_1h"] > -20.0) | (df["ROC_9_1d"] > -20.0)
    )
    # 4h high, 1h & 4h overbought
    long_entry_logic.append(
      (df["STOCHRSIk_14_14_3_3_4h"] < 80.0) | (df["ROC_9_1h"] < 10.0) | (df["ROC_9_4h"] < 10.0)
    )
    # 4h high, 4h & 1d overbought
    long_entry_logic.append(
      (df["STOCHRSIk_14_14_3_3_4h"] < 80.0) | (df["ROC_9_4h"] < 30.0) | (df["ROC_9_1d"] < 30.0)
    )
    # 1d top wick, 4h still high
    long_entry_logic.append((df["top_wick_pct_1d"] < 40.0) | (df["AROONU_14_4h"] < 50.0))
    # pump, 4h still high
    long_entry_logic.append(
      (((df["high_max_24_4h"] - df["low_min_24_4h"]) / df["low_min_24_4h"]) < 2.0)
      | (df["STOCHRSIk_14_14_3_3_4h"] < 50.0)
    )
    # pump, drop but not yet near the previous lows
    long_entry_logic.append(
      (((df["high_max_24_4h"] - df["low_min_24_4h"]) / df["low_min_24_4h"]) < 2.0)
      | (df["close"] > (df["high_max_6_4h"] * 0.75))
      | (df["close"] < (df["low_min_24_4h"] * 1.25))
    )
    # pump, drop but not yet near the previous lows
    long_entry_logic.append(
      (((df["high_max_12_1d"] - df["low_min_12_1d"]) / df["low_min_12_1d"]) < 2.0)
      | (df["close"] > (df["high_max_24_4h"] * 0.70))
      | (df["close"] < (df["low_min_12_1d"] * 1.25))
    )
    # big drop in last hour
    long_entry_logic.append(df["close"] > (df["close_max_12"] * 0.50))
    # big drop in last hour, 1d down move
    long_entry_logic.append((df["close"] > (df["close_max_12"] * 0.80)) | (df["RSI_3_1d"] > 15.0))
    # big drop in the last 12 hours, 4h still high
    long_entry_logic.append((df["close"] > (df["high_max_12_1h"] * 0.50)) | (df["AROONU_14_4h"] < 50.0))
    # big drop in the last 6 days, 1h still high
    long_entry_logic.append((df["close"] > (df["high_max_6_1d"] * 0.25)) | (df["AROONU_14_1h"] < 50.0))
    # big drop in the last 12 days, 1h down move
    long_entry_logic.append((df["close"] > (df["high_max_12_1d"] * 0.45)) | (df["RSI_3_1h"] > 5.0))
    # big drop in the last 12 days, 4h down move
    long_entry_logic.append((df["close"] > (df["high_max_12_1d"] * 0.40)) | (df["RSI_3_4h"] > 15.0))
    # big drop in the last 12 days, 1h still high
    long_entry_logic.append((df["close"] > (df["high_max_12_1d"] * 0.25)) | (df["AROONU_14_1h"] < 75.0))
    # big drop in the last 20 days, 1h down move
    long_entry_logic.append((df["close"] > (df["high_max_20_1d"] * 0.35)) | (df["RSI_3_1h"] > 10.0))
    # big drop in the last 20 days, 1h down move
    long_entry_logic.append((df["close"] > (df["high_max_20_1d"] * 0.25)) | (df["RSI_3_1h"] > 15.0))
    # big drop in the last 20 days, 1h down move
    long_entry_logic.append((df["close"] > (df["high_max_20_1d"] * 0.10)) | (df["RSI_3_1h"] > 20.0))
    # big drop in the last 20 days, 1d high, 1d downtrend
    long_entry_logic.append(
      (df["close"] > (df["high_max_20_1d"] * 0.20))
      | (df["STOCHRSIk_14_14_3_3_1d"] < 70.0)
      | (df["ROC_9_1d"] > -15.0)
    )
    # big drop in the last 30 days, 4h down move, 4h still high
    long_entry_logic.append(
      (df["close"] > (df["high_max_30_1d"] * 0.25)) | (df["RSI_3_4h"] > 45.0) | (df["RSI_14_4h"] < 40.0)
    )

    # Logic
    long_entry_logic.append(df["RSI_3"] < 50.0)
    long_entry_logic.append(df["AROONU_14_15m"] < 25.0)
    long_entry_logic.append(df["STOCHRSIk_14_14_3_3_15m"] < 20.0)
    long_entry_logic.append(df["close_15m"] < (df["EMA_20_15m"] * 0.924))


def append_long_46(df, long_entry_logic, allowed_empty_candles_288) -> None:
    """Append NFI long condition #46, a quick-mode long entry."""
    long_entry_logic.append(df["num_empty_288"] <= allowed_empty_candles_288)
    long_entry_logic.append(df["protections_long_global"] == True)

    # 5m & 1h down move
    long_entry_logic.append((df["RSI_3_15m"] > 3.0) | (df["RSI_3_1h"] > 5.0))
    # 15m & 4h down move, 4h still high
    long_entry_logic.append((df["RSI_3_15m"] > 3.0) | (df["RSI_3_4h"] > 20.0) | (df["AROONU_14_4h"] < 40.0))
    # 15m & 4h down move
    long_entry_logic.append((df["RSI_3_15m"] > 5.0) | (df["RSI_3_4h"] > 10.0))
    # 15m & 4h down move, 4h still high
    long_entry_logic.append((df["RSI_3_15m"] > 5.0) | (df["RSI_3_4h"] > 20.0) | (df["AROONU_14_4h"] < 40.0))
    # 15m & 4h down move, 4h still high
    long_entry_logic.append((df["RSI_3_15m"] > 5.0) | (df["RSI_3_4h"] > 30.0) | (df["AROONU_14_4h"] < 50.0))
    # 15m & 1h & 4h down move
    long_entry_logic.append((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1h"] > 10.0) | (df["RSI_3_4h"] > 30.0))
    # 15m & 1h down move, 4h still not low enough
    long_entry_logic.append((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1h"] > 10.0) | (df["RSI_14_4h"] < 30.0))
    # 15m & 1h & 4h down move
    long_entry_logic.append((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1h"] > 20.0) | (df["RSI_3_4h"] > 20.0))
    # 15m & 1h down move, 1h still high
    long_entry_logic.append((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1h"] > 20.0) | (df["AROONU_14_1h"] < 40.0))
    # 15m & 1h down move, 4h still high
    long_entry_logic.append(
      (df["RSI_3_15m"] > 10.0) | (df["RSI_3_1h"] > 25.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 40.0)
    )
    # 15m & 4h down move, 1d high
    long_entry_logic.append(
      (df["RSI_3_15m"] > 10.0) | (df["RSI_3_4h"] > 15.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 90.0)
    )
    # 15m & 4h down move, 4h downtrend
    long_entry_logic.append((df["RSI_3_15m"] > 10.0) | (df["RSI_3_4h"] > 15.0) | (df["ROC_9_4h"] > -20.0))
    # 15m & 4h down move, 4h still high
    long_entry_logic.append((df["RSI_3_15m"] > 10.0) | (df["RSI_3_4h"] > 20.0) | (df["AROONU_14_4h"] < 50.0))
    # 15m & 4h down move, 4h still not low enough
    long_entry_logic.append(
      (df["RSI_3_15m"] > 10.0) | (df["RSI_3_4h"] > 20.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 30.0)
    )
    # 15m & 4h down move, 1d high
    long_entry_logic.append(
      (df["RSI_3_15m"] > 10.0) | (df["RSI_3_4h"] > 30.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 90.0)
    )
    # 15m down move, 4h still high, 1d high
    long_entry_logic.append((df["RSI_3_15m"] > 10.0) | (df["AROONU_14_4h"] < 50.0) | (df["AROONU_14_1d"] < 90.0))
    # 15m & 1h down move, 4h high
    long_entry_logic.append((df["RSI_3_15m"] > 15.0) | (df["RSI_3_1h"] > 20.0) | (df["AROONU_14_4h"] < 60.0))
    # 15m & 4h down move, 1h still high
    long_entry_logic.append((df["RSI_3_15m"] > 15.0) | (df["RSI_3_4h"] > 15.0) | (df["AROONU_14_1h"] < 40.0))
    # 15m & 1h & 1d down move, 1h still not low enough, 1d high
    long_entry_logic.append(
      (df["RSI_3_15m"] > 20.0)
      | (df["RSI_3_1h"] > 20.0)
      | (df["RSI_3_1d"] > 30.0)
      | (df["RSI_14_1h"] < 30.0)
      | (df["AROONU_14_1d"] < 80.0)
    )
    # 15m & 1h down move, 4h still high, 4h overbought
    long_entry_logic.append(
      (df["RSI_3_15m"] > 20.0) | (df["RSI_3_1h"] > 20.0) | (df["AROONU_14_4h"] < 50.0) | (df["ROC_9_4h"] < 10.0)
    )
    # 15m & 1h down move, 4h high
    long_entry_logic.append((df["RSI_3_15m"] > 20.0) | (df["RSI_3_1h"] > 20.0) | (df["AROONU_14_4h"] < 70.0))
    # 15m down move, 1h & 4h still high
    long_entry_logic.append(
      (df["RSI_3_15m"] > 20.0) | (df["AROONU_14_1h"] < 40.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 50.0)
    )
    # 15m & 1h & 4h down move, 1d high
    long_entry_logic.append(
      (df["RSI_3_15m"] > 25.0) | (df["RSI_3_1h"] > 25.0) | (df["RSI_3_4h"] > 25.0) | (df["ROC_9_1d"] < 70.0)
    )
    # 15m & 4h down move, 4h high
    long_entry_logic.append((df["RSI_3_15m"] > 25.0) | (df["RSI_3_4h"] > 45.0) | (df["AROONU_14_4h"] < 85.0))
    # 15m & 1h down move, 15m still not low enough
    long_entry_logic.append((df["RSI_3_15m"] > 30.0) | (df["RSI_3_1h"] > 30.0) | (df["AROONU_14_15m"] < 15.0))
    # 15m & 1h down move, 1h high
    long_entry_logic.append((df["RSI_3_15m"] > 30.0) | (df["RSI_3_1h"] > 35.0) | (df["AROONU_14_1h"] < 80.0))
    # 1h down move, 1h still not low enough, 1d high
    long_entry_logic.append((df["RSI_3_1h"] > 3.0) | (df["AROONU_14_1h"] < 20.0) | (df["AROONU_14_1d"] < 90.0))
    # 1h & 4h down move
    long_entry_logic.append((df["RSI_3_1h"] > 5.0) | (df["RSI_3_4h"] > 10.0))
    # 1h & 4h down move, 4h downtrend
    long_entry_logic.append((df["RSI_3_1h"] > 5.0) | (df["RSI_3_4h"] > 15.0) | (df["ROC_9_4h"] > -30.0))
    # 1h & 4h down move, 4h still not low enough
    long_entry_logic.append(
      (df["RSI_3_1h"] > 5.0) | (df["RSI_3_4h"] > 30.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 30.0)
    )
    # 1h & 1d down move, 1d high
    long_entry_logic.append((df["RSI_3_1h"] > 5.0) | (df["RSI_3_1d"] > 45.0) | (df["AROONU_14_1d"] < 80.0))
    # 1h down move, 4h high
    long_entry_logic.append((df["RSI_3_1h"] > 5.0) | (df["AROONU_14_4h"] < 70.0))
    # 1h down move, 1d still high
    long_entry_logic.append((df["RSI_3_1h"] > 5.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 50.0))
    # 1h & 4h down move, 4h still not low enough
    long_entry_logic.append((df["RSI_3_1h"] > 10.0) | (df["RSI_3_4h"] > 20.0) | (df["RSI_14_4h"] < 30.0))
    # 1h & 4h down move, 4h still not low enough
    long_entry_logic.append((df["RSI_3_1h"] > 10.0) | (df["RSI_3_4h"] > 30.0) | (df["RSI_14_4h"] < 40.0))
    # 1h & 4h down move, 4h still not low enough
    long_entry_logic.append((df["RSI_3_1h"] > 10.0) | (df["RSI_3_4h"] > 30.0) | (df["AROONU_14_4h"] < 30.0))
    # 1h & 4h & 1d down move
    long_entry_logic.append((df["RSI_3_1h"] > 10.0) | (df["RSI_3_4h"] > 30.0) | (df["RSI_3_1d"] > 30.0))
    # 1h & 4h down move, 1d overbought
    long_entry_logic.append((df["RSI_3_1h"] > 10.0) | (df["RSI_3_4h"] > 35.0) | (df["ROC_9_1d"] < 50.0))
    # 1h & 4h down move, 4h high
    long_entry_logic.append((df["RSI_3_1h"] > 10.0) | (df["RSI_3_4h"] > 45.0) | (df["AROONU_14_4h"] < 70.0))
    # 1h & 4h down move, 4h still high
    long_entry_logic.append(
      (df["RSI_3_1h"] > 10.0) | (df["RSI_3_4h"] > 50.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 40.0)
    )
    # 1h & 1d down move, 4h still not low enough
    long_entry_logic.append(
      (df["RSI_3_1h"] > 10.0) | (df["RSI_3_1d"] > 25.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 30.0)
    )
    # 1h & 1d down move, 4h still high
    long_entry_logic.append((df["RSI_3_1h"] > 10.0) | (df["RSI_3_1d"] > 30.0) | (df["AROONU_14_4h"] < 50.0))
    # 1h down move, 1h still high
    long_entry_logic.append((df["RSI_3_1h"] > 10.0) | (df["AROONU_14_1h"] < 50.0))
    # 1h down move, 4h still high, 1d high
    long_entry_logic.append((df["RSI_3_1h"] > 10.0) | (df["AROONU_14_4h"] < 60.0) | (df["AROONU_14_1d"] < 90.0))
    # 1h down move, 1d high & overbought
    long_entry_logic.append((df["RSI_3_1h"] > 10.0) | (df["AROONU_14_1d"] < 80.0) | (df["ROC_9_1d"] < 30.0))
    # 1h & 4h down move, 1d high
    long_entry_logic.append((df["RSI_3_1h"] > 15.0) | (df["RSI_3_4h"] > 15.0) | (df["RSI_14_1d"] < 60.0))
    # 1h & 4h & 1d down move
    long_entry_logic.append((df["RSI_3_1h"] > 15.0) | (df["RSI_3_4h"] > 20.0) | (df["RSI_3_1d"] > 30.0))
    # 1h & 4h down move, 4h still not low enough
    long_entry_logic.append((df["RSI_3_1h"] > 15.0) | (df["RSI_3_4h"] > 20.0) | (df["AROONU_14_4h"] < 30.0))
    # 1h & 4h down move, 1d overbought
    long_entry_logic.append((df["RSI_3_1h"] > 15.0) | (df["RSI_3_4h"] > 20.0) | (df["ROC_9_1d"] < 50.0))
    # 1h & 4h & 1d down move
    long_entry_logic.append((df["RSI_3_1h"] > 15.0) | (df["RSI_3_4h"] > 25.0) | (df["RSI_3_1d"] > 25.0))
    # 1h & 4h down move, 1d high
    long_entry_logic.append(
      (df["RSI_3_1h"] > 15.0) | (df["RSI_3_4h"] > 30.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 80.0)
    )
    # 1h & 4h down move, 1h & 4h still high
    long_entry_logic.append(
      (df["RSI_3_1h"] > 15.0) | (df["RSI_3_4h"] > 40.0) | (df["RSI_14_1h"] < 40.0) | (df["RSI_14_4h"] < 50.0)
    )
    # 1h & 4h down move, 4h still high
    long_entry_logic.append(
      (df["RSI_3_1h"] > 15.0) | (df["RSI_3_4h"] > 45.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 50.0)
    )
    # 1h & 4h down move, 4h still high
    long_entry_logic.append((df["RSI_3_1h"] > 15.0) | (df["RSI_3_4h"] > 50.0) | (df["AROONU_14_4h"] < 40.0))
    # 1h & 1d down move, 1d still high
    long_entry_logic.append((df["RSI_3_1h"] > 15.0) | (df["RSI_3_1d"] > 15.0) | (df["AROONU_14_1d"] < 50.0))
    # 1h down move, 1h still high, 1d overbought
    long_entry_logic.append((df["RSI_3_1h"] > 15.0) | (df["AROONU_14_1h"] < 40.0) | (df["ROC_9_1d"] < 50.0))
    # 1h down move, 1d high, 4h downtrend
    long_entry_logic.append((df["RSI_3_1h"] > 15.0) | (df["AROONU_14_1d"] < 70.0) | (df["ROC_9_4h"] > -20.0))
    # 1h down move, 1d high & overbought
    long_entry_logic.append((df["RSI_3_1h"] > 15.0) | (df["AROONU_14_1d"] < 80.0) | (df["ROC_9_1d"] < 30.0))
    # 1h down move, 4h high
    long_entry_logic.append((df["RSI_3_1h"] > 15.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 70.0))
    # 1h & 4h down move, 1h still not low enough
    long_entry_logic.append((df["RSI_3_1h"] > 20.0) | (df["RSI_3_4h"] > 20.0) | (df["AROONU_14_1h"] < 30.0))
    # 1h & 4h down move, 4h still high
    long_entry_logic.append((df["RSI_3_1h"] > 20.0) | (df["RSI_3_4h"] > 20.0) | (df["RSI_14_4h"] < 40.0))
    # 1h & 4h down move, 4h still high
    long_entry_logic.append((df["RSI_3_1h"] > 20.0) | (df["RSI_3_4h"] > 20.0) | (df["AROONU_14_4h"] < 50.0))
    # 1h & 4h down move, 1d downtrend
    long_entry_logic.append((df["RSI_3_1h"] > 20.0) | (df["RSI_3_4h"] > 20.0) | (df["ROC_9_1d"] > -30.0))
    # 1h & 4h down move, 1d high
    long_entry_logic.append((df["RSI_3_1h"] > 20.0) | (df["RSI_3_4h"] > 35.0) | (df["AROONU_14_1d"] < 80.0))
    # 1h & 4h down move, 4h high
    long_entry_logic.append((df["RSI_3_1h"] > 20.0) | (df["RSI_3_4h"] > 45.0) | (df["AROONU_14_4h"] < 65.0))
    # 1h & 1d down move, 1d high
    long_entry_logic.append((df["RSI_3_1h"] > 20.0) | (df["RSI_3_1d"] > 20.0) | (df["AROONU_14_1d"] < 70.0))
    # 1h down move, 1h still high, 1d high
    long_entry_logic.append((df["RSI_3_1h"] > 20.0) | (df["AROONU_14_1h"] < 40.0) | (df["AROONU_14_1d"] < 90.0))
    # 4h down move, 4h still high, 1d high
    long_entry_logic.append((df["RSI_3_4h"] > 20.0) | (df["AROONU_14_4h"] < 50.0) | (df["AROONU_14_1d"] < 100.0))
    # 1h down move, 4h still high, 1d downtrend
    long_entry_logic.append(
      (df["RSI_3_1h"] > 20.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 40.0) | (df["ROC_9_1d"] > -25.0)
    )
    # 1h down move, 4h & 1d high
    long_entry_logic.append(
      (df["RSI_3_1h"] > 20.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 50.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 80.0)
    )
    # 1h & 4h down move, 1h still high
    long_entry_logic.append((df["RSI_3_1h"] > 25.0) | (df["RSI_3_4h"] > 35.0) | (df["AROONU_14_1h"] < 40.0))
    # 1h & 4h down move, 4h high
    long_entry_logic.append((df["RSI_3_1h"] > 25.0) | (df["RSI_3_4h"] > 40.0) | (df["AROONU_14_4h"] < 70.0))
    # 1h down move, 15m still not low enough, 4h high
    long_entry_logic.append(
      (df["RSI_3_1h"] > 25.0) | (df["RSI_14_15m"] < 30.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 60.0)
    )
    # 1h & 4h down move, 4h still high
    long_entry_logic.append(
      (df["RSI_3_1h"] > 25.0) | (df["RSI_3_4h"] > 35.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 50.0)
    )
    # 1h down move, 1h high
    long_entry_logic.append((df["RSI_3_1h"] > 25.0) | (df["AROONU_14_1h"] < 60.0))
    # 1h down move, 4h high
    long_entry_logic.append((df["RSI_3_1h"] > 25.0) | (df["AROONU_14_4h"] < 80.0))
    # 1h & 1d down move, 1d high
    long_entry_logic.append((df["RSI_3_1h"] > 30.0) | (df["RSI_3_1d"] > 45.0) | (df["AROONU_14_1d"] < 80.0))
    # 1h down move, 4h & 1d high
    long_entry_logic.append((df["RSI_3_1h"] > 30.0) | (df["AROONU_14_4h"] < 70.0) | (df["AROONU_14_1d"] < 100.0))
    # 1h down move, 4h high, 1d downtrend
    long_entry_logic.append((df["RSI_3_1h"] > 30.0) | (df["AROONU_14_4h"] < 100.0) | (df["ROC_9_1d"] > -30.0))
    # 1h down move, 4h high
    long_entry_logic.append((df["RSI_3_1h"] > 30.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 90.0))
    # 1h & 4h down move, 4h high
    long_entry_logic.append((df["RSI_3_1h"] > 35.0) | (df["RSI_3_4h"] > 55.0) | (df["AROONU_14_4h"] < 80.0))
    # 1h down move, 1h & 4h high
    long_entry_logic.append((df["RSI_3_1h"] > 35.0) | (df["AROONU_14_1h"] < 70.0) | (df["AROONU_14_4h"] < 90.0))
    # 1h down move, 4h high, 4h downtrend
    long_entry_logic.append((df["RSI_3_1h"] > 35.0) | (df["AROONU_14_4h"] < 70.0) | (df["CMF_20_4h"] > -0.30))
    # 1h down move, 1d high, 4h overbought
    long_entry_logic.append((df["RSI_3_1h"] > 35.0) | (df["AROONU_14_1d"] < 90.0) | (df["ROC_9_4h"] < 40.0))
    # 1h down move, 1h high, 1d overbought
    long_entry_logic.append((df["RSI_3_1h"] > 40.0) | (df["AROONU_14_1h"] < 70.0) | (df["ROC_9_1d"] < 20.0))
    # 1h down move, 1h & 4h high
    long_entry_logic.append((df["RSI_3_1h"] > 50.0) | (df["AROONU_14_1h"] < 70.0) | (df["AROONU_14_4h"] < 100.0))
    # 1h down move, 1h overbought
    long_entry_logic.append((df["RSI_3_1h"] > 50.0) | (df["ROC_9_1h"] < 40.0))
    # 4h & 1d down move, 1d high
    long_entry_logic.append((df["RSI_3_4h"] > 5.0) | (df["RSI_3_1d"] > 30.0) | (df["AROONU_14_1d"] < 70.0))
    # 4h down move, 1h & 4h downtrend
    long_entry_logic.append((df["RSI_3_4h"] > 5.0) | (df["ROC_9_1h"] > -15.0) | (df["ROC_9_4h"] > -20.0))
    # 4h & 1d down move
    long_entry_logic.append((df["RSI_3_4h"] > 10.0) | (df["RSI_3_1d"] > 20.0))
    # 4h & 1d down move, 1d high
    long_entry_logic.append((df["RSI_3_4h"] > 10.0) | (df["RSI_3_1d"] > 50.0) | (df["AROONU_14_1d"] < 90.0))
    # 4h down move, 4h & 1d still high
    long_entry_logic.append((df["RSI_3_4h"] > 10.0) | (df["AROONU_14_4h"] < 50.0) | (df["AROONU_14_1d"] < 50.0))
    # 4h & 1d down move, 1d low
    long_entry_logic.append((df["RSI_3_4h"] > 15.0) | (df["RSI_3_1d"] > 25.0) | (df["CMF_20_1d"] > -0.2))
    # 4h & 1d down move, 1d still high
    long_entry_logic.append((df["RSI_3_4h"] > 15.0) | (df["RSI_3_1d"] > 30.0) | (df["AROONU_14_1d"] < 50.0))
    # 4h & 1d down move, 1d overbought
    long_entry_logic.append((df["RSI_3_4h"] > 20.0) | (df["RSI_3_1d"] > 45.0) | (df["ROC_9_1d"] < 40.0))
    # 4h down move, 4h still not low enough, 1d downtrend
    long_entry_logic.append(
      (df["RSI_3_4h"] > 20.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 30.0) | (df["ROC_9_1d"] > -20.0)
    )
    # 4h down move, 4h & 1d downtrend
    long_entry_logic.append((df["RSI_3_4h"] > 20.0) | (df["ROC_9_4h"] > -20.0) | (df["ROC_9_1d"] > -20.0))
    # 4h down move, 4h high
    long_entry_logic.append((df["RSI_3_4h"] > 30.0) | (df["AROONU_14_4h"] < 90.0))
    # 4h down move, 4h & 1d high
    long_entry_logic.append(
      (df["RSI_3_4h"] > 35.0) | (df["AROONU_14_4h"] < 60.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 90.0)
    )
    # 4h down move, 4h overbought
    long_entry_logic.append((df["RSI_3_4h"] > 60.0) | (df["ROC_9_4h"] < 40.0))
    # 1d down move, 4h & 1d downtrend
    long_entry_logic.append((df["RSI_3_1d"] > 10.0) | (df["ROC_9_4h"] > -20.0) | (df["ROC_9_1d"] > -20.0))
    # 15m down move, 1d high, 1d downtrend
    long_entry_logic.append((df["RSI_3_1d"] > 15.0) | (df["AROONU_14_1d"] < 70.0) | (df["ROC_9_1d"] > -40.0))
    # 1d down move, 1d high, 1d downtrend
    long_entry_logic.append((df["RSI_3_1d"] > 25.0) | (df["AROONU_14_1d"] < 80.0) | (df["ROC_9_1d"] > -30.0))
    # 4h & 1d high, 4h overbought
    long_entry_logic.append((df["AROONU_14_4h"] < 80.0) | (df["AROONU_14_1d"] < 100.0) | (df["ROC_9_4h"] < 20.0))
    # 4h high, 1h overbought
    long_entry_logic.append((df["AROONU_14_4h"] < 80.0) | (df["ROC_9_1h"] < 40.0))
    # 4h high, 4h overbought
    long_entry_logic.append((df["AROONU_14_4h"] < 80.0) | (df["ROC_9_4h"] < 40.0))
    # 4h high, 1h overbought
    long_entry_logic.append((df["STOCHRSIk_14_14_3_3_4h"] < 70.0) | (df["ROC_9_1h"] < 40.0))
    # 4h high, 4h overbought
    long_entry_logic.append((df["STOCHRSIk_14_14_3_3_4h"] < 70.0) | (df["ROC_9_4h"] < 40.0))
    # 4h high, 4h overbought, 1d downtrend
    long_entry_logic.append(
      (df["STOCHRSIk_14_14_3_3_4h"] < 90.0) | (df["ROC_9_4h"] < 20.0) | (df["ROC_9_1d"] > -20.0)
    )
    # 1d green, 4h down move, 4h still high
    long_entry_logic.append((df["change_pct_1d"] < 40.0) | (df["RSI_3_4h"] > 35.0) | (df["AROONU_14_4h"] < 40.0))
    # 4h top wick, 1h down move, 1h still high
    long_entry_logic.append(
      (df["top_wick_pct_4h"] < 20.0) | (df["RSI_3_1h"] > 45.0) | (df["AROONU_14_1h"] < 50.0)
    )
    # pump, drop but not yet near the previous lows
    long_entry_logic.append(
      (((df["high_max_6_1d"] - df["low_min_6_1d"]) / df["low_min_6_1d"]) < 2.0)
      | (df["close"] > (df["high_max_12_4h"] * 0.50))
      | (df["close"] < (df["low_min_24_4h"] * 1.05))
    )
    # 1d overbought, drop but not yet near the previous lows
    long_entry_logic.append(
      (df["ROC_9_1d"] < 50.0)
      | (df["close"] > (df["high_max_6_1d"] * 0.70))
      | (df["close"] < (df["low_min_12_1d"] * 1.25))
    )
    # 1d overbought, drop but not yet near the previous lows
    long_entry_logic.append(
      (((df["high_max_12_1d"] - df["low_min_12_1d"]) / df["low_min_12_1d"]) < 2.5)
      | (df["close"] > (df["high_max_6_1d"] * 0.60))
      | (df["close"] < (df["low_min_12_1d"] * 1.25))
    )
    # big drop in the last 2 days, 1d down move
    long_entry_logic.append((df["close"] > (df["high_max_12_4h"] * 0.30)) | (df["RSI_3_1d"] > 30.0))
    # big drop in the last 12 days, 1h down move
    long_entry_logic.append((df["close"] > (df["high_max_12_1d"] * 0.30)) | (df["RSI_3_1h"] > 20.0))
    # big drop in the last 12 days, 4h still high
    long_entry_logic.append(
      (df["close"] > (df["high_max_12_1d"] * 0.40)) | (df["STOCHRSIk_14_14_3_3_4h"] < 50.0)
    )
    # big drop in the last 20 days, 1h down move
    long_entry_logic.append((df["close"] > (df["high_max_20_1d"] * 0.40)) | (df["RSI_3_1h"] > 10.0))
    # big drop in the last 20 days, 4h down move
    long_entry_logic.append((df["close"] > (df["high_max_20_1d"] * 0.10)) | (df["RSI_3_4h"] > 25.0))
    # big drop in the last 30 days, 4h down move
    long_entry_logic.append((df["close"] > (df["high_max_30_1d"] * 0.40)) | (df["RSI_3_4h"] > 15.0))
    # big drop in the last 30 days, 4h still not low enough
    long_entry_logic.append(
      (df["close"] > (df["high_max_30_1d"] * 0.25)) | (df["STOCHRSIk_14_14_3_3_4h"] < 30.0)
    )

    # Logic
    long_entry_logic.append(df["RSI_3"] < 40.0)
    long_entry_logic.append(df["RSI_3_15m"] < 50.0)
    long_entry_logic.append(df["WILLR_14_15m"] < -50.0)
    long_entry_logic.append(df["AROONU_14_15m"] < 25.0)
    long_entry_logic.append(df["STOCHRSIk_14_14_3_3_15m"] < 20.0)
    long_entry_logic.append(df["WILLR_84_1h"] < -70.0)
    long_entry_logic.append(df["STOCHRSIk_14_14_3_3_1h"] < 20.0)
    long_entry_logic.append(df["BBB_20_2.0_1h"] > 12.0)
    long_entry_logic.append(df["close_max_48"] >= (df["close"] * 1.10))

def append_long_161(df, long_entry_logic, allowed_empty_candles_288) -> None:
    """Append NFI long condition #161, the scalp-mode long entry."""
    # Protections
    long_entry_logic.append(df["num_empty_288"] <= allowed_empty_candles_288)
    long_entry_logic.append(df["protections_long_global"] == True)

    # 5m down move, 15m high
    long_entry_logic.append((df["RSI_3"] > 15.0) | (df["AROONU_14_15m"] < 80.0))
    # 15m & 1h down move, 4h high
    long_entry_logic.append((df["RSI_3_15m"] > 25.0) | (df["RSI_3_1h"] > 35.0) | (df["AROONU_14_4h"] < 70.0))
    # 15m & 4h down move, 4h still high
    long_entry_logic.append((df["RSI_3_15m"] > 25.0) | (df["RSI_3_4h"] > 50.0) | (df["AROONU_14_4h"] < 50.0))
    # 15m down move, 15m high
    long_entry_logic.append((df["RSI_3_15m"] > 25.0) | (df["AROONU_14_15m"] < 80.0))
    # 15m down move, 4h still high, 1d high
    long_entry_logic.append(
      (df["RSI_3_15m"] > 25.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 50.0) | (df["AROONU_14_1d"] < 90.0)
    )
    # 15m & 1h down move, 15m still high
    long_entry_logic.append((df["RSI_3_15m"] > 30.0) | (df["RSI_3_1h"] > 60.0) | (df["AROONU_14_15m"] < 50.0))
    # 15m down move, 15m & 4h still high
    long_entry_logic.append(
      (df["RSI_3_15m"] > 30.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 50.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 50.0)
    )
    # 15m & 4h down move, 4h high
    long_entry_logic.append((df["RSI_3_15m"] > 35.0) | (df["RSI_3_4h"] > 60.0) | (df["AROONU_14_4h"] < 80.0))
    # 15m & 1h down move, 1h high
    long_entry_logic.append((df["RSI_3_15m"] > 40.0) | (df["RSI_3_1h"] > 40.0) | (df["AROONU_14_1h"] < 70.0))
    # 15m & 1h down move, 1h still high
    long_entry_logic.append(
      (df["RSI_3_15m"] > 40.0) | (df["RSI_3_1h"] > 40.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 50.0)
    )
    # 15m & 1h down move, 4h high
    long_entry_logic.append((df["RSI_3_15m"] > 40.0) | (df["RSI_3_1h"] > 60.0) | (df["AROONU_14_4h"] < 80.0))
    # 15m & 4h down move, 15m high
    long_entry_logic.append(
      (df["RSI_3_15m"] > 40.0) | (df["RSI_3_4h"] > 40.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 50.0)
    )
    # 15m & 4h down move, 15m high
    long_entry_logic.append(
      (df["RSI_3_15m"] > 40.0) | (df["RSI_3_4h"] > 60.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 70.0)
    )
    # 15m down move, 15m & 1h still high
    long_entry_logic.append(
      (df["RSI_3_15m"] > 40.0) | (df["AROONU_14_15m"] < 50.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 50.0)
    )
    # 15m down move, 15m & 1h still high
    long_entry_logic.append(
      (df["RSI_3_15m"] > 40.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 50.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 50.0)
    )
    # 15m down move, 4h still high, 1d overbought
    long_entry_logic.append((df["RSI_3_15m"] > 40.0) | (df["AROONU_14_4h"] < 50.0) | (df["ROC_9_1d"] < 100.0))
    # 15m & 1h down move, 1h still high
    long_entry_logic.append(
      (df["RSI_3_15m"] > 45.0) | (df["RSI_3_1h"] > 45.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 40.0)
    )
    # 15m down move, 15m high, 1d overbought
    long_entry_logic.append((df["RSI_3_15m"] > 45.0) | (df["AROONU_14_15m"] < 60.0) | (df["ROC_9_1d"] < 50.0))
    # 15m down move, 15m high, 4h still high
    long_entry_logic.append(
      (df["RSI_3_15m"] > 45.0) | (df["AROONU_14_15m"] < 70.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 50.0)
    )
    # 15m down move, 15m still not low enough, 4h still high
    long_entry_logic.append(
      (df["RSI_3_15m"] > 45.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 30.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 50.0)
    )
    # 15m down move, 15m & 1h still high
    long_entry_logic.append(
      (df["RSI_3_15m"] > 45.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 45.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 40.0)
    )
    # 15m down move, 15m still not low enough, 4h high
    long_entry_logic.append(
      (df["RSI_3_15m"] > 50.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 30.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 90.0)
    )
    # 15m down move, 15m still high, 1d overbought
    long_entry_logic.append((df["RSI_3_15m"] > 50.0) | (df["AROONU_14_15m"] < 50.0) | (df["ROC_9_1d"] < 50.0))
    # 15m down move, 15m still high, 1h high
    long_entry_logic.append(
      (df["RSI_3_15m"] > 55.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 40.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 70.0)
    )
    # 15m down move, 15m still high, 4h high
    long_entry_logic.append(
      (df["RSI_3_15m"] > 55.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 50.0) | (df["AROONU_14_4h"] < 85.0)
    )
    # 15m down move, 15m & 1h still high
    long_entry_logic.append(
      (df["RSI_3_15m"] > 55.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 50.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 50.0)
    )
    # 1h down move, 4h still high, 1d high
    long_entry_logic.append(
      (df["RSI_3_1h"] > 25.0) | (df["AROONU_14_4h"] < 50.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 90.0)
    )
    # 1h & 4h down move, 1h still high
    long_entry_logic.append((df["RSI_3_1h"] > 30.0) | (df["RSI_3_4h"] > 65.0) | (df["AROONU_14_1h"] < 50.0))
    long_entry_logic.append(
      (df["RSI_3_1h"] > 30.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 40.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 90.0)
    )
    # 1h & 4h down move, 4h still high
    long_entry_logic.append(
      (df["RSI_3_1h"] > 35.0) | (df["RSI_3_4h"] > 55.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 50.0)
    )
    # 1h & 4h down move, 4h high
    long_entry_logic.append(
      (df["RSI_3_1h"] > 35.0) | (df["RSI_3_4h"] > 60.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 80.0)
    )
    # 1h down move, 15m & 1h still high
    long_entry_logic.append(
      (df["RSI_3_1h"] > 40.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 50.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 50.0)
    )
    # 1h down move, 1h still high, 4h high
    long_entry_logic.append(
      (df["RSI_3_1h"] > 40.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 50.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 70.0)
    )
    # 1h down move, 1h high
    long_entry_logic.append((df["RSI_3_1h"] > 40.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 60.0))
    # 1h down move, 4h & 1d high
    long_entry_logic.append((df["RSI_3_1h"] > 40.0) | (df["AROONU_14_4h"] < 85.0) | (df["AROONU_14_1d"] < 90.0))
    # 1h down move, 1h still high, 4h high
    long_entry_logic.append((df["RSI_3_1h"] > 45.0) | (df["AROONU_14_1h"] < 50.0) | (df["AROONU_14_4h"] < 90.0))
    # 1h down move, 1h still high, 1d high
    long_entry_logic.append((df["RSI_3_1h"] > 45.0) | (df["AROONU_14_1h"] < 50.0) | (df["AROONU_14_1d"] < 90.0))
    # 1h down move, 1h high
    long_entry_logic.append((df["RSI_3_1h"] > 45.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 60.0))
    # 1h & 4h down move, 15m high
    long_entry_logic.append((df["RSI_3_1h"] > 50.0) | (df["RSI_3_4h"] > 60.0) | (df["AROONU_14_15m"] < 70.0))
    # 1h down move, 15m still high, 4h high
    long_entry_logic.append((df["RSI_3_1h"] > 50.0) | (df["AROONU_14_15m"] < 50.0) | (df["AROONU_14_4h"] < 80.0))
    # 1h down move, 15m high, 1h still high
    long_entry_logic.append(
      (df["RSI_3_1h"] > 50.0) | (df["AROONU_14_15m"] < 70.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 40.0)
    )
    # 1h down move, 15m still high, 4h high
    long_entry_logic.append(
      (df["RSI_3_1h"] > 50.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 50.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 80.0)
    )
    # 1h down move, 15m & 1h high
    long_entry_logic.append(
      (df["RSI_3_1h"] > 50.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 60.0) | (df["AROONU_14_1h"] < 60.0)
    )
    # 1h down move, 1h & 1d high
    long_entry_logic.append(
      (df["RSI_3_1h"] > 50.0) | (df["AROONU_14_1h"] < 70.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 80.0)
    )
    # 1h down move, 4h still high, 1d high
    long_entry_logic.append(
      (df["RSI_3_1h"] > 50.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 50.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 90.0)
    )
    # 1h down move, 1h still high, 1d high
    long_entry_logic.append((df["RSI_3_1h"] > 50.0) | (df["AROONU_14_1h"] < 50.0) | (df["AROONU_14_1d"] < 90.0))
    # 1h down move, 4h overbought
    long_entry_logic.append((df["RSI_3_1h"] > 50.0) | (df["ROC_9_4h"] < 40.0))
    # 1h down move, 1h & 4h high
    long_entry_logic.append((df["RSI_3_1h"] > 55.0) | (df["AROONU_14_1h"] < 70.0) | (df["AROONU_14_4h"] < 100.0))
    # 1h down move, 5m up move, 1h still high
    long_entry_logic.append(
      (df["RSI_3_1h"] > 60.0) | (df["RSI_3"] < 60.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 50.0)
    )
    # 1h down move, 15m still not low enough, 4h high
    long_entry_logic.append(
      (df["RSI_3_1h"] > 60.0) | (df["AROONU_14_15m"] < 70.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 90.0)
    )
    # 1h down move, 15m still not low enough, 1h high
    long_entry_logic.append(
      (df["RSI_3_1h"] > 60.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 30.0) | (df["AROONU_14_1h"] < 70.0)
    )
    # 1h down move, 15m still not low enough, 1h high
    long_entry_logic.append(
      (df["RSI_3_1h"] > 60.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 30.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 60.0)
    )
    # 1h down move, 15m & 4h still high
    long_entry_logic.append(
      (df["RSI_3_1h"] > 60.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 50.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 50.0)
    )
    # 1h down move, 15m & 1h high
    long_entry_logic.append((df["RSI_3_1h"] > 60.0) | (df["AROONU_14_15m"] < 70.0) | (df["AROONU_14_1h"] < 90.0))
    # 1h down move, 1h still high, 4h high
    long_entry_logic.append(
      (df["RSI_3_1h"] > 60.0) | (df["AROONU_14_1h"] < 50.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 90.0)
    )
    # 1h down move, 1h high, 4h still high
    long_entry_logic.append((df["RSI_3_1h"] > 60.0) | (df["AROONU_14_1h"] < 80.0) | (df["AROONU_14_4h"] < 40.0))
    # 1h down move, 1h still high, 4h high
    long_entry_logic.append(
      (df["RSI_3_1h"] > 60.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 40.0) | (df["AROONU_14_4h"] < 70.0)
    )
    # 1h down move, 1h & 1d high
    long_entry_logic.append(
      (df["RSI_3_1h"] > 60.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 70.0) | (df["AROONU_14_1d"] < 90.0)
    )
    # 1h down move, 4h & 1d high
    long_entry_logic.append((df["RSI_3_1h"] > 60.0) | (df["RSI_14_4h"] < 70.0) | (df["RSI_14_1d"] < 80.0))
    # 15m & 1h & 4h down move, 4h high
    long_entry_logic.append(
      (df["RSI_3_15m"] > 50.0) | (df["RSI_3_1h"] > 65.0) | (df["RSI_3_4h"] > 65.0) | (df["AROONU_14_4h"] < 85.0)
    )
    # 4h down move, 15m high
    long_entry_logic.append((df["RSI_3_4h"] > 20.0) | (df["AROONU_14_15m"] < 80.0))
    # 4h down move, 1h high
    long_entry_logic.append((df["RSI_3_4h"] > 25.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 80.0))
    # 4h down move, 15m & 4h still high
    long_entry_logic.append((df["RSI_3_4h"] > 30.0) | (df["AROONU_14_15m"] < 50.0) | (df["AROONU_14_4h"] < 50.0))
    # 4h down move, 15m still high, 1d overbought
    long_entry_logic.append(
      (df["RSI_3_4h"] > 30.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 50.0) | (df["ROC_9_1d"] < 10.0)
    )
    # 4h down move, 1h & 4h still high
    long_entry_logic.append(
      (df["RSI_3_4h"] > 35.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 50.0) | (df["AROONU_14_4h"] < 50.0)
    )
    # 4h down move, 1d high & overbought
    long_entry_logic.append(
      (df["RSI_3_4h"] > 35.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 80.0) | (df["ROC_9_1d"] < 40.0)
    )
    # 4h down move, 15m & 1h high
    long_entry_logic.append(
      (df["RSI_3_4h"] > 40.0) | (df["AROONU_14_15m"] < 80.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 70.0)
    )
    # 4h down move, 1d high & overbought
    long_entry_logic.append((df["RSI_3_4h"] > 40.0) | (df["AROONU_14_1d"] < 80.0) | (df["ROC_9_1d"] < 20.0))
    # 4h down move, 15m still high, 1h high
    long_entry_logic.append(
      (df["RSI_3_4h"] > 40.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 40.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 80.0)
    )
    # 4h down move, 1h & 4h still high
    long_entry_logic.append(
      (df["RSI_3_4h"] > 40.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 50.0) | (df["RSI_14_4h"] < 50.0)
    )
    # 4h down move, 1h still high, 4h still moving down
    long_entry_logic.append(
      (df["RSI_3_4h"] > 40.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 50.0) | (df["CCI_20_change_pct_4h"] > -0.0)
    )
    # 4h down move, 1d high & overbought
    long_entry_logic.append(
      (df["RSI_3_4h"] > 40.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 80.0) | (df["ROC_9_1d"] < 10.0)
    )
    # 4h down move, 1h high, 4h still high
    long_entry_logic.append((df["RSI_3_4h"] > 45.0) | (df["AROONU_14_1h"] < 70.0) | (df["AROONU_14_4h"] < 50.0))
    # 4h down move, 15m high, 4h still high
    long_entry_logic.append(
      (df["RSI_3_4h"] > 50.0) | (df["AROONU_14_15m"] < 70.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 40.0)
    )
    # 4h down move, 15m still high, 1h high
    long_entry_logic.append(
      (df["RSI_3_4h"] > 50.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 40.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 70.0)
    )
    # 4h down move, 15m & 4h still high
    long_entry_logic.append(
      (df["RSI_3_4h"] > 50.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 50.0) | (df["AROONU_14_4h"] < 50.0)
    )
    # 4h down move, 15m high, 4h still not low enough
    long_entry_logic.append(
      (df["RSI_3_4h"] > 50.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 70.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 30.0)
    )
    # 4h down move, 1h still high, 4h high
    long_entry_logic.append(
      (df["RSI_3_4h"] > 50.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 50.0) | (df["AROONU_14_4h"] < 70.0)
    )
    # 4h down move, 15m & 1d high
    long_entry_logic.append((df["RSI_3_4h"] > 50.0) | (df["AROONU_14_15m"] < 70.0) | (df["AROONU_14_1d"] < 90.0))
    # 4h down move, 1d high & overbought
    long_entry_logic.append((df["RSI_3_4h"] > 50.0) | (df["AROONU_14_1d"] < 90.0) | (df["ROC_9_1d"] < 20.0))
    # 4h down move, 15m & 4h high
    long_entry_logic.append((df["RSI_3_4h"] > 60.0) | (df["AROONU_14_15m"] < 70.0) | (df["AROONU_14_4h"] < 70.0))
    # 4h down move, 15m high, 4h still high
    long_entry_logic.append((df["RSI_3_4h"] > 60.0) | (df["AROONU_14_15m"] < 80.0) | (df["AROONU_14_4h"] < 40.0))
    # 4h down move, 15m still high, 1h high
    long_entry_logic.append(
      (df["RSI_3_4h"] > 60.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 50.0) | (df["AROONU_14_1h"] < 70.0)
    )
    # 4h down move, 15m still high, 4h high
    long_entry_logic.append(
      (df["RSI_3_4h"] > 60.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 50.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 70.0)
    )
    # 4h down move, 15m & 4h high
    long_entry_logic.append(
      (df["RSI_3_4h"] > 60.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 70.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 60.0)
    )
    # 4h down move, 1h & 4h high
    long_entry_logic.append(
      (df["RSI_3_4h"] > 60.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 70.0) | (df["AROONU_14_4h"] < 70.0)
    )
    # 4h down move, 4h still high, 1d high
    long_entry_logic.append(
      (df["RSI_3_4h"] > 60.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 50.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 80.0)
    )
    # 15m still high, 1d high & overbought
    long_entry_logic.append(
      (df["AROONU_14_15m"] < 50.0) | (df["AROONU_14_1d"] < 100.0) | (df["ROC_9_1d"] < 100.0)
    )
    # 15m high, 4h high
    long_entry_logic.append((df["AROONU_14_15m"] < 70.0) | (df["AROONU_14_4h"] < 85.0))
    # 15m & 1d high, 1d overbought
    long_entry_logic.append((df["AROONU_14_15m"] < 70.0) | (df["AROONU_14_1d"] < 90.0) | (df["ROC_9_1d"] < 20.0))
    # 15m & 1d high, 4h overbought
    long_entry_logic.append(
      (df["AROONU_14_15m"] < 70.0) | (df["AROONU_14_1d"] < 100.0) | (df["ROC_9_4h"] < 10.0)
    )
    # 15m high, 4h still high
    long_entry_logic.append((df["AROONU_14_15m"] < 80.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 50.0))
    # 4h & 1d high, 1d overbought
    long_entry_logic.append(
      (df["AROONU_14_4h"] < 100.0) | (df["AROONU_14_1d"] < 100.0) | (df["ROC_9_1d"] < 20.0)
    )
    # 4h high, 4h overbought
    long_entry_logic.append((df["AROONU_14_4h"] < 70.0) | (df["ROC_9_4h"] < 40.0))
    # 4h high, 1d overbought
    long_entry_logic.append((df["AROONU_14_4h"] < 70.0) | (df["ROC_9_1d"] < 40.0))
    # 1d high, 4h overbought
    long_entry_logic.append((df["AROONU_14_1d"] < 90.0) | (df["ROC_9_4h"] < 40.0))
    # 1d high & overbought
    long_entry_logic.append((df["AROONU_14_1d"] < 100.0) | (df["ROC_9_1d"] < 200.0))
    # 15m high, 1h still high
    long_entry_logic.append((df["STOCHRSIk_14_14_3_3_15m"] < 70.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 40.0))
    # 15m & 4h high
    long_entry_logic.append((df["STOCHRSIk_14_14_3_3_15m"] < 70.0) | (df["AROONU_14_4h"] < 70.0))
    # 15m high, 1d overbought
    long_entry_logic.append((df["STOCHRSIk_14_14_3_3_15m"] < 70.0) | (df["ROC_9_1d"] < 10.0))
    # 15m high, 1h still not low enough
    long_entry_logic.append((df["STOCHRSIk_14_14_3_3_15m"] < 80.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 30.0))
    # 1d high, 4h overbought
    long_entry_logic.append((df["STOCHRSIk_14_14_3_3_1d"] < 80.0) | (df["ROC_9_4h"] < 40.0))
    # 1d high & overbought
    long_entry_logic.append((df["STOCHRSIk_14_14_3_3_1d"] < 90.0) | (df["ROC_9_1d"] < 30.0))
    # 4h & 1d overbought
    long_entry_logic.append((df["ROC_9_4h"] < 40.0) | (df["ROC_9_1d"] < 40.0))
    # 1d green with top wick, 1d overbought
    long_entry_logic.append(
      (df["change_pct_1d"] < 25.0) | (df["top_wick_pct_1d"] < 25.0) | (df["ROC_9_1d"] < 50.0)
    )

    # Logic
    long_entry_logic.append(df["RSI_14"] < 50.0)
    long_entry_logic.append(df["AROONU_14_15m"] < 90.0)
    long_entry_logic.append(df["STOCHRSIk_14_14_3_3_15m"] < 90.0)
    long_entry_logic.append(
      (df["SMA_21"].shift(1) < df["SMA_200"].shift(1).infer_objects(copy=False).fillna(value=np.nan))
      & df["SMA_200"].shift(1).notna()
    )
    long_entry_logic.append(
      (df["SMA_21"] > df["SMA_200"].infer_objects(copy=False).fillna(value=np.nan)) & df["SMA_200"].notna()
    )
    long_entry_logic.append(
      (df["close"] > df["EMA_200_1h"].infer_objects(copy=False).fillna(value=np.nan)) & df["EMA_200_1h"].notna()
    )
    long_entry_logic.append(
      (df["close"] > df["EMA_200_4h"].infer_objects(copy=False).fillna(value=np.nan)) & df["EMA_200_4h"].notna()
    )
    long_entry_logic.append(df["BBB_20_2.0"] > 1.5)
    long_entry_logic.append(df["BBB_20_2.0_1h"] > 6.0)


def append_long_162(df, long_entry_logic, allowed_empty_candles_288) -> None:
    """Append NFI long condition #162, the scalp-mode long entry."""
    # Protections
    long_entry_logic.append(df["num_empty_288"] <= allowed_empty_candles_288)
    long_entry_logic.append(df["protections_long_global"] == True)

    long_entry_logic.append(
      (df["RSI_3"] > 5.0) & (df["RSI_3_15m"] > 5.0) & (df["ROC_9_15m"] > -10.0) & (df["ROC_9_1d"] < 200.0)
    )

    long_entry_logic.append(
      # 15m & 1h down move, 4h high
      ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1h"] > 20.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 70.0))
      # 15m & 4h down move, 1h still high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_4h"] > 40.0) | (df["RSI_14_1h"] < 50.0))
      # 15m & 1d down move, 4h high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1d"] > 20.0) | (df["AROONU_14_4h"] < 90.0))
      # 15m down move, 15m still high, 1h high
      & ((df["RSI_3_15m"] > 10.0) | (df["AROONU_14_15m"] < 50.0) | (df["AROONU_14_1h"] < 80.0))
      # 15m down move, 15m high
      & ((df["RSI_3_15m"] > 10.0) | (df["AROONU_14_15m"] < 70.0))
      # 15m down move, 1h & 1d high
      & ((df["RSI_3_15m"] > 10.0) | (df["AROONU_14_1h"] < 90.0) | (df["AROONU_14_1d"] < 100.0))
      # 15m down move, 4h & 1d high
      & ((df["RSI_3_15m"] > 10.0) | (df["AROONU_14_4h"] < 75.0) | (df["AROONU_14_1d"] < 100.0))
      # 15m down move, 1d high, 1d downtrend
      & ((df["RSI_3_15m"] > 10.0) | (df["AROONU_14_1d"] < 85.0) | (df["CMF_20_1d"] > -0.40))
      # 15m & 1h down move, 15m still not low enough
      & ((df["RSI_3_15m"] > 15.0) | (df["RSI_3_1h"] > 20.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 30.0))
      # 15m & 1h down nove, 1h still high
      & ((df["RSI_3_15m"] > 15.0) | (df["RSI_3_1h"] > 20.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 50.0))
      # 15m & 1h down move, 4h high
      & ((df["RSI_3_15m"] > 15.0) | (df["RSI_3_1h"] > 30.0) | (df["AROONU_14_4h"] < 100.0))
      # 15m & 1h down move, 4h high
      & ((df["RSI_3_15m"] > 15.0) | (df["RSI_3_1h"] > 35.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 90.0))
      # 15m down move, 4h high, 4h downtrend
      & ((df["RSI_3_15m"] > 15.0) | (df["AROONU_14_4h"] < 60.0) | (df["ROC_9_4h"] > -20.0))
      # 15m down move, 4h & 1d downtrend
      & ((df["RSI_3_15m"] > 15.0) | (df["ROC_9_4h"] > -10.0) | (df["ROC_9_1d"] > -40.0))
      # 15m & 1h down move, 1h high
      & ((df["RSI_3_15m"] > 20.0) | (df["RSI_3_1h"] > 25.0) | (df["AROONU_14_1h"] < 70.0))
      # 15m down move, 4h high & overbought
      & ((df["RSI_3_15m"] > 20.0) | (df["AROONU_14_4h"] < 70.0) | (df["ROC_9_4h"] < 20.0))
      # 15m & 1h down move, 4h high
      & ((df["RSI_3_15m"] > 25.0) | (df["RSI_3_1h"] > 25.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 90.0))
      # 15m down move, 15m high, 1d overbought
      & ((df["RSI_3_15m"] > 25.0) | (df["AROONU_14_15m"] < 60.0) | (df["ROC_9_1d"] < 150.0))
      # 15m down move, 1h & 4h high
      & ((df["RSI_3_15m"] > 35.0) | (df["AROONU_14_1h"] < 80.0) | (df["RSI_14_4h"] < 80.0))
      # 1h & 4h down move, 15m stil high
      & ((df["RSI_3_1h"] > 3.0) | (df["RSI_3_4h"] > 10.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 50.0))
      # 1h & 4h down move, 1h still high
      & ((df["RSI_3_1h"] > 3.0) | (df["RSI_3_4h"] > 25.0) | (df["AROONU_14_1h"] < 40.0))
      # 1h & 4h down move, 4h high
      & ((df["RSI_3_1h"] > 5.0) | (df["RSI_3_4h"] > 20.0) | (df["AROONU_14_4h"] < 60.0))
      # 1h & 4h down move, 4h high
      & ((df["RSI_3_1h"] > 5.0) | (df["RSI_3_4h"] > 30.0) | (df["AROONU_14_4h"] < 90.0))
      # 1h down move, 4h high, 1d overbought
      & ((df["RSI_3_1h"] > 5.0) | (df["AROONU_14_4h"] < 60.0) | (df["ROC_9_1d"] < 10.0))
      # 1h & 4h down move, 4h still high
      & ((df["RSI_3_1h"] > 10.0) | (df["RSI_3_4h"] > 10.0) | (df["AROONU_14_4h"] < 50.0))
      # 1h & 3h down move, 1d high
      & ((df["RSI_3_1h"] > 10.0) | (df["RSI_3_4h"] > 40.0) | (df["AROONU_14_1d"] < 80.0))
      # 1h & 4h down move, 4h high
      & ((df["RSI_3_1h"] > 15.0) | (df["RSI_3_4h"] > 20.0) | (df["AROONU_14_4h"] < 70.0))
      # 1h & 4h down move, 4h high
      & ((df["RSI_3_1h"] > 20.0) | (df["RSI_3_4h"] > 35.0) | (df["AROONU_14_4h"] < 70.0))
      # 1h & 4h down move, 1d downtrend
      & ((df["RSI_3_1h"] > 15.0) | (df["RSI_3_4h"] > 25.0) | (df["ROC_9_1d"] > -30.0))
      # 1h down move, 1h & 1d high
      & ((df["RSI_3_1h"] > 15.0) | (df["AROONU_14_1h"] < 60.0) | (df["AROONU_14_1d"] < 85.0))
      # 1h down move, 1h high, 1d overbought
      & ((df["RSI_3_1h"] > 15.0) | (df["AROONU_14_1h"] < 60.0) | (df["ROC_9_1d"] < 50.0))
      # 1h down move, 1d high & overbought
      & ((df["RSI_3_1h"] > 15.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 90.0) | (df["ROC_9_1d"] < 40.0))
      # 1h down move, 1h high, 1d overbought
      & ((df["RSI_3_1h"] > 25.0) | (df["AROONU_14_1h"] < 60.0) | (df["ROC_9_1d"] < 100.0))
      # 1h down move, 1h high
      & ((df["RSI_3_1h"] > 25.0) | (df["AROONU_14_1h"] < 90.0))
      # 1h & 4h down move, 4h high
      & ((df["RSI_3_1h"] > 30.0) | (df["RSI_3_4h"] > 35.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 70.0))
      # 1h down move, 1h high, 4h overbought
      & ((df["RSI_3_1h"] > 30.0) | (df["AROONU_14_1h"] < 60.0) | (df["ROC_9_4h"] < 50.0))
      # 1h down move, 4h high & overbought
      & ((df["RSI_3_1h"] > 35.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 80.0) | (df["ROC_9_4h"] < 30.0))
      # 1h down move, 1h high, 4h downtrend
      & ((df["RSI_3_1h"] > 40.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 80.0) | (df["ROC_9_4h"] > -20.0))
      # 1h down move, 15m still high, 1d overbought
      & ((df["RSI_3_1h"] > 45.0) | (df["AROONU_14_15m"] < 50.0) | (df["ROC_9_1d"] < 50.0))
      # 1h down move, 4h & 1d overbought
      & ((df["RSI_3_1h"] > 45.0) | (df["ROC_9_4h"] < 10.0) | (df["ROC_9_1d"] < 50.0))
      # 1h down move,  4h high, 1d overbought
      & ((df["RSI_3_1h"] > 50.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 90.0) | (df["ROC_9_1d"] < 150.0))
      # 4h down move, 1d high
      & ((df["RSI_3_4h"] > 3.0) | (df["AROONU_14_1d"] < 90.0))
      # 4h down move, 15m still high
      & ((df["RSI_3_4h"] > 3.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 50.0))
      # 4h down move, 1d high
      & ((df["RSI_3_4h"] > 3.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 90.0))
      # 4h down move, 1d overbought
      & ((df["RSI_3_4h"] > 3.0) | (df["ROC_9_1d"] < 40.0))
      # 4h & 1d down move
      & ((df["RSI_3_4h"] > 5.0) | (df["RSI_3_1d"] > 10.0))
      # 4h down move, 1d high, 1h downtrend
      & ((df["RSI_3_4h"] > 10.0) | (df["AROONU_14_1d"] < 85.0) | (df["ROC_9_1h"] > -30.0))
      # 4h down move, 1h & 4h downtrend
      & ((df["RSI_3_4h"] > 10.0) | (df["ROC_9_1h"] > -40.0) | (df["ROC_9_4h"] > -40.0))
      # 4h & 1d down move, 4h still not low enough
      & ((df["RSI_3_4h"] > 20.0) | (df["RSI_3_1d"] > 20.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 30.0))
      # 4h down move, 4h still high, 1d downtrend
      & ((df["RSI_3_4h"] > 30.0) | (df["AROONU_14_4h"] < 50.0) | (df["ROC_9_1d"] > -40.0))
      # 4h down move, 15m still high, 1d overbought
      & ((df["RSI_3_4h"] > 40.0) | (df["AROONU_14_15m"] < 50.0) | (df["ROC_9_1d"] < 50.0))
      # 4h down move, 4h & 1d overbought
      & ((df["RSI_3_4h"] > 40.0) | (df["ROC_9_4h"] < 10.0) | (df["ROC_9_1d"] < 50.0))
      # 1d down move, 1h high
      & ((df["RSI_3_1d"] > 3.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 70.0))
      # 1d down move, 15m still high
      & ((df["RSI_3_1d"] > 3.0) | (df["AROONU_14_15m"] < 50.0))
      # 1d down move, 15m still high, 1h high
      & ((df["RSI_3_1d"] > 10.0) | (df["AROONU_14_15m"] < 40.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 70.0))
      # 1d down move, 1h & 4h high
      & ((df["RSI_3_1d"] > 10.0) | (df["AROONU_14_1h"] < 70.0) | (df["AROONU_14_4h"] < 90.0))
      # 1d down move, 4h high
      & ((df["RSI_3_1d"] > 20.0) | (df["RSI_14_4h"] < 80.0))
      # 1d downtrend, 1d high & overbought
      & ((df["CMF_20_1d"] > -0.30) | (df["AROONU_14_1d"] < 85.0) | (df["ROC_9_1d"] < 100.0))
      # 1h & 4h high, 1d overbought
      & ((df["AROONU_14_1h"] < 70.0) | (df["AROONU_14_4h"] < 70.0) | (df["ROC_9_1d"] < 30.0))
      # 1h & 4h high, 1d overbought
      & ((df["AROONU_14_1h"] < 90.0) | (df["AROONU_14_4h"] < 90.0) | (df["ROC_9_1d"] < 20.0))
      # 1h & 4h high
      & ((df["AROONU_14_1h"] < 100.0) | (df["AROONU_14_4h"] < 100.0))
      # 4h & 1d high, 4h overbought
      & ((df["AROONU_14_4h"] < 80.0) | (df["AROONU_14_1d"] < 100.0) | (df["ROC_9_4h"] < 30.0))
      # 4h high, 4h & 1d overbought
      & ((df["AROONU_14_4h"] < 80.0) | (df["ROC_9_4h"] < 20.0) | (df["ROC_9_1d"] < 20.0))
      # 1d still high, 1h & 4h downtrend
      & ((df["AROONU_14_1d"] < 50.0) | (df["ROC_9_1h"] > -20.0) | (df["ROC_9_4h"] > -20.0))
      # 1h high, 1h overbought
      & ((df["STOCHRSIk_14_14_3_3_1h"] < 80.0) | (df["ROC_9_1h"] < 50.0))
      # 1h high, 1d downtrend
      & ((df["STOCHRSIk_14_14_3_3_1h"] < 80.0) | (df["ROC_9_1d"] > -60.0))
      # 4h high, 1h overbought, 1d downtrend
      & ((df["STOCHRSIk_14_14_3_3_4h"] < 80.0) | (df["ROC_9_1h"] < 10.0) | (df["ROC_9_1d"] > -70.0))
      # 4h high, 1h & 4h overbought
      & ((df["STOCHRSIk_14_14_3_3_4h"] < 90.0) | (df["ROC_9_1h"] < 20.0) | (df["ROC_9_4h"] < 50.0))
      # 1h & 4h overbought
      & ((df["ROC_9_1h"] < 100.0) | (df["ROC_9_4h"] < 100.0))
      # 1h P&D, 1h down move
      & ((df["change_pct_1h"] > -10.0) | (df["change_pct_1h"].shift(12) < 10.0) | (df["RSI_3_1h"] > 50.0))
      # 4h P&D, 4h high
      & ((df["change_pct_4h"] > -15.0) | (df["change_pct_4h"].shift(48) < 30.0) | (df["AROONU_14_4h"] < 90.0))
      # 4h green, 15m & 1h down move
      & ((df["change_pct_4h"] < 10.0) | (df["RSI_3_15m"] > 10.0) | (df["RSI_3_1h"] > 35.0))
      # 4h green, 1h down move
      & ((df["change_pct_4h"] < 40.0) | (df["RSI_3_1h"] > 50.0))
      # 4h green with top wick
      & ((df["change_pct_4h"] < 50.0) | (df["change_pct_4h"] < 50.0))
      # 1d green with top wick, 15m still high
      & ((df["change_pct_1d"] < 10.0) | (df["top_wick_pct_1d"] < 8.0) | (df["AROONU_14_15m"] < 50.0))
      # 1d green, 4h down move, 4h still high
      & ((df["change_pct_1d"] < 40.0) | (df["RSI_3_4h"] > 35.0) | (df["AROONU_14_4h"] < 50.0))
      # 1d green with top wick, 4h down move
      & ((df["change_pct_1d"] < 40.0) | (df["top_wick_pct_1d"] < 8.0) | (df["RSI_3_4h"] > 55.0))
      # 1d top wick, 4h still high
      & ((df["top_wick_pct_1d"] < 50.0) | (df["AROONU_14_4h"] < 50.0))
      # big drop in last 4 days, 1d down move
      & ((df["close"] > (df["high_max_24_4h"] * 0.20)) | (df["RSI_3_1d"] > 20.0))
      # big drop in the last 20 days, 4h down move
      & ((df["close"] > (df["high_max_20_1d"] * 0.15)) | (df["RSI_3_4h"] > 20.0))
      # big drop in the last 20 days, 1d down move
      & ((df["close"] > (df["high_max_20_1d"] * 0.05)) | (df["RSI_3_1d"] > 20.0))
      # big drop in the last 20 days, 1h still high
      & ((df["close"] > (df["high_max_20_1d"] * 0.05)) | (df["STOCHRSIk_14_14_3_3_1h"] < 45.0))
      # big drop in the last 20 days, 4h high
      & ((df["close"] > (df["high_max_20_1d"] * 0.05)) | (df["STOCHRSIk_14_14_3_3_4h"] < 70.0))
    )

    # Logic
    long_entry_logic.append(
      (df["AROONU_14"] < 25.0)
      & (df["AROOND_14"] > 75.0)
      & (df["STOCHRSIk_14_14_3_3"] < 30.0)
      & (df["EMA_26"] > df["EMA_12"])
      & ((df["EMA_26"] - df["EMA_12"]) > (df["open"] * 0.030))
      & ((df["EMA_26"].shift() - df["EMA_12"].shift()) > (df["open"] / 100.0))
      & (df["close"] < df["SMA_9"])
    )


def append_long_163(df, long_entry_logic, allowed_empty_candles_288) -> None:
    """Append NFI long condition #163, the scalp-mode long entry."""
    # Protections
    long_entry_logic.append(df["num_empty_288"] <= allowed_empty_candles_288)
    long_entry_logic.append(df["protections_long_global"] == True)

    long_entry_logic.append((df["RSI_3"] > 10.0) & (df["RSI_3_15m"] > 10.0) & (df["RSI_3_1h"] > 20.0))

    long_entry_logic.append(
      # 5m & 15m & 4h down mnove, 4h high
      ((df["RSI_3"] > 15.0) | (df["RSI_3_15m"] > 20.0) | (df["RSI_3_4h"] > 40.0) | (df["AROONU_14_4h"] < 80.0))
      # 5m & 15m & 1d down move, 1h high
      & ((df["RSI_3"] > 15.0) | (df["RSI_3_15m"] > 25.0) | (df["RSI_3_1d"] > 25.0) | (df["AROONU_14_1h"] < 90.0))
      # 5m & 1h down move, 15m still high, 4h high
      & (
        (df["RSI_3"] > 20.0) | (df["RSI_3_1h"] > 40.0) | (df["RSI_14_15m"] < 40.0) | (df["AROONU_14_4h"] < 100.0)
      )
      # 5m & 1h & 15m down move, 1h still not low enough
      & ((df["RSI_3"] > 15.0) | (df["RSI_3_1h"] > 30.0) | (df["RSI_3_1d"] > 15.0) | (df["AROONU_14_1h"] < 30.0))
      # 15m & 4h down move, 4h high
      & ((df["RSI_3"] > 15.0) | (df["RSI_3_4h"] > 35.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 70.0))
      # 5m & 4h down move, 15m high
      & ((df["RSI_3"] > 15.0) | (df["RSI_3_4h"] > 45.0) | (df["AROONU_14_15m"] < 60.0))
      # 15m & 1h down move, 1h high
      & ((df["RSI_3_15m"] > 12.0) | (df["RSI_3_1h"] > 40.0) | (df["AROONU_14_1h"] < 100.0))
      # 15m & 1h & 4h & 1d down move
      & ((df["RSI_3_15m"] > 15.0) | (df["RSI_3_1h"] > 25.0) | (df["RSI_3_4h"] > 25.0) | (df["RSI_3_1d"] > 25.0))
      # 15m & 1h down move, 1h & 4h high
      & (
        (df["RSI_3_15m"] > 15.0)
        | (df["RSI_3_1h"] > 25.0)
        | (df["AROONU_14_1h"] < 75.0)
        | (df["AROONU_14_4h"] < 100.0)
      )
      # 15m & 1h & 4h down move, 1d overbought
      & ((df["RSI_3_15m"] > 15.0) | (df["RSI_3_1h"] > 30.0) | (df["RSI_3_4h"] > 35.0) | (df["ROC_9_1d"] < 40.0))
      # 15m & 1h & 4h down move, 1h downtrend, 4h high
      & (
        (df["RSI_3_15m"] > 15.0)
        | (df["RSI_3_1h"] > 30.0)
        | (df["RSI_3_4h"] > 55.0)
        | (df["CMF_20_1h"] > -0.10)
        | (df["AROONU_14_4h"] < 80.0)
      )
      # 15m & 1h down move, 15m high
      & ((df["RSI_3_15m"] > 15.0) | (df["RSI_3_1h"] > 30.0) | (df["AROONU_14_15m"] < 60.0))
      # 15m & 1h down move, 4h high
      & ((df["RSI_3_15m"] > 15.0) | (df["RSI_3_1h"] > 30.0) | (df["RSI_14_4h"] < 85.0))
      # 15m & 1h down move, 15m still high
      & ((df["RSI_3_15m"] > 15.0) | (df["RSI_3_1h"] > 30.0) | (df["AROONU_14_15m"] < 40.0))
      # 15m & 1h down move, 1h high
      & ((df["RSI_3_15m"] > 15.0) | (df["RSI_3_1h"] > 30.0) | (df["AROONU_14_1h"] < 70.0))
      # 15m & 1h down move, 1h high
      & ((df["RSI_3_15m"] > 15.0) | (df["RSI_3_1h"] > 30.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 70.0))
      # 15m & 1h down move, 1d overbought
      & ((df["RSI_3_15m"] > 15.0) | (df["RSI_3_1h"] > 30.0) | (df["ROC_9_1d"] < 30.0))
      # 15m & 1h & 4h down move, 4h high
      & ((df["RSI_3_15m"] > 15.0) | (df["RSI_3_1h"] > 35.0) | (df["RSI_3_4h"] > 65.0) | (df["MFI_14_4h"] < 85.0))
      # 15m & 1h & 1d down move, 15m high
      & (
        (df["RSI_3_15m"] > 15.0)
        | (df["RSI_3_1h"] > 35.0)
        | (df["RSI_3_1d"] > 40.0)
        | (df["AROONU_14_15m"] < 60.0)
      )
      # 15m & 1h down move, 15m high
      & ((df["RSI_3_15m"] > 15.0) | (df["RSI_3_1h"] > 35.0) | (df["AROONU_14_15m"] < 70.0))
      # 15m & 1h down move, 1h high
      & ((df["RSI_3_15m"] > 15.0) | (df["RSI_3_1h"] > 35.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 85.0))
      # 15m & 1h down move, 15m still not low enough, 1h & 4h high
      & (
        (df["RSI_3_15m"] > 15.0)
        | (df["RSI_3_1h"] > 40.0)
        | (df["AROONU_14_15m"] < 30.0)
        | (df["AROONU_14_1h"] < 80.0)
        | (df["AROONU_14_4h"] < 80.0)
      )
      # 15m & 1h down move, 4h high & overbought
      & ((df["RSI_3_15m"] > 15.0) | (df["RSI_3_1h"] > 45.0) | (df["RSI_14_4h"] < 70.0) | (df["ROC_9_4h"] < 50.0))
      # 15m & 1h down move, 1h high
      & ((df["RSI_3_15m"] > 15.0) | (df["RSI_3_1h"] > 50.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 90.0))
      # 15m & 4h down move, 15m high
      & ((df["RSI_3_15m"] > 15.0) | (df["RSI_3_4h"] > 30.0) | (df["AROONU_14_15m"] < 60.0))
      # 15m & 4h down move, 4h high
      & ((df["RSI_3_15m"] > 15.0) | (df["RSI_3_4h"] > 30.0) | (df["AROONU_14_4h"] < 80.0))
      # 15m & 4h down move, 1h still high
      & ((df["RSI_3_15m"] > 15.0) | (df["RSI_3_4h"] > 40.0) | (df["AROONU_14_1h"] < 40.0))
      # 15m & 4h down move, 1d high
      & ((df["RSI_3_15m"] > 15.0) | (df["RSI_3_4h"] > 35.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 90.0))
      # 15m & 4h down move, 1h high
      & ((df["RSI_3_15m"] > 15.0) | (df["RSI_3_4h"] > 35.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 60.0))
      # 15m & 4h down move, 1h high
      & ((df["RSI_3_15m"] > 15.0) | (df["RSI_3_4h"] > 50.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 80.0))
      # 15m down move, 4h & 1d up move, 1d downtrend
      & ((df["RSI_3_15m"] > 15.0) | (df["RSI_3_4h"] < 90.0) | (df["RSI_3_1d"] < 80.0) | (df["CMF_20_1d"] > -0.2))
      # 15m & 1d down move, 4h high
      & ((df["RSI_3_15m"] > 15.0) | (df["RSI_3_1d"] > 10.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 70.0))
      # 15m & 1h down move, 1h & 4h still high
      & (
        (df["RSI_3_15m"] > 15.0)
        | (df["RSI_3_1d"] > 15.0)
        | (df["AROONU_14_1h"] < 50.0)
        | (df["AROONU_14_4h"] < 50.0)
      )
      # 15m & 1d down move, 1h high
      & ((df["RSI_3_15m"] > 15.0) | (df["RSI_3_1d"] > 15.0) | (df["AROONU_14_1h"] < 100.0))
      # 15m & 1d down move, 1d high
      & ((df["RSI_3_15m"] > 15.0) | (df["RSI_3_1d"] > 20.0) | (df["AROONU_14_1d"] < 80.0))
      # 15m & 1d down move, 1d overbought
      & ((df["RSI_3_15m"] > 15.0) | (df["RSI_3_1d"] > 40.0) | (df["ROC_9_1d"] < 50.0))
      # 15m & 1d down move, 1d high
      & ((df["RSI_3_15m"] > 15.0) | (df["RSI_3_1d"] > 50.0) | (df["AROONU_14_1d"] < 70.0))
      # 15m & 1d down move, 1d high
      & ((df["RSI_3_15m"] > 15.0) | (df["RSI_3_1d"] > 60.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 80.0))
      # 15m down move, 15m & 4h high
      & ((df["RSI_3_15m"] > 15.0) | (df["AROONU_14_15m"] < 70.0) | (df["AROONU_14_4h"] < 90.0))
      # 15m down move, 15m & 1h high
      & ((df["RSI_3_15m"] > 15.0) | (df["AROONU_14_15m"] < 75.0) | (df["AROONU_14_1h"] < 100.0))
      # 15m down move, 1h high, 1d overbought
      & ((df["RSI_3_15m"] > 15.0) | (df["AROONU_14_1h"] < 90.0) | (df["ROC_9_1d"] < 80.0))
      # 15m down move, 1h high, 1d overbought
      & ((df["RSI_3_15m"] > 15.0) | (df["AROONU_14_1h"] < 100.0) | (df["ROC_9_1d"] < 40.0))
      # 15m down move, 4h still high, 4h downtrend
      & ((df["RSI_3_15m"] > 15.0) | (df["AROONU_14_4h"] < 40.0) | (df["ROC_9_4h"] > -20.0))
      # 15m down move, 1d high & overbought
      & ((df["RSI_3_15m"] > 15.0) | (df["AROONU_14_1d"] < 100.0) | (df["ROC_9_1d"] < 100.0))
      # 15m down move, 15m still not low enough, 4h high
      & (
        (df["RSI_3_15m"] > 15.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 30.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 50.0)
      )
      # 15m down move, 15m & 1h high
      & (
        (df["RSI_3_15m"] > 15.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 50.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 50.0)
      )
      # 15m down move, 1h high, 1d overbought
      & ((df["RSI_3_15m"] > 15.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 70.0) | (df["ROC_9_1d"] < 30.0))
      # 15m down move, 1h high, 1d overbought
      & ((df["RSI_3_15m"] > 15.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 70.0) | (df["ROC_9_1d"] < 150.0))
      # 15m down move, 1h high & overbought
      & ((df["RSI_3_15m"] > 15.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 80.0) | (df["ROC_9_1h"] < 20.0))
      # 15m down move, 1h high, 1d overbought
      & ((df["RSI_3_15m"] > 15.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 80.0) | (df["ROC_9_1d"] < 100.0))
      # 15m down move, 4h high, 1d overbought
      & ((df["RSI_3_15m"] > 15.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 80.0) | (df["ROC_9_1d"] < 25.0))
      # 15m down move, 4h high & overbought
      & ((df["RSI_3_15m"] > 15.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 90.0) | (df["ROC_9_4h"] < 25.0))
      # 15m down move, 4h high
      & (
        (df["RSI_3_15m"] > 15.0)
        | (df["RSI_14_4h"] < 70.0)
        | (df["STOCHRSIk_14_14_3_3_4h"] < 90.0)
        | (df["EMA_9"] < (df["EMA_26"] * 0.972))
      )
      # 15m down move, 4h high and downtrend
      & ((df["RSI_3_15m"] > 15.0) | (df["CMF_20_4h"] > -0.2) | (df["AROONU_14_4h"] < 80.0))
      # 15m down move, 1h high, 4h overbought
      & ((df["RSI_3_15m"] > 15.0) | (df["AROONU_14_1h"] < 90.0) | (df["ROC_9_4h"] < 20.0))
      # 15m down move, 4h & 1d downtrend
      & ((df["RSI_3_15m"] > 15.0) | (df["ROC_9_4h"] > -20.0) | (df["ROC_9_1d"] > -20.0))
      # 15m & 1h down move, 1h downtrend, 1h downtrend, 15m still high, 1h high
      & (
        (df["RSI_3_15m"] > 20.0)
        | (df["RSI_3_1h"] > 35.0)
        | (df["CMF_20_1h"] > -0.10)
        | (df["AROONU_14_15m"] < 40.0)
        | (df["AROONU_14_1h"] < 85.0)
      )
      # 15m & 1h down move, 4h high & overbought
      & ((df["RSI_3_15m"] > 20.0) | (df["RSI_3_1h"] > 45.0) | (df["RSI_14_4h"] < 70.0) | (df["ROC_9_4h"] < 50.0))
      # 15m & 4h down move, 15m high
      & ((df["RSI_3_15m"] > 20.0) | (df["RSI_3_4h"] > 25.0) | (df["AROONU_14_15m"] < 60.0))
      # 15m & 4h down move, 1h high
      & ((df["RSI_3_15m"] > 20.0) | (df["RSI_3_4h"] > 35.0) | (df["AROONU_14_1h"] < 100.0))
      # 15m & 1d down move, 4h high
      & ((df["RSI_3_15m"] > 20.0) | (df["RSI_3_1d"] > 20.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 70.0))
      # 15m down move, 15m still high, 4h high
      & (
        (df["RSI_3_15m"] > 20.0)
        | (df["RSI_14_15m"] < 40.0)
        | (df["RSI_14_4h"] < 75.0)
        | (df["AROONU_14_4h"] < 100.0)
      )
      # 15m down move, 4h downtrend, 4h overbought
      & ((df["RSI_3_15m"] > 20.0) | (df["CMF_20_4h"] > -0.0) | (df["ROC_9_4h"] < 40.0))
      # 15m down move, 1h & 4h high, 1f overbought
      & (
        (df["RSI_3_15m"] > 20.0)
        | (df["AROONU_14_1h"] < 85.0)
        | (df["RSI_14_4h"] < 70.0)
        | (df["ROC_9_1d"] < 80.0)
      )
      # 15m down move, 1h & 4h high
      & ((df["RSI_3_15m"] > 20.0) | (df["AROONU_14_1h"] < 90.0) | (df["AROONU_14_4h"] < 100.0))
      # 15m down move, 1d high, 4h overbought
      & ((df["RSI_3_15m"] > 20.0) | (df["AROONU_14_1d"] < 100.0) | (df["ROC_9_4h"] < 30.0))
      # 15m down move, 1h high & overbought
      & ((df["RSI_3_15m"] > 20.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 80.0) | (df["ROC_9_1h"] < 10.0))
      # 15m & 1d down move, 1d high
      & ((df["RSI_3_15m"] > 25.0) | (df["RSI_3_1d"] > 40.0) | (df["AROONU_14_1d"] < 80.0))
      # 15m down move, 4h high, 1d downtrend
      & ((df["RSI_3_15m"] > 25.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 90.0) | (df["ROC_9_1d"] > -30.0))
      # 15m & 1h down move, 15m still not low enough, 1h & 4h high
      & (
        (df["RSI_3_15m"] > 30.0)
        | (df["RSI_3_1h"] > 45.0)
        | (df["RSI_14_15m"] < 30.0)
        | (df["RSI_14_1h"] < 50.0)
        | (df["RSI_14_4h"] < 70.0)
        | (df["AROONU_14_15m"] < 20.0)
        | (df["AROONU_14_1h"] < 60.0)
        | (df["AROONU_14_4h"] < 100.0)
      )
      # 15m & 4h down move, 4h overbought
      & ((df["RSI_3_15m"] > 30.0) | (df["RSI_3_4h"] > 60.0) | (df["ROC_9_4h"] < 60.0))
      # 15m & 4h down move, 4h high
      & ((df["RSI_3_15m"] > 35.0) | (df["RSI_3_4h"] > 35.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 80.0))
      # 1h & 4h down move, 1d high
      & ((df["RSI_3_1h"] > 25.0) | (df["RSI_3_4h"] > 30.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 80.0))
      # 1h & 4h down move, 4h high
      & ((df["RSI_3_1h"] > 25.0) | (df["RSI_3_4h"] > 40.0) | (df["AROONU_14_4h"] < 70.0))
      # 1h & 4h down move, 4h high
      & ((df["RSI_3_1h"] > 25.0) | (df["RSI_3_4h"] > 45.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 80.0))
      # 1h & 4h down move, 1d high
      & ((df["RSI_3_1h"] > 25.0) | (df["RSI_3_4h"] > 65.0) | (df["AROONU_14_1d"] < 100.0))
      # 1h & 1d down move, 1d high
      & ((df["RSI_3_1h"] > 25.0) | (df["RSI_3_1d"] > 40.0) | (df["AROONU_14_1d"] < 70.0))
      # 1h down move, 15m downtrend, 4h still high
      & ((df["RSI_3_1h"] > 25.0) | (df["CMF_20_15m"] > -0.4) | (df["AROONU_14_4h"] < 50.0))
      # 1h down move, 4h downtrend, 4h high
      & ((df["RSI_3_1h"] > 25.0) | (df["CMF_20_4h"] > -0.25) | (df["AROONU_14_4h"] < 70.0))
      # 1h down move, 15m still high, 1d downtrend
      & ((df["RSI_3_1h"] > 25.0) | (df["AROONU_14_15m"] < 40.0) | (df["ROC_9_1d"] > -20.0))
      # 1h down move, 1h & 4h high
      & ((df["RSI_3_1h"] > 25.0) | (df["AROONU_14_1h"] < 60.0) | (df["AROONU_14_4h"] < 100.0))
      # 1h down move, 1h high, 1d downtrend
      & ((df["RSI_3_1h"] > 25.0) | (df["AROONU_14_1h"] < 90.0) | (df["CMF_20_1d"] > -0.2))
      # 1h down move, 4h high & overbought
      & ((df["RSI_3_1h"] > 25.0) | (df["AROONU_14_4h"] < 90.0) | (df["ROC_9_4h"] < 20.0))
      # 1h down move, 1h still not low enough, 1d downtrend
      & ((df["RSI_3_1h"] > 25.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 30.0) | (df["ROC_9_1d"] > -40.0))
      # 1h down move, 4h high, 1d overbought
      & ((df["RSI_3_1h"] > 25.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 90.0) | (df["ROC_9_1d"] < 25.0))
      # 1h & 4h down move, 1h still high
      & ((df["RSI_3_1h"] > 30.0) | (df["RSI_3_4h"] > 30.0) | (df["AROONU_14_1h"] < 40.0))
      # 1h & 1d down move, 1d still high
      & ((df["RSI_3_1h"] > 30.0) | (df["RSI_3_1d"] > 30.0) | (df["AROONU_14_1d"] < 40.0))
      # 1h down move, 15m & 4h high
      & ((df["RSI_3_1h"] > 30.0) | (df["AROONU_14_15m"] < 60.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 95.0))
      # 1h down move, 15m & 4h high
      & ((df["RSI_3_1h"] > 30.0) | (df["AROONU_14_15m"] < 70.0) | (df["AROONU_14_4h"] < 90.0))
      # 1h down move, 1h high
      & ((df["RSI_3_1h"] > 30.0) | (df["MFI_14_1h"] < 80.0) | (df["AROONU_14_1h"] < 90.0))
      # 1h down move, 1h still high, 1d overbought
      & ((df["RSI_3_1h"] > 30.0) | (df["AROONU_14_1h"] < 50.0) | (df["ROC_9_1d"] < 40.0))
      # 1h down move, 1h & 4h high
      & ((df["RSI_3_1h"] > 30.0) | (df["AROONU_14_1h"] < 80.0) | (df["AROONU_14_4h"] < 100.0))
      # 1h down move, 1h high, 1d downtrend
      & ((df["RSI_3_1h"] > 30.0) | (df["AROONU_14_1h"] < 90.0) | (df["CMF_20_1d"] > -0.2))
      # 1h down move, 1h highm 1d overbought
      & ((df["RSI_3_1h"] > 30.0) | (df["AROONU_14_1h"] < 90.0) | (df["ROC_9_1d"] < 40.0))
      # 1h down move, 4h high & overbought
      & ((df["RSI_3_1h"] > 30.0) | (df["AROONU_14_4h"] < 100.0) | (df["ROC_9_4h"] < 30.0))
      # 1h down move, 1d high, 4h overbought
      & ((df["RSI_3_1h"] > 30.0) | (df["AROONU_14_1d"] < 100.0) | (df["ROC_9_4h"] < 20.0))
      # 1h & 4h down move, 1h still high, 4h high
      & ((df["RSI_3_1h"] > 35.0) | (df["RSI_3_4h"] > 60.0) | (df["RSI_14_1h"] < 50.0) | (df["RSI_14_4h"] < 70.0))
      # 1h down move, 15m still not low enough, 1h high
      & ((df["RSI_3_1h"] > 35.0) | (df["AROONU_14_15m"] < 30.0) | (df["AROONU_14_1h"] < 80.0))
      # 1h down move, 1h & 1d high
      & ((df["RSI_3_1h"] > 35.0) | (df["AROONU_14_1h"] < 60.0) | (df["AROONU_14_1d"] < 100.0))
      # 1h down move, 1h high, 4h overbought
      & ((df["RSI_3_1h"] > 35.0) | (df["AROONU_14_1h"] < 70.0) | (df["ROC_9_4h"] < 25.0))
      # 1h down move, 1h & 4h high
      & ((df["RSI_3_1h"] > 35.0) | (df["AROONU_14_1h"] < 70.0) | (df["AROONU_14_4h"] < 90.0))
      # 1h down move, 1h & 1d high
      & ((df["RSI_3_1h"] > 35.0) | (df["AROONU_14_1h"] < 90.0) | (df["AROONU_14_1d"] < 90.0))
      # 1h & 1d down move, 1d high
      & ((df["RSI_3_1h"] > 40.0) | (df["RSI_3_1d"] > 55.0) | (df["AROONU_14_1d"] < 100.0))
      # 1h down move, 1h high, 4h overbought
      & ((df["RSI_3_1h"] > 40.0) | (df["AROONU_14_1h"] < 70.0) | (df["ROC_9_4h"] < 40.0))
      # 1h down move, 1h & 4h high
      & ((df["RSI_3_1h"] > 40.0) | (df["AROONU_14_1h"] < 80.0) | (df["AROONU_14_4h"] < 80.0))
      # 1h down move, 1h high, 1d overbought
      & ((df["RSI_3_1h"] > 40.0) | (df["AROONU_14_1h"] < 85.0) | (df["ROC_9_1d"] < 80.0))
      # 1h down move, 1h high, 15m downtrend
      & ((df["RSI_3_1h"] > 40.0) | (df["AROONU_14_1h"] < 90.0) | (df["ROC_9_15m"] > -10.0))
      # 1h down move, 1h high, 1d downtrend
      & ((df["RSI_3_1h"] > 40.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 80.0) | (df["ROC_9_1d"] > -40.0))
      # 1h & 4h down move, 1d overbought
      & ((df["RSI_3_1h"] > 45.0) | (df["RSI_3_4h"] > 65.0) | (df["ROC_9_1d"] < 200.0))
      # 1h & 1d down move, 4h high
      & ((df["RSI_3_1h"] > 45.0) | (df["RSI_3_1d"] > 50.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 90.0))
      # 1h down move, 1h high, 4h overbought
      & ((df["RSI_3_1h"] > 45.0) | (df["AROONU_14_1h"] < 100.0) | (df["ROC_9_4h"] < 10.0))
      # 1h & 4h down move, 1h & 4h high
      & (
        (df["RSI_3_1h"] > 50.0)
        | (df["RSI_3_4h"] > 65.0)
        | (df["AROONU_14_1h"] < 85.0)
        | (df["AROONU_14_4h"] < 100.0)
      )
      # 1h down move, 15m & 1h high
      & ((df["RSI_3_1h"] > 50.0) | (df["AROONU_14_15m"] < 60.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 80.0))
      # 1h down move, 4h & 1d high
      & ((df["RSI_3_1h"] > 50.0) | (df["AROONU_14_4h"] < 90.0) | (df["AROONU_14_1d"] < 90.0))
      # 1h down move, 4h high, 1h overbought
      & ((df["RSI_3_1h"] > 55.0) | (df["AROONU_14_4h"] < 100.0) | (df["ROC_9_1h"] < 20.0))
      # 1h down move, 15m & 1h high, 1d downtrend
      & (
        (df["RSI_3_1h"] > 60.0)
        | (df["AROONU_14_15m"] < 65.0)
        | (df["STOCHRSIk_14_14_3_3_1h"] < 80.0)
        | (df["CMF_20_1d"] > -0.0)
      )
      # 1h down move, 1h high, 1d downtrend
      & ((df["RSI_3_1h"] > 60.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 90.0) | (df["ROC_9_1d"] > -20.0))
      # 4h down move, 15m high
      & ((df["RSI_3_4h"] > 3.0) | (df["AROONU_14_15m"] < 50.0))
      # 4h & 1d down move, 1d high
      & ((df["RSI_3_4h"] > 10.0) | (df["RSI_3_1d"] > 50.0) | (df["AROONU_14_1d"] < 90.0))
      # 4h down move, 15m still not low enough, 4h downtrend
      & ((df["RSI_3_4h"] > 10.0) | (df["AROONU_14_15m"] < 30.0) | (df["CMF_20_4h"] > -0.30))
      # 4h down move, 15m & 1h still not low enough
      & ((df["RSI_3_4h"] > 10.0) | (df["AROONU_14_15m"] < 30.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 25.0))
      # 4h down move, 4h still high
      & ((df["RSI_3_4h"] > 10.0) | (df["AROONU_14_4h"] < 40.0))
      # 4h down move, 1h still high, 4h downtrend
      & ((df["RSI_3_4h"] > 10.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 50.0) | (df["CMF_20_4h"] > -0.3))
      # 4h down move, 4h high
      & ((df["RSI_3_4h"] > 14.0) | (df["AROONU_14_4h"] < 60.0))
      # 4h down move, 1d high & overbought
      & ((df["RSI_3_4h"] > 15.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 90.0) | (df["ROC_9_1d"] < 20.0))
      # 4h down move, 15m still high, 1d overbought
      & ((df["RSI_3_4h"] > 20.0) | (df["AROONU_14_15m"] < 40.0) | (df["ROC_9_1d"] < 20.0))
      # 4h & 1d down move, 1h & 4h low
      & ((df["RSI_3_4h"] > 25.0) | (df["RSI_3_1d"] > 25.0) | (df["CMF_20_1h"] > -0.3) | (df["CMF_20_4h"] > -0.4))
      # 4h down move, 4h still high 1d downtrend
      & ((df["RSI_3_4h"] > 25.0) | (df["AROONU_14_4h"] < 50.0) | (df["ROC_9_1d"] > -20.0))
      # 4h down move, 1d high & overbought
      & ((df["RSI_3_4h"] > 25.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 80.0) | (df["ROC_9_1d"] < 25.0))
      # 4h down move, 4h & 1d high
      & ((df["RSI_3_4h"] > 35.0) | (df["AROONU_14_4h"] < 70.0) | (df["AROONU_14_1d"] < 100.0))
      # 4h down move, 15m still high, 1d overbought
      & ((df["RSI_3_4h"] > 40.0) | (df["AROONU_14_15m"] < 50.0) | (df["ROC_9_1d"] < 50.0))
      # 4h down move, 4h high, 1d overbought
      & ((df["RSI_3_4h"] > 40.0) | (df["AROONU_14_4h"] < 80.0) | (df["ROC_9_1d"] < 20.0))
      # 4h down move, 1h high, 1d downtrend
      & ((df["RSI_3_4h"] > 40.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 80.0) | (df["ROC_9_1d"] > -20.0))
      # 4h down move, 4h & 1d overbought
      & ((df["RSI_3_4h"] > 40.0) | (df["ROC_9_4h"] < 10.0) | (df["ROC_9_1d"] < 50.0))
      # 4h down move, 4h high, 1d overbought
      & ((df["RSI_3_4h"] > 45.0) | (df["AROONU_14_4h"] < 70.0) | (df["ROC_9_1d"] < 20.0))
      # 4h down move, 1d high, 4h overbought
      & ((df["RSI_3_4h"] > 45.0) | (df["AROONU_14_1d"] < 90.0) | (df["ROC_9_4h"] < 10.0))
      # 4h down move, 4h still high, 1d downtrend
      & ((df["RSI_3_4h"] > 50.0) | (df["RSI_14_4h"] < 40.0) | (df["ROC_9_1d"] > -30.0))
      # 4h down move, 4h high & overbought
      & ((df["RSI_3_4h"] > 50.0) | (df["AROONU_14_4h"] < 85.0) | (df["ROC_9_4h"] < 10.0))
      # 4h down move, 15m still high, 1d overbought
      & ((df["RSI_3_4h"] > 55.0) | (df["AROONU_14_15m"] < 40.0) | (df["ROC_9_1d"] < 100.0))
      # 4h & 1d down move, 4h high, 1d overbought
      & (
        (df["RSI_3_4h"] > 60.0) | (df["RSI_3_1d"] > 60.0) | (df["AROONU_14_4h"] < 75.0) | (df["ROC_9_1d"] < 40.0)
      )
      # 4h down move, 4h & 1d high
      & ((df["RSI_3_4h"] > 70.0) | (df["AROONU_14_4h"] < 90.0) | (df["AROONU_14_1d"] < 100.0))
      # 1d down move, 4h high
      & ((df["RSI_3_1d"] > 3.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 60.0))
      # 1d down move, 1h high
      & ((df["RSI_3_1d"] > 5.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 80.0))
      # 1d down move, 15m & 1h still high
      & ((df["RSI_3_1d"] > 10.0) | (df["RSI_14_15m"] < 40.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 50.0))
      # 1d down move, 1h & 4h high
      & ((df["RSI_3_1d"] > 10.0) | (df["AROONU_14_1h"] < 80.0) | (df["AROONU_14_4h"] < 90.0))
      # 1d down move, 1h & 4h still high
      & ((df["RSI_3_1d"] > 10.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 40.0) | (df["AROONU_14_4h"] < 40.0))
      # 1d down move, 1h high & overbought
      & ((df["RSI_3_1d"] > 20.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 80.0) | (df["ROC_9_1h"] < 20.0))
      # 1d down move, 1d high & overbought
      & ((df["RSI_3_1d"] > 40.0) | (df["AROONU_14_1d"] < 70.0) | (df["ROC_9_1d"] < 20.0))
      # 1d down move, 4h high & overbought
      & ((df["RSI_3_1d"] > 45.0) | (df["AROONU_14_4h"] < 80.0) | (df["ROC_9_4h"] < 30.0))
      # 1d down move, 1h high, 1d overbought
      & ((df["RSI_3_1d"] > 60.0) | (df["AROONU_14_1h"] < 80.0) | (df["ROC_9_1d"] < 80.0))
      # 1d down move, 15m still high, 1d overbought
      & ((df["RSI_3_1d"] > 65.0) | (df["AROONU_14_15m"] < 40.0) | (df["ROC_9_1d"] < 100.0))
      # 1d down move, 4h & 1d high
      & ((df["RSI_3_1d"] > 65.0) | (df["ROC_9_4h"] < 10.0) | (df["ROC_9_1d"] < 10.0))
      # 5m still high, 1h down move, 15m still high, 1h high
      & (
        (df["RSI_3"] < 40.0)
        | (df["RSI_3_1h"] > 30.0)
        | (df["AROONU_14_15m"] < 50.0)
        | (df["AROONU_14_4h"] < 90.0)
      )
      # 5m still high, 15m high
      & ((df["RSI_3"] < 45.0) | (df["AROONU_14_15m"] < 70.0))
      # 5m still high, 1h down move, 4h high
      & ((df["RSI_3"] < 50.0) | (df["RSI_3_1h"] > 30.0) | (df["AROONU_14_4h"] < 100.0))
      # 15m down move, 1h high
      & ((df["RSI_14_15m"] > 25.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 80.0))
      # 15m down move, 4h & 1d high
      & (
        (df["RSI_14_15m"] > 30.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 90.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 70.0)
      )
      # 1h downtrend, 4h high, 1d downtrend
      & ((df["CMF_20_1h"] > -0.2) | (df["STOCHRSIk_14_14_3_3_4h"] < 90.0) | (df["CMF_20_1d"] > -0.25))
      # 15m & 1h high, 1d overbought
      & ((df["AROONU_14_15m"] < 60.0) | (df["AROONU_14_1h"] < 100.0) | (df["ROC_9_1d"] < 20.0))
      # 4h high, 4h & 1d overbought
      & ((df["AROONU_14_4h"] < 80.0) | (df["ROC_9_4h"] < 20.0) | (df["ROC_9_1d"] < 20.0))
      # 4h & 1d high, 1d overbought
      & ((df["AROONU_14_4h"] < 85.0) | (df["AROONU_14_1d"] < 85.0) | (df["ROC_9_1d"] < 60.0))
      # 4h & 1d high, 1d overbought
      & ((df["AROONU_14_4h"] < 100.0) | (df["AROONU_14_1d"] < 100.0) | (df["ROC_9_1d"] < 30.0))
      # 1d still high, 4h & 1d downtrend
      & ((df["AROONU_14_1d"] < 50.0) | (df["ROC_9_4h"] > -20.0) | (df["ROC_9_1d"] > -30.0))
      # 4h top wick, 15m & 1h down move
      & ((df["top_wick_pct_4h"] < 10.0) | (df["RSI_3_15m"] > 15.0) | (df["RSI_3_1h"] > 40.0))
      # 4h top wick, 1h down move, 1h high
      & ((df["top_wick_pct_4h"] < 10.0) | (df["RSI_3_1h"] > 30.0) | (df["AROONU_14_1h"] < 70.0))
      # 1d red, 1h down move, 1h still high
      & ((df["change_pct_1d"] > -15.0) | (df["RSI_3_1h"] > 25.0) | (df["AROONU_14_1h"] < 50.0))
      # 1d P&D, 1h high
      & (
        (df["change_pct_1d"] > -15.0)
        | (df["change_pct_1d"].shift(288) < 15.0)
        | (df["STOCHRSIk_14_14_3_3_1h"] < 80.0)
      )
      # 1d P&D, 1d downtrend
      & ((df["change_pct_1d"] > -5.0) | (df["change_pct_1d"].shift(288) < 30.0) | (df["CMF_20_1d"] > -0.1))
      # 1d P&D, 15m high
      & ((df["change_pct_1d"] > -10.0) | (df["change_pct_1d"].shift(288) < 40.0) | (df["AROONU_14_15m"] < 50.0))
      # 1d P&D, 1h high
      & (
        (df["change_pct_1d"] > -10.0)
        | (df["change_pct_1d"].shift(288) < 40.0)
        | (df["STOCHRSIk_14_14_3_3_1h"] < 70.0)
      )
      # 1d red with top wick, 1h high
      & ((df["change_pct_1d"] > -10.0) | (df["top_wick_pct_1d"] < 10.0) | (df["AROONU_14_1h"] < 80.0))
      # 1d green, 4m down move, 4h high
      & ((df["change_pct_1d"] < 25.0) | (df["RSI_3_4h"] > 55.0) | (df["AROONU_14_4h"] < 50.0))
      # 1d green with top wick, 1d low
      & ((df["change_pct_1d"] < 25.0) | (df["top_wick_pct_1d"] < 10.0) | (df["CMF_20_1d"] > -0.2))
      # 1d top wick, 1h still high
      & ((df["top_wick_pct_1d"] < 25.0) | (df["AROONU_14_1h"] < 50.0))
      # 1d top wick, 4h still high
      & ((df["top_wick_pct_1d"] < 30.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 50.0))
      # 1d top wick, 1h down move
      & ((df["top_wick_pct_1d"] < 50.0) | (df["RSI_3_1h"] > 30.0))
      # big drop in the last 12 days, 1h down move, 1h high
      & ((df["close"] > (df["high_max_12_1d"] * 0.35)) | (df["RSI_3_1h"] > 35.0) | (df["AROONU_14_1h"] < 70.0))
      # big drop in the last 20 days, 1h down move, 1h high
      & (
        (df["close"] > (df["high_max_20_1d"] * 0.30))
        | (df["RSI_3_1h"] > 30.0)
        | (df["STOCHRSIk_14_14_3_3_1h"] < 75.0)
      )
      # big drop in the last 20 days, 1d high, 1d downtrend
      & (
        (df["close"] > (df["high_max_20_1d"] * 0.20))
        | (df["STOCHRSIk_14_14_3_3_1d"] < 70.0)
        | (df["ROC_9_1d"] > -15.0)
      )
    )

    # Logic
    long_entry_logic.append(
      (df["RSI_14"] < 30.0)
      & (df["AROONU_14"] < 25.0)
      & (df["AROOND_14"] > 75.0)
      & (df["STOCHRSIk_14_14_3_3"] < 20.0)
      & (df["EMA_9"] < (df["EMA_26"] * 0.982))
      & (df["close"] < df["SMA_9"])
    )

def append_long_101(df, long_entry_logic, allowed_empty_candles_288) -> None:
    """Append NFI long condition #101, the rapid-mode long entry."""
    # Protections
    long_entry_logic.append(df["num_empty_288"] <= allowed_empty_candles_288)
    long_entry_logic.append(df["protections_long_global"] == True)

    long_entry_logic.append(df["RSI_14_1h"] < 80.0)
    long_entry_logic.append(df["RSI_14_4h"] < 80.0)
    long_entry_logic.append(df["RSI_14_1d"] < 80.0)
    # big drop in the last hour
    long_entry_logic.append(df["close"] > (df["close_max_12"] * 0.50))
    # 5m & 4h down move, 1d downtrend
    long_entry_logic.append((df["RSI_3"] > 5.0) | (df["RSI_3_4h"] > 10.0) | (df["ROC_9_1d"] > -20.0))
    # 5m & 4h down move, 15m still high
    long_entry_logic.append(
      (df["RSI_3"] > 5.0) | (df["RSI_3_4h"] > 25.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 50.0)
    )
    # 5 & 15m down move, 1h high
    long_entry_logic.append(
      (df["RSI_3"] > 10.0) | (df["RSI_3_15m"] > 40.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 90.0)
    )
    # 5m down move, 1h & 4h high
    long_entry_logic.append((df["RSI_3"] > 10.0) | (df["AROONU_14_1h"] < 85.0) | (df["AROONU_14_4h"] < 90.0))
    # 15m & 1h down move, 4h still not low enough
    long_entry_logic.append(
      (df["RSI_3_15m"] > 3.0) | (df["RSI_3_1h"] > 5.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 30.0)
    )
    # 15m & 1h down move, 1d still high
    long_entry_logic.append((df["RSI_3_15m"] > 3.0) | (df["RSI_3_1h"] > 5.0) | (df["AROONU_14_1d"] < 40.0))
    # 15m & 1h down move, 4h still high
    long_entry_logic.append((df["RSI_3_15m"] > 3.0) | (df["RSI_3_1h"] > 15.0) | (df["RSI_14_4h"] < 40.0))
    # 15m & 4h down move, 4h high
    long_entry_logic.append((df["RSI_3_15m"] > 3.0) | (df["RSI_3_1h"] > 30.0) | (df["AROONU_14_4h"] < 75.0))
    # 15m & 1h down move, 1h still not low enough
    long_entry_logic.append(
      (df["RSI_3_15m"] > 3.0) | (df["RSI_3_1h"] > 35.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 30.0)
    )
    # 15m & 4h down move, 4h still not low enough
    long_entry_logic.append(
      (df["RSI_3_15m"] > 3.0) | (df["RSI_3_4h"] > 10.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 20.0)
    )
    # 15m & 4h down move, 1d downtrend
    long_entry_logic.append((df["RSI_3_15m"] > 3.0) | (df["RSI_3_4h"] > 10.0) | (df["ROC_9_1d"] > -20.0))
    # 15m & 4h down move, 4h still not low enough
    long_entry_logic.append((df["RSI_3_15m"] > 3.0) | (df["RSI_3_4h"] > 25.0) | (df["AROONU_14_4h"] < 30.0))
    # 15m & 4h down move, 4h still not low enough
    long_entry_logic.append(
      (df["RSI_3_15m"] > 3.0) | (df["RSI_3_4h"] > 25.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 30.0)
    )
    # 15m down move, 15m still not low enough, 1h high
    long_entry_logic.append(
      (df["RSI_3_15m"] > 3.0) | (df["AROONU_14_15m"] < 20.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 60.0)
    )
    # 15m down move, 15m still not low enough, 4h high
    long_entry_logic.append(
      (df["RSI_3_15m"] > 3.0) | (df["AROONU_14_15m"] < 30.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 70.0)
    )
    # 15m down move, 4h high, 1d overbought
    long_entry_logic.append((df["RSI_3_15m"] > 3.0) | (df["AROONU_14_4h"] < 70.0) | (df["ROC_9_1d"] < 30.0))
    # 15m & 1h & 1d down move
    long_entry_logic.append((df["RSI_3_15m"] > 5.0) | (df["RSI_3_1h"] > 10.0) | (df["RSI_3_1d"] > 20.0))
    # 15m down move, 1h still not low enough, 1d high
    long_entry_logic.append(
      (df["RSI_3_15m"] > 5.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 30.0) | (df["AROONU_14_1d"] < 90.0)
    )
    # 15m & 1h down move, 1h still not low enough
    long_entry_logic.append(
      (df["RSI_3_15m"] > 5.0) | (df["RSI_3_1h"] > 30.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 30.0)
    )
    # 15m & 1h down move, 4h high
    long_entry_logic.append(
      (df["RSI_3_15m"] > 5.0) | (df["RSI_3_1h"] > 30.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 80.0)
    )
    # 15m & 1h down move, 4h high
    long_entry_logic.append(
      (df["RSI_3_15m"] > 5.0) | (df["RSI_3_1h"] > 40.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 80.0)
    )
    # 15m & 1h down move, 1h high
    long_entry_logic.append(
      (df["RSI_3_15m"] > 5.0) | (df["RSI_3_1h"] > 50.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 70.0)
    )
    # 15m & 1h down move, 4h high
    long_entry_logic.append(
      (df["RSI_3_15m"] > 5.0) | (df["RSI_3_1h"] > 50.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 90.0)
    )
    # 15m & 4h down move, 1d still high
    long_entry_logic.append(
      (df["RSI_3_15m"] > 5.0) | (df["RSI_3_4h"] > 5.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 40.0)
    )
    # 15m & 4h down move, 4h still high
    long_entry_logic.append(
      (df["RSI_3_15m"] > 5.0) | (df["RSI_3_4h"] > 40.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 50.0)
    )
    # 15m & 1d down move
    long_entry_logic.append((df["RSI_3_15m"] > 5.0) | (df["RSI_3_1d"] > 5.0))
    # 15m & 1d down move, 4h still not low enough
    long_entry_logic.append(
      (df["RSI_3_15m"] > 5.0) | (df["RSI_3_1d"] > 30.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 30.0)
    )
    # 15m down move, 1h still high, 4h high
    long_entry_logic.append(
      (df["RSI_3_15m"] > 5.0) | (df["AROONU_14_1h"] < 50.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 90.0)
    )
    # 15m down move, 1h high & overbought
    long_entry_logic.append((df["RSI_3_15m"] > 5.0) | (df["AROONU_14_1h"] < 80.0) | (df["ROC_9_1h"] < 10.0))
    # 15m down move, 1h high & overbought
    long_entry_logic.append(
      (df["RSI_3_15m"] > 5.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 80.0) | (df["ROC_9_1h"] < 10.0)
    )
    # 15m & 1h down move, 4h still high
    long_entry_logic.append(
      (df["RSI_3_15m"] > 10.0) | (df["RSI_3_1h"] > 20.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 50.0)
    )
    # 15m & 1h down move, 1h still not low enough
    long_entry_logic.append((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1h"] > 25.0) | (df["AROONU_14_1h"] < 25.0))
    # 15m & 1h down move, 1h still high
    long_entry_logic.append(
      (df["RSI_3_15m"] > 10.0) | (df["RSI_3_1h"] > 30.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 40.0)
    )
    # 15m & 1h down move, 4h still high
    long_entry_logic.append(
      (df["RSI_3_15m"] > 10.0) | (df["RSI_3_1h"] > 30.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 50.0)
    )
    # 15m & 1h down move, 1h still high
    long_entry_logic.append(
      (df["RSI_3_15m"] > 10.0) | (df["RSI_3_1h"] > 35.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 50.0)
    )
    # 15m & 1h down move, 1h high
    long_entry_logic.append((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1h"] > 50.0) | (df["AROONU_14_1h"] < 80.0))
    # 15m & 1h down move, 1h high
    long_entry_logic.append(
      (df["RSI_3_15m"] > 10.0) | (df["RSI_3_1h"] > 50.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 80.0)
    )
    # 15m & 4h down move, 15m still not low enough
    long_entry_logic.append(
      (df["RSI_3_15m"] > 10.0) | (df["RSI_3_4h"] > 10.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 10.0)
    )
    # 15m & 4h down move, 1d downtrend
    long_entry_logic.append((df["RSI_3_15m"] > 10.0) | (df["RSI_3_4h"] > 20.0) | (df["ROC_9_1d"] > -25.0))
    # 15m & 4h down move, 1d high
    long_entry_logic.append((df["RSI_3_15m"] > 10.0) | (df["RSI_3_4h"] > 25.0) | (df["AROONU_14_1d"] < 85.0))
    # 15m & 4h down move, 1h still high
    long_entry_logic.append(
      (df["RSI_3_15m"] > 10.0) | (df["RSI_3_4h"] > 30.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 50.0)
    )
    # 15m & 4h down move, 4h high
    long_entry_logic.append(
      (df["RSI_3_15m"] > 10.0) | (df["RSI_3_4h"] > 30.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 70.0)
    )
    # 15m & 1d down move, 1h still high
    long_entry_logic.append(
      (df["RSI_3_15m"] > 10.0) | (df["RSI_3_1d"] > 25.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 50.0)
    )
    # 15m down move, 15m still not low enough, 1h still high
    long_entry_logic.append(
      (df["RSI_3_15m"] > 10.0) | (df["AROONU_14_15m"] < 30.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 50.0)
    )
    # 15m down move, 1h still high, 4h high
    long_entry_logic.append(
      (df["RSI_3_15m"] > 10.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 50.0) | (df["AROONU_14_4h"] < 85.0)
    )
    # 15m down move, 1h & 4h high
    long_entry_logic.append(
      (df["RSI_3_15m"] > 10.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 70.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 75.0)
    )
    # 15m & 1h down move, 15m still not low enough
    long_entry_logic.append(
      (df["RSI_3_15m"] > 15.0) | (df["RSI_3_1h"] > 15.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 30.0)
    )
    # 15m & 1h down move, 4h high
    long_entry_logic.append(
      (df["RSI_3_15m"] > 15.0) | (df["RSI_3_1h"] > 20.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 90.0)
    )
    # 15m & 1h down move, 1h still high
    long_entry_logic.append(
      (df["RSI_3_15m"] > 15.0) | (df["RSI_3_1h"] > 25.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 40.0)
    )
    # 15m & 1h down move, 1h still high
    long_entry_logic.append((df["RSI_3_15m"] > 15.0) | (df["RSI_3_1h"] > 40.0) | (df["AROONU_14_1h"] < 50.0))
    # 15m & 4h & 1d down move
    long_entry_logic.append((df["RSI_3_15m"] > 15.0) | (df["RSI_3_4h"] > 15.0) | (df["RSI_3_1d"] > 15.0))
    # 15m & 4h down move, 1h high
    long_entry_logic.append(
      (df["RSI_3_15m"] > 15.0) | (df["RSI_3_4h"] > 15.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 80.0)
    )
    # 15m & 4h down move, 1h still high
    long_entry_logic.append(
      (df["RSI_3_15m"] > 15.0) | (df["RSI_3_4h"] > 20.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 50.0)
    )
    # 15m & 4h down move, 15m still not low enough
    long_entry_logic.append((df["RSI_3_15m"] > 15.0) | (df["RSI_3_4h"] > 25.0) | (df["AROONU_14_15m"] < 30.0))
    # 15m & 4h down move, 4h still high
    long_entry_logic.append((df["RSI_3_15m"] > 15.0) | (df["RSI_3_4h"] > 50.0) | (df["AROONU_14_4h"] < 50.0))
    # 1h & 1d down move, 1d overbought
    long_entry_logic.append((df["RSI_3_1h"] > 15.0) | (df["RSI_3_1d"] > 35.0) | (df["ROC_9_1d"] < 10.0))
    # 15m down move, 15m still not low enough, 1h high
    long_entry_logic.append(
      (df["RSI_3_15m"] > 15.0) | (df["AROONU_14_15m"] < 25.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 80.0)
    )
    # 15m down move, 4h high & overbought
    long_entry_logic.append((df["RSI_3_15m"] > 15.0) | (df["AROONU_14_4h"] < 80.0) | (df["ROC_9_4h"] < 40.0))
    # 15m down move, 1h & 4h high
    long_entry_logic.append(
      (df["RSI_3_15m"] > 15.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 70.0) | (df["AROONU_14_4h"] < 85.0)
    )
    # 15m & 1h down move, 4h high
    long_entry_logic.append(
      (df["RSI_3_15m"] > 20.0) | (df["RSI_3_1h"] > 30.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 90.0)
    )
    # 15m & 1d down move, 1h high
    long_entry_logic.append(
      (df["RSI_3_15m"] > 20.0) | (df["RSI_3_1d"] > 20.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 70.0)
    )
    # 15m down move, 1d high & overbought
    long_entry_logic.append((df["RSI_3_15m"] > 20.0) | (df["AROONU_14_1d"] < 100.0) | (df["ROC_9_1d"] < 20.0))
    # 15m down move, 1h high, 1d downtrend
    long_entry_logic.append(
      (df["RSI_3_15m"] > 20.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 80.0) | (df["ROC_9_1d"] > -20.0)
    )
    # 15m down move, 1d high & overbought
    long_entry_logic.append(
      (df["RSI_3_15m"] > 20.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 80.0) | (df["ROC_9_1d"] < 20.0)
    )
    # 15m & 1h down move, 1h high
    long_entry_logic.append(
      (df["RSI_3_15m"] > 25.0) | (df["RSI_3_1h"] > 25.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 60.0)
    )
    # 15m & 1h down move, 1h high
    long_entry_logic.append((df["RSI_3_15m"] > 25.0) | (df["RSI_3_1h"] > 60.0) | (df["AROONU_14_1h"] < 85.0))
    # 15m down move, 15m still not low enough, 4h high
    long_entry_logic.append(
      (df["RSI_3_15m"] > 25.0) | (df["AROONU_14_15m"] < 25.0) | (df["AROONU_14_4h"] < 60.0)
    )
    # 15m down move, 15m still not low enough, 1h high
    long_entry_logic.append(
      (df["RSI_3_15m"] > 25.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 30.0) | (df["AROONU_14_1h"] < 80.0)
    )
    # 15m & 1h down move, 1h high
    long_entry_logic.append((df["RSI_3_15m"] > 30.0) | (df["RSI_3_1h"] > 45.0) | (df["AROONU_14_1h"] < 70.0))
    # 1h & 4h down move, 15m downtrend
    long_entry_logic.append((df["RSI_3_1h"] > 3.0) | (df["RSI_3_4h"] > 3.0) | (df["ROC_9_15m"] > -30.0))
    # 1h & 4h & 1d down move
    long_entry_logic.append((df["RSI_3_1h"] > 3.0) | (df["RSI_3_4h"] > 15.0) | (df["RSI_3_1d"] > 25.0))
    # 1h & 4h down move, 4h high
    long_entry_logic.append((df["RSI_3_1h"] > 3.0) | (df["RSI_3_4h"] > 50.0) | (df["AROONU_14_4h"] < 70.0))
    # 1h & 4h down move, 4h downtrend
    long_entry_logic.append((df["RSI_3_1h"] > 5.0) | (df["RSI_3_4h"] > 5.0) | (df["ROC_9_4h"] > -20.0))
    # 1h & 4h down move, 4h downtrend
    long_entry_logic.append((df["RSI_3_1h"] > 5.0) | (df["RSI_3_4h"] > 15.0) | (df["ROC_9_4h"] > -30.0))
    # 1h & 4h down move, 4h still not low enough
    long_entry_logic.append(
      (df["RSI_3_1h"] > 5.0) | (df["RSI_3_4h"] > 20.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 20.0)
    )
    # 1h & 4h down move, 1d low
    long_entry_logic.append((df["RSI_3_1h"] > 10.0) | (df["RSI_3_4h"] > 10.0) | (df["CMF_20_1d"] > -0.2))
    # 1h & 4h down move, 4h still not low enough
    long_entry_logic.append((df["RSI_3_1h"] > 10.0) | (df["RSI_3_4h"] > 15.0) | (df["AROONU_14_4h"] < 20.0))
    # 1h & 4h down move, 4h still not low enough
    long_entry_logic.append(
      (df["RSI_3_1h"] > 10.0) | (df["RSI_3_4h"] > 25.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 30.0)
    )
    # 1h & 1d down move, 5m moving down
    long_entry_logic.append((df["RSI_3_1h"] > 10.0) | (df["RSI_3_1d"] > 15.0) | (df["ROC_2"] > -0.0))
    # 1h down move, 4h downtrend
    long_entry_logic.append((df["RSI_3_1h"] > 10.0) | (df["ROC_9_4h"] > -30.0))
    # 1h down move, 1d downtrend
    long_entry_logic.append((df["RSI_3_1h"] > 10.0) | (df["ROC_9_1d"] > -30.0))
    # 1h & 4h & 1d down move
    long_entry_logic.append((df["RSI_3_1h"] > 15.0) | (df["RSI_3_4h"] > 20.0) | (df["RSI_3_1d"] > 30.0))
    # 1h & 4h down move, 1h still high
    long_entry_logic.append(
      (df["RSI_3_1h"] > 15.0) | (df["RSI_3_4h"] > 30.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 40.0)
    )
    # 1h & 4h down move, 1h still not low enough
    long_entry_logic.append(
      (df["RSI_3_1h"] > 15.0) | (df["RSI_3_4h"] > 40.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 30.0)
    )
    # 1h & 4h down move, 1h still high
    long_entry_logic.append((df["RSI_3_1h"] > 15.0) | (df["RSI_3_1d"] > 10.0) | (df["AROONU_14_1h"] < 40.0))
    # 1h down move, 1d high & overbought
    long_entry_logic.append((df["RSI_3_1h"] > 20.0) | (df["AROONU_14_1d"] < 90.0) | (df["ROC_9_1d"] < 30.0))
    # 1h down move, 1h still not low enough, 4h high
    long_entry_logic.append(
      (df["RSI_3_1h"] > 20.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 20.0) | (df["AROONU_14_4h"] < 80.0)
    )
    # 1h & 4h down move, 1h still high
    long_entry_logic.append(
      (df["RSI_3_1h"] > 25.0) | (df["RSI_3_4h"] > 25.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 50.0)
    )
    # 1h & 4h down move, 1d high
    long_entry_logic.append(
      (df["RSI_3_1h"] > 25.0) | (df["RSI_3_4h"] > 30.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 80.0)
    )
    # 1h & 4h down move, 1h high
    long_entry_logic.append(
      (df["RSI_3_1h"] > 25.0) | (df["RSI_3_4h"] > 60.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 80.0)
    )
    # 1h & 4h down move, 1h still high
    long_entry_logic.append(
      (df["RSI_3_1h"] > 30.0) | (df["RSI_3_4h"] > 40.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 50.0)
    )
    # 1h down move, 4h high, 1d overbought
    long_entry_logic.append((df["RSI_3_1h"] > 30.0) | (df["AROONU_14_4h"] < 90.0) | (df["ROC_9_1d"] < 40.0))
    # 1h down move, 4h & 1d high
    long_entry_logic.append((df["RSI_3_1h"] > 30.0) | (df["AROONU_14_4h"] < 80.0) | (df["AROONU_14_1d"] < 100.0))
    # 1h down move, 15m high
    long_entry_logic.append((df["RSI_3_1h"] > 35.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 80.0))
    # 1h down move, 1h high, 1d overbought
    long_entry_logic.append((df["RSI_3_1h"] > 35.0) | (df["AROONU_14_1h"] < 70.0) | (df["ROC_9_1d"] < 20.0))
    # 1h down move, 1h & 4h high
    long_entry_logic.append((df["RSI_3_1h"] > 40.0) | (df["AROONU_14_1h"] < 80.0) | (df["AROONU_14_4h"] < 100.0))
    # 1h down move, 1h high & overbought
    long_entry_logic.append(
      (df["RSI_3_1h"] > 55.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 80.0) | (df["ROC_9_1h"] < 10.0)
    )
    # 1h down move, 4h high
    long_entry_logic.append((df["RSI_3_1h"] > 60.0) | (df["AROONU_14_4h"] < 90.0))
    # 4h down move, 15m still high
    long_entry_logic.append((df["RSI_3_4h"] > 5.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 40.0))
    # 4h down move, 1d still high, 1d downtrend
    long_entry_logic.append((df["RSI_3_4h"] > 10.0) | (df["AROONU_14_1d"] < 40.0) | (df["ROC_9_1d"] > -20.0))
    # 4h down move, 15m 4h still high
    long_entry_logic.append(
      (df["RSI_3_4h"] > 10.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 40.0) | (df["AROONU_14_4h"] < 50.0)
    )
    # 4h & 1d down move, 4h high
    long_entry_logic.append((df["RSI_3_4h"] > 15.0) | (df["RSI_3_1d"] > 25.0) | (df["AROONU_14_4h"] < 70.0))
    # 4h down move, 1h still high
    long_entry_logic.append((df["RSI_3_4h"] > 15.0) | (df["AROONU_14_1h"] < 50.0))
    # 4h down move, 4h still high
    long_entry_logic.append((df["RSI_3_4h"] > 15.0) | (df["AROONU_14_4h"] < 50.0))
    # 4h down move, 1d high & overbought
    long_entry_logic.append(
      (df["RSI_3_4h"] > 15.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 90.0) | (df["ROC_9_1d"] < 20.0)
    )
    # 4h down move, 4h & 1d downtrend
    long_entry_logic.append((df["RSI_3_4h"] > 15.0) | (df["ROC_9_4h"] > -10.0) | (df["ROC_9_1d"] > -15.0))
    # 4h down move, 4h & 1d downtrend
    long_entry_logic.append((df["RSI_3_4h"] > 20.0) | (df["ROC_9_4h"] > -20.0) | (df["ROC_9_1d"] > -30.0))
    # 4h dowqn move, 4h still high, 1d downtrend
    long_entry_logic.append(
      (df["RSI_3_4h"] > 25.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 50.0) | (df["ROC_9_1d"] > -30.0)
    )
    # 4h down move, 4h & 1d high
    long_entry_logic.append((df["RSI_3_4h"] > 35.0) | (df["AROONU_14_4h"] < 80.0) | (df["AROONU_14_1d"] < 100.0))
    # 4h & 1d down move, 4h still high
    long_entry_logic.append(
      (df["RSI_3_4h"] > 40.0) | (df["RSI_3_1d"] > 10.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 50.0)
    )
    # 4h down move, 4h high, 1d downtrend
    long_entry_logic.append(
      (df["RSI_3_4h"] > 40.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 70.0) | (df["ROC_9_1d"] > -60.0)
    )
    # 4h down move, 4h still high
    long_entry_logic.append((df["RSI_3_4h"] > 60.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 40.0))
    # 4h down move, 4h overbought
    long_entry_logic.append((df["RSI_3_4h"] > 60.0) | (df["ROC_9_4h"] < 20.0))
    # 1d down move, 1h still high, 4h high
    long_entry_logic.append((df["RSI_3_1d"] > 20.0) | (df["AROONU_14_1h"] < 50.0) | (df["AROONU_14_4h"] < 85.0))
    # 1d down move, 1h high & overbought
    long_entry_logic.append(
      (df["RSI_3_1d"] > 35.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 90.0) | (df["ROC_9_1h"] < 10.0)
    )
    # 1d down move, 4h high, 1d overbought
    long_entry_logic.append(
      (df["RSI_3_1d"] > 45.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 90.0) | (df["ROC_9_1d"] < 10.0)
    )
    # 4h still high, 4h moving lower, 4h overbought
    long_entry_logic.append(
      (df["AROONU_14_4h"] < 50.0) | (df["AROONU_14_4h"] > df["AROONU_14_4h"].shift(48)) | (df["ROC_9_4h"] < 40.0)
    )
    # 1h high, 1d downtrend
    long_entry_logic.append((df["AROONU_14_1d"] < 70.0) | (df["ROC_9_1d"] > -30.0))
    # 1d high, 4h & 1d overbought
    long_entry_logic.append((df["AROONU_14_1d"] < 85.0) | (df["ROC_9_4h"] < 60.0) | (df["ROC_9_1d"] < 60.0))
    # 1d high, 4h & 1d overbought
    long_entry_logic.append((df["AROONU_14_1d"] < 100.0) | (df["ROC_9_4h"] < 10.0) | (df["ROC_9_1d"] < 20.0))
    # 1h high, 4h downtrend
    long_entry_logic.append((df["STOCHRSIk_14_14_3_3_1h"] < 80.0) | (df["ROC_9_4h"] > -20.0))
    # 1h high, 4h overbought
    long_entry_logic.append((df["STOCHRSIk_14_14_3_3_1h"] < 80.0) | (df["ROC_9_4h"] < 80.0))
    # 4h high, 4h & 1d overbought
    long_entry_logic.append(
      (df["STOCHRSIk_14_14_3_3_4h"] < 80.0) | (df["ROC_9_4h"] < 30.0) | (df["ROC_9_1d"] < 30.0)
    )
    # 1d high, 4h & 1d overbought
    long_entry_logic.append(
      (df["STOCHRSIk_14_14_3_3_1d"] < 80.0) | (df["ROC_9_4h"] < 60.0) | (df["ROC_9_1d"] < 60.0)
    )
    # 1d red, 4h down move, 1h still high
    long_entry_logic.append(
      (df["change_pct_1d"] > -30.0) | (df["RSI_3_4h"] > 30.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 50.0)
    )
    # pump, drop but not yet near the previous lows
    long_entry_logic.append(
      (((df["high_max_24_4h"] - df["low_min_24_4h"]) / df["low_min_24_4h"]) < 2.0)
      | (df["close"] > (df["high_max_6_4h"] * 0.75))
      | (df["close"] < (df["low_min_24_4h"] * 1.25))
    )
    # 4h high, drop but not yet near the previous lows
    long_entry_logic.append(
      (df["AROONU_14_4h"] < 70.0)
      | (df["close"] > (df["high_max_6_4h"] * 0.80))
      | (df["close"] < (df["low_min_24_4h"] * 1.25))
    )
    # 4h high, drop but not yet near the previous lows
    long_entry_logic.append(
      (df["AROONU_14_4h"] < 80.0)
      | (df["close"] > (df["high_max_6_4h"] * 0.85))
      | (df["close"] < (df["low_min_24_4h"] * 1.25))
    )
    # 1h down move, drop but not yet near the previous lows
    long_entry_logic.append(
      (df["RSI_3_1h"] > 30.0)
      | (df["close"] > (df["high_max_12_4h"] * 0.50))
      | (df["close"] < (df["low_min_24_4h"] * 1.25))
    )
    # 1d overbought, drop but not yet near the previous lows
    long_entry_logic.append(
      (df["ROC_9_1d"] < 50.0)
      | (df["close"] > (df["high_max_6_1d"] * 0.70))
      | (df["close"] < (df["low_min_12_1d"] * 1.25))
    )
    # big drop in last 6 hours, 1d overbought
    long_entry_logic.append((df["close"] > (df["high_max_6_1h"] * 0.65)) | (df["ROC_9_1d"] < 50.0))
    # big drop in last 4 hours, 4h still not low enough
    long_entry_logic.append(
      (df["close"] > (df["high_max_24_4h"] * 0.50)) | (df["STOCHRSIk_14_14_3_3_4h"] < 30.0)
    )
    # big drop in the last 4 days, 4h down move
    long_entry_logic.append((df["close"] > (df["high_max_24_4h"] * 0.20)) | (df["RSI_3_4h"] > 20.0))
    # big drop in the last 6 days, 1d down move
    long_entry_logic.append((df["close"] > (df["high_max_6_1d"] * 0.30)) | (df["RSI_3_1d"] > 15.0))
    # big drop in the last 12 days, 4h high
    long_entry_logic.append(
      (df["close"] > (df["high_max_12_1d"] * 0.50)) | (df["STOCHRSIk_14_14_3_3_4h"] < 90.0)
    )
    # big drop in the last 30 days, 4h down move
    long_entry_logic.append((df["close"] > (df["high_max_20_1d"] * 0.10)) | (df["RSI_3_4h"] > 30.0))
    # big drop in the last 20 days, 1h still high
    long_entry_logic.append((df["close"] > (df["high_max_20_1d"] * 0.05)) | (df["AROONU_14_1h"] < 50.0))
    # big drop in the last 20 days, 1d high, 1d downtrend
    long_entry_logic.append(
      (df["close"] > (df["high_max_20_1d"] * 0.20))
      | (df["STOCHRSIk_14_14_3_3_1d"] < 70.0)
      | (df["ROC_9_1d"] > -15.0)
    )
    # big drop in the last 30 days, 1h down move
    long_entry_logic.append((df["close"] > (df["high_max_30_1d"] * 0.25)) | (df["RSI_3_1h"] > 15.0))

    # Logic
    long_entry_logic.append(df["RSI_3"] > 3.0)
    long_entry_logic.append(df["RSI_14"] < 36.0)
    long_entry_logic.append(df["AROONU_14"] < 25.0)
    long_entry_logic.append(df["STOCHRSIk_14_14_3_3"] < 20.0)
    long_entry_logic.append(df["close"] < (df["SMA_16"] * 0.946))
    long_entry_logic.append(df["AROONU_14_15m"] < 50.0)


def append_long_102(df, long_entry_logic, allowed_empty_candles_288) -> None:
    """Append NFI long condition #102, the rapid-mode long entry."""
    # Protections
    long_entry_logic.append(df["num_empty_288"] <= allowed_empty_candles_288)
    long_entry_logic.append(df["protections_long_global"] == True)

    long_entry_logic.append(df["RSI_3"] < 46.0)
    long_entry_logic.append(df["RSI_3_15m"] > 5.0)
    long_entry_logic.append(df["RSI_3_1h"] > 10.0)
    long_entry_logic.append(df["RSI_3_4h"] > 10.0)
    # 5m & 15m down move, 4h still high
    long_entry_logic.append(
      (df["RSI_3"] > 3.0) | (df["RSI_3_15m"] > 15.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 50.0)
    )
    # 5m & 15m down move, 15m still high
    long_entry_logic.append((df["RSI_3"] > 3.0) | (df["RSI_3_15m"] > 20.0) | (df["AROONU_14_15m"] < 40.0))
    # 5m & 15m down move, 1h still high
    long_entry_logic.append(
      (df["RSI_3"] > 3.0) | (df["RSI_3_15m"] > 25.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 40.0)
    )
    # 5m & 1h down move, 4h still high
    long_entry_logic.append((df["RSI_3"] > 3.0) | (df["RSI_3_1h"] > 25.0) | (df["AROONU_14_4h"] < 50.0))
    # 5m & 4h & 1d down move
    long_entry_logic.append((df["RSI_3"] > 3.0) | (df["RSI_3_4h"] > 20.0) | (df["RSI_3_1d"] > 20.0))
    # 5m & 1d down move, 15m still high
    long_entry_logic.append(
      (df["RSI_3"] > 3.0) | (df["RSI_3_1d"] > 10.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 40.0)
    )
    # 5m down move, 15m high
    long_entry_logic.append((df["RSI_3"] > 3.0) | (df["AROONU_14_15m"] < 70.0))
    # 5m down move, 15m & 1h still high
    long_entry_logic.append(
      (df["RSI_3"] > 3.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 40.0) | (df["AROONU_14_1h"] < 40.0)
    )
    # 5m down move, 1h high
    long_entry_logic.append(
      (df["RSI_3"] > 3.0) | (df["AROONU_14_1h"] < 70.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 50.0)
    )
    # 5m & 1h down move, 1h high
    long_entry_logic.append(
      (df["RSI_3"] > 5.0) | (df["RSI_3_1h"] > 40.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 60.0)
    )
    # 5m & 4h down move, 4h high
    long_entry_logic.append((df["RSI_3"] > 5.0) | (df["RSI_3_4h"] > 50.0) | (df["AROONU_14_4h"] < 70.0))
    # 5m down move, 15m still high, 1h high
    long_entry_logic.append((df["RSI_3"] > 5.0) | (df["RSI_14_15m"] < 40.0) | (df["AROONU_14_1h"] < 80.0))
    # 5m down move, 15m still high, 1h high
    long_entry_logic.append(
      (df["RSI_3"] > 5.0) | (df["AROONU_14_15m"] < 40.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 50.0)
    )
    # 5m down move, 15m & 4h high
    long_entry_logic.append(
      (df["RSI_3"] > 5.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 70.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 90.0)
    )
    # 5m & 15m down move, 4h high
    long_entry_logic.append((df["RSI_3"] > 10.0) | (df["RSI_3_15m"] > 20.0) | (df["AROONU_14_4h"] < 90.0))
    # 5m & 15m down move, 1d high
    long_entry_logic.append(
      (df["RSI_3"] > 10.0) | (df["RSI_3_15m"] > 20.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 80.0)
    )
    # 5m & 15m down move, 1h high
    long_entry_logic.append(
      (df["RSI_3"] > 10.0) | (df["RSI_3_15m"] > 25.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 90.0)
    )
    # 5m & 1h down move, 4h still high
    long_entry_logic.append(
      (df["RSI_3"] > 10.0) | (df["RSI_3_1h"] > 30.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 50.0)
    )
    # 5m down move, 1h & 4h high
    long_entry_logic.append((df["RSI_3"] > 10.0) | (df["AROONU_14_1h"] < 85.0) | (df["AROONU_14_4h"] < 90.0))
    # 5m down move, 4h high, 1d high
    long_entry_logic.append(
      (df["RSI_3"] > 10.0) | (df["AROONU_14_4h"] < 60.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 90.0)
    )
    # 5m down move, 15m still high, 1h high
    long_entry_logic.append(
      (df["RSI_3"] > 15.0) | (df["RSI_14_15m"] < 40.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 90.0)
    )
    # 5m down move, 15m still high, 4h high
    long_entry_logic.append(
      (df["RSI_3"] > 15.0) | (df["RSI_14_15m"] < 40.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 90.0)
    )
    # 15m down move, 15m still not low enough, 1h high
    long_entry_logic.append(
      (df["RSI_3_15m"] > 3.0) | (df["AROONU_14_15m"] < 20.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 60.0)
    )
    # 15m & 1h down move, 1d high
    long_entry_logic.append((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1h"] > 20.0) | (df["AROONU_14_1d"] < 70.0))
    # 15m & 1h down move, 1h still not low enough
    long_entry_logic.append(
      (df["RSI_3_15m"] > 10.0) | (df["RSI_3_1h"] > 20.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 20.0)
    )
    # 15m & 1h down move, 1h still not low enough
    long_entry_logic.append((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1h"] > 25.0) | (df["AROONU_14_1h"] < 30.0))
    # 15m & 1h down move, 1h still high
    long_entry_logic.append((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1h"] > 35.0) | (df["AROONU_14_1h"] < 50.0))
    # 15m & 1h down move, 1h still high
    long_entry_logic.append(
      (df["RSI_3_15m"] > 10.0) | (df["RSI_3_1h"] > 35.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 50.0)
    )
    # 15m & 1h down move, 4h still high
    long_entry_logic.append((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1h"] > 35.0) | (df["AROONU_14_4h"] < 70.0))
    # 15m & 4h down move, 4h still not low enough
    long_entry_logic.append((df["RSI_3_15m"] > 10.0) | (df["RSI_3_4h"] > 15.0) | (df["AROONU_14_4h"] < 30.0))
    # 15m& 4h down move, 15m still high
    long_entry_logic.append(
      (df["RSI_3_15m"] > 10.0) | (df["RSI_3_4h"] > 15.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 40.0)
    )
    # 15m & 4h down move, 15m still high
    long_entry_logic.append((df["RSI_3_15m"] > 10.0) | (df["RSI_3_4h"] > 20.0) | (df["AROONU_14_15m"] < 50.0))
    # 15m & 4h down move, 4h still not low enough
    long_entry_logic.append(
      (df["RSI_3_15m"] > 10.0) | (df["RSI_3_4h"] > 20.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 30.0)
    )
    # 15m & 4h down move, 4h still high
    long_entry_logic.append((df["RSI_3_15m"] > 10.0) | (df["RSI_3_4h"] > 25.0) | (df["AROONU_14_4h"] < 50.0))
    # 15m & 4h down move, 4h still high
    long_entry_logic.append(
      (df["RSI_3_15m"] > 10.0) | (df["RSI_3_4h"] > 30.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 40.0)
    )
    # 15m & 4h down move, 1h still high
    long_entry_logic.append(
      (df["RSI_3_15m"] > 10.0) | (df["RSI_3_4h"] > 20.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 40.0)
    )
    # 15m & 4h down move, 1d high
    long_entry_logic.append((df["RSI_3_15m"] > 10.0) | (df["RSI_3_4h"] > 25.0) | (df["AROONU_14_1d"] < 85.0))
    # 15m & 4h down move, 1h still high
    long_entry_logic.append(
      (df["RSI_3_15m"] > 10.0) | (df["RSI_3_4h"] > 30.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 50.0)
    )
    # 15m & 4h down move, 4h high
    long_entry_logic.append((df["RSI_3_15m"] > 10.0) | (df["RSI_3_4h"] > 30.0) | (df["AROONU_14_4h"] < 70.0))
    # 15m & 1d down move, 1h still high
    long_entry_logic.append(
      (df["RSI_3_15m"] > 10.0) | (df["RSI_3_1d"] > 25.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 50.0)
    )
    # 15m down move, 15m still not low enough, 1h high
    long_entry_logic.append(
      (df["RSI_3_15m"] > 10.0) | (df["AROONU_14_15m"] < 30.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 80.0)
    )
    # 15m down move, 1h high, 4h overbought
    long_entry_logic.append((df["RSI_3_15m"] > 10.0) | (df["AROONU_14_1h"] < 70.0) | (df["ROC_9_4h"] < 50.0))
    # 15m down move, 1d high & overbought
    long_entry_logic.append((df["RSI_3_15m"] > 10.0) | (df["AROONU_14_1d"] < 80.0) | (df["ROC_9_1d"] < 20.0))
    # 15m & 1h down move, 1h still high
    long_entry_logic.append((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1h"] > 30.0) | (df["AROONU_14_1h"] < 40.0))
    # 15m & 1h down move, 1h still high
    long_entry_logic.append((df["RSI_3_15m"] > 15.0) | (df["RSI_3_1h"] > 40.0) | (df["AROONU_14_1h"] < 50.0))
    # 15m & 1h down move, 1h still high
    long_entry_logic.append(
      (df["RSI_3_15m"] > 15.0) | (df["RSI_3_1h"] > 45.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 50.0)
    )
    # 15m & 1h down move, 4h high
    long_entry_logic.append((df["RSI_3_15m"] > 15.0) | (df["RSI_3_1h"] > 45.0) | (df["AROONU_14_4h"] < 80.0))
    # 15m & 1h down move, 15m still not low enough
    long_entry_logic.append(
      (df["RSI_3_15m"] > 15.0) | (df["RSI_3_1h"] > 45.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 50.0)
    )
    # 15m & 4h & 1d down move
    long_entry_logic.append((df["RSI_3_15m"] > 15.0) | (df["RSI_3_4h"] > 15.0) | (df["RSI_3_1d"] > 15.0))
    # 15m & 4h down move, 4h still high
    long_entry_logic.append((df["RSI_3_15m"] > 15.0) | (df["RSI_3_4h"] > 20.0) | (df["AROONU_14_4h"] < 50.0))
    # 15m & 4h down move, 15m still not low enough
    long_entry_logic.append(
      (df["RSI_3_15m"] > 15.0) | (df["RSI_3_4h"] > 30.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 25.0)
    )
    # 15m & 4h down move, 4h high
    long_entry_logic.append((df["RSI_3_15m"] > 15.0) | (df["RSI_3_4h"] > 35.0) | (df["AROONU_14_4h"] < 60.0))
    # 15m & 4h down move, 4h high
    long_entry_logic.append(
      (df["RSI_3_15m"] > 15.0) | (df["RSI_3_4h"] > 35.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 70.0)
    )
    # 15m & 4h down move, 4h still high
    long_entry_logic.append(
      (df["RSI_3_15m"] > 15.0) | (df["RSI_3_4h"] > 45.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 50.0)
    )
    # 15m down move, 15m still not low enough, 4h high
    long_entry_logic.append(
      (df["RSI_3_15m"] > 15.0) | (df["RSI_14_15m"] < 35.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 90.0)
    )
    # 15m down move, 15m still not low enough, 4h high
    long_entry_logic.append(
      (df["RSI_3_15m"] > 15.0) | (df["AROONU_14_15m"] < 30.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 90.0)
    )
    # 15m down move, 15m & 4h still high
    long_entry_logic.append(
      (df["RSI_3_15m"] > 15.0) | (df["AROONU_14_15m"] < 50.0) | (df["AROONU_14_4h"] < 50.0)
    )
    # 15m down move, 15m still high, 1h high
    long_entry_logic.append(
      (df["RSI_3_15m"] > 15.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 40.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 70.0)
    )
    # 15m down move, 1h still high, 4h high
    long_entry_logic.append(
      (df["RSI_3_15m"] > 15.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 50.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 60.0)
    )
    # 15m down move, 4h still high 1d overbought
    long_entry_logic.append((df["RSI_3_15m"] > 15.0) | (df["AROONU_14_4h"] < 50.0) | (df["ROC_9_1d"] < 50.0))
    # 15m & 1h down move, 15m still not low enough
    long_entry_logic.append((df["RSI_3_15m"] > 20.0) | (df["RSI_3_1h"] > 20.0) | (df["AROONU_14_15m"] < 30.0))
    # 15m & 1h down move, 4h high
    long_entry_logic.append(
      (df["RSI_3_15m"] > 20.0) | (df["RSI_3_1h"] > 30.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 90.0)
    )
    # 15m & 1h down move, 15m high
    long_entry_logic.append((df["RSI_3_15m"] > 20.0) | (df["RSI_3_1h"] > 40.0) | (df["AROONU_14_15m"] < 60.0))
    # 15m & 4h down move, 1h high
    long_entry_logic.append(
      (df["RSI_3_15m"] > 20.0) | (df["RSI_3_4h"] > 20.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 60.0)
    )
    # 15m & 4h down move, 4h high
    long_entry_logic.append((df["RSI_3_15m"] > 20.0) | (df["RSI_3_4h"] > 60.0) | (df["AROONU_14_4h"] < 80.0))
    # 15m & 1d down move, 4h high
    long_entry_logic.append(
      (df["RSI_3_15m"] > 20.0) | (df["RSI_3_1d"] > 20.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 90.0)
    )
    # 15m down move, 15m still not low enough, 4h high
    long_entry_logic.append((df["RSI_3_15m"] > 20.0) | (df["RSI_14_15m"] < 35.0) | (df["RSI_14_4h"] < 85.0))
    # 15m down move, 15m still not low enough, 1h high
    long_entry_logic.append(
      (df["RSI_3_15m"] > 20.0) | (df["AROONU_14_15m"] < 30.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 80.0)
    )
    # 15m down move, 15m still not low enough, 4h high
    long_entry_logic.append(
      (df["RSI_3_15m"] > 20.0) | (df["AROONU_14_15m"] < 30.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 70.0)
    )
    # 15m down move, 15m still high, 4d downtrend
    long_entry_logic.append((df["RSI_3_15m"] > 20.0) | (df["AROONU_14_15m"] < 40.0) | (df["ROC_9_4h"] > -20.0))
    # 15m down move, 15m still not low enough, 1h still high
    long_entry_logic.append(
      (df["RSI_3_15m"] > 20.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 30.0) | (df["AROONU_14_1h"] < 50.0)
    )
    # 15m down move, 15m & 1h still high
    long_entry_logic.append(
      (df["RSI_3_15m"] > 20.0) | (df["AROONU_14_15m"] < 50.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 40.0)
    )
    # 15m down move, 1h & 4h high
    long_entry_logic.append((df["RSI_3_15m"] > 20.0) | (df["AROONU_14_1h"] < 70.0) | (df["AROONU_14_4h"] < 90.0))
    # 15m & 1h down move, 1h high
    long_entry_logic.append((df["RSI_3_15m"] > 25.0) | (df["RSI_3_1h"] > 25.0) | (df["AROONU_14_1h"] < 80.0))
    # 15m & 1h down move, 4h high
    long_entry_logic.append(
      (df["RSI_3_15m"] > 25.0) | (df["RSI_3_1h"] > 35.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 80.0)
    )
    # 15m & 1h down move, 1d high
    long_entry_logic.append(
      (df["RSI_3_15m"] > 25.0) | (df["RSI_3_1h"] > 40.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 90.0)
    )
    # 15m & 1h down move, 1h high
    long_entry_logic.append((df["RSI_3_15m"] > 25.0) | (df["RSI_3_1h"] > 60.0) | (df["AROONU_14_1h"] < 85.0))
    # 15m & 4h down move, 15m still high
    long_entry_logic.append((df["RSI_3_15m"] > 25.0) | (df["RSI_3_4h"] > 40.0) | (df["AROONU_14_15m"] < 50.0))
    # 15m & 1d down move, 4h high
    long_entry_logic.append(
      (df["RSI_3_15m"] > 25.0) | (df["RSI_3_1d"] > 25.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 70.0)
    )
    # 15m & 1d down move, 1h high
    long_entry_logic.append(
      (df["RSI_3_15m"] > 25.0) | (df["RSI_3_1d"] > 30.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 80.0)
    )
    # 15m down move, 15m & 1h still high
    long_entry_logic.append(
      (df["RSI_3_15m"] > 25.0) | (df["AROONU_14_15m"] < 50.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 50.0)
    )
    # 15m down move, 15m still high, 4h high
    long_entry_logic.append(
      (df["RSI_3_15m"] > 25.0) | (df["AROONU_14_15m"] < 50.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 70.0)
    )
    # 15m down move, 15m high, 1d overbought
    long_entry_logic.append((df["RSI_3_15m"] > 25.0) | (df["AROONU_14_15m"] < 70.0) | (df["ROC_9_1d"] < 100.0))
    # 15m down move, 15m high
    long_entry_logic.append((df["RSI_3_15m"] > 25.0) | (df["AROONU_14_15m"] < 85.0))
    # 15m down move, 1h & 4h high
    long_entry_logic.append((df["RSI_3_15m"] > 25.0) | (df["AROONU_14_1h"] < 80.0) | (df["AROONU_14_4h"] < 90.0))
    # 15m down move, 1h & 4h high
    long_entry_logic.append(
      (df["RSI_3_15m"] > 25.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 70.0) | (df["AROONU_14_4h"] < 90.0)
    )
    # 15m down move, 4h high, 1d overbought
    long_entry_logic.append((df["RSI_3_15m"] > 25.0) | (df["AROONU_14_4h"] < 80.0) | (df["ROC_9_1d"] < 50.0))
    # 15m & 1h down move, 1h high
    long_entry_logic.append((df["RSI_3_15m"] > 30.0) | (df["RSI_3_1h"] > 45.0) | (df["AROONU_14_1h"] < 70.0))
    # 15m down move, 15m high, 4h still high
    long_entry_logic.append(
      (df["RSI_3_15m"] > 30.0) | (df["AROONU_14_15m"] < 70.0) | (df["AROONU_14_4h"] < 50.0)
    )
    # 15m down move, 15m still not low enough, 1h high
    long_entry_logic.append(
      (df["RSI_3_15m"] > 30.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 30.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 80.0)
    )
    # 15m down move, 1h still high, 4h high
    long_entry_logic.append((df["RSI_3_15m"] > 30.0) | (df["AROONU_14_1h"] < 50.0) | (df["AROONU_14_4h"] < 90.0))
    # 15m down move, 15m & 1h high
    long_entry_logic.append(
      (df["RSI_3_15m"] > 35.0) | (df["AROONU_14_15m"] < 70.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 70.0)
    )
    # 15m down move, 15m & 4h high
    long_entry_logic.append(
      (df["RSI_3_15m"] > 35.0) | (df["AROONU_14_15m"] < 70.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 90.0)
    )
    # 15m down move, 4h still high, 4h overbought
    long_entry_logic.append(
      (df["RSI_3_15m"] > 35.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 50.0) | (df["ROC_9_4h"] < 20.0)
    )
    # 15m down move, 15m still high, 1h high
    long_entry_logic.append((df["RSI_3_15m"] > 40.0) | (df["RSI_14_15m"] < 50.0) | (df["AROONU_14_1h"] < 80.0))
    # 15m down move, 15m high, 1h high
    long_entry_logic.append(
      (df["RSI_3_15m"] > 40.0) | (df["AROONU_14_15m"] < 70.0) | (df["AROONU_14_1h"] < 90.0)
    )
    # 15m down move, 15m high
    long_entry_logic.append((df["RSI_3_15m"] > 45.0) | (df["AROONU_14_15m"] < 90.0))
    # 1h & 4h down move, 4h still high
    long_entry_logic.append((df["RSI_3_1h"] > 15.0) | (df["RSI_3_4h"] > 20.0) | (df["RSI_14_4h"] < 40.0))
    # 1h & 4h down move, 1h still high
    long_entry_logic.append(
      (df["RSI_3_1h"] > 15.0) | (df["RSI_3_4h"] > 30.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 50.0)
    )
    # 1h & 4h down move, 4h still high
    long_entry_logic.append((df["RSI_3_1h"] > 15.0) | (df["RSI_3_4h"] > 30.0) | (df["AROONU_14_4h"] < 40.0))
    # 1h & 1d down move, 4h downtrend
    long_entry_logic.append((df["RSI_3_1h"] > 15.0) | (df["RSI_3_1d"] > 35.0) | (df["CMF_20_4h"] > -0.40))
    # 1h down move, 1d high & overbought
    long_entry_logic.append(
      (df["RSI_3_1h"] > 20.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 90.0) | (df["ROC_9_1d"] < 30.0)
    )
    # 1h & 4h down move, 4h still high
    long_entry_logic.append(
      (df["RSI_3_1h"] > 25.0) | (df["RSI_3_4h"] > 25.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 50.0)
    )
    # 1h & 4h down move, 4h high
    long_entry_logic.append((df["RSI_3_1h"] > 25.0) | (df["RSI_3_4h"] > 40.0) | (df["AROONU_14_4h"] < 70.0))
    # 1h down move, 1h still not low enough, 4h high
    long_entry_logic.append(
      (df["RSI_3_1h"] > 25.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 30.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 70.0)
    )
    # 1h down move, 1d still high, 1d downtrend
    long_entry_logic.append(
      (df["RSI_3_1h"] > 25.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 50.0) | (df["ROC_9_1d"] > -20.0)
    )
    # 1h down move, 4h high & overbought
    long_entry_logic.append((df["RSI_3_1h"] > 30.0) | (df["AROONU_14_4h"] < 70.0) | (df["ROC_9_4h"] < 10.0))
    # 1h down move, 4h high, 1d downtrend
    long_entry_logic.append((df["RSI_3_1h"] > 30.0) | (df["AROONU_14_4h"] < 70.0) | (df["ROC_9_1d"] > -50.0))
    # 1h down move, 4h high, 1d overbought
    long_entry_logic.append((df["RSI_3_1h"] > 30.0) | (df["AROONU_14_4h"] < 70.0) | (df["ROC_9_1d"] < 40.0))
    # 1h down move, 4h & 1d overbought
    long_entry_logic.append((df["RSI_3_1h"] > 30.0) | (df["ROC_9_4h"] < 10.0) | (df["ROC_9_1d"] < 40.0))
    # 1h & 4h down move, 4h high
    long_entry_logic.append(
      (df["RSI_3_1h"] > 35.0) | (df["RSI_3_4h"] > 55.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 80.0)
    )
    # 1h down move, 1h high, 1d overbought
    long_entry_logic.append((df["RSI_3_1h"] > 35.0) | (df["AROONU_14_1h"] < 70.0) | (df["ROC_9_1d"] < 20.0))
    # 1h down move, 4h high, 1d overbought
    long_entry_logic.append((df["RSI_3_1h"] > 40.0) | (df["RSI_14_4h"] < 75.0) | (df["ROC_9_1d"] < 100.0))
    # 1h down move, 1h still high, 1d high
    long_entry_logic.append((df["RSI_3_1h"] > 40.0) | (df["AROONU_14_1h"] < 50.0) | (df["AROONU_14_1d"] < 85.0))
    # 1h down move, 1h still high, 1d overbought
    long_entry_logic.append((df["RSI_3_1h"] > 40.0) | (df["AROONU_14_1h"] < 50.0) | (df["ROC_9_1d"] < 20.0))
    # 1h down move 1h high & overbought
    long_entry_logic.append((df["RSI_3_1h"] > 45.0) | (df["AROONU_14_1h"] < 90.0) | (df["ROC_9_1h"] < 10.0))
    # 1h down move, 1h high & overbought
    long_entry_logic.append(
      (df["RSI_3_1h"] > 55.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 80.0) | (df["ROC_9_1h"] < 10.0)
    )
    # 1h down move, 1d high, 1h overbought
    long_entry_logic.append((df["RSI_3_1h"] > 60.0) | (df["AROONU_14_1d"] < 90.0) | (df["ROC_9_1h"] < 10.0))
    # 4h down move, 4h still not low enough, 1d overbought
    long_entry_logic.append((df["RSI_3_4h"] > 15.0) | (df["AROONU_14_4h"] < 30.0) | (df["ROC_9_1d"] < 100.0))
    # 4h down move, 15m still high, 1d downtrend
    long_entry_logic.append(
      (df["RSI_3_4h"] > 15.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 50.0) | (df["ROC_9_1d"] > -20.0)
    )
    # 4h & 1d down move, 15m still not low enough
    long_entry_logic.append(
      (df["RSI_3_4h"] > 20.0) | (df["RSI_3_1d"] > 20.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 30.0)
    )
    # 4h down move, 4h still not low enough, 1d downtrend
    long_entry_logic.append(
      (df["RSI_3_4h"] > 20.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 30.0) | (df["ROC_9_1d"] > -20.0)
    )
    # 4h down move, 1d high, 4h downtrend
    long_entry_logic.append(
      (df["RSI_3_4h"] > 30.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 90.0) | (df["ROC_9_4h"] > -20.0)
    )
    # 4h down move, 4h high, 1d downtrend
    long_entry_logic.append(
      (df["RSI_3_4h"] > 35.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 70.0) | (df["ROC_9_1d"] > -30.0)
    )
    # 4h & 1d down move, 1d high
    long_entry_logic.append((df["RSI_3_4h"] > 40.0) | (df["RSI_3_1d"] > 60.0) | (df["AROONU_14_1d"] < 100.0))
    # 4h down move, 4h high, 1d downtrend
    long_entry_logic.append(
      (df["RSI_3_4h"] > 60.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 80.0) | (df["ROC_9_1d"] > -20.0)
    )
    # 4h down move, 15m high, 4h overbought
    long_entry_logic.append(
      (df["RSI_3_4h"] > 60.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 80.0) | (df["ROC_9_4h"] < 20.0)
    )
    # 4h down move, 4h & 1d overbought
    long_entry_logic.append((df["RSI_3_4h"] > 60.0) | (df["ROC_9_4h"] < 20.0) | (df["ROC_9_1d"] < 20.0))
    # 1d down move, 1h high, 1d downtrend
    long_entry_logic.append((df["RSI_3_1d"] > 10.0) | (df["AROONU_14_1h"] < 85.0) | (df["ROC_9_1d"] > -30.0))
    # 1d down move, 15m still not low enough, 1h still high
    long_entry_logic.append(
      (df["RSI_3_1d"] > 15.0) | (df["AROONU_14_15m"] < 30.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 50.0)
    )
    # 15m still not low enough, 1h high, 1d overbought
    long_entry_logic.append(
      (df["AROONU_14_15m"] < 30.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 80.0) | (df["ROC_9_1d"] < 100.0)
    )
    # 15m still high, 4h high & overbought
    long_entry_logic.append(
      (df["AROONU_14_15m"] < 40.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 80.0) | (df["ROC_9_4h"] < 30.0)
    )
    # 15m & 1h & 4h high
    long_entry_logic.append(
      (df["AROONU_14_15m"] < 70.0) | (df["AROONU_14_1h"] < 80.0) | (df["AROONU_14_4h"] < 90.0)
    )
    # 15m & 1h high, 4h overbought
    long_entry_logic.append((df["AROONU_14_15m"] < 70.0) | (df["AROONU_14_1h"] < 90.0) | (df["ROC_9_4h"] < 20.0))
    # 15m & 1d high, 1d overbought
    long_entry_logic.append(
      (df["AROONU_14_15m"] < 70.0) | (df["AROONU_14_1d"] < 90.0) | (df["ROC_9_1d"] < 100.0)
    )
    # 15m high
    long_entry_logic.append((df["AROONU_14_15m"] < 80.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 60.0))
    # 15m & 4h high
    long_entry_logic.append((df["AROONU_14_15m"] < 80.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 70.0))
    # 15m high, 1d overbought
    long_entry_logic.append((df["AROONU_14_15m"] < 80.0) | (df["ROC_9_1d"] < 50.0))
    # 15m & 4h high
    long_entry_logic.append((df["AROONU_14_15m"] < 90.0) | (df["AROONU_14_4h"] < 70.0))
    # 15m & 1h high
    long_entry_logic.append((df["AROONU_14_15m"] < 90.0) | (df["AROONU_14_1h"] < 90.0))
    # 1h still high, 4h high & overbought
    long_entry_logic.append((df["AROONU_14_1h"] < 50.0) | (df["AROONU_14_4h"] < 90.0) | (df["ROC_9_4h"] < 80.0))
    # 1h & 4h high, 1h overbought
    long_entry_logic.append((df["AROONU_14_1h"] < 80.0) | (df["AROONU_14_4h"] < 100.0) | (df["ROC_9_1h"] < 40.0))
    # 1h & 1d high, 1d overbought
    long_entry_logic.append((df["AROONU_14_1h"] < 80.0) | (df["AROONU_14_1d"] < 100.0) | (df["ROC_9_1d"] < 30.0))
    # 1h high, 4h & 1d overbought
    long_entry_logic.append((df["AROONU_14_1h"] < 90.0) | (df["ROC_9_4h"] < 20.0) | (df["ROC_9_1d"] < 40.0))
    # 4h & 1d high, 4h overbought
    long_entry_logic.append((df["AROONU_14_4h"] < 80.0) | (df["AROONU_14_1d"] < 100.0) | (df["ROC_9_4h"] < 30.0))
    # 4h & 1d high, 1d overbought
    long_entry_logic.append((df["AROONU_14_4h"] < 70.0) | (df["AROONU_14_1d"] < 100.0) | (df["ROC_9_1d"] < 10.0))
    # 4h high & overbought
    long_entry_logic.append(
      (df["AROONU_14_4h"] < 90.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 85.0) | (df["ROC_9_4h"] < 50.0)
    )
    # 1d high, 4h & 1d overbought
    long_entry_logic.append((df["AROONU_14_1d"] < 100.0) | (df["ROC_9_4h"] < 10.0) | (df["ROC_9_1d"] < 50.0))
    # 1d high, 4h & 1d overbought
    long_entry_logic.append((df["AROONU_14_1d"] < 100.0) | (df["ROC_9_4h"] < 20.0) | (df["ROC_9_1d"] < 40.0))
    # 4h high, 4h & 1d overbought
    long_entry_logic.append(
      (df["STOCHRSIk_14_14_3_3_4h"] < 70.0) | (df["ROC_9_4h"] < 30.0) | (df["ROC_9_1d"] < 30.0)
    )
    # 5m red, 1h still high
    long_entry_logic.append((df["change_pct"] > -5.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 50.0))
    # 1d top wick, 4h down move, 4h still high
    long_entry_logic.append(
      (df["top_wick_pct_1d"] < 30.0) | (df["RSI_3_4h"] > 60.0) | (df["AROONU_14_4h"] < 50.0)
    )
    # pump, drop but not yet near the previous lows
    long_entry_logic.append(
      (((df["high_max_24_4h"] - df["low_min_24_4h"]) / df["low_min_24_4h"]) < 2.0)
      | (df["close"] > (df["high_max_6_4h"] * 0.75))
      | (df["close"] < (df["low_min_24_4h"] * 1.25))
    )
    # 4h high, drop but not yet near the previous lows
    long_entry_logic.append(
      (df["STOCHRSIk_14_14_3_3_4h"] < 90.0)
      | (df["close"] > (df["close_max_48"] * 0.85))
      | (df["close"] < (df["low_min_24_1h"] * 1.25))
    )
    # 4h high, drop but not yet near the previous lows
    long_entry_logic.append(
      (df["AROONU_14_4h"] < 70.0)
      | (df["close"] > (df["high_max_6_4h"] * 0.80))
      | (df["close"] < (df["low_min_24_4h"] * 1.25))
    )
    # 1d overbought, drop but not yet near the previous lows
    long_entry_logic.append(
      (df["ROC_9_1d"] < 50.0)
      | (df["close"] > (df["high_max_6_1d"] * 0.70))
      | (df["close"] < (df["low_min_12_1d"] * 1.25))
    )
    # big drop in the last 4 days, 4h down move
    long_entry_logic.append((df["close"] > (df["high_max_24_4h"] * 0.20)) | (df["RSI_3_4h"] > 20.0))
    # big drop in the last 12 days, 1h high
    long_entry_logic.append(
      (df["close"] > (df["high_max_12_1d"] * 0.30)) | (df["STOCHRSIk_14_14_3_3_1h"] < 90.0)
    )
    # big drop in the last 20 days, 1d down move
    long_entry_logic.append((df["close"] > (df["high_max_20_1d"] * 0.40)) | (df["RSI_3_1d"] > 30.0))
    # big drop in the last 30 days, 4h down move, 4h still high
    long_entry_logic.append(
      (df["close"] > (df["high_max_30_1d"] * 0.25)) | (df["RSI_3_4h"] > 45.0) | (df["RSI_14_4h"] < 40.0)
    )
    # big drop in the last 30 days, 1h high
    long_entry_logic.append(
      (df["close"] > (df["high_max_30_1d"] * 0.20)) | (df["STOCHRSIk_14_14_3_3_1h"] < 80.0)
    )

    # Logic
    long_entry_logic.append(df["WILLR_14"] < -95.0)
    long_entry_logic.append(df["STOCHRSIk_14_14_3_3"] < 10.0)
    long_entry_logic.append(df["close"] < (df["BBL_20_2.0"] * 0.999))
    long_entry_logic.append(df["close"] < (df["EMA_20"] * 0.960))


def append_long_103(df, long_entry_logic, allowed_empty_candles_288) -> None:
    """Append NFI long condition #103, the rapid-mode long entry."""
    # Protections
    long_entry_logic.append(df["num_empty_288"] <= allowed_empty_candles_288)
    long_entry_logic.append(df["protections_long_global"] == True)

    long_entry_logic.append(df["ROC_2"] > -0.0)
    # 15m down move, 4h high, 1d overbought
    long_entry_logic.append(
      (df["RSI_3_15m"] > 10.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 70.0) | (df["ROC_9_1d"] < 80.0)
    )
    # 15m & 1h & 4h down move
    long_entry_logic.append((df["RSI_3_15m"] > 20.0) | (df["RSI_3_1h"] > 10.0) | (df["RSI_3_4h"] > 20.0))
    # 15m & 4h down move, 1h still high
    long_entry_logic.append(
      (df["RSI_3_15m"] > 10.0) | (df["RSI_3_4h"] > 20.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 50.0)
    )
    # 15m & 1h down move, 1h high
    long_entry_logic.append((df["RSI_3_15m"] > 15.0) | (df["RSI_3_1h"] > 40.0) | (df["AROONU_14_1h"] < 70.0))
    # 15m down move, 4h high & overbought
    long_entry_logic.append(
      (df["RSI_3_15m"] > 15.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 70.0) | (df["ROC_9_4h"] < 30.0)
    )
    # 15m & 1h down move, 15m high
    long_entry_logic.append((df["RSI_3_15m"] > 20.0) | (df["RSI_3_1h"] > 45.0) | (df["AROONU_14_15m"] < 70.0))
    # 15m & 4h down move, 15m still high
    long_entry_logic.append(
      (df["RSI_3_15m"] > 20.0) | (df["RSI_3_4h"] > 20.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 50.0)
    )
    # 15m down move, 15m still high, 1h high
    long_entry_logic.append(
      (df["RSI_3_15m"] > 20.0) | (df["RSI_14_15m"] < 40.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 70.0)
    )
    # 15m down move, 15m still high, 4h high
    long_entry_logic.append((df["RSI_3_15m"] > 20.0) | (df["RSI_14_15m"] < 40.0) | (df["AROONU_14_4h"] < 90.0))
    # 15m down move, 15m still high, 4h high
    long_entry_logic.append(
      (df["RSI_3_15m"] > 20.0) | (df["AROONU_14_15m"] < 50.0) | (df["AROONU_14_4h"] < 90.0)
    )
    # 15m down move, 15m & 1h high
    long_entry_logic.append(
      (df["RSI_3_15m"] > 20.0) | (df["AROONU_14_15m"] < 60.0) | (df["AROONU_14_1h"] < 70.0)
    )
    # 15m down move, 15m high, 4h still high
    long_entry_logic.append(
      (df["RSI_3_15m"] > 20.0) | (df["AROONU_14_15m"] < 70.0) | (df["AROONU_14_4h"] < 50.0)
    )
    # 15m down move, 15m & 1h still high
    long_entry_logic.append(
      (df["RSI_3_15m"] > 20.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 50.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 50.0)
    )
    # 15m down move, 4h overbought
    long_entry_logic.append((df["RSI_3_15m"] > 20.0) | (df["ROC_9_4h"] < 70.0))
    # 15m down move, 15m still high, 1h high
    long_entry_logic.append(
      (df["RSI_3_15m"] > 25.0) | (df["AROONU_14_15m"] < 50.0) | (df["AROONU_14_1h"] < 80.0)
    )
    # 15m down move, 4h & 1d high
    long_entry_logic.append(
      (df["RSI_3_15m"] > 25.0) | (df["AROONU_14_4h"] < 90.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 90.0)
    )
    # 15m down move, 1h & 1d high
    long_entry_logic.append(
      (df["RSI_3_15m"] > 25.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 80.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 90.0)
    )
    # 15m down move, 1h high & overbought
    long_entry_logic.append(
      (df["RSI_3_15m"] > 25.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 80.0) | (df["ROC_9_1h"] < 20.0)
    )
    # 15m & 1h down move, 15m high
    long_entry_logic.append((df["RSI_3_15m"] > 30.0) | (df["RSI_3_1h"] > 30.0) | (df["AROONU_14_15m"] < 70.0))
    # 15m down move, 15m & 1h high
    long_entry_logic.append(
      (df["RSI_3_15m"] > 30.0) | (df["AROONU_14_15m"] < 70.0) | (df["AROONU_14_1h"] < 90.0)
    )
    # 15m down move, 1h & 4h high
    long_entry_logic.append(
      (df["RSI_3_15m"] > 30.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 70.0) | (df["AROONU_14_4h"] < 90.0)
    )
    # 15m & 1h down move, 1h high
    long_entry_logic.append(
      (df["RSI_3_15m"] > 35.0) | (df["RSI_3_1h"] > 45.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 80.0)
    )
    # 15m down move, 15m still high, 4h high
    long_entry_logic.append(
      (df["RSI_3_15m"] > 35.0) | (df["AROONU_14_15m"] < 50.0) | (df["AROONU_14_4h"] < 80.0)
    )
    # 15m down move, 15m & 1h high
    long_entry_logic.append(
      (df["RSI_3_15m"] > 35.0) | (df["AROONU_14_15m"] < 70.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 80.0)
    )
    # 15m down move, 1h high, 4h overbought
    long_entry_logic.append((df["RSI_3_15m"] > 35.0) | (df["AROONU_14_1h"] < 85.0) | (df["ROC_9_4h"] < 80.0))
    # 1h & 4h down move, 1h still high
    long_entry_logic.append((df["RSI_3_1h"] > 10.0) | (df["RSI_3_4h"] > 20.0) | (df["AROONU_14_1h"] < 40.0))
    # 1h & 4h down move, 15m still not low enough
    long_entry_logic.append(
      (df["RSI_3_1h"] > 10.0) | (df["RSI_3_4h"] > 20.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 20.0)
    )
    # 1h down move, 1d high & overbought
    long_entry_logic.append((df["RSI_3_1h"] > 10.0) | (df["AROONU_14_1d"] < 90.0) | (df["ROC_9_1d"] < 10.0))
    # 1h & 4h down move, 4h still high
    long_entry_logic.append((df["RSI_3_1h"] > 15.0) | (df["RSI_3_4h"] > 20.0) | (df["AROONU_14_4h"] < 40.0))
    # 1h down move, 4h still high, 4h downtrend
    long_entry_logic.append((df["RSI_3_1h"] > 15.0) | (df["AROONU_14_4h"] < 50.0) | (df["ROC_9_4h"] > -20.0))
    # 1h down move, 15m still not low enough, 4h high
    long_entry_logic.append((df["RSI_3_1h"] > 20.0) | (df["AROONU_14_15m"] < 25.0) | (df["AROONU_14_4h"] < 80.0))
    # 1h down move, 4h & 1d high
    long_entry_logic.append(
      (df["RSI_3_1h"] > 30.0) | (df["AROONU_14_4h"] < 70.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 80.0)
    )
    # 1h down move, 4h high & overbought
    long_entry_logic.append((df["RSI_3_1h"] > 30.0) | (df["AROONU_14_4h"] < 70.0) | (df["ROC_9_4h"] < 10.0))
    # 1h down move, 4h high, 1d overbought
    long_entry_logic.append((df["RSI_3_1h"] > 30.0) | (df["AROONU_14_4h"] < 70.0) | (df["ROC_9_1d"] < 40.0))
    # 1h down move, 4h & 1d overbought
    long_entry_logic.append((df["RSI_3_1h"] > 30.0) | (df["ROC_9_4h"] < 10.0) | (df["ROC_9_1d"] < 40.0))
    # 1h down move, 4h & 1d overbought
    long_entry_logic.append((df["RSI_3_1h"] > 30.0) | (df["ROC_9_4h"] < 30.0) | (df["ROC_9_1d"] < 40.0))
    # 1h down move, 15m & 1h still high
    long_entry_logic.append(
      (df["RSI_3_1h"] > 40.0) | (df["AROONU_14_15m"] < 50.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 50.0)
    )
    # 1h down move, 1h still high, 4h high
    long_entry_logic.append((df["RSI_3_1h"] > 40.0) | (df["AROONU_14_1h"] < 50.0) | (df["AROONU_14_4h"] < 90.0))
    # 1h down move, 1d high & overbought
    long_entry_logic.append((df["RSI_3_1h"] > 45.0) | (df["AROONU_14_1d"] < 100.0) | (df["ROC_9_1d"] < 30.0))
    # 1h down move, 15m & 1h still high
    long_entry_logic.append((df["RSI_3_1h"] > 50.0) | (df["AROONU_14_15m"] < 50.0) | (df["AROONU_14_1h"] < 85.0))
    # 1h & 4h down move, 4h high
    long_entry_logic.append((df["RSI_3_1h"] > 60.0) | (df["RSI_3_4h"] > 60.0) | (df["AROONU_14_4h"] < 80.0))
    # 1h & 4h down move, 4h high
    long_entry_logic.append(
      (df["RSI_3_1h"] > 60.0) | (df["RSI_3_4h"] > 60.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 80.0)
    )
    # 4h down move, 1h & 4h downtrend
    long_entry_logic.append((df["RSI_3_4h"] > 5.0) | (df["ROC_9_1h"] > -30.0) | (df["ROC_9_4h"] > -30.0))
    # 1h down move, 4h high & overbought
    long_entry_logic.append(
      (df["RSI_3_1h"] > 50.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 90.0) | (df["ROC_9_4h"] < 20.0)
    )
    # 4h down move, 4h still high, 1d downtrend
    long_entry_logic.append((df["RSI_3_4h"] > 20.0) | (df["AROONU_14_4h"] < 50.0) | (df["ROC_9_1d"] > -40.0))
    # 1h down move, 15m & 1h still high
    long_entry_logic.append(
      (df["RSI_3_4h"] > 20.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 40.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 50.0)
    )
    # 4h down move, 15m still high, 4h high
    long_entry_logic.append(
      (df["RSI_3_4h"] > 25.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 50.0) | (df["AROONU_14_4h"] < 70.0)
    )
    # 4h down move, 15m still not low enough, 4h high
    long_entry_logic.append((df["RSI_3_4h"] > 35.0) | (df["AROONU_14_15m"] < 30.0) | (df["AROONU_14_4h"] < 70.0))
    # 4h down move, 1h high, 4h downtrend
    long_entry_logic.append((df["RSI_3_4h"] > 30.0) | (df["AROONU_14_1h"] < 70.0) | (df["ROC_9_4h"] > -10.0))
    # 4h down move, 4h still high, 1d downtrend
    long_entry_logic.append((df["RSI_3_4h"] > 50.0) | (df["RSI_14_4h"] < 40.0) | (df["ROC_9_1d"] > -30.0))
    # 4h down move, 4h high & overbought
    long_entry_logic.append((df["RSI_3_4h"] > 50.0) | (df["AROONU_14_4h"] < 80.0) | (df["ROC_9_4h"] < 20.0))
    # 4h down move, 4h still high, 1d downtrend
    long_entry_logic.append(
      (df["RSI_3_4h"] > 50.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 50.0) | (df["ROC_9_1d"] > -30.0)
    )
    # 4h down move, 15m still high, 1h high
    long_entry_logic.append((df["RSI_3_4h"] > 60.0) | (df["AROONU_14_15m"] < 50.0) | (df["AROONU_14_1h"] < 90.0))
    # 4h down move, 1h high, 1d overbought
    long_entry_logic.append(
      (df["RSI_3_4h"] > 60.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 90.0) | (df["ROC_9_1d"] < 30.0)
    )
    # 1d down move, 1h high, 1d downtrend
    long_entry_logic.append((df["RSI_3_1d"] > 10.0) | (df["AROONU_14_1h"] < 80.0) | (df["ROC_9_1d"] > -10.0))
    # 1d down move, 4h high
    long_entry_logic.append((df["RSI_3_1d"] > 10.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 80.0))
    # 1d down move, 15m still high, 1h high
    long_entry_logic.append((df["RSI_3_1d"] > 15.0) | (df["AROONU_14_15m"] < 50.0) | (df["AROONU_14_1h"] < 85.0))
    # 1d down move, 1h & 1d overbought
    long_entry_logic.append((df["RSI_3_1d"] > 45.0) | (df["ROC_9_1h"] < 80.0) | (df["ROC_9_1d"] < 80.0))
    # 15m still high, 1h & 4h high
    long_entry_logic.append(
      (df["RSI_14_15m"] < 40.0) | (df["AROONU_14_1h"] < 80.0) | (df["AROONU_14_4h"] < 90.0)
    )
    # 15m & 1h still high, 4h high
    long_entry_logic.append(
      (df["RSI_14_15m"] < 45.0) | (df["AROONU_14_1h"] < 40.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 70.0)
    )
    # 15m still high, 4h high & overbought
    long_entry_logic.append((df["RSI_14_15m"] < 50.0) | (df["AROONU_14_4h"] < 90.0) | (df["ROC_9_4h"] < 80.0))
    # 15m still high, 1h high, 4h still high
    long_entry_logic.append(
      (df["AROONU_14_15m"] < 50.0) | (df["AROONU_14_1h"] < 90.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 50.0)
    )
    # 15m still high, 1d high
    long_entry_logic.append((df["AROONU_14_15m"] < 50.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 90.0))
    # 15m & 1h
    long_entry_logic.append((df["AROONU_14_15m"] < 70.0) | (df["AROONU_14_1h"] < 90.0))
    # 15m & 1h & 4h high
    long_entry_logic.append(
      (df["AROONU_14_15m"] < 70.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 70.0) | (df["AROONU_14_4h"] < 90.0)
    )
    # 1h & 1d high, 4h downtrend
    long_entry_logic.append((df["AROONU_14_1h"] < 40.0) | (df["AROONU_14_1d"] < 70.0) | (df["ROC_9_4h"] > -20.0))
    # 1h & 4h high, 4h overbought
    long_entry_logic.append((df["AROONU_14_1h"] < 70.0) | (df["AROONU_14_4h"] < 90.0) | (df["ROC_9_4h"] < 10.0))
    # 1h high, 1h & 1d overbought
    long_entry_logic.append((df["AROONU_14_1h"] < 90.0) | (df["ROC_9_1h"] < 10.0) | (df["ROC_9_1d"] < 30.0))
    # 4h & 1d high, 1d overbought
    long_entry_logic.append((df["AROONU_14_4h"] < 70.0) | (df["AROONU_14_1d"] < 100.0) | (df["ROC_9_1d"] < 10.0))
    # 4h high, 4h & 1d overbought
    long_entry_logic.append((df["AROONU_14_4h"] < 80.0) | (df["ROC_9_4h"] < 80.0) | (df["ROC_9_1d"] < 100.0))
    # 1d high, 4h & 1d overbought
    long_entry_logic.append((df["AROONU_14_1d"] < 100.0) | (df["ROC_9_4h"] < 10.0) | (df["ROC_9_1d"] < 50.0))
    # 15m still high, 1h high
    long_entry_logic.append(
      (df["STOCHRSIk_14_14_3_3_15m"] < 40.0)
      | (df["AROONU_14_1h"] < 90.0)
      | (df["STOCHRSIk_14_14_3_3_1h"] < 90.0)
    )
    # 15m still high, 1d high
    long_entry_logic.append((df["STOCHRSIk_14_14_3_3_15m"] < 50.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 90.0))
    # 4h high, 4h & 1d overbought
    long_entry_logic.append(
      (df["STOCHRSIk_14_14_3_3_4h"] < 80.0) | (df["ROC_9_4h"] < 40.0) | (df["ROC_9_1d"] < 100.0)
    )
    # 1d green, 4h down move, 4h still high
    long_entry_logic.append((df["change_pct_1d"] < 40.0) | (df["RSI_3_4h"] > 35.0) | (df["AROONU_14_4h"] < 40.0))
    # 1d top wick, 4h high
    long_entry_logic.append((df["top_wick_pct_1d"] < 30.0) | (df["AROONU_14_4h"] < 90.0))
    # pump, 4h overbought
    long_entry_logic.append(
      (((df["high_max_6_1h"] - df["low_min_6_1h"]) / df["low_min_6_1h"]) < 0.5) | (df["ROC_9_4h"] < 50.0)
    )
    # pump, drop but not yet near the previous lows
    long_entry_logic.append(
      (((df["high_max_24_4h"] - df["low_min_24_4h"]) / df["low_min_24_4h"]) < 2.0)
      | (df["close"] > (df["high_max_6_4h"] * 0.85))
      | (df["close"] < (df["low_min_24_4h"] * 1.25))
    )
    # pump, 1h high
    long_entry_logic.append(
      (((df["high_max_24_4h"] - df["low_min_24_4h"]) / df["low_min_24_4h"]) < 4.0)
      | (df["STOCHRSIk_14_14_3_3_1h"] < 90.0)
    )
    # big drop in the last 2 days, 1d down move
    long_entry_logic.append((df["close"] > (df["high_max_12_4h"] * 0.30)) | (df["RSI_3_1d"] > 30.0))
    # big drop in the last 12 days, 1h still high
    long_entry_logic.append((df["close"] > (df["high_max_12_1d"] * 0.25)) | (df["AROONU_14_1h"] < 50.0))
    # big drop in the last 12 days, 1h still not low enough
    long_entry_logic.append(
      (df["close"] > (df["high_max_12_1d"] * 0.10)) | (df["STOCHRSIk_14_14_3_3_1h"] < 30.0)
    )
    # big drop in the last 12 days, 15m still high
    long_entry_logic.append((df["close"] > (df["high_max_12_1d"] * 0.20)) | (df["AROONU_14_15m"] < 50.0))
    # big drop in the last 20 days, 4h down move
    long_entry_logic.append((df["close"] > (df["high_max_20_1d"] * 0.10)) | (df["RSI_3_4h"] > 20.0))

    # Logic
    long_entry_logic.append(df["RSI_4"] < 45.0)
    long_entry_logic.append(df["RSI_14"] > 35.0)
    long_entry_logic.append(df["RSI_20"] < df["RSI_20"].shift(1))
    long_entry_logic.append(df["AROONU_14"] < 25.0)
    long_entry_logic.append(df["close"] < df["SMA_16"] * 0.960)


def append_long_104(df, long_entry_logic, allowed_empty_candles_288) -> None:
    """Append NFI long condition #104, the rapid-mode long entry."""
    # Protections
    long_entry_logic.append(df["num_empty_288"] <= allowed_empty_candles_288)
    long_entry_logic.append(df["protections_long_global"] == True)

    # 5m & 4h & 1d down move
    long_entry_logic.append((df["RSI_3"] > 3.0) | (df["RSI_3_4h"] > 20.0) | (df["RSI_3_1d"] > 20.0))
    # 5m & 4h down move, 1d downtrend
    long_entry_logic.append((df["RSI_3"] > 5.0) | (df["RSI_3_4h"] > 10.0) | (df["ROC_9_1d"] > -20.0))
    # 5m & 1h down move, 1h still high
    long_entry_logic.append(
      (df["RSI_3"] > 5.0) | (df["RSI_3_1h"] > 30.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 50.0)
    )
    # 15m & 4h & 1d down move
    long_entry_logic.append((df["RSI_3_15m"] > 3.0) | (df["RSI_3_4h"] > 10.0) | (df["RSI_3_1d"] > 15.0))
    # 15m & 1h down move
    long_entry_logic.append((df["RSI_3_15m"] > 3.0) | (df["RSI_3_1h"] > 3.0))
    # 15m & 1h down move, 4h still not low enough
    long_entry_logic.append((df["RSI_3_15m"] > 3.0) | (df["RSI_3_1h"] > 5.0) | (df["RSI_14_4h"] < 35.0))
    # 15m & 1h down move, 1d still high
    long_entry_logic.append((df["RSI_3_15m"] > 3.0) | (df["RSI_3_1h"] > 10.0) | (df["AROONU_14_1d"] < 50.0))
    # 15m & 1h down move, 1h still not low enough
    long_entry_logic.append(
      (df["RSI_3_15m"] > 3.0) | (df["RSI_3_1h"] > 15.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 30.0)
    )
    # 15m & 4h down move, 4h still high
    long_entry_logic.append((df["RSI_3_15m"] > 3.0) | (df["RSI_3_4h"] > 30.0) | (df["RSI_14_4h"] < 40.0))
    # 15m & 1h & 4h down move
    long_entry_logic.append((df["RSI_3_15m"] > 5.0) | (df["RSI_3_1h"] > 15.0) | (df["RSI_3_4h"] > 15.0))
    # 15m & 1h & 4h down move, 15m downtrend
    long_entry_logic.append(
      (df["RSI_3_15m"] > 5.0) | (df["RSI_3_1h"] > 20.0) | (df["RSI_3_4h"] > 20.0) | (df["CMF_20_15m"] > -0.20)
    )
    # 15m & 1h down move, 4h still not low enough
    long_entry_logic.append((df["RSI_3_15m"] > 5.0) | (df["RSI_3_1h"] > 20.0) | (df["AROONU_14_4h"] < 20.0))
    # 15m & 1h down move, 1h high
    long_entry_logic.append(
      (df["RSI_3_15m"] > 5.0) | (df["RSI_3_1h"] > 30.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 50.0)
    )
    # 15m & 4h down move, 4h still high
    long_entry_logic.append((df["RSI_3_15m"] > 5.0) | (df["RSI_3_4h"] > 15.0) | (df["AROONU_14_4h"] < 50.0))
    # 15m & 1h down move, 15m & 1h downtrend
    long_entry_logic.append(
      (df["RSI_3_15m"] > 10.0) | (df["RSI_3_1h"] > 10.0) | (df["CMF_20_15m"] > -0.40) | (df["CMF_20_1h"] > -0.40)
    )
    # 15m & 1h down move, 1h still not low enough
    long_entry_logic.append(
      (df["RSI_3_15m"] > 10.0) | (df["RSI_3_1h"] > 10.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 20.0)
    )
    # 15m & 1h down move, 4h still high
    long_entry_logic.append(
      (df["RSI_3_15m"] > 10.0) | (df["RSI_3_1h"] > 20.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 50.0)
    )
    # 15m & 1h down move, 4h overbought
    long_entry_logic.append((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1h"] > 40.0) | (df["ROC_9_4h"] < 50.0))
    # 15m & 1h down move, 1h high
    long_entry_logic.append((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1h"] > 25.0) | (df["AROONU_14_1h"] < 80.0))
    # 15m & 4h down move, 1h & 4h downtrend
    long_entry_logic.append(
      (df["RSI_3_15m"] > 10.0) | (df["RSI_3_4h"] > 10.0) | (df["CMF_20_1h"] > -0.20) | (df["CMF_20_4h"] > -0.20)
    )
    # 15m & 4h down move, 4h still not low enough
    long_entry_logic.append(
      (df["RSI_3_15m"] > 10.0) | (df["RSI_3_4h"] > 10.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 30.0)
    )
    # 15m & 4h down move, 4h still high
    long_entry_logic.append((df["RSI_3_15m"] > 10.0) | (df["RSI_3_4h"] > 10.0) | (df["AROONU_14_4h"] < 40.0))
    # 15m & 4h down move, 1d high
    long_entry_logic.append(
      (df["RSI_3_15m"] > 10.0) | (df["RSI_3_4h"] > 15.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 90.0)
    )
    # 15m & 4h down move, 1h high
    long_entry_logic.append(
      (df["RSI_3_15m"] > 10.0) | (df["RSI_3_4h"] > 20.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 70.0)
    )
    # 15m & 4h down move, 4h still high
    long_entry_logic.append(
      (df["RSI_3_15m"] > 10.0) | (df["RSI_3_4h"] > 20.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 40.0)
    )
    # 15m & 4h down move, 1d downtrend
    long_entry_logic.append((df["RSI_3_15m"] > 10.0) | (df["RSI_3_4h"] > 20.0) | (df["ROC_9_1d"] > -25.0))
    # 15m & 4h down move, 15m still not low enough
    long_entry_logic.append(
      (df["RSI_3_15m"] > 10.0) | (df["RSI_3_4h"] > 25.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 20.0)
    )
    # 15m & 4h down move, 4h high
    long_entry_logic.append((df["RSI_3_15m"] > 10.0) | (df["RSI_3_4h"] > 40.0) | (df["AROONU_14_4h"] < 80.0))
    # 15m & 1h down move, 4h still high
    long_entry_logic.append((df["RSI_3_15m"] > 15.0) | (df["RSI_3_1h"] > 20.0) | (df["AROONU_14_4h"] < 40.0))
    # 15m & 1h down move, 4h high
    long_entry_logic.append((df["RSI_3_15m"] > 15.0) | (df["RSI_3_1h"] > 25.0) | (df["AROONU_14_4h"] < 70.0))
    # 15m & 1h down move, 1h high
    long_entry_logic.append(
      (df["RSI_3_15m"] > 15.0) | (df["RSI_3_1h"] > 25.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 60.0)
    )
    # 15m & 1h down move, 1h still high
    long_entry_logic.append((df["RSI_3_15m"] > 15.0) | (df["RSI_3_1h"] > 30.0) | (df["AROONU_14_1h"] < 40.0))
    # 15m down move, 4h still high, 4h downtrend
    long_entry_logic.append((df["RSI_3_15m"] > 15.0) | (df["AROONU_14_4h"] < 40.0) | (df["ROC_9_4h"] > -20.0))
    # 15m down move, 1d high, 4h overbought
    long_entry_logic.append((df["RSI_3_15m"] > 15.0) | (df["AROONU_14_1d"] < 100.0) | (df["ROC_9_4h"] < 50.0))
    # 15m & 3h down move, 15m still not low enough
    long_entry_logic.append(
      (df["RSI_3_15m"] > 20.0) | (df["RSI_3_4h"] > 20.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 20.0)
    )
    # 15m & 1h down move, 1h still high
    long_entry_logic.append((df["RSI_3_15m"] > 25.0) | (df["RSI_3_1h"] > 25.0) | (df["RSI_14_1h"] < 40.0))
    # 15m & 4h down move, 4h high
    long_entry_logic.append((df["RSI_3_15m"] > 25.0) | (df["RSI_3_4h"] > 25.0) | (df["AROONU_14_4h"] < 70.0))
    # 15m down move, 15m still not low enough, 1d overbought
    long_entry_logic.append(
      (df["RSI_3_15m"] > 25.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 20.0) | (df["ROC_9_1d"] < 80.0)
    )
    # 1h & 4h down move
    long_entry_logic.append((df["RSI_3_1h"] > 3.0) | (df["RSI_3_4h"] > 10.0))
    # 1h & 4h down move, 4h still not low enough
    long_entry_logic.append(
      (df["RSI_3_1h"] > 3.0) | (df["RSI_3_4h"] > 25.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 30.0)
    )
    # 1h & 4h down move, 4h high
    long_entry_logic.append((df["RSI_3_1h"] > 3.0) | (df["RSI_3_4h"] > 50.0) | (df["AROONU_14_4h"] < 70.0))
    # 1h & 4h down move
    long_entry_logic.append((df["RSI_3_1h"] > 5.0) | (df["RSI_3_4h"] > 5.0))
    # 1h & 4h down move, 4h still high
    long_entry_logic.append((df["RSI_3_1h"] > 5.0) | (df["RSI_3_4h"] > 30.0) | (df["AROONU_14_4h"] < 50.0))
    # 1h down move, 1h still high
    long_entry_logic.append((df["RSI_3_1h"] > 5.0) | (df["AROONU_14_1h"] < 50.0))
    # 1h down move, 4h high
    long_entry_logic.append((df["RSI_3_1h"] > 5.0) | (df["AROONU_14_4h"] < 85.0))
    # 1h & 4h down move
    long_entry_logic.append((df["RSI_3_1h"] > 10.0) | (df["RSI_3_4h"] > 10.0))
    # 1h & 4h down move, 4h still not low enough
    long_entry_logic.append(
      (df["RSI_3_1h"] > 10.0) | (df["RSI_3_4h"] > 15.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 30.0)
    )
    # 1h & 4h down move, 1d still high
    long_entry_logic.append(
      (df["RSI_3_1h"] > 10.0) | (df["RSI_3_4h"] > 15.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 50.0)
    )
    # 1h & 1d down move, 1h still moving lower
    long_entry_logic.append(
      (df["RSI_3_1h"] > 10.0) | (df["RSI_3_1d"] > 15.0) | (df["CCI_20_change_pct_1h"] > -0.0)
    )
    # 1h down move, 1d high, 4h downtrend
    long_entry_logic.append((df["RSI_3_1h"] > 10.0) | (df["AROONU_14_1d"] < 85.0) | (df["ROC_9_4h"] > -10.0))
    # 1h & 4h down move, 1h still high
    long_entry_logic.append((df["RSI_3_1h"] > 15.0) | (df["RSI_3_4h"] > 15.0) | (df["AROONU_14_1h"] < 50.0))
    # 1h & 4h & 1d down move
    long_entry_logic.append((df["RSI_3_1h"] > 15.0) | (df["RSI_3_4h"] > 20.0) | (df["RSI_3_1d"] > 30.0))
    # 1h & 4h down move, 1h still not low enough
    long_entry_logic.append(
      (df["RSI_3_1h"] > 15.0) | (df["RSI_3_4h"] > 20.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 20.0)
    )
    # 1h & 4h down move, 4h still not low enough
    long_entry_logic.append(
      (df["RSI_3_1h"] > 15.0) | (df["RSI_3_4h"] > 20.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 30.0)
    )
    # 1h & 4h & 1d down move
    long_entry_logic.append((df["RSI_3_1h"] > 15.0) | (df["RSI_3_4h"] > 25.0) | (df["RSI_3_1d"] > 25.0))
    # 1h & 4h down move, 1h high
    long_entry_logic.append((df["RSI_3_1h"] > 15.0) | (df["RSI_3_4h"] > 40.0) | (df["AROONU_14_1h"] < 80.0))
    # 1h & 1d down move, 1d high
    long_entry_logic.append((df["RSI_3_1h"] > 15.0) | (df["RSI_3_1d"] > 25.0) | (df["AROONU_14_1d"] < 70.0))
    # 1h & 1d down move, 1d high
    long_entry_logic.append(
      (df["RSI_3_1h"] > 15.0) | (df["RSI_3_1d"] > 25.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 70.0)
    )
    # 1h down move, 1h & 4h high
    long_entry_logic.append((df["RSI_3_1h"] > 15.0) | (df["AROONU_14_1h"] < 60.0) | (df["AROONU_14_4h"] < 60.0))
    # 1h & 4h down move, 1d overbought
    long_entry_logic.append((df["RSI_3_1h"] > 20.0) | (df["RSI_3_4h"] > 20.0) | (df["ROC_9_1d"] < 50.0))
    # 1h & 4h down move, 1h still high
    long_entry_logic.append(
      (df["RSI_3_1h"] > 20.0) | (df["RSI_3_4h"] > 25.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 50.0)
    )
    # 1h & 1d down move, 1d high
    long_entry_logic.append((df["RSI_3_1h"] > 20.0) | (df["RSI_3_1d"] > 20.0) | (df["AROONU_14_1d"] < 70.0))
    # 4h & 1d down move, 1d high
    long_entry_logic.append((df["RSI_3_1h"] > 20.0) | (df["RSI_3_1d"] > 40.0) | (df["AROONU_14_1d"] < 80.0))
    # 1h down move, 1h still high, 4h high
    long_entry_logic.append((df["RSI_3_1h"] > 20.0) | (df["AROONU_14_1h"] < 50.0) | (df["AROONU_14_4h"] < 70.0))
    # 1h down move, 4h high
    long_entry_logic.append((df["RSI_3_1h"] > 20.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 90.0))
    # 1h down move, 1h & 1d high
    long_entry_logic.append((df["RSI_3_1h"] > 25.0) | (df["AROONU_14_1h"] < 70.0) | (df["AROONU_14_1d"] < 90.0))
    # 1h down move, 4h still high, 1d downtrend
    long_entry_logic.append((df["RSI_3_1h"] > 25.0) | (df["AROONU_14_4h"] < 40.0) | (df["ROC_9_1d"] > -20.0))
    # 1h down move, 1h still high, 1d overbought
    long_entry_logic.append(
      (df["RSI_3_1h"] > 25.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 50.0) | (df["ROC_9_1d"] < 40.0)
    )
    # 1h & 4h down move, 4h high
    long_entry_logic.append((df["RSI_3_1h"] > 30.0) | (df["RSI_3_4h"] > 45.0) | (df["AROONU_14_4h"] < 80.0))
    # 1h & dh down move, 4h high
    long_entry_logic.append((df["RSI_3_1h"] > 30.0) | (df["RSI_3_4h"] > 50.0) | (df["AROONU_14_4h"] < 85.0))
    # 1h down move, 4h still not low enough, 1d overbought
    long_entry_logic.append((df["RSI_3_1h"] > 30.0) | (df["AROONU_14_4h"] < 30.0) | (df["ROC_9_1d"] < 50.0))
    # 1h down move, 1h still not low enough, 4h downtrend
    long_entry_logic.append(
      (df["RSI_3_1h"] > 30.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 30.0) | (df["ROC_9_4h"] > -30.0)
    )
    # 1h down move, 4h still high, 1d downtrend
    long_entry_logic.append(
      (df["RSI_3_1h"] > 35.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 50.0) | (df["ROC_9_1d"] > -20.0)
    )
    # 1h down move, 4h & 1d overbought
    long_entry_logic.append((df["RSI_3_1h"] > 40.0) | (df["ROC_9_4h"] < 10.0) | (df["ROC_9_1d"] < 50.0))
    # 1h down move, 4h high & overbought
    long_entry_logic.append((df["RSI_3_1h"] > 50.0) | (df["AROONU_14_4h"] < 90.0) | (df["ROC_9_4h"] < 20.0))
    # 1h down move, 4h high & overbought
    long_entry_logic.append(
      (df["RSI_3_1h"] > 50.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 80.0) | (df["ROC_9_4h"] < 20.0)
    )
    # 4h down move, 15m not low enough, 1h still high
    long_entry_logic.append(
      (df["RSI_3_4h"] > 3.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 20.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 40.0)
    )
    # 4h & 1d down move, 4h downtrend
    long_entry_logic.append((df["RSI_3_4h"] > 5.0) | (df["RSI_3_1d"] > 20.0) | (df["ROC_9_4h"] > -20.0))
    # 4h & 1d down move, 1d high
    long_entry_logic.append((df["RSI_3_4h"] > 5.0) | (df["RSI_3_1d"] > 30.0) | (df["AROONU_14_1d"] < 70.0))
    # 4h down move, 4h still high, 1d downtrend
    long_entry_logic.append(
      (df["RSI_3_4h"] > 5.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 40.0) | (df["ROC_9_1d"] > -20.0)
    )
    # 4h down move, 1d still not low enough, 1d downtrend
    long_entry_logic.append(
      (df["RSI_3_4h"] > 5.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 30.0) | (df["ROC_9_1d"] > -20.0)
    )
    # 4h down move, 1h downtrend, 1h still not low enough
    long_entry_logic.append((df["RSI_3_4h"] > 10.0) | (df["CMF_20_1h"] > -0.25) | (df["AROONU_14_1h"] < 30.0))
    # 4h down move, 1h & 1d downtrend
    long_entry_logic.append((df["RSI_3_4h"] > 10.0) | (df["ROC_9_1h"] > -20.0) | (df["ROC_9_1d"] > -20.0))
    # 4h & 1d down move, 4h still high
    long_entry_logic.append(
      (df["RSI_3_4h"] > 15.0) | (df["RSI_3_1d"] > 45.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 40.0)
    )
    # 4h & 1d down move, 1d high
    long_entry_logic.append(
      (df["RSI_3_4h"] > 20.0) | (df["RSI_3_1d"] > 25.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 60.0)
    )
    # 4h down move, 1d high & overbought
    long_entry_logic.append((df["RSI_3_4h"] > 20.0) | (df["AROONU_14_1d"] < 70.0) | (df["ROC_9_1d"] < 50.0))
    # 4h down move, 1h still high, 1d downtrend
    long_entry_logic.append(
      (df["RSI_3_4h"] > 20.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 50.0) | (df["ROC_9_1d"] > -20.0)
    )
    # 4h down move, 1h high
    long_entry_logic.append((df["RSI_3_4h"] > 20.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 80.0))
    # 4h down move, 1d high, 1h downtrend
    long_entry_logic.append(
      (df["RSI_3_4h"] > 20.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 70.0) | (df["ROC_9_1h"] > -10.0)
    )
    # 4h down move, 4h still high, 1d overbought
    long_entry_logic.append((df["RSI_3_4h"] > 30.0) | (df["AROONU_14_4h"] < 40.0) | (df["ROC_9_1d"] < 100.0))
    # 4h down move, 4h still high, 1d overbought
    long_entry_logic.append((df["RSI_3_4h"] > 35.0) | (df["AROONU_14_4h"] < 50.0) | (df["ROC_9_1d"] < 40.0))
    # 4h down move, 4h still high, 1d high
    long_entry_logic.append((df["RSI_3_4h"] > 40.0) | (df["AROONU_14_4h"] < 50.0) | (df["AROONU_14_1d"] < 100.0))
    # 4h down move, 4h & 1d overbought
    long_entry_logic.append((df["RSI_3_4h"] > 40.0) | (df["ROC_9_4h"] < 10.0) | (df["ROC_9_1d"] < 50.0))
    # 1d down move, 1h still not low enough
    long_entry_logic.append((df["RSI_3_1d"] > 5.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 20.0))
    # 1h & 4h high, 4h overbought
    long_entry_logic.append((df["AROONU_14_1h"] < 60.0) | (df["AROONU_14_4h"] < 100.0) | (df["ROC_9_4h"] < 30.0))
    # 4h & 1d high, 4h overbought
    long_entry_logic.append((df["AROONU_14_4h"] < 60.0) | (df["AROONU_14_1d"] < 100.0) | (df["ROC_9_4h"] < 40.0))
    # 1d red, 4h down move, 1h still high
    long_entry_logic.append(
      (df["change_pct_1d"] > -30.0) | (df["RSI_3_4h"] > 30.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 50.0)
    )
    # pump, drop but not yet near the previous lows
    long_entry_logic.append(
      (((df["high_max_24_4h"] - df["low_min_24_4h"]) / df["low_min_24_4h"]) < 2.0)
      | (df["close"] > (df["high_max_12_4h"] * 0.60))
      | (df["close"] < (df["low_min_24_4h"] * 1.10))
    )
    # pump, drop but not yet near the previous lows
    long_entry_logic.append(
      (((df["high_max_12_1d"] - df["low_min_12_1d"]) / df["low_min_12_1d"]) < 5.0)
      | (df["close"] > (df["high_max_6_1d"] * 0.30))
      | (df["close"] < (df["low_min_12_1d"] * 1.25))
    )
    # big drop in the last hour
    long_entry_logic.append(df["close"] > (df["close_max_12"] * 0.50))
    # big drop in the last 12 days, 15m & 4h down move
    long_entry_logic.append(
      (df["close"] > (df["high_max_12_1d"] * 0.40)) | (df["RSI_3_15m"] > 10.0) | (df["RSI_3_4h"] > 10.0)
    )
    # big drop in the last 20 days, 15m & 1h down move
    long_entry_logic.append(
      (df["close"] > (df["high_max_20_1d"] * 0.40)) | (df["RSI_14_15m"] < 10.0) | (df["RSI_14_1h"] < 10.0)
    )
    # big drop in the last 20 days, 1d down move
    long_entry_logic.append((df["close"] > (df["high_max_20_1d"] * 0.25)) | (df["RSI_3_1d"] > 30.0))
    # big drop in the last 20 days, 4h still not low enough
    long_entry_logic.append((df["close"] > (df["high_max_20_1d"] * 0.10)) | (df["RSI_14_4h"] < 30.0))
    # big drop in the last 30 days, 4h down move
    long_entry_logic.append((df["close"] > (df["high_max_30_1d"] * 0.25)) | (df["RSI_3_4h"] > 20.0))

    # Logic
    long_entry_logic.append(df["RSI_3"] < 40.0)
    long_entry_logic.append(df["AROONU_14"] < 25.0)
    long_entry_logic.append(df["STOCHRSIk_14_14_3_3"] < 20.0)
    long_entry_logic.append(df["AROONU_14_15m"] < 25.0)
    long_entry_logic.append(df["STOCHRSIk_14_14_3_3_15m"] < 30.0)
    long_entry_logic.append(df["close"] < df["EMA_16"] * 0.975)
    long_entry_logic.append(((df["EMA_50"] - df["EMA_200"]) / df["close"] * 100.0) < -5.5)

def append_long_1(df, long_entry_logic, allowed_empty_candles_288) -> None:
    """Append NFI long condition #1, the normal-mode long entry."""
    # Protections
    long_entry_logic.append(df["num_empty_288"] <= allowed_empty_candles_288)
    long_entry_logic.append(df["protections_long_global"] == True)

    long_entry_logic.append(
      # 5m & 15m & 1h down move
      ((df["RSI_3"] > 3.0) | (df["RSI_3_15m"] > 3.0) | (df["RSI_3_change_pct_1h"] > -50.0))
      # 5m & 15m down move, 5h high
      & ((df["RSI_3"] > 3.0) | (df["RSI_3_15m"] > 5.0) | (df["RSI_14_4h"] < 60.0))
      # 5m & 15m down move, 4h high
      & ((df["RSI_3"] > 3.0) | (df["RSI_3_15m"] > 10.0) | (df["AROONU_14_4h"] < 100.0))
      # 5m & 1h down move
      & ((df["RSI_3"] > 3.0) | (df["RSI_3_1h"] > 5.0))
      # 5m & 1h down move, 15m still not low enough
      & ((df["RSI_3"] > 5.0) | (df["RSI_3_1h"] > 10.0) | (df["AROONU_14_15m"] < 30.0))
      # 5m & 1h down move, 4h high
      & ((df["RSI_3"] > 3.0) | (df["RSI_3_1h"] > 25.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 80.0))
      # 15m & 1h down move, 1d still high
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_1h"] > 3.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 50.0))
      # 5m & 1h down move, 15m still not low enough
      & ((df["RSI_3"] > 3.0) | (df["RSI_3_1h"] > 15.0) | (df["AROONU_14_15m"] < 30.0))
      # 5m & 4h down move, 4h high
      & ((df["RSI_3"] > 3.0) | (df["RSI_3_4h"] > 25.0) | (df["AROONU_14_4h"] < 70.0))
      # 5m down move, 15m high
      & ((df["RSI_3"] > 3.0) | (df["AROONU_14_15m"] < 80.0))
      # 5m & 4h down move, 4h high
      & ((df["RSI_3"] > 5.0) | (df["RSI_3_4h"] > 35.0) | (df["AROONU_14_4h"] < 70.0))
      # 15m down move, 1h downtrend, 1h high
      & ((df["RSI_3_15m"] > 1.0) | (df["CMF_20_1h"] > -0.1) | (df["AROONU_14_1h"] < 70.0))
      # 15m & 1h & 4h down move
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_1h"] > 10.0) | (df["RSI_3_4h"] > 15.0))
      # 15m & 1h down move, 1h still high
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_1h"] > 10.0) | (df["AROONU_14_1h"] < 50.0))
      # 15m & 1h down move, 1d high
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_1h"] > 10.0) | (df["AROONU_14_1d"] < 100.0))
      # 15m & 1h down move, 1h still high
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_1h"] > 10.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 40.0))
      # 15m & 1h & 4h & 1d down move
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_1h"] > 15.0) | (df["RSI_3_4h"] > 15.0) | (df["RSI_3_1d"] > 15.0))
      # 15m & 1h down move, 15m still high
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_1h"] > 20.0) | (df["AROONU_14_15m"] < 40.0))
      # 15m & 1h down move, 1h high
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_1h"] > 20.0) | (df["AROONU_14_1h"] < 70.0))
      # 15m & 1h down move, 1h high
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_1h"] > 30.0) | (df["AROONU_14_1h"] < 80.0))
      # 15m & 1h down move, 1h still high
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_1h"] > 35.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 50.0))
      # 15m & 1h down move, 1h high
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_1h"] > 40.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 70.0))
      # 15m & 1h down move, 1h high
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_1h"] > 45.0) | (df["AROONU_14_1h"] < 80.0))
      # 15m & 4h down move, 1d high
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_4h"] > 15.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 90.0))
      # 15m & 4h down move, 4h high
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_4h"] > 25.0) | (df["AROONU_14_4h"] < 60.0))
      # 15m & 4h down move, 1d downtrend
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_4h"] > 30.0) | (df["ROC_9_1d"] > -50.0))
      # 15m & 4h down move, 4h still high
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_4h"] > 35.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 50.0))
      # 15m down move, 15m downtrend
      & ((df["RSI_3_15m"] > 3.0) | (df["CMF_20_15m"] > -0.40) | (df["ROC_9_15m"] > -20.0))
      # 15m down move, 15m still high, 15m downtrend
      & ((df["RSI_3_15m"] > 3.0) | (df["AROONU_14_15m"] < 40.0) | (df["ROC_9_15m"] > -20.0))
      # 15m down move, 1h & 4h high
      & ((df["RSI_3_15m"] > 3.0) | (df["AROONU_14_1h"] < 85.0) | (df["AROONU_14_4h"] < 90.0))
      # 15m down move, 4h high, 15m downtrend
      & ((df["RSI_3_15m"] > 3.0) | (df["AROONU_14_4h"] < 70.0) | (df["ROC_9_15m"] > -20.0))
      # 15m down move, 4h high, 1d overbought
      & ((df["RSI_3_15m"] > 3.0) | (df["AROONU_14_4h"] < 85.0) | (df["ROC_9_1d"] < 100.0))
      # 15m down move, 1h high, 4h overbought
      & ((df["RSI_3_15m"] > 3.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 90.0) | (df["ROC_9_4h"] < 10.0))
      # 15m down move, 4h high & overbought
      & ((df["RSI_3_15m"] > 3.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 80.0) | (df["ROC_9_4h"] < 30.0))
      # 15m down move, drop in last half hour, 15m downtrend
      & ((df["RSI_3_15m"] > 3.0) | (df["close"] > (df["close_max_6"] * 0.75)) | (df["ROC_9_15m"] > -20.0))
      # 15m & 1h down move, 1h still high
      & ((df["RSI_3_15m"] > 5.0) | (df["RSI_3_1h"] > 5.0) | (df["AROONU_14_1h"] < 50.0))
      # 15m & 1h down move, 4h high
      & ((df["RSI_3_15m"] > 5.0) | (df["RSI_3_1h"] > 5.0) | (df["AROONU_14_4h"] < 70.0))
      # 15m & 1h down move, 1d overbought
      & ((df["RSI_3_15m"] > 5.0) | (df["RSI_3_1h"] > 5.0) | (df["ROC_9_1d"] < 40.0))
      # 5m & 1h down move, 1h overbought
      & ((df["RSI_3_15m"] > 5.0) | (df["RSI_3_1h"] > 60.0) | (df["ROC_9_1h"] < 40.0))
      # 15m & 4h down move, 1d still high
      & ((df["RSI_3_15m"] > 5.0) | (df["RSI_3_4h"] > 5.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 40.0))
      # 15m & 4h down move, 1d downtrend
      & ((df["RSI_3_15m"] > 5.0) | (df["RSI_3_4h"] > 5.0) | (df["ROC_9_1d"] > -20.0))
      # 15m & 4h down move, 1h still high
      & ((df["RSI_3_15m"] > 5.0) | (df["RSI_3_4h"] > 10.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 50.0))
      # 15m & 4h down move, 1d high
      & ((df["RSI_3_15m"] > 5.0) | (df["RSI_3_4h"] > 15.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 60.0))
      # 15m & 4h down move, 15m still high
      & ((df["RSI_3_15m"] > 5.0) | (df["RSI_3_4h"] > 30.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 50.0))
      # 15m down move, 15m & 4h still high
      & ((df["RSI_3_15m"] > 5.0) | (df["AROONU_14_15m"] < 50.0) | (df["AROONU_14_4h"] < 60.0))
      # 15m down move, 15m still high, 1d overbought
      & ((df["RSI_3_15m"] > 5.0) | (df["AROONU_14_15m"] < 50.0) | (df["ROC_9_1d"] < 80.0))
      # 15m down move, 15m high
      & ((df["RSI_3_15m"] > 5.0) | (df["AROONU_14_15m"] < 80.0))
      # 15m down move, 4h high, 1d overbought
      & ((df["RSI_3_15m"] > 5.0) | (df["AROONU_14_4h"] < 60.0) | (df["ROC_9_1d"] < 80.0))
      # 15m & 1h down move, 1h still high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1h"] > 10.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 40.0))
      # 15m & 1h down move, 4h high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1h"] > 10.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 70.0))
      # 15m & 1h down move, 1h still high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1h"] > 15.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 50.0))
      # 15m & 1h down move, 1d downtrend
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1h"] > 15.0) | (df["ROC_9_1d"] > -40.0))
      # 15m & 1h down move, 4h high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1h"] > 20.0) | (df["RSI_14_4h"] < 80.0))
      # 15m & 1h down move, 15m still high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1h"] > 20.0) | (df["AROONU_14_15m"] < 50.0))
      # 15m & 1h down move, 4h overbought
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1h"] > 25.0) | (df["ROC_9_4h"] < 80.0))
      # 15m & 4h down move, 1h high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_4h"] > 10.0) | (df["AROONU_14_1h"] < 75.0))
      # 15m & 4h down move, 15m still high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_4h"] > 10.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 50.0))
      # 15m & 4h down move, 1h still high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_4h"] > 10.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 40.0))
      # 15m & 4h down move, 4h downtrend
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_4h"] > 10.0) | (df["ROC_9_4h"] > -20.0))
      # 15m & 4h down move, 1d overbought
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_4h"] > 25.0) | (df["ROC_9_1d"] < 30.0))
      # 15m & 4h down move, 1h high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_4h"] > 30.0) | (df["AROONU_14_1h"] < 85.0))
      # 15m & 4h down move, 4h high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_4h"] > 60.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 90.0))
      # 15m & 1d down move, 1d high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1d"] > 50.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 80.0))
      # 15m down move & downtrend, 4h high
      & ((df["RSI_3_15m"] > 10.0) | (df["CMF_20_15m"] > -0.3) | (df["AROONU_14_4h"] < 100.0))
      # 15m down move, 15m & 4h high
      & ((df["RSI_3_15m"] > 10.0) | (df["AROONU_14_15m"] < 70.0) | (df["AROONU_14_4h"] < 80.0))
      # 15m down move, 1h high & overbought
      & ((df["RSI_3_15m"] > 10.0) | (df["AROONU_14_1h"] < 90.0) | (df["ROC_9_1h"] < 20.0))
      # 15m down move, 1h high, 1d downtrend
      & ((df["RSI_3_15m"] > 10.0) | (df["AROONU_14_1h"] < 90.0) | (df["ROC_9_1d"] > -40.0))
      # 15m down move, 1h high, 1d overbought
      & ((df["RSI_3_15m"] > 10.0) | (df["AROONU_14_1h"] < 100.0) | (df["ROC_9_1d"] < 80.0))
      # 15m down move, 1h high, 4h downtrend
      & ((df["RSI_3_15m"] > 10.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 70.0) | (df["ROC_9_4h"] > -25.0))
      # 15m down move, 1h high, 1d downtrend
      & ((df["RSI_3_15m"] > 10.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 70.0) | (df["ROC_9_1d"] > -50.0))
      # 15m down move, 1h high & overbought
      & ((df["RSI_3_15m"] > 10.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 90.0) | (df["ROC_9_1h"] < 20.0))
      # 15m down move, 1h & 1d overbought
      & ((df["RSI_3_15m"] > 10.0) | (df["ROC_9_1h"] < 10.0) | (df["ROC_9_1d"] < 80.0))
      # 15m down move, 4h high
      & ((df["RSI_3_15m"] > 10.0) | (df["ROC_9_4h"] < 60.0))
      # 15m & 1h down move, 1h high
      & ((df["RSI_3_15m"] > 15.0) | (df["RSI_3_1h"] > 20.0) | (df["AROONU_14_1h"] < 80.0))
      # 15m down move, 15m still high, 4h overbought
      & ((df["RSI_3_15m"] > 15.0) | (df["RSI_14_15m"] < 50.0) | (df["ROC_9_4h"] < 50.0))
      # 15m down move, 15m & 1h high
      & ((df["RSI_3_15m"] > 15.0) | (df["AROONU_14_15m"] < 70.0) | (df["AROONU_14_1h"] < 100.0))
      # 15m down move, 15m & 1h high
      & ((df["RSI_3_15m"] > 15.0) | (df["AROONU_14_15m"] < 80.0) | (df["AROONU_14_1h"] < 90.0))
      # 15m & 4h down move, 15m still high
      & ((df["RSI_3_15m"] > 20.0) | (df["RSI_3_4h"] > 35.0) | (df["AROONU_14_15m"] < 40.0))
      # 15m down move, 1h & 4h high
      & ((df["RSI_3_15m"] > 20.0) | (df["AROONU_14_1h"] < 100.0) | (df["AROONU_14_4h"] < 100.0))
      # 15m down move, 1h high & overbought
      & ((df["RSI_3_15m"] > 20.0) | (df["AROONU_14_1h"] < 100.0) | (df["ROC_9_1h"] < 20.0))
      # 15m down move, 1d overbought
      & ((df["RSI_3_15m"] > 30.0) | (df["ROC_9_1d"] < 80.0))
      # 15m & 4h down move, 15m high
      & ((df["RSI_3_15m"] > 40.0) | (df["RSI_3_4h"] > 45.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 70.0))
      # 1h & 4h down move, 4h downtrend
      & ((df["RSI_3_1h"] > 3.0) | (df["RSI_3_4h"] > 10.0) | (df["ROC_9_4h"] > -10.0))
      # 1h & 4h down move, 1h still high
      & ((df["RSI_3_1h"] > 3.0) | (df["RSI_3_4h"] > 15.0) | (df["AROONU_14_1h"] < 50.0))
      # 1h & 4h down move, 1d high
      & ((df["RSI_3_1h"] > 3.0) | (df["RSI_3_4h"] > 15.0) | (df["AROONU_14_1d"] < 90.0))
      # 1h & 4h down move, 1d high
      & ((df["RSI_3_1h"] > 3.0) | (df["RSI_3_4h"] > 25.0) | (df["AROONU_14_1d"] < 100.0))
      # 1h & 1d down move, 4h still high
      & ((df["RSI_3_1h"] > 3.0) | (df["RSI_3_1d"] > 15.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 50.0))
      # 1h & 4h down move, 1d overbought
      & ((df["RSI_3_1h"] > 5.0) | (df["RSI_3_4h"] > 5.0) | (df["ROC_9_1d"] < 10.0))
      # 1h & 4h down move, 4h still high
      & ((df["RSI_3_1h"] > 5.0) | (df["RSI_3_4h"] > 10.0) | (df["AROONU_14_4h"] < 40.0))
      # 1h & 4h down move, 1h downtrend
      & ((df["RSI_3_1h"] > 5.0) | (df["RSI_3_4h"] > 10.0) | (df["CMF_20_1h"] > -0.3))
      # 1h & 4h down move, 1d downtrend
      & ((df["RSI_3_1h"] > 5.0) | (df["RSI_3_4h"] > 10.0) | (df["ROC_9_1d"] > -40.0))
      # 1h & 4h down move, 4h still not low enough
      & ((df["RSI_3_1h"] > 5.0) | (df["RSI_3_4h"] > 15.0) | (df["AROONU_14_4h"] < 30.0))
      # 1h & 4h down move, 4h high
      & ((df["RSI_3_1h"] > 5.0) | (df["RSI_3_4h"] > 50.0) | (df["AROONU_14_4h"] < 70.0))
      # 1h & 4h down move, 1d overbought
      & ((df["RSI_3_1h"] > 5.0) | (df["RSI_3_4h"] > 20.0) | (df["ROC_9_1d"] < 40.0))
      # 1h & 1d down move, 1d downtrend
      & ((df["RSI_3_1h"] > 5.0) | (df["RSI_3_1d"] > 5.0) | (df["ROC_9_1d"] > -30.0))
      # 1h down move, 1h still high, 4h high
      & ((df["RSI_3_1h"] > 5.0) | (df["AROONU_14_1h"] < 50.0) | (df["AROONU_14_4h"] < 90.0))
      # 1h down move, 1d high, 4h downtrend
      & ((df["RSI_3_1h"] > 5.0) | (df["AROONU_14_1d"] < 90.0) | (df["ROC_9_4h"] > -30.0))
      # 1h & 4h down move, 15m still not low enough
      & ((df["RSI_3_1h"] > 10.0) | (df["RSI_3_4h"] > 10.0) | (df["AROONU_14_15m"] < 30.0))
      # 1h & 4h down move, 1h still high
      & ((df["RSI_3_1h"] > 10.0) | (df["RSI_3_4h"] > 10.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 50.0))
      # 1h & 1d down move, 4h high
      & ((df["RSI_3_1h"] > 10.0) | (df["RSI_3_1d"] > 20.0) | (df["AROONU_14_4h"] < 80.0))
      # 1h down move, 4h high
      & ((df["RSI_3_1h"] > 10.0) | (df["RSI_14_4h"] < 75.0))
      # 1h down move, 15m downtrend, 1d high
      & ((df["RSI_3_1h"] > 10.0) | (df["CMF_20_15m"] > -0.40) | (df["AROONU_14_1d"] < 70.0))
      # 1h down move, 1h high, 4h overbought
      & ((df["RSI_3_1h"] > 10.0) | (df["AROONU_14_1h"] < 70.0) | (df["ROC_9_4h"] < 10.0))
      # 1h down move, 4h overbought
      & ((df["RSI_3_1h"] > 10.0) | (df["ROC_9_4h"] < 50.0))
      # 1h & 4h down move, 4h still high
      & ((df["RSI_3_1h"] > 15.0) | (df["RSI_3_4h"] > 15.0) | (df["AROONU_14_4h"] < 40.0))
      # 1h & 4h down move, 4h high
      & ((df["RSI_3_1h"] > 15.0) | (df["RSI_3_4h"] > 20.0) | (df["AROONU_14_4h"] < 80.0))
      # 1h & 4h down move, 1d overbought
      & ((df["RSI_3_1h"] > 15.0) | (df["RSI_3_4h"] > 25.0) | (df["ROC_9_1d"] < 40.0))
      # 15m down move, 1h high, 1d downtrend
      & ((df["RSI_3_1h"] > 15.0) | (df["AROONU_14_1h"] < 70.0) | (df["ROC_9_1d"] > -20.0))
      # 1h down move, 1h high, 1d overbought
      & ((df["RSI_3_1h"] > 15.0) | (df["AROONU_14_1h"] < 70.0) | (df["ROC_9_1d"] < 50.0))
      # 1h down move, 1h high
      & ((df["RSI_3_1h"] > 15.0) | (df["AROONU_14_1h"] < 80.0))
      # 1h down mve, 4h high, 1d overbought
      & ((df["RSI_3_1h"] > 15.0) | (df["AROONU_14_4h"] < 80.0) | (df["ROC_9_1d"] < 30.0))
      # 1h down move, 1d high & overbought
      & ((df["RSI_3_1h"] > 15.0) | (df["AROONU_14_1d"] < 80.0) | (df["ROC_9_1d"] < 40.0))
      # 1h down move, 1h & 4h downtrend
      & ((df["RSI_3_1h"] > 15.0) | (df["ROC_9_1h"] > -30.0) | (df["ROC_9_4h"] > -30.0))
      # 1h & 4h down move, 4h overbought
      & ((df["RSI_3_1h"] > 20.0) | (df["RSI_3_4h"] > 50.0) | (df["ROC_9_4h"] < 80.0))
      # 1h down move, 1h still high, 4h downtrend
      & ((df["RSI_3_1h"] > 20.0) | (df["AROONU_14_1h"] < 40.0) | (df["ROC_9_4h"] > -30.0))
      # 1h down move, 4h high, 1d overbought
      & ((df["RSI_3_1h"] > 20.0) | (df["AROONU_14_4h"] < 70.0) | (df["ROC_9_1d"] < 200.0))
      # 1h down move, 4h high, 1d overbought
      & ((df["RSI_3_1h"] > 20.0) | (df["AROONU_14_4h"] < 90.0) | (df["ROC_9_1d"] < 60.0))
      # 1h down move, 4h high & overbought
      & ((df["RSI_3_1h"] > 20.0) | (df["AROONU_14_4h"] < 100.0) | (df["ROC_9_4h"] < 50.0))
      # 1h down move, 1d high & overbought
      & ((df["RSI_3_1h"] > 20.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 90.0) | (df["ROC_9_1d"] < 80.0))
      # 1h down move, 1h high, 15n downtrend
      & ((df["RSI_3_1h"] > 25.0) | (df["AROONU_14_1h"] < 70.0) | (df["ROC_9_15m"] > -20.0))
      # 1h down move, 1h still high, 1d overbought
      & ((df["RSI_3_1h"] > 25.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 50.0) | (df["ROC_9_1d"] < 40.0))
      # 1h down move, 4h & 1d overbought
      & ((df["RSI_3_1h"] > 25.0) | (df["ROC_9_4h"] < 80.0) | (df["ROC_9_1d"] < 100.0))
      # 1h down move, 4h high, 1d downtrend
      & ((df["RSI_3_1h"] > 35.0) | (df["AROONU_14_4h"] < 90.0) | (df["ROC_9_1d"] > -20.0))
      # 1h down move, 1d high & overbought
      & ((df["RSI_3_1h"] > 35.0) | (df["AROONU_14_1d"] < 90.0) | (df["ROC_9_1d"] < 80.0))
      # 1h down move, 4h & 1d overbought
      & ((df["RSI_3_1h"] > 35.0) | (df["ROC_9_4h"] < 40.0) | (df["ROC_9_1d"] < 80.0))
      # 1h down move, 1h downtrend, 1h high
      & ((df["RSI_3_1h"] > 40.0) | (df["CMF_20_1h"] > -0.25) | (df["AROONU_14_1h"] < 90.0))
      # 1h down move, 1h & 4h high
      & ((df["RSI_3_1h"] > 40.0) | (df["AROONU_14_1h"] < 60.0) | (df["AROONU_14_4h"] < 100.0))
      # 1h down move, 1h high, 15m downtrend
      & ((df["RSI_3_1h"] > 40.0) | (df["AROONU_14_1h"] < 80.0) | (df["ROC_9_15m"] > -15.0))
      # 1h down move, 1h high, 1d overbought
      & ((df["RSI_3_1h"] > 40.0) | (df["AROONU_14_1h"] < 80.0) | (df["ROC_9_1d"] < 100.0))
      # 1h down move, 1h & 4h high
      & ((df["RSI_3_1h"] > 45.0) | (df["AROONU_14_1h"] < 80.0) | (df["AROONU_14_4h"] < 100.0))
      # 1h down move, 1h high & overbought
      & ((df["RSI_3_1h"] > 50.0) | (df["AROONU_14_1h"] < 90.0) | (df["ROC_9_1h"] < 20.0))
      # 1h down move, 1h still high, 4h high
      & ((df["RSI_3_1h"] > 60.0) | (df["AROONU_14_1h"] < 50.0) | (df["RSI_14_4h"] < 90.0))
      # 4h & 1d down move, 1d high
      & ((df["RSI_3_4h"] > 5.0) | (df["RSI_3_1d"] > 20.0) | (df["AROONU_14_1d"] < 40.0))
      # 4h down move, 4h & 1d downtrend
      & ((df["RSI_3_4h"] > 5.0) | (df["ROC_9_4h"] > -30.0) | (df["ROC_9_1d"] > -40.0))
      # 4h & 1d down move, 4h still not low enough
      & ((df["RSI_3_4h"] > 10.0) | (df["RSI_3_1d"] > 15.0) | (df["AROONU_14_4h"] < 20.0))
      # 4h & 1d down move, 1d still high
      & ((df["RSI_3_4h"] > 10.0) | (df["RSI_3_1d"] > 25.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 50.0))
      # 4h down move, 4h still high
      & ((df["RSI_3_4h"] > 10.0) | (df["AROONU_14_4h"] < 50.0))
      # 4h down move, 1d high
      & ((df["RSI_3_4h"] > 10.0) | (df["AROONU_14_1d"] < 100.0))
      # 4h down move, 1h high, 1d downtrend
      & ((df["RSI_3_4h"] > 10.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 60.0) | (df["ROC_9_1d"] > -40.0))
      # 4h down move, 4h still not low enough, 1d downtrend
      & ((df["RSI_3_4h"] > 10.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 30.0) | (df["ROC_9_1d"] > -20.0))
      # 4h down move, 1h & 4h downtrend
      & ((df["RSI_3_4h"] > 10.0) | (df["ROC_9_1h"] > -30.0) | (df["ROC_9_4h"] > -30.0))
      # 4h down move, 4h & 1d downtrend
      & ((df["RSI_3_4h"] > 15.0) | (df["ROC_9_4h"] > -20.0) | (df["ROC_9_1d"] > -30.0))
      # 4h down move, 1d high & overbought
      & ((df["RSI_3_4h"] > 20.0) | (df["AROONU_14_1d"] < 80.0) | (df["ROC_9_1d"] < 80.0))
      # 4h down move, 4h still high, 1d downtrend
      & ((df["RSI_3_4h"] > 25.0) | (df["AROONU_14_4h"] < 50.0) | (df["ROC_9_1d"] > -40.0))
      # 4h down move, 4h high, 1d overbought
      & ((df["RSI_3_4h"] > 30.0) | (df["AROONU_14_4h"] < 80.0) | (df["ROC_9_1d"] < 50.0))
      # 4h down move, 1d overbought
      & ((df["RSI_3_4h"] > 45.0) | (df["ROC_9_1d"] < 80.0))
      # 4h down move, 4h high, 1d overbought
      & ((df["RSI_3_4h"] > 50.0) | (df["AROONU_14_4h"] < 70.0) | (df["ROC_9_1d"] < 40.0))
      # 4h down move, 1h high, 1d overbought
      & ((df["RSI_3_4h"] > 60.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 90.0) | (df["ROC_9_1d"] < 60.0))
      # 1d down move, 1h high, 1d downtrend
      & ((df["RSI_3_1d"] > 5.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 90.0) | (df["ROC_9_1d"] > -20.0))
      # 1d down move, 1h still high, 4h high
      & ((df["RSI_3_1d"] > 20.0) | (df["AROONU_14_1h"] < 50.0) | (df["AROONU_14_4h"] < 90.0))
      # 1d down move, 1h & 4h high
      & ((df["RSI_3_1d"] > 25.0) | (df["AROONU_14_1h"] < 80.0) | (df["AROONU_14_4h"] < 90.0))
      # 1d down move, 1d high
      & ((df["RSI_3_1d"] > 40.0) | (df["AROONU_14_1d"] < 80.0))
      # 1d down move, 4h still high, 1d overbought
      & ((df["RSI_3_1d"] > 50.0) | (df["AROONU_14_4h"] < 50.0) | (df["ROC_9_1d"] < 200.0))
      # 1d down move, 1d high & overbought
      & ((df["RSI_3_1d"] > 60.0) | (df["AROONU_14_1d"] < 80.0) | (df["ROC_9_1d"] < 50.0))
      # 1h down move, 4h high, 1d overbought
      & ((df["RSI_3_change_pct_1h"] > -75.0) | (df["AROONU_14_4h"] < 90.0) | (df["ROC_9_1d"] < 100.0))
      # 15m & 1h & 4h downtrend
      & ((df["CMF_20_15m"] > -0.3) | (df["CMF_20_1h"] > -0.3) | (df["CMF_20_4h"] > -0.3))
      # 15m high, 1d overbought
      & ((df["AROONU_14_15m"] < 70.0) | (df["ROC_9_1d"] < 80.0))
      # 1h still high, 1h & 4h downtrend
      & ((df["AROONU_14_1h"] < 40.0) | (df["ROC_9_1h"] > -20.0) | (df["ROC_9_4h"] > -30.0))
      # 1h & 4h high, 1h overbought
      & ((df["AROONU_14_1h"] < 85.0) | (df["AROONU_14_4h"] < 90.0) | (df["ROC_9_1h"] < 20.0))
      # 1h high, 1h & 4h overbought
      & ((df["AROONU_14_1h"] < 85.0) | (df["ROC_9_1h"] < 10.0) | (df["ROC_9_1d"] < 30.0))
      # 1h high, 1h overbought, 1d downtrend
      & ((df["AROONU_14_1h"] < 85.0) | (df["ROC_9_1h"] < 20.0) | (df["ROC_9_1d"] > -40.0))
      # 4h & 1d high, 1d overbought
      & ((df["AROONU_14_4h"] < 80.0) | (df["AROONU_14_1d"] < 100.0) | (df["ROC_9_1d"] < 50.0))
      # 4h high, 1h downtrend
      & ((df["AROONU_14_4h"] < 80.0) | (df["ROC_9_1h"] > -15.0))
      # 4h high, 1d downtrend
      & ((df["AROONU_14_4h"] < 80.0) | (df["ROC_9_1d"] > -40.0))
      # 1d high, 4h downtrend, 1d overbought
      & ((df["AROONU_14_1d"] < 85.0) | (df["ROC_9_4h"] > -25.0) | (df["ROC_9_1d"] < 50.0))
      # 1d high, 1h & 4h downtrend
      & ((df["AROONU_14_1d"] < 90.0) | (df["ROC_9_1h"] > -10.0) | (df["ROC_9_4h"] > -20.0))
      # 1d high, 4h & 1d overbought
      & ((df["AROONU_14_1d"] < 90.0) | (df["ROC_9_4h"] < 40.0) | (df["ROC_9_1d"] < 80.0))
      # 1h high, 4h overbought
      & ((df["STOCHRSIk_14_14_3_3_1h"] < 80.0) | (df["ROC_9_4h"] < 80.0))
      # 4h high, 1h downtrend
      & ((df["STOCHRSIk_14_14_3_3_4h"] < 70.0) | (df["ROC_9_1h"] > -15.0))
      # 4h high, 1d downtrend
      & ((df["STOCHRSIk_14_14_3_3_4h"] < 70.0) | (df["ROC_9_1d"] > -40.0))
      # 5m down move, 15m still not low enough, 1h high
      & ((df["ROC_2"] > -10.0) | (df["AROONU_14_15m"] < 30.0) | (df["AROONU_14_1h"] < 80.0))
      # 5m down move, 15m still high
      & ((df["ROC_2"] > -10.0) | (df["AROONU_14_15m"] < 50.0))
      # 5m down move, 15m & 1h down move, 15m still high
      & (
        (df["ROC_9"] > -15.0) | (df["RSI_3_15m"] > 5.0) | (df["RSI_3_1h"] > 35.0) | (df["AROONU_14_15m"] < 50.0)
      )
      # 5m down move, 4h down move, 15m downtrend, 1h high
      & (
        (df["ROC_9"] > -15.0) | (df["RSI_3_4h"] > 45.0) | (df["CMF_20_15m"] > -0.3) | (df["AROONU_14_1h"] < 60.0)
      )
      # 1h downtrend, 4h high & overbought
      & ((df["ROC_9_1h"] > -25.0) | (df["AROONU_14_4h"] < 80.0) | (df["ROC_9_4h"] < 80.0))
      # 1h & 4h overbought, 1d downtrend
      & ((df["ROC_9_1h"] < 20.0) | (df["ROC_9_4h"] < 20.0) | (df["ROC_9_1d"] > -40.0))
      # 1d P&D, 1d downtrend
      & ((df["change_pct_1d"] > -5.0) | (df["change_pct_1d"].shift(288) < 30.0) | (df["CMF_20_1d"] > -0.0))
      # 1d green with top wick, 1h down move
      & ((df["change_pct_1d"] < 20.0) | (df["top_wick_pct_1d"] < 15.0) | (df["RSI_3_1h"] > 20.0))
      # 1d green with top wick, 4h high
      & ((df["change_pct_1d"] < 25.0) | (df["top_wick_pct_1d"] < 25.0) | (df["AROONU_14_4h"] < 80.0))
      # 1d green, 1h down move, 1d downtrend
      & ((df["change_pct_1d"] < 40.0) | (df["RSI_3_1h"] > 25.0) | (df["CMF_20_1d"] > -0.2))
      # 1d green with top wick, 4h overbought
      & ((df["change_pct_1d"] < 50.0) | (df["top_wick_pct_1d"] < 30.0) | (df["ROC_9_4h"] < 80.0))
      # big drop in the last hour, 15m downtrend
      & ((df["close"] > (df["close_max_12"] * 0.65)) | (df["CMF_20_15m"] > -0.5))
      # big drop in the last 6 hours, 1h down move, 1h high
      & ((df["close"] > (df["high_max_6_1h"] * 0.60)) | (df["RSI_3_1h"] > 20.0) | (df["AROONU_14_1h"] < 60.0))
      # big drop in the last 24 hours,  1h still high
      & ((df["close"] > (df["high_max_24_1h"] * 0.40)) | (df["STOCHRSIk_14_14_3_3_1h"] < 45.0))
      # big drop in the last 4 days, 1h high
      & ((df["close"] > (df["high_max_24_4h"] * 0.20)) | (df["AROONU_14_1h"] < 70.0))
      # big drop in the last 20 days, 1d high, 1d downtrend
      & (
        (df["close"] > (df["high_max_20_1d"] * 0.20))
        | (df["STOCHRSIk_14_14_3_3_1d"] < 70.0)
        | (df["ROC_9_1d"] > -15.0)
      )
    )

    # Logic
    long_entry_logic.append(
      (df["EMA_26"] > df["EMA_12"])
      & ((df["EMA_26"] - df["EMA_12"]) > (df["open"] * 0.034))
      & ((df["EMA_26"].shift() - df["EMA_12"].shift()) > (df["open"] / 100.0))
      & (df["close"] < (df["BBL_20_2.0"] * 0.999))
    )


def append_long_2(df, long_entry_logic, allowed_empty_candles_288) -> None:
    """Append NFI long condition #2, the normal-mode long entry."""
    # Protections
    long_entry_logic.append(df["num_empty_288"] <= allowed_empty_candles_288)
    long_entry_logic.append(df["protections_long_global"] == True)

    long_entry_logic.append(
      # 5m & 1h down move, 1h still not low enough
      ((df["RSI_3"] > 3.0) | (df["RSI_3_1h"] > 10.0) | (df["AROONU_14_1h"] < 30.0))
      # 5m & 1h down move, 1d high
      & ((df["RSI_3"] > 3.0) | (df["RSI_3_1h"] > 20.0) | (df["AROONU_14_1d"] < 100.0))
      # 5m & 1h down move, 1h still high
      & ((df["RSI_3"] > 3.0) | (df["RSI_3_1h"] > 30.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 50.0))
      # 5m & 1h down move, 1d high
      & ((df["RSI_3"] > 3.0) | (df["RSI_3_1h"] > 35.0) | (df["AROONU_14_1d"] < 100.0))
      # 5m & 4h down move, 15m still not low enough
      & ((df["RSI_3"] > 3.0) | (df["RSI_3_4h"] > 3.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 30.0))
      # 5m & 4h down move, 1d downtrend
      & ((df["RSI_3"] > 3.0) | (df["RSI_3_4h"] > 15.0) | (df["ROC_9_1d"] > -30.0))
      # 5m & 4h down move, 4h high
      & ((df["RSI_3"] > 3.0) | (df["RSI_3_4h"] > 45.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 80.0))
      # 5m & 4h down move, 15m still high
      & ((df["RSI_3"] > 5.0) | (df["RSI_3_4h"] > 25.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 50.0))
      # 5m & 1d down move, 1h still high
      & ((df["RSI_3"] > 3.0) | (df["RSI_3_1d"] > 10.0) | (df["AROONU_14_1h"] < 40.0))
      # 5m & 1d down move, 1h still high
      & ((df["RSI_3"] > 3.0) | (df["RSI_3_1d"] > 10.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 50.0))
      # 5m & 1d down move, 1d downtrend
      & ((df["RSI_3"] > 3.0) | (df["RSI_3_1d"] > 15.0) | (df["CMF_20_1d"] > -0.25))
      # 5m & 1d down move, 15m still high
      & ((df["RSI_3"] > 3.0) | (df["RSI_3_1d"] > 20.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 40.0))
      # 5m down move, 1h high
      & ((df["RSI_3"] > 3.0) | (df["AROONU_14_1h"] < 80.0))
      # 5m down move, 4h high, 1d overbought
      & ((df["RSI_3"] > 3.0) | (df["AROONU_14_4h"] < 80.0) | (df["ROC_9_1d"] < 30.0))
      # 5m down move, 4h high & overbought
      & ((df["RSI_3"] > 3.0) | (df["AROONU_14_4h"] < 100.0) | (df["ROC_9_4h"] < 20.0))
      # 5m down move, 4h & 1d overbought
      & ((df["RSI_3"] > 3.0) | (df["ROC_9_4h"] < 20.0) | (df["ROC_9_1d"] < 40.0))
      # 5m down move, 1d downtrend
      & ((df["RSI_3"] > 3.0) | (df["ROC_9_1d"] > -40.0))
      # 5m & 15m down move, 15m still high
      & ((df["RSI_3"] > 5.0) | (df["RSI_3_15m"] > 10.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 40.0))
      # 5m & 15m down move, 1h high
      & ((df["RSI_3"] > 5.0) | (df["RSI_3_15m"] > 30.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 80.0))
      # 5m & 4h down move, 1d downtrend
      & ((df["RSI_3"] > 5.0) | (df["RSI_3_4h"] > 10.0) | (df["ROC_9_1d"] > -20.0))
      # 5m & 4h down move, 4h still not low enough
      & ((df["RSI_3"] > 5.0) | (df["RSI_3_4h"] > 15.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 20.0))
      # 5m down move, 4h high, 1h overbought
      & ((df["RSI_3"] > 10.0) | (df["AROONU_14_4h"] < 100.0) | (df["ROC_9_1h"] < 30.0))
      # 15m & 1h down move, 1h still high
      & ((df["RSI_3_15m"] > 1.0) | (df["RSI_3_1h"] > 25.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 40.0))
      # 15m & 1h & 4h down move
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_1h"] > 3.0) | (df["RSI_3_4h"] > 15.0))
      # 15m & 1h down move, 4h still high
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_1h"] > 3.0) | (df["AROONU_14_4h"] < 50.0))
      # 15m & 1h down move, 15m downtrend
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_1h"] > 5.0) | (df["CMF_20_15m"] > -0.30))
      # 15m & 1h down move, 15m still not low enough
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_1h"] > 5.0) | (df["AROONU_14_15m"] < 30.0))
      # 15m & 1h down move, 1h still not low enough
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_1h"] > 5.0) | (df["AROONU_14_1h"] < 25.0))
      # 15m & 1h down move, 1h still not low enough
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_1h"] > 5.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 30.0))
      # 15m & 1h & 4h down move
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_1h"] > 10.0) | (df["RSI_3_4h"] > 10.0))
      # 15m & 1h down move, 1h high
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_1h"] > 10.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 30.0))
      # 15m & 1h down move, 1d downtrend
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_1h"] > 10.0) | (df["ROC_9_1d"] > -40.0))
      # 15m & 1h down move, 15m downtrend
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_1h"] > 15.0) | (df["CMF_20_15m"] > -0.40))
      # 15m & 1h down move, 4h still high
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_1h"] > 15.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 50.0))
      # 15m & 1h down move, 1h high
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_1h"] > 20.0) | (df["AROONU_14_1h"] < 70.0))
      # 15m & 1h down move, 1h still high
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_1h"] > 20.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 50.0))
      # 15m & 1h down move, 4h high
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_1h"] > 20.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 60.0))
      # 15m & 1h down move, 1h high
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_1h"] > 30.0) | (df["AROONU_14_1h"] < 60.0))
      # 15m & 1h down move, 1h high
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_1h"] > 30.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 70.0))
      # 15m & 1h down move, 1h still high
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_1h"] > 35.0) | (df["AROONU_14_1h"] < 40.0))
      # 15m & 1h down move, 1d high
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_1h"] > 35.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 70.0))
      # 15m & 1h down move, 1h high
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_1h"] > 40.0) | (df["AROONU_14_1h"] < 70.0))
      # 15m & 1h down move, 4h high
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_1h"] > 40.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 80.0))
      # 15m & 1h down move, 1h high
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_1h"] > 45.0) | (df["AROONU_14_1h"] < 85.0))
      # 15m & 1h down move, 1h high
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_1h"] > 60.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 80.0))
      # 15m & 4h down move, 4h downtrend
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_4h"] > 5.0) | (df["CMF_20_4h"] > -0.35))
      # 15m & 4h down move, 1d high
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_4h"] > 10.0) | (df["AROONU_14_1d"] < 80.0))
      # 15m & 4h down move, 1d downtrend
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_4h"] > 10.0) | (df["ROC_9_1d"] > -20.0))
      # 15m & 4h down move, 4h still high
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_4h"] > 30.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 40.0))
      # 15m & 4h down move, 4h still high
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_4h"] > 35.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 50.0))
      # 15m down move, 15m still not low enough, 1h high
      & ((df["RSI_3_15m"] > 3.0) | (df["AROONU_14_15m"] < 20.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 60.0))
      # 15m down move, 15m still not low enough, 1h still high
      & ((df["RSI_3_15m"] > 3.0) | (df["AROONU_14_15m"] < 30.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 50.0))
      # 15m down move, 1h high, 1d overbought
      & ((df["RSI_3_15m"] > 3.0) | (df["AROONU_14_1h"] < 70.0) | (df["ROC_9_1d"] < 20.0))
      # 15m down move, 4h still high, 15m downtrend
      & ((df["RSI_3_15m"] > 3.0) | (df["AROONU_14_4h"] < 40.0) | (df["CMF_20_15m"] > -0.35))
      # 15m down move, 4h high, 1d overbought
      & ((df["RSI_3_15m"] > 3.0) | (df["AROONU_14_4h"] < 70.0) | (df["ROC_9_1d"] < 30.0))
      # 15m down move, 4h & 1d downtrend
      & ((df["RSI_3_15m"] > 3.0) | (df["ROC_9_4h"] > -30.0) | (df["ROC_9_1d"] > -50.0))
      # 15m & 1h & 4h down move
      & ((df["RSI_3_15m"] > 5.0) | (df["RSI_3_1h"] > 5.0) | (df["RSI_3_4h"] > 10.0))
      # 15m & 1h down move, 4h still high
      & ((df["RSI_3_15m"] > 5.0) | (df["RSI_3_1h"] > 10.0) | (df["RSI_14_4h"] < 40.0))
      # 15m & 1h down move, 1h still high
      & ((df["RSI_3_15m"] > 5.0) | (df["RSI_3_1h"] > 10.0) | (df["AROONU_14_1h"] < 40.0))
      # 15m & 1h down move, 4h high
      & ((df["RSI_3_15m"] > 5.0) | (df["RSI_3_1h"] > 10.0) | (df["AROONU_14_4h"] < 100.0))
      # 15m & 1h down move, 4h high
      & ((df["RSI_3_15m"] > 5.0) | (df["RSI_3_1h"] > 15.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 60.0))
      # 15m & 1h down move, 1h high
      & ((df["RSI_3_15m"] > 5.0) | (df["RSI_3_1h"] > 40.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 80.0))
      # 15m & 1h down move, 1h high
      & ((df["RSI_3_15m"] > 5.0) | (df["RSI_3_1h"] > 45.0) | (df["AROONU_14_1h"] < 80.0))
      # 15m & 4h down move, 1d still high
      & ((df["RSI_3_15m"] > 5.0) | (df["RSI_3_4h"] > 5.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 40.0))
      # 15m & 4h down move, 15m still not low enough
      & ((df["RSI_3_15m"] > 5.0) | (df["RSI_3_4h"] > 10.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 30.0))
      # 15m & 4h down move, 1d high
      & ((df["RSI_3_15m"] > 5.0) | (df["RSI_3_4h"] > 10.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 70.0))
      # 15m & 4h down move, 15m still high
      & ((df["RSI_3_15m"] > 5.0) | (df["RSI_3_4h"] > 15.0) | (df["AROONU_14_15m"] < 40.0))
      # 15m & 4h down move, 1h still high
      & ((df["RSI_3_15m"] > 5.0) | (df["RSI_3_4h"] > 15.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 50.0))
      # 15m & 4h down move, 4h still high
      & ((df["RSI_3_15m"] > 5.0) | (df["RSI_3_4h"] > 15.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 50.0))
      # 15m & 4h down move, 1d overbought
      & ((df["RSI_3_15m"] > 5.0) | (df["RSI_3_4h"] > 20.0) | (df["ROC_9_1d"] < 10.0))
      # 15m & 4h down move, 4h still high
      & ((df["RSI_3_15m"] > 5.0) | (df["RSI_3_4h"] > 45.0) | (df["AROONU_14_4h"] < 40.0))
      # 15m & 1d down move, 15m still not low enough
      & ((df["RSI_3_15m"] > 5.0) | (df["RSI_3_1d"] > 10.0) | (df["AROONU_14_15m"] < 30.0))
      # 15m & 1d down move, 1h high
      & ((df["RSI_3_15m"] > 5.0) | (df["RSI_3_1d"] > 40.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 90.0))
      # 15m down move, 15m downtrend, 4h still not low enough
      & ((df["RSI_3_15m"] > 5.0) | (df["CMF_20_15m"] > -0.30) | (df["STOCHRSIk_14_14_3_3_4h"] < 30.0))
      # 15m down move, 15m still not low enough, 4h high
      & ((df["RSI_3_15m"] > 5.0) | (df["AROONU_14_15m"] < 20.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 70.0))
      # 15m down move, 15m stil high, 1h still high
      & ((df["RSI_3_15m"] > 5.0) | (df["AROONU_14_15m"] < 40.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 50.0))
      # 15m down move, 1d high & overbought
      & ((df["RSI_3_15m"] > 5.0) | (df["AROONU_14_1d"] < 80.0) | (df["ROC_9_1d"] < 20.0))
      # 15m down move, 15m still not low enough, 1h still high
      & (
        (df["RSI_3_15m"] > 5.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 20.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 50.0)
      )
      # 15m down move, 1h still high, 4h overbought
      & ((df["RSI_3_15m"] > 5.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 50.0) | (df["ROC_9_4h"] < 30.0))
      # 15m down move, 1h high & overbought
      & ((df["RSI_3_15m"] > 5.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 80.0) | (df["ROC_9_1h"] < 20.0))
      # 15m & 1h down move, 15m high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1h"] > 10.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 50.0))
      # 15m & 1h down move, 1h still high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1h"] > 10.0) | (df["AROONU_14_1h"] < 50.0))
      # 15m & 1h down move, 4h high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1h"] > 10.0) | (df["AROONU_14_4h"] < 60.0))
      # 15m & 1h down move, 1d high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1h"] > 10.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 70.0))
      # 15m & 1h down move, 1h high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1h"] > 15.0) | (df["AROONU_14_1h"] < 80.0))
      # 15m & 1h down move, 4h high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1h"] > 20.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 70.0))
      # 15m & 1h down move, 4h high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1h"] > 25.0) | (df["AROONU_14_4h"] < 75.0))
      # 15m & 1h down move, 4h still high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1h"] > 25.0) | (df["AROONU_14_4h"] < 50.0))
      # 15m & 1h down move, 1d downtrend
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1h"] > 25.0) | (df["ROC_9_1d"] > -50.0))
      # 15m & 1h down move, 1d overbought
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1h"] > 30.0) | (df["ROC_9_1d"] < 30.0))
      # 15m & 1h down move, 4h still high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1h"] > 35.0) | (df["RSI_14_4h"] < 50.0))
      # 15m & 1h down move, 1h high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1h"] > 35.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 60.0))
      # 15m & 1h down move, 4h high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1h"] > 40.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 80.0))
      # 15m & 1h down move, 1h high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1h"] > 50.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 70.0))
      # 15m & 1h down move, 4h high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1h"] > 50.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 80.0))
      # 16m & 1h down move, 1h high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1h"] > 55.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 70.0))
      # 15m & 1h down move, 4h high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1h"] > 55.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 90.0))
      # 15m & 1h down move, 1h high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1h"] > 40.0) | (df["AROONU_14_1h"] < 70.0))
      # 15m & 4h down move, 4h still not low enough
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_4h"] > 10.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 30.0))
      # 15m & 4h down move, 1d high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_4h"] > 10.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 80.0))
      # 15m & 4h down move, 1d overbought
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_4h"] > 10.0) | (df["ROC_9_1d"] < 20.0))
      # 15m & 4h down move, 4h still not low enough
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_4h"] > 20.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 30.0))
      # 15m & 4h down move, 1d high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_4h"] > 30.0) | (df["AROONU_14_1d"] < 90.0))
      # 15m & 4h down move, 1d high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_4h"] > 30.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 90.0))
      # 15m & 4h down move, 1d overbought
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_4h"] > 30.0) | (df["ROC_9_1d"] < 30.0))
      # 15m & 4h down move, 4h overbought
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_4h"] > 55.0) | (df["ROC_9_4h"] < 50.0))
      # 15m & 1d down move, 1d still high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1d"] > 10.0) | (df["RSI_14_1d"] < 40.0))
      # 15m & 1d down move, 1h high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1d"] > 10.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 90.0))
      # 15m & 1d down move, 4h high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1d"] > 15.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 90.0))
      # 15m down move, 15m downtrend, 1h high
      & ((df["RSI_3_15m"] > 10.0) | (df["CMF_20_15m"] > -0.40) | (df["AROONU_14_1h"] < 80.0))
      # 15m down move, 1h high, 1d overbought
      & ((df["RSI_3_15m"] > 10.0) | (df["AROONU_14_1h"] < 80.0) | (df["ROC_9_1d"] < 20.0))
      # 15m down move, 4h & 1d high
      & ((df["RSI_3_15m"] > 10.0) | (df["AROONU_14_4h"] < 70.0) | (df["AROONU_14_1d"] < 100.0))
      # 15m down move, 4h high & overbought
      & ((df["RSI_3_15m"] > 10.0) | (df["AROONU_14_4h"] < 70.0) | (df["ROC_9_4h"] < 10.0))
      # 15m down move, 15m still not low enough, 4h high
      & ((df["RSI_3_15m"] > 10.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 20.0) | (df["AROONU_14_4h"] < 70.0))
      # 15m down move, 15m sill high, 4h high
      & ((df["RSI_3_15m"] > 10.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 40.0) | (df["AROONU_14_4h"] < 60.0))
      # 15m down move, 4h high, 1d downtrend
      & ((df["RSI_3_15m"] > 10.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 80.0) | (df["ROC_9_1d"] > -30.0))
      # 15m & 1h down move, 4h downtrend
      & ((df["RSI_3_15m"] > 15.0) | (df["RSI_3_1h"] > 15.0) | (df["ROC_9_4h"] > -20.0))
      # 15m & 1h down move, 1h downtrend
      & ((df["RSI_3_15m"] > 15.0) | (df["RSI_3_1h"] > 20.0) | (df["CMF_20_1h"] > -0.30))
      # 15m & 1h down move, 1d overbought
      & ((df["RSI_3_15m"] > 15.0) | (df["RSI_3_1h"] > 25.0) | (df["ROC_9_1d"] < 100.0))
      # 15m & 1h down move, 4h high
      & ((df["RSI_3_15m"] > 15.0) | (df["RSI_3_1h"] > 30.0) | (df["AROONU_14_4h"] < 80.0))
      # 15m & 1h down move, 1h high
      & ((df["RSI_3_15m"] > 15.0) | (df["RSI_3_1h"] > 40.0) | (df["AROONU_14_1h"] < 70.0))
      # 15m & 1h down move, 1d high
      & ((df["RSI_3_15m"] > 15.0) | (df["RSI_3_1h"] > 40.0) | (df["AROONU_14_1d"] < 90.0))
      # 15m & 1h down move, 4h high
      & ((df["RSI_3_15m"] > 15.0) | (df["RSI_3_1h"] > 45.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 70.0))
      # 15m & 4h down move, 1h high
      & ((df["RSI_3_15m"] > 15.0) | (df["RSI_3_4h"] > 15.0) | (df["AROONU_14_1h"] < 70.0))
      # 15m & 4h down move, 4h downtrend
      & ((df["RSI_3_15m"] > 15.0) | (df["RSI_3_4h"] > 15.0) | (df["ROC_9_4h"] > -20.0))
      # 15m & 4h down move, 1d high
      & ((df["RSI_3_15m"] > 15.0) | (df["RSI_3_4h"] > 20.0) | (df["AROONU_14_1d"] < 90.0))
      # 15m & 1d down move, 1h still high
      & ((df["RSI_3_15m"] > 15.0) | (df["RSI_3_1d"] > 15.0) | (df["AROONU_14_1h"] < 40.0))
      # 15m & 1d down move, 4h high
      & ((df["RSI_3_15m"] > 15.0) | (df["RSI_3_1d"] > 30.0) | (df["AROONU_14_4h"] < 90.0))
      # 15m down move, 15m still not low enough, 4h high
      & ((df["RSI_3_15m"] > 15.0) | (df["AROONU_14_15m"] < 25.0) | (df["AROONU_14_4h"] < 60.0))
      # 15m down move, 15m still not low enough, 1h high
      & ((df["RSI_3_15m"] > 15.0) | (df["AROONU_14_15m"] < 30.0) | (df["AROONU_14_1h"] < 70.0))
      # 15m down move, 15m & 4h still high
      & ((df["RSI_3_15m"] > 15.0) | (df["AROONU_14_15m"] < 40.0) | (df["AROONU_14_4h"] < 40.0))
      # 15m down move, 1h still high, 4h overbought
      & ((df["RSI_3_15m"] > 15.0) | (df["AROONU_14_1h"] < 50.0) | (df["ROC_9_4h"] < 60.0))
      # 15m down move, 1h & 4h high
      & ((df["RSI_3_15m"] > 15.0) | (df["AROONU_14_1h"] < 60.0) | (df["AROONU_14_4h"] < 90.0))
      # 15m down move, 1h & 1d high
      & ((df["RSI_3_15m"] > 15.0) | (df["AROONU_14_1h"] < 70.0) | (df["AROONU_14_1d"] < 90.0))
      # 15m down move, 4h high, 4h downtrend
      & ((df["RSI_3_15m"] > 15.0) | (df["AROONU_14_4h"] < 60.0) | (df["ROC_9_4h"] > -20.0))
      # 15m down move, 4h & 1d high
      & ((df["RSI_3_15m"] > 15.0) | (df["AROONU_14_4h"] < 75.0) | (df["AROONU_14_1d"] < 100.0))
      # 15m down move, 15m still high, 1d overbought
      & ((df["RSI_3_15m"] > 15.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 50.0) | (df["ROC_9_1d"] < 100.0))
      # 15m down move, 1h high & overbought
      & ((df["RSI_3_15m"] > 15.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 90.0) | (df["ROC_9_1h"] < 10.0))
      # 15m down move, 4h high, 1d overbought
      & ((df["RSI_3_15m"] > 15.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 70.0) | (df["ROC_9_1d"] < 10.0))
      # 15m & 1h down move, 15m still not low enough
      & ((df["RSI_3_15m"] > 20.0) | (df["RSI_3_1h"] > 20.0) | (df["AROONU_14_15m"] < 30.0))
      # 15m & 1h down move, 4h overbought
      & ((df["RSI_3_15m"] > 20.0) | (df["RSI_3_1h"] > 20.0) | (df["ROC_9_4h"] < 50.0))
      # 15m & 1h down move, 15m high
      & ((df["RSI_3_15m"] > 20.0) | (df["RSI_3_1h"] > 25.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 80.0))
      # 15m & 1h down move, 4h high
      & ((df["RSI_3_15m"] > 20.0) | (df["RSI_3_1h"] > 25.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 80.0))
      # 15m & 1h down move, 1h high
      & ((df["RSI_3_15m"] > 20.0) | (df["RSI_3_1h"] > 30.0) | (df["AROONU_14_1h"] < 70.0))
      # 15m & 1h down move, 1h high
      & ((df["RSI_3_15m"] > 20.0) | (df["RSI_3_1h"] > 45.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 80.0))
      # 15m & 4h down move, 1h high
      & ((df["RSI_3_15m"] > 20.0) | (df["RSI_3_4h"] > 20.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 80.0))
      # 15m & 4h down move, 4h high
      & ((df["RSI_3_15m"] > 20.0) | (df["RSI_3_4h"] > 40.0) | (df["AROONU_14_4h"] < 80.0))
      # 15m down move, 1h & 4h high
      & ((df["RSI_3_15m"] > 20.0) | (df["AROONU_14_1h"] < 80.0) | (df["AROONU_14_4h"] < 80.0))
      # 15m down move, 1h & 1d high
      & ((df["RSI_3_15m"] > 20.0) | (df["AROONU_14_1h"] < 80.0) | (df["AROONU_14_1d"] < 80.0))
      # 15m down move, 1h high, 1d downtrend
      & ((df["RSI_3_15m"] > 20.0) | (df["AROONU_14_1h"] < 90.0) | (df["ROC_9_1d"] > -30.0))
      # 15m down move, 1h high, 1d overbought
      & ((df["RSI_3_15m"] > 20.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 70.0) | (df["ROC_9_1d"] < 100.0))
      # 15m down move, 1h high, 1d downtrend
      & ((df["RSI_3_15m"] > 20.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 80.0) | (df["ROC_9_1d"] > -20.0))
      # 15m down move, 1h high & overbought
      & ((df["RSI_3_15m"] > 20.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 90.0) | (df["ROC_9_1h"] < 10.0))
      # 15m & 4h down move, 1h overbought
      & ((df["RSI_3_15m"] > 25.0) | (df["RSI_3_4h"] > 35.0) | (df["ROC_9_1h"] < 100.0))
      # 15m down move, 15m still not low enough, 1h high
      & ((df["RSI_3_15m"] > 25.0) | (df["AROONU_14_15m"] < 20.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 90.0))
      # 15m down move, 1h & 4h high
      & ((df["RSI_3_15m"] > 25.0) | (df["AROONU_14_1h"] < 70.0) | (df["AROONU_14_4h"] < 100.0))
      # 15m down move, 1h high, 1d overbought
      & ((df["RSI_3_15m"] > 25.0) | (df["AROONU_14_1h"] < 70.0) | (df["ROC_9_1d"] < 50.0))
      # 15m down move, 4h high, 1d overbought
      & ((df["RSI_3_15m"] > 25.0) | (df["AROONU_14_4h"] < 70.0) | (df["ROC_9_1d"] < 50.0))
      # 15m down move, 4h high & overbought
      & ((df["RSI_3_15m"] > 30.0) | (df["AROONU_14_4h"] < 70.0) | (df["ROC_9_4h"] < 50.0))
      # 15m down move, 1h high, 1d downtrend
      & ((df["RSI_3_15m"] > 30.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 80.0) | (df["ROC_9_1d"] > -20.0))
      # 15m down move, 4h high & overbought
      & ((df["RSI_3_15m"] > 30.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 80.0) | (df["ROC_9_4h"] < 30.0))
      # 15m down move, 1h high, 4h overbought
      & ((df["RSI_3_15m"] > 35.0) | (df["AROONU_14_1h"] < 80.0) | (df["ROC_9_4h"] < 80.0))
      # 15m down move, 4h high & overbought
      & ((df["RSI_3_15m"] > 35.0) | (df["AROONU_14_4h"] < 90.0) | (df["ROC_9_4h"] < 50.0))
      # 15m down move, 4h high, 1d overbought
      & ((df["RSI_3_15m"] > 35.0) | (df["AROONU_14_4h"] < 100.0) | (df["ROC_9_1h"] < 20.0))
      # 15m down move, 1h high, 1d overbought
      & ((df["RSI_3_15m"] > 35.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 80.0) | (df["ROC_9_1d"] < 80.0))
      # 15m down move, 4h high & overbought
      & ((df["RSI_3_15m"] > 40.0) | (df["AROONU_14_4h"] < 100.0) | (df["ROC_9_4h"] < 40.0))
      # 1h & 4h down move, 1d downtrend
      & ((df["RSI_3_1h"] > 1.0) | (df["RSI_3_4h"] > 15.0) | (df["ROC_9_1d"] > -10.0))
      # 1h down move, 15m downtrend, 1h still high
      & ((df["RSI_3_1h"] > 3.0) | (df["CMF_20_15m"] > -0.40) | (df["AROONU_14_1h"] < 40.0))
      # 1h & 4h down move, 15m downtrend
      & ((df["RSI_3_1h"] > 3.0) | (df["RSI_3_4h"] > 3.0) | (df["ROC_9_15m"] > -30.0))
      # 1h & 4h down move, 4h still high
      & ((df["RSI_3_1h"] > 3.0) | (df["RSI_3_4h"] > 5.0) | (df["AROONU_14_4h"] < 40.0))
      # 1h & 4h down move, 4h still high
      & ((df["RSI_3_1h"] > 3.0) | (df["RSI_3_4h"] > 15.0) | (df["RSI_14_4h"] < 40.0))
      # 1h & 4h down move, 1h still not low enough
      & ((df["RSI_3_1h"] > 3.0) | (df["RSI_3_4h"] > 20.0) | (df["AROONU_14_1h"] < 20.0))
      # 1h & 4h down move, 1d high
      & ((df["RSI_3_1h"] > 3.0) | (df["RSI_3_4h"] > 20.0) | (df["AROONU_14_1d"] < 80.0))
      # 1h & 4h down move, 1d overbought
      & ((df["RSI_3_1h"] > 3.0) | (df["RSI_3_4h"] > 25.0) | (df["ROC_9_1d"] < 10.0))
      # 1h & 4h down move, 4h high
      & ((df["RSI_3_1h"] > 3.0) | (df["RSI_3_4h"] > 50.0) | (df["AROONU_14_4h"] < 70.0))
      # 1h & 1d down move, 15m still high
      & ((df["RSI_3_1h"] > 3.0) | (df["RSI_3_1d"] > 10.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 50.0))
      # 1h & 4h down move, 4h high
      & ((df["RSI_3_1h"] > 5.0) | (df["RSI_3_4h"] > 5.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 40.0))
      # 1h & 4h down move, 1d still high
      & ((df["RSI_3_1h"] > 5.0) | (df["RSI_3_4h"] > 5.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 50.0))
      # 1h & 4h down move, 1d downtrend
      & ((df["RSI_3_1h"] > 5.0) | (df["RSI_3_4h"] > 5.0) | (df["ROC_9_1d"] > -30.0))
      # 1h % 4h down move, 4h downtrend
      & ((df["RSI_3_1h"] > 5.0) | (df["RSI_3_4h"] > 10.0) | (df["CMF_20_4h"] > -0.30))
      # 1h & 4h down move, 4h still high
      & ((df["RSI_3_1h"] > 5.0) | (df["RSI_3_4h"] > 60.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 50.0))
      # 1h & 4h down move, 15m high
      & ((df["RSI_3_1h"] > 5.0) | (df["RSI_3_4h"] > 10.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 70.0))
      # 1h & 4h down move, 1h still high
      & ((df["RSI_3_1h"] > 5.0) | (df["RSI_3_4h"] > 15.0) | (df["AROONU_14_1h"] < 50.0))
      # 1h & 4h down move, 4h downtrend
      & ((df["RSI_3_1h"] > 5.0) | (df["RSI_3_4h"] > 15.0) | (df["ROC_9_4h"] > -30.0))
      # 1h down move, 4h still high, 1d downtrend
      & ((df["RSI_3_1h"] > 5.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 50.0) | (df["ROC_9_1d"] > -50.0))
      # 1h & 4h & 1d down move
      & ((df["RSI_3_1h"] > 10.0) | (df["RSI_3_4h"] > 10.0) | (df["RSI_3_1d"] > 15.0))
      # 1h & 4h down move, 1d still high
      & ((df["RSI_3_1h"] > 10.0) | (df["RSI_3_4h"] > 10.0) | (df["AROONU_14_1d"] < 40.0))
      # 1h & 4h down move, 1h still not low enough
      & ((df["RSI_3_1h"] > 10.0) | (df["RSI_3_4h"] > 10.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 20.0))
      # 1h & 4h down move, 1d downtrend
      & ((df["RSI_3_1h"] > 10.0) | (df["RSI_3_4h"] > 10.0) | (df["ROC_9_1d"] > -20.0))
      # 1h & 4h down move, 15m high
      & ((df["RSI_3_1h"] > 10.0) | (df["RSI_3_4h"] > 15.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 70.0))
      # 1h & 4h down move, 1d downtrend
      & ((df["RSI_3_1h"] > 10.0) | (df["RSI_3_4h"] > 15.0) | (df["ROC_9_1d"] > -40.0))
      # 1h & 4h down move, 4h still high
      & ((df["RSI_3_1h"] > 10.0) | (df["RSI_3_4h"] > 30.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 50.0))
      # 1h & 1d down move, 15m still high
      & ((df["RSI_3_1h"] > 10.0) | (df["RSI_3_1d"] > 15.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 40.0))
      # 1h & 4h down move, 4h still high
      & ((df["RSI_3_1h"] > 10.0) | (df["RSI_3_4h"] > 35.0) | (df["RSI_14_4h"] < 40.0))
      # 1h down move, 1h still not low enough 1d overbought
      & ((df["RSI_3_1h"] > 10.0) | (df["AROONU_14_1h"] < 30.0) | (df["ROC_9_1d"] < 100.0))
      # 1h & 4h down move, 1d high
      & ((df["RSI_3_1h"] > 15.0) | (df["RSI_3_4h"] > 15.0) | (df["RSI_14_1d"] < 60.0))
      # 1h & 4h down move, 1h still not low enough
      & ((df["RSI_3_1h"] > 15.0) | (df["RSI_3_4h"] > 15.0) | (df["AROONU_14_1h"] < 20.0))
      # 1h & 4h down move, 15m still high
      & ((df["RSI_3_1h"] > 15.0) | (df["RSI_3_4h"] > 15.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 50.0))
      # 1h & 4h down move, 4h downtrend
      & ((df["RSI_3_1h"] > 15.0) | (df["RSI_3_4h"] > 15.0) | (df["ROC_9_4h"] > -20.0))
      # 1h & 4h down move, 4h still high
      & ((df["RSI_3_1h"] > 15.0) | (df["RSI_3_4h"] > 20.0) | (df["RSI_14_4h"] < 40.0))
      # 1h & 4h down move, 4h still not low enough
      & ((df["RSI_3_1h"] > 15.0) | (df["RSI_3_4h"] > 25.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 30.0))
      # 1h & 4h down move, 1d high
      & ((df["RSI_3_1h"] > 15.0) | (df["RSI_3_4h"] > 30.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 80.0))
      # 1h & 4h down move, 4h downtrend
      & ((df["RSI_3_1h"] > 15.0) | (df["RSI_3_4h"] > 30.0) | (df["ROC_9_4h"] > -30.0))
      # 1h & 4h down move, 4h high
      & ((df["RSI_3_1h"] > 15.0) | (df["RSI_3_4h"] > 40.0) | (df["AROONU_14_4h"] < 70.0))
      # 1h & 4h down move, 4h still high
      & ((df["RSI_3_1h"] > 15.0) | (df["RSI_3_4h"] > 40.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 50.0))
      # 1h & 1d down move, 1d high
      & ((df["RSI_3_1h"] > 15.0) | (df["RSI_3_1d"] > 25.0) | (df["AROONU_14_1d"] < 80.0))
      # 1h & 1d down move, 1d overbought
      & ((df["RSI_3_1h"] > 15.0) | (df["RSI_3_1d"] > 35.0) | (df["ROC_9_1d"] < 10.0))
      # 1h down move, 1h still high, 1d downtrend
      & ((df["RSI_3_1h"] > 15.0) | (df["AROONU_14_1h"] < 40.0) | (df["ROC_9_1d"] > -40.0))
      # 1h down move, 4h high, 1d high
      & ((df["RSI_3_1h"] > 15.0) | (df["AROONU_14_4h"] < 60.0) | (df["AROONU_14_1d"] < 100.0))
      # 1h down move, 4h high, 1d overbought
      & ((df["RSI_3_1h"] > 15.0) | (df["AROONU_14_4h"] < 60.0) | (df["ROC_9_1d"] < 50.0))
      # 1h down move, 4h high & overbought
      & ((df["RSI_3_1h"] > 15.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 60.0) | (df["ROC_9_4h"] < 10.0))
      # 1h down move, 1d high & overbought
      & ((df["RSI_3_1h"] > 15.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 90.0) | (df["ROC_9_1d"] < 40.0))
      # 1h down move, 4h & 1d downtrend
      & ((df["RSI_3_1h"] > 15.0) | (df["ROC_9_4h"] > -20.0) | (df["ROC_9_1d"] > -20.0))
      # 1h & 4h down move, 1d overbought
      & ((df["RSI_3_1h"] > 20.0) | (df["RSI_3_4h"] > 20.0) | (df["ROC_9_1d"] < 20.0))
      # 1h & 4h down move, 4h still high
      & ((df["RSI_3_1h"] > 20.0) | (df["RSI_3_4h"] > 35.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 50.0))
      # 1h & 1d down move, 1h still high
      & ((df["RSI_3_1h"] > 20.0) | (df["RSI_3_1d"] > 30.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 50.0))
      # 1h down move, 1h high, 4h downtrend
      & ((df["RSI_3_1h"] > 20.0) | (df["AROONU_14_1h"] < 70.0) | (df["ROC_9_4h"] > -10.0))
      # 1h down move, 1h high, 4h overbought
      & ((df["RSI_3_1h"] > 20.0) | (df["AROONU_14_1h"] < 70.0) | (df["ROC_9_4h"] < 10.0))
      # 1h down move, 1h high, 1h still not low enough
      & ((df["RSI_3_1h"] > 20.0) | (df["AROONU_14_1d"] < 80.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 20.0))
      # 1h down move, 1d high & overbought
      & ((df["RSI_3_1h"] > 20.0) | (df["AROONU_14_1d"] < 100.0) | (df["ROC_9_1d"] < 20.0))
      # 1h down move, 1d high, 4h downtrend
      & ((df["RSI_3_1h"] > 20.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 80.0) | (df["ROC_9_4h"] > -20.0))
      # 1h & 4h down move, 4h high
      & ((df["RSI_3_1h"] > 25.0) | (df["RSI_3_4h"] > 30.0) | (df["AROONU_14_4h"] < 60.0))
      # 1h & 4h down move, 1d downtrend
      & ((df["RSI_3_1h"] > 25.0) | (df["RSI_3_4h"] > 30.0) | (df["ROC_9_1d"] > -30.0))
      # 1h down move, 1h & 4h high
      & ((df["RSI_3_1h"] > 25.0) | (df["AROONU_14_1h"] < 60.0) | (df["AROONU_14_4h"] < 90.0))
      # 1h down move, 1h high
      & ((df["RSI_3_1h"] > 25.0) | (df["AROONU_14_1h"] < 85.0))
      # 1h down move, 4h high, 4h downtrend
      & ((df["RSI_3_1h"] > 25.0) | (df["AROONU_14_4h"] < 70.0) | (df["CMF_20_4h"] > -0.50))
      # 1h down move, 1d high & overbought
      & ((df["RSI_3_1h"] > 25.0) | (df["AROONU_14_1d"] < 80.0) | (df["ROC_9_1d"] < 40.0))
      # 1h down move, 4h & 1d overbought
      & ((df["RSI_3_1h"] > 25.0) | (df["ROC_9_4h"] < 30.0) | (df["ROC_9_1d"] < 100.0))
      # 1h down move, 1h & 4h high
      & ((df["RSI_3_1h"] > 30.0) | (df["AROONU_14_1h"] < 60.0) | (df["AROONU_14_4h"] < 100.0))
      # 1h down move, 1h high, 4h overbought
      & ((df["RSI_3_1h"] > 30.0) | (df["AROONU_14_1h"] < 70.0) | (df["ROC_9_4h"] < 10.0))
      # 1h down move, 4h & 1d high
      & ((df["RSI_3_1h"] > 30.0) | (df["AROONU_14_4h"] < 80.0) | (df["AROONU_14_1d"] < 100.0))
      # 1h down move, 4h high, 1d overbought
      & ((df["RSI_3_1h"] > 30.0) | (df["AROONU_14_4h"] < 80.0) | (df["ROC_9_1d"] < 30.0))
      # 1h down move, 4h downtrend, 1d overbought
      & ((df["RSI_3_1h"] > 30.0) | (df["ROC_9_4h"] > -30.0) | (df["ROC_9_1d"] < 200.0))
      # 1h down move, 4h & 1d downtrend
      & ((df["RSI_3_1h"] > 30.0) | (df["ROC_9_4h"] > -25.0) | (df["ROC_9_1d"] > -60.0))
      # 1h & 4h down move, 1h still high
      & ((df["RSI_3_1h"] > 35.0) | (df["RSI_3_4h"] > 35.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 40.0))
      # 1h down move, 1h still high, 4h downtrend
      & ((df["RSI_3_1h"] > 35.0) | (df["AROONU_14_1h"] < 50.0) | (df["ROC_9_4h"] > -20.0))
      # 1h down move, 1h high, 1d downtrend
      & ((df["RSI_3_1h"] > 35.0) | (df["AROONU_14_1h"] < 70.0) | (df["ROC_9_1d"] > -25.0))
      # 1h down move, 4h high & overbought
      & ((df["RSI_3_1h"] > 35.0) | (df["AROONU_14_4h"] < 85.0) | (df["ROC_9_4h"] < 100.0))
      # 1h down move, 4h high, 1d overbought
      & ((df["RSI_3_1h"] > 35.0) | (df["AROONU_14_4h"] < 85.0) | (df["ROC_9_1d"] < 100.0))
      # 1h down move, 1d high, 4h overbought
      & ((df["RSI_3_1h"] > 35.0) | (df["AROONU_14_1d"] < 100.0) | (df["ROC_9_4h"] < 40.0))
      # 1h down move, 1h still high, 1d overbought
      & ((df["RSI_3_1h"] > 35.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 50.0) | (df["ROC_9_1d"] < 200.0))
      # 1h down move, 1h & 4h high
      & ((df["RSI_3_1h"] > 40.0) | (df["AROONU_14_1h"] < 70.0) | (df["AROONU_14_4h"] < 100.0))
      # 1h down move, 1h & 1d high
      & ((df["RSI_3_1h"] > 40.0) | (df["AROONU_14_1h"] < 80.0) | (df["AROONU_14_1d"] < 80.0))
      # 1h down move, 1h high, 1d overbought
      & ((df["RSI_3_1h"] > 40.0) | (df["AROONU_14_1h"] < 80.0) | (df["ROC_9_1d"] < 10.0))
      # 1h & 4h down move, 4h high
      & ((df["RSI_3_1h"] > 45.0) | (df["RSI_3_4h"] > 60.0) | (df["AROONU_14_4h"] < 100.0))
      # 1h & 4h down move, 1d overbought
      & ((df["RSI_3_1h"] > 45.0) | (df["RSI_3_4h"] > 65.0) | (df["ROC_9_1d"] < 200.0))
      # 1h down move, 1h high & overbought
      & ((df["RSI_3_1h"] > 50.0) | (df["AROONU_14_1h"] < 80.0) | (df["ROC_9_1h"] < 10.0))
      # 1h down move, 4h high, 1h overbought
      & ((df["RSI_3_1h"] > 50.0) | (df["AROONU_14_4h"] < 85.0) | (df["ROC_9_1h"] < 20.0))
      # 1h down move, 4h high, 1d downtrend
      & ((df["RSI_3_1h"] > 50.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 60.0) | (df["ROC_9_1d"] > -60.0))
      # 1h down move, 4h high & overbought
      & ((df["RSI_3_1h"] > 50.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 80.0) | (df["ROC_9_4h"] < 100.0))
      # 1h down move, 1h & 4h overbought
      & ((df["RSI_3_1h"] > 50.0) | (df["ROC_9_1h"] < 10.0) | (df["ROC_9_4h"] < 100.0))
      # 1h down move, 1h high & overbought
      & ((df["RSI_3_1h"] > 55.0) | (df["AROONU_14_1h"] < 90.0) | (df["ROC_9_1h"] < 10.0))
      # 1h down move, 4h high & overbought
      & ((df["RSI_3_1h"] > 55.0) | (df["AROONU_14_4h"] < 100.0) | (df["ROC_9_4h"] < 10.0))
      # 1h down move, 1h high & overbought
      & ((df["RSI_3_1h"] > 55.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 80.0) | (df["ROC_9_1h"] < 10.0))
      # 4h & 1d down move, 1d still high
      & ((df["RSI_3_4h"] > 3.0) | (df["RSI_3_1d"] > 15.0) | (df["AROONU_14_1d"] < 40.0))
      # 4h & 1d down move, 1d still high
      & ((df["RSI_3_4h"] > 3.0) | (df["RSI_3_1d"] > 20.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 40.0))
      # 4h & 1d down move, 1d downtrend
      & ((df["RSI_3_4h"] > 5.0) | (df["RSI_3_1d"] > 15.0) | (df["ROC_9_1d"] > -20.0))
      # 4h down move, 15m still high
      & ((df["RSI_3_4h"] > 5.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 50.0))
      # 4h & 1d down move, 1h still not low enough
      & ((df["RSI_3_4h"] > 10.0) | (df["RSI_3_1d"] > 10.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 20.0))
      # 4h & 1d down move, 1d still high
      & ((df["RSI_3_4h"] > 10.0) | (df["RSI_3_1d"] > 15.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 40.0))
      # 4h & 1d down move, 1d downtrend
      & ((df["RSI_3_4h"] > 10.0) | (df["RSI_3_1d"] > 20.0) | (df["ROC_9_1d"] > -25.0))
      # 4h & 1d down move, 1d high
      & ((df["RSI_3_4h"] > 10.0) | (df["RSI_3_1d"] > 35.0) | (df["AROONU_14_1d"] < 100.0))
      # 4h & 1d down move, 1d overbought
      & ((df["RSI_3_4h"] > 10.0) | (df["RSI_3_1d"] > 45.0) | (df["ROC_9_1d"] < 10.0))
      # 4h down move, 1d still high, 1d downtrend
      & ((df["RSI_3_4h"] > 10.0) | (df["AROONU_14_1d"] < 40.0) | (df["ROC_9_1d"] > -20.0))
      # 4h down move, 1d high & overbought
      & ((df["RSI_3_4h"] > 10.0) | (df["AROONU_14_1d"] < 90.0) | (df["ROC_9_1d"] < 40.0))
      # 4h down move, 4h still high, 1d downtrend
      & ((df["RSI_3_4h"] > 10.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 40.0) | (df["ROC_9_1d"] > -20.0))
      # 4h & 1d down move, 1d high
      & ((df["RSI_3_4h"] > 15.0) | (df["RSI_3_1d"] > 20.0) | (df["AROONU_14_1d"] < 60.0))
      # 4h down move, 4h still high, 1d downtrend
      & ((df["RSI_3_4h"] > 15.0) | (df["AROONU_14_4h"] < 50.0) | (df["ROC_9_1d"] > -20.0))
      # 4h & 1d down move, 4h still high
      & ((df["RSI_3_4h"] > 20.0) | (df["RSI_3_1d"] > 20.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 40.0))
      # 4h & 1d down move, 1d high
      & ((df["RSI_3_4h"] > 20.0) | (df["RSI_3_1d"] > 20.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 80.0))
      # 4h down move, 1h high, 1d downtrend
      & ((df["RSI_3_4h"] > 15.0) | (df["AROONU_14_1h"] < 90.0) | (df["ROC_9_1d"] > -10.0))
      # 4h down move, 4h still high, 4h downtrend
      & ((df["RSI_3_4h"] > 15.0) | (df["AROONU_14_4h"] < 50.0) | (df["ROC_9_4h"] > -20.0))
      # 4h down move, 1d high & overbought
      & ((df["RSI_3_4h"] > 20.0) | (df["AROONU_14_1d"] < 70.0) | (df["ROC_9_1d"] < 50.0))
      # 4h & 1d down move, 1d overbought
      & ((df["RSI_3_4h"] > 25.0) | (df["RSI_3_1d"] > 40.0) | (df["ROC_9_1d"] < 30.0))
      # 4h down move, 4h still high, 1d overbought
      & ((df["RSI_3_4h"] > 25.0) | (df["AROONU_14_4h"] < 40.0) | (df["ROC_9_1d"] < 100.0))
      # 4h down move, 4h still high. 4h downtrend
      & ((df["RSI_3_4h"] > 25.0) | (df["AROONU_14_4h"] < 50.0) | (df["CMF_20_4h"] > -0.40))
      # 4h down move, 4h still high, 1d downtrend
      & ((df["RSI_3_4h"] > 25.0) | (df["AROONU_14_4h"] < 50.0) | (df["ROC_9_1d"] > -40.0))
      # 4h down move, 4h high, 4h downtrend
      & ((df["RSI_3_4h"] > 25.0) | (df["AROONU_14_4h"] < 70.0) | (df["ROC_9_4h"] > -30.0))
      # 4h & 1d down move, 1d overbought
      & ((df["RSI_3_4h"] > 30.0) | (df["RSI_3_1d"] > 60.0) | (df["ROC_9_1d"] < 60.0))
      # 4h down move, 1d downtrend
      & ((df["RSI_3_4h"] > 30.0) | (df["ROC_9_1d"] > -50.0))
      # 4h down move, 4h & 1d overbought
      & ((df["RSI_3_4h"] > 35.0) | (df["ROC_9_4h"] < 30.0) | (df["ROC_9_1d"] < 200.0))
      # 4h down move, 1h high, 1d overbought
      & ((df["RSI_3_4h"] > 40.0) | (df["AROONU_14_1h"] < 70.0) | (df["ROC_9_1d"] < 40.0))
      # 4h down move, 4h & 1d downtrend
      & ((df["RSI_3_4h"] > 40.0) | (df["AROONU_14_4h"] < 80.0) | (df["AROONU_14_1d"] < 100.0))
      # 4h down move, 4h high, 1d downtrend
      & ((df["RSI_3_4h"] > 40.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 70.0) | (df["ROC_9_1d"] > -60.0))
      # 4h down move, 1d high & overbought
      & ((df["RSI_3_4h"] > 40.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 90.0) | (df["ROC_9_1d"] < 100.0))
      # 4h & 1d down move, 1d high
      & ((df["RSI_3_4h"] > 45.0) | (df["RSI_3_1d"] > 45.0) | (df["AROONU_14_1d"] < 100.0))
      # 4h down move, 4h high, 1d downtrend
      & ((df["RSI_3_4h"] > 45.0) | (df["AROONU_14_4h"] < 70.0) | (df["ROC_9_1d"] > -30.0))
      # 4h down move, 4h high & overbought
      & ((df["RSI_3_4h"] > 50.0) | (df["AROONU_14_4h"] < 70.0) | (df["ROC_9_4h"] < 10.0))
      # 4h down move, 1d high & overbought
      & ((df["RSI_3_4h"] > 50.0) | (df["AROONU_14_1d"] < 85.0) | (df["ROC_9_1d"] < 80.0))
      # 4h down move, 1d high, 4h overbought
      & ((df["RSI_3_4h"] > 55.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 90.0) | (df["ROC_9_4h"] < 10.0))
      # 4h down move, 4h high & overbought
      & ((df["RSI_3_4h"] > 60.0) | (df["AROONU_14_4h"] < 70.0) | (df["ROC_9_4h"] < 20.0))
      # 4h down move, 1d high & overbought
      & ((df["RSI_3_4h"] > 60.0) | (df["AROONU_14_1d"] < 100.0) | (df["ROC_9_1d"] < 200.0))
      # 4h down move, 4h & 1d overbought
      & ((df["RSI_3_4h"] > 60.0) | (df["ROC_9_4h"] < 20.0) | (df["ROC_9_1d"] < 20.0))
      # 4h down move, 4h overbought
      & ((df["RSI_3_4h"] > 60.0) | (df["ROC_9_4h"] < 60.0))
      # 1d down move, 1d high, 1d downtrend
      & ((df["RSI_3_1d"] > 5.0) | (df["AROONU_14_1d"] < 80.0) | (df["ROC_9_1d"] > -20.0))
      # 1d down move, 1h & 4h high
      & ((df["RSI_3_1d"] > 10.0) | (df["AROONU_14_1h"] < 50.0) | (df["AROONU_14_4h"] < 90.0))
      # 1d down move, 1h high
      & ((df["RSI_3_1d"] > 10.0) | (df["AROONU_14_1h"] < 70.0))
      # 1d down move, 1h high, 1d downtrend
      & ((df["RSI_3_1d"] > 10.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 80.0) | (df["ROC_9_1d"] > -20.0))
      # 1d down move, 1h overbought, 1d downtrend
      & ((df["RSI_3_1d"] > 15.0) | (df["ROC_9_1h"] < 20.0) | (df["ROC_9_1d"] > -50.0))
      # 1d down move, 1h high, 1d downtrend
      & ((df["RSI_3_1d"] > 20.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 90.0) | (df["ROC_9_1d"] > -10.0))
      # 1d down move, 1h high, 1d overbought
      & ((df["RSI_3_1d"] > 25.0) | (df["AROONU_14_1h"] < 70.0) | (df["ROC_9_1d"] < 25.0))
      # 1d down move, 1d still high, 1d downtrend
      & ((df["RSI_3_1d"] > 25.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 50.0) | (df["ROC_9_1d"] > -20.0))
      # 1d down move, 1h high & overbought
      & ((df["RSI_3_1d"] > 40.0) | (df["AROONU_14_1d"] < 70.0) | (df["ROC_9_1d"] < 80.0))
      # 1d down move, 4h high & overbought
      & ((df["RSI_3_1d"] > 45.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 90.0) | (df["ROC_9_4h"] < 60.0))
      # 1d downtrend, 1d high & overbought
      & ((df["CMF_20_1d"] > -0.40) | (df["AROONU_14_1d"] < 85.0) | (df["ROC_9_1d"] < 20.0))
      # 1h high, 4h & 1d overbought
      & ((df["AROONU_14_1h"] < 70.0) | (df["ROC_9_4h"] < 50.0) | (df["ROC_9_1d"] < 200.0))
      # 1h & 4h high, 1d overbought
      & ((df["AROONU_14_1h"] < 70.0) | (df["AROONU_14_4h"] < 90.0) | (df["ROC_9_1d"] < 50.0))
      # 1h & 4h high, 1d downtrend
      & ((df["AROONU_14_1h"] < 70.0) | (df["AROONU_14_4h"] < 100.0) | (df["ROC_9_1d"] > -40.0))
      # 1h high, 4h & 1d downtrend
      & ((df["AROONU_14_1h"] < 70.0) | (df["ROC_9_4h"] > -30.0) | (df["ROC_9_1d"] > -50.0))
      # 1h & 4h high, 1h overbought
      & ((df["AROONU_14_1h"] < 80.0) | (df["AROONU_14_4h"] < 90.0) | (df["ROC_9_1h"] < 30.0))
      # 1h & 4high, 1d downtrend
      & ((df["AROONU_14_1h"] < 80.0) | (df["AROONU_14_4h"] < 100.0) | (df["ROC_9_1d"] > -20.0))
      # 1h & 4h high, 1d overbought
      & ((df["AROONU_14_1h"] < 80.0) | (df["AROONU_14_4h"] < 100.0) | (df["ROC_9_1d"] < 80.0))
      # 1h & 1d high, 1d overbought
      & ((df["AROONU_14_1h"] < 80.0) | (df["AROONU_14_1d"] < 100.0) | (df["ROC_9_1d"] < 30.0))
      # 1h high, 1d downtrend
      & ((df["AROONU_14_1h"] < 80.0) | (df["ROC_9_1d"] > -40.0))
      # 1h & 4h high, 1d overbought
      & ((df["AROONU_14_1h"] < 90.0) | (df["AROONU_14_4h"] < 100.0) | (df["ROC_9_1d"] < 30.0))
      # 1h high, 4h & 1d overbought
      & ((df["AROONU_14_1h"] < 90.0) | (df["ROC_9_4h"] < 40.0) | (df["ROC_9_1d"] < 40.0))
      # 4h still high, 5m downtrend
      & ((df["AROONU_14_4h"] < 40.0) | (df["ROC_9"] > -40.0))
      # 4h high & overbought
      & ((df["AROONU_14_4h"] < 70.0) | (df["ROC_9_4h"] < 80.0))
      # 4h & 1d high, 1d overbought
      & ((df["AROONU_14_4h"] < 80.0) | (df["AROONU_14_1d"] < 100.0) | (df["ROC_9_1d"] < 40.0))
      # 4h high, 1h & 4h overbought
      & ((df["AROONU_14_4h"] < 100.0) | (df["ROC_9_1h"] < 10.0) | (df["ROC_9_4h"] < 20.0))
      # 1d high, 1d downtrend
      & ((df["AROONU_14_1d"] < 80.0) | (df["ROC_9_1d"] > -30.0))
      # 1d high, 1h & 4h downtrend
      & ((df["AROONU_14_1d"] < 85.0) | (df["ROC_9_1h"] > -30.0) | (df["ROC_9_4h"] > -50.0))
      # 1d high, 4h & 1d overbought
      & ((df["AROONU_14_1d"] < 85.0) | (df["ROC_9_4h"] < 60.0) | (df["ROC_9_1d"] < 60.0))
      # 1d high, 1h & 4h down move
      & ((df["AROONU_14_1d"] < 100.0) | (df["ROC_9_1h"] < 25.0) | (df["ROC_9_4h"] < 60.0))
      # 15m high, 1d overbought
      & ((df["STOCHRSIk_14_14_3_3_15m"] < 70.0) | (df["ROC_9_1d"] < 60.0))
      # 1h high, 1d downtrend
      & ((df["STOCHRSIk_14_14_3_3_1h"] < 70.0) | (df["ROC_9_1d"] > -50.0))
      # 1h high, 1d overbought
      & ((df["STOCHRSIk_14_14_3_3_1h"] < 70.0) | (df["ROC_9_1d"] < 40.0))
      # 1h high, 4h downtrend
      & ((df["STOCHRSIk_14_14_3_3_1h"] < 80.0) | (df["ROC_9_4h"] > -20.0))
      # 1h high, 4h overbought
      & ((df["STOCHRSIk_14_14_3_3_1h"] < 80.0) | (df["ROC_9_4h"] < 80.0))
      # 4h high, 1h & 4h overbought
      & ((df["STOCHRSIk_14_14_3_3_4h"] < 80.0) | (df["ROC_9_1h"] < 10.0) | (df["ROC_9_4h"] < 20.0))
      # 1d high, 1h & 1d overbought
      & ((df["STOCHRSIk_14_14_3_3_1d"] < 80.0) | (df["ROC_9_1h"] < 10.0) | (df["ROC_9_1d"] < 80.0))
      # 1d high, 4h & 1d overbought
      & ((df["STOCHRSIk_14_14_3_3_1d"] < 80.0) | (df["ROC_9_4h"] < 60.0) | (df["ROC_9_1d"] < 60.0))
      # big drop in the last 20 days, 1d high, 1d downtrend
      & (
        (df["close"] > (df["high_max_20_1d"] * 0.20))
        | (df["STOCHRSIk_14_14_3_3_1d"] < 70.0)
        | (df["ROC_9_1d"] > -15.0)
      )
      # drop in last 20 days, 1h high, 1d downtrend
      & ((df["close"] > (df["high_max_20_1d"] * 0.20)) | (df["AROONU_14_1h"] < 70.0) | (df["ROC_9_1d"] > -70.0))
      # drop in last 20 days. 4h high
      & ((df["close"] > (df["high_max_20_1d"] * 0.10)) | (df["STOCHRSIk_14_14_3_3_4h"] < 90.0))
    )

    # Logic
    long_entry_logic.append(
      # (df["RSI_3"] > 5.0)
      (df["AROONU_14"] < 30.0)
      & (df["STOCHRSIk_14_14_3_3"] < 30.0)
      # & (df["RSI_3_15m"] > 5.0)
      & (df["AROONU_14_15m"] < 50.0)
      & (df["close"] < (df["EMA_20"] * 0.948))
    )


def append_long_3(df, long_entry_logic, allowed_empty_candles_288) -> None:
    """Append NFI long condition #3, the normal-mode long entry."""
    # Protections
    long_entry_logic.append(df["num_empty_288"] <= allowed_empty_candles_288)
    long_entry_logic.append(df["protections_long_global"] == True)

    long_entry_logic.append(
      # 5m & 4h down move, 1h still high
      ((df["RSI_3"] > 5.0) | (df["RSI_3_4h"] > 15.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 50.0))
      # 5m down move, 15m high, 1d overbought
      & ((df["RSI_3"] > 5.0) | (df["AROONU_14_15m"] < 70.0) | (df["ROC_9_1d"] < 40.0))
      # 5m down move, 15m still high, 1d downtrend
      & ((df["RSI_3"] > 5.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 50.0) | (df["ROC_9_1d"] > -20.0))
      # 5m down move, 1h still high, 4h downtrend
      & ((df["RSI_3"] > 5.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 50.0) | (df["ROC_9_4h"] > -10.0))
      # 5m down move, 1h high. 1d downtrend
      & ((df["RSI_3"] > 5.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 80.0) | (df["ROC_9_1d"] > -30.0))
      # 5m down move, 15m & 1h high
      & ((df["RSI_3"] > 10.0) | (df["AROONU_14_15m"] < 70.0) | (df["AROONU_14_1h"] < 100.0))
      # 5m down move, 15m & 1d high
      & ((df["RSI_3"] > 10.0) | (df["AROONU_14_15m"] < 70.0) | (df["AROONU_14_1d"] < 100.0))
      # 5m down move, 1h & 1d high
      & ((df["RSI_3"] > 15.0) | (df["AROONU_14_1h"] < 80.0) | (df["AROONU_14_1d"] < 90.0))
      # 15m & 1h dowbn move, 1d high
      & ((df["RSI_3_15m"] > 5.0) | (df["RSI_3_1h"] > 25.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 90.0))
      # 15m & 1d down move, 1h high
      & ((df["RSI_3_15m"] > 5.0) | (df["RSI_3_1d"] > 15.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 60.0))
      # 15m & 1h down move, 15m still high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1h"] > 35.0) | (df["AROONU_14_15m"] < 50.0))
      # 15m & 1h down move, 1h still high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_4h"] > 10.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 40.0))
      # 15m & 4h down move, 15m still high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_4h"] > 20.0) | (df["AROONU_14_15m"] < 50.0))
      # 15m down move, 15m still high, 1h high
      & ((df["RSI_3_15m"] > 10.0) | (df["AROONU_14_15m"] < 40.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 90.0))
      # 15m down move, 15m still high, 1h high
      & ((df["RSI_3_15m"] > 10.0) | (df["AROONU_14_15m"] < 50.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 80.0))
      # 15m down move, 15m still high, 1d overbought
      & ((df["RSI_3_15m"] > 10.0) | (df["AROONU_14_15m"] < 50.0) | (df["ROC_9_1d"] < 100.0))
      # 15m down move, 15m high, 1d overbought
      & ((df["RSI_3_15m"] > 10.0) | (df["AROONU_14_15m"] < 60.0) | (df["ROC_9_1d"] < 50.0))
      # 15m down move, 4h high, 1d downtrend
      & ((df["RSI_3_15m"] > 10.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 80.0) | (df["ROC_9_1d"] > -20.0))
      # 15m & 1h down move, 4h still high
      & ((df["RSI_3_15m"] > 15.0) | (df["RSI_3_1h"] > 35.0) | (df["AROONU_14_4h"] < 50.0))
      # 15m & 1h down move, 1h high
      & ((df["RSI_3_15m"] > 15.0) | (df["RSI_3_1h"] > 35.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 60.0))
      # 15m & 1h down move, 1h high
      & ((df["RSI_3_15m"] > 15.0) | (df["RSI_3_1h"] > 45.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 80.0))
      # 15m & 1h down move, 1h high
      & ((df["RSI_3_15m"] > 15.0) | (df["RSI_3_1h"] > 50.0) | (df["AROONU_14_1h"] < 80.0))
      # 15m & 4h down move, 4h high
      & ((df["RSI_3_15m"] > 15.0) | (df["RSI_3_4h"] > 15.0) | (df["AROONU_14_4h"] < 70.0))
      # 15m & 4h down move, 1d downtrend
      & ((df["RSI_3_15m"] > 15.0) | (df["RSI_3_4h"] > 15.0) | (df["ROC_9_1d"] > -30.0))
      # 15m & 4h down move, 15m still high
      & ((df["RSI_3_15m"] > 15.0) | (df["RSI_3_4h"] > 15.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 50.0))
      # 15m & 4h down move, 1d high
      & ((df["RSI_3_15m"] > 15.0) | (df["RSI_3_4h"] > 20.0) | (df["AROONU_14_1d"] < 100.0))
      # 15m & 1d down move, 15m high
      & ((df["RSI_3_15m"] > 15.0) | (df["RSI_3_1d"] > 15.0) | (df["AROONU_14_15m"] < 70.0))
      # 15m down move, 4h downtrend. 15m high
      & ((df["RSI_3_15m"] > 15.0) | (df["CMF_20_4h"] > -0.30) | (df["AROONU_14_15m"] < 60.0))
      # 15m down move, 15m still high, 1h still high
      & ((df["RSI_3_15m"] > 15.0) | (df["AROONU_14_15m"] < 40.0) | (df["AROONU_14_1h"] < 50.0))
      # 15m down move, 15m high, 4h downtrend
      & ((df["RSI_3_15m"] > 15.0) | (df["AROONU_14_15m"] < 60.0) | (df["ROC_9_4h"] > -20.0))
      # 15m down move, 15m high, 1d downtrend
      & ((df["RSI_3_15m"] > 15.0) | (df["AROONU_14_15m"] < 60.0) | (df["ROC_9_1d"] > -70.0))
      # 15m down move, 15m high, 1d overbought
      & ((df["RSI_3_15m"] > 15.0) | (df["AROONU_14_15m"] < 60.0) | (df["ROC_9_1d"] < 100.0))
      # 15m down move, 15m & 1h high
      & ((df["RSI_3_15m"] > 15.0) | (df["AROONU_14_15m"] < 70.0) | (df["AROONU_14_1h"] < 70.0))
      # 15m down move, 15m & 4h high
      & ((df["RSI_3_15m"] > 15.0) | (df["AROONU_14_15m"] < 70.0) | (df["AROONU_14_4h"] < 70.0))
      # 15m down move, 15m & 1d high
      & ((df["RSI_3_15m"] > 15.0) | (df["AROONU_14_15m"] < 70.0) | (df["AROONU_14_1d"] < 100.0))
      # 15m down move, 15m still high, 4h high
      & ((df["RSI_3_15m"] > 15.0) | (df["AROONU_14_15m"] < 70.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 80.0))
      # 15m down move, 15m high, 1d overbought
      & ((df["RSI_3_15m"] > 15.0) | (df["AROONU_14_15m"] < 70.0) | (df["ROC_9_1d"] < 50.0))
      # 15m down move, 4h high, 1d downtrend
      & ((df["RSI_3_15m"] > 15.0) | (df["AROONU_14_4h"] < 50.0) | (df["ROC_9_1d"] > -40.0))
      # 15m down move, 1h high, 1d overbought
      & ((df["RSI_3_15m"] > 15.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 80.0) | (df["ROC_9_1d"] < 20.0))
      # 15m down move, 4h & 1d overbought
      & ((df["RSI_3_15m"] > 15.0) | (df["ROC_9_4h"] < 25.0) | (df["ROC_9_1d"] < 100.0))
      # 15m & 1h down move, 1h still high
      & ((df["RSI_3_15m"] > 20.0) | (df["RSI_3_1h"] > 25.0) | (df["AROONU_14_1h"] < 40.0))
      # 15m & 1h down move, 1h high
      & ((df["RSI_3_15m"] > 20.0) | (df["RSI_3_1h"] > 45.0) | (df["AROONU_14_1h"] < 85.0))
      # 15m & 1h down move, 4h high
      & ((df["RSI_3_15m"] > 20.0) | (df["RSI_3_1h"] > 45.0) | (df["AROONU_14_4h"] < 80.0))
      # 15m & 1h down move, 1d high
      & ((df["RSI_3_15m"] > 20.0) | (df["RSI_3_1h"] > 45.0) | (df["AROONU_14_1d"] < 100.0))
      # 15m & 4h down move, 15m high
      & ((df["RSI_3_15m"] > 20.0) | (df["RSI_3_4h"] > 20.0) | (df["AROONU_14_15m"] < 60.0))
      # 15m & 4h down move, 15m high
      & ((df["RSI_3_15m"] > 20.0) | (df["RSI_3_4h"] > 30.0) | (df["AROONU_14_15m"] < 75.0))
      # 15m & 4h down move, 1d high
      & ((df["RSI_3_15m"] > 20.0) | (df["RSI_3_4h"] > 30.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 90.0))
      # 15m & 4h down move, 4h high
      & ((df["RSI_3_15m"] > 20.0) | (df["RSI_3_4h"] > 60.0) | (df["AROONU_14_4h"] < 70.0))
      # 15m & 1h down move, 15m still high
      & ((df["RSI_3_15m"] > 20.0) | (df["RSI_3_1d"] > 25.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 50.0))
      # 15m & 1d down move, 1h still high
      & ((df["RSI_3_15m"] > 20.0) | (df["RSI_3_1d"] > 25.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 50.0))
      # 15m & 1d down move, 1h high
      & ((df["RSI_3_15m"] > 20.0) | (df["RSI_3_1d"] > 40.0) | (df["AROONU_14_1h"] < 90.0))
      # 15m &1d down move, 1d overbought
      & ((df["RSI_3_15m"] > 20.0) | (df["RSI_3_1d"] > 50.0) | (df["ROC_9_1d"] < 20.0))
      # 15m down move, 15m still not low enough, 4h overbought
      & ((df["RSI_3_15m"] > 20.0) | (df["AROONU_14_15m"] < 30.0) | (df["ROC_9_4h"] < 60.0))
      # 15m down move, 15m still high, 4h high
      & ((df["RSI_3_15m"] > 20.0) | (df["AROONU_14_15m"] < 40.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 90.0))
      # 15m down move, 15m still high, 1h high
      & ((df["RSI_3_15m"] > 20.0) | (df["AROONU_14_15m"] < 50.0) | (df["AROONU_14_1h"] < 100.0))
      # 15m down move, 15m still high, 4h high
      & ((df["RSI_3_15m"] > 20.0) | (df["AROONU_14_15m"] < 50.0) | (df["AROONU_14_4h"] < 70.0))
      # 15m down move, 15m still high, 1d overbought
      & ((df["RSI_3_15m"] > 20.0) | (df["AROONU_14_15m"] < 50.0) | (df["ROC_9_1d"] < 50.0))
      # 15m down move, 15m high, 4h downtrend
      & ((df["RSI_3_15m"] > 20.0) | (df["AROONU_14_15m"] < 60.0) | (df["ROC_9_4h"] > -40.0))
      # 15m down move, 15m high, 4h overbought
      & ((df["RSI_3_15m"] > 20.0) | (df["AROONU_14_15m"] < 60.0) | (df["ROC_9_4h"] < 10.0))
      # 15m down move, 15m high, 4h overbought
      & ((df["RSI_3_15m"] > 20.0) | (df["AROONU_14_15m"] < 70.0) | (df["ROC_9_4h"] < 20.0))
      # 15m down move, 15m high, 1d downtrend
      & ((df["RSI_3_15m"] > 20.0) | (df["AROONU_14_15m"] < 70.0) | (df["ROC_9_1d"] > -20.0))
      # 15m down move, 15m high, 1d overbought
      & ((df["RSI_3_15m"] > 20.0) | (df["AROONU_14_15m"] < 70.0) | (df["ROC_9_1d"] < 50.0))
      # 15m down move, 1h high, 4h overbought
      & ((df["RSI_3_15m"] > 20.0) | (df["AROONU_14_1h"] < 80.0) | (df["ROC_9_4h"] < 20.0))
      # 15m down move, 4h high & overbought
      & ((df["RSI_3_15m"] > 20.0) | (df["AROONU_14_4h"] < 70.0) | (df["ROC_9_4h"] < 50.0))
      # 15m down move, 1h high, 4h downtrend
      & ((df["RSI_3_15m"] > 20.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 60.0) | (df["ROC_9_4h"] > -20.0))
      # 15m down move, 1h high, 1d overbought
      & ((df["RSI_3_15m"] > 20.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 80.0) | (df["ROC_9_1d"] < 30.0))
      # 15m down move, 1h high
      & ((df["RSI_3_15m"] > 20.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 90.0))
      # 15m down move, 4h still high, 1d downtrend
      & ((df["RSI_3_15m"] > 20.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 40.0) | (df["ROC_9_1d"] > -20.0))
      # 15m down move, 4h high, 1d downtrend
      & ((df["RSI_3_15m"] > 20.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 80.0) | (df["ROC_9_1d"] > -30.0))
      # 15m down move, 4h & 1d overbought
      & ((df["RSI_3_15m"] > 20.0) | (df["ROC_9_4h"] < 25.0) | (df["ROC_9_1d"] < 100.0))
      # 15m & 1h down move, 15m high
      & ((df["RSI_3_15m"] > 25.0) | (df["RSI_3_1h"] > 30.0) | (df["AROONU_14_15m"] < 70.0))
      # 15m & 4h down move, 15m high
      & ((df["RSI_3_15m"] > 25.0) | (df["RSI_3_4h"] > 40.0) | (df["AROONU_14_15m"] < 75.0))
      # 15m & 4h down move, 1h high
      & ((df["RSI_3_15m"] > 25.0) | (df["RSI_3_4h"] > 50.0) | (df["AROONU_14_1h"] < 100.0))
      # 15m & 4h down move, 1h high
      & ((df["RSI_3_15m"] > 25.0) | (df["RSI_3_4h"] > 60.0) | (df["AROONU_14_1h"] < 100.0))
      # 15m & 4h down move, 4h high
      & ((df["RSI_3_15m"] > 25.0) | (df["RSI_3_4h"] > 60.0) | (df["AROONU_14_4h"] < 80.0))
      # 15m & 1d down move, 1d high
      & ((df["RSI_3_15m"] > 25.0) | (df["RSI_3_1d"] > 30.0) | (df["AROONU_14_1d"] < 75.0))
      # 15m & 1d down move, 1d high
      & ((df["RSI_3_15m"] > 25.0) | (df["RSI_3_1d"] > 45.0) | (df["AROONU_14_1d"] < 90.0))
      # 15m down move, 15m high, 4h downtrend
      & ((df["RSI_3_15m"] > 25.0) | (df["AROONU_14_15m"] < 70.0) | (df["ROC_9_4h"] > -20.0))
      # 15m down move, 15m high, 4h overbought
      & ((df["RSI_3_15m"] > 25.0) | (df["AROONU_14_15m"] < 70.0) | (df["ROC_9_4h"] < 10.0))
      # 15m down move, 15m high, 1d overbought
      & ((df["RSI_3_15m"] > 25.0) | (df["AROONU_14_15m"] < 70.0) | (df["ROC_9_1d"] < 60.0))
      # 15m down move, 1h & 4h high
      & ((df["RSI_3_15m"] > 25.0) | (df["AROONU_14_1h"] < 70.0) | (df["AROONU_14_4h"] < 70.0))
      # 15m down move, 1h high, 1d downtrend
      & ((df["RSI_3_15m"] > 25.0) | (df["AROONU_14_1h"] < 70.0) | (df["ROC_9_4h"] > -10.0))
      # 15m down move, 1h high, 1d overbought
      & ((df["RSI_3_15m"] > 25.0) | (df["AROONU_14_1h"] < 90.0) | (df["ROC_9_1d"] < 20.0))
      # 15m down move, 4h high, 1d high
      & ((df["RSI_3_15m"] > 25.0) | (df["AROONU_14_4h"] < 60.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 90.0))
      # 15m down move, 4h high & overbought
      & ((df["RSI_3_15m"] > 25.0) | (df["AROONU_14_4h"] < 80.0) | (df["ROC_9_4h"] < 10.0))
      # 15m down move, 15m still high, 1h still high
      & ((df["RSI_3_15m"] > 25.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 50.0) | (df["AROONU_14_1h"] < 50.0))
      # 15m down move, 1h high, 4h high
      & ((df["RSI_3_15m"] > 25.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 70.0) | (df["AROONU_14_4h"] < 100.0))
      # 15m down move, 4h & 1d overbought
      & ((df["RSI_3_15m"] > 25.0) | (df["ROC_9_4h"] < 50.0) | (df["ROC_9_1d"] < 50.0))
      # 15m & 1h down move, 1h high
      & ((df["RSI_3_15m"] > 30.0) | (df["RSI_3_1h"] > 30.0) | (df["AROONU_14_1h"] < 80.0))
      # 15m & 1h down move, 1d overbought
      & ((df["RSI_3_15m"] > 30.0) | (df["RSI_3_1h"] > 30.0) | (df["ROC_9_1d"] < 40.0))
      # 15m & 4h down move, 4h high
      & ((df["RSI_3_15m"] > 30.0) | (df["RSI_3_4h"] > 35.0) | (df["AROONU_14_4h"] < 70.0))
      # 15m down move, 1d high, 15m high
      & ((df["RSI_3_15m"] > 30.0) | (df["RSI_14_1d"] < 70.0) | (df["AROONU_14_15m"] < 70.0))
      # 15m down move, 15m high, 1d downtrend
      & ((df["RSI_3_15m"] > 30.0) | (df["AROONU_14_15m"] < 60.0) | (df["ROC_9_1d"] > -40.0))
      # 15m down move, 15m high, 15m downtrend
      & ((df["RSI_3_15m"] > 30.0) | (df["AROONU_14_15m"] < 70.0) | (df["CMF_20_15m"] > -0.30))
      # 15m down move, 15m high, 1d overbought
      & ((df["RSI_3_15m"] > 30.0) | (df["AROONU_14_15m"] < 70.0) | (df["ROC_9_1d"] < 70.0))
      # 15m down move, 1h high, 1d overbought
      & ((df["RSI_3_15m"] > 30.0) | (df["AROONU_14_1h"] < 100.0) | (df["ROC_9_1d"] < 30.0))
      # 15m down move, 4h high & overbought
      & ((df["RSI_3_15m"] > 30.0) | (df["AROONU_14_4h"] < 70.0) | (df["ROC_9_4h"] < 60.0))
      # 15m down move, 15m high, 4h overbought
      & ((df["RSI_3_15m"] > 30.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 70.0) | (df["ROC_9_4h"] < 70.0))
      # 15m down move, 1h high, 1d overbought
      & ((df["RSI_3_15m"] > 30.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 90.0) | (df["ROC_9_1d"] < 50.0))
      # 15m down move, 15m high, 4h high
      & ((df["RSI_3_15m"] > 35.0) | (df["AROONU_14_15m"] < 60.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 90.0))
      # 15m down move, 15m high, 4h overbought
      & ((df["RSI_3_15m"] > 35.0) | (df["AROONU_14_15m"] < 70.0) | (df["ROC_9_4h"] < 80.0))
      # 15m down move, 1h high, 4h overbought
      & ((df["RSI_3_15m"] > 35.0) | (df["AROONU_14_1h"] < 90.0) | (df["ROC_9_4h"] < 100.0))
      # 15m down move, 4h high, 1d overbought
      & ((df["RSI_3_15m"] > 35.0) | (df["AROONU_14_4h"] < 80.0) | (df["ROC_9_1d"] < 200.0))
      # 15m down move, 1h high, 1d downtrend
      & ((df["RSI_3_15m"] > 35.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 90.0) | (df["ROC_9_1d"] > -50.0))
      # 15m down move, 4h high & overbought
      & ((df["RSI_3_15m"] > 35.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 90.0) | (df["ROC_9_4h"] < 20.0))
      # 15m down move, 15m high, 1h downtrend
      & ((df["RSI_3_15m"] > 40.0) | (df["AROONU_14_15m"] < 70.0) | (df["ROC_9_1h"] > -20.0))
      # 15m down move, 15m & 4h high
      & ((df["RSI_3_15m"] > 40.0) | (df["AROONU_14_15m"] < 75.0) | (df["AROONU_14_4h"] < 75.0))
      # 15m down move, 4h high & overbought
      & ((df["RSI_3_15m"] > 40.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 80.0) | (df["ROC_9_4h"] < 30.0))
      # 1h & 4h down move, 15m still high
      & ((df["RSI_3_1h"] > 5.0) | (df["RSI_3_4h"] > 10.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 50.0))
      # 1h & 4h down move, 4h still high
      & ((df["RSI_3_1h"] > 10.0) | (df["RSI_3_4h"] > 10.0) | (df["AROONU_14_4h"] < 50.0))
      # 1h down move, 4h still high, 4h downtrend
      & ((df["RSI_3_1h"] > 10.0) | (df["AROONU_14_4h"] < 40.0) | (df["ROC_9_4h"] > -20.0))
      # 1h down move, 4h high & overbought
      & ((df["RSI_3_1h"] > 10.0) | (df["AROONU_14_4h"] < 70.0) | (df["ROC_9_4h"] < 20.0))
      # 1h & 4h down move, 1d high
      & ((df["RSI_3_1h"] > 15.0) | (df["RSI_3_4h"] > 15.0) | (df["RSI_14_1d"] < 60.0))
      # 1h & 4h down move, 15m high
      & ((df["RSI_3_1h"] > 15.0) | (df["RSI_3_4h"] > 15.0) | (df["AROONU_14_15m"] < 70.0))
      # 1h & 4h down move, 1d downtrend
      & ((df["RSI_3_1h"] > 15.0) | (df["RSI_3_4h"] > 20.0) | (df["ROC_9_1d"] > -30.0))
      # 1h & 1d down move, 1d overbought
      & ((df["RSI_3_1h"] > 15.0) | (df["RSI_3_1d"] > 35.0) | (df["ROC_9_1d"] < 10.0))
      # 1h & 1d down move, 1d overbought
      & ((df["RSI_3_1h"] > 15.0) | (df["RSI_3_1d"] > 60.0) | (df["ROC_9_1d"] < 40.0))
      # 1h down move, 1h still not low enough, 1d downtrend
      & ((df["RSI_3_1h"] > 15.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 30.0) | (df["ROC_9_1d"] > -30.0))
      # 1h & 4h down move, 1d high
      & ((df["RSI_3_1h"] > 20.0) | (df["RSI_3_4h"] > 25.0) | (df["AROONU_14_1d"] < 80.0))
      # 1h & 4h down move, 1d overbought
      & ((df["RSI_3_1h"] > 20.0) | (df["RSI_3_4h"] > 25.0) | (df["ROC_9_1d"] < 30.0))
      # 1h down move, 4h high, 1d overbought
      & ((df["RSI_3_1h"] > 20.0) | (df["AROONU_14_4h"] < 80.0) | (df["ROC_9_1d"] < 100.0))
      # 1h & 4h down move, 4h high
      & ((df["RSI_3_1h"] > 25.0) | (df["RSI_3_4h"] > 40.0) | (df["AROONU_14_4h"] < 80.0))
      # 1h & 1d down move, 1d still high
      & ((df["RSI_3_1h"] > 25.0) | (df["RSI_3_1d"] > 40.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 50.0))
      # 1h down move, 1h high, 1d overbought
      & ((df["RSI_3_1h"] > 25.0) | (df["AROONU_14_1h"] < 70.0) | (df["ROC_9_1d"] < 20.0))
      # 1h down move, 1d high & overbought
      & ((df["RSI_3_1h"] > 25.0) | (df["AROONU_14_1d"] < 80.0) | (df["ROC_9_1d"] < 20.0))
      # 1h down move, 4h high, 1d downtrend
      & ((df["RSI_3_1h"] > 25.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 60.0) | (df["ROC_9_1d"] > -20.0))
      # 1h down move, 4h downtrend, 1d overbought
      & ((df["RSI_3_1h"] > 25.0) | (df["ROC_9_4h"] > -40.0) | (df["ROC_9_1d"] < 50.0))
      # 1h down move, 15m & 1h still high
      & ((df["RSI_3_1h"] > 30.0) | (df["AROONU_14_15m"] < 40.0) | (df["AROONU_14_1h"] < 50.0))
      # 1h down move, 1h still high 1d overbought
      & ((df["RSI_3_1h"] > 30.0) | (df["AROONU_14_1h"] < 50.0) | (df["ROC_9_1d"] < 200.0))
      # 1h down move, 1h high, 4h downtrend
      & ((df["RSI_3_1h"] > 30.0) | (df["AROONU_14_1h"] < 60.0) | (df["ROC_9_4h"] > -20.0))
      # 1h down move, 1h high, 1d overbought
      & ((df["RSI_3_1h"] > 30.0) | (df["AROONU_14_1h"] < 70.0) | (df["ROC_9_1d"] < 30.0))
      # 1h down move, 4h high & overbought
      & ((df["RSI_3_1h"] > 30.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 60.0) | (df["ROC_9_4h"] < 20.0))
      # 1h down move, 4h & 1h overbought
      & ((df["RSI_3_1h"] > 30.0) | (df["ROC_9_4h"] < 30.0) | (df["ROC_9_1d"] < 40.0))
      # 1h & 1d down move, 1h high
      & ((df["RSI_3_1h"] > 35.0) | (df["RSI_3_1d"] > 35.0) | (df["AROONU_14_1h"] < 75.0))
      # 1h down move, 15m still high, 4h  high
      & ((df["RSI_3_1h"] > 35.0) | (df["AROONU_14_15m"] < 40.0) | (df["AROONU_14_4h"] < 80.0))
      # 1h down move, 15m still high, 4h high
      & ((df["RSI_3_1h"] > 35.0) | (df["AROONU_14_15m"] < 40.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 70.0))
      # 1h down move, 15m still high, 4h high
      & ((df["RSI_3_1h"] > 35.0) | (df["AROONU_14_15m"] < 50.0) | (df["AROONU_14_4h"] < 70.0))
      # 1h down move, 15m & 1d high
      & ((df["RSI_3_1h"] > 35.0) | (df["AROONU_14_15m"] < 60.0) | (df["AROONU_14_1d"] < 80.0))
      # 1h down move, 1h & 4h high
      & ((df["RSI_3_1h"] > 35.0) | (df["AROONU_14_1h"] < 70.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 90.0))
      # 1h down move, 1h & 1d high
      & ((df["RSI_3_1h"] > 35.0) | (df["AROONU_14_1h"] < 80.0) | (df["AROONU_14_1d"] < 90.0))
      # 1h down move, 1h downtrend, 4h overbought
      & ((df["RSI_3_1h"] > 35.0) | (df["CMF_20_1h"] > -0.30) | (df["ROC_9_4h"] < 20.0))
      # 1h down move, 1h high, 1d downtrend
      & ((df["RSI_3_1h"] > 35.0) | (df["AROONU_14_1h"] < 70.0) | (df["ROC_9_1d"] > -80.0))
      # 1h down move, 1h high, 1d overbought
      & ((df["RSI_3_1h"] > 35.0) | (df["AROONU_14_1h"] < 80.0) | (df["ROC_9_1d"] < 50.0))
      # 1h down move, 4h high, 1d downtrend
      & ((df["RSI_3_1h"] > 35.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 80.0) | (df["ROC_9_1d"] > -50.0))
      # 1h & 4h down move, 1h high
      & ((df["RSI_3_1h"] > 40.0) | (df["RSI_3_4h"] > 50.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 70.0))
      # 1h & 4h down move, 4h high
      & ((df["RSI_3_1h"] > 40.0) | (df["RSI_3_4h"] > 50.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 60.0))
      # 1h down move, 15m still high, 4h downtrend
      & ((df["RSI_3_1h"] > 40.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 40.0) | (df["ROC_9_4h"] > -15.0))
      # 1h down move, 15m still high, 1d overbought
      & ((df["RSI_3_1h"] > 40.0) | (df["AROONU_14_15m"] < 50.0) | (df["ROC_9_1d"] < 50.0))
      # 1h down move, 15m & 4h high
      & ((df["RSI_3_1h"] > 40.0) | (df["AROONU_14_15m"] < 70.0) | (df["AROONU_14_4h"] < 70.0))
      # 1h down move, 1h still high, 4h high
      & ((df["RSI_3_1h"] > 40.0) | (df["AROONU_14_1h"] < 50.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 80.0))
      # 1h down move, 1h still high, 1d overbought
      & ((df["RSI_3_1h"] > 40.0) | (df["AROONU_14_1h"] < 50.0) | (df["ROC_9_1d"] < 100.0))
      # 1h down move, 1h high, 4h overbought
      & ((df["RSI_3_1h"] > 40.0) | (df["AROONU_14_1h"] < 70.0) | (df["ROC_9_4h"] < 20.0))
      # 1h down move, 1h high, 1d downtrend
      & ((df["RSI_3_1h"] > 40.0) | (df["AROONU_14_1h"] < 85.0) | (df["ROC_9_1d"] > -60.0))
      # 1h down move, 1h & 4h high
      & ((df["RSI_3_1h"] > 40.0) | (df["AROONU_14_1h"] < 90.0) | (df["AROONU_14_4h"] < 100.0))
      # 1h down move, 1h high, 1d downtrend
      & ((df["RSI_3_1h"] > 40.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 80.0) | (df["CMF_20_1d"] > -0.20))
      # 1h down move, 4h & 1d overbought
      & ((df["RSI_3_1h"] > 40.0) | (df["ROC_9_4h"] < 10.0) | (df["ROC_9_1d"] < 50.0))
      # 1h down move, 15m high, 4h overbought
      & ((df["RSI_3_1h"] > 45.0) | (df["AROONU_14_15m"] < 70.0) | (df["ROC_9_4h"] < 30.0))
      # 1h down move, 1h high, 4h overbought
      & ((df["RSI_3_1h"] > 45.0) | (df["AROONU_14_1h"] < 100.0) | (df["ROC_9_4h"] < 20.0))
      # 1h down move, 4h high & overbought
      & ((df["RSI_3_1h"] > 45.0) | (df["AROONU_14_4h"] < 80.0) | (df["ROC_9_4h"] < 20.0))
      # 1h down move, 4h high & overbought
      & ((df["RSI_3_1h"] > 45.0) | (df["AROONU_14_4h"] < 80.0) | (df["ROC_9_4h"] < 40.0))
      # 1h down move, 1d high & overbought
      & ((df["RSI_3_1h"] > 45.0) | (df["AROONU_14_1d"] < 100.0) | (df["ROC_9_1d"] < 30.0))
      # 1h down move, 1h still high, 1d overbought
      & ((df["RSI_3_1h"] > 45.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 40.0) | (df["ROC_9_1d"] < 200.0))
      # 1h down move, 15m & 1h high
      & ((df["RSI_3_1h"] > 50.0) | (df["AROONU_14_15m"] < 70.0) | (df["AROONU_14_1h"] < 100.0))
      # 1h down move, 1h high, 4h overbought
      & ((df["RSI_3_1h"] > 50.0) | (df["AROONU_14_1h"] < 80.0) | (df["ROC_9_4h"] < 10.0))
      # 1h down move, 4h still high, 1d overbought
      & ((df["RSI_3_1h"] > 50.0) | (df["AROONU_14_4h"] < 50.0) | (df["ROC_9_1d"] < 200.0))
      # 1h down move, 4h high & overbought
      & ((df["RSI_3_1h"] > 50.0) | (df["AROONU_14_4h"] < 100.0) | (df["ROC_9_4h"] < 50.0))
      # 1h down move, 1h & 4h high
      & ((df["RSI_3_1h"] > 50.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 80.0) | (df["AROONU_14_4h"] < 100.0))
      # 1h down move, 4h high & overbought
      & ((df["RSI_3_1h"] > 50.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 70.0) | (df["ROC_9_4h"] < 10.0))
      # 1h down move, 1h high, 1d high
      & ((df["RSI_3_1h"] > 55.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 70.0) | (df["AROONU_14_1d"] < 100.0))
      # 1h down move, 1h high, 1d downtrend
      & ((df["RSI_3_1h"] > 55.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 80.0) | (df["ROC_9_1d"] > -30.0))
      # 1h down move, 4h high & overbought
      & ((df["RSI_3_1h"] > 55.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 80.0) | (df["ROC_9_4h"] < 100.0))
      # 1h down move, 1h high, 1d overbought
      & ((df["RSI_3_1h"] > 60.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 80.0) | (df["ROC_9_1d"] < 100.0))
      # 1h down move, 15m & 1h high
      & ((df["RSI_3_1h"] > 65.0) | (df["AROONU_14_15m"] < 70.0) | (df["AROONU_14_1h"] < 100.0))
      # 1h down move, 1h high & overbought
      & ((df["RSI_3_1h"] > 65.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 80.0) | (df["ROC_9_1h"] < 10.0))
      # 4h down move, 1h still high, 1d downtrend
      & ((df["RSI_3_4h"] > 3.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 40.0) | (df["ROC_9_1d"] > -30.0))
      # 4h down move, 1h still high, 4h downtrend
      & ((df["RSI_3_4h"] > 3.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 50.0) | (df["ROC_9_4h"] > -30.0))
      # 4h down move, 4h & 1d downtrend
      & ((df["RSI_3_4h"] > 3.0) | (df["ROC_9_4h"] > -20.0) | (df["ROC_9_1d"] > -20.0))
      # 4h down move, 15m high, 1h still high
      & ((df["RSI_3_4h"] > 5.0) | (df["AROONU_14_15m"] < 70.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 50.0))
      # 4h down move, 15m high
      & ((df["RSI_3_4h"] > 5.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 70.0))
      # 4h down move, 4h still high, 1d downtrend
      & ((df["RSI_3_4h"] > 5.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 40.0) | (df["ROC_9_1d"] > -20.0))
      # 4h & 1d down move, 1d still high
      & ((df["RSI_3_4h"] > 10.0) | (df["RSI_3_1d"] > 20.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 50.0))
      # 4h & 1d down move, 1d downtrend
      & ((df["RSI_3_4h"] > 10.0) | (df["RSI_3_1d"] > 20.0) | (df["ROC_9_1d"] > -20.0))
      # 4h & 1d down move, 4h still high
      & ((df["RSI_3_4h"] > 10.0) | (df["RSI_3_1d"] > 30.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 50.0))
      # 4h & 1d down move, 1d still high
      & ((df["RSI_3_4h"] > 10.0) | (df["RSI_3_1d"] > 35.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 40.0))
      # 4h down move, 15m still not low enough, 1d downtrend
      & ((df["RSI_3_4h"] > 10.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 30.0) | (df["ROC_9_1d"] > -40.0))
      # 4h down move, 15m high, 4h downtrend
      & ((df["RSI_3_4h"] > 10.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 60.0) | (df["ROC_9_4h"] > -50.0))
      # 4h down move, 15m high
      & ((df["RSI_3_4h"] > 10.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 70.0))
      # 4h & 1d down move, 15m high
      & ((df["RSI_3_4h"] > 15.0) | (df["RSI_3_1d"] > 35.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 70.0))
      # 4h & 1d down move, 4h high
      & ((df["RSI_3_4h"] > 15.0) | (df["RSI_3_1d"] > 35.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 70.0))
      # 4h & 1d down move, 1d high
      & ((df["RSI_3_4h"] > 15.0) | (df["RSI_3_1d"] > 40.0) | (df["AROONU_14_1d"] < 70.0))
      # 4h down move, 15m still high, 1h high
      & ((df["RSI_3_4h"] > 15.0) | (df["AROONU_14_15m"] < 50.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 60.0))
      # 4h down move, 15m & 1d high
      & ((df["RSI_3_4h"] > 15.0) | (df["AROONU_14_15m"] < 70.0) | (df["AROONU_14_1d"] < 80.0))
      # 4h down move, 15m high
      & ((df["RSI_3_4h"] > 15.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 80.0))
      # 4h down move, 1d high
      & ((df["RSI_3_4h"] > 15.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 80.0))
      # 4h down move, 1h & 4h downtrend
      & ((df["RSI_3_4h"] > 15.0) | (df["ROC_9_1h"] > -30.0) | (df["ROC_9_4h"] > -30.0))
      # 4h & 1d down move, 1h still high
      & ((df["RSI_3_4h"] > 20.0) | (df["RSI_3_1d"] > 20.0) | (df["AROONU_14_1h"] < 40.0))
      # 4h & 1d down move, 15m high
      & ((df["RSI_3_4h"] > 20.0) | (df["RSI_3_1d"] > 25.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 70.0))
      # 4h & 1d down move, 1d overbought
      & ((df["RSI_3_4h"] > 20.0) | (df["RSI_3_1d"] > 55.0) | (df["ROC_9_1d"] < 50.0))
      # 4h down move, 15m & 4h still high
      & ((df["RSI_3_4h"] > 20.0) | (df["AROONU_14_15m"] < 50.0) | (df["AROONU_14_4h"] < 50.0))
      # 4h down move, 15m high, 1d high
      & ((df["RSI_3_4h"] > 20.0) | (df["AROONU_14_15m"] < 70.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 70.0))
      # 4h down move, 4h still high, 1d downtrend
      & ((df["RSI_3_4h"] > 20.0) | (df["AROONU_14_4h"] < 50.0) | (df["ROC_9_1d"] > -40.0))
      # 4h down move, 1d high & overbought
      & ((df["RSI_3_4h"] > 20.0) | (df["AROONU_14_1d"] < 90.0) | (df["ROC_9_1d"] < 10.0))
      # 4h down move, 15m high, 4h downtrend
      & ((df["RSI_3_4h"] > 20.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 80.0) | (df["ROC_9_4h"] > -50.0))
      # 4h down move, 1h high, 1d downtrend
      & ((df["RSI_3_4h"] > 20.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 60.0) | (df["ROC_9_1d"] > -40.0))
      # 4h down move, 4h still not low enough, 4h downtrend
      & ((df["RSI_3_4h"] > 20.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 30.0) | (df["ROC_9_4h"] > -10.0))
      # 4h down move, 4h high, 1d downtrend
      & ((df["RSI_3_4h"] > 20.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 60.0) | (df["ROC_9_1d"] > -60.0))
      # 4h & 1d down move, 1d high
      & ((df["RSI_3_4h"] > 25.0) | (df["RSI_3_1d"] > 30.0) | (df["AROONU_14_1d"] < 80.0))
      # 4h & 1d down move, 1d overbought
      & ((df["RSI_3_4h"] > 25.0) | (df["RSI_3_1d"] > 40.0) | (df["ROC_9_1d"] < 30.0))
      # 4h down move, 15m still high, 1h high
      & ((df["RSI_3_4h"] > 25.0) | (df["AROONU_14_15m"] < 50.0) | (df["AROONU_14_1h"] < 100.0))
      # 4h down move, 15m & 4h still high
      & ((df["RSI_3_4h"] > 25.0) | (df["AROONU_14_15m"] < 50.0) | (df["AROONU_14_4h"] < 50.0))
      # 4h down move, 15m high, 1d overbought
      & ((df["RSI_3_4h"] > 25.0) | (df["AROONU_14_15m"] < 70.0) | (df["ROC_9_1d"] < 100.0))
      # 4h down move, 1h high, 1d overbought
      & ((df["RSI_3_4h"] > 25.0) | (df["AROONU_14_1h"] < 90.0) | (df["ROC_9_1d"] < 50.0))
      # 4h down move, 4h & 1d high
      & ((df["RSI_3_4h"] > 25.0) | (df["AROONU_14_4h"] < 60.0) | (df["AROONU_14_1d"] < 100.0))
      # 4h down move, 4h high, 1d downtrend
      & ((df["RSI_3_4h"] > 25.0) | (df["AROONU_14_4h"] < 60.0) | (df["ROC_9_1d"] > -70.0))
      # 4h down move, 4h high, 1d downtrend
      & ((df["RSI_3_4h"] > 25.0) | (df["AROONU_14_4h"] < 70.0) | (df["ROC_9_1d"] > -20.0))
      # 4h down move, 4h high, 1d overbought
      & ((df["RSI_3_4h"] > 25.0) | (df["AROONU_14_4h"] < 70.0) | (df["ROC_9_1d"] < 40.0))
      # 4h down move, 1h still high, 1d overbought
      & ((df["RSI_3_4h"] > 25.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 50.0) | (df["ROC_9_1d"] < 100.0))
      # 4h down move, 4h high, 1d downtrend
      & ((df["RSI_3_4h"] > 25.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 80.0) | (df["ROC_9_1d"] > -50.0))
      # 4h down move, 1h high, 1h downtrend
      & ((df["RSI_3_4h"] > 30.0) | (df["AROONU_14_1h"] < 70.0) | (df["ROC_9_1h"] > -10.0))
      # 4h & 1d down move, 1d overbought
      & ((df["RSI_3_4h"] > 30.0) | (df["RSI_3_1d"] > 50.0) | (df["ROC_9_1d"] < 100.0))
      # 4h down move, 1d downtrend, 1d overbought
      & ((df["RSI_3_4h"] > 30.0) | (df["CMF_20_1d"] > -0.30) | (df["ROC_9_1d"] < 40.0))
      # 4h down move, 15m high, 4h high
      & ((df["RSI_3_4h"] > 30.0) | (df["AROONU_14_15m"] < 60.0) | (df["AROONU_14_4h"] < 90.0))
      # 4h down move, 1h high, 1d downtrend
      & ((df["RSI_3_4h"] > 30.0) | (df["AROONU_14_1h"] < 90.0) | (df["ROC_9_1d"] > -20.0))
      # 4h down move, 1h high, 1d downtrend
      & ((df["RSI_3_4h"] > 30.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 80.0) | (df["ROC_9_1d"] > -40.0))
      # 4h down move, 1h high, 1d overbought
      & ((df["RSI_3_4h"] > 30.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 90.0) | (df["ROC_9_1d"] < 50.0))
      # 4h down move, 1d high & overbought
      & ((df["RSI_3_4h"] > 30.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 80.0) | (df["ROC_9_1d"] < 10.0))
      # 4h down move, 15m still high, 1h high
      & ((df["RSI_3_4h"] > 35.0) | (df["AROONU_14_15m"] < 40.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 90.0))
      # 4h down move, 15m still high, 4h high
      & ((df["RSI_3_4h"] > 35.0) | (df["AROONU_14_15m"] < 50.0) | (df["AROONU_14_4h"] < 80.0))
      # 4h down move, 15m high, 1h high
      & ((df["RSI_3_4h"] > 35.0) | (df["AROONU_14_15m"] < 70.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 70.0))
      # 4h down move, 4h & 1d high
      & ((df["RSI_3_4h"] > 35.0) | (df["AROONU_14_4h"] < 80.0) | (df["AROONU_14_1d"] < 100.0))
      # 4h down move, 1d high, 1d downtrend
      & ((df["RSI_3_4h"] > 35.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 60.0) | (df["ROC_9_1d"] > -30.0))
      # 4h down move, 1d high & overbought
      & ((df["RSI_3_4h"] > 35.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 90.0) | (df["ROC_9_1d"] < 40.0))
      # 4h down move, 15m still high, 1d overbought
      & ((df["RSI_3_4h"] > 40.0) | (df["AROONU_14_15m"] < 50.0) | (df["ROC_9_1d"] < 50.0))
      # 4h down move, 15m high, 1d overbought
      & ((df["RSI_3_4h"] > 40.0) | (df["AROONU_14_15m"] < 70.0) | (df["ROC_9_1d"] < 200.0))
      # 4h down move, 1h & 4h high
      & ((df["RSI_3_4h"] > 40.0) | (df["AROONU_14_1h"] < 70.0) | (df["AROONU_14_4h"] < 80.0))
      # 4h down move, 1d high & overbought
      & ((df["RSI_3_4h"] > 40.0) | (df["AROONU_14_1d"] < 100.0) | (df["ROC_9_1d"] < 20.0))
      # 4h down move, 15m high, 1h high
      & ((df["RSI_3_4h"] > 40.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 70.0) | (df["AROONU_14_1h"] < 100.0))
      # 4h down move, 1h high, 1d overbought
      & ((df["RSI_3_4h"] > 40.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 70.0) | (df["ROC_9_1d"] < 60.0))
      # 4h down move, 4h & 1d overbought
      & ((df["RSI_3_4h"] > 40.0) | (df["ROC_9_4h"] < 10.0) | (df["ROC_9_1d"] < 30.0))
      # 4h down move, 15m still high, 4h high
      & ((df["RSI_3_4h"] > 45.0) | (df["AROONU_14_15m"] < 40.0) | (df["AROONU_14_4h"] < 90.0))
      # 45 down move, 15m high, 1h high
      & ((df["RSI_3_4h"] > 45.0) | (df["AROONU_14_15m"] < 70.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 70.0))
      # 4h down move, 15m high, 4h high
      & ((df["RSI_3_4h"] > 45.0) | (df["AROONU_14_15m"] < 70.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 70.0))
      # 4h down move, 4h high, 1d overbought
      & ((df["RSI_3_4h"] > 45.0) | (df["AROONU_14_4h"] < 60.0) | (df["ROC_9_1d"] < 100.0))
      # 4h down move, 4h high & overbought
      & ((df["RSI_3_4h"] > 45.0) | (df["AROONU_14_4h"] < 80.0) | (df["ROC_9_4h"] < 30.0))
      # 4h down move, 1d high & overbought
      & ((df["RSI_3_4h"] > 45.0) | (df["AROONU_14_1d"] < 70.0) | (df["ROC_9_1d"] < 30.0))
      # 4h down move, 1d high, 1d downtrend
      & ((df["RSI_3_4h"] > 45.0) | (df["AROONU_14_1d"] < 80.0) | (df["ROC_9_1d"] > -15.0))
      # 4h down move, 1d high, 4h overbought
      & ((df["RSI_3_4h"] > 45.0) | (df["AROONU_14_1d"] < 90.0) | (df["ROC_9_4h"] < 10.0))
      # 4h down move, 1d high & overbought
      & ((df["RSI_3_4h"] > 45.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 90.0) | (df["ROC_9_1d"] < 20.0))
      # 4h down move, 4h & 1d overbought
      & ((df["RSI_3_4h"] > 45.0) | (df["ROC_9_4h"] < 30.0) | (df["ROC_9_1d"] < 200.0))
      # 4h down move, 15m & 1h high
      & ((df["RSI_3_4h"] > 50.0) | (df["AROONU_14_15m"] < 70.0) | (df["AROONU_14_1h"] < 100.0))
      # 4h down move, 4h still high, 1h high
      & ((df["RSI_3_4h"] > 50.0) | (df["AROONU_14_4h"] < 40.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 70.0))
      # 4h down move, 4h high, 1d overbought
      & ((df["RSI_3_4h"] > 50.0) | (df["AROONU_14_4h"] < 70.0) | (df["ROC_9_1d"] < 40.0))
      # 4h down move, 1d high & overbought
      & ((df["RSI_3_4h"] > 50.0) | (df["AROONU_14_1d"] < 85.0) | (df["ROC_9_1d"] < 80.0))
      # 4h down move, 1d high, 4h overbought
      & ((df["RSI_3_4h"] > 50.0) | (df["AROONU_14_1d"] < 90.0) | (df["ROC_9_4h"] < 10.0))
      # 4h down move, 4h high, 1d downtrend
      & ((df["RSI_3_4h"] > 50.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 60.0) | (df["ROC_9_1d"] > -20.0))
      # 4h down move, 4h downtrend, 1d overbought
      & ((df["RSI_3_4h"] > 50.0) | (df["ROC_9_4h"] > -20.0) | (df["ROC_9_1d"] < 20.0))
      # 4h down move, 1h high, 4h overbought
      & ((df["RSI_3_4h"] > 55.0) | (df["AROONU_14_1h"] < 100.0) | (df["ROC_9_4h"] < 20.0))
      # 4h down move, 4h high & overbought
      & ((df["RSI_3_4h"] > 55.0) | (df["AROONU_14_4h"] < 70.0) | (df["ROC_9_4h"] < 20.0))
      # 4h down move, 1d high & overbought
      & ((df["RSI_3_4h"] > 55.0) | (df["AROONU_14_1d"] < 90.0) | (df["ROC_9_1d"] < 60.0))
      # 4h down move, 4h high & overbought
      & ((df["RSI_3_4h"] > 55.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 80.0) | (df["ROC_9_4h"] < 10.0))
      # 4h down move, 15m high, 1h high
      & ((df["RSI_3_4h"] > 60.0) | (df["AROONU_14_15m"] < 60.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 90.0))
      # 4h down move, 4h high & overbought
      & ((df["RSI_3_4h"] > 60.0) | (df["AROONU_14_4h"] < 70.0) | (df["ROC_9_4h"] < 30.0))
      # 4h down move, 4h still high, 1d downtrend
      & ((df["RSI_3_4h"] > 60.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 50.0) | (df["ROC_9_1d"] > -30.0))
      # 4h down move, 4h & 1d overbought
      & ((df["RSI_3_4h"] > 60.0) | (df["ROC_9_4h"] < 30.0) | (df["ROC_9_1d"] < 50.0))
      # 4h down move, 15m high, 4h high
      & ((df["RSI_3_4h"] > 65.0) | (df["AROONU_14_15m"] < 70.0) | (df["AROONU_14_4h"] < 90.0))
      # 4h down move, 4h high & overbought
      & ((df["RSI_3_4h"] > 65.0) | (df["AROONU_14_4h"] < 80.0) | (df["ROC_9_4h"] < 10.0))
      # 1d down move, 4h & 1d downtrend
      & ((df["RSI_3_1d"] > 3.0) | (df["ROC_9_4h"] > -40.0) | (df["ROC_9_1d"] > -50.0))
      # 1d down move, 15m still high, 4h high
      & ((df["RSI_3_1d"] > 10.0) | (df["AROONU_14_15m"] < 70.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 80.0))
      # 1d down move, 4h & 1d downtrend
      & ((df["RSI_3_1d"] > 10.0) | (df["ROC_9_4h"] > -20.0) | (df["ROC_9_1d"] > -60.0))
      # 1d down move, 4h & 1d downtrend
      & ((df["RSI_3_1d"] > 10.0) | (df["ROC_9_4h"] > -30.0) | (df["ROC_9_1d"] > -50.0))
      # 1d down move, 1h high, 1d downtrend
      & ((df["RSI_3_1d"] > 15.0) | (df["AROONU_14_1h"] < 85.0) | (df["ROC_9_1d"] > -30.0))
      # 1d down move, 4h & 1d downtrend
      & ((df["RSI_3_1d"] > 15.0) | (df["ROC_9_4h"] > -10.0) | (df["ROC_9_1d"] > -40.0))
      # 1d down move, 15m high, 1h high
      & ((df["RSI_3_1d"] > 20.0) | (df["AROONU_14_15m"] < 60.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 80.0))
      # 1d down move, 15m high, 1h high
      & ((df["RSI_3_1d"] > 20.0) | (df["AROONU_14_15m"] < 70.0) | (df["AROONU_14_1h"] < 100.0))
      # 1d down move, 4h high, 4h downtrend
      & ((df["RSI_3_1d"] > 20.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 70.0) | (df["ROC_9_4h"] > -20.0))
      # 1d down move, 15m high, 4h high
      & ((df["RSI_3_1d"] > 25.0) | (df["AROONU_14_15m"] < 70.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 80.0))
      # 1d down move, 15m high, 4h downtrend
      & ((df["RSI_3_1d"] > 25.0) | (df["AROONU_14_15m"] < 70.0) | (df["ROC_9_4h"] > -30.0))
      # 1d down move, 1h & 1d high
      & ((df["RSI_3_1d"] > 25.0) | (df["AROONU_14_1h"] < 80.0) | (df["AROONU_14_1d"] < 80.0))
      # 1d down move, 1d still high, 1d downtrend
      & ((df["RSI_3_1d"] > 25.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 50.0) | (df["ROC_9_1d"] > -20.0))
      # 1d down move, 1d high & overbought
      & ((df["RSI_3_1d"] > 30.0) | (df["AROONU_14_1d"] < 60.0) | (df["ROC_9_1d"] < 10.0))
      # 1d down move, 1h high, 1d downtrend
      & ((df["RSI_3_1d"] > 30.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 70.0) | (df["ROC_9_1d"] < 20.0))
      # 1d down move, 1h & 1d high
      & ((df["RSI_3_1d"] > 35.0) | (df["AROONU_14_1h"] < 70.0) | (df["AROONU_14_1d"] < 90.0))
      # 1d down move, 1h high, 1d overbought
      & ((df["RSI_3_1d"] > 40.0) | (df["AROONU_14_1h"] < 90.0) | (df["ROC_9_1d"] < 80.0))
      # 1d down move, 1d high & overbought
      & ((df["RSI_3_1d"] > 40.0) | (df["AROONU_14_1d"] < 100.0) | (df["ROC_9_1d"] < 30.0))
      # 1d down move, 1d high & overbought
      & ((df["RSI_3_1d"] > 40.0) | (df["AROONU_14_1d"] < 80.0) | (df["ROC_9_1d"] < 10.0))
      # 1d down move, 1h high, 1d overbought
      & ((df["RSI_3_1d"] > 40.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 70.0) | (df["ROC_9_1d"] < 50.0))
      # 15m still high, 4h high, 1d overbought
      & ((df["AROONU_14_15m"] < 50.0) | (df["RSI_14_4h"] < 60.0) | (df["ROC_9_1d"] < 70.0))
      # 15m still high, 1h downtrend, 4h overbought
      & ((df["AROONU_14_15m"] < 50.0) | (df["ROC_9_1h"] > -10.0) | (df["ROC_9_4h"] < 40.0))
      # 15m high, 4h high & overbought
      & ((df["AROONU_14_15m"] < 60.0) | (df["AROONU_14_4h"] < 70.0) | (df["ROC_9_4h"] < 20.0))
      # 15m & 4h high, 1d overbought
      & ((df["AROONU_14_15m"] < 60.0) | (df["AROONU_14_4h"] < 70.0) | (df["ROC_9_1d"] < 10.0))
      # 15m high, 15m & 4h overbought
      & ((df["AROONU_14_15m"] < 60.0) | (df["ROC_9_15m"] < 10.0) | (df["ROC_9_4h"] < 20.0))
      # 15m high, 4h downtrend
      & ((df["AROONU_14_15m"] < 60.0) | (df["ROC_9_4h"] > -30.0))
      # 15m & 1h & 4h high
      & ((df["AROONU_14_15m"] < 70.0) | (df["AROONU_14_1h"] < 100.0) | (df["AROONU_14_4h"] < 100.0))
      # 15m & 4h & 1d high
      & ((df["AROONU_14_15m"] < 70.0) | (df["AROONU_14_4h"] < 70.0) | (df["AROONU_14_1d"] < 90.0))
      # 15m & 4h high, 4h overbought
      & ((df["AROONU_14_15m"] < 70.0) | (df["AROONU_14_4h"] < 70.0) | (df["ROC_9_4h"] < 10.0))
      # 15m & 4h high, 1d downtrend
      & ((df["AROONU_14_15m"] < 70.0) | (df["AROONU_14_4h"] < 70.0) | (df["ROC_9_1d"] > -20.0))
      # 15m & 1d high, 1d overbought
      & ((df["AROONU_14_15m"] < 70.0) | (df["AROONU_14_1d"] < 90.0) | (df["ROC_9_1d"] < 100.0))
      # 15m high, 4h downtrend, 1d overbought
      & ((df["AROONU_14_15m"] < 70.0) | (df["ROC_9_4h"] > -30.0) | (df["ROC_9_1d"] < 200.0))
      # 4h down move, 1h still high, 1d downtrend
      & ((df["RSI_3_4h"] > 15.0) | (df["AROONU_14_1h"] < 40.0) | (df["ROC_9_1d"] > -50.0))
      # 1h high, 1d high & overbought
      & ((df["AROONU_14_1h"] < 90.0) | (df["AROONU_14_1d"] < 100.0) | (df["ROC_9_1d"] < 30.0))
      # 1h high, 4h downtrend
      & ((df["AROONU_14_1h"] < 90.0) | (df["ROC_9_4h"] > -20.0))
      # 1h high, 4h & 1d overbought
      & ((df["AROONU_14_1h"] < 90.0) | (df["ROC_9_4h"] < 10.0) | (df["ROC_9_1d"] < 20.0))
      # 4h & 1d high, 4h overbought
      & ((df["AROONU_14_4h"] < 80.0) | (df["AROONU_14_1d"] < 100.0) | (df["ROC_9_4h"] < 10.0))
      # 4h & 1d high, 1d downtrend
      & ((df["AROONU_14_4h"] < 80.0) | (df["AROONU_14_1d"] < 100.0) | (df["ROC_9_1d"] > -20.0))
      # 1d high, 4h & 1d downtrend
      & ((df["AROONU_14_1d"] < 80.0) | (df["ROC_9_4h"] > -20.0) | (df["ROC_9_1d"] > -20.0))
      # 1d high, 1h & 4h downtrend
      & ((df["AROONU_14_1d"] < 85.0) | (df["ROC_9_1h"] > -30.0) | (df["ROC_9_4h"] > -50.0))
      # 1d high, 4h downtrend
      & ((df["AROONU_14_1d"] < 85.0) | (df["ROC_9_4h"] > -30.0))
      # 1d high, 4h downtrend, 1d overbought
      & ((df["AROONU_14_1d"] < 85.0) | (df["ROC_9_4h"] > -30.0) | (df["ROC_9_1d"] < 70.0))
      # 1d high, 4h & 1d overbought
      & ((df["AROONU_14_1d"] < 100.0) | (df["ROC_9_4h"] < 30.0) | (df["ROC_9_1d"] < 40.0))
      # 15m & 1h high, 1d overbought
      & (
        (df["STOCHRSIk_14_14_3_3_15m"] < 70.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 70.0) | (df["ROC_9_1d"] < 50.0)
      )
      # 15m & 1d high
      & ((df["STOCHRSIk_14_14_3_3_15m"] < 90.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 90.0))
      # 1h high, 4h & 1d downtrend
      & ((df["STOCHRSIk_14_14_3_3_1h"] < 60.0) | (df["ROC_9_4h"] > -30.0) | (df["ROC_9_1d"] > -30.0))
      # 1h high, 4h downtrend
      & ((df["STOCHRSIk_14_14_3_3_1h"] < 70.0) | (df["ROC_9_4h"] > -30.0))
      # 1h high, 1d downtrend
      & ((df["STOCHRSIk_14_14_3_3_1h"] < 70.0) | (df["ROC_9_1d"] > -20.0))
      # 4h high, 4h overbought, 1d downtrend
      & ((df["STOCHRSIk_14_14_3_3_4h"] < 90.0) | (df["ROC_9_4h"] < 20.0) | (df["ROC_9_1d"] > -20.0))
      # 1d still high, 4h & 1d downtrend
      & ((df["STOCHRSIk_14_14_3_3_1d"] < 50.0) | (df["ROC_9_4h"] > -30.0) | (df["ROC_9_1d"] > -30.0))
      # 1d P&D, 4h downtrend
      & ((df["change_pct_1d"] > -50.0) | (df["change_pct_1d"].shift(288) < 50.0) | (df["RSI_3_4h"] > 15.0))
      # 1d P&D, 15m high
      & ((df["change_pct_1d"] > -20.0) | (df["change_pct_1d"].shift(288) < 20.0) | (df["AROONU_14_15m"] < 70.0))
      # 1d red with top wick, 4h high
      & ((df["change_pct_1d"] > -20.0) | (df["top_wick_pct_1d"] < 20.0) | (df["AROONU_14_4h"] < 80.0))
      # 1d red, previous 1d top wick, 15m high
      & (
        (df["change_pct_1d"] > -10.0) | (df["top_wick_pct_1d"].shift(288) < 40.0) | (df["AROONU_14_15m"] < 70.0)
      )
      # 1d green with top wick, 4h overbought
      & ((df["change_pct_1d"] < 15.0) | (df["top_wick_pct_1d"] < 15.0) | (df["ROC_9_4h"] < 20.0))
      # 1d green, 15m down move, 1h high
      & ((df["change_pct_1d"] < 50.0) | (df["RSI_3_15m"] > 25.0) | (df["AROONU_14_1h"] < 70.0))
      # 1d green, 4h down move, 4h still high
      & ((df["change_pct_1d"] < 40.0) | (df["RSI_3_4h"] > 35.0) | (df["AROONU_14_4h"] < 40.0))
      # 1d top wick, 4h down move, 1d overbought
      & ((df["top_wick_pct_1d"] < 50.0) | (df["RSI_3_4h"] > 35.0) | (df["ROC_9_1d"] < 60.0))
      # big drop in the last 20 days, 1d high, 1d downtrend
      & (
        (df["close"] > (df["high_max_20_1d"] * 0.20))
        | (df["STOCHRSIk_14_14_3_3_1d"] < 70.0)
        | (df["ROC_9_1d"] > -15.0)
      )
    )

    # Logic
    long_entry_logic.append(
      (df["RSI_20"] < df["RSI_20"].shift(1))
      & (df["RSI_4"] < 45.0)
      & (df["RSI_14"] > 30.0)
      & (df["AROONU_14"] < 20.0)
      & (df["STOCHRSIk_14_14_3_3"] < 20.0)
      & (df["close"] < df["SMA_16"] * 0.965)
      & (df["close"] < df["SMA_16_1h"] * 0.985)
    )


def append_long_4(df, long_entry_logic, allowed_empty_candles_288) -> None:
    """Append NFI long condition #4, the normal-mode long entry."""
    # Protections
    long_entry_logic.append(df["num_empty_288"] <= allowed_empty_candles_288)
    long_entry_logic.append(df["protections_long_global"] == True)

    long_entry_logic.append(
      (df["RSI_3_15m"] > 3.0)
      # 5m & 1h down move, 1d still high
      & ((df["RSI_3"] > 3.0) | (df["RSI_3_1h"] > 3.0) | (df["AROONU_14_1d"] < 40.0))
      # 5m & 1h & 4h down move
      & ((df["RSI_3"] > 3.0) | (df["RSI_3_1h"] > 5.0) | (df["RSI_3_4h"] > 10.0))
      # 5m & 1h down move, 1h still not low enough
      & ((df["RSI_3"] > 3.0) | (df["RSI_3_1h"] > 10.0) | (df["AROONU_14_1h"] < 30.0))
      # 5m & 1h down move, 1d high
      & ((df["RSI_3"] > 3.0) | (df["RSI_3_1h"] > 15.0) | (df["AROONU_14_1d"] < 80.0))
      # 5m & 1h down move, 1d high
      & ((df["RSI_3"] > 3.0) | (df["RSI_3_1h"] > 20.0) | (df["AROONU_14_1d"] < 100.0))
      # 5m & 1h down move, 1h high
      & ((df["RSI_3"] > 3.0) | (df["RSI_3_1h"] > 50.0) | (df["AROONU_14_1h"] < 70.0))
      # 5m & 1h down move, 1h still high
      & ((df["RSI_3"] > 3.0) | (df["RSI_3_1h"] > 30.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 50.0))
      # 5m & 1h down move, 1d downtrend
      & ((df["RSI_3"] > 3.0) | (df["RSI_3_4h"] > 15.0) | (df["ROC_9_1d"] > -30.0))
      # 5m & 4h down move, 4h high
      & ((df["RSI_3"] > 3.0) | (df["RSI_3_4h"] > 25.0) | (df["AROONU_14_4h"] < 70.0))
      # 5m & 1d down move, 15m still high
      & ((df["RSI_3"] > 3.0) | (df["RSI_3_1d"] > 20.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 40.0))
      # 5m & 4h down move, 15m still high
      & ((df["RSI_3"] > 5.0) | (df["RSI_3_4h"] > 25.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 50.0))
      # 5m down move, 4h high, 1h overbought
      & ((df["RSI_3"] > 10.0) | (df["AROONU_14_4h"] < 100.0) | (df["ROC_9_1h"] < 30.0))
      # 15m & 1h down move, 1d still high
      & ((df["RSI_3_15m"] > 5.0) | (df["RSI_3_1h"] > 5.0) | (df["AROONU_14_1d"] < 40.0))
      # 15m & 1h down move, 1d still high
      & ((df["RSI_3_15m"] > 5.0) | (df["RSI_3_1h"] > 10.0) | (df["AROONU_14_1d"] < 50.0))
      # 15m & 1h down move, 1h still high
      & ((df["RSI_3_15m"] > 5.0) | (df["RSI_3_1h"] > 30.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 40.0))
      # 15m & 1h down move, 4h high
      & ((df["RSI_3_15m"] > 5.0) | (df["RSI_3_1h"] > 40.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 70.0))
      # 15m & 4h down move, 1d overbought
      & ((df["RSI_3_15m"] > 5.0) | (df["RSI_3_4h"] > 15.0) | (df["ROC_9_1d"] < 70.0))
      # 15m & 4h down move, 1d high
      & ((df["RSI_3_15m"] > 5.0) | (df["RSI_3_4h"] > 30.0) | (df["AROONU_14_1d"] < 100.0))
      # 15m & 1h down move, 15m stil high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1h"] > 10.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 50.0))
      # 15m & 1h down move, 4h downtrend
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1h"] > 10.0) | (df["ROC_9_4h"] > -40.0))
      # 15m & 1h down move, 1h still high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1h"] > 15.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 50.0))
      # 15m & 1h down move, 4h high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1h"] > 15.0) | (df["AROONU_14_4h"] < 70.0))
      # 15m & 1h down move, 1d overbought
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1h"] > 20.0) | (df["ROC_9_1d"] < 40.0))
      # 15m & 1h down move, 1h high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1h"] > 25.0) | (df["AROONU_14_1h"] < 80.0))
      # 15m down move, 4h high, 1d overbought
      & ((df["RSI_3_15m"] > 10.0) | (df["AROONU_14_4h"] < 70.0) | (df["ROC_9_1d"] < 100.0))
      # 15m down move, 4h & 1d high
      & ((df["RSI_3_15m"] > 10.0) | (df["AROONU_14_4h"] < 90.0) | (df["AROONU_14_1d"] < 100.0))
      # 15m down move, 1h high, 1d downtrend
      & ((df["RSI_3_15m"] > 10.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 70.0) | (df["ROC_9_1d"] > -50.0))
      # 15m down move, 1h high
      & ((df["RSI_3_15m"] > 10.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 80.0))
      # 15m & 1h down move, 1h still high
      & ((df["RSI_3_15m"] > 15.0) | (df["RSI_3_1h"] > 25.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 40.0))
      # 15m & 4h down move, 1d high
      & ((df["RSI_3_15m"] > 15.0) | (df["RSI_3_4h"] > 15.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 80.0))
      # 15m down move, 4h high & overbought
      & ((df["RSI_3_15m"] > 15.0) | (df["AROONU_14_4h"] < 70.0) | (df["ROC_9_4h"] < 20.0))
      # 15m down move, 4h high & overbought
      & ((df["RSI_3_15m"] > 15.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 90.0) | (df["ROC_9_4h"] < 10.0))
      # 15m down move, 4h & 1d downtrend
      & ((df["RSI_3_15m"] > 15.0) | (df["ROC_9_4h"] > -10.0) | (df["ROC_9_1d"] > -40.0))
      # 15m & 1h down move, 1h high
      & ((df["RSI_3_15m"] > 20.0) | (df["RSI_3_1h"] > 20.0) | (df["AROONU_14_1h"] < 70.0))
      # 15m down move, 4h high, 1d overbought
      & ((df["RSI_3_15m"] > 20.0) | (df["AROONU_14_4h"] < 90.0) | (df["ROC_9_1d"] < 100.0))
      # 15m down move, 4h high, 1h overbought
      & ((df["RSI_3_15m"] > 20.0) | (df["AROONU_14_4h"] < 100.0) | (df["ROC_9_1h"] < 30.0))
      # 15m down move, 1h high & overbought
      & ((df["RSI_3_15m"] > 20.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 90.0) | (df["ROC_9_1h"] < 10.0))
      # 15m & 4h down move, 4h high
      & ((df["RSI_3_15m"] > 25.0) | (df["RSI_3_4h"] > 50.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 80.0))
      # 15m down move, 4h high, 4h overbought
      & ((df["RSI_3_15m"] > 25.0) | (df["AROONU_14_4h"] < 60.0) | (df["ROC_9_4h"] < 50.0))
      # 15m & 1h down move, 4h high
      & ((df["RSI_3_15m"] > 30.0) | (df["RSI_3_1h"] > 40.0) | (df["AROONU_14_4h"] < 85.0))
      # 15m & 1h down move, 4h overbought
      & ((df["RSI_3_15m"] > 40.0) | (df["RSI_3_1h"] > 50.0) | (df["ROC_9_4h"] < 50.0))
      # 1h & 4h down move, 15m downtrend
      & ((df["RSI_3_1h"] > 3.0) | (df["RSI_3_4h"] > 3.0) | (df["ROC_9_15m"] > -30.0))
      # 1h & 4h down move, 15m downtrend
      & ((df["RSI_3_1h"] > 3.0) | (df["RSI_3_4h"] > 10.0) | (df["CMF_20_15m"] > -0.40))
      # 1h & 4h down move, 1d high
      & ((df["RSI_3_1h"] > 3.0) | (df["RSI_3_4h"] > 20.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 70.0))
      # 1h down move, 1h high, 4h high
      & ((df["RSI_3_1h"] > 3.0) | (df["AROONU_14_1h"] < 70.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 80.0))
      # 1h down move, 15m still high
      & ((df["RSI_3_1h"] > 3.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 50.0))
      # 1h down move, 1h still high, 4h overbought
      & ((df["RSI_3_1h"] > 3.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 50.0) | (df["ROC_9_4h"] < 20.0))
      # 1h & 4h & 1d down move
      & ((df["RSI_3_1h"] > 5.0) | (df["RSI_3_4h"] > 5.0) | (df["RSI_3_1d"] > 10.0))
      # 1h & 4h down move, 1h downtrend
      & ((df["RSI_3_1h"] > 5.0) | (df["RSI_3_4h"] > 5.0) | (df["ROC_9_1h"] > -20.0))
      # 1h & 4h down move, 1d downtrend
      & ((df["RSI_3_1h"] > 5.0) | (df["RSI_3_4h"] > 10.0) | (df["ROC_9_1d"] > -40.0))
      # 1h down move, 4h high, 1h downtrend
      & ((df["RSI_3_1h"] > 5.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 70.0) | (df["ROC_9_1h"] > -40.0))
      # 1h down move, 4h high, 1h downtrend
      & ((df["RSI_3_1h"] > 5.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 70.0) | (df["CMF_20_1h"] > -0.40))
      # 1h down move, 1d high & overbought
      & ((df["RSI_3_1h"] > 5.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 90.0) | (df["ROC_9_1d"] < 20.0))
      # 1h down move, 1d overbought
      & ((df["RSI_3_1h"] > 5.0) | (df["ROC_9_1d"] < 100.0))
      # 1h & 4h & 1d down move
      & ((df["RSI_3_1h"] > 10.0) | (df["RSI_3_4h"] > 10.0) | (df["RSI_3_1d"] > 15.0))
      # 1h & 4h down move, 4h still high
      & ((df["RSI_3_1h"] > 10.0) | (df["RSI_3_4h"] > 15.0) | (df["RSI_14_4h"] < 40.0))
      # 1h & 4h down move, 1h downtrend
      & ((df["RSI_3_1h"] > 10.0) | (df["RSI_3_4h"] > 15.0) | (df["ROC_9_1h"] > -20.0))
      # 1h & 4h down move, 1h still high
      & ((df["RSI_3_1h"] > 10.0) | (df["RSI_3_4h"] > 20.0) | (df["AROONU_14_1h"] < 50.0))
      # 1h & 4h down move, 4h still high
      & ((df["RSI_3_1h"] > 10.0) | (df["RSI_3_4h"] > 35.0) | (df["RSI_14_4h"] < 40.0))
      # 1h & 3h down move, 1d high
      & ((df["RSI_3_1h"] > 10.0) | (df["RSI_3_4h"] > 40.0) | (df["AROONU_14_1d"] < 80.0))
      # 1h & 1d down move, 1d high
      & ((df["RSI_3_1h"] > 10.0) | (df["RSI_3_1d"] > 45.0) | (df["AROONU_14_1d"] < 70.0))
      # 1h down move, 4h high
      & ((df["RSI_3_1h"] > 10.0) | (df["AROONU_14_4h"] < 85.0))
      # 1h down move, 1d high, 15m downtrend
      & ((df["RSI_3_1h"] > 10.0) | (df["AROONU_14_1d"] < 70.0) | (df["ROC_9_15m"] > -50.0))
      # 1h down move, 4h & 1d downtrend
      & ((df["RSI_3_1h"] > 10.0) | (df["ROC_9_4h"] > -15.0) | (df["ROC_9_1d"] > -30.0))
      # 1h & 4h down move, 4h still high
      & ((df["RSI_3_1h"] > 15.0) | (df["RSI_3_4h"] > 15.0) | (df["RSI_14_4h"] < 40.0))
      # 1h & 4h down move, 1h still not low enough
      & ((df["RSI_3_1h"] > 15.0) | (df["RSI_3_4h"] > 15.0) | (df["AROONU_14_1h"] < 20.0))
      # 1h & 4h down move, 4h still not low enough
      & ((df["RSI_3_1h"] > 15.0) | (df["RSI_3_4h"] > 25.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 30.0))
      # 1h & 1d down move, 1d still high
      & ((df["RSI_3_1h"] > 15.0) | (df["RSI_3_1d"] > 20.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 40.0))
      # 1h & 1d down move, 1d high
      & ((df["RSI_3_1h"] > 15.0) | (df["RSI_3_1d"] > 25.0) | (df["AROONU_14_1d"] < 80.0))
      # 1h down move, 1h still high, 4h downtrend
      & ((df["RSI_3_1h"] > 15.0) | (df["AROONU_14_1h"] < 40.0) | (df["ROC_9_4h"] > -30.0))
      # 1h down move, 1d high, 4h downtrend
      & ((df["RSI_3_1h"] > 15.0) | (df["AROONU_14_1d"] < 90.0) | (df["ROC_9_4h"] > -20.0))
      # 1h down move, 1d high & overbought
      & ((df["RSI_3_1h"] > 15.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 90.0) | (df["ROC_9_1d"] < 40.0))
      # 1h down move, 1h still high, 4h downtrend
      & ((df["RSI_3_1h"] > 20.0) | (df["AROONU_14_1h"] < 50.0) | (df["ROC_9_4h"] > -50.0))
      # 1h down move, 1h high
      & ((df["RSI_3_1h"] > 20.0) | (df["AROONU_14_1h"] < 80.0))
      # 1h down move, 1h still high, 1d overbought
      & ((df["RSI_3_1h"] > 25.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 50.0) | (df["ROC_9_1d"] < 40.0))
      # 1h down move, 1h & 4h high
      & ((df["RSI_3_1h"] > 30.0) | (df["AROONU_14_1h"] < 70.0) | (df["AROONU_14_4h"] < 70.0))
      # 1h down move, 4h high, 1d overbought
      & ((df["RSI_3_1h"] > 30.0) | (df["AROONU_14_4h"] < 80.0) | (df["ROC_9_1d"] < 30.0))
      # 1h down move, 1d high & overbought
      & ((df["RSI_3_1h"] > 30.0) | (df["AROONU_14_1d"] < 80.0) | (df["ROC_9_1d"] < 200.0))
      # 1h & 4h down move, 1d overbought
      & ((df["RSI_3_1h"] > 30.0) | (df["RSI_3_4h"] > 30.0) | (df["ROC_9_1d"] < 40.0))
      # 1h & 4h down move, 15m high
      & ((df["RSI_3_1h"] > 30.0) | (df["RSI_3_4h"] > 40.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 80.0))
      # 1h & 4h down move, 1h high
      & ((df["RSI_3_1h"] > 30.0) | (df["RSI_3_4h"] > 50.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 70.0))
      # 1h down move, 15m still high, 1h high
      & ((df["RSI_3_1h"] > 30.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 40.0) | (df["AROONU_14_1h"] < 60.0))
      # 1h down move, 1h still high, 4h high
      & ((df["RSI_3_1h"] > 30.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 40.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 70.0))
      # 1h down move, 4h & 1d downtrend
      & ((df["RSI_3_1h"] > 30.0) | (df["ROC_9_4h"] > -25.0) | (df["ROC_9_1d"] > -60.0))
      # 1h down move, 4h & 1d overbought
      & ((df["RSI_3_1h"] > 30.0) | (df["ROC_9_4h"] < 20.0) | (df["ROC_9_1d"] < 100.0))
      # 1h down move, 1h high, 1d overbought
      & ((df["RSI_3_1h"] > 35.0) | (df["AROONU_14_1h"] < 70.0) | (df["ROC_9_1d"] < 20.0))
      # 1h down move, 4h high, 1d overbought
      & ((df["RSI_3_1h"] > 35.0) | (df["AROONU_14_4h"] < 85.0) | (df["ROC_9_1d"] < 100.0))
      # 1h down move, 1h still high, 1d overbought
      & ((df["RSI_3_1h"] > 35.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 50.0) | (df["ROC_9_1d"] < 200.0))
      # 1h down move, 1h & 4h high
      & ((df["RSI_3_1h"] > 45.0) | (df["AROONU_14_1h"] < 70.0) | (df["AROONU_14_4h"] < 100.0))
      # 1h down move, 4h high, 1d downtrend
      & ((df["RSI_3_1h"] > 50.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 60.0) | (df["ROC_9_1d"] > -60.0))
      # 1h down move, 4h high & overbought
      & ((df["RSI_3_1h"] > 50.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 90.0) | (df["ROC_9_4h"] < 40.0))
      # 1h down move, 1h high & overbought
      & ((df["RSI_3_1h"] > 55.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 80.0) | (df["ROC_9_1h"] < 10.0))
      # 1h down move, 4h & 1d overbought
      & ((df["RSI_3_1h"] > 60.0) | (df["ROC_9_4h"] < 30.0) | (df["ROC_9_1d"] < 60.0))
      # 4h down move, 4h high, 4h downtrend
      & ((df["RSI_3_4h"] > 3.0) | (df["AROONU_14_4h"] < 50.0) | (df["ROC_9_4h"] > -40.0))
      # 4h & 1d down move, 1h still not low enough
      & ((df["RSI_3_4h"] > 5.0) | (df["RSI_3_1d"] > 10.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 30.0))
      # 4h & 1d down move, 1d high
      & ((df["RSI_3_4h"] > 5.0) | (df["RSI_3_1d"] > 45.0) | (df["AROONU_14_1d"] < 70.0))
      # 4h down move, 4h & 1d downtrend
      & ((df["RSI_3_4h"] > 5.0) | (df["ROC_9_4h"] > -15.0) | (df["ROC_9_1d"] > -20.0))
      # 4h & 1d down move, 1h still high
      & ((df["RSI_3_4h"] > 10.0) | (df["RSI_3_1d"] > 10.0) | (df["AROONU_14_1h"] < 40.0))
      # 4h & 1d down move, 1h high
      & ((df["RSI_3_4h"] > 10.0) | (df["RSI_3_1d"] > 15.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 70.0))
      # 4h & 1d down move, 1d still high
      & ((df["RSI_3_4h"] > 10.0) | (df["RSI_3_1d"] > 25.0) | (df["AROONU_14_1d"] < 40.0))
      # 4h & 1d down move, 1d still high
      & ((df["RSI_3_4h"] > 10.0) | (df["RSI_3_1d"] > 25.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 50.0))
      # 4h & 1d down move, 1d high
      & ((df["RSI_3_4h"] > 15.0) | (df["RSI_3_1d"] > 20.0) | (df["AROONU_14_1d"] < 60.0))
      # 4h & 1d down move, 4h high
      & ((df["RSI_3_4h"] > 15.0) | (df["RSI_3_1d"] > 25.0) | (df["AROONU_14_4h"] < 70.0))
      # 4h down move, 1d high & overbought
      & ((df["RSI_3_4h"] > 15.0) | (df["AROONU_14_1d"] < 90.0) | (df["ROC_9_1d"] < 20.0))
      # 4h down move, 4h still high, 1d downtrend
      & ((df["RSI_3_4h"] > 20.0) | (df["AROONU_14_4h"] < 50.0) | (df["ROC_9_1d"] > -10.0))
      # 4h down move, 1d high & overbought
      & ((df["RSI_3_4h"] > 20.0) | (df["AROONU_14_1d"] < 80.0) | (df["ROC_9_1d"] < 80.0))
      # 4h down move, 4h & 1d downtrend
      & ((df["RSI_3_4h"] > 20.0) | (df["ROC_9_4h"] > -20.0) | (df["ROC_9_1d"] > -30.0))
      # 4h down move, 4h still high, 1d downtrend
      & ((df["RSI_3_4h"] > 30.0) | (df["AROONU_14_4h"] < 50.0) | (df["ROC_9_1d"] > -40.0))
      # 4h down move, 1d high & overbought
      & ((df["RSI_3_4h"] > 40.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 90.0) | (df["ROC_9_1d"] < 200.0))
      # 4h down move, 4h high, 1d downtrend
      & ((df["RSI_3_4h"] > 45.0) | (df["AROONU_14_4h"] < 70.0) | (df["ROC_9_1d"] > -30.0))
      # 4h down move, 4h high & overbought
      & ((df["RSI_3_4h"] > 60.0) | (df["AROONU_14_4h"] < 70.0) | (df["ROC_9_4h"] < 20.0))
      # 4h down move, 4h & 1d overbought
      & ((df["RSI_3_4h"] > 60.0) | (df["ROC_9_4h"] < 20.0) | (df["ROC_9_1d"] < 20.0))
      # 1h still high, 4h & 1d downtrend
      & ((df["AROONU_14_1h"] < 40.0) | (df["ROC_9_4h"] > -20.0) | (df["ROC_9_1d"] > -40.0))
      # 1h & 4h high, 1h overbought
      & ((df["AROONU_14_1h"] < 70.0) | (df["AROONU_14_4h"] < 100.0) | (df["ROC_9_1h"] < 80.0))
      # 1h high, 1d overbought
      & ((df["AROONU_14_1h"] < 70.0) | (df["ROC_9_1d"] < 70.0))
      # 1h & 4h high, 1h overbought
      & ((df["AROONU_14_1h"] < 80.0) | (df["AROONU_14_4h"] < 90.0) | (df["ROC_9_1h"] < 30.0))
      # 1h & 1d high, 1h overbought
      & ((df["AROONU_14_1h"] < 80.0) | (df["AROONU_14_1d"] < 90.0) | (df["ROC_9_1h"] < 30.0))
      # 4h still not low enough, 4h & 1d downtrend
      & ((df["AROONU_14_4h"] < 30.0) | (df["ROC_9_4h"] > -40.0) | (df["ROC_9_1d"] > -40.0))
      # 4h still high, 5m downtrend
      & ((df["AROONU_14_4h"] < 40.0) | (df["ROC_9"] > -40.0))
      # 4h high, 4h & 1d overbought
      & ((df["AROONU_14_4h"] < 60.0) | (df["ROC_9_4h"] < 30.0) | (df["ROC_9_1d"] < 50.0))
      # 4h & 1d high, 4h overbought
      & ((df["AROONU_14_4h"] < 80.0) | (df["AROONU_14_1d"] < 100.0) | (df["ROC_9_4h"] < 50.0))
      # 4h high, 1h & 1d overbought
      & ((df["AROONU_14_4h"] < 100.0) | (df["ROC_9_1h"] < 30.0) | (df["ROC_9_1d"] < 100.0))
      # 4h high, 1h & 4h high
      & ((df["AROONU_14_4h"] < 100.0) | (df["ROC_9_1h"] < 50.0) | (df["ROC_9_4h"] < 100.0))
      # 1d high, 4h & 1d downtrend
      & ((df["AROONU_14_1d"] < 70.0) | (df["ROC_9_4h"] > -40.0) | (df["ROC_9_1d"] > -40.0))
      # 1d high, 1h & 1d overbought
      & ((df["AROONU_14_1d"] < 80.0) | (df["ROC_9_1h"] < 30.0) | (df["ROC_9_1d"] < 200.0))
      # 1d high, 4h & 1d overbought
      & ((df["AROONU_14_1d"] < 90.0) | (df["ROC_9_4h"] < 20.0) | (df["ROC_9_1d"] < 50.0))
      # 1h high, 4h overbought
      & ((df["STOCHRSIk_14_14_3_3_1h"] < 80.0) | (df["ROC_9_4h"] < 80.0))
      # 4h & 1d overbought
      & ((df["ROC_9_4h"] < 100.0) | (df["ROC_9_1d"] < 200.0))
      # big drop in the last 20 days, 1d high, 1d downtrend
      & (
        (df["close"] > (df["high_max_20_1d"] * 0.20))
        | (df["STOCHRSIk_14_14_3_3_1d"] < 70.0)
        | (df["ROC_9_1d"] > -15.0)
      )
      # drop in last 20 days, 1h high, 1d downtrend
      & ((df["close"] > (df["high_max_20_1d"] * 0.20)) | (df["AROONU_14_1h"] < 70.0) | (df["ROC_9_1d"] > -70.0))
    )

    # Logic
    long_entry_logic.append(
      (df["AROONU_14"] < 25.0)
      & (df["AROONU_14_15m"] < 25.0)
      & (df["close"] < (df["EMA_9"] * 0.946))
      & (df["close"] < (df["EMA_20"] * 0.960))
    )


def append_long_5(df, long_entry_logic, allowed_empty_candles_288) -> None:
    """Append NFI long condition #5, the normal-mode long entry."""
    # Protections
    long_entry_logic.append(df["num_empty_288"] <= allowed_empty_candles_288)
    long_entry_logic.append(df["protections_long_global"] == True)

    long_entry_logic.append(
      (df["RSI_3_15m"] > 20.0)
      # 5m & 1h down move, 1h still not low enough
      & ((df["RSI_3"] > 3.0) | (df["RSI_3_1h"] > 10.0) | (df["AROONU_14_1h"] < 30.0))
      # 5m & 1h down move, 1d high
      & ((df["RSI_3"] > 3.0) | (df["RSI_3_1h"] > 20.0) | (df["AROONU_14_1d"] < 100.0))
      # 5m & 1h down move, 1h still high
      & ((df["RSI_3"] > 3.0) | (df["RSI_3_1h"] > 30.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 50.0))
      # 5m & 4h down move, 15m still high
      & ((df["RSI_3"] > 3.0) | (df["RSI_3_4h"] > 3.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 40.0))
      # 15m & 1h down move, 4h high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1h"] > 30.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 60.0))
      # 15m & 1h down move, 1h still high
      & ((df["RSI_3_15m"] > 25.0) | (df["RSI_3_1h"] > 25.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 50.0))
      # 1h & 4h down move, 4h high
      & ((df["RSI_3_15m"] > 25.0) | (df["RSI_3_1h"] > 25.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 80.0))
      # 15m & 1h down move, 4h overbought
      & ((df["RSI_3_15m"] > 25.0) | (df["RSI_3_1h"] > 30.0) | (df["ROC_9_4h"] < 70.0))
      # 15m & 1h down move, 1h high
      & ((df["RSI_3_15m"] > 25.0) | (df["RSI_3_1h"] > 40.0) | (df["AROONU_14_1h"] < 80.0))
      # 15m & 1h down move, 1h high
      & ((df["RSI_3_15m"] > 25.0) | (df["RSI_3_1h"] > 50.0) | (df["AROONU_14_1h"] < 85.0))
      # 15m & 1h down move, 1h high
      & ((df["RSI_3_15m"] > 25.0) | (df["RSI_3_1h"] > 55.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 80.0))
      # 15m down move, 15m stil not low enough, 4h high
      & ((df["RSI_3_15m"] > 25.0) | (df["AROONU_14_15m"] < 30.0) | (df["AROONU_14_4h"] < 60.0))
      # 15m down move, 15m high, 1h high
      & ((df["RSI_3_15m"] > 25.0) | (df["AROONU_14_15m"] < 60.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 70.0))
      # 15m down move, 4h & 1d overbought
      & ((df["RSI_3_15m"] > 25.0) | (df["ROC_9_4h"] < 10.0) | (df["ROC_9_1d"] < 50.0))
      # 15m & 4h down move, 4h high
      & ((df["RSI_3_15m"] > 30.0) | (df["RSI_3_4h"] > 50.0) | (df["AROONU_14_4h"] < 80.0))
      # 15m & 1h down move, 1h high
      & ((df["RSI_3_15m"] > 30.0) | (df["RSI_3_1h"] > 30.0) | (df["AROONU_14_1h"] < 85.0))
      # 15m down move, 15m still high, 1d high
      & ((df["RSI_3_15m"] > 30.0) | (df["AROONU_14_15m"] < 50.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 70.0))
      # 15m down move, 15m high, 4h high
      & ((df["RSI_3_15m"] > 30.0) | (df["AROONU_14_15m"] < 60.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 70.0))
      # 15m down move, 1h & 4h high
      & ((df["RSI_3_15m"] > 30.0) | (df["AROONU_14_1h"] < 85.0) | (df["AROONU_14_4h"] < 100.0))
      # 15m down move, 4h & 1d high
      & ((df["RSI_3_15m"] > 30.0) | (df["AROONU_14_4h"] < 80.0) | (df["AROONU_14_1d"] < 100.0))
      # 15m down move, 4h high, 1h downtrend
      & ((df["RSI_3_15m"] < 30.0) | (df["AROONU_14_4h"] < 85.0) | (df["ROC_9_1h"] > -40.0))
      # 15m down move, 4h high & overbought
      & ((df["RSI_3_15m"] > 30.0) | (df["AROONU_14_4h"] < 100.0) | (df["ROC_9_4h"] < 25.0))
      # 15m & 4h down move, 4h high
      & ((df["RSI_3_15m"] > 35.0) | (df["RSI_3_4h"] > 35.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 80.0))
      # 15m down move, 15m high, 4h overbought
      & ((df["RSI_3_15m"] > 35.0) | (df["AROONU_14_15m"] < 70.0) | (df["ROC_9_4h"] < 10.0))
      # 15m down move, 1h high, 4h overbought
      & ((df["RSI_3_15m"] > 35.0) | (df["AROONU_14_1h"] < 85.0) | (df["ROC_9_4h"] < 80.0))
      # 15m down move, 4h high, 1h overbought
      & ((df["RSI_3_15m"] > 35.0) | (df["AROONU_14_4h"] < 100.0) | (df["ROC_9_1h"] < 20.0))
      # 15m & 1h down move, 1h high
      & ((df["RSI_3_15m"] > 40.0) | (df["RSI_3_1h"] > 40.0) | (df["AROONU_14_1h"] < 100.0))
      # 15m down move, 15m still high, 1h high
      & ((df["RSI_3_15m"] > 45.0) | (df["AROONU_14_15m"] < 50.0) | (df["AROONU_14_1h"] < 85.0))
      # 1h & 4h down move, 1d high
      & ((df["RSI_3_1h"] > 3.0) | (df["RSI_3_4h"] > 5.0) | (df["AROONU_14_1d"] < 70.0))
      # 1h & 4h down move, 4h still high
      & ((df["RSI_3_1h"] > 3.0) | (df["RSI_3_4h"] > 10.0) | (df["AROONU_14_4h"] < 40.0))
      # 1h & 4h down move, 1d overbought
      & ((df["RSI_3_1h"] > 3.0) | (df["RSI_3_4h"] > 10.0) | (df["ROC_9_1d"] < 15.0))
      # 1h & 4h down move, 4h downtrend
      & ((df["RSI_3_1h"] > 3.0) | (df["RSI_3_4h"] > 15.0) | (df["ROC_9_4h"] > -40.0))
      # 1h & 4h down move, 1d downtrend
      & ((df["RSI_3_1h"] > 3.0) | (df["RSI_3_4h"] > 25.0) | (df["ROC_9_1d"] > -50.0))
      # 1h & 1d down move, 1d high
      & ((df["RSI_3_1h"] > 3.0) | (df["RSI_3_1d"] > 25.0) | (df["AROONU_14_1d"] < 80.0))
      # 1h & 4h down move, 1h downtrend
      & ((df["RSI_3_1h"] > 5.0) | (df["RSI_3_4h"] > 20.0) | (df["ROC_9_1h"] > -15.0))
      # 1h & 4h down move, 4h still high
      & ((df["RSI_3_1h"] > 10.0) | (df["RSI_3_4h"] > 10.0) | (df["AROONU_14_4h"] < 50.0))
      # 1h & 4h down move, 15m still high
      & ((df["RSI_3_1h"] > 10.0) | (df["RSI_3_4h"] > 10.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 50.0))
      # 1h & 4h down move, 1h downtrend
      & ((df["RSI_3_1h"] > 10.0) | (df["RSI_3_4h"] > 10.0) | (df["ROC_9_1h"] > -20.0))
      # 1h & 4h & 1d down move
      & ((df["RSI_3_1h"] > 10.0) | (df["RSI_3_4h"] > 15.0) | (df["RSI_3_1d"] > 15.0))
      # 1h & 4h down move, 15m high
      & ((df["RSI_3_1h"] > 10.0) | (df["RSI_3_4h"] > 15.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 70.0))
      # 1h & 4h down move, 4h high
      & ((df["RSI_3_1h"] > 10.0) | (df["RSI_3_4h"] > 15.0) | (df["AROONU_14_4h"] < 60.0))
      # 1h & 4h down move, 1d overbought
      & ((df["RSI_3_1h"] > 10.0) | (df["RSI_3_4h"] > 30.0) | (df["ROC_9_1d"] < 100.0))
      # 1h & 4h down move, 4h still high
      & ((df["RSI_3_1h"] > 10.0) | (df["RSI_3_4h"] > 45.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 40.0))
      # 1h down move, 4h downtrend. 4h still not low enough
      & ((df["RSI_3_1h"] > 10.0) | (df["ROC_9_4h"] > -20.0) | (df["AROONU_14_4h"] < 30.0))
      # 1h down move, 15m still high, 4h high
      & ((df["RSI_3_1h"] > 10.0) | (df["AROONU_14_15m"] < 40.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 90.0))
      # 1h down move, 15m high, 4h downtrend
      & ((df["RSI_3_1h"] > 10.0) | (df["AROONU_14_15m"] < 70.0) | (df["ROC_9_4h"] > -10.0))
      # 1h down move, 1h still high, 15m downtrend
      & ((df["RSI_3_1h"] > 10.0) | (df["AROONU_14_1h"] < 40.0) | (df["CMF_20_15m"] > -0.30))
      # 1h down move, 1d high, 4h overbought
      & ((df["RSI_3_1h"] > 10.0) | (df["AROONU_14_1d"] < 100.0) | (df["ROC_9_4h"] < 20.0))
      # 1h down move, 1h still high, 1d downtrend
      & ((df["RSI_3_1h"] > 10.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 50.0) | (df["ROC_9_1d"] > -40.0))
      # 1h down move, 1d high & overbought
      & ((df["RSI_3_1h"] > 10.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 80.0) | (df["ROC_9_1d"] < 30.0))
      # 1h & 4h down move, 1h still high
      & ((df["RSI_3_1h"] > 15.0) | (df["RSI_3_4h"] > 15.0) | (df["AROONU_14_1h"] < 50.0))
      # 1h & 4h down move, 1h still not low enough
      & ((df["RSI_3_1h"] > 15.0) | (df["RSI_3_4h"] > 15.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 30.0))
      # 1h & 4h down move, 1d downtrend
      & ((df["RSI_3_1h"] > 15.0) | (df["RSI_3_4h"] > 20.0) | (df["ROC_9_1d"] > -40.0))
      # 1h & 4h down move, 4h high
      & ((df["RSI_3_1h"] > 15.0) | (df["RSI_3_4h"] > 50.0) | (df["AROONU_14_4h"] < 100.0))
      # 1h & 1d down move, 4h high
      & ((df["RSI_3_1h"] > 15.0) | (df["RSI_3_1d"] > 15.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 80.0))
      # 1h down move, 4h high, 1d overbought
      & ((df["RSI_3_1h"] > 15.0) | (df["AROONU_14_4h"] < 60.0) | (df["ROC_9_1d"] < 50.0))
      # 1h down move, 4h high, 1d high
      & ((df["RSI_3_1h"] > 15.0) | (df["AROONU_14_4h"] < 80.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 80.0))
      # 1h down move, 1d high, 1d downtrend
      & ((df["RSI_3_1h"] > 15.0) | (df["AROONU_14_1d"] < 70.0) | (df["ROC_9_1d"] > -20.0))
      # 1h down move, 1d high, 4h overbought
      & ((df["RSI_3_1h"] > 15.0) | (df["AROONU_14_1d"] < 100.0) | (df["ROC_9_4h"] < 60.0))
      # 1h down move, 1d high & overbought
      & ((df["RSI_3_1h"] > 15.0) | (df["AROONU_14_1d"] < 100.0) | (df["ROC_9_1d"] < 10.0))
      # 1h down move, 4h & 1d overbought
      & ((df["RSI_3_1h"] > 15.0) | (df["ROC_9_4h"] < 10.0) | (df["ROC_9_1d"] < 60.0))
      # 1h & 4h down move, 4h high
      & ((df["RSI_3_1h"] > 20.0) | (df["RSI_3_4h"] > 20.0) | (df["AROONU_14_4h"] < 70.0))
      # 1h & 4h down move, 4h high
      & ((df["RSI_3_1h"] > 20.0) | (df["RSI_3_4h"] > 40.0) | (df["AROONU_14_4h"] < 80.0))
      # 1h & 1d down move, 1h still high
      & ((df["RSI_3_1h"] > 20.0) | (df["RSI_3_1d"] > 30.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 50.0))
      # 1h & 4h down move, 15m high
      & ((df["RSI_3_1h"] > 25.0) | (df["RSI_3_4h"] > 25.0) | (df["AROONU_14_15m"] < 70.0))
      # 1h down move, 4h downtrend, 4h high
      & ((df["RSI_3_1h"] > 25.0) | (df["CMF_20_4h"] > -0.50) | (df["AROONU_14_4h"] < 70.0))
      # 1h down move, 1d high & overbought
      & ((df["RSI_3_1h"] > 25.0) | (df["AROONU_14_1d"] < 90.0) | (df["ROC_9_1d"] < 30.0))
      # 1h down move, 4h high, 1d downtrend
      & ((df["RSI_3_1h"] > 25.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 80.0) | (df["ROC_9_1d"] > -30.0))
      # 1h & 4h down move, 4h high
      & ((df["RSI_3_1h"] > 30.0) | (df["RSI_3_4h"] > 50.0) | (df["AROONU_14_4h"] < 85.0))
      # 1h down move, 1h & 4h high
      & ((df["RSI_3_1h"] > 30.0) | (df["AROONU_14_1h"] < 70.0) | (df["AROONU_14_4h"] < 85.0))
      # 1h down move, 1h high, 4h overbought
      & ((df["RSI_3_1h"] > 30.0) | (df["AROONU_14_1h"] < 70.0) | (df["ROC_9_4h"] < 20.0))
      # 1h down move, 4h high, 1d overbought
      & ((df["RSI_3_1h"] > 30.0) | (df["AROONU_14_4h"] < 80.0) | (df["ROC_9_1d"] < 30.0))
      # 1h down move, 4h high & overbought
      & ((df["RSI_3_1h"] > 30.0) | (df["AROONU_14_4h"] < 90.0) | (df["ROC_9_4h"] < 100.0))
      # 1h down move, 15m still high, 1h high
      & ((df["RSI_3_1h"] > 30.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 40.0) | (df["AROONU_14_1h"] < 60.0))
      # 1h down move, 1h high, 1d downtrend
      & ((df["RSI_3_1h"] > 30.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 70.0) | (df["ROC_9_1d"] > -40.0))
      # 1h down move, 4h high, 1d downtrend
      & ((df["RSI_3_1h"] > 30.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 90.0) | (df["ROC_9_1d"] > -50.0))
      # 1h down move, 4h downtrend, 1d over
      & ((df["RSI_3_1h"] > 30.0) | (df["ROC_9_4h"] > -30.0) | (df["ROC_9_1d"] < 50.0))
      # 1h down move, 1h still high, 1d overbought
      & ((df["RSI_3_1h"] > 35.0) | (df["AROONU_14_1h"] < 50.0) | (df["ROC_9_1d"] < 20.0))
      # 1h down move, 1h & 4h high
      & ((df["RSI_3_1h"] > 35.0) | (df["AROONU_14_1h"] < 70.0) | (df["AROONU_14_4h"] < 100.0))
      # 1h down move, 1h high, 1d downtrend
      & ((df["RSI_3_1h"] > 35.0) | (df["AROONU_14_1h"] < 70.0) | (df["ROC_9_1d"] > -25.0))
      # 1h down move, 1h high, 4h downtrend
      & ((df["RSI_3_1h"] > 35.0) | (df["AROONU_14_1h"] < 80.0) | (df["ROC_9_4h"] > -20.0))
      # 1h down move, 1h still high, 1d overbought
      & ((df["RSI_3_1h"] > 35.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 50.0) | (df["ROC_9_1d"] < 200.0))
      # 1h down move, 15m high, 1h high
      & ((df["RSI_3_1h"] > 40.0) | (df["AROONU_14_15m"] < 60.0) | (df["AROONU_14_1h"] < 70.0))
      # 1h down move, 1h still high, 1d overbought
      & ((df["RSI_3_1h"] > 40.0) | (df["AROONU_14_1h"] < 40.0) | (df["ROC_9_1d"] < 100.0))
      # 1h down move, 1h & 4h high
      & ((df["RSI_3_1h"] > 40.0) | (df["AROONU_14_1h"] < 80.0) | (df["AROONU_14_4h"] < 100.0))
      # 1h down move, 1d high & overbought
      & ((df["RSI_3_1h"] > 40.0) | (df["AROONU_14_1d"] < 80.0) | (df["ROC_9_1d"] < 50.0))
      # 1h down move, 1h & 4h overbought
      & ((df["RSI_3_1h"] > 40.0) | (df["ROC_9_1h"] < 20.0) | (df["ROC_9_4h"] < 20.0))
      # 1h & 4h down move, 1d overbought
      & ((df["RSI_3_1h"] > 45.0) | (df["RSI_3_4h"] > 65.0) | (df["ROC_9_1d"] < 200.0))
      # 1h down move, 15m still high, 1h high
      & ((df["RSI_3_1h"] > 45.0) | (df["AROONU_14_15m"] < 50.0) | (df["AROONU_14_1h"] < 85.0))
      # 1h down move, 1h high, 4h overbought
      & ((df["RSI_3_1h"] > 45.0) | (df["AROONU_14_1h"] < 80.0) | (df["ROC_9_4h"] < 50.0))
      # 1h down move, 1h high, 1d overbought
      & ((df["RSI_3_1h"] > 45.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 70.0) | (df["ROC_9_1d"] < 50.0))
      # 1h down move, 1h high, 1d downtrend
      & ((df["RSI_3_1h"] > 50.0) | (df["AROONU_14_1h"] < 90.0) | (df["ROC_9_1d"] > -30.0))
      # 1h down move, 4h high, 1h overbought
      & ((df["RSI_3_1h"] > 50.0) | (df["AROONU_14_4h"] < 90.0) | (df["ROC_9_1h"] < 40.0))
      # 1h down move, 4h & 1d high
      & ((df["RSI_3_1h"] > 50.0) | (df["AROONU_14_4h"] < 100.0) | (df["AROONU_14_1d"] < 100.0))
      # 1h down move, 4h high, 1d downtrend
      & ((df["RSI_3_1h"] > 50.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 60.0) | (df["ROC_9_1d"] > -60.0))
      # 1h down move, 4h & 1d overbought
      & ((df["RSI_3_1h"] > 50.0) | (df["ROC_9_4h"] < 20.0) | (df["ROC_9_1d"] < 80.0))
      # 1h down move, 15m high, 1h high
      & ((df["RSI_3_1h"] > 55.0) | (df["AROONU_14_15m"] < 60.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 80.0))
      # 1h down move, 1h high & overbought
      & ((df["RSI_3_1h"] > 55.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 60.0) | (df["ROC_9_1d"] < 10.0))
      # 1h down move, 4h & 1d overbought
      & ((df["RSI_3_1h"] > 60.0) | (df["ROC_9_4h"] < 10.0) | (df["ROC_9_1d"] < 40.0))
      # 1h down move, 4h high, 1d overbought
      & ((df["RSI_3_1h"] > 60.0) | (df["AROONU_14_4h"] < 80.0) | (df["ROC_9_1d"] < 40.0))
      # 4h & 1d down move, 4h downtrend
      & ((df["RSI_3_4h"] > 3.0) | (df["RSI_3_1d"] > 10.0) | (df["ROC_9_4h"] > -20.0))
      # 4h & 1d down move, 1h still not low enough
      & ((df["RSI_3_4h"] > 5.0) | (df["RSI_3_1d"] > 10.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 30.0))
      # 4h down move, 1d high, 4h downtrend
      & ((df["RSI_3_4h"] > 5.0) | (df["AROONU_14_1d"] < 80.0) | (df["ROC_9_4h"] > -10.0))
      # 4h & 1d down move, 15m high
      & ((df["RSI_3_4h"] > 10.0) | (df["RSI_3_1d"] > 15.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 80.0))
      # 4h & 1d down move, 1d downtrend
      & ((df["RSI_3_4h"] > 10.0) | (df["RSI_3_1d"] > 15.0) | (df["ROC_9_1d"] > -15.0))
      # 4h & 1d down move, 1d still high
      & ((df["RSI_3_4h"] > 10.0) | (df["RSI_3_1d"] > 25.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 50.0))
      # 4h down move, 15m downtrend, 1d high
      & ((df["RSI_3_4h"] > 10.0) | (df["CMF_20_15m"] > -0.30) | (df["AROONU_14_1d"] < 80.0))
      # 4h down move, 15m still high, 1d downtrend
      & ((df["RSI_3_4h"] > 10.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 50.0) | (df["ROC_9_1d"] > -25.0))
      # 4h down move, 15m high
      & ((df["RSI_3_4h"] > 10.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 80.0))
      # 4h down move, 1h high, 1d downtrend
      & ((df["RSI_3_4h"] > 10.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 70.0) | (df["ROC_9_1d"] > -20.0))
      # 4h down move, 4h still high, 1d downtrend
      & ((df["RSI_3_4h"] > 10.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 40.0) | (df["ROC_9_1d"] > -20.0))
      # 4h down move, 4h downtrend, 1d overbought
      & ((df["RSI_3_4h"] > 10.0) | (df["ROC_9_4h"] > -30.0) | (df["ROC_9_1d"] < 40.0))
      # 4h & 1d down move, 4h downtrend
      & ((df["RSI_3_4h"] > 15.0) | (df["RSI_3_1d"] > 20.0) | (df["ROC_9_4h"] > -40.0))
      # 4h down move, 1h high, 1d downtrend
      & ((df["RSI_3_4h"] > 15.0) | (df["AROONU_14_1h"] < 90.0) | (df["ROC_9_1d"] > -10.0))
      # 4h down move, 4h still high, 1d downtrend
      & ((df["RSI_3_4h"] > 15.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 50.0) | (df["ROC_9_1d"] > -20.0))
      # 4h down move, 1h & 4h downtrend
      & ((df["RSI_3_4h"] > 15.0) | (df["ROC_9_1h"] > -30.0) | (df["ROC_9_4h"] > -30.0))
      # 4h & 1ddown move, 1d high
      & ((df["RSI_3_4h"] > 20.0) | (df["RSI_3_1d"] > 20.0) | (df["AROONU_14_1d"] < 80.0))
      # 4h down move, 1d high, 1d downtrend
      & ((df["RSI_3_4h"] > 20.0) | (df["AROONU_14_1d"] < 80.0) | (df["ROC_9_1d"] > -30.0))
      # 4h down move, 1d high & overbought
      & ((df["RSI_3_4h"] > 20.0) | (df["AROONU_14_1d"] < 80.0) | (df["ROC_9_1d"] < 70.0))
      # 4h down move, 4h still high. 4h downtrend
      & ((df["RSI_3_4h"] > 25.0) | (df["AROONU_14_4h"] < 50.0) | (df["CMF_20_4h"] > -0.40))
      # 4h down move, 4h high, 1d downtrend
      & ((df["RSI_3_4h"] > 25.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 60.0) | (df["ROC_9_1d"] > -70.0))
      # 4h down move, 1h high, 4h downtrend
      & ((df["RSI_3_4h"] > 30.0) | (df["AROONU_14_1h"] < 70.0) | (df["ROC_9_4h"] > -10.0))
      # 4h down move, 1h high, 1d downtrend
      & ((df["RSI_3_4h"] > 30.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 60.0) | (df["ROC_9_1d"] > -40.0))
      # 4h down move, 4h & 1d high
      & ((df["RSI_3_4h"] > 35.0) | (df["AROONU_14_4h"] < 70.0) | (df["AROONU_14_1d"] < 100.0))
      # 4h down move, 4h high & overbought
      & ((df["RSI_3_4h"] > 50.0) | (df["AROONU_14_4h"] < 80.0) | (df["ROC_9_4h"] < 10.0))
      # 4h down move, 4h high, 1d overbought
      & ((df["RSI_3_4h"] > 50.0) | (df["AROONU_14_4h"] < 80.0) | (df["ROC_9_1d"] < 40.0))
      # 4h down move, 4h & 1d overbought
      & ((df["RSI_3_4h"] > 50.0) | (df["ROC_9_4h"] < 10.0) | (df["ROC_9_1d"] < 40.0))
      # 1d down move, 1d high, 1d downtrend
      & ((df["RSI_3_1d"] > 10.0) | (df["AROONU_14_1d"] < 70.0) | (df["ROC_9_1d"] > -10.0))
      # 1d down move, 1h high, 4h downtrend
      & ((df["RSI_3_1d"] > 30.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 90.0) | (df["ROC_9_4h"] > -30.0))
      # 15m & 1h & 4h downtrend
      & ((df["CMF_20_15m"] > -0.30) | (df["CMF_20_1h"] > -0.30) | (df["CMF_20_4h"] > -0.30))
      # 1d downtrend, 1d high & overbought
      & ((df["CMF_20_1d"] > -0.40) | (df["AROONU_14_1d"] < 85.0) | (df["ROC_9_1d"] < 20.0))
      # 15m not low enough, 1h & 4h downtrend
      & ((df["AROONU_14_15m"] < 20.0) | (df["ROC_9_1h"] > -30.0) | (df["ROC_9_4h"] > -50.0))
      # 15m high, 1h high & overbought
      & ((df["AROONU_14_15m"] < 70.0) | (df["AROONU_14_1h"] < 85.0) | (df["ROC_9_1h"] < 10.0))
      # 4h high, 4h & 1d overbought
      & ((df["AROONU_14_4h"] < 70.0) | (df["ROC_9_4h"] < 60.0) | (df["ROC_9_1d"] < 80.0))
      # 1h & 4h high, 4h overbought
      & ((df["AROONU_14_1h"] < 80.0) | (df["AROONU_14_4h"] < 100.0) | (df["ROC_9_4h"] < 10.0))
      # 1h & 1d high, 1d overbought
      & ((df["AROONU_14_1h"] < 80.0) | (df["AROONU_14_1d"] < 80.0) | (df["ROC_9_1d"] < 200.0))
      # 1h high, 1h overbought
      & ((df["AROONU_14_1h"] < 80.0) | (df["ROC_9_1h"] < 10.0))
      # 4h still high, 5m downtrend
      & ((df["AROONU_14_4h"] < 40.0) | (df["ROC_9"] > -40.0))
      # 4h & 1d high, 4h overbought
      & ((df["AROONU_14_4h"] < 80.0) | (df["AROONU_14_1d"] < 100.0) | (df["ROC_9_4h"] < 80.0))
      # 4h & 1d high, 1d overbought
      & ((df["AROONU_14_4h"] < 80.0) | (df["AROONU_14_1d"] < 100.0) | (df["ROC_9_1d"] < 80.0))
      # 4h high, 1h & 4h overbought
      & ((df["AROONU_14_4h"] < 85.0) | (df["ROC_9_1h"] < 80.0) | (df["ROC_9_4h"] < 80.0))
      # 4h high, 4h & 1d overbought
      & ((df["AROONU_14_4h"] < 85.0) | (df["ROC_9_4h"] < 10.0) | (df["ROC_9_1d"] < 40.0))
      # 4h & 1d high, 4h overbought
      & ((df["AROONU_14_4h"] < 100.0) | (df["AROONU_14_1d"] < 100.0) | (df["ROC_9_4h"] < 40.0))
      # 4h high, 1h & 1d overbought
      & ((df["AROONU_14_4h"] < 100.0) | (df["ROC_9_1h"] < 40.0) | (df["ROC_9_1d"] < 100.0))
      # 4h high, 4h & 1d overbought
      & ((df["AROONU_14_4h"] < 100.0) | (df["ROC_9_4h"] < 20.0) | (df["ROC_9_1d"] < 80.0))
      # 1d high, 1h & 4h down move
      & ((df["AROONU_14_1d"] < 100.0) | (df["ROC_9_1h"] < 25.0) | (df["ROC_9_4h"] < 60.0))
      # 1d high, 1h downtrend, 1d overbought
      & ((df["AROONU_14_1d"] < 100.0) | (df["ROC_9_1h"] > -30.0) | (df["ROC_9_1d"] < 100.0))
      # 1d high, 4h & 1d overbought
      & ((df["AROONU_14_1d"] < 100.0) | (df["ROC_9_4h"] < 20.0) | (df["ROC_9_1d"] < 80.0))
      # 15m high, 4h & 1d downtrend
      & ((df["STOCHRSIk_14_14_3_3_15m"] < 70.0) | (df["ROC_9_4h"] > -30.0) | (df["ROC_9_1d"] > -30.0))
      # 1h high, 4h & 1d overbought
      & ((df["STOCHRSIk_14_14_3_3_1h"] < 90.0) | (df["ROC_9_4h"] < 20.0) | (df["ROC_9_1d"] < 100.0))
      # 4h high, 1h overbought, 1d downtrend
      & ((df["STOCHRSIk_14_14_3_3_4h"] < 80.0) | (df["ROC_9_1h"] < 40.0) | (df["ROC_9_1d"] > -70.0))
      # 4h high, 4h & 1d overbought
      & ((df["STOCHRSIk_14_14_3_3_4h"] < 80.0) | (df["ROC_9_4h"] < 80.0) | (df["ROC_9_1d"] < 100.0))
      # 4h high, 1h & 4h overbought
      & ((df["STOCHRSIk_14_14_3_3_4h"] < 90.0) | (df["ROC_9_1h"] < 10.0) | (df["ROC_9_4h"] < 80.0))
      # 4h high, 1h & 4h overbought
      & ((df["STOCHRSIk_14_14_3_3_4h"] < 90.0) | (df["ROC_9_1h"] < 20.0) | (df["ROC_9_4h"] < 50.0))
      # 1d high, 4h & 1d overbought
      & ((df["STOCHRSIk_14_14_3_3_1d"] < 90.0) | (df["ROC_9_4h"] < 40.0) | (df["ROC_9_1d"] < 100.0))
      # 1d P&D, dh downtrend
      & ((df["change_pct_1d"] > -50.0) | (df["change_pct_1d"].shift(288) < 50.0) | (df["RSI_3_4h"] > 15.0))
      # big drop in the last 20 days, 1d high, 1d downtrend
      & (
        (df["close"] > (df["high_max_20_1d"] * 0.20))
        | (df["STOCHRSIk_14_14_3_3_1d"] < 70.0)
        | (df["ROC_9_1d"] > -15.0)
      )
      # drop in last 20 days, 1h high, 1d downtrend
      & ((df["close"] > (df["high_max_20_1d"] * 0.20)) | (df["AROONU_14_1h"] < 70.0) | (df["ROC_9_1d"] > -70.0))
      # drop in last 20 days. 4h high
      & ((df["close"] > (df["high_max_20_1d"] * 0.10)) | (df["STOCHRSIk_14_14_3_3_4h"] < 90.0))
    )

    # Logic
    long_entry_logic.append(
      (df["RSI_3"] < 50.0)
      & (df["AROONU_14"] < 25.0)
      & (df["STOCHRSIk_14_14_3_3"] < 30.0)
      & (df["EMA_26"] > df["EMA_12"])
      & ((df["EMA_26"] - df["EMA_12"]) > (df["open"] * 0.020))
      & ((df["EMA_26"].shift() - df["EMA_12"].shift()) > (df["open"] / 100.0))
    )


def append_long_6(df, long_entry_logic, allowed_empty_candles_288) -> None:
    """Append NFI long condition #6, the normal-mode long entry."""
    # Protections
    long_entry_logic.append(df["num_empty_288"] <= allowed_empty_candles_288)
    long_entry_logic.append(df["protections_long_global"] == True)

    long_entry_logic.append(
      # 5m & 15m down move, 15m still high
      ((df["RSI_3"] > 3.0) | (df["RSI_3_15m"] > 10.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 40.0))
      # 5m & 15m down move, 15m still high
      & ((df["RSI_3"] > 3.0) | (df["RSI_3_15m"] > 15.0) | (df["AROONU_14_15m"] < 40.0))
      # 5m & 15m down move, 1d downtrend
      & ((df["RSI_3"] > 3.0) | (df["RSI_3_15m"] > 15.0) | (df["ROC_9_1d"] > -20.0))
      # 5m & 15m down move, 1d downtrend
      & ((df["RSI_3"] > 3.0) | (df["RSI_3_15m"] > 25.0) | (df["ROC_9_1d"] > -30.0))
      # 5m & 1h down move, 1h still not low enough
      & ((df["RSI_3"] > 3.0) | (df["RSI_3_1h"] > 20.0) | (df["AROONU_14_1h"] < 30.0))
      # 5m & 1h down move, 1h still high
      & ((df["RSI_3"] > 3.0) | (df["RSI_3_1h"] > 30.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 50.0))
      # 5m & 4h down move, 4h still high
      & ((df["RSI_3"] > 3.0) | (df["RSI_3_4h"] > 15.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 50.0))
      # 5m & 4h & 1d down move
      & ((df["RSI_3"] > 3.0) | (df["RSI_3_4h"] > 20.0) | (df["RSI_3_1d"] > 35.0))
      # 5m & 4h down move, 4h high
      & ((df["RSI_3"] > 3.0) | (df["RSI_3_4h"] > 30.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 70.0))
      # 5m & 4h down move, 4h still high
      & ((df["RSI_3"] > 3.0) | (df["RSI_3_4h"] > 55.0) | (df["AROONU_14_4h"] < 50.0))
      # 5m & 1d down move, 15m still high
      & ((df["RSI_3"] > 3.0) | (df["RSI_3_1d"] > 20.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 40.0))
      # 5m down move, 4h & 1d overbought
      & ((df["RSI_3"] > 3.0) | (df["ROC_9_4h"] < 20.0) | (df["ROC_9_1d"] < 40.0))
      # 5m & 1h down move, 4h high
      & ((df["RSI_3"] > 5.0) | (df["RSI_3_1h"] > 40.0) | (df["AROONU_14_4h"] < 60.0))
      # 5m & 1h down move, 1h high
      & ((df["RSI_3"] > 5.0) | (df["RSI_3_1h"] > 60.0) | (df["AROONU_14_1h"] < 80.0))
      # 5m & 4h down move, 1d downtrend
      & ((df["RSI_3"] > 5.0) | (df["RSI_3_4h"] > 5.0) | (df["ROC_9_1d"] > -20.0))
      # 5m & 4h down move, 4h still high
      & ((df["RSI_3"] > 5.0) | (df["RSI_3_4h"] > 15.0) | (df["AROONU_14_4h"] < 40.0))
      # 5m & 4h down move, 15m still high
      & ((df["RSI_3"] > 5.0) | (df["RSI_3_4h"] > 25.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 50.0))
      # 5m & 4h down move, 1d overbought
      & ((df["RSI_3"] > 5.0) | (df["RSI_3_4h"] > 30.0) | (df["ROC_9_1d"] < 60.0))
      # 5m & 4h down move, 4h high
      & ((df["RSI_3"] > 5.0) | (df["RSI_3_4h"] > 60.0) | (df["AROONU_14_4h"] < 80.0))
      # 5m down move, 15m still not low enough, 4h high
      & ((df["RSI_3"] > 5.0) | (df["AROONU_14_15m"] < 20.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 70.0))
      # 5m down move, 1h & 1d high
      & ((df["RSI_3"] > 5.0) | (df["AROONU_14_1h"] < 70.0) | (df["AROONU_14_1d"] < 100.0))
      # 5m down move, 4h high & overbought
      & ((df["RSI_3"] > 5.0) | (df["AROONU_14_4h"] < 100.0) | (df["ROC_9_4h"] < 25.0))
      # 5m down move, 1h high
      & ((df["RSI_3"] > 5.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 80.0))
      # 5m & 1d down move, 1d still high
      & ((df["RSI_3"] > 10.0) | (df["RSI_3_1d"] > 15.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 40.0))
      # 15m & 1h down move, 1h still high
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_1h"] > 20.0) | (df["AROONU_14_1h"] < 50.0))
      # 15m & 1h down move, 4h still not low enough
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_1h"] > 20.0) | (df["AROONU_14_4h"] < 20.0))
      # 15m & 1h down move, 1h still not low enough
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_1h"] > 25.0) | (df["AROONU_14_1h"] < 20.0))
      # 15m & 1h down move, 4h still high
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_1h"] > 25.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 40.0))
      # 15m & 1h down move, 4h high
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_1h"] > 40.0) | (df["AROONU_14_4h"] < 70.0))
      # 15m & 4h down move, 1h still not low enough
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_4h"] > 10.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 30.0))
      # 15m & 4h down move, 1d downtrend
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_4h"] > 15.0) | (df["ROC_9_1d"] > -10.0))
      # 15m & 4h down move, 4h still not low enough
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_4h"] > 20.0) | (df["AROONU_14_4h"] < 20.0))
      # 15m & 4h down move, 1h still high
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_4h"] > 30.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 40.0))
      # 15m & 4h down move, 1h high
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_4h"] > 45.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 60.0))
      # 15m & 1d down move, 15m still not low enough
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_1d"] > 10.0) | (df["AROONU_14_15m"] < 30.0))
      # 15m & 1d down move, 4h high
      & ((df["RSI_3_15m"] > 3.0) | (df["RSI_3_1d"] > 55.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 70.0))
      # 1h & 1d downtrend, 1d high
      & ((df["RSI_3_15m"] > 3.0) | (df["AROONU_14_1d"] < 70.0) | (df["ROC_9_1d"] < 10.0))
      # 15m & 1h down move, 1h high
      & ((df["RSI_3_15m"] > 5.0) | (df["RSI_3_1h"] > 25.0) | (df["AROONU_14_1h"] < 60.0))
      # 15m & 1h down move, 1h still high
      & ((df["RSI_3_15m"] > 5.0) | (df["RSI_3_1h"] > 25.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 40.0))
      # 15m & 1h down move, 4h still high
      & ((df["RSI_3_15m"] > 5.0) | (df["RSI_3_1h"] > 25.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 30.0))
      # 15m & 1h down move, 4h high
      & ((df["RSI_3_15m"] > 5.0) | (df["RSI_3_1h"] > 30.0) | (df["AROONU_14_4h"] < 90.0))
      # 15m & 1h & 4h down move, 15m downtrend
      & (
        (df["RSI_3_15m"] > 5.0) | (df["RSI_3_1h"] > 40.0) | (df["RSI_3_4h"] > 50.0) | (df["CMF_20_15m"] > -0.30)
      )
      # 15m & 1h down move, 1h still high
      & ((df["RSI_3_15m"] > 5.0) | (df["RSI_3_1h"] > 40.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 50.0))
      # 15m & 1h down move, 4h high
      & ((df["RSI_3_15m"] > 5.0) | (df["RSI_3_1h"] > 55.0) | (df["AROONU_14_4h"] < 100.0))
      # 15m & 4h down move, 15m still not low enough
      & ((df["RSI_3_15m"] > 5.0) | (df["RSI_3_4h"] > 20.0) | (df["AROONU_14_15m"] < 30.0))
      # 15m & 4h down move, 4h high
      & ((df["RSI_3_15m"] > 5.0) | (df["RSI_3_4h"] > 35.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 60.0))
      # 15m down move, 15m still high, 1h still high
      & ((df["RSI_3_15m"] > 5.0) | (df["AROONU_14_15m"] < 30.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 50.0))
      # 15m down move, 1h still high, 1d high
      & ((df["RSI_3_15m"] > 5.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 40.0) | (df["AROONU_14_1d"] < 70.0))
      # 15m down move, 1h & 4h high
      & ((df["RSI_3_15m"] > 5.0) | (df["AROONU_14_1h"] < 70.0) | (df["AROONU_14_4h"] < 90.0))
      # 15m down move, 15m & 1h still not low enough
      & (
        (df["RSI_3_15m"] > 5.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 30.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 30.0)
      )
      # 15m & 1h down move, 1h still high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1h"] > 20.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 50.0))
      # 15m & 1h down move, 4h still high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1h"] > 20.0) | (df["AROONU_14_4h"] < 40.0))
      # 15m & 1h down move, 4h high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1h"] > 20.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 60.0))
      # 15m & 1h down move, 4h still high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1h"] > 25.0) | (df["AROONU_14_4h"] < 50.0))
      # 15m & 1h down move, 4h high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1h"] > 30.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 70.0))
      # 15m & 1h down move, 4h high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1h"] > 30.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 60.0))
      # 15m & 1h down move, 1d overbought
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1h"] > 30.0) | (df["ROC_9_1d"] < 30.0))
      # 15m & 1h down move, 1d downtrend
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1h"] > 30.0) | (df["ROC_9_1d"] > -40.0))
      # 15m & 1h down move, 1h still high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1h"] > 35.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 40.0))
      # 15m & 1h down move, 1h still high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1h"] > 45.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 40.0))
      # 15m & 1h down move, 1d overbought
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1h"] > 45.0) | (df["ROC_9_1d"] < 150.0))
      # 15m & 1h down move, 4h high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1h"] > 50.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 80.0))
      # 15m & 1h down move, 1h high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1h"] > 55.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 60.0))
      # 15m & 1h down move, 1h high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1h"] > 65.0) | (df["AROONU_14_1h"] < 80.0))
      # 15m & 4h down move, 1d high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_4h"] > 10.0) | (df["AROONU_14_1d"] < 80.0))
      # 15m & 4h down move, 4h still not low enough
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_4h"] > 10.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 30.0))
      # 15m & 4h down move, 1d high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_4h"] > 10.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 70.0))
      # 15m & 4h down move, 1d high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_4h"] > 15.0) | (df["RSI_14_1d"] < 60.0))
      # 15m & 4h down move, 4h still high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_4h"] > 20.0) | (df["AROONU_14_4h"] < 40.0))
      # 15m & 4h down move, 1d high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_4h"] > 20.0) | (df["AROONU_14_1d"] < 90.0))
      # 15m & 4h down move, 1h still high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_4h"] > 20.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 50.0))
      # 15m & 4h down move, 4h still high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_4h"] > 20.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 40.0))
      # 15m & 4h down move, 1d high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_4h"] > 20.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 90.0))
      # 15m & 4h down move, 1d overbought
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_4h"] > 20.0) | (df["ROC_9_1d"] < 20.0))
      # 15m & 4h down move, 4h downtrend
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_4h"] > 25.0) | (df["CMF_20_4h"] > -0.30))
      # 15m & 4h down move, 1d overbought
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_4h"] > 25.0) | (df["ROC_9_1d"] < 30.0))
      # 15m & 4h down move, 4h still high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_4h"] > 30.0) | (df["AROONU_14_4h"] < 50.0))
      # 15m & 4h down move, 4h high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_4h"] > 45.0) | (df["AROONU_14_4h"] < 70.0))
      # 15m & 4h down move, 4h high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_4h"] > 50.0) | (df["AROONU_14_4h"] < 75.0))
      # 15m & 4h down move, 4h high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_4h"] > 60.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 80.0))
      # 15m & 1d down move, 1h still high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1d"] > 10.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 40.0))
      # 15m & 1d down move, 1d high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1d"] > 20.0) | (df["AROONU_14_1d"] < 75.0))
      # 15m & 1d down move, 1d overbought
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1d"] > 50.0) | (df["ROC_9_1d"] < 20.0))
      # 15m down move, 15m downtrend, 4h still high
      & ((df["RSI_3_15m"] > 10.0) | (df["CMF_20_15m"] > -0.40) | (df["STOCHRSIk_14_14_3_3_4h"] < 50.0))
      # 15m down move, 1h downtrend, 4h still high
      & ((df["RSI_3_15m"] > 10.0) | (df["CMF_20_1h"] > -0.30) | (df["STOCHRSIk_14_14_3_3_4h"] < 40.0))
      # 15m down move, 15m still not low enough, 4h high
      & ((df["RSI_3_15m"] > 10.0) | (df["AROONU_14_15m"] < 30.0) | (df["AROONU_14_4h"] < 60.0))
      # 15m down move, 15m still high, 1h still high
      & ((df["RSI_3_15m"] > 10.0) | (df["AROONU_14_15m"] < 40.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 50.0))
      # 15m down move, 4h high & overbought
      & ((df["RSI_3_15m"] > 10.0) | (df["AROONU_14_4h"] < 90.0) | (df["ROC_9_4h"] < 20.0))
      # 15m down move, 1h still not low enough, 1d overbought
      & ((df["RSI_3_15m"] > 10.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 30.0) | (df["ROC_9_1d"] < 100.0))
      # 15m down move, 1h still high, 4h downtrend
      & ((df["RSI_3_15m"] > 10.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 50.0) | (df["ROC_9_4h"] > -20.0))
      # 15m down move, 4h high & overbought
      & ((df["RSI_3_15m"] > 10.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 70.0) | (df["ROC_9_4h"] < 10.0))
      # 15m down move, 4h high, 1d overbought
      & ((df["RSI_3_15m"] > 10.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 70.0) | (df["ROC_9_1d"] < 10.0))
      # 15m & 1h & 4h down move
      & ((df["RSI_3_15m"] > 15.0) | (df["RSI_3_1h"] > 15.0) | (df["RSI_3_1h"] > 15.0))
      # 15m & 1h down move, 1h still high
      & ((df["RSI_3_15m"] > 15.0) | (df["RSI_3_1h"] > 15.0) | (df["AROONU_14_1h"] < 40.0))
      # 15m & 1h down move, 1h downtrend
      & ((df["RSI_3_15m"] > 15.0) | (df["RSI_3_1h"] > 20.0) | (df["CMF_20_1h"] > -0.30))
      # 15m & 1h down move, 1h still high
      & ((df["RSI_3_15m"] > 15.0) | (df["RSI_3_1h"] > 25.0) | (df["AROONU_14_1h"] < 50.0))
      # 15m & 1h down move, 4h high
      & ((df["RSI_3_15m"] > 15.0) | (df["RSI_3_1h"] > 25.0) | (df["AROONU_14_4h"] < 70.0))
      # 15m & 1h down move, 1h still high
      & ((df["RSI_3_15m"] > 15.0) | (df["RSI_3_1h"] > 25.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 40.0))
      # 15m & 1h down move, 1d overbought
      & ((df["RSI_3_15m"] > 15.0) | (df["RSI_3_1h"] > 25.0) | (df["ROC_9_1d"] < 100.0))
      # 15m & 1h down move, 1d high
      & ((df["RSI_3_15m"] > 15.0) | (df["RSI_3_1h"] > 30.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 80.0))
      # 15m & 1h down move, 4h high
      & ((df["RSI_3_15m"] > 15.0) | (df["RSI_3_1h"] > 50.0) | (df["AROONU_14_4h"] < 100.0))
      # 15m & 1h down move, 1h high
      & ((df["RSI_3_15m"] > 15.0) | (df["RSI_3_1h"] > 55.0) | (df["AROONU_14_1h"] < 90.0))
      # 15m & 4h down move, 1d high
      & ((df["RSI_3_15m"] > 15.0) | (df["RSI_3_4h"] > 20.0) | (df["AROONU_14_1d"] < 90.0))
      # 15m & 4h down move, 15m still high
      & ((df["RSI_3_15m"] > 15.0) | (df["RSI_3_4h"] > 20.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 50.0))
      # 15m & 4h down move, 1h high
      & ((df["RSI_3_15m"] > 15.0) | (df["RSI_3_4h"] > 30.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 60.0))
      # 15m & 4h down move, 4h high
      & ((df["RSI_3_15m"] > 15.0) | (df["RSI_3_4h"] > 35.0) | (df["AROONU_14_4h"] < 60.0))
      # 15m & 4h down move, 4h high
      & ((df["RSI_3_15m"] > 15.0) | (df["RSI_3_4h"] > 35.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 70.0))
      # 15m & 4h down move, 4h high
      & ((df["RSI_3_15m"] > 15.0) | (df["RSI_3_4h"] > 40.0) | (df["AROONU_14_4h"] < 80.0))
      # 15m & 4h down move, 1d overbought
      & ((df["RSI_3_15m"] > 15.0) | (df["RSI_3_4h"] > 40.0) | (df["ROC_9_1d"] < 40.0))
      # 15m & 4h down move, 1d overbought
      & ((df["RSI_3_15m"] > 15.0) | (df["RSI_3_4h"] > 45.0) | (df["ROC_9_1d"] < 80.0))
      # 15m & 4h down move, 4h high
      & ((df["RSI_3_15m"] > 15.0) | (df["RSI_3_4h"] > 55.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 70.0))
      # 15m & 1d down move, 1h still high
      & ((df["RSI_3_15m"] > 15.0) | (df["RSI_3_1d"] > 15.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 30.0))
      # 15m & 1d down move, 1h still high
      & ((df["RSI_3_15m"] > 15.0) | (df["RSI_3_1d"] > 20.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 50.0))
      # 15m & 1d down move, 1d overbought
      & ((df["RSI_3_15m"] > 15.0) | (df["RSI_3_1d"] > 30.0) | (df["ROC_9_1d"] < 10.0))
      # 15m down move, 15m still not low enough, 1h high
      & ((df["RSI_3_15m"] > 15.0) | (df["AROONU_14_15m"] < 25.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 80.0))
      # 15m down move, 15m still high, 4h high
      & ((df["RSI_3_15m"] > 15.0) | (df["AROONU_14_15m"] < 40.0) | (df["AROONU_14_4h"] < 70.0))
      # 15m down move, 1h still high, 1d overbought
      & ((df["RSI_3_15m"] > 15.0) | (df["AROONU_14_1h"] < 50.0) | (df["ROC_9_1d"] < 80.0))
      # 15m down move, 1h & 4h high
      & ((df["RSI_3_15m"] > 15.0) | (df["AROONU_14_1h"] < 60.0) | (df["AROONU_14_4h"] < 90.0))
      # 15m down move, 1h & 4h high
      & ((df["RSI_3_15m"] > 15.0) | (df["AROONU_14_1h"] < 80.0) | (df["AROONU_14_4h"] < 85.0))
      # 15m down move, 1h & 1d high
      & ((df["RSI_3_15m"] > 15.0) | (df["AROONU_14_1h"] < 70.0) | (df["AROONU_14_1d"] < 70.0))
      # 15m down move, 1h & 4h high
      & ((df["RSI_3_15m"] > 15.0) | (df["AROONU_14_1h"] < 85.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 90.0))
      # 15m down move, 4h high, 4h downtrend
      & ((df["RSI_3_15m"] > 15.0) | (df["AROONU_14_4h"] < 60.0) | (df["ROC_9_4h"] > -20.0))
      # 15m down move, 4h & 1d high
      & ((df["RSI_3_15m"] > 15.0) | (df["AROONU_14_4h"] < 70.0) | (df["AROONU_14_1d"] < 100.0))
      # 15m down move, 4h high & overbought
      & ((df["RSI_3_15m"] > 15.0) | (df["AROONU_14_4h"] < 70.0) | (df["ROC_9_4h"] < 30.0))
      # 15m down move, 4h high, 1h overbought
      & ((df["RSI_3_15m"] > 15.0) | (df["AROONU_14_4h"] < 90.0) | (df["ROC_9_1h"] < 25.0))
      # 15m down move, 4h high, 1h overbought
      & ((df["RSI_3_15m"] > 15.0) | (df["AROONU_14_4h"] < 100.0) | (df["ROC_9_1h"] < 10.0))
      # 15m down move, 1h still high, 4h overbought
      & ((df["RSI_3_15m"] > 15.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 50.0) | (df["ROC_9_4h"] < 10.0))
      # 15m down move, 1h high, 4h downtrend
      & ((df["RSI_3_15m"] > 15.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 80.0) | (df["ROC_9_4h"] > -20.0))
      # 15m down move, 4h high & overbought
      & ((df["RSI_3_15m"] > 15.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 90.0) | (df["ROC_9_4h"] < 20.0))
      # 15m & 1h down move, 1h still high
      & ((df["RSI_3_15m"] > 20.0) | (df["RSI_3_1h"] > 20.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 20.0))
      # 15m & 1h down move, 1d downtrend
      & ((df["RSI_3_15m"] > 20.0) | (df["RSI_3_1h"] > 30.0) | (df["ROC_9_1d"] > -30.0))
      # 15m & 1h down move, 1h overbought
      & ((df["RSI_3_15m"] > 20.0) | (df["RSI_3_1h"] > 50.0) | (df["ROC_9_1h"] < 10.0))
      # 15m & 1h down move, 4h high
      & ((df["RSI_3_15m"] > 20.0) | (df["RSI_3_1h"] > 25.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 80.0))
      # 15m & 1h down move, 1d high
      & ((df["RSI_3_15m"] > 20.0) | (df["RSI_3_1h"] > 35.0) | (df["AROONU_14_1d"] < 100.0))
      # 15m & 1h down move, 1h high
      & ((df["RSI_3_15m"] > 20.0) | (df["RSI_3_1h"] > 45.0) | (df["AROONU_14_1h"] < 70.0))
      # 15m & 1h down move, 1h high
      & ((df["RSI_3_15m"] > 20.0) | (df["RSI_3_1h"] > 60.0) | (df["AROONU_14_1h"] < 90.0))
      # 15m & 1h down move, 4h high
      & ((df["RSI_3_15m"] > 20.0) | (df["RSI_3_1h"] > 60.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 90.0))
      # 15m & 4h & 1d down move
      & ((df["RSI_3_15m"] > 20.0) | (df["RSI_3_4h"] > 20.0) | (df["RSI_3_1d"] > 20.0))
      # 15m & 4h down move, 1d high
      & ((df["RSI_3_15m"] > 20.0) | (df["RSI_3_4h"] > 20.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 90.0))
      # 15m & 4h down move, 1d high
      & ((df["RSI_3_15m"] > 20.0) | (df["RSI_3_4h"] > 45.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 90.0))
      # 15m & 1d down move, 1h high
      & ((df["RSI_3_15m"] > 20.0) | (df["RSI_3_1d"] > 20.0) | (df["AROONU_14_1h"] < 70.0))
      # 15m & 1d down move, 15m still high
      & ((df["RSI_3_15m"] > 20.0) | (df["RSI_3_1d"] > 30.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 50.0))
      # 15m down move, 15m still not low enough, 1h high
      & ((df["RSI_3_15m"] > 20.0) | (df["AROONU_14_15m"] < 25.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 90.0))
      # 15m down move, 15m still high, 1h high
      & ((df["RSI_3_15m"] > 20.0) | (df["AROONU_14_15m"] < 40.0) | (df["AROONU_14_1h"] < 70.0))
      # 15m down move, 15m still high, 4h high
      & ((df["RSI_3_15m"] > 20.0) | (df["AROONU_14_15m"] < 40.0) | (df["AROONU_14_4h"] < 70.0))
      # 15m down move, 1h & 4h high
      & ((df["RSI_3_15m"] > 20.0) | (df["AROONU_14_1h"] < 80.0) | (df["AROONU_14_4h"] < 80.0))
      # 15m down move, 1h high, 1d overbought
      & ((df["RSI_3_15m"] > 20.0) | (df["AROONU_14_1h"] < 80.0) | (df["ROC_9_1d"] < 10.0))
      # 15m down move, 4h high & overbought
      & ((df["RSI_3_15m"] > 20.0) | (df["AROONU_14_4h"] < 70.0) | (df["ROC_9_4h"] < 30.0))
      # 15m down move, 4h high, 1h overbought
      & ((df["RSI_3_15m"] > 20.0) | (df["AROONU_14_4h"] < 100.0) | (df["ROC_9_1h"] < 30.0))
      # 15m down move, 1d high, 4h downtrend
      & ((df["RSI_3_15m"] > 20.0) | (df["AROONU_14_1d"] < 90.0) | (df["ROC_9_4h"] > -20.0))
      # 15m down move, 1d high, 4h overbought
      & ((df["RSI_3_15m"] > 20.0) | (df["AROONU_14_1d"] < 100.0) | (df["ROC_9_4h"] < 20.0))
      # 15m down move, 1d high, 1d overbought
      & ((df["RSI_3_15m"] > 20.0) | (df["AROONU_14_1d"] < 100.0) | (df["ROC_9_1d"] < 20.0))
      # 15m down move, 15m high, 4h downtrend
      & ((df["RSI_3_15m"] > 20.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 60.0) | (df["ROC_9_4h"] > -50.0))
      # 15 down move, 1h high, 1d overbought
      & ((df["RSI_3_15m"] > 20.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 70.0) | (df["ROC_9_1d"] < 10.0))
      # 15m down move, 4h high, 15m downtrend
      & ((df["RSI_3_15m"] > 20.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 70.0) | (df["CMF_20_15m"] > -0.40))
      # 15m & 1h down move, 15m high
      & ((df["RSI_3_15m"] > 25.0) | (df["RSI_3_1h"] > 25.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 70.0))
      # 15m & 1h down move, 1h still high
      & ((df["RSI_3_15m"] > 25.0) | (df["RSI_3_1h"] > 35.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 50.0))
      # 15m & 1h down move, 1d high
      & ((df["RSI_3_15m"] > 25.0) | (df["RSI_3_1h"] > 40.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 90.0))
      # 15m & 1h down move, 1h high
      & ((df["RSI_3_15m"] > 25.0) | (df["RSI_3_1h"] > 50.0) | (df["AROONU_14_1h"] < 85.0))
      # 15m & 1h down move, 4h high
      & ((df["RSI_3_15m"] > 25.0) | (df["RSI_3_1h"] > 60.0) | (df["AROONU_14_4h"] < 100.0))
      # 15m & 1h down move, 4h high
      & ((df["RSI_3_15m"] > 25.0) | (df["RSI_3_1h"] > 60.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 90.0))
      # 15m & 4h down move, 4h overbought
      & ((df["RSI_3_15m"] > 25.0) | (df["RSI_3_4h"] > 55.0) | (df["ROC_9_4h"] < 30.0))
      # 15m & 1d down move, 1h high
      & ((df["RSI_3_15m"] > 25.0) | (df["RSI_3_1d"] > 25.0) | (df["AROONU_14_1h"] < 80.0))
      # 15m down move, 15m still not low enough, 1h high
      & ((df["RSI_3_15m"] > 25.0) | (df["AROONU_14_15m"] < 25.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 90.0))
      # 15m down move, 15m still high, 1h high
      & ((df["RSI_3_15m"] > 25.0) | (df["AROONU_14_15m"] < 40.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 80.0))
      # 15m down move, 1h high, 1d overbought
      & ((df["RSI_3_15m"] > 25.0) | (df["AROONU_14_1h"] < 60.0) | (df["ROC_9_1d"] < 60.0))
      # 15m down move, 1h high, 4h overbought
      & ((df["RSI_3_15m"] > 25.0) | (df["AROONU_14_1h"] < 70.0) | (df["ROC_9_4h"] < 40.0))
      # 15m down move, 1h & 4h high
      & ((df["RSI_3_15m"] > 25.0) | (df["AROONU_14_1h"] < 85.0) | (df["AROONU_14_4h"] < 100.0))
      # 15m down move, 1h & 4h high
      & ((df["RSI_3_15m"] > 25.0) | (df["AROONU_14_1h"] < 90.0) | (df["AROONU_14_4h"] < 90.0))
      # 15m down move, 4h high & overbought
      & ((df["RSI_3_15m"] > 25.0) | (df["AROONU_14_4h"] < 70.0) | (df["ROC_9_4h"] < 50.0))
      # 15m down move, 4h high, 1d overbought
      & ((df["RSI_3_15m"] > 25.0) | (df["AROONU_14_4h"] < 80.0) | (df["ROC_9_1d"] < 100.0))
      # 15m down move, 1h high, 1d downtrend
      & ((df["RSI_3_15m"] > 25.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 70.0) | (df["ROC_9_1d"] > -20.0))
      # 15m down move, 1h high & overbought
      & ((df["RSI_3_15m"] > 25.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 90.0) | (df["ROC_9_1h"] < 20.0))
      # 15m down move, 4h high & overbought
      & ((df["RSI_3_15m"] > 25.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 90.0) | (df["ROC_9_4h"] < 30.0))
      # 15m & 1h down move, 1h high
      & ((df["RSI_3_15m"] > 30.0) | (df["RSI_3_1h"] > 35.0) | (df["AROONU_14_1h"] < 80.0))
      # 15m & 1h down move, 1h high
      & ((df["RSI_3_15m"] > 30.0) | (df["RSI_3_1h"] > 55.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 80.0))
      # 15m & 4h down move, 15m high
      & ((df["RSI_3_15m"] > 30.0) | (df["RSI_3_4h"] > 30.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 70.0))
      # 15m down move, 1h high & overbought
      & ((df["RSI_3_15m"] > 30.0) | (df["AROONU_14_1h"] < 90.0) | (df["ROC_9_1h"] < 10.0))
      # 15m down move, 15m still high, 4h high
      & ((df["RSI_3_15m"] > 35.0) | (df["AROONU_14_15m"] < 40.0) | (df["AROONU_14_4h"] < 85.0))
      # 15m down move, 4h high & overbought
      & ((df["RSI_3_15m"] > 30.0) | (df["AROONU_14_4h"] < 100.0) | (df["ROC_9_4h"] < 40.0))
      # 15m down move, 4h high & overbought
      & ((df["RSI_3_15m"] > 30.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 90.0) | (df["ROC_9_4h"] < 40.0))
      # 15m & 1h down move, 1h high
      & ((df["RSI_3_15m"] > 35.0) | (df["RSI_3_1h"] > 40.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 70.0))
      # 15m & 1h down move, 1h high
      & ((df["RSI_3_15m"] > 35.0) | (df["RSI_3_1h"] > 65.0) | (df["AROONU_14_1h"] < 80.0))
      # 15m & 4h down move, 4h high
      & ((df["RSI_3_15m"] > 35.0) | (df["RSI_3_4h"] > 35.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 80.0))
      # 15m down move, 15m still not low enough, 1h high
      & ((df["RSI_3_15m"] > 35.0) | (df["AROONU_14_15m"] < 25.0) | (df["AROONU_14_1h"] < 80.0))
      # 15m down move, 15m still not low enough, 1h high
      & ((df["RSI_3_15m"] > 35.0) | (df["AROONU_14_15m"] < 25.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 80.0))
      # 15m down move, 1m still high, 4h overbought
      & ((df["RSI_3_15m"] > 35.0) | (df["AROONU_14_15m"] < 40.0) | (df["ROC_9_4h"] < 50.0))
      # 15m down move, 1h high, 4h overbought
      & ((df["RSI_3_15m"] > 35.0) | (df["AROONU_14_1h"] < 80.0) | (df["ROC_9_4h"] < 10.0))
      # 15m down move, 4h high & overbought
      & ((df["RSI_3_15m"] > 35.0) | (df["AROONU_14_4h"] < 100.0) | (df["ROC_9_4h"] < 70.0))
      # 15m down move, 1h high & overbought
      & ((df["RSI_3_15m"] > 35.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 90.0) | (df["ROC_9_1h"] < 40.0))
      # 15m & 1h down move, 4h high
      & ((df["RSI_3_15m"] > 40.0) | (df["RSI_3_1h"] > 40.0) | (df["AROONU_14_4h"] < 100.0))
      # 15m & 4h down move, 1h high
      & ((df["RSI_3_15m"] > 40.0) | (df["RSI_3_4h"] > 45.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 90.0))
      # 15m down move, 15m still high, 1d high
      & ((df["RSI_3_15m"] > 40.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 40.0) | (df["ROC_9_1d"] < 100.0))
      # 15m down move, 4h high & overbought
      & ((df["RSI_3_15m"] > 40.0) | (df["AROONU_14_4h"] < 100.0) | (df["ROC_9_4h"] < 40.0))
      # 15m down move, 1h high, 4h overbought
      & ((df["RSI_3_15m"] > 50.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 80.0) | (df["ROC_9_4h"] < 40.0))
      # 1h & 4h down move, 1d high
      & ((df["RSI_3_1h"] > 3.0) | (df["RSI_3_4h"] > 15.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 70.0))
      # 1h & 4h down move, 4h high
      & ((df["RSI_3_1h"] > 5.0) | (df["RSI_3_4h"] > 5.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 40.0))
      # 1h & 4h down move, 4h high
      & ((df["RSI_3_1h"] > 5.0) | (df["RSI_3_4h"] > 30.0) | (df["AROONU_14_4h"] < 70.0))
      # 1h & 4h down move, 4h still high
      & ((df["RSI_3_1h"] > 10.0) | (df["RSI_3_4h"] > 10.0) | (df["AROONU_14_4h"] < 50.0))
      # 1h & 4h down move, 4h high
      & ((df["RSI_3_1h"] > 10.0) | (df["RSI_3_4h"] > 15.0) | (df["AROONU_14_4h"] < 70.0))
      # 1h & 4h down move, 1d downtrend
      & ((df["RSI_3_1h"] > 10.0) | (df["RSI_3_4h"] > 15.0) | (df["ROC_9_1d"] > -40.0))
      # 1h & 4h down move, 1h still high
      & ((df["RSI_3_1h"] > 10.0) | (df["RSI_3_4h"] > 30.0) | (df["AROONU_14_1h"] < 50.0))
      # 1h & 4h down move, 15m still not low enough
      & ((df["RSI_3_1h"] > 10.0) | (df["RSI_3_4h"] > 40.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 30.0))
      # 1h down move, 1d high, 1d downtrend
      & ((df["RSI_3_1h"] > 10.0) | (df["AROONU_14_1d"] < 70.0) | (df["ROC_9_1d"] > -20.0))
      # 1h down move, 4h high, 1d downtrend
      & ((df["RSI_3_1h"] > 10.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 50.0) | (df["ROC_9_1d"] > -40.0))
      # 1h & 4h down move, 15m high
      & ((df["RSI_3_1h"] > 15.0) | (df["RSI_3_4h"] > 15.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 70.0))
      # 1h & 4h down move, 4h still not low enough
      & ((df["RSI_3_1h"] > 15.0) | (df["RSI_3_4h"] > 20.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 30.0))
      # 1h & 4h down move, 1d downtrend
      & ((df["RSI_3_1h"] > 15.0) | (df["RSI_3_4h"] > 20.0) | (df["ROC_9_1d"] > -30.0))
      # 1h & 4h down move, 1h high
      & ((df["RSI_3_1h"] > 15.0) | (df["RSI_3_4h"] > 35.0) | (df["AROONU_14_1h"] < 70.0))
      # 1h & 4h down move, 4h still high
      & ((df["RSI_3_1h"] > 15.0) | (df["RSI_3_4h"] > 35.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 50.0))
      # 1h down move, 1d high & overbought
      & ((df["RSI_3_1h"] > 15.0) | (df["AROONU_14_1d"] < 80.0) | (df["ROC_9_1d"] < 10.0))
      # 1h down move, 1d high, 4h downtrend
      & ((df["RSI_3_1h"] > 15.0) | (df["AROONU_14_1d"] < 90.0) | (df["ROC_9_4h"] > -20.0))
      # 1h & 4h down move, 4h high
      & ((df["RSI_3_1h"] > 20.0) | (df["RSI_3_4h"] > 35.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 70.0))
      # 1h & 1d down move, 1d high
      & ((df["RSI_3_1h"] > 20.0) | (df["RSI_3_1d"] > 50.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 60.0))
      # 1h down move, 1h high, 1d overbought
      & ((df["RSI_3_1h"] > 20.0) | (df["AROONU_14_1h"] < 60.0) | (df["ROC_9_1d"] < 50.0))
      # 1h down move, 1h high, 1d overbought
      & ((df["RSI_3_1h"] > 20.0) | (df["AROONU_14_1h"] < 70.0) | (df["ROC_9_1d"] < 20.0))
      # 1h down move, 1d high, 4h downtrend
      & ((df["RSI_3_1h"] > 20.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 80.0) | (df["ROC_9_4h"] > -20.0))
      # 1h down move, 4h downtrend, 1d overbought
      & ((df["RSI_3_1h"] > 20.0) | (df["ROC_9_4h"] > -10.0) | (df["ROC_9_1d"] < 20.0))
      # 1h & 4h down move, 1h still high
      & ((df["RSI_3_1h"] > 25.0) | (df["RSI_3_4h"] > 10.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 40.0))
      # 1h & 4h down move, 15m high
      & ((df["RSI_3_1h"] > 25.0) | (df["RSI_3_4h"] > 30.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 70.0))
      # 1h down move, 4h downtrend, 4h high
      & ((df["RSI_3_1h"] > 25.0) | (df["CMF_20_4h"] > -0.50) | (df["AROONU_14_4h"] < 70.0))
      # 1h down move, 1h still high, 1d high
      & ((df["RSI_3_1h"] > 25.0) | (df["AROONU_14_1h"] < 40.0) | (df["AROONU_14_1d"] < 90.0))
      # 1h down move, 1h still high, 4h overbought
      & ((df["RSI_3_1h"] > 25.0) | (df["AROONU_14_1h"] < 50.0) | (df["ROC_9_4h"] < 60.0))
      # 1h down move, 4h high, 1d overbought
      & ((df["RSI_3_1h"] > 25.0) | (df["AROONU_14_4h"] < 40.0) | (df["ROC_9_1d"] < 100.0))
      # 1h down move, 1d still high, 1d downtrend
      & ((df["RSI_3_1h"] > 25.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 50.0) | (df["ROC_9_1d"] > -20.0))
      # 1h & 4h down move, 1d high
      & ((df["RSI_3_1h"] > 30.0) | (df["RSI_3_4h"] > 35.0) | (df["RSI_14_1d"] < 80.0))
      # 1h & 4h down move, 4h high
      & ((df["RSI_3_1h"] > 30.0) | (df["RSI_3_4h"] > 40.0) | (df["AROONU_14_4h"] < 60.0))
      # 1h & 4h down move, 4h high
      & ((df["RSI_3_1h"] > 30.0) | (df["RSI_3_4h"] > 60.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 80.0))
      # 1h & 1d down move, 1h high
      & ((df["RSI_3_1h"] > 30.0) | (df["RSI_3_1d"] > 30.0) | (df["AROONU_14_1h"] < 60.0))
      # 1h down move, 4h & 1d down move
      & ((df["RSI_3_1h"] > 30.0) | (df["AROONU_14_4h"] < 70.0) | (df["AROONU_14_1d"] < 100.0))
      # 1h down move, 4h high & overbought
      & ((df["RSI_3_1h"] > 30.0) | (df["AROONU_14_4h"] < 85.0) | (df["ROC_9_4h"] < 80.0))
      # 1h down move, 1d still high, 1d downtrend
      & ((df["RSI_3_1h"] > 30.0) | (df["AROONU_14_1d"] < 40.0) | (df["ROC_9_1d"] > -20.0))
      # 1h down move, 1d high, 4h downtrend
      & ((df["RSI_3_1h"] > 30.0) | (df["AROONU_14_1d"] < 100.0) | (df["ROC_9_4h"] > -30.0))
      # 1h down move, 1d high & overbought
      & ((df["RSI_3_1h"] > 30.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 90.0) | (df["ROC_9_1d"] < 20.0))
      # 1h down move, 4h & 1d downtrend
      & ((df["RSI_3_1h"] > 30.0) | (df["ROC_9_4h"] > -25.0) | (df["ROC_9_1d"] > -60.0))
      # 1h & 1d down move, 1h high
      & ((df["RSI_3_1h"] > 35.0) | (df["RSI_3_1d"] > 35.0) | (df["AROONU_14_1h"] < 75.0))
      # 1h down move, 1h & 4h high
      & ((df["RSI_3_1h"] > 35.0) | (df["AROONU_14_1h"] < 60.0) | (df["AROONU_14_4h"] < 70.0))
      # 1h down move, 4h high, 1d downtrend
      & ((df["RSI_3_1h"] > 35.0) | (df["AROONU_14_4h"] < 70.0) | (df["ROC_9_1d"] > -30.0))
      # 1h down move, 1d high, 4h overbought
      & ((df["RSI_3_1h"] > 35.0) | (df["AROONU_14_1d"] < 90.0) | (df["ROC_9_4h"] < 40.0))
      # 1h down move, 4h & 1d overbought
      & ((df["RSI_3_1h"] > 35.0) | (df["ROC_9_4h"] < 10.0) | (df["ROC_9_1d"] < 50.0))
      # 1h & 1d down move, 1d high
      & ((df["RSI_3_1h"] > 35.0) | (df["RSI_3_1d"] > 45.0) | (df["AROONU_14_1d"] < 90.0))
      # 1h & 4h down move, 1h high
      & ((df["RSI_3_1h"] > 40.0) | (df["RSI_3_4h"] > 50.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 60.0))
      # 1h down move, 1h high, 1d overbought
      & ((df["RSI_3_1h"] > 40.0) | (df["AROONU_14_1h"] < 60.0) | (df["ROC_9_1d"] < 40.0))
      # 1h down move, 1h still high, 1d high
      & ((df["RSI_3_1h"] > 40.0) | (df["AROONU_14_1h"] < 50.0) | (df["AROONU_14_1d"] < 85.0))
      # 1h down move, 1h still high, 1d overbought
      & ((df["RSI_3_1h"] > 40.0) | (df["AROONU_14_1h"] < 50.0) | (df["ROC_9_1d"] < 20.0))
      # 1h down move, 1h high, 4h overbought
      & ((df["RSI_3_1h"] > 40.0) | (df["AROONU_14_1h"] < 70.0) | (df["ROC_9_4h"] < 30.0))
      # 1h down move, 1h high, 15m downtrend
      & ((df["RSI_3_1h"] > 40.0) | (df["AROONU_14_1h"] < 80.0) | (df["ROC_9_15m"] > -15.0))
      # 1h down move, 1d high & overbought
      & ((df["RSI_3_1h"] > 40.0) | (df["AROONU_14_1d"] < 80.0) | (df["ROC_9_1d"] < 50.0))
      # 1h down move, 1d high, 4h overbought
      & ((df["RSI_3_1h"] > 40.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 90.0) | (df["ROC_9_4h"] < 20.0))
      # 1h & 4h down move, 1d overbought
      & ((df["RSI_3_1h"] > 45.0) | (df["RSI_3_4h"] > 65.0) | (df["ROC_9_1d"] < 200.0))
      # 1h down move, 1h still not low enough, 1d downtrend
      & ((df["RSI_3_1h"] > 45.0) | (df["AROONU_14_1h"] < 30.0) | (df["ROC_9_1d"] > -25.0))
      # 1h down move, 1h still high, 1d overbought
      & ((df["RSI_3_1h"] > 45.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 40.0) | (df["ROC_9_1d"] < 100.0))
      # 1h down move, 4h high, 1h overbought
      & ((df["RSI_3_1h"] > 50.0) | (df["AROONU_14_4h"] < 85.0) | (df["ROC_9_1h"] < 20.0))
      # 1h down move, 1d high, 4h overbought
      & ((df["RSI_3_1h"] > 50.0) | (df["AROONU_14_1d"] < 90.0) | (df["ROC_9_4h"] < 20.0))
      # 1h down move, 1h high & overbought
      & ((df["RSI_3_1h"] > 50.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 80.0) | (df["ROC_9_1h"] < 10.0))
      # 1h down move, 1h & 4h overbought
      & ((df["RSI_3_1h"] > 50.0) | (df["ROC_9_1h"] < 10.0) | (df["ROC_9_4h"] < 100.0))
      # 1h down move, 4h & 1d overbought
      & ((df["RSI_3_1h"] > 50.0) | (df["ROC_9_4h"] < 20.0) | (df["ROC_9_1d"] < 20.0))
      # 1h & 4h down move, 1h high
      & ((df["RSI_3_1h"] > 55.0) | (df["RSI_3_4h"] > 55.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 70.0))
      # 1h down move, 1h high, 4h overbought
      & ((df["RSI_3_1h"] > 55.0) | (df["AROONU_14_1h"] < 80.0) | (df["ROC_9_4h"] < 10.0))
      # 1h down move, 4h high & overbought
      & ((df["RSI_3_1h"] > 55.0) | (df["AROONU_14_4h"] < 100.0) | (df["ROC_9_4h"] < 10.0))
      # 1h & 1d down move, 1h high
      & ((df["RSI_3_1h"] > 60.0) | (df["RSI_3_1d"] > 60.0) | (df["AROONU_14_1h"] < 70.0))
      # 1h down move, 4 high, 1h overbought
      & ((df["RSI_3_1h"] > 60.0) | (df["AROONU_14_4h"] < 100.0) | (df["ROC_9_1h"] < 10.0))
      # 1h down move, 1d high, 1h overbought
      & ((df["RSI_3_1h"] > 60.0) | (df["AROONU_14_1d"] < 90.0) | (df["ROC_9_1h"] < 10.0))
      # 1h down move, 1h high, 1d downtrend
      & ((df["RSI_3_1h"] > 60.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 70.0) | (df["ROC_9_1d"] > -10.0))
      # 1h down move, 1h high, 1d overbought
      & ((df["RSI_3_1h"] > 60.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 80.0) | (df["ROC_9_1d"] < 100.0))
      # 1h down move, 1h high, 4h overbought
      & ((df["RSI_3_1h"] > 65.0) | (df["AROONU_14_1h"] < 70.0) | (df["ROC_9_4h"] < 25.0))
      # 1h down move, 1h high, 1d overbought
      & ((df["RSI_3_1h"] > 65.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 90.0) | (df["ROC_9_1d"] < 20.0))
      # 4h down move, 1h still not low enough, 4h downtrend
      & ((df["RSI_3_4h"] > 3.0) | (df["AROONU_14_1h"] < 20.0) | (df["ROC_9_4h"] > -10.0))
      # 4h down move, 4h & 1d downtrend
      & ((df["RSI_3_4h"] > 3.0) | (df["ROC_9_4h"] > -10.0) | (df["ROC_9_1d"] > -10.0))
      # 4h & 1d down move, 15m still high
      & ((df["RSI_3_4h"] > 5.0) | (df["RSI_3_1d"] > 25.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 40.0))
      # 4h & 1d down move, 1h still not low enough
      & ((df["RSI_3_4h"] > 10.0) | (df["RSI_3_1d"] > 10.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 20.0))
      # 4h & 1d down move, 1d downtrend
      & ((df["RSI_3_4h"] > 10.0) | (df["RSI_3_1d"] > 15.0) | (df["ROC_9_1d"] > -40.0))
      # 4h & 1d down move, 1d still high
      & ((df["RSI_3_4h"] > 10.0) | (df["RSI_3_1d"] > 20.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 50.0))
      # 4h & 1d down move, 1d high
      & ((df["RSI_3_4h"] > 10.0) | (df["RSI_3_1d"] > 35.0) | (df["AROONU_14_1d"] < 100.0))
      # 4h & 1d down move, 1d overbought
      & ((df["RSI_3_4h"] > 10.0) | (df["RSI_3_1d"] > 45.0) | (df["ROC_9_1d"] < 10.0))
      # 4h down move, 15m high
      & ((df["RSI_3_4h"] > 10.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 70.0))
      # 4h & 1d down move, 4h high
      & ((df["RSI_3_4h"] > 15.0) | (df["RSI_3_1d"] > 25.0) | (df["AROONU_14_4h"] < 70.0))
      # 4h & 1d down move, 1h still high
      & ((df["RSI_3_4h"] > 15.0) | (df["RSI_3_1d"] > 30.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 40.0))
      # 4h & 1d down move, 1d high
      & ((df["RSI_3_4h"] > 15.0) | (df["RSI_3_1d"] > 25.0) | (df["AROONU_14_1d"] < 70.0))
      # 4h & 1d down move, 1d downtrend
      & ((df["RSI_3_4h"] > 15.0) | (df["RSI_3_1d"] > 25.0) | (df["ROC_9_1d"] > -15.0))
      # 4h & 1d down move, 4h still high
      & ((df["RSI_3_4h"] > 15.0) | (df["RSI_3_1d"] > 50.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 40.0))
      # 4h down move, 4h still not low enough, 1d downtrend
      & ((df["RSI_3_4h"] > 15.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 20.0) | (df["ROC_9_1d"] > -20.0))
      # 4h down move, 1h & 4h downtrend
      & ((df["RSI_3_4h"] > 15.0) | (df["ROC_9_1h"] > -30.0) | (df["ROC_9_4h"] > -30.0))
      # 4h & 1d down move, 1d high
      & ((df["RSI_3_4h"] > 20.0) | (df["RSI_3_1d"] > 20.0) | (df["AROONU_14_1d"] < 60.0))
      # 4h & 1d down move, 4h still high
      & ((df["RSI_3_4h"] > 20.0) | (df["RSI_3_1d"] > 20.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 40.0))
      # 4h & 1d down move, 1d overbought
      & ((df["RSI_3_4h"] > 20.0) | (df["RSI_3_1d"] > 45.0) | (df["ROC_9_1d"] < 40.0))
      # 4h down move, 15m high
      & ((df["RSI_3_4h"] > 20.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 80.0))
      # 4h down move, 1h high, 4h downtrend
      & ((df["RSI_3_4h"] > 20.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 70.0) | (df["ROC_9_4h"] > -20.0))
      # 4h down move, 4h still high, 4h downtrend
      & ((df["RSI_3_4h"] > 25.0) | (df["AROONU_14_4h"] < 50.0) | (df["CMF_20_4h"] > -0.40))
      # 4h down move, 4h high, 1d downtrend
      & ((df["RSI_3_4h"] > 25.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 70.0) | (df["ROC_9_1d"] > -30.0))
      # 4h & 1d down move, 1d high
      & ((df["RSI_3_4h"] > 30.0) | (df["RSI_3_1d"] > 50.0) | (df["AROONU_14_1d"] < 90.0))
      # 4h down move, 1h high, 1h downtrend
      & ((df["RSI_3_4h"] > 30.0) | (df["AROONU_14_1h"] < 70.0) | (df["ROC_9_1h"] > -10.0))
      # 4h down move, 1h high, 4h downtrend
      & ((df["RSI_3_4h"] > 30.0) | (df["AROONU_14_1h"] < 70.0) | (df["ROC_9_4h"] > -10.0))
      # 4h down move, 1h still high, 1d overbought
      & ((df["RSI_3_4h"] > 30.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 40.0) | (df["ROC_9_1d"] < 30.0))
      # 4h & 1d down move, 1d overbought
      & ((df["RSI_3_4h"] > 35.0) | (df["RSI_3_1d"] > 50.0) | (df["ROC_9_1d"] < 100.0))
      # 4h down move, 4h & 1d high
      & ((df["RSI_3_4h"] > 35.0) | (df["AROONU_14_4h"] < 80.0) | (df["AROONU_14_1d"] < 100.0))
      # 4h down move, 4h high, 1d downtrend
      & ((df["RSI_3_4h"] > 45.0) | (df["AROONU_14_4h"] < 70.0) | (df["ROC_9_1d"] > -30.0))
      # 4h & 1d down move, 1d high
      & ((df["RSI_3_4h"] > 40.0) | (df["RSI_3_1d"] > 60.0) | (df["AROONU_14_1d"] < 100.0))
      # 4h down move, 4h high, 1d downtrend
      & ((df["RSI_3_4h"] > 40.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 70.0) | (df["ROC_9_1d"] > -60.0))
      # 4h down move, 1d high & overbought
      & ((df["RSI_3_4h"] > 45.0) | (df["AROONU_14_1d"] < 70.0) | (df["ROC_9_1d"] < 20.0))
      # 4h down move, 4h high & overbought
      & ((df["RSI_3_4h"] > 45.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 60.0) | (df["ROC_9_4h"] < 20.0))
      # 4h down move, 4h high, 1d overbought
      & ((df["RSI_3_4h"] > 45.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 80.0) | (df["ROC_9_1d"] < 10.0))
      # 4h down move, 1h high, 1d downtrend
      & ((df["RSI_3_4h"] > 50.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 80.0) | (df["ROC_9_1d"] > -30.0))
      # 4h down move, 4h high & overbought
      & ((df["RSI_3_4h"] > 55.0) | (df["AROONU_14_4h"] < 70.0) | (df["ROC_9_4h"] < 20.0))
      # 4h down move, 4h high, 1d overbought
      & ((df["RSI_3_4h"] > 55.0) | (df["AROONU_14_4h"] < 70.0) | (df["ROC_9_1d"] < 100.0))
      # 4h down move, 1d high & overbought
      & ((df["RSI_3_4h"] > 55.0) | (df["AROONU_14_1d"] < 90.0) | (df["ROC_9_1d"] < 60.0))
      # 4h down move, 4h & 1d high
      & ((df["RSI_3_4h"] > 60.0) | (df["AROONU_14_4h"] < 70.0) | (df["AROONU_14_1d"] < 70.0))
      # 4h down move, 1d high, 4h overbought
      & ((df["RSI_3_4h"] > 60.0) | (df["AROONU_14_1d"] < 100.0) | (df["ROC_9_4h"] < 10.0))
      # 4h down move, 1d high & overbought
      & ((df["RSI_3_4h"] > 60.0) | (df["AROONU_14_1d"] < 100.0) | (df["ROC_9_1d"] < 200.0))
      # 4h down move, 4h still high, 4h overbought
      & ((df["RSI_3_4h"] > 60.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 50.0) | (df["ROC_9_4h"] < 10.0))
      # 4h down move, 4h high, 1d overbought
      & ((df["RSI_3_4h"] > 65.0) | (df["AROONU_14_4h"] < 75.0) | (df["ROC_9_1d"] < 30.0))
      # 4h down move, 4h high & overbought
      & ((df["RSI_3_4h"] > 65.0) | (df["AROONU_14_4h"] < 80.0) | (df["ROC_9_4h"] < 20.0))
      # 1d down move, 1d still not low enough, 1d downtrend
      & ((df["RSI_3_1d"] > 5.0) | (df["AROONU_14_1d"] < 20.0) | (df["ROC_9_1d"] > -20.0))
      # 1d down move, 15m still high
      & ((df["RSI_3_1d"] > 5.0) | (df["STOCHRSIk_14_14_3_3_15m"] < 40.0))
      # 1d down move, 1h high
      & ((df["RSI_3_1d"] > 10.0) | (df["AROONU_14_1h"] < 70.0))
      # 1d down move, 4h downtrend, 4h high
      & ((df["RSI_3_1d"] > 20.0) | (df["CMF_20_4h"] > -0.25) | (df["AROONU_14_4h"] < 70.0))
      # 1d down move, 1d still high, 1d downtrend
      & ((df["RSI_3_1d"] > 25.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 50.0) | (df["ROC_9_1d"] > -20.0))
      # 1d down move, 4h & 1d high
      & ((df["RSI_3_1d"] > 40.0) | (df["AROONU_14_4h"] < 70.0) | (df["AROONU_14_1d"] < 100.0))
      # 1d down move, 1d high & overbought
      & ((df["RSI_3_1d"] > 40.0) | (df["AROONU_14_1d"] < 80.0) | (df["ROC_9_1d"] < 10.0))
      # 1d down move, 1h high, 1d overbought
      & ((df["RSI_3_1d"] > 60.0) | (df["AROONU_14_1h"] < 70.0) | (df["ROC_9_1d"] < 100.0))
      # 4h downtrend, 4h high & over
      & ((df["CMF_20_4h"] > -0.10) | (df["AROONU_14_4h"] < 100.0) | (df["ROC_9_4h"] < 30.0))
      # 15m still high, 4h high, 1h overbought
      & ((df["AROONU_14_15m"] < 40.0) | (df["AROONU_14_4h"] < 85.0) | (df["ROC_9_1h"] < 20.0))
      # 15m still high, 4h high, 1h overbought
      & ((df["AROONU_14_15m"] < 40.0) | (df["AROONU_14_4h"] < 100.0) | (df["ROC_9_1h"] < 20.0))
      # 4h down move, 1h still high, 1d downtrend
      & ((df["RSI_3_4h"] > 15.0) | (df["AROONU_14_1h"] < 40.0) | (df["ROC_9_1d"] > -50.0))
      # 1h high, 4h high & overbought
      & ((df["AROONU_14_1h"] < 80.0) | (df["AROONU_14_4h"] < 80.0) | (df["ROC_9_4h"] < 30.0))
      # 1h & 4h high, 1h overbought
      & ((df["AROONU_14_1h"] < 80.0) | (df["AROONU_14_4h"] < 90.0) | (df["ROC_9_1h"] < 30.0))
      # 1h & 4h & 1d high
      & ((df["AROONU_14_1h"] < 80.0) | (df["AROONU_14_4h"] < 100.0) | (df["AROONU_14_1d"] < 100.0))
      # 1h & 4h high, 1d overbought
      & ((df["AROONU_14_1h"] < 80.0) | (df["AROONU_14_4h"] < 100.0) | (df["ROC_9_1d"] < 30.0))
      # 1h high, 1h overbought
      & ((df["AROONU_14_1h"] < 80.0) | (df["ROC_9_1h"] < 10.0))
      # 1h & 1d high, 4h overbought
      & ((df["AROONU_14_1h"] < 80.0) | (df["AROONU_14_1d"] < 100.0) | (df["ROC_9_4h"] < 10.0))
      # 1h high, 1h & 4h overbought
      & ((df["AROONU_14_1h"] < 80.0) | (df["ROC_9_1h"] < 10.0) | (df["ROC_9_4h"] < 10.0))
      # 1h high, 1h overbought, 1d downtrend
      & ((df["AROONU_14_1h"] < 80.0) | (df["ROC_9_1h"] < 50.0) | (df["ROC_9_1d"] > -50.0))
      # 1h high, 4h &1d overbought
      & ((df["AROONU_14_1h"] < 85.0) | (df["ROC_9_4h"] < 30.0) | (df["ROC_9_1d"] < 30.0))
      # 1h high, 4h & 1d overbought
      & ((df["AROONU_14_1h"] < 90.0) | (df["ROC_9_4h"] < 10.0) | (df["ROC_9_1d"] < 15.0))
      # 4h & 1d high, 4h overbought
      & ((df["AROONU_14_4h"] < 70.0) | (df["AROONU_14_1d"] < 100.0) | (df["ROC_9_4h"] < 50.0))
      # 4h & 1d high, 1d overbought
      & ((df["AROONU_14_4h"] < 70.0) | (df["AROONU_14_1d"] < 100.0) | (df["ROC_9_1d"] < 20.0))
      # 4h & 1d high, 4h overbought
      & ((df["AROONU_14_4h"] < 90.0) | (df["AROONU_14_1d"] < 100.0) | (df["ROC_9_4h"] < 30.0))
      # 1d high, 4h & 1d overbought
      & ((df["AROONU_14_1d"] < 70.0) | (df["ROC_9_4h"] < 30.0) | (df["ROC_9_1d"] < 200.0))
      # 1d high, 1h & 1d overbought
      & ((df["AROONU_14_1d"] < 80.0) | (df["ROC_9_1h"] < 20.0) | (df["ROC_9_1d"] < 50.0))
      # 1d high, 1d downtrend
      & ((df["AROONU_14_1d"] < 80.0) | (df["ROC_9_1d"] > -30.0))
      # 1d high, 1h & 4h downtrend
      & ((df["AROONU_14_1d"] < 85.0) | (df["ROC_9_1h"] > -30.0) | (df["ROC_9_4h"] > -50.0))
      # 1d high, 1h & 1d overbought
      & ((df["AROONU_14_1d"] < 90.0) | (df["ROC_9_1h"] < 10.0) | (df["ROC_9_1d"] < 50.0))
      # 1d high, 4h & 1d overbought
      & ((df["AROONU_14_1d"] < 100.0) | (df["ROC_9_4h"] < 10.0) | (df["ROC_9_1d"] < 20.0))
      # 15m still not low enough, 4h high, 1d overbought
      & ((df["STOCHRSIk_14_14_3_3_15m"] < 30.0) | (df["AROONU_14_4h"] < 100.0) | (df["ROC_9_1d"] < 30.0))
      # 15m still high, 4h high & overbought
      & (
        (df["STOCHRSIk_14_14_3_3_15m"] < 40.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 80.0) | (df["ROC_9_4h"] < 30.0)
      )
      # 1h high, 1d overbought
      & ((df["STOCHRSIk_14_14_3_3_1h"] < 70.0) | (df["ROC_9_1d"] < 40.0))
      # 1h high, 1h overbought, 4h downtrend
      & ((df["STOCHRSIk_14_14_3_3_1h"] < 80.0) | (df["ROC_9_1h"] < 10.0) | (df["ROC_9_4h"] > -10.0))
      # 1h high, 4h & 1d downtrend
      & ((df["STOCHRSIk_14_14_3_3_1h"] < 80.0) | (df["ROC_9_4h"] > -20.0) | (df["ROC_9_1d"] > -80.0))
      # 1h down move, 1h & 1d overbought
      & ((df["STOCHRSIk_14_14_3_3_1h"] < 90.0) | (df["ROC_9_1h"] < 10.0) | (df["ROC_9_1d"] < 50.0))
      # 1h high & overbought
      & ((df["STOCHRSIk_14_14_3_3_1h"] < 90.0) | (df["ROC_9_1h"] < 40.0))
      # 4h high, 1h & 1d overbought
      & ((df["STOCHRSIk_14_14_3_3_4h"] < 70.0) | (df["ROC_9_1h"] < 20.0) | (df["ROC_9_1d"] < 200.0))
      # 4h high, 1h & 4h overbought
      & ((df["STOCHRSIk_14_14_3_3_4h"] < 80.0) | (df["ROC_9_1h"] < 10.0) | (df["ROC_9_4h"] < 20.0))
      # 4h high, 4h & 1d overbought
      & ((df["STOCHRSIk_14_14_3_3_4h"] < 80.0) | (df["ROC_9_4h"] < 30.0) | (df["ROC_9_1d"] < 30.0))
      # 4h high, 1d downtrend
      & ((df["STOCHRSIk_14_14_3_3_4h"] < 80.0) | (df["ROC_9_1d"] > -50.0))
      # 4h high, 1h & 1d overbought
      & ((df["STOCHRSIk_14_14_3_3_4h"] < 90.0) | (df["ROC_9_1h"] < 20.0) | (df["ROC_9_1d"] < 20.0))
      # 4h high, 4h & 1d overbought
      & ((df["STOCHRSIk_14_14_3_3_4h"] < 90.0) | (df["ROC_9_4h"] < 10.0) | (df["ROC_9_1d"] < 10.0))
      # 1d hihg, 1h & 1d overbought
      & ((df["STOCHRSIk_14_14_3_3_1d"] < 90.0) | (df["ROC_9_1h"] < 30.0) | (df["ROC_9_1d"] < 100.0))
      # 1d P&D, dh downtrend
      & ((df["change_pct_1d"] > -50.0) | (df["change_pct_1d"].shift(288) < 50.0) | (df["RSI_3_4h"] > 15.0))
      # big drop in the last 20 days, 1d high, 1d downtrend
      & (
        (df["close"] > (df["high_max_20_1d"] * 0.20))
        | (df["STOCHRSIk_14_14_3_3_1d"] < 70.0)
        | (df["ROC_9_1d"] > -15.0)
      )
      # drop in last 20 days, 1h high, 1d downtrend
      & ((df["close"] > (df["high_max_20_1d"] * 0.20)) | (df["AROONU_14_1h"] < 70.0) | (df["ROC_9_1d"] > -70.0))
      # drop in last 20 days. 4h high
      & ((df["close"] > (df["high_max_20_1d"] * 0.10)) | (df["STOCHRSIk_14_14_3_3_4h"] < 90.0))
    )

    # Logic
    long_entry_logic.append(
      (df["RSI_20"] < df["RSI_20"].shift(1))
      & (df["RSI_3"] < 46.0)
      & (df["AROONU_14"] < 25.0)
      & (df["STOCHRSIk_14_14_3_3"] < 20.0)
      & (df["AROONU_14_15m"] < 50.0)
      & (df["close"] < df["SMA_16"] * 0.960)
    )


def append_long_21(df, long_entry_logic, allowed_empty_candles_288) -> None:
    """Append NFI long condition #21, the pump-mode long entry."""
    # Protections
    long_entry_logic.append(df["num_empty_288"] <= allowed_empty_candles_288)
    # long_entry_logic.append(df["protections_long_global"] == True)

    long_entry_logic.append(
      # 5m down move, 4h high, 1h overbought
      ((df["RSI_3"] > 10.0) | (df["AROONU_14_4h"] < 100.0) | (df["ROC_9_1h"] < 30.0))
      # 15m down move, 1h & 4h overbought
      & ((df["RSI_3_15m"] > 5.0) | (df["ROC_9_1h"] < 25.0) | (df["ROC_9_4h"] < 50.0))
      # 15m & 1h down move, 1d overbought
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1h"] > 20.0) | (df["ROC_9_1d"] < 80.0))
      # 15m & 1h down move, 1h high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1h"] > 35.0) | (df["AROONU_14_1h"] < 80.0))
      # 15m & 1h down move, 1h high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1h"] > 35.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 80.0))
      # 15m & 1h down move, 4h overbought
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1h"] > 45.0) | (df["ROC_9_4h"] < 50.0))
      # 15m & 1h down move, 4h overbought
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_1h"] > 60.0) | (df["ROC_9_4h"] < 70.0))
      # 15m & 4h down move, 4h high
      & ((df["RSI_3_15m"] > 10.0) | (df["RSI_3_4h"] > 55.0) | (df["AROONU_14_4h"] < 90.0))
      # 15m down move, 4h high & overbought
      & ((df["RSI_3_15m"] > 10.0) | (df["AROONU_14_4h"] < 100.0) | (df["ROC_9_4h"] < 80.0))
      # 15m down move, 1h high, 1d downtrend
      & ((df["RSI_3_15m"] > 10.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 70.0) | (df["ROC_9_1d"] > -50.0))
      # 15m down move, 4h high & overbought
      & ((df["RSI_3_15m"] > 10.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 80.0) | (df["ROC_9_4h"] < 30.0))
      # 15m down move, 1d high, 1d downtrend
      & ((df["RSI_3_15m"] > 10.0) | (df["STOCHRSIk_14_14_3_3_1d"] < 70.0) | (df["ROC_9_1d"] > -15.0))
      # 15m & 1h down move, 4h overbought
      & ((df["RSI_3_15m"] > 15.0) | (df["RSI_3_1h"] > 35.0) | (df["ROC_9_4h"] < 100.0))
      # 15m & 1d down move, 1h high
      & ((df["RSI_3_15m"] > 15.0) | (df["RSI_3_1d"] > 35.0) | (df["AROONU_14_1h"] < 90.0))
      # 15m down move, 15m still high, 4h high
      & ((df["RSI_3_15m"] > 15.0) | (df["AROONU_14_15m"] < 40.0) | (df["AROONU_14_4h"] < 100.0))
      # 15m down move, 1h & 4h high
      & ((df["RSI_3_15m"] > 15.0) | (df["AROONU_14_1h"] < 40.0) | (df["AROONU_14_4h"] < 100.0))
      # 15m down move, 1h high, 4h overbought
      & ((df["RSI_3_15m"] > 15.0) | (df["AROONU_14_1h"] < 60.0) | (df["ROC_9_4h"] < 80.0))
      # 15m down move, 4h high, 4h downtrend
      & ((df["RSI_3_15m"] > 15.0) | (df["AROONU_14_4h"] < 90.0) | (df["CMF_20_4h"] > -0.25))
      # 15m down move, 1h & 4h high
      & ((df["RSI_3_15m"] > 15.0) | (df["ROC_9_1h"] < 30.0) | (df["ROC_9_4h"] < 50.0))
      # 15m down move, 4h & 1d overbought
      & ((df["RSI_3_15m"] > 15.0) | (df["ROC_9_4h"] < 60.0) | (df["ROC_9_1d"] < 80.0))
      # 15m down move, 1h & 4h high
      & ((df["RSI_3_15m"] > 20.0) | (df["AROONU_14_1h"] < 60.0) | (df["AROONU_14_4h"] < 100.0))
      # 15m down move, 4h high, 1h overbought
      & ((df["RSI_3_15m"] > 20.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 80.0) | (df["ROC_9_1h"] < 10.0))
      # 15m down move, 4h & 1d overbought
      & ((df["RSI_3_15m"] > 20.0) | (df["ROC_9_4h"] < 80.0) | (df["ROC_9_1d"] < 200.0))
      # 15m & 1h down move, 1d overbought
      & ((df["RSI_3_15m"] > 25.0) | (df["RSI_3_1h"] > 25.0) | (df["ROC_9_1d"] < 80.0))
      # 15m & 1h down move, 1h high
      & ((df["RSI_3_15m"] > 25.0) | (df["RSI_3_1h"] > 55.0) | (df["AROONU_14_1h"] < 90.0))
      # 15m down move, 15m still high, 1d downtrend
      & ((df["RSI_3_15m"] > 25.0) | (df["AROONU_14_15m"] < 40.0) | (df["ROC_9_1d"] > -25.0))
      # 15m down move, 1h & 4h high
      & ((df["RSI_3_15m"] > 25.0) | (df["AROONU_14_1h"] < 90.0) | (df["AROONU_14_4h"] < 100.0))
      # 15m down move, 4h high, 1h overbought
      & ((df["RSI_3_15m"] > 25.0) | (df["AROONU_14_4h"] < 100.0) | (df["ROC_9_1h"] < 20.0))
      # 15m down move, 4h high, 1d overbought
      & ((df["RSI_3_15m"] > 25.0) | (df["AROONU_14_4h"] < 100.0) | (df["ROC_9_1d"] < 100.0))
      # 15m down move, 1h high & overbought
      & ((df["RSI_3_15m"] > 25.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 90.0) | (df["ROC_9_1h"] < 20.0))
      # 15m down move, 1h & 4h overbought
      & ((df["RSI_3_15m"] > 25.0) | (df["ROC_9_1h"] < 40.0) | (df["ROC_9_4h"] < 40.0))
      # 15m down move, 4h high & overbought
      & ((df["RSI_3_15m"] > 30.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 90.0) | (df["ROC_9_4h"] < 200.0))
      # 15m down move, 1h & 4h overbought
      & ((df["RSI_3_15m"] > 30.0) | (df["ROC_9_1h"] < 60.0) | (df["ROC_9_4h"] < 80.0))
      # 15m down move, 4h & 1d overbought
      & ((df["RSI_3_15m"] > 40.0) | (df["ROC_9_4h"] < 100.0) | (df["ROC_9_1d"] < 100.0))
      # 1h down move, 4h overbought, 1d downtrend
      & ((df["RSI_3_1h"] > 15.0) | (df["ROC_9_4h"] < 50.0) | (df["ROC_9_1d"] > -30.0))
      # 1h & 4h down move, 4h high
      & ((df["RSI_3_1h"] > 20.0) | (df["ROC_9_4h"] < 50.0) | (df["AROONU_14_4h"] < 80.0))
      # 1h & 4h down move, 1h still high
      & ((df["RSI_3_1h"] > 20.0) | (df["ROC_9_4h"] < 50.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 40.0))
      # 1h & 4h down move, 4h overbought
      & ((df["RSI_3_1h"] > 20.0) | (df["ROC_9_4h"] < 50.0) | (df["ROC_9_4h"] < 10.0))
      # 1h down move, 1h & 4h high
      & ((df["RSI_3_1h"] > 20.0) | (df["AROONU_14_1h"] < 80.0) | (df["AROONU_14_4h"] < 100.0))
      # 1h down move, 4h high & overbought
      & ((df["RSI_3_1h"] > 20.0) | (df["AROONU_14_4h"] < 80.0) | (df["ROC_9_4h"] < 10.0))
      # 1h down move, 4h high & overbought
      & ((df["RSI_3_1h"] > 20.0) | (df["AROONU_14_4h"] < 100.0) | (df["ROC_9_4h"] < 50.0))
      # 1h down move, 1h still high, 1d overbought
      & ((df["RSI_3_1h"] > 20.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 40.0) | (df["ROC_9_4h"] < 10.0))
      # 1h down move, 4h & 1d overbought
      & ((df["RSI_3_1h"] > 20.0) | (df["ROC_9_4h"] < 40.0) | (df["ROC_9_1d"] < 100.0))
      # 1h down move, 1d high, 4h overbought
      & ((df["RSI_3_1h"] > 25.0) | (df["AROONU_14_1d"] < 100.0) | (df["ROC_9_4h"] < 60.0))
      # 1h down move, 4h high & overbought
      & ((df["RSI_3_1h"] > 30.0) | (df["AROONU_14_4h"] < 80.0) | (df["ROC_9_4h"] < 30.0))
      # 1h down move, 1h high, 1d downtrend
      & ((df["RSI_3_1h"] > 35.0) | (df["AROONU_14_1h"] < 80.0) | (df["ROC_9_1d"] > -40.0))
      # 1h down move, 4h high, 1d downtrend
      & ((df["RSI_3_1h"] > 35.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 80.0) | (df["ROC_9_1d"] > -50.0))
      # 1h down move, 1h & 1d overbought
      & ((df["RSI_3_1h"] > 40.0) | (df["ROC_9_1h"] < 30.0) | (df["ROC_9_1d"] < 60.0))
      # 1h down move, 1h high, 4h overbought
      & ((df["RSI_3_1h"] > 45.0) | (df["AROONU_14_1h"] < 80.0) | (df["ROC_9_4h"] < 25.0))
      # 1h down move, 4h high, 1h overbought
      & ((df["RSI_3_1h"] > 45.0) | (df["AROONU_14_4h"] < 90.0) | (df["ROC_9_1h"] < 20.0))
      # 1h down move, 4h high, 1h overbought
      & ((df["RSI_3_1h"] > 45.0) | (df["AROONU_14_4h"] < 100.0) | (df["ROC_9_1h"] < 10.0))
      # 1h down move, 1d high, 1d downtrend
      & ((df["RSI_3_1h"] > 45.0) | (df["AROONU_14_1d"] < 100.0) | (df["ROC_9_1d"] > -25.0))
      # 1h down move, 1h high & overbought
      & ((df["RSI_3_1h"] > 50.0) | (df["AROONU_14_1h"] < 90.0) | (df["ROC_9_1h"] < 10.0))
      # 1h down move, 1h high, 1d downtrend
      & ((df["RSI_3_1h"] > 50.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 70.0) | (df["ROC_9_1d"] > -20.0))
      # 1h down move, 1h & 1d overbought
      & ((df["RSI_3_1h"] > 50.0) | (df["ROC_9_1h"] < 25.0) | (df["ROC_9_1d"] < 200.0))
      # 1h down move, 1h high, 4h overbought
      & ((df["RSI_3_1h"] > 55.0) | (df["AROONU_14_1h"] < 70.0) | (df["ROC_9_4h"] < 40.0))
      # 1h down move, 4h high & overbought
      & ((df["RSI_3_1h"] > 55.0) | (df["AROONU_14_4h"] < 85.0) | (df["ROC_9_4h"] < 80.0))
      # 1h down move, 4h high & overbought
      & ((df["RSI_3_1h"] > 60.0) | (df["AROONU_14_4h"] < 80.0) | (df["ROC_9_4h"] < 100.0))
      # 1h down move, 1h & 1d overbought
      & ((df["RSI_3_1h"] > 60.0) | (df["ROC_9_1h"] < 10.0) | (df["ROC_9_1d"] < 250.0))
      # 1h down move, 1h high, 4h overbought
      & ((df["RSI_3_1h"] > 65.0) | (df["AROONU_14_1h"] < 80.0) | (df["ROC_9_4h"] < 30.0))
      # 1h down move, 1h overbought
      & ((df["RSI_3_1h"] > 65.0) | (df["ROC_9_1h"] < 40.0))
      # 4h down move, 1h high & overbought
      & ((df["RSI_3_4h"] > 3.0) | (df["AROONU_14_1h"] < 85.0) | (df["ROC_9_1h"] < 60.0))
      # 1d down move, 4h high & overbought
      & ((df["RSI_3_1d"] > 5.0) | (df["AROONU_14_4h"] < 90.0) | (df["ROC_9_4h"] < 50.0))
      # 1d down move, 1h high
      & ((df["RSI_3_1d"] > 10.0) | (df["AROONU_14_1h"] < 70.0))
      # 1d down move, 4h high, 1h overbought
      & ((df["RSI_3_1d"] > 20.0) | (df["AROONU_14_4h"] < 100.0) | (df["ROC_9_1h"] < 25.0))
      # 1d down move, 4h high, 4h overbought
      & ((df["RSI_3_1d"] > 20.0) | (df["AROONU_14_4h"] < 100.0) | (df["ROC_9_4h"] < 40.0))
      # 1d down move, 1h & 4h overbought
      & ((df["RSI_3_1d"] > 30.0) | (df["ROC_9_1h"] < 30.0) | (df["ROC_9_4h"] < 60.0))
      # 1d down move, 4h high & overbought
      & ((df["RSI_3_1d"] > 35.0) | (df["AROONU_14_4h"] < 100.0) | (df["ROC_9_4h"] < 20.0))
      # 1d down move, 1h & 4h high
      & ((df["RSI_3_1d"] > 40.0) | (df["AROONU_14_1h"] < 80.0) | (df["AROONU_14_4h"] < 100.0))
      # 1d down move, 4h & 1d high
      & ((df["RSI_3_1d"] > 40.0) | (df["AROONU_14_4h"] < 70.0) | (df["AROONU_14_1d"] < 100.0))
      # 1d down move, 4h high & overbought
      & ((df["RSI_3_1d"] > 45.0) | (df["AROONU_14_4h"] < 80.0) | (df["ROC_9_4h"] < 30.0))
      # 1d down move, 1h high, 1d overbought
      & ((df["RSI_3_1d"] > 60.0) | (df["AROONU_14_1h"] < 75.0) | (df["ROC_9_1d"] < 20.0))
      # 1d down move, 1h & 4h high
      & ((df["RSI_3_1d"] > 65.0) | (df["AROONU_14_1h"] < 90.0) | (df["AROONU_14_4h"] < 100.0))
      # 1d downtrend, 1d high & overbought
      & ((df["CMF_20_1d"] > -0.40) | (df["AROONU_14_1d"] < 85.0) | (df["ROC_9_1d"] < 20.0))
      # 15m not low enough, 1h high, 1d overbought
      & ((df["AROONU_14_15m"] < 25.0) | (df["STOCHRSIk_14_14_3_3_1h"] < 90.0) | (df["ROC_9_1d"] < 200.0))
      # 1h still high, 1h & 4h overbought
      & ((df["AROONU_14_1h"] < 50.0) | (df["ROC_9_1h"] < 40.0) | (df["ROC_9_4h"] < 40.0))
      # 1h & 4h high, 4h overbought
      & ((df["AROONU_14_1h"] < 70.0) | (df["AROONU_14_4h"] < 100.0) | (df["ROC_9_4h"] < 20.0))
      # 1h & 4h high, 4h overbought
      & ((df["AROONU_14_1h"] < 80.0) | (df["AROONU_14_4h"] < 80.0) | (df["ROC_9_4h"] < 30.0))
      # 1h & 4h high, 1h overbought
      & ((df["AROONU_14_1h"] < 80.0) | (df["AROONU_14_4h"] < 90.0) | (df["ROC_9_1h"] < 30.0))
      # 1h & 4h high, 1d overbought
      & ((df["AROONU_14_1h"] < 80.0) | (df["AROONU_14_4h"] < 90.0) | (df["ROC_9_1d"] < 100.0))
      # 1h & 1d high, 4h overbought
      & ((df["AROONU_14_1h"] < 90.0) | (df["AROONU_14_1d"] < 90.0) | (df["ROC_9_4h"] < 30.0))
      # 1h & 4h high, 1h overbought
      & ((df["AROONU_14_1h"] < 80.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 90.0) | (df["ROC_9_1h"] < 10.0))
      # 1h high & overbought
      & ((df["AROONU_14_1h"] < 80.0) | (df["ROC_9_1h"] < 80.0))
      # 1h high, 1h & 4h overbought
      & ((df["AROONU_14_1h"] < 80.0) | (df["ROC_9_1h"] < 10.0) | (df["ROC_9_4h"] < 10.0))
      # 1h high, 4h overbought, 1d downtrend
      & ((df["AROONU_14_1h"] < 80.0) | (df["ROC_9_4h"] < 10.0) | (df["ROC_9_1d"] > -50.0))
      # 1h & 4h high, 15m downtrend
      & ((df["AROONU_14_1h"] < 85.0) | (df["AROONU_14_4h"] < 85.0) | (df["ROC_9_15m"] > -40.0))
      # 1h & 4h high, 1h overbought
      & ((df["AROONU_14_1h"] < 90.0) | (df["AROONU_14_4h"] < 90.0) | (df["ROC_9_1h"] < 10.0))
      # 4h high, 1h overbought, 1d downtrend
      & ((df["AROONU_14_4h"] < 80.0) | (df["ROC_9_1h"] < 30.0) | (df["ROC_9_1d"] > -30.0))
      # 4h & 1d high, 4h downtrend
      & ((df["AROONU_14_4h"] < 85.0) | (df["AROONU_14_1d"] < 100.0) | (df["CMF_20_4h"] > -0.30))
      # 4h & 1d high, 1h overbought
      & ((df["AROONU_14_4h"] < 85.0) | (df["AROONU_14_1d"] < 90.0) | (df["ROC_9_1h"] < 20.0))
      # 4h & 1d high, 4h overbought
      & ((df["AROONU_14_4h"] < 85.0) | (df["AROONU_14_1d"] < 90.0) | (df["ROC_9_4h"] < 60.0))
      # 4h high, 1h & 4h overbought
      & ((df["AROONU_14_4h"] < 85.0) | (df["ROC_9_1h"] < 10.0) | (df["ROC_9_4h"] < 20.0))
      # 4h high, 1d high & overbought
      & ((df["AROONU_14_4h"] < 90.0) | (df["AROONU_14_1d"] < 100.0) | (df["ROC_9_1d"] < 30.0))
      # 4h high, 1h & 4h overbought
      & ((df["AROONU_14_4h"] < 90.0) | (df["ROC_9_1h"] < 40.0) | (df["ROC_9_4h"] < 40.0))
      # 4h high, 4h & 1d overbought
      & ((df["AROONU_14_4h"] < 90.0) | (df["ROC_9_4h"] < 30.0) | (df["ROC_9_1d"] < 100.0))
      # 4h high, 1h & 4h overbought
      & ((df["AROONU_14_4h"] < 100.0) | (df["ROC_9_1h"] < 40.0) | (df["ROC_9_4h"] < 80.0))
      # 1d high, 1h & 4h overbought
      & ((df["AROONU_14_1d"] < 100.0) | (df["ROC_9_1h"] < 10.0) | (df["ROC_9_4h"] < 20.0))
      # 1h high, 1h & 4h overbought
      & ((df["STOCHRSIk_14_14_3_3_1h"] < 60.0) | (df["ROC_9_1h"] < 40.0) | (df["ROC_9_4h"] < 40.0))
      # 1h high, 1h overbought
      & ((df["STOCHRSIk_14_14_3_3_1h"] < 80.0) | (df["ROC_9_1h"] < 10.0))
      # 1h high, 4h overbought. 1d downtrend
      & ((df["STOCHRSIk_14_14_3_3_1h"] < 80.0) | (df["ROC_9_4h"] < 40.0) | (df["CMF_20_1d"] > -0.25))
      # 4h high, 1h & 4h overbought
      & ((df["STOCHRSIk_14_14_3_3_4h"] < 90.0) | (df["ROC_9_1h"] < 10.0) | (df["ROC_9_4h"] < 20.0))
      # 4h high & 4h & 1d overbought
      & ((df["STOCHRSIk_14_14_3_3_4h"] < 90.0) | (df["ROC_9_4h"] < 20.0) | (df["ROC_9_1d"] < 20.0))
      # 1d high, 1h & 4h overbought
      & ((df["STOCHRSIk_14_14_3_3_1d"] < 80.0) | (df["ROC_9_1h"] < 10.0) | (df["ROC_9_4h"] < 20.0))
      # 1d hihg, 1h & 1d overbought
      & ((df["STOCHRSIk_14_14_3_3_1d"] < 90.0) | (df["ROC_9_1h"] < 30.0) | (df["ROC_9_1d"] < 100.0))
      # 1d high, 4h & 1d overbought
      & ((df["STOCHRSIk_14_14_3_3_1d"] < 90.0) | (df["ROC_9_4h"] < 40.0) | (df["ROC_9_1d"] < 100.0))
    )

    # Logic
    long_entry_logic.append(
      (df["AROONU_14"] < 25.0)
      & (df["STOCHRSIk_14_14_3_3"] < 20.0)
      & (df["AROONU_14_15m"] < 50.0)
      & (df["close"] < df["EMA_16"] * 0.960)
      & (((df["EMA_50"] - df["EMA_200"]) / df["close"] * 100.0) > 6.0)
    )

