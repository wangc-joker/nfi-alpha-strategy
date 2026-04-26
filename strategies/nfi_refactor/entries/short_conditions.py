import numpy as np
import pandas as pd

def append_short_504(df, short_entry_logic, allowed_empty_candles_288) -> None:
    """Append NFI short condition #504, a normal-mode short entry."""
    # Protections
    short_entry_logic.append(df["num_empty_288"] <= allowed_empty_candles_288)

    short_entry_logic.append(df["RSI_3_1h"] >= 5.0)
    short_entry_logic.append(df["RSI_3_4h"] >= 20.0)
    short_entry_logic.append(df["RSI_3_1d"] >= 20.0)
    short_entry_logic.append(df["RSI_14_1h"] > 20.0)
    short_entry_logic.append(df["RSI_14_4h"] > 20.0)
    short_entry_logic.append(df["RSI_14_1d"] > 10.0)
    # 15m & 1h down move, 4h still high
    short_entry_logic.append(
        (df["RSI_3_15m"] < 95.0)
        | (df["MFI_14_15m"] < 90.0)
        | (df["RSI_3_1h"] < 80.0)
        | (df["STOCHRSIk_14_14_3_3_4h"] > 50.0)
    )
    # 15m & 1h down move, 4h still high
    short_entry_logic.append(
        (df["RSI_3_15m"] < 90.0) | (df["MFI_14_15m"] < 85.0) | (df["STOCHRSIk_14_14_3_3_4h"] > 30.0)
    )
    # 14m & 4h down move, 4h still high
    short_entry_logic.append(
        (df["RSI_3_15m"] < 90.0) | (df["RSI_3_4h"] < 85.0) | (df["STOCHRSIk_14_14_3_3_4h"] > 60.0)
    )
    # 15m down move, 1h & 4h still high
    short_entry_logic.append(
        (df["RSI_3_15m"] < 90.0) | (df["UO_7_14_28_1h"] < 45.0) | (df["STOCHRSIk_14_14_3_3_4h"] > 30.0)
    )
    # 1h strong down move, 4h still high
    short_entry_logic.append(
        (df["RSI_3_1h"] < 95.0) | (df["RSI_14_change_pct_1h"] < 40.0) | (df["STOCHRSIk_14_14_3_3_4h"] > 30.0)
    )
    # 1h strong down move, 4h down move, 4h still high
    short_entry_logic.append(
        (df["RSI_3_1h"] < 95.0) | (df["RSI_3_change_pct_4h"] < 50.0) | (df["STOCHRSIk_14_14_3_3_4h"] > 50.0)
    )
    # 1h & 4h down move, 4h still not low enough
    short_entry_logic.append(
        (df["RSI_3_1h"] < 95.0) | (df["RSI_3_4h"] < 90.0) | (df["STOCHRSIk_14_14_3_3_4h"] > 75.0)
    )
    # 1h & 4h down move, 4h still not low enough
    short_entry_logic.append((df["RSI_3_1h"] < 95.0) | (df["RSI_3_4h"] < 75.0) | (df["AROOND_14_4h"] < 50.0))
    # 15m down move, 1h strong downtrend
    short_entry_logic.append((df["RSI_3_15m"] < 95.0) | (df["RSI_3_1h"] < 95.0) | (df["MFI_14_1h"] > 5.0))
    # 15m downtrend, 4h down move, 4h stil high
    short_entry_logic.append(
        (df["ROC_9_15m"] > -20.0) | (df["RSI_3_4h"] < 75.0) | (df["STOCHRSIk_14_14_3_3_4h"] > 30.0)
    )

    # Logic
    short_entry_logic.append(df["AROOND_14"] < 25.0)
    short_entry_logic.append(df["AROOND_14_15m"] < 25.0)
    short_entry_logic.append(df["close"] > (df["EMA_9"] * 1.058))
    short_entry_logic.append(df["close"] > (df["EMA_20"] * 1.040))

