"""Long entry condition helpers extracted from NFI."""

import numpy as np

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