def append_short_501(df, short_entry_logic, allowed_empty_candles_288) -> None:
    """Append NFI short condition #501, a normal-mode short entry."""
    short_entry_logic.append(df["num_empty_288"] <= allowed_empty_candles_288)
    short_entry_logic.append(df["protections_short_global"] == True)
    short_entry_logic.append(df["global_protections_short_pump"] == True)
    short_entry_logic.append(df["global_protections_short_dump"] == True)

    short_entry_logic.append(df["RSI_3_1h"] >= 5.0)
    short_entry_logic.append(df["RSI_3_4h"] >= 20.0)
    short_entry_logic.append(df["RSI_3_1d"] >= 20.0)
    short_entry_logic.append(df["RSI_14_1h"] > 20.0)
    short_entry_logic.append(df["RSI_14_4h"] > 20.0)
    short_entry_logic.append(df["RSI_14_1d"] > 10.0)
    # 5m up move, 4h still not high enough
    short_entry_logic.append((df["RSI_3"] < 97.0) | (df["AROONU_14_4h"] > 60.0))
    # 5m up move, 4h still low
    short_entry_logic.append((df["RSI_3"] < 97.0) | (df["STOCHRSIk_14_14_3_3_4h"] > 50.0))
    # 5m & 15m strong up move
    short_entry_logic.append((df["RSI_3"] < 95.0) | (df["RSI_3_15m"] < 95.0))
    # 5m & 1h up move, 1d uptrend
    short_entry_logic.append((df["RSI_3"] < 95.0) | (df["RSI_3_1h"] < 90.0) | (df["ROC_9_1d"] < 100.0))
    # 5m up move, 15m & 1h still not high enough
    short_entry_logic.append((df["RSI_3"] < 95.0) | (df["AROOND_14_15m"] < 25.0) | (df["AROOND_14_1h"] < 25.0))
    # 4m up move, 1h & 4h still low
    short_entry_logic.append(
      (df["RSI_3"] < 95.0) | (df["STOCHRSIk_14_14_3_3_1h"] > 70.0) | (df["STOCHRSIk_14_14_3_3_4h"] > 70.0)
    )
    # 4m & 1h up move, 1h still low
    short_entry_logic.append(
      (df["RSI_3"] < 90.0) | (df["RSI_3_1h"] < 80.0) | (df["STOCHRSIk_14_14_3_3_1h"] > 50.0)
    )
    # 15m & 1h up move, 4h low
    short_entry_logic.append((df["RSI_3"] < 90.0) | (df["RSI_3_1h"] < 80.0) | (df["AROONU_14_4h"] > 20.0))
    # 5m up move, 15m & 1h uptrend
    short_entry_logic.append((df["RSI_3"] < 90.0) | (df["CMF_20_15m"] < 0.30) | (df["CMF_20_1h"] < 0.30))
    # 5m up move, 15m stil low
    short_entry_logic.append((df["RSI_3"] < 90.0) | (df["AROONU_14_15m"] > 50.0))
    # 5m up move, 15m & 1h still not high enough
    short_entry_logic.append(
      (df["RSI_3"] < 90.0) | (df["STOCHRSIk_14_14_3_3_15m"] > 60.0) | (df["STOCHRSIk_14_14_3_3_1h"] > 75.0)
    )
    # 15m up move, 1h low
    short_entry_logic.append((df["RSI_3_15m"] < 97.0) | (df["AROONU_14_1h"] > 30.0))
    # 15m & 1h up move, 4h still going up
    short_entry_logic.append(
      (df["RSI_3_15m"] < 95.0) | (df["RSI_3_1h"] < 95.0) | (df["CCI_20_change_pct_4h"] < -0.0)
    )
    # 15m & 1h up move, 4h still not high enough
    short_entry_logic.append(
      (df["RSI_3_15m"] < 95.0) | (df["RSI_3_1h"] < 90.0) | (df["STOCHRSIk_14_14_3_3_4h"] > 80.0)
    )
    # 15m & 1h up move, 4h still not high enough
    short_entry_logic.append(
      (df["RSI_3_15m"] < 95.0) | (df["RSI_3_1h"] < 85.0) | (df["STOCHRSIk_14_14_3_3_4h"] > 50.0)
    )
    # 15m & 1h up move, 1h still low
    short_entry_logic.append(
      (df["RSI_3_15m"] < 95.0) | (df["RSI_3_1h"] < 70.0) | (df["STOCHRSIk_14_14_3_3_1h"] > 50.0)
    )
    # 15m & 4h up move, 1h still not high enough
    short_entry_logic.append(
      (df["RSI_3_15m"] < 95.0) | (df["RSI_3_4h"] < 95.0) | (df["STOCHRSIk_14_14_3_3_1h"] > 75.0)
    )
    # 15m up move, 1d lost, 1h low
    short_entry_logic.append((df["RSI_3_15m"] < 95.0) | (df["RSI_14_1d"] > 40.0) | (df["AROONU_14_1h"] > 40.0))
    # 15m up move, 15m & 4h uptrend
    short_entry_logic.append(
      (df["RSI_3_15m"] < 95.0) | (df["AROONU_14_15m"] < 90.0) | (df["AROONU_14_4h"] < 90.0)
    )
    # 15m up move, 15m stil not high enough, 1h low
    short_entry_logic.append(
      (df["RSI_3_15m"] < 95.0) | (df["STOCHRSIk_14_14_3_3_15m"] > 70.0) | (df["STOCHRSIk_14_14_3_3_1h"] > 10.0)
    )
    # 15m up move, 1h still not high enough, 4h low
    short_entry_logic.append(
      (df["RSI_3_15m"] < 95.0) | (df["STOCHRSIk_14_14_3_3_1h"] > 70.0) | (df["AROONU_14_4h"] > 20.0)
    )
    # 15m up move, 1h & 4h still not high enough
    short_entry_logic.append(
      (df["RSI_3_15m"] < 95.0) | (df["STOCHRSIk_14_14_3_3_1h"] > 70.0) | (df["STOCHRSIk_14_14_3_3_4h"] > 80.0)
    )
    # 15m up move, 4h still not high enough
    short_entry_logic.append((df["RSI_3_15m"] < 95.0) | (df["AROONU_14_4h"] > 70.0))
    # 15m up move, 4h & 1d uptrend
    short_entry_logic.append((df["RSI_3_15m"] < 95.0) | (df["ROC_9_4h"] < 30.0) | (df["ROC_9_1d"] < 50.0))
    # 15m up move, 1h up move, 1h still not high enough
    short_entry_logic.append(
      (df["RSI_3_15m"] < 95.0) | (df["RSI_3_change_pct_1h"] < 80.0) | (df["STOCHRSIk_14_14_3_3_1h"] > 50.0)
    )
    # 15m & 1h up move, 1h still not high enough
    short_entry_logic.append(
      (df["RSI_3_15m"] < 90.0) | (df["RSI_3_1h"] < 85.0) | (df["STOCHRSIk_14_14_3_3_1h"] > 70.0)
    )
    # 15m & 1h up move, 1h not high enough
    short_entry_logic.append((df["RSI_3_15m"] < 90.0) | (df["RSI_3_1h"] < 90.0) | (df["AROOND_14_1h"] < 50.0))
    # 15m & 1h up move, 1d stil not high enough
    short_entry_logic.append((df["RSI_3_15m"] < 90.0) | (df["RSI_3_1h"] < 90.0) | (df["RSI_14_1h"] > 80.0))
    # 15m & 1h up move, 1d uptrend
    short_entry_logic.append((df["RSI_3_15m"] < 90.0) | (df["RSI_3_1h"] < 80.0) | (df["ROC_9_1d"] < 40.0))
    # 15m & 1h up move, 15m still not high enough
    short_entry_logic.append(
      (df["RSI_3_15m"] < 90.0) | (df["RSI_3_1h"] < 80.0) | (df["STOCHRSIk_14_14_3_3_15m"] > 60.0)
    )
    # 15m & 4h up move, 1h still not high enough
    short_entry_logic.append(
      (df["RSI_3_15m"] < 90.0) | (df["RSI_3_4h"] < 90.0) | (df["STOCHRSIk_14_14_3_3_1h"] > 80.0)
    )
    # 15m & 4h up move, 1h still not high enough
    short_entry_logic.append(
      (df["RSI_3_15m"] < 90.0) | (df["RSI_3_4h"] < 90.0) | (df["STOCHRSIk_14_14_3_3_1h"] > 90.0)
    )
    # 15m & 4h up move, 4h not high enough
    short_entry_logic.append((df["RSI_3_15m"] < 90.0) | (df["RSI_3_4h"] < 90.0) | (df["AROOND_14_4h"] < 50.0))
    # 15m & 4h up move, 1d low
    short_entry_logic.append(
      (df["RSI_3_15m"] < 90.0) | (df["RSI_3_4h"] < 85.0) | (df["STOCHRSIk_14_14_3_3_1d"] > 30.0)
    )
    # 15m & 4h up move, 1h low
    short_entry_logic.append(
      (df["RSI_3_15m"] < 90.0) | (df["RSI_3_4h"] < 70.0) | (df["STOCHRSIk_14_14_3_3_1h"] > 20.0)
    )
    # 15m & 4h up move, 4h low
    short_entry_logic.append((df["RSI_3_15m"] < 90.0) | (df["RSI_3_4h"] < 60.0) | (df["AROONU_14_4h"] > 30.0))
    # 15m up move, 1h & 4h low
    short_entry_logic.append(
      (df["RSI_3_15m"] < 90.0) | (df["AROONU_14_1h"] > 40.0) | (df["AROONU_14_4h"] > 10.0)
    )
    # 15m up move, 1h still low, 4h low
    short_entry_logic.append(
      (df["RSI_3_15m"] < 90.0) | (df["AROONU_14_1h"] > 60.0) | (df["STOCHRSIk_14_14_3_3_4h"] > 30.0)
    )
    # 15m up move, 1h low, 4h still not high enough
    short_entry_logic.append(
      (df["RSI_3_15m"] < 90.0) | (df["STOCHRSIk_14_14_3_3_1h"] > 30.0) | (df["STOCHRSIk_14_14_3_3_4h"] > 70.0)
    )
    # 15m & 4h up move, 1d low
    short_entry_logic.append(
      (df["RSI_3_15m"] < 90.0) | (df["RSI_3_4h"] < 70.0) | (df["STOCHRSIk_14_14_3_3_1d"] > 20.0)
    )
    # 15m & 1h up move, 4h low
    short_entry_logic.append(
      (df["RSI_3_15m"] < 85.0) | (df["RSI_3_1h"] < 85.0) | (df["STOCHRSIk_14_14_3_3_4h"] > 20.0)
    )
    # 15m & 1h up move, 1d still low
    short_entry_logic.append(
      (df["RSI_3_15m"] < 85.0) | (df["RSI_3_1h"] < 85.0) | (df["STOCHRSIk_14_14_3_3_1d"] > 60.0)
    )
    # 15m & 1h up move, 1h low
    short_entry_logic.append(
      (df["RSI_3_15m"] < 85.0) | (df["RSI_3_1h"] < 70.0) | (df["STOCHRSIk_14_14_3_3_1h"] > 30.0)
    )
    # 15m & 1h up move, 4h low
    short_entry_logic.append(
      (df["RSI_3_15m"] < 85.0) | (df["RSI_3_1h"] < 70.0) | (df["STOCHRSIk_14_14_3_3_4h"] > 30.0)
    )
    # 15m & 4h down move, 4h still not high enough
    short_entry_logic.append(
      (df["RSI_3_15m"] < 85.0) | (df["RSI_3_4h"] < 90.0) | (df["STOCHRSIk_14_14_3_3_4h"] > 75.0)
    )
    # 15m & 4h up move, 15m low
    short_entry_logic.append(
      (df["RSI_3_15m"] < 85.0) | (df["RSI_3_4h"] < 85.0) | (df["STOCHRSIk_14_14_3_3_15m"] > 50.0)
    )
    # 15m down move, 15m still not high enough, 4h low
    short_entry_logic.append(
      (df["RSI_3_15m"] < 85.0) | (df["RSI_14_15m"] > 70.0) | (df["STOCHRSIk_14_14_3_3_4h"] > 40.0)
    )
    # 15m up move, 4h overbought
    short_entry_logic.append((df["RSI_3_15m"] < 85.0) | (df["ROC_9_4h"] < 50.0))
    # 15m & 1h up move, 1h still not high enough
    short_entry_logic.append((df["RSI_3_15m"] < 80.0) | (df["RSI_3_1h"] < 70.0) | (df["AROONU_14_1h"] > 60.0))
    # 15m & 4h up move, 15m still low
    short_entry_logic.append((df["RSI_3_15m"] < 80.0) | (df["RSI_3_4h"] < 80.0) | (df["AROONU_14_15m"] > 50.0))
    # 15m up move, 1h low
    short_entry_logic.append((df["RSI_3_15m"] < 80.0) | (df["STOCHRSIk_14_14_3_3_1h"] > 20.0))
    # 15m & 1h up move, 1h low
    short_entry_logic.append((df["RSI_3_15m"] < 70.0) | (df["RSI_3_1h"] < 70.0) | (df["AROONU_14_1h"] > 30.0))
    # 15m up move, 15m still not high enough, 1h still low
    short_entry_logic.append(
      (df["RSI_3_15m"] < 70.0) | (df["STOCHRSIk_14_14_3_3_15m"] > 90.0) | (df["STOCHRSIk_14_14_3_3_1h"] > 50.0)
    )
    # 1h & 4h up move, 1h still not high enough
    short_entry_logic.append(
      (df["RSI_3_1h"] < 95.0) | (df["RSI_3_4h"] < 95.0) | (df["STOCHRSIk_14_14_3_3_1h"] > 70.0)
    )
    # 1h up move, 4h low
    short_entry_logic.append((df["RSI_3_1h"] < 95.0) | (df["STOCHRSIk_14_14_3_3_4h"] > 30.0))
    # 1h & 4h up move, 4h still not high enough
    short_entry_logic.append((df["RSI_3_1h"] < 95.0) | (df["RSI_3_4h"] < 95.0) | (df["UO_7_14_28_4h"] > 60.0))
    # 1h & 4h up move, 4h still low
    short_entry_logic.append(
      (df["RSI_3_1h"] < 95.0) | (df["RSI_3_4h"] < 85.0) | (df["STOCHRSIk_14_14_3_3_4h"] > 50.0)
    )
    # 1h & 4h up move, 4h uptrend
    short_entry_logic.append((df["RSI_3_1h"] < 95.0) | (df["RSI_3_4h"] < 85.0) | (df["ROC_9_4h"] < 40.0))
    # 1h & 1d strong up move
    short_entry_logic.append((df["RSI_3_1h"] < 95.0) | (df["RSI_3_1d"] < 95.0))
    # 1h up move, 4h still low
    short_entry_logic.append((df["RSI_3_1h"] < 95.0) | (df["RSI_14_4h"] > 60.0))
    # 1h up move, 1d still low, 1h uptrend
    short_entry_logic.append((df["RSI_3_1h"] < 95.0) | (df["RSI_14_1d"] > 50.0) | (df["ROC_9_1h"] < 30.0))
    # 1h & 4h strong up move
    short_entry_logic.append((df["RSI_3_1h"] < 95.0) | (df["MFI_14_1h"] < 95.0) | (df["RSI_3_4h"] < 95.0))
    # 1h up move, 1d still low, 1h uptrend
    short_entry_logic.append(
      (df["RSI_3_1h"] < 95.0) | (df["STOCHRSIk_14_14_3_3_1d"] > 50.0) | (df["ROC_9_1h"] < 20.0)
    )
    # 1h strong up move, 15m still move higher
    short_entry_logic.append((df["RSI_3_1h"] < 95.0) | (df["CCI_20_change_pct_15m"] < -0.0))
    # 1h & 4h up move, 1h still low
    short_entry_logic.append(
      (df["RSI_3_1h"] < 90.0) | (df["RSI_3_4h"] < 90.0) | (df["STOCHRSIk_14_14_3_3_1h"] > 50.0)
    )
    # 1h & 4h up move, 1d still not high enough
    short_entry_logic.append(
      (df["RSI_3_1h"] < 90.0) | (df["RSI_3_4h"] < 90.0) | (df["STOCHRSIk_14_14_3_3_1d"] > 70.0)
    )
    # 1h up move, 4h low, 1d overbought
    short_entry_logic.append((df["RSI_3_1h"] < 90.0) | (df["AROONU_14_4h"] > 20.0) | (df["ROC_9_1d"] < 50.0))
    # 1h up move, 1h still low, 1d uptrend
    short_entry_logic.append(
      (df["RSI_3_1h"] < 90.0) | (df["STOCHRSIk_14_14_3_3_1h"] > 60.0) | (df["ROC_9_1d"] < 50.0)
    )
    # 1h up move, 1h still not high enough, 1d low
    short_entry_logic.append(
      (df["RSI_3_1h"] < 90.0) | (df["STOCHRSIk_14_14_3_3_1h"] > 70.0) | (df["STOCHRSIk_14_14_3_3_1d"] > 30.0)
    )
    # 1h up move, 4h low, 1h uptrend
    short_entry_logic.append(
      (df["RSI_3_1h"] < 90.0) | (df["STOCHRSIk_14_14_3_3_4h"] > 20.0) | (df["ROC_9_1h"] < 10.0)
    )
    # 1h up move, 4h low, 1h overbought
    short_entry_logic.append(
      (df["RSI_3_1h"] < 90.0) | (df["STOCHRSIk_14_14_3_3_4h"] > 40.0) | (df["ROC_9_1h"] < 30.0)
    )
    # 1h up move, 15m & 1h uptrend
    short_entry_logic.append((df["RSI_3_1h"] < 90.0) | (df["ROC_9_15m"] < 15.0) | (df["ROC_9_1h"] < 15.0))
    # 1h up move, 15m & 4h still low
    short_entry_logic.append(
      (df["RSI_3_1h"] < 85.0) | (df["STOCHRSIk_14_14_3_3_15m"] > 50.0) | (df["STOCHRSIk_14_14_3_3_4h"] > 50.0)
    )
    # 1h & 4h up move, 15m still not high enough
    short_entry_logic.append((df["RSI_3_1h"] < 85.0) | (df["RSI_3_4h"] < 85.0) | (df["AROOND_14_15m"] < 50.0))
    # 1h & 4h up move, 15m still not high enough
    short_entry_logic.append(
      (df["RSI_3_1h"] < 85.0) | (df["RSI_3_4h"] < 85.0) | (df["STOCHRSIk_14_14_3_3_15m"] > 90.0)
    )
    # 1h up move, 15m still not high enough, 1h still low
    short_entry_logic.append(
      (df["RSI_3_1h"] < 80.0) | (df["STOCHRSIk_14_14_3_3_15m"] > 80.0) | (df["STOCHRSIk_14_14_3_3_1h"] > 50.0)
    )
    # 1h up move, 1h still low
    short_entry_logic.append((df["RSI_3_1h"] < 80.0) | (df["STOCHRSIk_14_14_3_3_1h"] > 60.0))
    # 4h & 1d strong up move
    short_entry_logic.append((df["RSI_3_4h"] < 95.0) | (df["RSI_3_1d"] < 95.0))
    # 4h up move, 15m still low, 1h not high enough
    short_entry_logic.append(
      (df["RSI_3_4h"] < 95.0) | (df["STOCHRSIk_14_14_3_3_15m"] > 50.0) | (df["AROOND_14_1h"] < 25.0)
    )
    # 4h up move, 15m still not high enough, 4h overbought
    short_entry_logic.append(
      (df["RSI_3_4h"] < 95.0) | (df["STOCHRSIk_14_14_3_3_15m"] > 70.0) | (df["ROC_9_4h"] < 60.0)
    )
    # 4h up move, 15m uptrend
    short_entry_logic.append((df["RSI_3_4h"] < 95.0) | (df["ROC_9_15m"] < 20.0))
    # 4h up move, 1h uptrend
    short_entry_logic.append((df["RSI_3_4h"] < 95.0) | (df["ROC_9_1h"] < 20.0))
    # 4h up move, 1h & 4h overbought
    short_entry_logic.append((df["RSI_3_4h"] < 95.0) | (df["ROC_9_1h"] < 30.0) | (df["ROC_9_4h"] < 60.0))
    # 4h up move, 1h still low
    short_entry_logic.append((df["RSI_3_4h"] < 90.0) | (df["AROONU_14_1h"] > 40.0))
    # 4h up move, 1d still low, 4h uptrend
    short_entry_logic.append((df["RSI_3_4h"] < 85.0) | (df["RSI_14_1d"] > 40.0) | (df["ROC_9_4h"] < 20.0))
    # 4h up move, 4h still low
    short_entry_logic.append((df["RSI_3_4h"] < 80.0) | (df["STOCHRSIk_14_14_3_3_4h"] > 50.0))
    # 4h up move, 1h low
    short_entry_logic.append((df["RSI_3_4h"] < 70.0) | (df["AROONU_14_1h"] > 25.0))
    # 4h up move, 1d low
    short_entry_logic.append((df["RSI_3_4h"] < 70.0) | (df["AROONU_14_1d"] > 20.0))
    # 4h up move, 1h low
    short_entry_logic.append((df["RSI_3_4h"] < 70.0) | (df["STOCHRSIk_14_14_3_3_1h"] > 20.0))
    # 4h up move, 1d low
    short_entry_logic.append((df["RSI_3_4h"] < 70.0) | (df["STOCHRSIk_14_14_3_3_1d"] > 20.0))
    # 1d up move, 1h & 4h still not low enough
    short_entry_logic.append(
      (df["RSI_3_1d"] < 90.0) | (df["STOCHRSIk_14_14_3_3_1h"] > 80.0) | (df["STOCHRSIk_14_14_3_3_4h"] > 50.0)
    )
    # 4h still not high enough, 4h overbought, 4h uptrend
    short_entry_logic.append(
      (df["RSI_14_4h"] > 80.0) | (df["ROC_9_4h"] < 40.0) | (df["CCI_20_change_pct_4h"] < 0.0)
    )
    # 15m & 1h uptrend, 4h still low
    short_entry_logic.append(
      (df["CMF_20_15m"] < 0.30) | (df["CMF_20_1h"] < 0.30) | (df["STOCHRSIk_14_14_3_3_4h"] > 60.0)
    )
    # 15m uptrend, 1h low
    short_entry_logic.append((df["AROONU_14_15m"] < 100.0) | (df["STOCHRSIk_14_14_3_3_1h"] > 20.0))
    # 1h & 4h uptrend
    short_entry_logic.append((df["AROONU_14_1h"] < 100.0) | (df["AROONU_14_4h"] < 100.0))
    # 1h uptrend, 4h uptrend
    short_entry_logic.append((df["AROONU_14_1h"] < 100.0) | (df["ROC_9_4h"] < 20.0))
    # 4h uptrend, 1d uptrend
    short_entry_logic.append((df["AROONU_14_4h"] < 100.0) | (df["AROONU_14_1d"] < 100.0))
    # 4h uptrend, 15m uptrend
    short_entry_logic.append((df["AROONU_14_4h"] < 100.0) | (df["ROC_9_15m"] < 10.0))
    # 4h uptrend, 1h uptrend
    short_entry_logic.append((df["AROONU_14_4h"] < 100.0) | (df["ROC_9_1h"] < 20.0))
    # 1d uptrend, 15m uptrend
    short_entry_logic.append((df["AROONU_14_1d"] < 100.0) | (df["ROC_9_15m"] < 20.0))
    # 1d uptrend, 1h uptrend
    short_entry_logic.append((df["AROONU_14_1d"] < 100.0) | (df["ROC_9_1h"] < 20.0))
    # 15m still not high enough, 1h & 4h overbought
    short_entry_logic.append(
      (df["STOCHRSIk_14_14_3_3_15m"] > 70.0) | (df["ROC_9_1h"] < 30.0) | (df["ROC_9_4h"] < 60.0)
    )
    # 1h & 4h overbought, 1h uptrend
    short_entry_logic.append(
      (df["ROC_9_1h"] < 10.0) | (df["ROC_9_4h"] < 40.0) | (df["CCI_20_change_pct_1h"] < 0.0)
    )
    # 1h & 4h overbought, 4h uptrend
    short_entry_logic.append(
      (df["ROC_9_1h"] < 10.0) | (df["ROC_9_4h"] < 40.0) | (df["CCI_20_change_pct_4h"] < 0.0)
    )
    # 1h & 4h & 1d uptrend
    short_entry_logic.append((df["ROC_9_1h"] < 10.0) | (df["ROC_9_4h"] < 10.0) | (df["ROC_9_1d"] < 20.0))
    # 5m green, 15m still not high enough
    short_entry_logic.append((df["change_pct"] < 5.0) | (df["AROOND_14_15m"] < 50.0))
    # 5m green, 15m still not high enough
    short_entry_logic.append((df["change_pct"] < 5.0) | (df["STOCHRSIk_14_14_3_3_15m"] > 90.0))
    # pump in the last half hour, 1h low
    short_entry_logic.append((df["close"] < (df["close_min_6"] * 1.20)) | (df["AROONU_14_1h"] > 30.0))
    # pump in the last half hour, 15m still low
    short_entry_logic.append((df["close"] < (df["close_min_6"] * 1.20)) | (df["STOCHRSIk_14_14_3_3_15m"] > 40.0))
    # pump in the last half hour, 1d uptrend
    short_entry_logic.append((df["close"] < (df["close_min_6"] * 1.20)) | (df["ROC_9_1d"] < 20.0))
    # big pump in the last 4 hours, 15m still low
    short_entry_logic.append((df["close"] < (df["close_min_48"] * 1.50)) | (df["AROONU_14_15m"] > 50.0))

    # Logic
    short_entry_logic.append(df["EMA_12"] > df["EMA_26"])
    short_entry_logic.append((df["EMA_12"] - df["EMA_26"]) > (df["open"] * 0.030))
    short_entry_logic.append((df["EMA_12"].shift() - df["EMA_26"].shift()) > (df["open"] / 100.0))
    short_entry_logic.append(df["close"] > (df["BBU_20_2.0"] * 1.004))

def append_short_502(df, short_entry_logic, allowed_empty_candles_288) -> None:
    """Append NFI short condition #502, the normal-mode short entry."""
    # Protections
    short_entry_logic.append(df["num_empty_288"] <= allowed_empty_candles_288)
    short_entry_logic.append(df["protections_short_global"] == True)

    # 5m & 15m & 1h & 4h up move
    short_entry_logic.append(
      (df["RSI_3"] < 97.0) | (df["RSI_3_15m"] < 90.0) | (df["RSI_3_1h"] < 90.0) | (df["RSI_3_4h"] < 80.0)
    )
    # 5m & 4h up move
    short_entry_logic.append((df["RSI_3"] < 97.0) | (df["RSI_3_4h"] < 95.0))
    # 5m up move, 4h still not high enough
    short_entry_logic.append((df["RSI_3"] < 97.0) | (df["STOCHRSIk_14_14_3_3_4h"] > 80.0))
    # 5m & 15m strong up move
    short_entry_logic.append((df["RSI_3"] < 95.0) | (df["RSI_3_15m"] < 95.0))
    # 5m & 15m up move, 4h low
    short_entry_logic.append((df["RSI_3"] < 95.0) | (df["RSI_3_15m"] < 90.0) | (df["AROONU_14_4h"] > 30.0))
    # 5m & 1h & 4h up move
    short_entry_logic.append((df["RSI_3"] < 95.0) | (df["RSI_3_1h"] < 90.0) | (df["RSI_3_4h"] < 90.0))
    # 5m & 1h up move, 15m still not high enough
    short_entry_logic.append(
      (df["RSI_3"] < 95.0) | (df["RSI_3_1h"] < 85.0) | (df["STOCHRSIk_14_14_3_3_15m"] > 70.0)
    )
    # 5m up move, 15m still low
    short_entry_logic.append((df["RSI_3"] < 95.0) | (df["STOCHRSIk_14_14_3_3_15m"] > 50.0))
    # 5m up move, 4h low
    short_entry_logic.append((df["RSI_3"] < 90.0) | (df["AROONU_14_4h"] > 20.0))
    # 15m & 1h down move, 4h still not high enough
    short_entry_logic.append(
      (df["RSI_3_15m"] < 97.0) | (df["RSI_3_1h"] < 85.0) | (df["STOCHRSIk_14_14_3_3_4h"] > 80.0)
    )
    # 15m up move, 1h still low
    short_entry_logic.append((df["RSI_3_15m"] < 97.0) | (df["STOCHRSIk_14_14_3_3_1h"] > 60.0))
    # 15m & 1h & 4h up move
    short_entry_logic.append((df["RSI_3_15m"] < 95.0) | (df["RSI_3_1h"] < 90.0) | (df["RSI_3_4h"] < 85.0))
    # 15m & 1h up move, 4h still low
    short_entry_logic.append(
      (df["RSI_3_15m"] < 95.0) | (df["RSI_3_1h"] < 85.0) | (df["STOCHRSIk_14_14_3_3_4h"] > 60.0)
    )
    # 15m up move, 1h still low
    short_entry_logic.append((df["RSI_3_15m"] < 95.0) | (df["STOCHRSIk_14_14_3_3_1h"] > 40.0))
    # 15m up move, 4h still not high enough
    short_entry_logic.append((df["RSI_3_15m"] < 95.0) | (df["AROONU_14_4h"] > 70.0))
    # 15m & 1h & 4h up move
    short_entry_logic.append((df["RSI_3_15m"] < 90.0) | (df["RSI_3_1h"] < 90.0) | (df["RSI_3_4h"] < 90.0))
    # 15m & 1h up move, 15m still not high enough
    short_entry_logic.append(
      (df["RSI_3_15m"] < 90.0) | (df["RSI_3_1h"] < 90.0) | (df["STOCHRSIk_14_14_3_3_15m"] > 80.0)
    )
    # 15m & 1h up move, 1d low
    short_entry_logic.append(
      (df["RSI_3_15m"] < 90.0) | (df["RSI_3_1h"] < 90.0) | (df["STOCHRSIk_14_14_3_3_1d"] > 40.0)
    )
    # 15m & 1h up move, 1h still not high enough
    short_entry_logic.append(
      (df["RSI_3_15m"] < 90.0) | (df["RSI_3_1h"] < 85.0) | (df["STOCHRSIk_14_14_3_3_1h"] > 80.0)
    )
    # 15m & 1h up move, 4h stil low
    short_entry_logic.append((df["RSI_3_15m"] < 90.0) | (df["RSI_3_1h"] < 80.0) | (df["AROONU_14_4h"] > 50.0))
    # 15m & 4h up move, 1d low
    short_entry_logic.append((df["RSI_3_15m"] < 90.0) | (df["RSI_3_4h"] < 85.0) | (df["RSI_14_1d"] > 40.0))
    # 15m & 4h up move, 1d low
    short_entry_logic.append(
      (df["RSI_3_15m"] < 90.0) | (df["RSI_3_4h"] < 85.0) | (df["STOCHRSIk_14_14_3_3_1d"] > 30.0)
    )
    # 15m up move, 1h still low, 1d low
    short_entry_logic.append(
      (df["RSI_3_15m"] < 90.0) | (df["AROONU_14_1h"] > 50.0) | (df["AROONU_14_1d"] > 30.0)
    )
    # 15m up move, 1h high
    short_entry_logic.append((df["RSI_3_15m"] < 90.0) | (df["AROONU_14_1h"] < 100.0))
    # 15m up move, 1h still low
    short_entry_logic.append((df["RSI_3_15m"] < 90.0) | (df["STOCHRSIk_14_14_3_3_1h"] > 50.0))
    # 15m up move, 4h uptrend
    short_entry_logic.append((df["RSI_3_15m"] < 90.0) | (df["ROC_9_4h"] < 20.0))
    # 15m & 1h up move, 1h still low
    short_entry_logic.append(
      (df["RSI_3_15m"] < 85.0) | (df["RSI_3_1h"] < 65.0) | (df["STOCHRSIk_14_14_3_3_1h"] > 60.0)
    )
    # 15m up move, 1h low
    short_entry_logic.append((df["RSI_3_15m"] < 85.0) | (df["STOCHRSIk_14_14_3_3_1h"] > 30.0))
    # 15m & 4h up move, 15m still low
    short_entry_logic.append((df["RSI_3_15m"] < 80.0) | (df["RSI_3_4h"] < 75.0) | (df["AROONU_14_15m"] > 50.0))
    # 15m up move, 1h low
    short_entry_logic.append((df["RSI_3_15m"] < 80.0) | (df["AROONU_14_1h"] > 10.0))
    # 15m up move, 1h low, 1d uptrend
    short_entry_logic.append((df["RSI_3_15m"] < 80.0) | (df["AROONU_14_1h"] > 40.0) | (df["ROC_9_1d"] < 100.0))
    # 15m up move, 4h low
    short_entry_logic.append((df["RSI_3_15m"] < 80.0) | (df["STOCHRSIk_14_14_3_3_4h"] > 40.0))
    # 15m up move, 1h uptrend
    short_entry_logic.append((df["RSI_3_15m"] < 75.0) | (df["ROC_9_1h"] < 40.0))
    # 1h & 1d strong up move
    short_entry_logic.append((df["RSI_3_1h"] < 95.0) | (df["RSI_3_1d"] < 95.0))
    # 1h up move, 1h still not high enough
    short_entry_logic.append((df["RSI_3_1h"] < 95.0) | (df["STOCHRSIk_14_14_3_3_1h"] > 70.0))
    # 1h up move, 4h still low, 1h moving higher
    short_entry_logic.append(
      (df["RSI_3_1h"] < 95.0) | (df["STOCHRSIk_14_14_3_3_4h"] > 60.0) | (df["CCI_20_change_pct_1h"] < -0.0)
    )
    # 1h up move, 1d low
    short_entry_logic.append((df["RSI_3_1h"] < 95.0) | (df["RSI_14_1d"] > 40.0))
    # 1h strong up move, 15m still move higher
    short_entry_logic.append((df["RSI_3_1h"] < 95.0) | (df["CCI_20_change_pct_15m"] < -0.0))
    # 1h up move, relative stable before the hour
    short_entry_logic.append((df["RSI_3_1h"] < 95.0) | (df["close_min_12"] > (df["close_min_48"] * 1.10)))
    # 1h up move, 15m uptrend
    short_entry_logic.append((df["RSI_3_1h"] < 90.0) | (df["AROONU_14_15m"] < 100.0))
    # 1h up move, 1d low
    short_entry_logic.append((df["RSI_3_1h"] < 90.0) | (df["STOCHRSIk_14_14_3_3_1d"] > 10.0))
    # 1h up move, 1h & 4h uptrend
    short_entry_logic.append((df["RSI_3_1h"] < 90.0) | (df["ROC_9_1h"] < 30.0) | (df["ROC_9_4h"] < 30.0))
    # 1h up move, 4h uptrend
    short_entry_logic.append((df["RSI_3_1h"] < 90.0) | (df["ROC_9_4h"] < 20.0))
    # 1h up move, 4h still low
    short_entry_logic.append((df["RSI_3_1h"] < 85.0) | (df["AROONU_14_4h"] > 50.0))
    # 1h & 4h up move, 1d low
    short_entry_logic.append(
      (df["RSI_3_1h"] < 80.0) | (df["RSI_3_4h"] < 80.0) | (df["STOCHRSIk_14_14_3_3_1d"] > 30.0)
    )
    # 1h up move, 1h still not high enough
    short_entry_logic.append((df["RSI_3_1h"] < 80.0) | (df["STOCHRSIk_14_14_3_3_1h"] > 70.0))
    # 1h up move, 4h still low, 1h still moving higher
    short_entry_logic.append(
      (df["RSI_3_1h"] < 80.0) | (df["RSI_14_4h"] > 60.0) | (df["CCI_20_change_pct_1h"] < -0.0)
    )
    # 1h up move, 4h low
    short_entry_logic.append((df["RSI_3_1h"] < 80.0) | (df["STOCHRSIk_14_14_3_3_4h"] > 20.0))
    # 1h up move, 4h low
    short_entry_logic.append((df["RSI_3_1h"] < 80.0) | (df["AROONU_14_4h"] > 10.0))
    # 1h up move, 1h still low
    short_entry_logic.append((df["RSI_3_1h"] < 75.0) | (df["STOCHRSIk_14_14_3_3_1h"] > 50.0))
    # 1h up move, 4h low
    short_entry_logic.append((df["RSI_3_1h"] < 70.0) | (df["RSI_14_4h"] > 40.0))
    # 1h up move, 4h low
    short_entry_logic.append((df["RSI_3_1h"] < 70.0) | (df["STOCHRSIk_14_14_3_3_4h"] > 40.0))
    # 1h up move, 1h uptrend
    short_entry_logic.append((df["RSI_3_1h"] < 70.0) | (df["ROC_9_1h"] < 40.0))
    # 1h up move, 1h low
    short_entry_logic.append((df["RSI_3_1h"] < 60.0) | (df["STOCHRSIk_14_14_3_3_1h"] > 20.0))
    # 4h up move, 1d still low
    short_entry_logic.append((df["RSI_3_4h"] < 97.0) | (df["RSI_14_1d"] > 50.0))
    # 4h up move, 1h still not high enough
    short_entry_logic.append((df["RSI_3_4h"] < 95.0) | (df["STOCHRSIk_14_14_3_3_1h"] > 70.0))
    # 4h up move, 4h still not high enough
    short_entry_logic.append((df["RSI_3_4h"] < 95.0) | (df["STOCHRSIk_14_14_3_3_4h"] > 80.0))
    # 4h up move, 15m still not high enough, 4h moving higher
    short_entry_logic.append(
      (df["RSI_3_4h"] < 90.0) | (df["STOCHRSIk_14_14_3_3_15m"] > 80.0) | (df["CCI_20_change_pct_4h"] < 0.0)
    )
    # 4h up move, 15m still low
    short_entry_logic.append((df["RSI_3_4h"] < 90.0) | (df["STOCHRSIk_14_14_3_3_15m"] > 50.0))
    # 4h up move, 1h still low
    short_entry_logic.append((df["RSI_3_4h"] < 90.0) | (df["AROONU_14_1h"] > 40.0))
    # 4h up move, 4h still not high enough
    short_entry_logic.append((df["RSI_3_4h"] < 90.0) | (df["STOCHRSIk_14_14_3_3_4h"] > 75.0))
    # 4h up move, 4h still not high enough
    short_entry_logic.append((df["RSI_3_4h"] < 85.0) | (df["STOCHRSIk_14_14_3_3_4h"] > 70.0))
    # 4h up move, 1d still low, 4h uptrend
    short_entry_logic.append((df["RSI_3_4h"] < 85.0) | (df["RSI_14_1d"] > 50.0) | (df["ROC_9_4h"] < 20.0))
    # 4h up move, 4h uptrend
    short_entry_logic.append((df["RSI_3_4h"] < 80.0) | (df["ROC_9_4h"] < 20.0))
    # 4h up move, 1h low
    short_entry_logic.append((df["RSI_3_4h"] < 75.0) | (df["STOCHRSIk_14_14_3_3_1h"] > 20.0))
    # 4h up move, 4h low
    short_entry_logic.append((df["RSI_3_4h"] < 70.0) | (df["STOCHRSIk_14_14_3_3_4h"] > 40.0))
    # 1d up move, 1h still not high enough
    short_entry_logic.append((df["RSI_3_1d"] < 95.0) | (df["STOCHRSIk_14_14_3_3_1h"] > 90.0))
    # 1d up move, 1h still low
    short_entry_logic.append((df["RSI_3_1d"] < 90.0) | (df["STOCHRSIk_14_14_3_3_1h"] > 50.0))
    # 1d up move, 4h still low
    short_entry_logic.append((df["RSI_3_1d"] < 80.0) | (df["STOCHRSIk_14_14_3_3_4h"] > 40.0))
    # 15m low, 1h still low
    short_entry_logic.append((df["AROONU_14_15m"] > 20.0) | (df["STOCHRSIk_14_14_3_3_1h"] > 50.0))
    # 15m low, 4h low
    short_entry_logic.append((df["AROONU_14_15m"] > 20.0) | (df["STOCHRSIk_14_14_3_3_4h"] > 20.0))
    # 15m still low, 1h low
    short_entry_logic.append((df["AROONU_14_15m"] > 50.0) | (df["STOCHRSIk_14_14_3_3_1h"] > 30.0))
    # 15m still not high enough, 4h low
    short_entry_logic.append((df["STOCHRSIk_14_14_3_3_15m"] > 70.0) | (df["AROONU_14_4h"] > 10.0))
    # 1h & 4h low
    short_entry_logic.append((df["AROONU_14_1h"] > 20.0) | (df["AROONU_14_4h"] > 20.0))
    # 1h & 4h low
    short_entry_logic.append((df["AROONU_14_1h"] > 20.0) | (df["STOCHRSIk_14_14_3_3_4h"] > 20.0))
    # 1h low, 1d low
    short_entry_logic.append((df["AROONU_14_1h"] > 30.0) | (df["STOCHRSIk_14_14_3_3_1d"] > 30.0))
    # 4h still not high enough, 4h & 1d uptrend
    short_entry_logic.append((df["AROONU_14_4h"] > 70.0) | (df["ROC_9_4h"] < 60.0) | (df["ROC_9_1d"] < 200.0))
    # 1h & 4h low
    short_entry_logic.append((df["STOCHRSIk_14_14_3_3_1h"] > 20.0) | (df["AROONU_14_4h"] > 20.0))
    # 1d big green, 1d still not high enough
    short_entry_logic.append((df["change_pct_1d"] < 30.0) | (df["RSI_14_1d"] > 65.0))
    # rise in the last hour, relatively stable before the hour
    short_entry_logic.append(
      (df["close"] < (df["close_min_12"] * 1.10)) | (df["close_min_12"] > (df["close_min_48"] * 1.10))
    )
    # big pump in the last 6 days, 4h still not high enough
    short_entry_logic.append((df["close"] < (df["low_min_6_1d"] * 4.0)) | (df["STOCHRSIk_14_14_3_3_4h"] > 80.0))
    # big pump in the last 20 days, 1h up move
    short_entry_logic.append((df["close"] < (df["low_min_20_1d"] * 6.0)) | (df["RSI_3_1h"] < 90.0))

    # Logic
    short_entry_logic.append(df["AROOND_14"] < 25.0)
    short_entry_logic.append(df["STOCHRSIk_14_14_3_3"] > 80.0)
    short_entry_logic.append(df["close"] > (df["EMA_20"] * 1.060))
    short_entry_logic.append(df["close"] > (df["BBU_20_2.0"] * 0.995))
    short_entry_logic.append(df["AROOND_14_15m"] < 25.0)


def append_short_503(df, short_entry_logic, allowed_empty_candles_288) -> None:
    """Append NFI short condition #503, the normal-mode short entry."""
    # Protections
    short_entry_logic.append(df["num_empty_288"] <= allowed_empty_candles_288)

    short_entry_logic.append(df["RSI_3_1h"] >= 5.0)
    short_entry_logic.append(df["RSI_3_4h"] >= 20.0)
    short_entry_logic.append(df["RSI_3_1d"] >= 20.0)
    short_entry_logic.append(df["RSI_14_1h"] > 20.0)
    short_entry_logic.append(df["RSI_14_4h"] > 20.0)
    short_entry_logic.append(df["RSI_14_1d"] > 10.0)
    # 5m strong down move
    short_entry_logic.append((df["RSI_3"] < 98.0) | (df["ROC_9"] < 50.0))
    # 5m down move, 4h still high
    short_entry_logic.append(
      (df["RSI_3"] < 90.0) | (df["MFI_14"] > 10.0) | (df["STOCHRSIk_14_14_3_3_4h"] > 30.0)
    )
    # 5m & 1h down move, 1h still high
    short_entry_logic.append(
      (df["RSI_3"] < 90.0) | (df["RSI_3_1h"] < 90.0) | (df["STOCHRSIk_14_14_3_3_1h"] > 70.0)
    )
    # 5m down move, 4h downtrend, 1h still high
    short_entry_logic.append(
      (df["RSI_3"] < 95.0) | (df["RSI_3_4h"] < 85.0) | (df["STOCHRSIk_14_14_3_3_1h"] > 30.0)
    )
    # 5m & 4h strong down move, 4h still not low enough
    short_entry_logic.append(
      (df["RSI_3"] < 95.0) | (df["RSI_3_1h"] < 95.0) | (df["STOCHRSIk_14_14_3_3_4h"] > 60.0)
    )
    # 5m down move, 1h high, 1d overbought
    short_entry_logic.append((df["RSI_3"] < 90.0) | (df["ROC_9_1h"] < 15.0) | (df["ROC_9_1d"] > -40.0))
    # 5m down move, 1h & 4h high
    short_entry_logic.append(
      (df["RSI_3"] < 90.0) | (df["UO_7_14_28_1h"] > 40.0) | (df["STOCHRSIk_14_14_3_3_4h"] > 30.0)
    )
    # 5m down move, 1h high, 4h downtrend
    short_entry_logic.append(
      (df["RSI_3"] < 98.0) | (df["STOCHRSIk_14_14_3_3_1h"] > 10.0) | (df["ROC_9_4h"] < 10.0)
    )
    # 5m & 1h down move, 4h down
    short_entry_logic.append((df["RSI_3"] < 90.0) | (df["RSI_3_1h"] < 85.0) | (df["CMF_20_4h"] > -0.2))
    # 5m down move, 1h high
    short_entry_logic.append((df["RSI_14_change_pct"] < 40.0) | (df["STOCHRSIk_14_14_3_3_1h"] > 30.0))
    # 5m down move, 1h high
    short_entry_logic.append((df["RSI_14_change_pct"] < 40.0) | (df["STOCHRSIk_14_14_3_3_4h"] > 30.0))
    # 15m & 1h down move, 4h still high
    short_entry_logic.append(
      (df["RSI_3_15m"] < 95.0) | (df["RSI_3_1h"] < 85.0) | (df["STOCHRSIk_14_14_3_3_4h"] > 50.0)
    )
    # 15m down move, 15m still not low enough, 1h & 4h still not low enough
    short_entry_logic.append(
      (df["RSI_3_15m"] < 95.0)
      | (df["AROOND_14_15m"] < 25.0)
      | (df["STOCHRSIk_14_14_3_3_1h"] > 75.0)
      | (df["MFI_14_4h"] > 50.0)
    )
    # 5m & 1h down move, 1h still high
    short_entry_logic.append(
      (df["RSI_3_15m"] < 95.0) | (df["RSI_3_1h"] < 85.0) | (df["STOCHRSIk_14_14_3_3_1h"] > 50.0)
    )
    # 15m & 4h down move, 1h still not low
    short_entry_logic.append(
      (df["RSI_3_15m"] < 95.0) | (df["RSI_3_4h"] < 90.0) | (df["STOCHRSIk_14_14_3_3_1h"] > 70.0)
    )
    # 15m & 4h down move, 4h still not low enough
    short_entry_logic.append(
      (df["RSI_3_15m"] < 95.0) | (df["RSI_3_4h"] < 80.0) | (df["STOCHRSIk_14_14_3_3_4h"] > 60.0)
    )
    # 15m down move, 1h & 4h still high
    short_entry_logic.append(
      (df["RSI_3_15m"] < 95.0) | (df["STOCHRSIk_14_14_3_3_1h"] > 50.0) | (df["RSI_14_4h"] > 50.0)
    )
    # 15m & 1h & 4h down move
    short_entry_logic.append(
      (df["RSI_3_15m"] < 90.0) | (df["RSI_3_change_pct_1h"] > -60.0) | (df["RSI_3_change_pct_4h"] > -40.0)
    )
    # 15m down move, 1d downtrend, 1h still high
    short_entry_logic.append(
      (df["RSI_3_15m"] < 90.0) | (df["ROC_9_1d"] > -25.0) | (df["STOCHRSIk_14_14_3_3_1h"] > 30.0)
    )
    # 15m & 1d down move, 1h still high
    short_entry_logic.append(
      (df["RSI_3_15m"] < 90.0) | (df["RSI_3_1d"] < 90.0) | (df["STOCHRSIk_14_14_3_3_1h"] > 30.0)
    )
    # 15m & 4h down move, 1h still high
    short_entry_logic.append(
      (df["RSI_3_15m"] < 90.0) | (df["RSI_3_4h"] < 95.0) | (df["STOCHRSIk_14_14_3_3_1h"] > 50.0)
    )
    # 15m down move, 15m still not low enough, 4h down move
    short_entry_logic.append((df["RSI_3_15m"] < 90.0) | (df["AROOND_14_15m"] < 50.0) | (df["RSI_3_4h"] < 85.0))
    # 15m down move, 1h still high, 1d strong downtrend
    short_entry_logic.append((df["RSI_3_15m"] < 80.0) | (df["AROOND_14_1h"] < 25.0) | (df["MFI_14_1d"] < 90.0))
    # 15m down move, 1h still high, 1d downtrend
    short_entry_logic.append(
      (df["RSI_3_15m"] < 85.0) | (df["STOCHRSIk_14_14_3_3_1h"] > 30.0) | (df["ROC_9_1d"] < 50.0)
    )
    # 15m down move, 4h still high, 1d downtrend
    short_entry_logic.append(
      (df["RSI_3_15m"] < 85.0) | (df["STOCHRSIk_14_14_3_3_4h"] > 30.0) | (df["ROC_9_1d"] < 50.0)
    )
    # 15m & 4h down move, 1d downtrend
    short_entry_logic.append((df["RSI_3_15m"] < 85.0) | (df["RSI_3_4h"] < 85.0) | (df["ROC_9_1d"] > -70.0))
    # 15m down move, 15m not low enough, 1h overbought
    short_entry_logic.append(
      (df["RSI_14_change_pct_15m"] > -40.0) | (df["STOCHRSIk_14_14_3_3_15m"] > 90.0) | (df["RSI_14_1h"] > 30.0)
    )
    # 15m strong down move, 1h still high
    short_entry_logic.append((df["ROC_9_15m"] < 15.0) | (df["STOCHRSIk_14_14_3_3_1h"] > 50.0))
    # 15m downtrend, 1h & 4h still high
    short_entry_logic.append(
      (df["ROC_9_15m"] < 10.0) | (df["STOCHRSIk_14_14_3_3_1h"] > 50.0) | (df["STOCHRSIk_14_14_3_3_4h"] > 50.0)
    )
    # 15m & 1h & 4h down move
    short_entry_logic.append(
      (df["RSI_3_15m"] < 95.0) | (df["RSI_3_1h"] < 95.0) | (df["CCI_20_change_pct_4h"] < 0.0)
    )
    # 15m strong down move
    short_entry_logic.append((df["RSI_3_15m"] < 90.0) | (df["MFI_14_15m"] < 85.0) | (df["AROOND_14_15m"] < 25.0))
    # 14m down move, 4h still high
    short_entry_logic.append(
      (df["RSI_3_15m"] < 80.0) | (df["AROOND_14_15m"] < 50.0) | (df["UO_7_14_28_4h"] > 50.0)
    )
    # 15m down move, 1h stil high, 1d overbought
    short_entry_logic.append((df["RSI_3_15m"] < 85.0) | (df["AROOND_14_1h"] < 25.0) | (df["ROC_9_1d"] > -80.0))
    # 15m down move, 1h high, 1d overbought
    short_entry_logic.append(
      (df["RSI_3_15m"] < 90.0) | (df["STOCHRSIk_14_14_3_3_1h"] > 30.0) | (df["ROC_9_1d"] > -50.0)
    )
    # 1h & 4h down move, 4h still high
    short_entry_logic.append(
      (df["RSI_3_1h"] < 90.0) | (df["RSI_3_change_pct_4h"] < 65.0) | (df["STOCHRSIk_14_14_3_3_4h"] > 50.0)
    )
    # 1h & 4h down move, 4h still high
    short_entry_logic.append(
      (df["RSI_3_1h"] < 90.0) | (df["RSI_3_4h"] < 85.0) | (df["STOCHRSIk_14_14_3_3_4h"] < 10.0)
    )
    # 1h down move, 4h still not low enough, 1d overbought
    short_entry_logic.append((df["RSI_3_1h"] < 90.0) | (df["AROOND_14_4h"] < 25.0) | (df["ROC_9_1d"] > -120.0))
    # 1h down move, 1h still not low enough, 4h still not low
    short_entry_logic.append(
      (df["RSI_3_1h"] < 90.0) | (df["STOCHRSIk_14_14_3_3_1h"] > 70.0) | (df["RSI_14_4h"] > 50.0)
    )
    # 1h down move, 4h still high
    short_entry_logic.append((df["RSI_3_1h"] < 95.0) | (df["RSI_14_4h"] > 60.0))
    # 1h down move, 4h still high, 1d downtrend
    short_entry_logic.append(
      (df["RSI_3_1h"] < 80.0) | (df["STOCHRSIk_14_14_3_3_4h"] > 30.0) | (df["ROC_9_1d"] < 50.0)
    )
    # 1h down move, 4h still high, 1d downtrend
    short_entry_logic.append(
      (df["RSI_3_change_pct_1h"] > -65.0) | (df["STOCHRSIk_14_14_3_3_4h"] > 30.0) | (df["ROC_9_1d"] < 50.0)
    )
    # 4h & 1d down move, 1h still high
    short_entry_logic.append(
      (df["RSI_3_4h"] < 90.0) | (df["ROC_2_1d"] < 20.0) | (df["STOCHRSIk_14_14_3_3_1h"] > 50.0)
    )
    # 15m still high, 1h down move, 4h high
    short_entry_logic.append(
      (df["AROOND_14_15m"] < 50.0) | (df["RSI_3_change_pct_1h"] < 50.0) | (df["STOCHRSIk_14_14_3_3_4h"] > 30.0)
    )
    # 15m still high, 1h & 4h down move, 4h still high
    short_entry_logic.append(
      (df["AROOND_14_15m"] < 50.0)
      | (df["RSI_3_1h"] < 85.0)
      | (df["RSI_3_4h"] < 80.0)
      | (df["STOCHRSIk_14_14_3_3_4h"] > 80.0)
    )
    # 15m & 1h still high, 4h overbought
    short_entry_logic.append(
      (df["AROOND_14_15m"] < 50.0) | (df["AROOND_14_1h"] < 50.0) | (df["ROC_9_4h"] > -40.0)
    )
    # 15m still high, 1h down move, 1d downtrend
    short_entry_logic.append(
      (df["STOCHRSIk_14_14_3_3_15m"] > 30.0) | (df["RSI_3_4h"] < 90.0) | (df["ROC_9_1d"] < 50.0)
    )
    # 1h & 4h still high, 1d strong down move
    short_entry_logic.append(
      (df["STOCHRSIk_14_14_3_3_1h"] > 50.0) | (df["UO_7_14_28_4h"] > 55.0) | (df["RSI_3_1d"] < 90.0)
    )
    # 1h still high, 4h & 1d downtrend
    short_entry_logic.append((df["AROOND_14_1h"] < 25.0) | (df["ROC_9_4h"] < 20.0) | (df["ROC_9_1d"] < 50.0))
    # 4h moving down, 1d P&D
    short_entry_logic.append(
      (df["ROC_9_4h"] < 30.0) | (df["RSI_3_change_pct_1d"] < 50.0) | (df["ROC_9_1d"] > -50.0)
    )
    # 1d strong downtrend, 4h still high
    short_entry_logic.append(
      (df["ROC_2_1d"] < 20.0) | (df["ROC_9_1d"] < 50.0) | (df["STOCHRSIk_14_14_3_3_4h"] > 70.0)
    )
    # 1d P&D, 1d overbought
    short_entry_logic.append(
      (df["ROC_2_1d"] < 10.0) | (df["ROC_9_1d"] > -50.0) | (df["STOCHRSIk_14_14_3_3_1h"] > 5.0)
    )
    # 1h red, previous 1h green, 1h overbought
    short_entry_logic.append(
      (df["change_pct_1h"] < 1.0) | (df["change_pct_1h"].shift(12) > -5.0) | (df["RSI_14_1h"].shift(12) < 80.0)
    )
    # 1h red, 1h stil high, 4h downtrend
    short_entry_logic.append(
      (df["change_pct_1h"] < 5.0) | (df["STOCHRSIk_14_14_3_3_1h"] > 50.0) | (df["ROC_9_4h"] > -25.0)
    )
    # 4h red, 15m down move, 4h still high
    short_entry_logic.append(
      (df["change_pct_4h"] < 5.0) | (df["RSI_3_15m"] < 90.0) | (df["STOCHRSIk_14_14_3_3_4h"] > 30.0)
    )
    # 4h red, previous 4h green, 4h overbought
    short_entry_logic.append(
      (df["change_pct_4h"] < 5.0) | (df["change_pct_4h"].shift(48) > -5.0) | (df["ROC_9_4h"].shift(48) > -25.0)
    )
    # 4h red, 4h still not low enough, 1h downtrend, 1h overbought
    short_entry_logic.append(
      (df["change_pct_4h"] < 10.0)
      | (df["AROOND_14_4h"] < 25.0)
      | (df["ROC_9_1h"] < 20.0)
      | (df["ROC_9_1d"] > -40.0)
    )
    # 4h red, 4h still high, 1d downtrend
    short_entry_logic.append(
      (df["change_pct_4h"] < 10.0) | (df["STOCHRSIk_14_14_3_3_4h"] > 30.0) | (df["ROC_9_1d"] < 40.0)
    )
    # 1d P&D, 1d overbought
    short_entry_logic.append(
      (df["change_pct_1d"] < 10.0) | (df["change_pct_1d"].shift(288) > -10.0) | (df["ROC_9_1d"] > -100.0)
    )
    # 1d P&D, 4h still high
    short_entry_logic.append(
      (df["change_pct_1d"] < 15.0) | (df["change_pct_1d"].shift(288) > -15.0) | (df["AROOND_14_4h"] < 50.0)
    )
    short_entry_logic.append(
      (df["RSI_3_1h"] < 90.0) | (df["RSI_3_4h"] < 95.0) | (df["CCI_20_change_pct_4h"] < 0.0)
    )

    # Logic
    short_entry_logic.append(df["RSI_20"] > df["RSI_20"].shift(1))
    short_entry_logic.append(df["RSI_4"] > 54.0)
    short_entry_logic.append(df["AROOND_14"] < 25.0)
    short_entry_logic.append(df["close"] > df["SMA_16"] * 1.058)


def append_short_541(df, short_entry_logic, allowed_empty_candles_288) -> None:
    """Append NFI short condition #541, the quick-mode short entry."""
    # Protections
    short_entry_logic.append(df["num_empty_288"] <= allowed_empty_candles_288)

    # 5m & 15m down move, 4h still high
    short_entry_logic.append(
      (df["RSI_3"] < 95.0) | (df["RSI_3_change_pct_15m"] < 50.0) | (df["RSI_14_4h"] > 50.0)
    )
    # 5m & 15m & 1h down move
    short_entry_logic.append((df["RSI_3"] < 95.0) | (df["RSI_3_15m"] < 95.0) | (df["RSI_3_1h"] < 95.0))
    # 5m strong down move
    short_entry_logic.append((df["RSI_3"] < 98.0) | (df["ROC_9"] < 50.0))
    # 15m & 1h strong down move & downtrend
    short_entry_logic.append((df["RSI_3_15m"] < 95.0) | (df["RSI_3_1h"] < 95.0) | (df["MFI_14_1h"] > 5.0))
    # 15m strong down move, 4h high
    short_entry_logic.append((df["RSI_3_15m"] < 95.0) | (df["STOCHRSIk_14_14_3_3_4h"] > 10.0))
    # 15m & 1h down move
    short_entry_logic.append(
      (df["RSI_3_15m"] < 95.0) | (df["RSI_3_1h"] < 95.0) | (df["CCI_20_change_pct_1h"] > 0.0)
    )
    # 15m & 1h down move, 4h high
    short_entry_logic.append(
      (df["RSI_3_15m"] < 95.0) | (df["RSI_3_1h"] < 85.0) | (df["STOCHRSIk_14_14_3_3_4h"] > 30.0)
    )
    # 15m & 1h down move, 4h still high
    short_entry_logic.append(
      (df["RSI_3_15m"] < 95.0) | (df["RSI_3_change_pct_1h"] < 50.0) | (df["MFI_14_4h"] > 50.0)
    )
    # 15m strong down move, 1h still high
    short_entry_logic.append(
      (df["RSI_3_15m"] < 95.0) | (df["MFI_14_15m"] < 90.0) | (df["STOCHRSIk_14_14_3_3_1h"] > 50.0)
    )
    # 15m & 1h down move, 1h not low enough
    short_entry_logic.append(
      (df["RSI_3_15m"] < 95.0) | (df["RSI_3_1h"] < 95.0) | (df["STOCHRSIk_14_14_3_3_1h"] > 80.0)
    )
    # 15m down move, 1h strong down move
    short_entry_logic.append((df["RSI_3_15m"] < 95.0) | (df["RSI_14_change_pct_1h"] < 70.0))
    # 15m down move, 4h & 1d downtrend
    short_entry_logic.append((df["RSI_3_15m"] < 95.0) | (df["ROC_9_4h"] < 30.0) | (df["ROC_9_1d"] < 50.0))
    # 15m down move, 1h strong down move, 4h stil high
    short_entry_logic.append(
      (df["RSI_3_15m"] < 90.0) | (df["RSI_3_1h"] < 95.0) | (df["STOCHRSIk_14_14_3_3_4h"] > 50.0)
    )
    # 15m down move, 1h & 4h still high
    short_entry_logic.append(
      (df["RSI_3_15m"] < 85.0) | (df["STOCHRSIk_14_14_3_3_1h"] > 50.0) | (df["STOCHRSIk_14_14_3_3_4h"] > 50.0)
    )
    # 15m down move, 1h downtrend, 4h still high
    short_entry_logic.append(
      (df["RSI_3_15m"] < 90.0) | (df["ROC_9_1h"] < 20.0) | (df["STOCHRSIk_14_14_3_3_4h"] > 50.0)
    )
    # 15m & 1h down move, 4h high
    short_entry_logic.append(
      (df["RSI_3_15m"] < 90.0) | (df["RSI_3_1h"] < 85.0) | (df["STOCHRSIk_14_14_3_3_4h"] > 30.0)
    )
    # 15m down move, 1h down move, 4h high
    short_entry_logic.append(
      (df["RSI_3_15m"] < 85.0) | (df["RSI_3_change_pct_1h"] < 30.0) | (df["STOCHRSIk_14_14_3_3_4h"] > 10.0)
    )
    # 1m down move, 1h still dropping, 4h overbought
    short_entry_logic.append(
      (df["RSI_3_15m"] < 90.0) | (df["CCI_20_change_pct_1h"] < 0.0) | (df["RSI_14_4h"] > 20.0)
    )
    # 15m down move, 1h high
    short_entry_logic.append((df["RSI_3_change_pct_15m"] < 70.0) | (df["STOCHRSIk_14_14_3_3_1h"] > 10.0))
    # 1h strong down move, 4h high
    short_entry_logic.append((df["RSI_3_1h"] < 95.0) | (df["STOCHRSIk_14_14_3_3_4h"] > 10.0))
    # 1h down move, 4h downtrend, 4h not low enough
    short_entry_logic.append(
      (df["RSI_3_1h"] < 95.0) | (df["CMF_20_4h"] > -0.25) | (df["STOCHRSIk_14_14_3_3_4h"] > 70.0)
    )
    # 1h down move, 4h high, 1d overbought
    short_entry_logic.append((df["RSI_3_1h"] < 90.0) | (df["RSI_14_4h"] > 40.0) | (df["ROC_9_1d"] > -50.0))
    # 1h down move, 4h strong down move
    short_entry_logic.append((df["RSI_3_1h"] < 95.0) | (df["RSI_14_change_pct_4h"] < 40.0))
    # 1h & 4h down move, 4h still going down
    short_entry_logic.append(
      (df["RSI_3_1h"] < 95.0) | (df["RSI_3_4h"] < 95.0) | (df["CCI_20_change_pct_4h"] < 0.0)
    )
    # 1h & 4h down move, 4h still not low enough
    short_entry_logic.append(
      (df["RSI_3_1h"] < 95.0) | (df["RSI_3_change_pct_4h"] < 65.0) | (df["STOCHRSIk_14_14_3_3_4h"] > 70.0)
    )
    # 1h down move, 4h down move, 4h P&D
    short_entry_logic.append(
      (df["RSI_3_1h"] < 90.0) | (df["RSI_3_change_pct_4h"] < 70.0) | (df["RSI_14_4h"].shift(48) > 30.0)
    )
    # 1h & 4h down move, 4h still not low enough, 1d still high
    short_entry_logic.append(
      (df["RSI_3_1h"] < 90.0)
      | (df["RSI_3_change_pct_4h"] < 50.0)
      | (df["AROOND_14_4h"] < 25.0)
      | (df["STOCHRSIk_14_14_3_3_1d"] > 60.0)
    )
    # 1h down move, 1h still high, 1d going down
    short_entry_logic.append(
      (df["RSI_3_1h"] < 85.0) | (df["STOCHRSIk_14_14_3_3_1h"] > 50.0) | (df["ROC_2_1d"] > -50.0)
    )
    # 4h downtrend, 4h still high, 1d strong downtrend
    short_entry_logic.append(
      (df["RSI_3_4h"] < 85.0) | (df["STOCHRSIk_14_14_3_3_4h"] > 70.0) | (df["ROC_9_1d"] < 60.0)
    )
    # 15m down move, 1h strong down move, 1d overbought
    short_entry_logic.append(
      (df["MFI_14_15m"] < 80.0) | (df["RSI_3_change_pct_1h"] < 80.0) | (df["ROC_9_1d"] > -50.0)
    )
    # 1h not low enough, 4h high, 1d strong downtrend
    short_entry_logic.append(
      (df["STOCHRSIk_14_14_3_3_1h"] > 70.0) | (df["STOCHRSIk_14_14_3_3_4h"] > 10.0) | (df["ROC_9_1d"] < 60.0)
    )
    # 1h down move, 4h still high, 1d downtrend
    short_entry_logic.append(
      (df["RSI_3_change_pct_1h"] < 65.0) | (df["STOCHRSIk_14_14_3_3_4h"] > 30.0) | (df["ROC_9_1d"] < 50.0)
    )
    # 15m strong down move, 1h still high
    short_entry_logic.append((df["ROC_9_15m"] < 15.0) | (df["STOCHRSIk_14_14_3_3_1h"] > 30.0))
    # 15m downtrend, 4h down move, 4h stil high
    short_entry_logic.append(
      (df["ROC_9_15m"] < 15.0) | (df["RSI_3_4h"] < 75.0) | (df["STOCHRSIk_14_14_3_3_4h"] > 30.0)
    )
    # 1h downtrend, 4h overbought
    short_entry_logic.append((df["ROC_2_1h"] < 5.0) | (df["RSI_14_4h"] > 20.0) | (df["ROC_9_4h"] > -25.0))
    # 1h P&D, 4h still high
    short_entry_logic.append(
      (df["ROC_2_1h"] < 10.0) | (df["ROC_9_1h"] > -5.0) | (df["STOCHRSIk_14_14_3_3_4h"] > 30.0)
    )
    # 1h downtrend, 4h down move, 1d downtrend
    short_entry_logic.append((df["ROC_9_1h"] < 40.0) | (df["RSI_3_4h"] < 90.0) | (df["ROC_9_1d"] < 50.0))
    short_entry_logic.append((df["ROC_9_4h"] > -200.0) | (df["RSI_14_4h"] > 20.0))
    # 4h down move, 1d P&D
    short_entry_logic.append((df["ROC_9_4h"] < 20.0) | (df["ROC_2_1d"] < 20.0) | (df["ROC_9_1d"] > -50.0))
    # 1h P&D, 4h overbought
    short_entry_logic.append(
      (df["change_pct_1h"] < 2.0) | (df["change_pct_1h"].shift(12) > 2.0) | (df["RSI_14_4h"] > 20.0)
    )
    # 1h P&D, 1d overbought
    short_entry_logic.append(
      (df["change_pct_1h"] < 5.0) | (df["change_pct_1h"].shift(12) > -5.0) | (df["ROC_9_1d"] > -100.0)
    )
    # 1h & 4h red, 1h not low enough
    short_entry_logic.append(
      (df["change_pct_1h"] < 10.0) | (df["change_pct_4h"] < 10.0) | (df["MFI_14_1h"] > 50.0)
    )
    # 1h red, 1h still not low enough, 1d down move
    short_entry_logic.append((df["change_pct_1h"] < 15.0) | (df["MFI_14_1h"] > 50.0) | (df["RSI_3_1d"] < 90.0))
    # 4h red, previous 4h green, 4h overbought
    short_entry_logic.append(
      (df["change_pct_4h"] < 5.0) | (df["change_pct_4h"].shift(48) > -5.0) | (df["RSI_14_4h"].shift(48) > 20.0)
    )
    # 1d P&D, 1d overbought
    short_entry_logic.append(
      (df["change_pct_1d"] < 10.0) | (df["change_pct_1d"].shift(288) > -10.0) | (df["ROC_9_1d"] > -100.0)
    )
    # 1d P&D, 4h still high
    short_entry_logic.append(
      (df["change_pct_1d"] < 15.0) | (df["change_pct_1d"].shift(288) > -15.0) | (df["AROOND_14_4h"] < 50.0)
    )

    # Logic
    short_entry_logic.append(df["RSI_14"] > 64.0)
    short_entry_logic.append(df["AROOND_14"] < 25.0)
    short_entry_logic.append(df["AROONU_14"] > 75.0)
    short_entry_logic.append(df["EMA_9"] > (df["EMA_26"] * 1.040))


def append_short_542(df, short_entry_logic, allowed_empty_candles_288) -> None:
    """Append NFI short condition #542, the quick-mode short entry."""
    # Protections
    short_entry_logic.append(df["num_empty_288"] <= allowed_empty_candles_288)
    short_entry_logic.append(df["protections_short_global"] == True)

    # 5m & 15m up move, 15m stil low
    short_entry_logic.append((df["RSI_3"] < 90.0) | (df["RSI_3_15m"] < 80.0) | (df["AROONU_14_15m"] > 60.0))
    # 15m & 1h up move, 4h still low
    short_entry_logic.append((df["RSI_3_15m"] < 95.0) | (df["RSI_3_1h"] < 95.0) | (df["RSI_14_4h"] > 60.0))
    # 15m & 1h up move, 4h still not high enough
    short_entry_logic.append(
      (df["RSI_3_15m"] < 95.0) | (df["RSI_3_1h"] < 95.0) | (df["STOCHRSIk_14_14_3_3_4h"] > 80.0)
    )
    # 15m & 1h up move, 1h still moving higher
    short_entry_logic.append(
      (df["RSI_3_15m"] < 95.0) | (df["RSI_3_1h"] < 90.0) | (df["CCI_20_change_pct_1h"] < -0.0)
    )
    # 15m & 4h up move, 4h still moving higher
    short_entry_logic.append(
      (df["RSI_3_15m"] < 90.0) | (df["RSI_3_4h"] < 95.0) | (df["CCI_20_change_pct_4h"] < -0.0)
    )
    # 15m & 1d up move, 4h uptrend
    short_entry_logic.append((df["RSI_3_15m"] < 90.0) | (df["RSI_3_1d"] < 80.0) | (df["ROC_9_4h"] < 20.0))
    # 15m up move, 15m & 4h high
    short_entry_logic.append(
      (df["RSI_3_15m"] < 90.0) | (df["AROONU_14_15m"] < 100.0) | (df["AROONU_14_4h"] < 100.0)
    )
    # 15m up move, 15m still not high enough, 1d uptrend
    short_entry_logic.append(
      (df["RSI_3_15m"] < 90.0) | (df["STOCHRSIk_14_14_3_3_15m"] > 80.0) | (df["ROC_9_1d"] < 80.0)
    )
    # 15m & 4h up move, 15m still not high enough
    short_entry_logic.append(
      (df["RSI_3_15m"] < 85.0) | (df["RSI_3_4h"] < 90.0) | (df["STOCHRSIk_14_14_3_3_15m"] > 70.0)
    )
    # 15m & 4h up move, 1d uptrend
    short_entry_logic.append((df["RSI_3_15m"] < 85.0) | (df["RSI_3_4h"] < 85.0) | (df["ROC_9_1d"] < 50.0))
    # 15m & 4h up move, 4h still not high enough
    short_entry_logic.append((df["RSI_3_15m"] < 85.0) | (df["RSI_3_4h"] < 80.0) | (df["RSI_14_4h"] > 60.0))
    # 15m up move, 15m still not high enough, 4h still low
    short_entry_logic.append(
      (df["RSI_3_15m"] < 85.0) | (df["STOCHRSIk_14_14_3_3_15m"] > 80.0) | (df["AROONU_14_4h"] > 50.0)
    )
    # 15m up move, 4h overbought
    short_entry_logic.append((df["RSI_3_15m"] < 85.0) | (df["ROC_9_4h"] < 50.0))
    # 15m & 1h up move, 15m still low
    short_entry_logic.append((df["RSI_3_15m"] < 70.0) | (df["RSI_3_1h"] < 70.0) | (df["AROONU_14_15m"] > 40.0))
    # 15m & 1h up move, 15m still low
    short_entry_logic.append(
      (df["RSI_3_15m"] < 70.0) | (df["RSI_3_1h"] < 70.0) | (df["STOCHRSIk_14_14_3_3_15m"] > 40.0)
    )
    # # 15m & 1h up move, 4h low
    short_entry_logic.append((df["RSI_3_15m"] < 70.0) | (df["RSI_3_1h"] < 60.0) | (df["AROONU_14_4h"] > 40.0))
    # 1h & 1d up move, 1h still moving higher
    short_entry_logic.append(
      (df["RSI_3_1h"] < 97.0) | (df["RSI_3_1d"] < 95.0) | (df["CCI_20_change_pct_1h"] < -0.0)
    )
    # 1h & 4h up move, 15m still not high enough
    short_entry_logic.append(
      (df["RSI_3_1h"] < 95.0) | (df["RSI_3_4h"] < 95.0) | (df["STOCHRSIk_14_14_3_3_15m"] > 80.0)
    )
    # 1h & 4h up move, 1d uptrend
    short_entry_logic.append((df["RSI_3_1h"] < 95.0) | (df["RSI_3_4h"] < 95.0) | (df["ROC_9_1d"] < 100.0))
    # 1h & 4h up move, 1d still low
    short_entry_logic.append((df["RSI_3_1h"] < 95.0) | (df["RSI_3_4h"] < 85.0) | (df["RSI_14_1d"] > 50.0))
    # 1h up move, 4h still low, 1h still moving higher
    short_entry_logic.append(
      (df["RSI_3_1h"] < 95.0) | (df["RSI_14_4h"] > 60.0) | (df["CCI_20_change_pct_1h"] < -0.0)
    )
    # 1h up move, 4h low
    short_entry_logic.append((df["RSI_3_1h"] < 95.0) | (df["AROONU_14_4h"] > 10.0))
    # 1h & 4h up move, 1h still moving higher
    short_entry_logic.append(
      (df["RSI_3_1h"] < 90.0) | (df["RSI_3_4h"] < 85.0) | (df["CCI_20_change_pct_1h"] < -0.0)
    )
    # 1h & 4h up move, 4h still not high enough
    short_entry_logic.append(
      (df["RSI_3_1h"] < 90.0) | (df["RSI_3_4h"] < 70.0) | (df["STOCHRSIk_14_14_3_3_4h"] > 80.0)
    )
    # 1h & 1d up move, 15m still low
    short_entry_logic.append(
      (df["RSI_3_1h"] < 90.0) | (df["RSI_3_1d"] < 90.0) | (df["STOCHRSIk_14_14_3_3_15m"] > 60.0)
    )
    # 1h up move, 15m high
    short_entry_logic.append((df["RSI_3_1h"] < 90.0) | (df["AROONU_14_15m"] < 100.0))
    # 1h up move, 4h low
    short_entry_logic.append((df["RSI_3_1h"] < 90.0) | (df["STOCHRSIk_14_14_3_3_4h"] > 30.0))
    # 1h up move, 4h still low, 1h still moving higher
    short_entry_logic.append(
      (df["RSI_3_1h"] < 90.0) | (df["STOCHRSIk_14_14_3_3_4h"] > 60.0) | (df["CCI_20_change_pct_1h"] < -0.0)
    )
    # 1h up move, 15m uptrend
    short_entry_logic.append((df["RSI_3_1h"] < 90.0) | (df["ROC_9_15m"] < 30.0))
    # 1h up move, 15m & 4h uptrend
    short_entry_logic.append((df["RSI_3_1h"] < 90.0) | (df["ROC_9_15m"] < 20.0) | (df["ROC_9_4h"] < 20.0))
    # 1h & 4h up move, 4h still moving higher
    short_entry_logic.append(
      (df["RSI_3_1h"] < 85.0) | (df["RSI_3_4h"] < 80.0) | (df["CCI_20_change_pct_4h"] < -0.0)
    )
    # 1h up move, 15m low
    short_entry_logic.append((df["RSI_3_1h"] < 85.0) | (df["AROONU_14_15m"] > 40.0))
    # 1h up move, 4h still not high enough, 1d low
    short_entry_logic.append((df["RSI_3_1h"] < 85.0) | (df["AROONU_14_4h"] > 80.0) | (df["RSI_14_1d"] > 40.0))
    # 1h & 4h up move, 4h still low
    short_entry_logic.append((df["RSI_3_1h"] < 80.0) | (df["RSI_3_4h"] < 80.0) | (df["AROONU_14_4h"] > 50.0))
    # 1h & 4h up move, 1d still low
    short_entry_logic.append((df["RSI_3_1h"] < 80.0) | (df["RSI_3_4h"] < 80.0) | (df["AROONU_14_1d"] > 50.0))
    # 1h & 4h up move, 1d low
    short_entry_logic.append(
      (df["RSI_3_1h"] < 80.0) | (df["RSI_3_4h"] < 70.0) | (df["STOCHRSIk_14_14_3_3_1d"] > 30.0)
    )
    # 1h up move, 1d still low, 1d uptrend
    short_entry_logic.append((df["RSI_3_1h"] < 80.0) | (df["AROONU_14_1d"] > 50.0) | (df["ROC_9_1d"] < 30.0))
    # 1h up move, 1d low
    short_entry_logic.append((df["RSI_3_1h"] < 80.0) | (df["STOCHRSIk_14_14_3_3_1d"] > 20.0))
    # 1h up move, 4h & 1d uptrend
    short_entry_logic.append((df["RSI_3_1h"] < 80.0) | (df["ROC_9_4h"] < 20.0) | (df["ROC_9_1d"] < 40.0))
    # 4h up move, 1d low
    short_entry_logic.append((df["RSI_3_4h"] < 95.0) | (df["RSI_14_1d"] > 40.0))
    # 4h down move, 15m still not high enough, 1d low
    short_entry_logic.append(
      (df["RSI_3_4h"] < 95.0) | (df["STOCHRSIk_14_14_3_3_15m"] > 80.0) | (df["AROOND_14_1d"] < 75.0)
    )
    # 4h up move, 1h & 4h uptrend
    short_entry_logic.append((df["RSI_3_4h"] < 95.0) | (df["ROC_9_1h"] < 20.0) | (df["ROC_9_4h"] < 20.0))
    # 4h up move, 15m low
    short_entry_logic.append((df["RSI_3_4h"] < 90.0) | (df["STOCHRSIk_14_14_3_3_15m"] > 45.0))
    # 4h up move, 4h & 1d uptrend
    short_entry_logic.append((df["RSI_3_4h"] < 90.0) | (df["ROC_9_4h"] < 20.0) | (df["ROC_9_1d"] < 40.0))
    # 4h up move, 15m still not high enough
    short_entry_logic.append((df["RSI_3_4h"] < 85.0) | (df["AROONU_14_15m"] > 60.0))
    # 4h up move, 15m low
    short_entry_logic.append((df["RSI_3_4h"] < 85.0) | (df["STOCHRSIk_14_14_3_3_15m"] > 30.0))
    # 4h up move, 4h uptrend
    short_entry_logic.append((df["RSI_3_4h"] < 80.0) | (df["AROONU_14_4h"] < 100.0) | (df["ROC_9_4h"] < 20.0))
    # 4h up move, 15m still low, 4h still not high enough
    short_entry_logic.append(
      (df["RSI_3_4h"] < 80.0) | (df["STOCHRSIk_14_14_3_3_15m"] > 60.0) | (df["AROONU_14_4h"] > 80.0)
    )
    # 4h up move, 15m still low, 4h still not high enough
    short_entry_logic.append(
      (df["RSI_3_4h"] < 75.0) | (df["STOCHRSIk_14_14_3_3_15m"] > 60.0) | (df["STOCHRSIk_14_14_3_3_4h"] > 80.0)
    )
    # 1d up move, 4h low
    short_entry_logic.append((df["RSI_3_1d"] < 85.0) | (df["STOCHRSIk_14_14_3_3_4h"] > 40.0))
    # 4h still not high enough, 4h overbought, 4h uptrend
    short_entry_logic.append(
      (df["RSI_14_4h"] > 80.0) | (df["ROC_9_4h"] < 40.0) | (df["CCI_20_change_pct_4h"] < 0.0)
    )
    # 15m & 1h high, 4h uptrend
    short_entry_logic.append(
      (df["AROONU_14_15m"] < 100.0) | (df["AROONU_14_1h"] < 100.0) | (df["ROC_9_4h"] < 20.0)
    )
    # 15m & 4h high, 1h uptrend
    short_entry_logic.append(
      (df["AROONU_14_15m"] < 100.0) | (df["AROONU_14_4h"] < 100.0) | (df["ROC_9_1h"] < 20.0)
    )
    # 15m high, 1d low
    short_entry_logic.append((df["AROONU_14_15m"] < 100.0) | (df["STOCHRSIk_14_14_3_3_1d"] > 20.0))
    # 15m high & uptrend
    short_entry_logic.append((df["AROONU_14_15m"] < 100.0) | (df["ROC_9_15m"] < 30.0))
    # 15m high, 1h & 4h uptrend
    short_entry_logic.append((df["AROONU_14_15m"] < 100.0) | (df["ROC_9_1h"] < 20.0) | (df["ROC_9_4h"] < 20.0))
    # 1h high, 15m uptrend
    short_entry_logic.append((df["AROONU_14_1h"] < 100.0) | (df["ROC_9_15m"] < 20.0))
    # 15m & 4h still not high enough
    short_entry_logic.append((df["STOCHRSIk_14_14_3_3_15m"] > 70.0) | (df["STOCHRSIk_14_14_3_3_4h"] > 70.0))
    # 1h & 4h overbought, 1h uptrend
    short_entry_logic.append(
      (df["ROC_9_1h"] < 10.0) | (df["ROC_9_4h"] < 40.0) | (df["CCI_20_change_pct_1h"] < 0.0)
    )
    # 1h & 4h overbought, 4h uptrend
    short_entry_logic.append(
      (df["ROC_9_1h"] < 10.0) | (df["ROC_9_4h"] < 40.0) | (df["CCI_20_change_pct_4h"] < 0.0)
    )
    # 1d bot wick, 4h still not high enough
    short_entry_logic.append((df["bot_wick_pct_1d"] < 30.0) | (df["STOCHRSIk_14_14_3_3_4h"] > 80.0))
    # rise in the last 12 hours, relatively stable before the 12 hours
    short_entry_logic.append(
      (df["close"] < (df["low_min_12_1h"] * 1.30)) | (df["low_min_12_1h"] > (df["low_min_24_1h"] * 1.10))
    )
    # big pump in the last 30 days, 4h up move
    short_entry_logic.append((df["close"] < (df["low_min_30_1d"] * 4.0)) | (df["RSI_3_4h"] < 85.0))

    # Logic
    short_entry_logic.append(df["WILLR_14"] > -50.0)
    short_entry_logic.append(df["AROONU_14"] > 75.0)
    short_entry_logic.append(df["AROOND_14"] < 25.0)
    short_entry_logic.append(df["STOCHRSIk_14_14_3_3"] > 80.0)
    short_entry_logic.append(df["WILLR_84_1h"] > -30.0)
    short_entry_logic.append(df["STOCHRSIk_14_14_3_3_1h"] > 80.0)
    short_entry_logic.append(df["BBB_20_2.0_1h"] > 20.0)
    short_entry_logic.append(df["close_min_48"] <= (df["close"] * 0.90))


def append_short_543(df, short_entry_logic, allowed_empty_candles_288) -> None:
    """Append NFI short condition #543, the rapid-mode short entry."""
    # Protections
    short_entry_logic.append(df["num_empty_288"] <= allowed_empty_candles_288)

    short_entry_logic.append(df["RSI_14_1h"] > 20.0)
    short_entry_logic.append(df["RSI_14_4h"] > 20.0)
    short_entry_logic.append(df["RSI_14_1d"] > 10.0)
    # 5m strong down move
    short_entry_logic.append((df["RSI_3"] < 98.0) | (df["ROC_9"] < 50.0))
    # 15m down move, 1h down move, 1h still not low enough
    short_entry_logic.append(
      (df["RSI_3_15m"] < 95.0) | (df["RSI_3_change_pct_1h"] < 60.0) | (df["STOCHRSIk_14_14_3_3_1h"] > 50.0)
    )
    # 15m down move, 1h down move, 4h still not low enough
    short_entry_logic.append(
      (df["RSI_3_15m"] < 95.0) | (df["RSI_3_change_pct_1h"] < 40.0) | (df["STOCHRSIk_14_14_3_3_4h"] > 30.0)
    )
    # 5m down move, 1h down, 4h high
    short_entry_logic.append(
      (df["RSI_3_15m"] < 95.0) | (df["CMF_20_1h"] < 0.2) | (df["STOCHRSIk_14_14_3_3_4h"] > 50.0)
    )
    # 15m down move, 1h still not low enough, 4h high
    short_entry_logic.append(
      (df["RSI_3_15m"] < 95.0) | (df["AROOND_14_1h"] < 25.0) | (df["STOCHRSIk_14_14_3_3_4h"] > 10.0)
    )
    # 15m down move, 1h still high
    short_entry_logic.append(
      (df["RSI_3_15m"] < 90.0) | (df["OBV_change_pct_15m"] < 50.0) | (df["STOCHRSIk_14_14_3_3_1h"] > 30.0)
    )
    # 5m & 1h strong down move, 1h still not low enough
    short_entry_logic.append(
      (df["RSI_3_15m"] < 95.0) | (df["RSI_3_1h"] < 95.0) | (df["STOCHRSIk_14_14_3_3_1h"] > 70.0)
    )
    # 5m & 1h strong downtrend
    short_entry_logic.append((df["RSI_3_15m"] < 95.0) | (df["RSI_3_1h"] < 95.0) | (df["MFI_14_1h"] < 90.0))
    # 15m & 1h down move, 4h still high
    short_entry_logic.append(
      (df["RSI_3_15m"] < 95.0)
      | (df["RSI_3_1h"] < 80.0)
      | (df["STOCHRSIk_14_14_3_3_4h"] > 70.0)
      | (df["AROOND_14_4h"] < 50.0)
    )
    # 15m & 1h down move, 4h still high, 4h downtrend
    short_entry_logic.append(
      (df["RSI_3_15m"] < 95.0) | (df["RSI_3_1h"] < 90.0) | (df["UO_7_14_28_4h"] > 60.0) | (df["ROC_9_4h"] < 20.0)
    )
    # 15m & 1h down move, 1d strong downtrend
    short_entry_logic.append((df["RSI_3_15m"] < 95.0) | (df["RSI_3_1h"] < 90.0) | (df["ROC_9_1d"] < 50.0))
    # 15m & 4h down move, 4h still not low enough
    short_entry_logic.append(
      (df["RSI_3_15m"] < 90.0) | (df["RSI_3_4h"] < 85.0) | (df["STOCHRSIk_14_14_3_3_4h"] > 55.0)
    )
    # 15m down move, 15m still not low enough, 1h still high
    short_entry_logic.append(
      (df["RSI_3_15m"] < 85.0) | (df["STOCHRSIk_14_14_3_3_15m"] > 50.0) | (df["STOCHRSIk_14_14_3_3_1h"] > 30.0)
    )
    # 15m & 1h down move, 1h still high
    short_entry_logic.append(
      (df["RSI_3_15m"] < 85.0) | (df["RSI_3_1h"] < 75.0) | (df["STOCHRSIk_14_14_3_3_1h"] > 30.0)
    )
    # 15m down move, 15m still not low enoug, 1h high
    short_entry_logic.append(
      (df["RSI_3_15m"] < 85.0) | (df["AROOND_14_15m"] < 25.0) | (df["STOCHRSIk_14_14_3_3_1h"] > 10.0)
    )
    # 15m down move, 1h downtrend, 4h overbought
    short_entry_logic.append((df["RSI_3_15m"] < 85.0) | (df["ROC_9_1h"] < 5.0) | (df["ROC_9_4h"] > -35.0))
    # 1h & 4h down move, 4h still not low enough
    short_entry_logic.append(
      (df["RSI_3_1h"] < 95.0) | (df["RSI_3_4h"] < 90.0) | (df["STOCHRSIk_14_14_3_3_4h"] > 75.0)
    )
    # 1h & 4h down move, 4h still high
    short_entry_logic.append(
      (df["RSI_3_1h"] < 95.0) | (df["RSI_3_change_pct_4h"] < 50.0) | (df["STOCHRSIk_14_14_3_3_4h"] > 50.0)
    )
    # 1h & 4h down move, 4h still not low enough
    short_entry_logic.append(
      (df["RSI_3_1h"] < 95.0) | (df["RSI_3_change_pct_4h"] < 65.0) | (df["STOCHRSIk_14_14_3_3_4h"] > 70.0)
    )
    # 1h down move, 1h still not low enough, 4h still not low
    short_entry_logic.append(
      (df["RSI_3_1h"] < 90.0) | (df["STOCHRSIk_14_14_3_3_1h"] > 70.0) | (df["RSI_14_4h"] > 50.0)
    )
    # 1h down move, 1h not low enough, 1h still high
    short_entry_logic.append(
      (df["RSI_3_1h"] < 85.0) | (df["AROOND_14_1h"] < 50.0) | (df["STOCHRSIk_14_14_3_3_4h"] > 50.0)
    )
    # 4h down move, 15m still not low enough, 1h still high
    short_entry_logic.append(
      (df["RSI_3_4h"] < 80.0) | (df["STOCHRSIk_14_14_3_3_15m"] > 70.0) | (df["STOCHRSIk_14_14_3_3_1h"] > 30.0)
    )
    # 4h down move, 4h still high, 1d downtrend
    short_entry_logic.append(
      (df["RSI_3_4h"] < 75.0) | (df["STOCHRSIk_14_14_3_3_4h"] > 50.0) | (df["ROC_9_1d"] < 50.0)
    )
    # 4h & 1d down move, 1d strong downtrend
    short_entry_logic.append((df["RSI_3_4h"] < 90.0) | (df["RSI_3_1d"] < 90.0) | (df["ROC_9_1d"] < 60.0))
    # 4h overbought, 1h still high, 1d downtrend
    short_entry_logic.append(
      (df["ROC_9_4h"] > -50.0) | (df["STOCHRSIk_14_14_3_3_1h"] > 70.0) | (df["ROC_9_1d"] < 50.0)
    )
    # 4h red, previous 4h green, 4h overbought
    short_entry_logic.append(
      (df["change_pct_4h"] < 5.0) | (df["change_pct_4h"].shift(48) > -5.0) | (df["RSI_14_4h"].shift(48) > 20.0)
    )
    # 4h red, 4h moving down, 4h still high, 1d downtrend
    short_entry_logic.append(
      (df["change_pct_4h"] < 10.0)
      | (df["CCI_20_change_pct_4h"] < 0.0)
      | (df["STOCHRSIk_14_14_3_3_4h"] > 50.0)
      | (df["ROC_9_1d"] < 40.0)
    )

    # Logic
    short_entry_logic.append(df["RSI_14"] > 60.0)
    short_entry_logic.append(df["MFI_14"] > 60.0)
    short_entry_logic.append(df["AROOND_14"] < 25.0)
    short_entry_logic.append(df["EMA_26"] < df["EMA_12"])
    short_entry_logic.append((df["EMA_26"] - df["EMA_12"]) > (df["open"] * 0.024))
    short_entry_logic.append((df["EMA_26"].shift() - df["EMA_12"].shift()) > (df["open"] / 100.0))
    short_entry_logic.append(df["close"] < (df["EMA_20"] * 0.958))
    short_entry_logic.append(df["close"] < (df["BBL_20_2.0"] * 0.992))


def append_short_641(df, short_entry_logic, allowed_empty_candles_288, is_pair_short_top_coins_mode) -> None:
    """Append NFI short condition #641, the top-coins-mode short entry."""
    # Protections
    short_entry_logic.append(is_pair_short_top_coins_mode)

    short_entry_logic.append(df["num_empty_288"] <= allowed_empty_candles_288)

    short_entry_logic.append(df["RSI_3_1h"] >= 5.0)
    short_entry_logic.append(df["RSI_3_4h"] >= 20.0)
    short_entry_logic.append(df["RSI_3_1d"] >= 20.0)
    short_entry_logic.append(df["RSI_14_1h"] > 20.0)
    short_entry_logic.append(df["RSI_14_4h"] > 20.0)
    short_entry_logic.append(df["RSI_14_1d"] > 10.0)
    # 5m down move, 1h still not low enough, 4h high
    short_entry_logic.append(
      (df["RSI_3"] < 90.0) | (df["STOCHRSIk_14_14_3_3_1h"] > 90.0) | (df["STOCHRSIk_14_14_3_3_4h"] > 30.0)
    )
    # 5m down move, 1h high, 4h still not low enough
    short_entry_logic.append(
      (df["RSI_3"] < 90.0) | (df["STOCHRSIk_14_14_3_3_1h"] > 20.0) | (df["STOCHRSIk_14_14_3_3_4h"] > 90.0)
    )
    # 15m down move, 15m still not low enough, 1h still high
    short_entry_logic.append(
      (df["RSI_3_15m"] < 95.0) | (df["AROOND_14_15m"] < 25.0) | (df["STOCHRSIk_14_14_3_3_1h"] > 50.0)
    )
    # 15m & 1h down move, 1d still not low enough
    short_entry_logic.append(
      (df["RSI_3_15m"] < 95.0) | (df["RSI_3_1h"] < 95.0) | (df["STOCHRSIk_14_14_3_3_1d"] > 70.0)
    )
    # 15m & 1h down move, 1h still not low enough
    short_entry_logic.append(
      (df["RSI_3_15m"] < 85.0) | (df["RSI_3_1h"] < 85.0) | (df["STOCHRSIk_14_14_3_3_1h"] > 70.0)
    )
    # 15m down move, 1h high, 4h still high
    short_entry_logic.append(
      (df["RSI_3_15m"] < 85.0) | (df["STOCHRSIk_14_14_3_3_1h"] > 30.0) | (df["STOCHRSIk_14_14_3_3_4h"] > 75.0)
    )
    # 15m & 1h down move, 4h still high
    short_entry_logic.append(
      (df["RSI_3_15m"] < 80.0) | (df["RSI_3_1h"] < 70.0) | (df["STOCHRSIk_14_14_3_3_4h"] > 50.0)
    )
    # 15m down move, 1h still not low enough, 4h still high
    short_entry_logic.append(
      (df["RSI_3_15m"] < 75.0) | (df["STOCHRSIk_14_14_3_3_1h"] > 80.0) | (df["STOCHRSIk_14_14_3_3_4h"] > 60.0)
    )
    # 1h & 4h & 1d down move
    short_entry_logic.append((df["RSI_3_1h"] < 95.0) | (df["RSI_3_4h"] < 90.0) | (df["RSI_3_1d"] < 80.0))
    # 1h & 4h down move, 15m not low enough
    short_entry_logic.append(
      (df["RSI_3_1h"] < 90.0) | (df["RSI_3_4h"] < 90.0) | (df["STOCHRSIk_14_14_3_3_15m"] > 75.0)
    )
    # 1h down move, 1h still not low enough, 4h still high
    short_entry_logic.append(
      (df["RSI_3_1h"] < 90.0) | (df["STOCHRSIk_14_14_3_3_1h"] > 90.0) | (df["STOCHRSIk_14_14_3_3_4h"] > 50.0)
    )
    # 1h & 4h down move, 1h still not low enough
    short_entry_logic.append(
      (df["RSI_3_1h"] < 85.0) | (df["RSI_3_4h"] < 75.0) | (df["STOCHRSIk_14_14_3_3_1h"] > 90.0)
    )
    # 1h & 4h down move, 4h still high
    short_entry_logic.append(
      (df["RSI_3_1h"] < 85.0) | (df["RSI_3_4h"] < 75.0) | (df["STOCHRSIk_14_14_3_3_4h"] > 50.0)
    )
    # 1h & 4h down move, 1h still not low enough
    short_entry_logic.append(
      (df["RSI_3_1h"] < 80.0) | (df["RSI_3_4h"] < 85.0) | (df["STOCHRSIk_14_14_3_3_1h"] > 75.0)
    )
    # 1h & 4h down move, 4h still not low enough
    short_entry_logic.append(
      (df["RSI_3_1h"] < 80.0) | (df["RSI_3_4h"] < 85.0) | (df["STOCHRSIk_14_14_3_3_4h"] > 75.0)
    )
    # 1h down move, 1h & 4h still not low enough
    short_entry_logic.append(
      (df["RSI_3_1h"] < 80.0) | (df["STOCHRSIk_14_14_3_3_1h"] > 90.0) | (df["STOCHRSIk_14_14_3_3_4h"] > 70.0)
    )
    # 4h down move, 15m still high, 1h still not low enough
    short_entry_logic.append(
      (df["RSI_3_4h"] < 85.0) | (df["STOCHRSIk_14_14_3_3_15m"] > 50.0) | (df["STOCHRSIk_14_14_3_3_1h"] > 75.0)
    )
    # 4h down move, 15m & 4h still not low enough
    short_entry_logic.append(
      (df["RSI_3_4h"] < 15.0) | (df["STOCHRSIk_14_14_3_3_15m"] > 30.0) | (df["STOCHRSIk_14_14_3_3_4h"] > 80.0)
    )

    # Logic
    short_entry_logic.append(df["RSI_20"] > df["RSI_20"].shift(1))
    short_entry_logic.append(df["RSI_3"] > 70.0)
    short_entry_logic.append(df["AROOND_14"] < 25.0)
    short_entry_logic.append(df["close"] > df["SMA_16"] * 1.044)


def append_short_642(df, short_entry_logic, allowed_empty_candles_288, is_pair_short_top_coins_mode) -> None:
    """Append NFI short condition #642, the top-coins-mode short entry."""
    # Protections
    short_entry_logic.append(is_pair_short_top_coins_mode)

    short_entry_logic.append(df["num_empty_288"] <= allowed_empty_candles_288)

    # 5m & 1h & 4h down move
    short_entry_logic.append((df["RSI_3"] < 90.0) | (df["RSI_3_1h"] < 95.0) | (df["RSI_3_4h"] < 90.0))
    # 5m down move, 15m & 4h still high
    short_entry_logic.append(
      (df["RSI_3"] < 90.0) | (df["STOCHRSIk_14_14_3_3_15m"] > 60.0) | (df["STOCHRSIk_14_14_3_3_4h"] > 60.0)
    )
    # 5m down move, 15m still high, 1h high
    short_entry_logic.append(
      (df["RSI_3"] < 85.0) | (df["AROOND_14_15m"] < 50.0) | (df["STOCHRSIk_14_14_3_3_1h"] > 20.0)
    )
    # 15m & 1h down move, 1h still not low enough
    short_entry_logic.append(
      (df["RSI_3_15m"] < 95.0) | (df["RSI_3_1h"] < 95.0) | (df["STOCHRSIk_14_14_3_3_1h"] > 90.0)
    )
    # 15m & 1h down move, 1d still not low enough
    short_entry_logic.append(
      (df["RSI_3_15m"] < 95.0) | (df["RSI_3_1h"] < 95.0) | (df["STOCHRSIk_14_14_3_3_1d"] > 70.0)
    )
    # 15m strong down move, 4h high
    short_entry_logic.append((df["RSI_3_15m"] < 95.0) | (df["STOCHRSIk_14_14_3_3_4h"] > 20.0))
    # 15m & 1h down move, 1h still not low enough
    short_entry_logic.append(
      (df["RSI_3_15m"] < 95.0) | (df["RSI_3_1h"] < 80.0) | (df["STOCHRSIk_14_14_3_3_1h"] > 80.0)
    )
    # 15m down move, 15m stil high, 1h still not low enough
    short_entry_logic.append(
      (df["RSI_3_15m"] < 90.0) | (df["STOCHRSIk_14_14_3_3_15m"] > 50.0) | (df["STOCHRSIk_14_14_3_3_1h"] > 80.0)
    )
    # 15m down move, 1h & 4h still high
    short_entry_logic.append(
      (df["RSI_3_15m"] < 90.0) | (df["STOCHRSIk_14_14_3_3_1h"] > 60.0) | (df["STOCHRSIk_14_14_3_3_4h"] > 60.0)
    )
    # 15m & 1h down move, 4h still not low enough
    short_entry_logic.append(
      (df["RSI_3_15m"] < 95.0) | (df["RSI_3_1h"] < 70.0) | (df["STOCHRSIk_14_14_3_3_4h"] > 50.0)
    )
    # 15m down move, 15m still not low enough, 4h high
    short_entry_logic.append(
      (df["RSI_3_15m"] < 85.0) | (df["STOCHRSIk_14_14_3_3_15m"] > 80.0) | (df["STOCHRSIk_14_14_3_3_4h"] > 20.0)
    )
    # 15m down move, 4h still high, 1d high
    short_entry_logic.append(
      (df["RSI_3_15m"] < 85.0) | (df["STOCHRSIk_14_14_3_3_4h"] > 60.0) | (df["STOCHRSIk_14_14_3_3_1d"] > 30.0)
    )
    # 15m & 4h down move, 1d still high
    short_entry_logic.append(
      (df["RSI_3_15m"] < 85.0) | (df["RSI_3_4h"] < 75.0) | (df["STOCHRSIk_14_14_3_3_1d"] > 50.0)
    )
    # 15m & 1h down move, 4h still not low enough
    short_entry_logic.append(
      (df["RSI_3_15m"] < 80.0) | (df["RSI_3_1h"] < 80.0) | (df["STOCHRSIk_14_14_3_3_4h"] > 70.0)
    )
    # 15m & 1h down move, 4h still not low enough
    short_entry_logic.append(
      (df["RSI_3_15m"] < 75.0) | (df["RSI_3_1h"] < 75.0) | (df["STOCHRSIk_14_14_3_3_4h"] > 70.0)
    )
    # 15m & 4h down move, 4h still not low enough
    short_entry_logic.append(
      (df["RSI_3_15m"] < 75.0) | (df["RSI_3_4h"] < 75.0) | (df["STOCHRSIk_14_14_3_3_4h"] > 80.0)
    )
    # 15m down move, 1h still high, 4h still high
    short_entry_logic.append(
      (df["RSI_3_15m"] < 75.0) | (df["STOCHRSIk_14_14_3_3_1h"] > 80.0) | (df["STOCHRSIk_14_14_3_3_4h"] > 60.0)
    )
    # 15m down move, 1h still not low enough, 4h high
    short_entry_logic.append(
      (df["RSI_3_15m"] < 75.0) | (df["STOCHRSIk_14_14_3_3_1h"] > 90.0) | (df["STOCHRSIk_14_14_3_3_4h"] > 30.0)
    )
    # 15m down move, 1h high, 4h still not low enough
    short_entry_logic.append(
      (df["RSI_3_15m"] < 75.0) | (df["STOCHRSIk_14_14_3_3_1h"] > 20.0) | (df["STOCHRSIk_14_14_3_3_4h"] > 90.0)
    )
    # 15m down move, 4h high, 1d stil high
    short_entry_logic.append(
      (df["RSI_3_15m"] < 75.0) | (df["STOCHRSIk_14_14_3_3_4h"] > 20.0) | (df["STOCHRSIk_14_14_3_3_1d"] > 50.0)
    )
    # 15m & 4h down move, 1h still not low enough
    short_entry_logic.append(
      (df["RSI_3_15m"] < 70.0) | (df["RSI_3_4h"] < 85.0) | (df["STOCHRSIk_14_14_3_3_1h"] > 70.0)
    )
    # 15m & 4h down move, 1h still high
    short_entry_logic.append(
      (df["RSI_3_15m"] < 70.0) | (df["RSI_3_4h"] < 80.0) | (df["STOCHRSIk_14_14_3_3_1h"] > 50.0)
    )
    # 15m down move, 15m still high 4h still high
    short_entry_logic.append(
      (df["RSI_3_15m"] < 70.0) | (df["STOCHRSIk_14_14_3_3_15m"] > 70.0) | (df["STOCHRSIk_14_14_3_3_4h"] > 50.0)
    )
    # 15m down move, 1h still high, 4h high
    short_entry_logic.append(
      (df["RSI_3_15m"] < 70.0) | (df["STOCHRSIk_14_14_3_3_1h"] > 50.0) | (df["STOCHRSIk_14_14_3_3_4h"] > 10.0)
    )
    # 1h & 4h down move, 1h still not low enough
    short_entry_logic.append(
      (df["RSI_3_1h"] < 95.0) | (df["RSI_3_4h"] < 95.0) | (df["STOCHRSIk_14_14_3_3_1h"] > 90.0)
    )
    # 1h & 4h down move, 4h still not low enough
    short_entry_logic.append(
      (df["RSI_3_1h"] < 95.0) | (df["RSI_3_4h"] < 85.0) | (df["STOCHRSIk_14_14_3_3_4h"] > 80.0)
    )
    # 1h & 4h down move, 1h still not low enough
    short_entry_logic.append(
      (df["RSI_3_1h"] < 90.0) | (df["RSI_3_4h"] < 90.0) | (df["STOCHRSIk_14_14_3_3_1h"] > 90.0)
    )
    # 1h & 4h down move, 4h still not low enough
    short_entry_logic.append(
      (df["RSI_3_1h"] < 90.0) | (df["RSI_3_4h"] < 90.0) | (df["STOCHRSIk_14_14_3_3_4h"] > 80.0)
    )
    # 1h & 4h down move, 1h still not low enough
    short_entry_logic.append(
      (df["RSI_3_1h"] < 90.0) | (df["RSI_3_4h"] < 85.0) | (df["STOCHRSIk_14_14_3_3_1h"] > 85.0)
    )
    # 1h & 4h down move, 1d still high
    short_entry_logic.append(
      (df["RSI_3_1h"] < 90.0) | (df["RSI_3_4h"] < 85.0) | (df["STOCHRSIk_14_14_3_3_1d"] > 50.0)
    )
    # 1h & 4h down move, 4h still not low enough
    short_entry_logic.append(
      (df["RSI_3_1h"] < 85.0) | (df["RSI_3_4h"] < 75.0) | (df["STOCHRSIk_14_14_3_3_4h"] > 85.0)
    )
    # 1h down move, 4h still high, 1d high
    short_entry_logic.append(
      (df["RSI_3_1h"] < 80.0) | (df["STOCHRSIk_14_14_3_3_4h"] > 60.0) | (df["STOCHRSIk_14_14_3_3_1d"] > 30.0)
    )
    # 1h & 4h down move, 1h still not low enough
    short_entry_logic.append(
      (df["RSI_3_1h"] < 80.0) | (df["RSI_3_4h"] < 85.0) | (df["STOCHRSIk_14_14_3_3_1h"] > 75.0)
    )
    # 1h & 4h down move, 15m still high
    short_entry_logic.append(
      (df["RSI_3_1h"] < 80.0) | (df["RSI_3_4h"] < 80.0) | (df["STOCHRSIk_14_14_3_3_15m"] > 50.0)
    )
    # 1h & 4h down move, 4h still not low enough
    short_entry_logic.append(
      (df["RSI_3_1h"] < 75.0) | (df["RSI_3_4h"] < 90.0) | (df["STOCHRSIk_14_14_3_3_1h"] > 75.0)
    )
    # 1h & 4h down move, 1h still high
    short_entry_logic.append(
      (df["RSI_3_1h"] < 70.0) | (df["RSI_3_4h"] < 85.0) | (df["STOCHRSIk_14_14_3_3_1h"] > 60.0)
    )
    # 1h down move, 1h still not low enough, 4h still high
    short_entry_logic.append(
      (df["RSI_3_1h"] < 70.0) | (df["STOCHRSIk_14_14_3_3_1h"] > 80.0) | (df["STOCHRSIk_14_14_3_3_4h"] > 50.0)
    )
    # 4h down move, 15m still high, 1h still not low enough
    short_entry_logic.append(
      (df["RSI_3_4h"] < 85.0) | (df["STOCHRSIk_14_14_3_3_15m"] > 60.0) | (df["STOCHRSIk_14_14_3_3_1h"] > 80.0)
    )
    # 4h down move, 15m still high, 4h still not low enough
    short_entry_logic.append(
      (df["RSI_3_4h"] < 75.0) | (df["STOCHRSIk_14_14_3_3_15m"] > 50.0) | (df["STOCHRSIk_14_14_3_3_4h"] > 75.0)
    )
    # 4h down move, 1h still not low enough, 1d still high
    short_entry_logic.append(
      (df["RSI_3_4h"] < 25.0) | (df["STOCHRSIk_14_14_3_3_1h"] > 70.0) | (df["STOCHRSIk_14_14_3_3_1d"] > 50.0)
    )
    # 15m & 1h still high, 4h high
    short_entry_logic.append(
      (df["STOCHRSIk_14_14_3_3_15m"] > 70.0)
      | (df["STOCHRSIk_14_14_3_3_1h"] > 70.0)
      | (df["STOCHRSIk_14_14_3_3_4h"] > 10.0)
    )
    # 15m still high, 1h & 1d high
    short_entry_logic.append(
      (df["STOCHRSIk_14_14_3_3_15m"] > 60.0)
      | (df["STOCHRSIk_14_14_3_3_1h"] > 30.0)
      | (df["STOCHRSIk_14_14_3_3_1d"] > 30.0)
    )
    # 15m & 4h high
    short_entry_logic.append((df["STOCHRSIk_14_14_3_3_15m"] > 50.0) | (df["STOCHRSIk_14_14_3_3_4h"] > 20.0))
    # 15m high, 1h & 4h still not low enough
    short_entry_logic.append(
      (df["STOCHRSIk_14_14_3_3_15m"] > 30.0)
      | (df["STOCHRSIk_14_14_3_3_1h"] > 75.0)
      | (df["STOCHRSIk_14_14_3_3_4h"] > 75.0)
    )
    # 15m & 4h high
    short_entry_logic.append((df["STOCHRSIk_14_14_3_3_15m"] > 30.0) | (df["STOCHRSIk_14_14_3_3_4h"] > 30.0))
    # 1h & 4h still high, 1d high
    short_entry_logic.append(
      (df["STOCHRSIk_14_14_3_3_1h"] > 70.0)
      | (df["STOCHRSIk_14_14_3_3_4h"] > 70.0)
      | (df["STOCHRSIk_14_14_3_3_1d"] > 50.0)
    )
    # 1h & 4h high
    short_entry_logic.append((df["STOCHRSIk_14_14_3_3_1h"] > 30.0) | (df["STOCHRSIk_14_14_3_3_4h"] > 10.0))
    # 1h & 4h high
    short_entry_logic.append((df["STOCHRSIk_14_14_3_3_1h"] > 20.0) | (df["STOCHRSIk_14_14_3_3_4h"] > 20.0))
    # 4h & 1d high
    short_entry_logic.append((df["STOCHRSIk_14_14_3_3_4h"] > 20.0) | (df["STOCHRSIk_14_14_3_3_1d"] > 20.0))
    # 1d red, 1d high
    short_entry_logic.append((df["change_pct_1d"] < 5.0) | (df["STOCHRSIk_14_14_3_3_1d"] > 20.0))
    # 1d P&D, 1d high
    short_entry_logic.append(
      (df["change_pct_1d"] < 10.0)
      | (df["change_pct_1d"].shift(288) > -10.0)
      | (df["STOCHRSIk_14_14_3_3_1d"] > 50.0)
    )

    # Logic
    short_entry_logic.append(df["RSI_4"] > 54.0)
    short_entry_logic.append(df["RSI_20"] > df["RSI_20"].shift(1))
    short_entry_logic.append(df["close"] > df["SMA_16"] * 1.042)


def append_short_661(df, short_entry_logic, allowed_empty_candles_288) -> None:
    """Append NFI short condition #661, the scalp-mode short entry."""
    # Protections
    short_entry_logic.append(df["num_empty_288"] <= allowed_empty_candles_288)

    # 15m down move, 15m high
    short_entry_logic.append((df["RSI_3_15m"] < 75.0) | (df["AROOND_14_15m"] < 80.0))
    # 15m & 1h down move, 15m still high
    short_entry_logic.append((df["RSI_3_15m"] < 70.0) | (df["RSI_3_1h"] < 40.0) | (df["AROOND_14_15m"] < 50.0))
    # 15m down move, 15m & 4h still high
    short_entry_logic.append(
      (df["RSI_3_15m"] < 70.0) | (df["STOCHRSIk_14_14_3_3_15m"] > 50.0) | (df["STOCHRSIk_14_14_3_3_4h"] > 50.0)
    )
    # 15m & 1h down move, 1h high
    short_entry_logic.append((df["RSI_3_15m"] < 60.0) | (df["RSI_3_1h"] < 60.0) | (df["AROOND_14_1h"] < 70.0))
    # 15m & 1h down move, 1h still high
    short_entry_logic.append(
      (df["RSI_3_15m"] < 60.0) | (df["RSI_3_1h"] < 60.0) | (df["STOCHRSIk_14_14_3_3_1h"] > 50.0)
    )
    # 15m & 1h down move, 4h high
    short_entry_logic.append((df["RSI_3_15m"] < 60.0) | (df["RSI_3_1h"] < 40.0) | (df["AROOND_14_4h"] < 80.0))
    # 15m & 4h down move, 15m high
    short_entry_logic.append(
      (df["RSI_3_15m"] < 60.0) | (df["RSI_3_4h"] < 60.0) | (df["STOCHRSIk_14_14_3_3_15m"] > 50.0)
    )
    # 15m & 4h down move, 15m high
    short_entry_logic.append(
      (df["RSI_3_15m"] < 60.0) | (df["RSI_3_4h"] < 40.0) | (df["STOCHRSIk_14_14_3_3_15m"] > 30.0)
    )
    # 15m down move, 15m & 1h still high
    short_entry_logic.append(
      (df["RSI_3_15m"] < 60.0) | (df["AROOND_14_15m"] < 50.0) | (df["STOCHRSIk_14_14_3_3_1h"] > 50.0)
    )
    # 15m down move, 15m & 1h still high
    short_entry_logic.append(
      (df["RSI_3_15m"] < 60.0) | (df["STOCHRSIk_14_14_3_3_15m"] > 50.0) | (df["STOCHRSIk_14_14_3_3_1h"] > 50.0)
    )
    # 15m down move, 4h still high, 1d overbought
    short_entry_logic.append((df["RSI_3_15m"] < 60.0) | (df["AROOND_14_4h"] < 50.0) | (df["ROC_9_1d"] > -100.0))
    # 15m down move, 15m high, 4h still high
    short_entry_logic.append(
      (df["RSI_3_15m"] < 55.0) | (df["AROOND_14_15m"] > 30.0) | (df["STOCHRSIk_14_14_3_3_4h"] > 50.0)
    )
    # 15m down move, 15m & 1h still high
    short_entry_logic.append(
      (df["RSI_3_15m"] < 55.0) | (df["STOCHRSIk_14_14_3_3_15m"] > 55.0) | (df["STOCHRSIk_14_14_3_3_1h"] > 60.0)
    )
    # 15m down move, 15m still not low enough, 4h high
    short_entry_logic.append(
      (df["RSI_3_15m"] < 50.0) | (df["STOCHRSIk_14_14_3_3_15m"] > 70.0) | (df["STOCHRSIk_14_14_3_3_4h"] > 10.0)
    )
    # 1h down move, 4h still high, 1d high
    short_entry_logic.append(
      (df["RSI_3_1h"] < 75.0) | (df["AROOND_14_4h"] < 50.0) | (df["STOCHRSIk_14_14_3_3_1d"] > 10.0)
    )
    short_entry_logic.append(
      (df["RSI_3_1h"] < 70.0) | (df["STOCHRSIk_14_14_3_3_1h"] > 60.0) | (df["STOCHRSIk_14_14_3_3_1d"] > 10.0)
    )
    # 1h & 4h down move, 4h high
    short_entry_logic.append(
      (df["RSI_3_1h"] < 65.0) | (df["RSI_3_4h"] < 40.0) | (df["STOCHRSIk_14_14_3_3_4h"] > 20.0)
    )
    # 1h down move, 15m & 1h still high
    short_entry_logic.append(
      (df["RSI_3_1h"] < 60.0) | (df["STOCHRSIk_14_14_3_3_15m"] > 50.0) | (df["STOCHRSIk_14_14_3_3_1h"] > 50.0)
    )
    # 1h down move, 1h still high, 4h high
    short_entry_logic.append(
      (df["RSI_3_1h"] < 60.0) | (df["STOCHRSIk_14_14_3_3_1h"] > 50.0) | (df["STOCHRSIk_14_14_3_3_4h"] > 70.0)
    )
    # 1h down move, 1h high
    short_entry_logic.append((df["RSI_3_1h"] < 60.0) | (df["STOCHRSIk_14_14_3_3_1h"] > 40.0))
    # 1h down move, 4h & 1d high
    short_entry_logic.append((df["RSI_3_1h"] < 60.0) | (df["AROOND_14_4h"] < 85.0) | (df["AROOND_14_1d"] < 90.0))
    # 1h down move, 1h still high, 4h high
    short_entry_logic.append((df["RSI_3_1h"] < 55.0) | (df["AROOND_14_1h"] < 50.0) | (df["AROOND_14_4h"] < 90.0))
    # 1h down move, 1h high
    short_entry_logic.append((df["RSI_3_1h"] < 55.0) | (df["STOCHRSIk_14_14_3_3_1h"] > 40.0))
    # 1h & 4h down move, 15m high
    short_entry_logic.append((df["RSI_3_1h"] < 50.0) | (df["RSI_3_4h"] < 40.0) | (df["AROOND_14_15m"] < 70.0))
    # 1h down move, 15m still high, 4h high
    short_entry_logic.append(
      (df["RSI_3_1h"] < 50.0) | (df["AROOND_14_15m"] < 50.0) | (df["AROOND_14_4h"] < 80.0)
    )
    # 1h down move, 15m high, 1h still high
    short_entry_logic.append(
      (df["RSI_3_1h"] < 50.0) | (df["AROOND_14_15m"] < 70.0) | (df["STOCHRSIk_14_14_3_3_1h"] > 60.0)
    )
    # 1h down move, 15m still high, 4h high
    short_entry_logic.append(
      (df["RSI_3_1h"] < 50.0) | (df["STOCHRSIk_14_14_3_3_15m"] > 50.0) | (df["STOCHRSIk_14_14_3_3_4h"] > 20.0)
    )
    # 1h down move, 15m & 1h high
    short_entry_logic.append(
      (df["RSI_3_1h"] < 50.0) | (df["STOCHRSIk_14_14_3_3_15m"] > 40.0) | (df["AROOND_14_1h"] < 60.0)
    )
    # 1h down move, 1h & 1d high
    short_entry_logic.append(
      (df["RSI_3_1h"] < 50.0) | (df["AROOND_14_1h"] < 70.0) | (df["STOCHRSIk_14_14_3_3_1d"] > 20.0)
    )
    # 1h down move, 4h still high, 1d high
    short_entry_logic.append(
      (df["RSI_3_1h"] < 50.0) | (df["STOCHRSIk_14_14_3_3_4h"] > 50.0) | (df["STOCHRSIk_14_14_3_3_1d"] > 10.0)
    )
    # 1h down move, 5m up move, 1h still high
    short_entry_logic.append(
      (df["RSI_3_1h"] < 40.0) | (df["RSI_3"] > 40.0) | (df["STOCHRSIk_14_14_3_3_1h"] > 50.0)
    )
    # 1h down move, 15m still not low enough, 1h high
    short_entry_logic.append(
      (df["RSI_3_1h"] < 40.0) | (df["STOCHRSIk_14_14_3_3_15m"] > 70.0) | (df["AROOND_14_1h"] < 70.0)
    )
    # 1h down move, 15m still not low enough, 1h high
    short_entry_logic.append(
      (df["RSI_3_1h"] < 40.0) | (df["STOCHRSIk_14_14_3_3_15m"] > 70.0) | (df["STOCHRSIk_14_14_3_3_1h"] > 40.0)
    )
    # 1h down move, 15m & 4h still high
    short_entry_logic.append(
      (df["RSI_3_1h"] < 40.0) | (df["STOCHRSIk_14_14_3_3_15m"] > 50.0) | (df["STOCHRSIk_14_14_3_3_4h"] > 50.0)
    )
    # 1h down move, 15m & 1h high
    short_entry_logic.append(
      (df["RSI_3_1h"] < 40.0) | (df["AROOND_14_15m"] < 70.0) | (df["AROOND_14_1h"] < 90.0)
    )
    # 1h down move, 1h still high, 4h high
    short_entry_logic.append(
      (df["RSI_3_1h"] < 40.0) | (df["AROOND_14_1h"] < 50.0) | (df["STOCHRSIk_14_14_3_3_4h"] > 10.0)
    )
    # 1h down move, 1h high, 4h still high
    short_entry_logic.append((df["RSI_3_1h"] < 40.0) | (df["AROOND_14_1h"] < 80.0) | (df["AROOND_14_4h"] < 40.0))
    # 1h down move, 1h still high, 4h high
    short_entry_logic.append(
      (df["RSI_3_1h"] < 40.0) | (df["STOCHRSIk_14_14_3_3_1h"] > 60.0) | (df["AROOND_14_4h"] < 70.0)
    )
    # 1h down move, 1h & 1d high
    short_entry_logic.append(
      (df["RSI_3_1h"] < 40.0) | (df["STOCHRSIk_14_14_3_3_1h"] > 30.0) | (df["AROOND_14_1d"] < 90.0)
    )
    # 1h down move, 4h & 1d high
    short_entry_logic.append((df["RSI_3_1h"] < 40.0) | (df["RSI_14_4h"] > 30.0) | (df["RSI_14_1d"] > 20.0))
    # 4h down move, 15m high
    short_entry_logic.append((df["RSI_3_4h"] < 80.0) | (df["AROOND_14_15m"] < 80.0))
    # 4h down move, 1h high
    short_entry_logic.append((df["RSI_3_4h"] < 75.0) | (df["STOCHRSIk_14_14_3_3_1h"] > 20.0))
    # 4h down move, 1h & 4h still high
    short_entry_logic.append(
      (df["RSI_3_4h"] < 65.0) | (df["STOCHRSIk_14_14_3_3_1h"] > 50.0) | (df["AROOND_14_4h"] < 50.0)
    )
    # 4h down move, 15m & 1h high
    short_entry_logic.append(
      (df["RSI_3_4h"] < 60.0) | (df["AROOND_14_15m"] < 80.0) | (df["STOCHRSIk_14_14_3_3_1h"] > 30.0)
    )
    # 4h down move, 15m still high, 1h high
    short_entry_logic.append(
      (df["RSI_3_4h"] < 60.0) | (df["STOCHRSIk_14_14_3_3_15m"] > 60.0) | (df["STOCHRSIk_14_14_3_3_1h"] > 20.0)
    )
    # 4h down move, 1h still high, 4h still moving down
    short_entry_logic.append(
      (df["RSI_3_4h"] < 60.0) | (df["STOCHRSIk_14_14_3_3_1h"] > 50.0) | (df["CCI_20_change_pct_4h"] < 0.0)
    )
    # 4h down move, 1h high, 4h still high
    short_entry_logic.append((df["RSI_3_4h"] < 55.0) | (df["AROOND_14_1h"] < 70.0) | (df["AROOND_14_4h"] < 50.0))
    # 4h down move, 15m high, 4h still high
    short_entry_logic.append(
      (df["RSI_3_4h"] < 50.0) | (df["AROOND_14_15m"] < 70.0) | (df["STOCHRSIk_14_14_3_3_4h"] > 60.0)
    )
    # 4h down move, 15m still high, 1h high
    short_entry_logic.append(
      (df["RSI_3_4h"] < 50.0) | (df["STOCHRSIk_14_14_3_3_15m"] > 60.0) | (df["STOCHRSIk_14_14_3_3_1h"] > 30.0)
    )
    # 4h down move, 15m & 4h still high
    short_entry_logic.append(
      (df["RSI_3_4h"] < 50.0) | (df["STOCHRSIk_14_14_3_3_15m"] > 50.0) | (df["AROOND_14_4h"] < 50.0)
    )
    # 4h down move, 15m high, 4h still not low enough
    short_entry_logic.append(
      (df["RSI_3_4h"] < 50.0) | (df["STOCHRSIk_14_14_3_3_15m"] > 30.0) | (df["STOCHRSIk_14_14_3_3_4h"] > 70.0)
    )
    # 4h down move, 1h still high, 4h high
    short_entry_logic.append(
      (df["RSI_3_4h"] < 50.0) | (df["STOCHRSIk_14_14_3_3_1h"] > 50.0) | (df["AROOND_14_4h"] < 70.0)
    )
    # 4h down move, 15m & 4h high
    short_entry_logic.append(
      (df["RSI_3_4h"] < 40.0) | (df["AROOND_14_15m"] < 70.0) | (df["AROOND_14_4h"] < 70.0)
    )
    # 4h down move, 15m high, 4h still high
    short_entry_logic.append(
      (df["RSI_3_4h"] < 40.0) | (df["AROOND_14_15m"] < 80.0) | (df["AROOND_14_4h"] < 40.0)
    )
    # 4h down move, 15m still high, 4h high
    short_entry_logic.append(
      (df["RSI_3_4h"] < 40.0) | (df["STOCHRSIk_14_14_3_3_15m"] > 50.0) | (df["STOCHRSIk_14_14_3_3_4h"] > 30.0)
    )
    # 4h down move, 15m & 4h high
    short_entry_logic.append(
      (df["RSI_3_4h"] < 40.0) | (df["STOCHRSIk_14_14_3_3_15m"] > 30.0) | (df["STOCHRSIk_14_14_3_3_4h"] > 40.0)
    )
    # 4h down move, 1h & 4h high
    short_entry_logic.append(
      (df["RSI_3_4h"] < 40.0) | (df["STOCHRSIk_14_14_3_3_1h"] > 30.0) | (df["AROOND_14_4h"] < 70.0)
    )
    # 4h down move, 4h still high, 1d high
    short_entry_logic.append(
      (df["RSI_3_4h"] < 40.0) | (df["STOCHRSIk_14_14_3_3_4h"] > 50.0) | (df["STOCHRSIk_14_14_3_3_1d"] > 20.0)
    )
    # 15m high, 4h high
    short_entry_logic.append((df["AROOND_14_15m"] < 70.0) | (df["AROOND_14_4h"] < 85.0))
    # 15m high, 4h still high
    short_entry_logic.append((df["AROOND_14_15m"] < 80.0) | (df["STOCHRSIk_14_14_3_3_4h"] > 50.0))
    # 15m high, 1h still high
    short_entry_logic.append((df["STOCHRSIk_14_14_3_3_15m"] > 30.0) | (df["STOCHRSIk_14_14_3_3_1h"] > 60.0))
    # 15m & 4h high
    short_entry_logic.append((df["STOCHRSIk_14_14_3_3_15m"] > 30.0) | (df["AROOND_14_4h"] < 70.0))
    # 15m high, 1h still not low enough
    short_entry_logic.append((df["STOCHRSIk_14_14_3_3_15m"] > 20.0) | (df["STOCHRSIk_14_14_3_3_1h"] > 70.0))

    # Logic
    short_entry_logic.append(df["RSI_14"] > 50.0)
    short_entry_logic.append(df["AROOND_14_15m"] < 90.0)
    short_entry_logic.append(df["STOCHRSIk_14_14_3_3_15m"] > 10.0)
    if isinstance(df["SMA_200"].iloc[-1], np.float64):
      short_entry_logic.append(df["SMA_21"].shift(1) > df["SMA_200"].shift(1))
      short_entry_logic.append(df["SMA_21"] < df["SMA_200"])
    else:
      short_entry_logic.append(pd.Series([False]))
    if isinstance(df["EMA_200_1h"].iloc[-1], np.float64):
      short_entry_logic.append(df["close"] < df["EMA_200_1h"])
    else:
      short_entry_logic.append(pd.Series([False]))
    if isinstance(df["EMA_200_4h"].iloc[-1], np.float64):
      short_entry_logic.append(df["close"] < df["EMA_200_4h"])
    else:
      short_entry_logic.append(pd.Series([False]))
    short_entry_logic.append(df["BBB_20_2.0_1h"] > 4.0)

