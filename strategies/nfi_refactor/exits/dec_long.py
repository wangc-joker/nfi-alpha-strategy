"""DEC long exit signal library extracted from NFI."""

import numpy as np

def long_exit_dec(
    strategy,
    mode_name: str,
    current_profit: float,
    max_profit: float,
    max_loss: float,
    last_candle,
    previous_candle_1,
    previous_candle_2,
    previous_candle_3,
    previous_candle_4,
    previous_candle_5,
    trade: "Trade",
    current_time: "datetime",
    buy_tag,
  ) -> tuple:
    if 0.01 > current_profit >= 0.001:
      if (
        (last_candle["WILLR_14"] > -1.0)
        and (last_candle["RSI_14"] > 78.0)
        and (
          isinstance(last_candle["EMA_200_1h"], np.float64) and (last_candle["EMA_12_1h"] < last_candle["EMA_200_1h"])
        )
        and (
          isinstance(last_candle["EMA_200_4h"], np.float64) and (last_candle["EMA_12_4h"] < last_candle["EMA_200_4h"])
        )
        and (last_candle["KST_10_15_20_30_10_10_10_15_1h"] < last_candle["KSTs_9_1h"])
        and (last_candle["KST_10_15_20_30_10_10_10_15_4h"] < last_candle["KSTs_9_4h"])
      ):
        return True, f"exit_{mode_name}_d_0_1"
      elif (
        (last_candle["WILLR_14"] > -1.0)
        and (last_candle["RSI_14"] > 78.0)
        and (last_candle["CMF_20_1h"] < -0.0)
        and (
          isinstance(last_candle["EMA_200_1h"], np.float64) and (last_candle["EMA_12_1h"] < last_candle["EMA_200_1h"])
        )
        and (
          isinstance(last_candle["EMA_200_4h"], np.float64) and (last_candle["EMA_12_4h"] < last_candle["EMA_200_4h"])
        )
      ):
        return True, f"exit_{mode_name}_d_0_2"
      elif (
        (last_candle["WILLR_14"] > -1.0)
        and (last_candle["STOCHRSIk_14_14_3_3"] > 99.0)
        and (last_candle["CMF_20_1h"] < -0.0)
        and (last_candle["CMF_20_4h"] < -0.0)
        and (
          (last_candle["STOCHRSIk_14_14_3_3_4h"] > 20.0) and (last_candle["STOCHRSIk_14_14_3_3_change_pct_4h"] < -10.0)
        )
      ):
        return True, f"exit_{mode_name}_d_0_3"
      elif (
        (last_candle["WILLR_14"] > -1.0)
        and (last_candle["RSI_14"] > 78.0)
        and (last_candle["STOCHRSIk_14_14_3_3"] > 95.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 70.0)
        and (
          isinstance(last_candle["EMA_200_1h"], np.float64) and (last_candle["EMA_12_1h"] < last_candle["EMA_200_1h"])
        )
        and (
          isinstance(last_candle["EMA_200_4h"], np.float64) and (last_candle["EMA_12_4h"] < last_candle["EMA_200_4h"])
        )
      ):
        return True, f"exit_{mode_name}_d_0_4"
      elif (
        (last_candle["WILLR_14"] > -1.0)
        and (last_candle["RSI_14"] > 78.0)
        and (last_candle["ROC_9_1h"] < -5.0)
        and (last_candle["ROC_9_4h"] < -5.0)
      ):
        return True, f"exit_{mode_name}_d_0_5"
      elif (
        (last_candle["RSI_3"] > 95.0)
        and (last_candle["STOCHRSIk_14_14_3_3"] > 95.0)
        and (last_candle["RSI_14"] < 40.0)
        and (last_candle["ROC_9_1h"] < -10.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 50.0))
      ):
        return True, f"exit_{mode_name}_d_0_6"
      elif (
        (last_candle["RSI_14"] < 50.0)
        and (last_candle["STOCHRSIk_14_14_3_3"] > 95.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -40.0))
      ):
        return True, f"exit_{mode_name}_d_0_7"
      elif (
        (last_candle["WILLR_14"] > -1.0)
        and (last_candle["STOCHRSIk_14_14_3_3"] > 99.0)
        and (last_candle["CMF_20_1h"] < -0.1)
        and (last_candle["CMF_20_4h"] < -0.1)
        and (last_candle["change_pct_1d"] < -5.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 15.0))
      ):
        return True, f"exit_{mode_name}_d_0_8"
      elif (
        (last_candle["WILLR_14"] > -1.0)
        and (last_candle["RSI_3"] > 99.0)
        and (last_candle["change_pct_4h"] < -5.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 30.0))
      ):
        return True, f"exit_{mode_name}_d_0_9"
      elif (
        (last_candle["WILLR_14"] > -1.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["ROC_9_1h"] < -10.0)
        and (last_candle["ROC_9_4h"] < -10.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 10.0))
      ):
        return True, f"exit_{mode_name}_d_0_10"
      elif (
        (last_candle["RSI_3"] > 95.0)
        and (last_candle["RSI_14"] < 45.0)
        and (last_candle["ROC_9_15m"] < -10.0)
        and (last_candle["ROC_9_1h"] < -10.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -20.0))
      ):
        return True, f"exit_{mode_name}_d_0_11"
      elif (
        (last_candle["RSI_3"] > 95.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_4h"] < 10.0)
        and (last_candle["ROC_9_1h"] < -20.0)
        and (last_candle["ROC_9_4h"] < -20.0)
      ):
        return True, f"exit_{mode_name}_d_0_12"
      elif (last_candle["RSI_3"] > 99.0) and (last_candle["RSI_3_4h"] < 5.0) and (last_candle["ROC_9_4h"] < -25.0):
        return True, f"exit_{mode_name}_d_0_13"
      elif (
        (last_candle["RSI_3"] > 99.0)
        and (last_candle["WILLR_14"] > -1.0)
        and (last_candle["RSI_3_4h"] < 5.0)
        and (last_candle["AROONU_14_4h"] > 25.0)
      ):
        return True, f"exit_{mode_name}_d_0_14"
      elif (last_candle["RSI_3"] > 99.0) and (last_candle["RSI_14"] > 78.0) and (last_candle["ROC_9_4h"] < -30.0):
        return True, f"exit_{mode_name}_d_0_15"
      elif (
        (last_candle["RSI_3"] > 99.0)
        and (last_candle["AROONU_14_4h"] > 25.0)
        and (last_candle["ROC_9_4h"] < -25.0)
        and (last_candle["AROONU_14_1d"] > 50.0)
        and (last_candle["change_pct_1d"] < -15.0)
      ):
        return True, f"exit_{mode_name}_d_0_16"
      elif (
        (last_candle["RSI_3"] > 99.0)
        and (last_candle["WILLR_14"] > -1.0)
        and (last_candle["RSI_3_1h"] < 10.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 90.0)
        and (last_candle["ROC_9_4h"] > 30.0)
      ):
        return True, f"exit_{mode_name}_d_0_17"
      elif (
        (last_candle["RSI_3"] > 95.0)
        and (last_candle["RSI_14"] > 75.0)
        and (last_candle["RSI_3_4h"] < 20.0)
        and (last_candle["ROC_2_1d"] < -50.0)
      ):
        return True, f"exit_{mode_name}_d_0_18"
      elif (
        (last_candle["RSI_3"] > 99.0)
        and (last_candle["RSI_14"] > 78.0)
        and (last_candle["RSI_3_4h"] < 10.0)
        and (
          isinstance(last_candle["STOCHRSIk_14_14_3_3_1d"], np.float64)
          and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 70.0)
        )
      ):
        return True, f"exit_{mode_name}_d_0_19"
      elif (
        (last_candle["RSI_3"] > 90.0)
        and (last_candle["RSI_14"] < 40.0)
        and (last_candle["RSI_3_1h"] < 10.0)
        and (last_candle["AROONU_14_1h"] > 25.0)
      ):
        return True, f"exit_{mode_name}_d_0_20"
      elif (
        (last_candle["RSI_3"] > 95.0)
        and (last_candle["RSI_14"] < 40.0)
        and (last_candle["RSI_3_1h"] < 20.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 90.0)
      ):
        return True, f"exit_{mode_name}_d_0_21"
      elif (
        (last_candle["RSI_3"] > 99.0)
        and (last_candle["WILLR_14"] > -1.0)
        and (last_candle["change_pct_4h"] < -5.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -30.0))
      ):
        return True, f"exit_{mode_name}_d_0_22"
      elif (
        (last_candle["RSI_3"] > 98.0)
        and (last_candle["WILLR_14"] > -5.0)
        and (last_candle["RSI_3_1h"] < 15.0)
        and (last_candle["RSI_3_1d"] < 5.0)
      ):
        return True, f"exit_{mode_name}_d_0_23"
      elif (
        (last_candle["RSI_3"] > 99.0)
        and (last_candle["RSI_14"] > 78.0)
        and (last_candle["WILLR_14"] > -5.0)
        and (last_candle["RSI_3_4h"] < 30.0)
        and (last_candle["AROONU_14_4h"] > 75.0)
      ):
        return True, f"exit_{mode_name}_d_0_24"
      elif (
        (last_candle["RSI_3"] > 95.0)
        and (last_candle["WILLR_14"] > -2.0)
        and (last_candle["RSI_3_4h"] < 10.0)
        and (last_candle["ROC_9_4h"] < -15.0)
        and (
          isinstance(last_candle["STOCHRSIk_14_14_3_3_1d"], np.float64)
          and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 50.0)
        )
      ):
        return True, f"exit_{mode_name}_d_0_25"
      elif (
        (last_candle["RSI_3"] > 95.0)
        and (last_candle["WILLR_14"] > -1.0)
        and (last_candle["RSI_3_4h"] < 15.0)
        and (last_candle["ROC_9_4h"] < -20.0)
      ):
        return True, f"exit_{mode_name}_d_0_26"
      elif (
        (last_candle["RSI_3"] > 95.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_1h"] < 20.0)
        and (last_candle["RSI_3_4h"] < 20.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 20.0)
      ):
        return True, f"exit_{mode_name}_d_0_27"
      elif (
        (last_candle["RSI_3"] > 95.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_15m"] < 10.0)
        and (last_candle["ROC_9_4h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_0_28"
      elif (
        (last_candle["RSI_3"] > 95.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_1h"] < 20.0)
        and (last_candle["RSI_3_4h"] < 20.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 30.0)
      ):
        return True, f"exit_{mode_name}_d_0_29"
      elif (
        (last_candle["RSI_3"] > 99.0)
        and (last_candle["RSI_3_1h"] < 25.0)
        and (last_candle["RSI_3_4h"] < 10.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 70.0)
      ):
        return True, f"exit_{mode_name}_d_0_30"
      elif (
        (last_candle["RSI_3"] > 95.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_1h"] < 15.0)
        and (last_candle["RSI_3_4h"] < 15.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 25.0)
      ):
        return True, f"exit_{mode_name}_d_0_31"
      elif (
        (last_candle["RSI_3"] > 95.0)
        and (last_candle["RSI_3_1h"] < 15.0)
        and (last_candle["ROC_2_4h"] < -30.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 30.0)
      ):
        return True, f"exit_{mode_name}_d_0_32"
      elif (
        (last_candle["RSI_3"] > 95.0)
        and (last_candle["WILLR_14"] > -1.0)
        and (last_candle["ROC_2_1h"] < -10.0)
        and (last_candle["ROC_9_1h"] > 30.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_0_33"
      elif (
        (last_candle["RSI_3"] > 65.0)
        and (last_candle["RSI_3_15m"] < 30.0)
        and (last_candle["RSI_14_1h"] > 80.0)
        and (last_candle["ROC_9_1h"] > 40.0)
      ):
        return True, f"exit_{mode_name}_d_0_34"
      elif (
        (last_candle["RSI_3"] > 95.0)
        and (last_candle["WILLR_14"] > -5.0)
        and (last_candle["RSI_3_1d"] < 25.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 75.0)
      ):
        return True, f"exit_{mode_name}_d_0_35"
      elif (
        (last_candle["RSI_3"] > 95.0)
        and (last_candle["WILLR_14"] > -1.0)
        and (last_candle["ROC_9_4h"] < -25.0)
        and (last_candle["RSI_3_1d"] < 25.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_0_36"
      elif (
        (last_candle["RSI_3"] > 84.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_1h"] < 20.0)
        and (last_candle["RSI_3_1d"] < 25.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_0_37"
      elif (
        (last_candle["RSI_3"] > 90.0)
        and (last_candle["WILLR_14"] > -10.0)
        and (last_candle["RSI_3_4h"] < 10.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 20.0)
      ):
        return True, f"exit_{mode_name}_d_0_38"
      elif (
        (last_candle["RSI_3"] > 99.0)
        and (last_candle["WILLR_14"] > -1.0)
        and (last_candle["CMF_20_4h"] < -0.0)
        and (last_candle["RSI_3_4h"] < 10.0)
      ):
        return True, f"exit_{mode_name}_d_0_39"
      elif (
        (last_candle["RSI_3"] > 98.0)
        and (last_candle["WILLR_14"] > -2.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 30.0)
        and (
          isinstance(last_candle["STOCHRSIk_14_14_3_3_1d"], np.float64)
          and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 90.0)
        )
      ):
        return True, f"exit_{mode_name}_d_0_40"
      elif (
        (last_candle["RSI_3"] > 98.0)
        and (last_candle["WILLR_14"] > -5.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 25.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 50.0))
      ):
        return True, f"exit_{mode_name}_d_0_41"
      elif (
        (last_candle["RSI_3"] > 95.0)
        and (last_candle["WILLR_14"] > -2.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 30.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 40.0))
        and (
          isinstance(last_candle["STOCHRSIk_14_14_3_3_1d"], np.float64)
          and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 70.0)
        )
      ):
        return True, f"exit_{mode_name}_d_0_42"
      elif (
        (last_candle["RSI_3"] > 95.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_1h"] < 15.0)
        and (last_candle["RSI_3_4h"] < 40.0)
        and (
          isinstance(last_candle["STOCHRSIk_14_14_3_3_1d"], np.float64)
          and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 90.0)
        )
      ):
        return True, f"exit_{mode_name}_d_0_43"
      elif (
        (last_candle["RSI_3"] > 90.0)
        and (last_candle["WILLR_14"] > -2.0)
        and (last_candle["RSI_3_4h"] < 30.0)
        and (last_candle["RSI_3_1d"] < 25.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -30.0))
      ):
        return True, f"exit_{mode_name}_d_0_44"
      elif (last_candle["RSI_3"] > 96.0) and (last_candle["WILLR_14"] > -4.0) and (last_candle["RSI_3_1h"] < 10.0):
        return True, f"exit_{mode_name}_d_0_45"
      elif (
        (last_candle["RSI_3"] > 98.0)
        and (last_candle["RSI_3_1h"] < 15.0)
        and (last_candle["RSI_3_4h"] < 10.0)
        and (last_candle["ROC_2_1d"] < -20.0)
      ):
        return True, f"exit_{mode_name}_d_0_46"
      elif (
        (last_candle["RSI_3"] > 98.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 80.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 40.0)
        and (last_candle["change_pct_1d"] < -5.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -5.0))
      ):
        return True, f"exit_{mode_name}_d_0_47"
      elif (
        (last_candle["RSI_3"] > 70.0)
        and (last_candle["RSI_14"] < 42.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (last_candle["RSI_3_4h"] < 20.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_0_48"
      elif (
        (last_candle["RSI_3"] > 95.0)
        and (last_candle["WILLR_14"] > -2.0)
        and (last_candle["RSI_3_4h"] < 20.0)
        and (last_candle["change_pct_1d"] < -5.0)
        and (
          isinstance(last_candle["STOCHRSIk_14_14_3_3_1d"], np.float64)
          and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 50.0)
        )
      ):
        return True, f"exit_{mode_name}_d_0_49"
      elif (
        (last_candle["RSI_3"] > 80.0)
        and (last_candle["WILLR_14"] > -2.0)
        and (last_candle["RSI_3_1d"] < 10.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 90.0)
      ):
        return True, f"exit_{mode_name}_d_0_50"
      elif (
        (last_candle["RSI_3"] > 68.0)
        and (last_candle["RSI_14"] < 44.0)
        and (last_candle["RSI_3_4h"] < 20.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_0_51"
      elif (
        (last_candle["RSI_3"] > 95.0)
        and (last_candle["RSI_14"] > 62.0)
        and (last_candle["WILLR_14"] > -10.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 70.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -15.0))
      ):
        return True, f"exit_{mode_name}_d_0_52"
      elif (
        (last_candle["RSI_3"] > 95.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["WILLR_14"] > -5.0)
        and (last_candle["RSI_3_1h"] < 20.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
        and (
          isinstance(last_candle["STOCHRSIk_14_14_3_3_1d"], np.float64)
          and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 50.0)
        )
      ):
        return True, f"exit_{mode_name}_d_0_53"
      elif (
        (last_candle["RSI_3"] > 80.0)
        and (last_candle["RSI_14"] < 44.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
        and (last_candle["ROC_9_4h"] < -10.0)
        and (last_candle["change_pct_1d"] < -10.0)
      ):
        return True, f"exit_{mode_name}_d_0_54"
      elif (
        (last_candle["RSI_3"] > 98.0)
        and (last_candle["WILLR_14"] > -12.0)
        and (last_candle["ROC_9_4h"] < -5.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 10.0))
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_0_55"
      elif (
        (last_candle["RSI_3"] > 95.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (last_candle["RSI_3_4h"] < 25.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -30.0))
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 10.0)
      ):
        return True, f"exit_{mode_name}_d_0_56"
      elif (
        (last_candle["RSI_3"] > 50.0)
        and (last_candle["RSI_14"] < 34.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -30.0))
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 70.0)
      ):
        return True, f"exit_{mode_name}_d_0_57"
      elif (
        (last_candle["RSI_3"] > 95.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (last_candle["RSI_3_4h"] < 30.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -15.0))
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_0_58"
      elif (
        (last_candle["RSI_3"] > 95.0)
        and (last_candle["WILLR_14"] > -10.0)
        and (last_candle["RSI_3_4h"] < 25.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -15.0))
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 40.0)
      ):
        return True, f"exit_{mode_name}_d_0_59"
      elif (
        (last_candle["RSI_3"] > 95.0)
        and (last_candle["RSI_14"] < 38.0)
        and (last_candle["RSI_14_4h"] > 65.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_0_60"
      elif (
        (last_candle["RSI_3"] > 98.0)
        and (last_candle["WILLR_14"] > -25.0)
        and (last_candle["RSI_3_4h"] < 10.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 30.0)
      ):
        return True, f"exit_{mode_name}_d_0_61"
      elif (
        (last_candle["RSI_3"] > 88.0)
        and (last_candle["WILLR_14"] > -1.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (last_candle["RSI_3_4h"] < 20.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 20.0))
        and (last_candle["change_pct_1d"] < -5.0)
      ):
        return True, f"exit_{mode_name}_d_0_62"
      elif (
        (last_candle["RSI_3"] > 98.0)
        and (last_candle["RSI_3_1d"] < 25.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 80.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 30.0)
      ):
        return True, f"exit_{mode_name}_d_0_63"
      elif (
        (last_candle["RSI_3"] > 98.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (last_candle["RSI_3_4h"] < 30.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 30.0))
      ):
        return True, f"exit_{mode_name}_d_0_64"
      elif (
        (last_candle["RSI_3"] > 90.0)
        and (last_candle["RSI_14"] < 40.0)
        and (last_candle["RSI_3_1h"] < 20.0)
        and (last_candle["RSI_3_4h"] < 15.0)
      ):
        return True, f"exit_{mode_name}_d_0_65"
      elif (
        (last_candle["RSI_3"] > 84.0)
        and (last_candle["RSI_14"] < 46.0)
        and (last_candle["RSI_3_1h"] < 20.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_0_66"
      elif (
        (last_candle["RSI_3"] > 50.0)
        and (last_candle["RSI_14"] < 40.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 80.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -25.0))
      ):
        return True, f"exit_{mode_name}_d_0_67"
      elif (
        (last_candle["RSI_3"] > 86.0)
        and (last_candle["RSI_14"] < 46.0)
        and (last_candle["RSI_3_1h"] < 25.0)
        and (last_candle["ROC_2_4h"] < -30.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 25.0)
      ):
        return True, f"exit_{mode_name}_d_0_68"
      elif (
        (last_candle["RSI_3"] > 97.0)
        and (last_candle["ROC_9_4h"] > 20.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
        and (last_candle["change_pct_4h"] < -5.0)
      ):
        return True, f"exit_{mode_name}_d_0_69"
      elif (
        (last_candle["RSI_3"] > 95.0)
        and (last_candle["RSI_14"] < 38.0)
        and (last_candle["RSI_3_1h"] < 25.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 20.0)
      ):
        return True, f"exit_{mode_name}_d_0_70"
      elif (
        (last_candle["RSI_3"] > 95.0)
        and (last_candle["RSI_14"] < 42.0)
        and (last_candle["RSI_3_4h"] < 25.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 20.0)
      ):
        return True, f"exit_{mode_name}_d_0_71"
      elif (
        (last_candle["RSI_3"] > 95.0)
        and (last_candle["RSI_14"] < 40.0)
        and (last_candle["RSI_3_1h"] < 10.0)
        and (last_candle["AROONU_14_4h"] > 25.0)
      ):
        return True, f"exit_{mode_name}_d_0_72"
      elif (
        (last_candle["RSI_3"] > 95.0)
        and (last_candle["RSI_3_1h"] < 25.0)
        and (last_candle["RSI_3_4h"] < 15.0)
        and (last_candle["ROC_9_4h"] < -20.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -25.0))
      ):
        return True, f"exit_{mode_name}_d_0_73"
      elif (
        (last_candle["RSI_3"] > 99.0)
        and (last_candle["WILLR_14"] > -10.0)
        and (last_candle["RSI_3_4h"] < 25.0)
        and (last_candle["RSI_3_1d"] < 25.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_0_74"
      elif (
        (last_candle["RSI_3"] > 98.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (last_candle["RSI_3_4h"] < 20.0)
        and (
          isinstance(last_candle["STOCHRSIk_14_14_3_3_1d"], np.float64)
          and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 50.0)
        )
      ):
        return True, f"exit_{mode_name}_d_0_75"
      elif (
        (last_candle["RSI_3"] > 95.0)
        and (last_candle["RSI_14"] < 48.0)
        and (last_candle["ROC_9_1h"] > 80.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 80.0)
      ):
        return True, f"exit_{mode_name}_d_0_76"
      elif (
        (last_candle["RSI_3"] > 95.0)
        and (last_candle["RSI_14"] < 44.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 50.0))
      ):
        return True, f"exit_{mode_name}_d_0_77"
      elif (
        (last_candle["RSI_3"] > 98.0)
        and (last_candle["WILLR_14"] > -14.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (last_candle["RSI_3_4h"] < 20.0)
        and (last_candle["RSI_3_1d"] < 20.0)
      ):
        return True, f"exit_{mode_name}_d_0_78"
      elif (
        (last_candle["RSI_3"] > 94.0)
        and (last_candle["WILLR_14"] > -1.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (last_candle["RSI_3_4h"] < 10.0)
      ):
        return True, f"exit_{mode_name}_d_0_79"
      elif (
        (last_candle["RSI_3"] > 74.0)
        and (last_candle["RSI_14"] < 44.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 50.0))
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 25.0)
      ):
        return True, f"exit_{mode_name}_d_0_80"
      elif (
        (last_candle["RSI_3"] > 96.0)
        and (last_candle["WILLR_14"] > -8.0)
        and (last_candle["RSI_3_1h"] < 25.0)
        and (last_candle["RSI_3_4h"] < 25.0)
        and (isinstance(last_candle["RSI_14_1d"], np.float64) and (last_candle["RSI_14_1d"] > 50.0))
      ):
        return True, f"exit_{mode_name}_d_0_81"
      elif (
        (last_candle["RSI_3"] > 84.0)
        and (last_candle["WILLR_14"] > -8.0)
        and (last_candle["RSI_3_4h"] < 30.0)
        and (last_candle["RSI_3_1d"] < 15.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 40.0)
      ):
        return True, f"exit_{mode_name}_d_0_82"
      elif (
        (last_candle["RSI_3"] > 95.0)
        and (last_candle["RSI_14"] < 44.0)
        and (last_candle["RSI_3_1h"] < 40.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 40.0)
      ):
        return True, f"exit_{mode_name}_d_0_83"
      elif (
        (last_candle["RSI_3"] > 99.0)
        and (last_candle["WILLR_14"] > -1.0)
        and (last_candle["RSI_3_4h"] < 30.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 20.0)
      ):
        return True, f"exit_{mode_name}_d_0_84"
      elif (
        (last_candle["RSI_3"] > 99.0)
        and (last_candle["WILLR_14"] > -6.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (last_candle["RSI_3_4h"] < 40.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_0_85"
      elif (
        (last_candle["RSI_3"] > 96.0)
        and (last_candle["RSI_14_4h"] > 80.0)
        and (last_candle["ROC_2_1h"] < -5.0)
        and (last_candle["ROC_9_1h"] > 5.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_0_86"
      elif (
        (last_candle["RSI_3"] > 95.0)
        and (last_candle["RSI_14"] < 42.0)
        and (last_candle["RSI_3_1h"] < 45.0)
        and (last_candle["RSI_3_4h"] < 50.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_0_87"
      elif (
        (last_candle["RSI_3"] > 95.0)
        and (last_candle["WILLR_14"] > -2.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 40.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
        and (last_candle["change_pct_1h"] < -2.0)
      ):
        return True, f"exit_{mode_name}_d_0_88"
      elif (
        (last_candle["RSI_3"] > 90.0)
        and (last_candle["RSI_14"] < 38.0)
        and (last_candle["ROC_9_1h"] < -5.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 25.0))
      ):
        return True, f"exit_{mode_name}_d_0_89"
      elif (
        (last_candle["RSI_3"] > 94.0)
        and (last_candle["WILLR_14"] > -25.0)
        and (last_candle["RSI_3_1h"] < 50.0)
        and (last_candle["RSI_3_4h"] < 30.0)
        and (last_candle["AROONU_14_4h"] > 50.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 40.0))
      ):
        return True, f"exit_{mode_name}_d_0_90"
      elif (
        (last_candle["RSI_3"] > 90.0)
        and (last_candle["RSI_14"] < 44.0)
        and (last_candle["RSI_3_1h"] < 25.0)
        and (last_candle["RSI_3_4h"] < 25.0)
        and (last_candle["AROONU_14_4h"] > 50.0)
        and (
          isinstance(last_candle["STOCHRSIk_14_14_3_3_1d"], np.float64)
          and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 50.0)
        )
      ):
        return True, f"exit_{mode_name}_d_0_91"
      elif (
        (last_candle["RSI_3"] > 95.0)
        and (last_candle["RSI_14"] < 46.0)
        and (last_candle["RSI_3_1h"] < 40.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 25.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -25.0))
      ):
        return True, f"exit_{mode_name}_d_0_92"
      elif (
        (last_candle["RSI_3"] > 90.0)
        and (last_candle["RSI_14"] < 48.0)
        and (last_candle["RSI_3_15m"] < 50.0)
        and (last_candle["AROONU_14_1h"] > 75.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 70.0)
        and (last_candle["AROONU_14_4h"] > 50.0)
        and (
          isinstance(last_candle["STOCHRSIk_14_14_3_3_1d"], np.float64)
          and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 90.0)
        )
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 30.0))
      ):
        return True, f"exit_{mode_name}_d_0_93"
      elif (
        (last_candle["RSI_3"] > 95.0)
        and (last_candle["RSI_14"] < 48.0)
        and (last_candle["RSI_3_1h"] < 25.0)
        and (last_candle["RSI_3_4h"] < 45.0)
        and (last_candle["AROONU_14_1h"] > 75.0)
        and (
          isinstance(last_candle["STOCHRSIk_14_14_3_3_1d"], np.float64)
          and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 90.0)
        )
      ):
        return True, f"exit_{mode_name}_d_0_94"
      elif (
        (last_candle["RSI_3"] > 95.0)
        and (last_candle["WILLR_14"] > -10.0)
        and (last_candle["RSI_3_1h"] < 45.0)
        and (last_candle["RSI_3_4h"] < 40.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 10.0)
        and (isinstance(last_candle["AROONU_14_1d"], np.float64) and (last_candle["AROONU_14_1d"] > 75.0))
      ):
        return True, f"exit_{mode_name}_d_0_95"
      elif (
        (last_candle["RSI_3"] > 90.0)
        and (last_candle["RSI_14"] < 44.0)
        and (last_candle["RSI_3_1h"] < 45.0)
        and (last_candle["RSI_3_1d"] < 45.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_0_96"
      elif (
        (last_candle["RSI_3"] > 84.0)
        and (last_candle["RSI_14"] < 44.0)
        and (last_candle["RSI_3_1h"] < 35.0)
        and (last_candle["AROONU_14_4h"] > 50.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 30.0)
      ):
        return True, f"exit_{mode_name}_d_0_97"
      elif (
        (last_candle["RSI_3"] > 92.0)
        and (last_candle["RSI_3_15m"] > 74.0)
        and (last_candle["RSI_3_1h"] < 60.0)
        and (last_candle["RSI_3_4h"] < 60.0)
        and (last_candle["RSI_3_1d"] > 80.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_0_98"
      elif (
        (last_candle["RSI_3"] > 95.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_1h"] < 65.0)
        and (last_candle["RSI_3_4h"] < 60.0)
        and (last_candle["AROONU_14_4h"] > 50.0)
        and (last_candle["STOCHk_14_3_3_4h"] > 40.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 80.0))
      ):
        return True, f"exit_{mode_name}_d_0_99"
      elif (
        (last_candle["RSI_3"] > 99.0)
        and (last_candle["RSI_14"] > 78.0)
        and (last_candle["RSI_3_15m"] > 70.0)
        and (last_candle["RSI_3_4h"] < 80.0)
      ):
        return True, f"exit_{mode_name}_d_0_100"
      elif (
        (last_candle["RSI_3"] > 86.0)
        and (last_candle["WILLR_14"] > -14.0)
        and (last_candle["RSI_3_1h"] < 50.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 40.0)
        and (isinstance(last_candle["ROC_9_4h"], np.float64) and (last_candle["ROC_9_4h"] > 40.0))
      ):
        return True, f"exit_{mode_name}_d_0_101"
      elif (
        (last_candle["RSI_3"] > 95.0)
        and (last_candle["RSI_14"] < 46.0)
        and (last_candle["RSI_3_1h"] < 60.0)
        and (last_candle["RSI_3_4h"] < 40.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 30.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 40.0))
      ):
        return True, f"exit_{mode_name}_d_0_102"
      elif (
        (last_candle["RSI_3"] > 95.0)
        and (last_candle["RSI_14"] < 54.0)
        and (last_candle["RSI_3_1h"] < 60.0)
        and (last_candle["RSI_14_4h"] > 70.0)
        and (isinstance(last_candle["ROC_9_4h"], np.float64) and (last_candle["ROC_9_4h"] > 80.0))
      ):
        return True, f"exit_{mode_name}_d_0_103"
      elif (
        (last_candle["RSI_3"] > 95.0)
        and (last_candle["RSI_14"] < 46.0)
        and (last_candle["RSI_3_1h"] < 60.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 40.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 90.0)
        and (last_candle["ROC_9_4h"] > 40.0)
      ):
        return True, f"exit_{mode_name}_d_0_104"
      elif (
        (last_candle["RSI_3"] > 95.0)
        and (last_candle["RSI_14"] < 46.0)
        and (last_candle["RSI_3_15m"] < 55.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 90.0)
        and (last_candle["ROC_9_4h"] > 25.0)
      ):
        return True, f"exit_{mode_name}_d_0_105"
      elif (
        (last_candle["RSI_3"] > 95.0)
        and (last_candle["RSI_14"] < 46.0)
        and (last_candle["RSI_3_1h"] < 50.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
        and (last_candle["RSI_14_4h"] > 70.0)
        and (last_candle["ROC_9_4h"] > 40.0)
      ):
        return True, f"exit_{mode_name}_d_0_106"
      elif (
        (last_candle["RSI_3"] > 95.0)
        and (last_candle["RSI_14"] < 46.0)
        and (last_candle["RSI_3_1h"] < 50.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 70.0)
        and (last_candle["RSI_14_4h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_0_107"
      elif (
        (last_candle["RSI_3"] > 95.0)
        and (last_candle["RSI_14"] < 46.0)
        and (last_candle["RSI_3_1h"] < 60.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 80.0)
      ):
        return True, f"exit_{mode_name}_d_0_108"
      elif (
        (last_candle["RSI_3"] > 95.0)
        and (last_candle["WILLR_14"] > -6.0)
        and (last_candle["RSI_3_1h"] < 50.0)
        and (last_candle["RSI_3_4h"] < 20.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 50.0))
      ):
        return True, f"exit_{mode_name}_d_0_109"
      elif (
        (last_candle["RSI_3"] > 95.0)
        and (last_candle["RSI_3_4h"] < 65.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
        and (last_candle["ROC_9_4h"] > 25.0)
      ):
        return True, f"exit_{mode_name}_d_0_110"
      elif (
        (last_candle["RSI_3"] > 95.0)
        and (last_candle["RSI_14"] < 42.0)
        and (last_candle["RSI_3_1h"] < 50.0)
        and (last_candle["RSI_14_4h"] > 70.0)
        and (last_candle["AROONU_14_1h"] > 75.0)
        and (last_candle["AROONU_14_4h"] > 75.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 20.0))
      ):
        return True, f"exit_{mode_name}_d_0_111"
      elif (
        (last_candle["RSI_3"] > 95.0)
        and (last_candle["WILLR_14"] > -20.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_1h"] < 35.0)
        and (last_candle["RSI_3_4h"] < 35.0)
        and (last_candle["RSI_3_1d"] < 60.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 30.0))
      ):
        return True, f"exit_{mode_name}_d_0_112"
      elif (
        (last_candle["RSI_3"] > 95.0)
        and (last_candle["WILLR_14"] > -1.0)
        and (last_candle["RSI_3_1d"] < 30.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
        and (isinstance(last_candle["ROC_9_4h"], np.float64) and (last_candle["ROC_9_4h"] > 10.0))
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -10.0))
      ):
        return True, f"exit_{mode_name}_d_0_113"
      elif (
        (last_candle["RSI_3"] > 95.0)
        and (last_candle["RSI_14"] < 48.0)
        and (last_candle["RSI_3_1h"] < 20.0)
        and (last_candle["RSI_3_4h"] < 30.0)
        and (last_candle["RSI_3_1d"] < 30.0)
      ):
        return True, f"exit_{mode_name}_d_0_114"
      elif (
        (last_candle["RSI_3"] > 95.0)
        and (last_candle["RSI_14"] < 46.0)
        and (last_candle["RSI_3_15m"] < 30.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_0_115"
      elif (
        (last_candle["RSI_3"] > 92.0)
        and (last_candle["RSI_3_1h"] < 15.0)
        and (last_candle["RSI_3_4h"] < 40.0)
        and (last_candle["AROONU_14_4h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_0_116"
      elif (
        (last_candle["RSI_3"] > 95.0)
        and (last_candle["RSI_3_1h"] < 50.0)
        and (last_candle["AROONU_14_1h"] > 80.0)
        and (last_candle["AROONU_14_4h"] > 80.0)
      ):
        return True, f"exit_{mode_name}_d_0_117"
      elif (
        (last_candle["RSI_3"] > 92.0)
        and (last_candle["RSI_3_1h"] < 20.0)
        and (last_candle["RSI_3_4h"] < 60.0)
        and (last_candle["AROONU_14_4h"] > 40.0)
      ):
        return True, f"exit_{mode_name}_d_0_118"
      elif (
        (last_candle["RSI_3"] > 95.0)
        and (last_candle["WILLR_14"] > -20.0)
        and (last_candle["RSI_3_1h"] < 60.0)
        and (last_candle["RSI_3_4h"] < 60.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 40.0)
      ):
        return True, f"exit_{mode_name}_d_0_119"
      elif (
        (last_candle["RSI_3"] > 95.0)
        and (last_candle["RSI_14"] < 46.0)
        and (last_candle["RSI_3_1h"] < 40.0)
        and (last_candle["AROONU_14_4h"] > 75.0)
      ):
        return True, f"exit_{mode_name}_d_0_120"
      elif (
        (last_candle["RSI_3"] > 95.0)
        and (last_candle["RSI_14"] < 44.0)
        and (last_candle["RSI_3_1h"] < 50.0)
        and (last_candle["RSI_14_4h"] > 85.0)
      ):
        return True, f"exit_{mode_name}_d_0_121"
      elif (
        (last_candle["RSI_3"] > 95.0)
        and (last_candle["RSI_14"] < 42.0)
        and (last_candle["RSI_3_4h"] < 30.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_0_122"
      elif (
        (last_candle["RSI_3"] > 95.0)
        and (last_candle["WILLR_14"] > -2.0)
        and (last_candle["RSI_3_1h"] < 10.0)
        and (last_candle["RSI_3_1d"] < 30.0)
      ):
        return True, f"exit_{mode_name}_d_0_123"
      elif (
        (last_candle["RSI_3"] > 95.0)
        and (last_candle["RSI_3_1h"] < 15.0)
        and (
          isinstance(last_candle["STOCHRSIk_14_14_3_3_1d"], np.float64)
          and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 80.0)
        )
      ):
        return True, f"exit_{mode_name}_d_0_124"
      elif (
        (last_candle["RSI_3"] > 95.0)
        and (last_candle["WILLR_14"] > -2.0)
        and (last_candle["RSI_3_1h"] < 10.0)
        and (last_candle["RSI_3_4h"] < 40.0)
        and (last_candle["RSI_3_1d"] < 40.0)
        and (last_candle["close"] < (last_candle["high_max_30_1d"] * 0.50))
      ):
        return True, f"exit_{mode_name}_d_0_125"
      elif (
        (last_candle["RSI_3"] > 95.0)
        and (last_candle["RSI_3_1h"] < 15.0)
        and (last_candle["RSI_3_4h"] < 40.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_0_126"
      elif (
        (last_candle["RSI_3"] > 95.0)
        and (last_candle["RSI_3_1h"] < 10.0)
        and (last_candle["RSI_3_4h"] < 30.0)
        and (last_candle["RSI_3_1d"] < 40.0)
      ):
        return True, f"exit_{mode_name}_d_0_127"
      elif (last_candle["RSI_3"] > 96.0) and (last_candle["RSI_3_4h"] < 30.0) and (last_candle["AROONU_14_4h"] > 85.0):
        return True, f"exit_{mode_name}_d_0_128"
      elif (
        (last_candle["RSI_3"] > 95.0)
        and (last_candle["RSI_3_4h"] < 25.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 80.0))
      ):
        return True, f"exit_{mode_name}_d_0_129"
      elif (
        (last_candle["RSI_3"] > 95.0)
        and (last_candle["RSI_14_1h"] > 65.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 80.0)
        and (last_candle["CCI_20_change_pct_1h"] < -0.0)
      ):
        return True, f"exit_{mode_name}_d_0_130"
      elif (
        (last_candle["RSI_14"] < 36.0)
        and (last_candle["RSI_3_1h"] < 20.0)
        and (last_candle["RSI_3_4h"] < 30.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_0_131"
      elif (
        (last_candle["RSI_3"] > 95.0)
        and (last_candle["RSI_3_1h"] < 35.0)
        and (last_candle["RSI_3_4h"] < 35.0)
        and (last_candle["AROONU_14_1h"] > 50.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 40.0)
      ):
        return True, f"exit_{mode_name}_d_0_132"
      elif (
        (last_candle["RSI_3"] > 95.0)
        and (last_candle["AROONU_14_15m"] > 75.0)
        and (last_candle["AROONU_14_1h"] > 75.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 25.0))
      ):
        return True, f"exit_{mode_name}_d_0_133"
    elif 0.02 > current_profit >= 0.01:
      if (
        (last_candle["WILLR_14"] > -1.0)
        and (last_candle["RSI_14"] > 78.0)
        and (
          isinstance(last_candle["EMA_200_1h"], np.float64) and (last_candle["EMA_12_1h"] < last_candle["EMA_200_1h"])
        )
        and (
          isinstance(last_candle["EMA_200_4h"], np.float64) and (last_candle["EMA_12_4h"] < last_candle["EMA_200_4h"])
        )
        and (last_candle["KST_10_15_20_30_10_10_10_15_1h"] < last_candle["KSTs_9_1h"])
        and (last_candle["KST_10_15_20_30_10_10_10_15_4h"] < last_candle["KSTs_9_4h"])
      ):
        return True, f"exit_{mode_name}_d_1_1"
      elif (
        (last_candle["WILLR_14"] > -1.0)
        and (last_candle["RSI_14"] > 68.0)
        and (last_candle["CMF_20_1h"] < -0.0)
        and (
          isinstance(last_candle["EMA_200_1h"], np.float64) and (last_candle["EMA_12_1h"] < last_candle["EMA_200_1h"])
        )
        and (
          isinstance(last_candle["EMA_200_4h"], np.float64) and (last_candle["EMA_12_4h"] < last_candle["EMA_200_4h"])
        )
      ):
        return True, f"exit_{mode_name}_d_1_2"
      elif (
        (last_candle["WILLR_14"] > -8.0)
        and (last_candle["STOCHRSIk_14_14_3_3"] > 99.0)
        and (last_candle["CMF_20_1h"] < -0.0)
        and (last_candle["CMF_20_4h"] < -0.0)
        and (
          (last_candle["STOCHRSIk_14_14_3_3_4h"] > 20.0) and (last_candle["STOCHRSIk_14_14_3_3_change_pct_4h"] < -10.0)
        )
      ):
        return True, f"exit_{mode_name}_d_1_3"
      elif (
        (last_candle["WILLR_14"] > -30.0)
        and (last_candle["RSI_14"] > 65.0)
        and (last_candle["STOCHRSIk_14_14_3_3"] > 95.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 70.0)
        and (
          isinstance(last_candle["EMA_200_1h"], np.float64) and (last_candle["EMA_12_1h"] < last_candle["EMA_200_1h"])
        )
        and (
          isinstance(last_candle["EMA_200_4h"], np.float64) and (last_candle["EMA_12_4h"] < last_candle["EMA_200_4h"])
        )
      ):
        return True, f"exit_{mode_name}_d_1_4"
      elif (
        (last_candle["WILLR_14"] > -2.0)
        and (last_candle["RSI_14"] > 72.0)
        and (last_candle["ROC_9_1h"] < -5.0)
        and (last_candle["ROC_9_4h"] < -5.0)
      ):
        return True, f"exit_{mode_name}_d_1_5"
      elif (
        (last_candle["RSI_3"] > 70.0)
        and (last_candle["STOCHRSIk_14_14_3_3"] > 70.0)
        and (last_candle["RSI_14"] < 40.0)
        and (last_candle["ROC_9_1h"] < -10.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 50.0))
      ):
        return True, f"exit_{mode_name}_d_1_6"
      elif (
        (last_candle["RSI_14"] < 50.0)
        and (last_candle["STOCHRSIk_14_14_3_3"] > 70.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -40.0))
      ):
        return True, f"exit_{mode_name}_d_1_7"
      elif (
        (last_candle["WILLR_14"] > -2.0)
        and (last_candle["STOCHRSIk_14_14_3_3"] > 95.0)
        and (last_candle["CMF_20_1h"] < -0.1)
        and (last_candle["CMF_20_4h"] < -0.1)
        and (last_candle["change_pct_1d"] < -5.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 15.0))
      ):
        return True, f"exit_{mode_name}_d_1_8"
      elif (
        (last_candle["WILLR_14"] > -2.0)
        and (last_candle["RSI_3"] > 95.0)
        and (last_candle["change_pct_4h"] < -5.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 30.0))
      ):
        return True, f"exit_{mode_name}_d_1_9"
      elif (
        (last_candle["WILLR_14"] > -20.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["ROC_9_1h"] < -10.0)
        and (last_candle["ROC_9_4h"] < -10.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 10.0))
      ):
        return True, f"exit_{mode_name}_d_1_10"
      elif (
        (last_candle["RSI_3"] > 75.0)
        and (last_candle["RSI_14"] < 45.0)
        and (last_candle["ROC_9_15m"] < -10.0)
        and (last_candle["ROC_9_1h"] < -10.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -20.0))
      ):
        return True, f"exit_{mode_name}_d_1_11"
      elif (
        (last_candle["RSI_3"] > 95.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_4h"] < 10.0)
        and (last_candle["ROC_9_1h"] < -20.0)
        and (last_candle["ROC_9_4h"] < -20.0)
      ):
        return True, f"exit_{mode_name}_d_1_12"
      elif (last_candle["RSI_3"] > 80.0) and (last_candle["RSI_3_4h"] < 5.0) and (last_candle["ROC_9_4h"] < -25.0):
        return True, f"exit_{mode_name}_d_1_13"
      elif (
        (last_candle["RSI_3"] > 90.0)
        and (last_candle["WILLR_14"] > -4.0)
        and (last_candle["RSI_3_4h"] < 5.0)
        and (last_candle["AROONU_14_4h"] > 25.0)
      ):
        return True, f"exit_{mode_name}_d_1_14"
      elif (last_candle["RSI_3"] > 95.0) and (last_candle["RSI_14"] > 75.0) and (last_candle["ROC_9_4h"] < -30.0):
        return True, f"exit_{mode_name}_d_1_15"
      elif (
        (last_candle["RSI_3"] > 95.0)
        and (last_candle["AROONU_14_4h"] > 25.0)
        and (last_candle["ROC_9_4h"] < -25.0)
        and (last_candle["AROONU_14_1d"] > 50.0)
        and (last_candle["change_pct_1d"] < -15.0)
      ):
        return True, f"exit_{mode_name}_d_1_16"
      elif (
        (last_candle["RSI_3"] > 90.0)
        and (last_candle["WILLR_14"] > -10.0)
        and (last_candle["RSI_3_1h"] < 10.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 90.0)
        and (last_candle["ROC_9_4h"] > 30.0)
      ):
        return True, f"exit_{mode_name}_d_1_17"
      elif (
        (last_candle["RSI_3"] > 75.0)
        and (last_candle["RSI_14"] > 60.0)
        and (last_candle["RSI_3_4h"] < 20.0)
        and (last_candle["ROC_2_1d"] < -50.0)
      ):
        return True, f"exit_{mode_name}_d_1_18"
      elif (
        (last_candle["RSI_3"] > 95.0)
        and (last_candle["RSI_14"] > 72.0)
        and (last_candle["RSI_3_4h"] < 10.0)
        and (
          isinstance(last_candle["STOCHRSIk_14_14_3_3_1d"], np.float64)
          and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 70.0)
        )
      ):
        return True, f"exit_{mode_name}_d_1_19"
      elif (
        (last_candle["RSI_3"] > 50.0)
        and (last_candle["RSI_14"] < 40.0)
        and (last_candle["RSI_3_1h"] < 10.0)
        and (last_candle["AROONU_14_1h"] > 25.0)
      ):
        return True, f"exit_{mode_name}_d_1_20"
      elif (
        (last_candle["RSI_3"] > 80.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_1h"] < 20.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 90.0)
      ):
        return True, f"exit_{mode_name}_d_1_21"
      elif (
        (last_candle["RSI_3"] > 98.0)
        and (last_candle["WILLR_14"] > -2.0)
        and (last_candle["change_pct_4h"] < -5.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -30.0))
      ):
        return True, f"exit_{mode_name}_d_1_22"
      elif (
        (last_candle["RSI_3"] > 95.0)
        and (last_candle["WILLR_14"] > -10.0)
        and (last_candle["RSI_3_1h"] < 15.0)
        and (last_candle["RSI_3_1d"] < 5.0)
      ):
        return True, f"exit_{mode_name}_d_1_23"
      elif (
        (last_candle["RSI_3"] > 95.0)
        and (last_candle["RSI_14"] > 75.0)
        and (last_candle["WILLR_14"] > -10.0)
        and (last_candle["RSI_3_4h"] < 30.0)
        and (last_candle["AROONU_14_4h"] > 75.0)
      ):
        return True, f"exit_{mode_name}_d_1_24"
      elif (
        (last_candle["RSI_3"] > 90.0)
        and (last_candle["WILLR_14"] > -4.0)
        and (last_candle["RSI_3_4h"] < 10.0)
        and (last_candle["ROC_9_4h"] < -15.0)
        and (
          isinstance(last_candle["STOCHRSIk_14_14_3_3_1d"], np.float64)
          and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 50.0)
        )
      ):
        return True, f"exit_{mode_name}_d_1_25"
      elif (
        (last_candle["RSI_3"] > 85.0)
        and (last_candle["WILLR_14"] > -4.0)
        and (last_candle["RSI_3_4h"] < 15.0)
        and (last_candle["ROC_9_4h"] < -20.0)
      ):
        return True, f"exit_{mode_name}_d_1_26"
      elif (
        (last_candle["RSI_3"] > 65.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_1h"] < 20.0)
        and (last_candle["RSI_3_4h"] < 20.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 20.0)
      ):
        return True, f"exit_{mode_name}_d_1_27"
      elif (
        (last_candle["RSI_3"] > 80.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_15m"] < 10.0)
        and (last_candle["ROC_9_4h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_1_28"
      elif (
        (last_candle["RSI_3"] > 90.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_1h"] < 20.0)
        and (last_candle["RSI_3_4h"] < 20.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 30.0)
      ):
        return True, f"exit_{mode_name}_d_1_29"
      elif (
        (last_candle["RSI_3"] > 90.0)
        and (last_candle["RSI_3_1h"] < 25.0)
        and (last_candle["RSI_3_4h"] < 10.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 70.0)
      ):
        return True, f"exit_{mode_name}_d_1_30"
      elif (
        (last_candle["RSI_3"] > 80.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_1h"] < 15.0)
        and (last_candle["RSI_3_4h"] < 15.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 25.0)
      ):
        return True, f"exit_{mode_name}_d_1_31"
      elif (
        (last_candle["RSI_3"] > 90.0)
        and (last_candle["RSI_3_1h"] < 15.0)
        and (last_candle["ROC_2_4h"] < -30.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 30.0)
      ):
        return True, f"exit_{mode_name}_d_1_32"
      elif (
        (last_candle["RSI_3"] > 90.0)
        and (last_candle["WILLR_14"] > -2.0)
        and (last_candle["ROC_2_1h"] < -10.0)
        and (last_candle["ROC_9_1h"] > 30.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_1_33"
      elif (
        (last_candle["RSI_3"] > 65.0)
        and (last_candle["RSI_3_15m"] < 30.0)
        and (last_candle["RSI_14_1h"] > 80.0)
        and (last_candle["ROC_9_1h"] > 40.0)
      ):
        return True, f"exit_{mode_name}_d_1_34"
      elif (
        (last_candle["RSI_3"] > 88.0)
        and (last_candle["WILLR_14"] > -6.0)
        and (last_candle["RSI_3_1d"] < 25.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 75.0)
      ):
        return True, f"exit_{mode_name}_d_1_35"
      elif (
        (last_candle["RSI_3"] > 85.0)
        and (last_candle["WILLR_14"] > -15.0)
        and (last_candle["ROC_9_4h"] < -25.0)
        and (last_candle["RSI_3_1d"] < 25.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_1_36"
      elif (
        (last_candle["RSI_3"] > 82.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_1h"] < 20.0)
        and (last_candle["RSI_3_1d"] < 25.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_1_37"
      elif (
        (last_candle["RSI_3"] > 85.0)
        and (last_candle["WILLR_14"] > -15.0)
        and (last_candle["RSI_3_4h"] < 10.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 20.0)
      ):
        return True, f"exit_{mode_name}_d_1_38"
      elif (
        (last_candle["RSI_3"] > 95.0)
        and (last_candle["WILLR_14"] > -5.0)
        and (last_candle["CMF_20_4h"] < -0.0)
        and (last_candle["RSI_3_4h"] < 10.0)
      ):
        return True, f"exit_{mode_name}_d_1_39"
      elif (
        (last_candle["RSI_3"] > 85.0)
        and (last_candle["WILLR_14"] > -15.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 30.0)
        and (
          isinstance(last_candle["STOCHRSIk_14_14_3_3_1d"], np.float64)
          and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 90.0)
        )
      ):
        return True, f"exit_{mode_name}_d_1_40"
      elif (
        (last_candle["RSI_3"] > 95.0)
        and (last_candle["WILLR_14"] > -10.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 25.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 50.0))
      ):
        return True, f"exit_{mode_name}_d_1_41"
      elif (
        (last_candle["RSI_3"] > 90.0)
        and (last_candle["WILLR_14"] > -25.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 30.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 40.0))
        and (
          isinstance(last_candle["STOCHRSIk_14_14_3_3_1d"], np.float64)
          and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 70.0)
        )
      ):
        return True, f"exit_{mode_name}_d_1_42"
      elif (
        (last_candle["RSI_3"] > 80.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_1h"] < 15.0)
        and (last_candle["RSI_3_4h"] < 40.0)
        and (
          isinstance(last_candle["STOCHRSIk_14_14_3_3_1d"], np.float64)
          and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 90.0)
        )
      ):
        return True, f"exit_{mode_name}_d_1_43"
      elif (
        (last_candle["RSI_3"] > 65.0)
        and (last_candle["WILLR_14"] > -5.0)
        and (last_candle["RSI_3_4h"] < 30.0)
        and (last_candle["RSI_3_1d"] < 25.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -30.0))
      ):
        return True, f"exit_{mode_name}_d_1_44"
      elif (last_candle["RSI_3"] > 94.0) and (last_candle["WILLR_14"] > -6.0) and (last_candle["RSI_3_1h"] < 10.0):
        return True, f"exit_{mode_name}_d_1_45"
      elif (
        (last_candle["RSI_3"] > 70.0)
        and (last_candle["RSI_3_1h"] < 15.0)
        and (last_candle["RSI_3_4h"] < 10.0)
        and (last_candle["ROC_2_1d"] < -20.0)
      ):
        return True, f"exit_{mode_name}_d_1_46"
      elif (
        (last_candle["RSI_3"] > 86.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 80.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 40.0)
        and (last_candle["change_pct_1d"] < -5.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -5.0))
      ):
        return True, f"exit_{mode_name}_d_1_47"
      elif (
        (last_candle["RSI_3"] > 65.0)
        and (last_candle["RSI_14"] < 46.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (last_candle["RSI_3_4h"] < 20.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_1_48"
      elif (
        (last_candle["RSI_3"] > 90.0)
        and (last_candle["WILLR_14"] > -4.0)
        and (last_candle["RSI_3_4h"] < 20.0)
        and (last_candle["change_pct_1d"] < -5.0)
        and (
          isinstance(last_candle["STOCHRSIk_14_14_3_3_1d"], np.float64)
          and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 50.0)
        )
      ):
        return True, f"exit_{mode_name}_d_1_49"
      elif (
        (last_candle["RSI_3"] > 80.0)
        and (last_candle["WILLR_14"] > -4.0)
        and (last_candle["RSI_3_1d"] < 10.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 90.0)
      ):
        return True, f"exit_{mode_name}_d_1_50"
      elif (
        (last_candle["RSI_3"] > 66.0)
        and (last_candle["RSI_14"] < 46.0)
        and (last_candle["RSI_3_4h"] < 20.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_1_51"
      elif (
        (last_candle["RSI_3"] > 80.0)
        and (last_candle["RSI_14"] > 60.0)
        and (last_candle["WILLR_14"] > -10.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 70.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -15.0))
      ):
        return True, f"exit_{mode_name}_d_1_52"
      elif (
        (last_candle["RSI_3"] > 70.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["WILLR_14"] > -25.0)
        and (last_candle["RSI_3_1h"] < 20.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
        and (
          isinstance(last_candle["STOCHRSIk_14_14_3_3_1d"], np.float64)
          and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 50.0)
        )
      ):
        return True, f"exit_{mode_name}_d_1_53"
      elif (
        (last_candle["RSI_3"] > 78.0)
        and (last_candle["RSI_14"] < 46.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
        and (last_candle["ROC_9_4h"] < -10.0)
        and (last_candle["change_pct_1d"] < -10.0)
      ):
        return True, f"exit_{mode_name}_d_1_54"
      elif (
        (last_candle["RSI_3"] > 94.0)
        and (last_candle["WILLR_14"] > -14.0)
        and (last_candle["ROC_9_4h"] < -5.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 10.0))
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_1_55"
      elif (
        (last_candle["RSI_3"] > 60.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (last_candle["RSI_3_4h"] < 25.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -30.0))
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 10.0)
      ):
        return True, f"exit_{mode_name}_d_1_56"
      elif (
        (last_candle["RSI_3"] > 50.0)
        and (last_candle["RSI_14"] < 36.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -30.0))
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 70.0)
      ):
        return True, f"exit_{mode_name}_d_1_57"
      elif (
        (last_candle["RSI_3"] > 70.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (last_candle["RSI_3_4h"] < 30.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -15.0))
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_1_58"
      elif (
        (last_candle["RSI_3"] > 85.0)
        and (last_candle["WILLR_14"] > -12.0)
        and (last_candle["RSI_3_4h"] < 25.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -15.0))
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 40.0)
      ):
        return True, f"exit_{mode_name}_d_1_59"
      elif (
        (last_candle["RSI_3"] > 65.0)
        and (last_candle["RSI_14"] < 40.0)
        and (last_candle["RSI_14_4h"] > 65.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_1_60"
      elif (
        (last_candle["RSI_3"] > 90.0)
        and (last_candle["WILLR_14"] > -25.0)
        and (last_candle["RSI_3_4h"] < 10.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 30.0)
      ):
        return True, f"exit_{mode_name}_d_1_61"
      elif (
        (last_candle["RSI_3"] > 86.0)
        and (last_candle["WILLR_14"] > -2.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (last_candle["RSI_3_4h"] < 20.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 20.0))
        and (last_candle["change_pct_1d"] < -5.0)
      ):
        return True, f"exit_{mode_name}_d_1_62"
      elif (
        (last_candle["RSI_3"] > 68.0)
        and (last_candle["RSI_3_1d"] < 25.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 80.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 30.0)
      ):
        return True, f"exit_{mode_name}_d_1_63"
      elif (
        (last_candle["RSI_3"] > 88.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (last_candle["RSI_3_4h"] < 30.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 30.0))
      ):
        return True, f"exit_{mode_name}_d_1_64"
      elif (
        (last_candle["RSI_3"] > 68.0)
        and (last_candle["RSI_14"] < 42.0)
        and (last_candle["RSI_3_1h"] < 20.0)
        and (last_candle["RSI_3_4h"] < 15.0)
      ):
        return True, f"exit_{mode_name}_d_1_65"
      elif (
        (last_candle["RSI_3"] > 82.0)
        and (last_candle["RSI_14"] < 48.0)
        and (last_candle["RSI_3_1h"] < 20.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_1_66"
      elif (
        (last_candle["RSI_3"] > 50.0)
        and (last_candle["RSI_14"] < 42.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 80.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -25.0))
      ):
        return True, f"exit_{mode_name}_d_1_67"
      elif (
        (last_candle["RSI_3"] > 84.0)
        and (last_candle["RSI_14"] < 48.0)
        and (last_candle["RSI_3_1h"] < 25.0)
        and (last_candle["ROC_2_4h"] < -30.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 25.0)
      ):
        return True, f"exit_{mode_name}_d_1_68"
      elif (
        (last_candle["RSI_3"] > 96.0)
        and (last_candle["ROC_9_4h"] > 20.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
        and (last_candle["change_pct_4h"] < -5.0)
      ):
        return True, f"exit_{mode_name}_d_1_69"
      elif (
        (last_candle["RSI_3"] > 66.0)
        and (last_candle["RSI_14"] < 40.0)
        and (last_candle["RSI_3_1h"] < 25.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 20.0)
      ):
        return True, f"exit_{mode_name}_d_1_70"
      elif (
        (last_candle["RSI_3"] > 64.0)
        and (last_candle["RSI_14"] < 44.0)
        and (last_candle["RSI_3_4h"] < 25.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 20.0)
      ):
        return True, f"exit_{mode_name}_d_1_71"
      elif (
        (last_candle["RSI_3"] > 78.0)
        and (last_candle["RSI_14"] < 42.0)
        and (last_candle["RSI_3_1h"] < 10.0)
        and (last_candle["AROONU_14_4h"] > 25.0)
      ):
        return True, f"exit_{mode_name}_d_1_72"
      elif (
        (last_candle["RSI_3"] > 78.0)
        and (last_candle["RSI_3_1h"] < 25.0)
        and (last_candle["RSI_3_4h"] < 15.0)
        and (last_candle["ROC_9_4h"] < -20.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -25.0))
      ):
        return True, f"exit_{mode_name}_d_1_73"
      elif (
        (last_candle["RSI_3"] > 98.0)
        and (last_candle["WILLR_14"] > -10.0)
        and (last_candle["RSI_3_4h"] < 25.0)
        and (last_candle["RSI_3_1d"] < 25.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_1_74"
      elif (
        (last_candle["RSI_3"] > 96.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (last_candle["RSI_3_4h"] < 20.0)
        and (
          isinstance(last_candle["STOCHRSIk_14_14_3_3_1d"], np.float64)
          and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 50.0)
        )
      ):
        return True, f"exit_{mode_name}_d_1_75"
      elif (
        (last_candle["RSI_3"] > 68.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["ROC_9_1h"] > 80.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 80.0)
      ):
        return True, f"exit_{mode_name}_d_1_76"
      elif (
        (last_candle["RSI_3"] > 76.0)
        and (last_candle["RSI_14"] < 46.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 50.0))
      ):
        return True, f"exit_{mode_name}_d_1_77"
      elif (
        (last_candle["RSI_3"] > 86.0)
        and (last_candle["WILLR_14"] > -16.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (last_candle["RSI_3_4h"] < 20.0)
        and (last_candle["RSI_3_1d"] < 20.0)
      ):
        return True, f"exit_{mode_name}_d_1_78"
      elif (
        (last_candle["RSI_3"] > 92.0)
        and (last_candle["WILLR_14"] > -2.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (last_candle["RSI_3_4h"] < 10.0)
      ):
        return True, f"exit_{mode_name}_d_1_79"
      elif (
        (last_candle["RSI_3"] > 72.0)
        and (last_candle["RSI_14"] < 46.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 50.0))
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 25.0)
      ):
        return True, f"exit_{mode_name}_d_1_80"
      elif (
        (last_candle["RSI_3"] > 84.0)
        and (last_candle["WILLR_14"] > -10.0)
        and (last_candle["RSI_3_1h"] < 25.0)
        and (last_candle["RSI_3_4h"] < 25.0)
        and (isinstance(last_candle["RSI_14_1d"], np.float64) and (last_candle["RSI_14_1d"] > 50.0))
      ):
        return True, f"exit_{mode_name}_d_1_81"
      elif (
        (last_candle["RSI_3"] > 82.0)
        and (last_candle["WILLR_14"] > -10.0)
        and (last_candle["RSI_3_4h"] < 30.0)
        and (last_candle["RSI_3_1d"] < 15.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 40.0)
      ):
        return True, f"exit_{mode_name}_d_1_82"
      elif (
        (last_candle["RSI_3"] > 72.0)
        and (last_candle["RSI_14"] < 46.0)
        and (last_candle["RSI_3_1h"] < 40.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 40.0)
      ):
        return True, f"exit_{mode_name}_d_1_83"
      elif (
        (last_candle["RSI_3"] > 90.0)
        and (last_candle["WILLR_14"] > -2.0)
        and (last_candle["RSI_3_4h"] < 30.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 20.0)
      ):
        return True, f"exit_{mode_name}_d_1_84"
      elif (
        (last_candle["RSI_3"] > 88.0)
        and (last_candle["WILLR_14"] > -8.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (last_candle["RSI_3_4h"] < 40.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_1_85"
      elif (
        (last_candle["RSI_3"] > 94.0)
        and (last_candle["RSI_14_4h"] > 80.0)
        and (last_candle["ROC_2_1h"] < -5.0)
        and (last_candle["ROC_9_1h"] > 5.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_1_86"
      elif (
        (last_candle["RSI_3"] > 66.0)
        and (last_candle["RSI_14"] < 44.0)
        and (last_candle["RSI_3_1h"] < 45.0)
        and (last_candle["RSI_3_4h"] < 50.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_1_87"
      elif (
        (last_candle["RSI_3"] > 88.0)
        and (last_candle["WILLR_14"] > -20.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 40.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
        and (last_candle["change_pct_1h"] < -2.0)
      ):
        return True, f"exit_{mode_name}_d_1_88"
      elif (
        (last_candle["RSI_3"] > 78.0)
        and (last_candle["RSI_14"] < 40.0)
        and (last_candle["ROC_9_1h"] < -5.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 25.0))
      ):
        return True, f"exit_{mode_name}_d_1_89"
      elif (
        (last_candle["RSI_3"] > 92.0)
        and (last_candle["WILLR_14"] > -25.0)
        and (last_candle["RSI_3_1h"] < 50.0)
        and (last_candle["RSI_3_4h"] < 30.0)
        and (last_candle["AROONU_14_4h"] > 50.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 40.0))
      ):
        return True, f"exit_{mode_name}_d_1_90"
      elif (
        (last_candle["RSI_3"] > 72.0)
        and (last_candle["RSI_14"] < 46.0)
        and (last_candle["RSI_3_1h"] < 25.0)
        and (last_candle["RSI_3_4h"] < 25.0)
        and (last_candle["AROONU_14_4h"] > 50.0)
        and (
          isinstance(last_candle["STOCHRSIk_14_14_3_3_1d"], np.float64)
          and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 50.0)
        )
      ):
        return True, f"exit_{mode_name}_d_1_91"
      elif (
        (last_candle["RSI_3"] > 80.0)
        and (last_candle["RSI_14"] < 48.0)
        and (last_candle["RSI_3_1h"] < 40.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 25.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -25.0))
      ):
        return True, f"exit_{mode_name}_d_1_92"
      elif (
        (last_candle["RSI_3"] > 72.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_15m"] < 50.0)
        and (last_candle["AROONU_14_1h"] > 75.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 70.0)
        and (last_candle["AROONU_14_4h"] > 50.0)
        and (
          isinstance(last_candle["STOCHRSIk_14_14_3_3_1d"], np.float64)
          and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 90.0)
        )
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 30.0))
      ):
        return True, f"exit_{mode_name}_d_1_93"
      elif (
        (last_candle["RSI_3"] > 80.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_1h"] < 25.0)
        and (last_candle["RSI_3_4h"] < 45.0)
        and (last_candle["AROONU_14_1h"] > 75.0)
        and (
          isinstance(last_candle["STOCHRSIk_14_14_3_3_1d"], np.float64)
          and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 90.0)
        )
      ):
        return True, f"exit_{mode_name}_d_1_94"
      elif (
        (last_candle["RSI_3"] > 84.0)
        and (last_candle["WILLR_14"] > -12.0)
        and (last_candle["RSI_3_1h"] < 45.0)
        and (last_candle["RSI_3_4h"] < 40.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 10.0)
        and (isinstance(last_candle["AROONU_14_1d"], np.float64) and (last_candle["AROONU_14_1d"] > 75.0))
      ):
        return True, f"exit_{mode_name}_d_1_95"
      elif (
        (last_candle["RSI_3"] > 62.0)
        and (last_candle["RSI_14"] < 46.0)
        and (last_candle["RSI_3_1h"] < 45.0)
        and (last_candle["RSI_3_1d"] < 45.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_1_96"
      elif (
        (last_candle["RSI_3"] > 84.0)
        and (last_candle["RSI_14"] < 46.0)
        and (last_candle["RSI_3_1h"] < 35.0)
        and (last_candle["AROONU_14_4h"] > 50.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 30.0)
      ):
        return True, f"exit_{mode_name}_d_1_97"
      elif (
        (last_candle["RSI_3"] > 90.0)
        and (last_candle["RSI_3_15m"] > 72.0)
        and (last_candle["RSI_3_1h"] < 60.0)
        and (last_candle["RSI_3_4h"] < 60.0)
        and (last_candle["RSI_3_1d"] > 80.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_1_98"
      elif (
        (last_candle["RSI_3"] > 60.0)
        and (last_candle["RSI_14"] < 52.0)
        and (last_candle["RSI_3_1h"] < 65.0)
        and (last_candle["RSI_3_4h"] < 60.0)
        and (last_candle["AROONU_14_4h"] > 50.0)
        and (last_candle["STOCHk_14_3_3_4h"] > 40.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 80.0))
      ):
        return True, f"exit_{mode_name}_d_1_99"
      elif (
        (last_candle["RSI_3"] > 98.0)
        and (last_candle["RSI_14"] > 76.0)
        and (last_candle["RSI_3_15m"] > 70.0)
        and (last_candle["RSI_3_4h"] < 80.0)
      ):
        return True, f"exit_{mode_name}_d_1_100"
      elif (
        (last_candle["RSI_3"] > 84.0)
        and (last_candle["WILLR_14"] > -16.0)
        and (last_candle["RSI_3_1h"] < 50.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 40.0)
        and (isinstance(last_candle["ROC_9_4h"], np.float64) and (last_candle["ROC_9_4h"] > 40.0))
      ):
        return True, f"exit_{mode_name}_d_1_101"
      elif (
        (last_candle["RSI_3"] > 68.0)
        and (last_candle["RSI_14"] < 48.0)
        and (last_candle["RSI_3_1h"] < 60.0)
        and (last_candle["RSI_3_4h"] < 40.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 30.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 40.0))
      ):
        return True, f"exit_{mode_name}_d_1_102"
      elif (
        (last_candle["RSI_3"] > 78.0)
        and (last_candle["RSI_14"] < 56.0)
        and (last_candle["RSI_3_1h"] < 60.0)
        and (last_candle["RSI_14_4h"] > 70.0)
        and (isinstance(last_candle["ROC_9_4h"], np.float64) and (last_candle["ROC_9_4h"] > 80.0))
      ):
        return True, f"exit_{mode_name}_d_1_103"
      elif (
        (last_candle["RSI_3"] > 64.0)
        and (last_candle["RSI_14"] < 48.0)
        and (last_candle["RSI_3_1h"] < 60.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 40.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 90.0)
        and (last_candle["ROC_9_4h"] > 40.0)
      ):
        return True, f"exit_{mode_name}_d_1_104"
      elif (
        (last_candle["RSI_3"] > 78.0)
        and (last_candle["RSI_14"] < 48.0)
        and (last_candle["RSI_3_15m"] < 55.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 90.0)
        and (last_candle["ROC_9_4h"] > 25.0)
      ):
        return True, f"exit_{mode_name}_d_1_105"
      elif (
        (last_candle["RSI_3"] > 72.0)
        and (last_candle["RSI_14"] < 48.0)
        and (last_candle["RSI_3_1h"] < 50.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
        and (last_candle["RSI_14_4h"] > 70.0)
        and (last_candle["ROC_9_4h"] > 40.0)
      ):
        return True, f"exit_{mode_name}_d_1_106"
      elif (
        (last_candle["RSI_3"] > 74.0)
        and (last_candle["RSI_14"] < 48.0)
        and (last_candle["RSI_3_1h"] < 50.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 70.0)
        and (last_candle["RSI_14_4h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_1_107"
      elif (
        (last_candle["RSI_3"] > 56.0)
        and (last_candle["RSI_14"] < 48.0)
        and (last_candle["RSI_3_1h"] < 60.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 80.0)
      ):
        return True, f"exit_{mode_name}_d_1_108"
      elif (
        (last_candle["RSI_3"] > 76.0)
        and (last_candle["WILLR_14"] > -8.0)
        and (last_candle["RSI_3_1h"] < 50.0)
        and (last_candle["RSI_3_4h"] < 20.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 50.0))
      ):
        return True, f"exit_{mode_name}_d_1_109"
      elif (
        (last_candle["RSI_3"] > 72.0)
        and (last_candle["RSI_3_4h"] < 65.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
        and (last_candle["ROC_9_4h"] > 25.0)
      ):
        return True, f"exit_{mode_name}_d_1_110"
      elif (
        (last_candle["RSI_3"] > 50.0)
        and (last_candle["RSI_14"] < 44.0)
        and (last_candle["RSI_3_1h"] < 50.0)
        and (last_candle["RSI_14_4h"] > 70.0)
        and (last_candle["AROONU_14_1h"] > 75.0)
        and (last_candle["AROONU_14_4h"] > 75.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 20.0))
      ):
        return True, f"exit_{mode_name}_d_1_111"
      elif (
        (last_candle["RSI_3"] > 80.0)
        and (last_candle["WILLR_14"] > -25.0)
        and (last_candle["RSI_14"] < 52.0)
        and (last_candle["RSI_3_1h"] < 35.0)
        and (last_candle["RSI_3_4h"] < 35.0)
        and (last_candle["RSI_3_1d"] < 60.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 30.0))
      ):
        return True, f"exit_{mode_name}_d_1_112"
      elif (
        (last_candle["RSI_3"] > 84.0)
        and (last_candle["WILLR_14"] > -2.0)
        and (last_candle["RSI_3_1d"] < 30.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
        and (isinstance(last_candle["ROC_9_4h"], np.float64) and (last_candle["ROC_9_4h"] > 10.0))
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -10.0))
      ):
        return True, f"exit_{mode_name}_d_1_113"
      elif (
        (last_candle["RSI_3"] > 84.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_1h"] < 20.0)
        and (last_candle["RSI_3_4h"] < 30.0)
        and (last_candle["RSI_3_1d"] < 30.0)
      ):
        return True, f"exit_{mode_name}_d_1_114"
      elif (
        (last_candle["RSI_3"] > 78.0)
        and (last_candle["RSI_14"] < 48.0)
        and (last_candle["RSI_3_15m"] < 30.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_1_115"
      elif (
        (last_candle["RSI_3"] > 90.0)
        and (last_candle["RSI_3_1h"] < 15.0)
        and (last_candle["RSI_3_4h"] < 40.0)
        and (last_candle["AROONU_14_4h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_1_116"
      elif (
        (last_candle["RSI_3"] > 86.0)
        and (last_candle["RSI_3_1h"] < 50.0)
        and (last_candle["AROONU_14_1h"] > 80.0)
        and (last_candle["AROONU_14_4h"] > 80.0)
      ):
        return True, f"exit_{mode_name}_d_1_117"
      elif (
        (last_candle["RSI_3"] > 90.0)
        and (last_candle["RSI_3_1h"] < 20.0)
        and (last_candle["RSI_3_4h"] < 60.0)
        and (last_candle["AROONU_14_4h"] > 40.0)
      ):
        return True, f"exit_{mode_name}_d_1_118"
      elif (
        (last_candle["RSI_3"] > 86.0)
        and (last_candle["WILLR_14"] > -20.0)
        and (last_candle["RSI_3_1h"] < 60.0)
        and (last_candle["RSI_3_4h"] < 60.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 40.0)
      ):
        return True, f"exit_{mode_name}_d_1_119"
      elif (
        (last_candle["RSI_3"] > 54.0)
        and (last_candle["RSI_14"] < 48.0)
        and (last_candle["RSI_3_1h"] < 40.0)
        and (last_candle["AROONU_14_4h"] > 75.0)
      ):
        return True, f"exit_{mode_name}_d_1_120"
      elif (
        (last_candle["RSI_3"] > 60.0)
        and (last_candle["RSI_14"] < 46.0)
        and (last_candle["RSI_3_1h"] < 50.0)
        and (last_candle["RSI_14_4h"] > 85.0)
      ):
        return True, f"exit_{mode_name}_d_1_121"
      elif (
        (last_candle["RSI_3"] > 58.0)
        and (last_candle["RSI_14"] < 44.0)
        and (last_candle["RSI_3_4h"] < 30.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_1_122"
      elif (
        (last_candle["RSI_3"] > 88.0)
        and (last_candle["WILLR_14"] > -4.0)
        and (last_candle["RSI_3_1h"] < 10.0)
        and (last_candle["RSI_3_1d"] < 30.0)
      ):
        return True, f"exit_{mode_name}_d_1_123"
      elif (
        (last_candle["RSI_3"] > 88.0)
        and (last_candle["RSI_3_1h"] < 15.0)
        and (
          isinstance(last_candle["STOCHRSIk_14_14_3_3_1d"], np.float64)
          and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 80.0)
        )
      ):
        return True, f"exit_{mode_name}_d_1_124"
      elif (
        (last_candle["RSI_3"] > 76.0)
        and (last_candle["WILLR_14"] > -4.0)
        and (last_candle["RSI_3_1h"] < 10.0)
        and (last_candle["RSI_3_4h"] < 40.0)
        and (last_candle["RSI_3_1d"] < 40.0)
        and (last_candle["close"] < (last_candle["high_max_30_1d"] * 0.50))
      ):
        return True, f"exit_{mode_name}_d_1_125"
      elif (
        (last_candle["RSI_3"] > 90.0)
        and (last_candle["RSI_3_1h"] < 15.0)
        and (last_candle["RSI_3_4h"] < 40.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_1_126"
      elif (
        (last_candle["RSI_3"] > 90.0)
        and (last_candle["RSI_3_1h"] < 10.0)
        and (last_candle["RSI_3_4h"] < 30.0)
        and (last_candle["RSI_3_1d"] < 40.0)
      ):
        return True, f"exit_{mode_name}_d_1_127"
      elif (last_candle["RSI_3"] > 94.0) and (last_candle["RSI_3_4h"] < 30.0) and (last_candle["AROONU_14_4h"] > 85.0):
        return True, f"exit_{mode_name}_d_1_128"
      elif (
        (last_candle["RSI_3"] > 86.0)
        and (last_candle["RSI_3_4h"] < 25.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 80.0))
      ):
        return True, f"exit_{mode_name}_d_1_129"
      elif (
        (last_candle["RSI_3"] > 74.0)
        and (last_candle["RSI_14_1h"] > 65.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 80.0)
        and (last_candle["CCI_20_change_pct_1h"] < -0.0)
      ):
        return True, f"exit_{mode_name}_d_1_130"
      elif (
        (last_candle["RSI_14"] < 38.0)
        and (last_candle["RSI_3_1h"] < 20.0)
        and (last_candle["RSI_3_4h"] < 30.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_1_131"
      elif (
        (last_candle["RSI_3"] > 80.0)
        and (last_candle["RSI_3_1h"] < 35.0)
        and (last_candle["RSI_3_4h"] < 35.0)
        and (last_candle["AROONU_14_1h"] > 50.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 40.0)
      ):
        return True, f"exit_{mode_name}_d_1_132"
      elif (
        (last_candle["RSI_3"] > 80.0)
        and (last_candle["AROONU_14_15m"] > 75.0)
        and (last_candle["AROONU_14_1h"] > 75.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 25.0))
      ):
        return True, f"exit_{mode_name}_d_1_133"
    elif 0.03 > current_profit >= 0.02:
      if (
        (last_candle["WILLR_14"] > -1.0)
        and (last_candle["RSI_14"] > 78.0)
        and (
          isinstance(last_candle["EMA_200_1h"], np.float64) and (last_candle["EMA_12_1h"] < last_candle["EMA_200_1h"])
        )
        and (
          isinstance(last_candle["EMA_200_4h"], np.float64) and (last_candle["EMA_12_4h"] < last_candle["EMA_200_4h"])
        )
        and (last_candle["KST_10_15_20_30_10_10_10_15_1h"] < last_candle["KSTs_9_1h"])
        and (last_candle["KST_10_15_20_30_10_10_10_15_4h"] < last_candle["KSTs_9_4h"])
      ):
        return True, f"exit_{mode_name}_d_2_1"
      elif (
        (last_candle["WILLR_14"] > -1.0)
        and (last_candle["RSI_14"] > 66.0)
        and (last_candle["CMF_20_1h"] < -0.0)
        and (
          isinstance(last_candle["EMA_200_1h"], np.float64) and (last_candle["EMA_12_1h"] < last_candle["EMA_200_1h"])
        )
        and (
          isinstance(last_candle["EMA_200_4h"], np.float64) and (last_candle["EMA_12_4h"] < last_candle["EMA_200_4h"])
        )
      ):
        return True, f"exit_{mode_name}_d_2_2"
      elif (
        (last_candle["WILLR_14"] > -10.0)
        and (last_candle["STOCHRSIk_14_14_3_3"] > 99.0)
        and (last_candle["CMF_20_1h"] < -0.0)
        and (last_candle["CMF_20_4h"] < -0.0)
        and (
          (last_candle["STOCHRSIk_14_14_3_3_4h"] > 20.0) and (last_candle["STOCHRSIk_14_14_3_3_change_pct_4h"] < -10.0)
        )
      ):
        return True, f"exit_{mode_name}_d_2_3"
      elif (
        (last_candle["WILLR_14"] > -30.0)
        and (last_candle["RSI_14"] > 65.0)
        and (last_candle["STOCHRSIk_14_14_3_3"] > 95.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 70.0)
        and (
          isinstance(last_candle["EMA_200_1h"], np.float64) and (last_candle["EMA_12_1h"] < last_candle["EMA_200_1h"])
        )
        and (
          isinstance(last_candle["EMA_200_4h"], np.float64) and (last_candle["EMA_12_4h"] < last_candle["EMA_200_4h"])
        )
      ):
        return True, f"exit_{mode_name}_d_2_4"
      elif (
        (last_candle["WILLR_14"] > -4.0)
        and (last_candle["RSI_14"] > 70.0)
        and (last_candle["ROC_9_1h"] < -5.0)
        and (last_candle["ROC_9_4h"] < -5.0)
      ):
        return True, f"exit_{mode_name}_d_2_5"
      elif (
        (last_candle["RSI_3"] > 70.0)
        and (last_candle["STOCHRSIk_14_14_3_3"] > 70.0)
        and (last_candle["RSI_14"] < 40.0)
        and (last_candle["ROC_9_1h"] < -10.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 50.0))
      ):
        return True, f"exit_{mode_name}_d_2_6"
      elif (
        (last_candle["RSI_14"] < 50.0)
        and (last_candle["STOCHRSIk_14_14_3_3"] > 70.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -40.0))
      ):
        return True, f"exit_{mode_name}_d_2_7"
      elif (
        (last_candle["WILLR_14"] > -4.0)
        and (last_candle["STOCHRSIk_14_14_3_3"] > 95.0)
        and (last_candle["CMF_20_1h"] < -0.1)
        and (last_candle["CMF_20_4h"] < -0.1)
        and (last_candle["change_pct_1d"] < -5.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 15.0))
      ):
        return True, f"exit_{mode_name}_d_2_8"
      elif (
        (last_candle["WILLR_14"] > -4.0)
        and (last_candle["RSI_3"] > 95.0)
        and (last_candle["change_pct_4h"] < -5.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 30.0))
      ):
        return True, f"exit_{mode_name}_d_2_9"
      elif (
        (last_candle["WILLR_14"] > -20.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["ROC_9_1h"] < -10.0)
        and (last_candle["ROC_9_4h"] < -10.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 10.0))
      ):
        return True, f"exit_{mode_name}_d_2_10"
      elif (
        (last_candle["RSI_3"] > 75.0)
        and (last_candle["RSI_14"] < 45.0)
        and (last_candle["ROC_9_15m"] < -10.0)
        and (last_candle["ROC_9_1h"] < -10.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -20.0))
      ):
        return True, f"exit_{mode_name}_d_2_11"
      elif (
        (last_candle["RSI_3"] > 80.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_4h"] < 10.0)
        and (last_candle["ROC_9_1h"] < -20.0)
        and (last_candle["ROC_9_4h"] < -20.0)
      ):
        return True, f"exit_{mode_name}_d_2_12"
      elif (last_candle["RSI_3"] > 80.0) and (last_candle["RSI_3_4h"] < 5.0) and (last_candle["ROC_9_4h"] < -25.0):
        return True, f"exit_{mode_name}_d_2_13"
      elif (
        (last_candle["RSI_3"] > 90.0)
        and (last_candle["WILLR_14"] > -6.0)
        and (last_candle["RSI_3_4h"] < 5.0)
        and (last_candle["AROONU_14_4h"] > 25.0)
      ):
        return True, f"exit_{mode_name}_d_2_14"
      elif (last_candle["RSI_3"] > 92.0) and (last_candle["RSI_14"] > 70.0) and (last_candle["ROC_9_4h"] < -30.0):
        return True, f"exit_{mode_name}_d_2_15"
      elif (
        (last_candle["RSI_3"] > 70.0)
        and (last_candle["AROONU_14_4h"] > 25.0)
        and (last_candle["ROC_9_4h"] < -25.0)
        and (last_candle["AROONU_14_1d"] > 50.0)
        and (last_candle["change_pct_1d"] < -15.0)
      ):
        return True, f"exit_{mode_name}_d_2_16"
      elif (
        (last_candle["RSI_3"] > 80.0)
        and (last_candle["WILLR_14"] > -20.0)
        and (last_candle["RSI_3_1h"] < 10.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 90.0)
        and (last_candle["ROC_9_4h"] > 30.0)
      ):
        return True, f"exit_{mode_name}_d_2_17"
      elif (
        (last_candle["RSI_3"] > 75.0)
        and (last_candle["RSI_14"] > 60.0)
        and (last_candle["RSI_3_4h"] < 20.0)
        and (last_candle["ROC_2_1d"] < -50.0)
      ):
        return True, f"exit_{mode_name}_d_2_18"
      elif (
        (last_candle["RSI_3"] > 90.0)
        and (last_candle["RSI_14"] > 70.0)
        and (last_candle["RSI_3_4h"] < 10.0)
        and (
          isinstance(last_candle["STOCHRSIk_14_14_3_3_1d"], np.float64)
          and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 70.0)
        )
      ):
        return True, f"exit_{mode_name}_d_2_19"
      elif (
        (last_candle["RSI_3"] > 48.0)
        and (last_candle["RSI_14"] < 42.0)
        and (last_candle["RSI_3_1h"] < 10.0)
        and (last_candle["AROONU_14_1h"] > 25.0)
      ):
        return True, f"exit_{mode_name}_d_2_20"
      elif (
        (last_candle["RSI_3"] > 70.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_1h"] < 20.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 90.0)
      ):
        return True, f"exit_{mode_name}_d_2_21"
      elif (
        (last_candle["RSI_3"] > 96.0)
        and (last_candle["WILLR_14"] > -4.0)
        and (last_candle["change_pct_4h"] < -5.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -30.0))
      ):
        return True, f"exit_{mode_name}_d_2_22"
      elif (
        (last_candle["RSI_3"] > 90.0)
        and (last_candle["WILLR_14"] > -15.0)
        and (last_candle["RSI_3_1h"] < 15.0)
        and (last_candle["RSI_3_1d"] < 5.0)
      ):
        return True, f"exit_{mode_name}_d_2_23"
      elif (
        (last_candle["RSI_3"] > 90.0)
        and (last_candle["RSI_14"] > 70.0)
        and (last_candle["WILLR_14"] > -20.0)
        and (last_candle["RSI_3_4h"] < 30.0)
        and (last_candle["AROONU_14_4h"] > 75.0)
      ):
        return True, f"exit_{mode_name}_d_2_24"
      elif (
        (last_candle["RSI_3"] > 85.0)
        and (last_candle["WILLR_14"] > -6.0)
        and (last_candle["RSI_3_4h"] < 10.0)
        and (last_candle["ROC_9_4h"] < -15.0)
        and (
          isinstance(last_candle["STOCHRSIk_14_14_3_3_1d"], np.float64)
          and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 50.0)
        )
      ):
        return True, f"exit_{mode_name}_d_2_25"
      elif (
        (last_candle["RSI_3"] > 80.0)
        and (last_candle["WILLR_14"] > -6.0)
        and (last_candle["RSI_3_4h"] < 15.0)
        and (last_candle["ROC_9_4h"] < -20.0)
      ):
        return True, f"exit_{mode_name}_d_2_26"
      elif (
        (last_candle["RSI_3"] > 65.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_1h"] < 20.0)
        and (last_candle["RSI_3_4h"] < 20.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 20.0)
      ):
        return True, f"exit_{mode_name}_d_2_27"
      elif (
        (last_candle["RSI_3"] > 75.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_15m"] < 10.0)
        and (last_candle["ROC_9_4h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_2_28"
      elif (
        (last_candle["RSI_3"] > 75.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_1h"] < 20.0)
        and (last_candle["RSI_3_4h"] < 20.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 30.0)
      ):
        return True, f"exit_{mode_name}_d_2_29"
      elif (
        (last_candle["RSI_3"] > 85.0)
        and (last_candle["RSI_3_1h"] < 25.0)
        and (last_candle["RSI_3_4h"] < 10.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 70.0)
      ):
        return True, f"exit_{mode_name}_d_2_30"
      elif (
        (last_candle["RSI_3"] > 75.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_1h"] < 15.0)
        and (last_candle["RSI_3_4h"] < 15.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 25.0)
      ):
        return True, f"exit_{mode_name}_d_2_31"
      elif (
        (last_candle["RSI_3"] > 85.0)
        and (last_candle["RSI_3_1h"] < 15.0)
        and (last_candle["ROC_2_4h"] < -30.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 30.0)
      ):
        return True, f"exit_{mode_name}_d_2_32"
      elif (
        (last_candle["RSI_3"] > 85.0)
        and (last_candle["WILLR_14"] > -4.0)
        and (last_candle["ROC_2_1h"] < -10.0)
        and (last_candle["ROC_9_1h"] > 30.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_2_33"
      elif (
        (last_candle["RSI_3"] > 65.0)
        and (last_candle["RSI_3_15m"] < 30.0)
        and (last_candle["RSI_14_1h"] > 80.0)
        and (last_candle["ROC_9_1h"] > 40.0)
      ):
        return True, f"exit_{mode_name}_d_2_34"
      elif (
        (last_candle["RSI_3"] > 86.0)
        and (last_candle["WILLR_14"] > -7.0)
        and (last_candle["RSI_3_1d"] < 25.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 75.0)
      ):
        return True, f"exit_{mode_name}_d_2_35"
      elif (
        (last_candle["RSI_3"] > 80.0)
        and (last_candle["WILLR_14"] > -20.0)
        and (last_candle["ROC_9_4h"] < -25.0)
        and (last_candle["RSI_3_1d"] < 25.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_2_36"
      elif (
        (last_candle["RSI_3"] > 80.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_1h"] < 20.0)
        and (last_candle["RSI_3_1d"] < 25.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_2_37"
      elif (
        (last_candle["RSI_3"] > 80.0)
        and (last_candle["WILLR_14"] > -20.0)
        and (last_candle["RSI_3_4h"] < 10.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 20.0)
      ):
        return True, f"exit_{mode_name}_d_2_38"
      elif (
        (last_candle["RSI_3"] > 94.0)
        and (last_candle["WILLR_14"] > -6.0)
        and (last_candle["CMF_20_4h"] < -0.0)
        and (last_candle["RSI_3_4h"] < 10.0)
      ):
        return True, f"exit_{mode_name}_d_2_39"
      elif (
        (last_candle["RSI_3"] > 80.0)
        and (last_candle["WILLR_14"] > -20.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 30.0)
        and (
          isinstance(last_candle["STOCHRSIk_14_14_3_3_1d"], np.float64)
          and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 90.0)
        )
      ):
        return True, f"exit_{mode_name}_d_2_40"
      elif (
        (last_candle["RSI_3"] > 90.0)
        and (last_candle["WILLR_14"] > -15.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 25.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 50.0))
      ):
        return True, f"exit_{mode_name}_d_2_41"
      elif (
        (last_candle["RSI_3"] > 85.0)
        and (last_candle["WILLR_14"] > -30.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 30.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 40.0))
        and (
          isinstance(last_candle["STOCHRSIk_14_14_3_3_1d"], np.float64)
          and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 70.0)
        )
      ):
        return True, f"exit_{mode_name}_d_2_42"
      elif (
        (last_candle["RSI_3"] > 80.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_1h"] < 15.0)
        and (last_candle["RSI_3_4h"] < 40.0)
        and (
          isinstance(last_candle["STOCHRSIk_14_14_3_3_1d"], np.float64)
          and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 90.0)
        )
      ):
        return True, f"exit_{mode_name}_d_2_43"
      elif (
        (last_candle["RSI_3"] > 60.0)
        and (last_candle["WILLR_14"] > -10.0)
        and (last_candle["RSI_3_4h"] < 30.0)
        and (last_candle["RSI_3_1d"] < 25.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -30.0))
      ):
        return True, f"exit_{mode_name}_d_2_44"
      elif (last_candle["RSI_3"] > 92.0) and (last_candle["WILLR_14"] > -8.0) and (last_candle["RSI_3_1h"] < 10.0):
        return True, f"exit_{mode_name}_d_2_45"
      elif (
        (last_candle["RSI_3"] > 70.0)
        and (last_candle["RSI_3_1h"] < 15.0)
        and (last_candle["RSI_3_4h"] < 10.0)
        and (last_candle["ROC_2_1d"] < -20.0)
      ):
        return True, f"exit_{mode_name}_d_2_46"
      elif (
        (last_candle["RSI_3"] > 84.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 80.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 40.0)
        and (last_candle["change_pct_1d"] < -5.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -5.0))
      ):
        return True, f"exit_{mode_name}_d_2_47"
      elif (
        (last_candle["RSI_3"] > 60.0)
        and (last_candle["RSI_14"] < 46.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (last_candle["RSI_3_4h"] < 20.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_2_48"
      elif (
        (last_candle["RSI_3"] > 85.0)
        and (last_candle["WILLR_14"] > -6.0)
        and (last_candle["RSI_3_4h"] < 20.0)
        and (last_candle["change_pct_1d"] < -5.0)
        and (
          isinstance(last_candle["STOCHRSIk_14_14_3_3_1d"], np.float64)
          and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 50.0)
        )
      ):
        return True, f"exit_{mode_name}_d_2_49"
      elif (
        (last_candle["RSI_3"] > 80.0)
        and (last_candle["WILLR_14"] > -6.0)
        and (last_candle["RSI_3_1d"] < 10.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 90.0)
      ):
        return True, f"exit_{mode_name}_d_2_50"
      elif (
        (last_candle["RSI_3"] > 64.0)
        and (last_candle["RSI_14"] < 48.0)
        and (last_candle["RSI_3_4h"] < 20.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_2_51"
      elif (
        (last_candle["RSI_3"] > 78.0)
        and (last_candle["RSI_14"] > 58.0)
        and (last_candle["WILLR_14"] > -10.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 70.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -15.0))
      ):
        return True, f"exit_{mode_name}_d_2_52"
      elif (
        (last_candle["RSI_3"] > 70.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["WILLR_14"] > -25.0)
        and (last_candle["RSI_3_1h"] < 20.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
        and (
          isinstance(last_candle["STOCHRSIk_14_14_3_3_1d"], np.float64)
          and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 50.0)
        )
      ):
        return True, f"exit_{mode_name}_d_2_53"
      elif (
        (last_candle["RSI_3"] > 76.0)
        and (last_candle["RSI_14"] < 48.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
        and (last_candle["ROC_9_4h"] < -10.0)
        and (last_candle["change_pct_1d"] < -10.0)
      ):
        return True, f"exit_{mode_name}_d_2_54"
      elif (
        (last_candle["RSI_3"] > 92.0)
        and (last_candle["WILLR_14"] > -16.0)
        and (last_candle["ROC_9_4h"] < -5.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 10.0))
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_2_55"
      elif (
        (last_candle["RSI_3"] > 60.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (last_candle["RSI_3_4h"] < 25.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -30.0))
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 10.0)
      ):
        return True, f"exit_{mode_name}_d_2_56"
      elif (
        (last_candle["RSI_3"] > 50.0)
        and (last_candle["RSI_14"] < 38.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -30.0))
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 70.0)
      ):
        return True, f"exit_{mode_name}_d_2_57"
      elif (
        (last_candle["RSI_3"] > 70.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (last_candle["RSI_3_4h"] < 30.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -15.0))
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_2_58"
      elif (
        (last_candle["RSI_3"] > 85.0)
        and (last_candle["WILLR_14"] > -14.0)
        and (last_candle["RSI_3_4h"] < 25.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -15.0))
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 40.0)
      ):
        return True, f"exit_{mode_name}_d_2_59"
      elif (
        (last_candle["RSI_3"] > 65.0)
        and (last_candle["RSI_14"] < 42.0)
        and (last_candle["RSI_14_4h"] > 65.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_2_60"
      elif (
        (last_candle["RSI_3"] > 90.0)
        and (last_candle["WILLR_14"] > -25.0)
        and (last_candle["RSI_3_4h"] < 10.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 30.0)
      ):
        return True, f"exit_{mode_name}_d_2_61"
      elif (
        (last_candle["RSI_3"] > 84.0)
        and (last_candle["WILLR_14"] > -4.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (last_candle["RSI_3_4h"] < 20.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 20.0))
        and (last_candle["change_pct_1d"] < -5.0)
      ):
        return True, f"exit_{mode_name}_d_2_62"
      elif (
        (last_candle["RSI_3"] > 66.0)
        and (last_candle["RSI_3_1d"] < 25.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 80.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 30.0)
      ):
        return True, f"exit_{mode_name}_d_2_63"
      elif (
        (last_candle["RSI_3"] > 86.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (last_candle["RSI_3_4h"] < 30.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 30.0))
      ):
        return True, f"exit_{mode_name}_d_2_64"
      elif (
        (last_candle["RSI_3"] > 66.0)
        and (last_candle["RSI_14"] < 44.0)
        and (last_candle["RSI_3_1h"] < 20.0)
        and (last_candle["RSI_3_4h"] < 15.0)
      ):
        return True, f"exit_{mode_name}_d_2_65"
      elif (
        (last_candle["RSI_3"] > 80.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_1h"] < 20.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_2_66"
      elif (
        (last_candle["RSI_3"] > 50.0)
        and (last_candle["RSI_14"] < 44.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 80.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -25.0))
      ):
        return True, f"exit_{mode_name}_d_2_67"
      elif (
        (last_candle["RSI_3"] > 82.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_1h"] < 25.0)
        and (last_candle["ROC_2_4h"] < -30.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 25.0)
      ):
        return True, f"exit_{mode_name}_d_2_68"
      elif (
        (last_candle["RSI_3"] > 95.0)
        and (last_candle["ROC_9_4h"] > 20.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
        and (last_candle["change_pct_4h"] < -5.0)
      ):
        return True, f"exit_{mode_name}_d_2_69"
      elif (
        (last_candle["RSI_3"] > 64.0)
        and (last_candle["RSI_14"] < 42.0)
        and (last_candle["RSI_3_1h"] < 25.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 20.0)
      ):
        return True, f"exit_{mode_name}_d_2_70"
      elif (
        (last_candle["RSI_3"] > 62.0)
        and (last_candle["RSI_14"] < 46.0)
        and (last_candle["RSI_3_4h"] < 25.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 20.0)
      ):
        return True, f"exit_{mode_name}_d_2_71"
      elif (
        (last_candle["RSI_3"] > 76.0)
        and (last_candle["RSI_14"] < 44.0)
        and (last_candle["RSI_3_1h"] < 10.0)
        and (last_candle["AROONU_14_4h"] > 25.0)
      ):
        return True, f"exit_{mode_name}_d_2_72"
      elif (
        (last_candle["RSI_3"] > 76.0)
        and (last_candle["RSI_3_1h"] < 25.0)
        and (last_candle["RSI_3_4h"] < 15.0)
        and (last_candle["ROC_9_4h"] < -20.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -25.0))
      ):
        return True, f"exit_{mode_name}_d_2_73"
      elif (
        (last_candle["RSI_3"] > 97.0)
        and (last_candle["WILLR_14"] > -10.0)
        and (last_candle["RSI_3_4h"] < 25.0)
        and (last_candle["RSI_3_1d"] < 25.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_2_74"
      elif (
        (last_candle["RSI_3"] > 94.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (last_candle["RSI_3_4h"] < 20.0)
        and (
          isinstance(last_candle["STOCHRSIk_14_14_3_3_1d"], np.float64)
          and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 50.0)
        )
      ):
        return True, f"exit_{mode_name}_d_2_75"
      elif (
        (last_candle["RSI_3"] > 66.0)
        and (last_candle["RSI_14"] < 52.0)
        and (last_candle["ROC_9_1h"] > 80.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 80.0)
      ):
        return True, f"exit_{mode_name}_d_2_76"
      elif (
        (last_candle["RSI_3"] > 74.0)
        and (last_candle["RSI_14"] < 48.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 50.0))
      ):
        return True, f"exit_{mode_name}_d_2_77"
      elif (
        (last_candle["RSI_3"] > 84.0)
        and (last_candle["WILLR_14"] > -18.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (last_candle["RSI_3_4h"] < 20.0)
        and (last_candle["RSI_3_1d"] < 20.0)
      ):
        return True, f"exit_{mode_name}_d_2_78"
      elif (
        (last_candle["RSI_3"] > 90.0)
        and (last_candle["WILLR_14"] > -4.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (last_candle["RSI_3_4h"] < 10.0)
      ):
        return True, f"exit_{mode_name}_d_2_79"
      elif (
        (last_candle["RSI_3"] > 70.0)
        and (last_candle["RSI_14"] < 48.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 50.0))
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 25.0)
      ):
        return True, f"exit_{mode_name}_d_2_80"
      elif (
        (last_candle["RSI_3"] > 82.0)
        and (last_candle["WILLR_14"] > -12.0)
        and (last_candle["RSI_3_1h"] < 25.0)
        and (last_candle["RSI_3_4h"] < 25.0)
        and (isinstance(last_candle["RSI_14_1d"], np.float64) and (last_candle["RSI_14_1d"] > 50.0))
      ):
        return True, f"exit_{mode_name}_d_2_81"
      elif (
        (last_candle["RSI_3"] > 80.0)
        and (last_candle["WILLR_14"] > -12.0)
        and (last_candle["RSI_3_4h"] < 30.0)
        and (last_candle["RSI_3_1d"] < 15.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 40.0)
      ):
        return True, f"exit_{mode_name}_d_2_82"
      elif (
        (last_candle["RSI_3"] > 70.0)
        and (last_candle["RSI_14"] < 48.0)
        and (last_candle["RSI_3_1h"] < 40.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 40.0)
      ):
        return True, f"exit_{mode_name}_d_2_83"
      elif (
        (last_candle["RSI_3"] > 88.0)
        and (last_candle["WILLR_14"] > -4.0)
        and (last_candle["RSI_3_4h"] < 30.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 20.0)
      ):
        return True, f"exit_{mode_name}_d_2_84"
      elif (
        (last_candle["RSI_3"] > 86.0)
        and (last_candle["WILLR_14"] > -10.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (last_candle["RSI_3_4h"] < 40.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_2_85"
      elif (
        (last_candle["RSI_3"] > 92.0)
        and (last_candle["RSI_14_4h"] > 80.0)
        and (last_candle["ROC_2_1h"] < -5.0)
        and (last_candle["ROC_9_1h"] > 5.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_2_86"
      elif (
        (last_candle["RSI_3"] > 64.0)
        and (last_candle["RSI_14"] < 46.0)
        and (last_candle["RSI_3_1h"] < 45.0)
        and (last_candle["RSI_3_4h"] < 50.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_2_87"
      elif (
        (last_candle["RSI_3"] > 86.0)
        and (last_candle["WILLR_14"] > -22.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 40.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
        and (last_candle["change_pct_1h"] < -2.0)
      ):
        return True, f"exit_{mode_name}_d_2_88"
      elif (
        (last_candle["RSI_3"] > 76.0)
        and (last_candle["RSI_14"] < 42.0)
        and (last_candle["ROC_9_1h"] < -5.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 25.0))
      ):
        return True, f"exit_{mode_name}_d_2_89"
      elif (
        (last_candle["RSI_3"] > 90.0)
        and (last_candle["WILLR_14"] > -25.0)
        and (last_candle["RSI_3_1h"] < 50.0)
        and (last_candle["RSI_3_4h"] < 30.0)
        and (last_candle["AROONU_14_4h"] > 50.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 40.0))
      ):
        return True, f"exit_{mode_name}_d_2_90"
      elif (
        (last_candle["RSI_3"] > 70.0)
        and (last_candle["RSI_14"] < 48.0)
        and (last_candle["RSI_3_1h"] < 25.0)
        and (last_candle["RSI_3_4h"] < 25.0)
        and (last_candle["AROONU_14_4h"] > 50.0)
        and (
          isinstance(last_candle["STOCHRSIk_14_14_3_3_1d"], np.float64)
          and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 50.0)
        )
      ):
        return True, f"exit_{mode_name}_d_2_91"
      elif (
        (last_candle["RSI_3"] > 78.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_1h"] < 40.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 25.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -25.0))
      ):
        return True, f"exit_{mode_name}_d_2_92"
      elif (
        (last_candle["RSI_3"] > 70.0)
        and (last_candle["RSI_14"] < 52.0)
        and (last_candle["RSI_3_15m"] < 50.0)
        and (last_candle["AROONU_14_1h"] > 75.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 70.0)
        and (last_candle["AROONU_14_4h"] > 50.0)
        and (
          isinstance(last_candle["STOCHRSIk_14_14_3_3_1d"], np.float64)
          and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 90.0)
        )
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 30.0))
      ):
        return True, f"exit_{mode_name}_d_2_93"
      elif (
        (last_candle["RSI_3"] > 78.0)
        and (last_candle["RSI_14"] < 52.0)
        and (last_candle["RSI_3_1h"] < 25.0)
        and (last_candle["RSI_3_4h"] < 45.0)
        and (last_candle["AROONU_14_1h"] > 75.0)
        and (
          isinstance(last_candle["STOCHRSIk_14_14_3_3_1d"], np.float64)
          and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 90.0)
        )
      ):
        return True, f"exit_{mode_name}_d_2_94"
      elif (
        (last_candle["RSI_3"] > 82.0)
        and (last_candle["WILLR_14"] > -14.0)
        and (last_candle["RSI_3_1h"] < 45.0)
        and (last_candle["RSI_3_4h"] < 40.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 10.0)
        and (isinstance(last_candle["AROONU_14_1d"], np.float64) and (last_candle["AROONU_14_1d"] > 75.0))
      ):
        return True, f"exit_{mode_name}_d_2_95"
      elif (
        (last_candle["RSI_3"] > 60.0)
        and (last_candle["RSI_14"] < 48.0)
        and (last_candle["RSI_3_1h"] < 45.0)
        and (last_candle["RSI_3_1d"] < 45.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_2_96"
      elif (
        (last_candle["RSI_3"] > 82.0)
        and (last_candle["RSI_14"] < 48.0)
        and (last_candle["RSI_3_1h"] < 35.0)
        and (last_candle["AROONU_14_4h"] > 50.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 30.0)
      ):
        return True, f"exit_{mode_name}_d_2_97"
      elif (
        (last_candle["RSI_3"] > 88.0)
        and (last_candle["RSI_3_15m"] > 70.0)
        and (last_candle["RSI_3_1h"] < 60.0)
        and (last_candle["RSI_3_4h"] < 60.0)
        and (last_candle["RSI_3_1d"] > 80.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_2_98"
      elif (
        (last_candle["RSI_3"] > 58.0)
        and (last_candle["RSI_14"] < 54.0)
        and (last_candle["RSI_3_1h"] < 65.0)
        and (last_candle["RSI_3_4h"] < 60.0)
        and (last_candle["AROONU_14_4h"] > 50.0)
        and (last_candle["STOCHk_14_3_3_4h"] > 40.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 80.0))
      ):
        return True, f"exit_{mode_name}_d_2_99"
      elif (
        (last_candle["RSI_3"] > 96.0)
        and (last_candle["RSI_14"] > 74.0)
        and (last_candle["RSI_3_15m"] > 70.0)
        and (last_candle["RSI_3_4h"] < 80.0)
      ):
        return True, f"exit_{mode_name}_d_2_100"
      elif (
        (last_candle["RSI_3"] > 82.0)
        and (last_candle["WILLR_14"] > -18.0)
        and (last_candle["RSI_3_1h"] < 50.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 40.0)
        and (isinstance(last_candle["ROC_9_4h"], np.float64) and (last_candle["ROC_9_4h"] > 40.0))
      ):
        return True, f"exit_{mode_name}_d_2_101"
      elif (
        (last_candle["RSI_3"] > 66.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_1h"] < 60.0)
        and (last_candle["RSI_3_4h"] < 40.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 30.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 40.0))
      ):
        return True, f"exit_{mode_name}_d_2_102"
      elif (
        (last_candle["RSI_3"] > 76.0)
        and (last_candle["RSI_14"] < 58.0)
        and (last_candle["RSI_3_1h"] < 60.0)
        and (last_candle["RSI_14_4h"] > 70.0)
        and (isinstance(last_candle["ROC_9_4h"], np.float64) and (last_candle["ROC_9_4h"] > 80.0))
      ):
        return True, f"exit_{mode_name}_d_2_103"
      elif (
        (last_candle["RSI_3"] > 62.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_1h"] < 60.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 40.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 90.0)
        and (last_candle["ROC_9_4h"] > 40.0)
      ):
        return True, f"exit_{mode_name}_d_2_104"
      elif (
        (last_candle["RSI_3"] > 76.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_15m"] < 55.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 90.0)
        and (last_candle["ROC_9_4h"] > 25.0)
      ):
        return True, f"exit_{mode_name}_d_2_105"
      elif (
        (last_candle["RSI_3"] > 70.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_1h"] < 50.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
        and (last_candle["RSI_14_4h"] > 70.0)
        and (last_candle["ROC_9_4h"] > 40.0)
      ):
        return True, f"exit_{mode_name}_d_2_106"
      elif (
        (last_candle["RSI_3"] > 72.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_1h"] < 50.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 70.0)
        and (last_candle["RSI_14_4h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_2_107"
      elif (
        (last_candle["RSI_3"] > 54.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_1h"] < 60.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 80.0)
      ):
        return True, f"exit_{mode_name}_d_2_108"
      elif (
        (last_candle["RSI_3"] > 74.0)
        and (last_candle["WILLR_14"] > -10.0)
        and (last_candle["RSI_3_1h"] < 50.0)
        and (last_candle["RSI_3_4h"] < 20.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 50.0))
      ):
        return True, f"exit_{mode_name}_d_2_109"
      elif (
        (last_candle["RSI_3"] > 70.0)
        and (last_candle["RSI_3_4h"] < 65.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
        and (last_candle["ROC_9_4h"] > 25.0)
      ):
        return True, f"exit_{mode_name}_d_2_110"
      elif (
        (last_candle["RSI_3"] > 48.0)
        and (last_candle["RSI_14"] < 46.0)
        and (last_candle["RSI_3_1h"] < 50.0)
        and (last_candle["RSI_14_4h"] > 70.0)
        and (last_candle["AROONU_14_1h"] > 75.0)
        and (last_candle["AROONU_14_4h"] > 75.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 20.0))
      ):
        return True, f"exit_{mode_name}_d_2_111"
      elif (
        (last_candle["RSI_3"] > 78.0)
        and (last_candle["WILLR_14"] > -30.0)
        and (last_candle["RSI_14"] < 54.0)
        and (last_candle["RSI_3_1h"] < 35.0)
        and (last_candle["RSI_3_4h"] < 35.0)
        and (last_candle["RSI_3_1d"] < 60.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 30.0))
      ):
        return True, f"exit_{mode_name}_d_2_112"
      elif (
        (last_candle["RSI_3"] > 82.0)
        and (last_candle["WILLR_14"] > -4.0)
        and (last_candle["RSI_3_1d"] < 30.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
        and (isinstance(last_candle["ROC_9_4h"], np.float64) and (last_candle["ROC_9_4h"] > 10.0))
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -10.0))
      ):
        return True, f"exit_{mode_name}_d_2_113"
      elif (
        (last_candle["RSI_3"] > 82.0)
        and (last_candle["RSI_14"] < 52.0)
        and (last_candle["RSI_3_1h"] < 20.0)
        and (last_candle["RSI_3_4h"] < 30.0)
        and (last_candle["RSI_3_1d"] < 30.0)
      ):
        return True, f"exit_{mode_name}_d_2_114"
      elif (
        (last_candle["RSI_3"] > 76.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_15m"] < 30.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_2_115"
      elif (
        (last_candle["RSI_3"] > 88.0)
        and (last_candle["RSI_3_1h"] < 15.0)
        and (last_candle["RSI_3_4h"] < 40.0)
        and (last_candle["AROONU_14_4h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_2_116"
      elif (
        (last_candle["RSI_3"] > 84.0)
        and (last_candle["RSI_3_1h"] < 50.0)
        and (last_candle["AROONU_14_1h"] > 80.0)
        and (last_candle["AROONU_14_4h"] > 80.0)
      ):
        return True, f"exit_{mode_name}_d_2_117"
      elif (
        (last_candle["RSI_3"] > 88.0)
        and (last_candle["RSI_3_1h"] < 20.0)
        and (last_candle["RSI_3_4h"] < 60.0)
        and (last_candle["AROONU_14_4h"] > 40.0)
      ):
        return True, f"exit_{mode_name}_d_2_118"
      elif (
        (last_candle["RSI_3"] > 84.0)
        and (last_candle["WILLR_14"] > -20.0)
        and (last_candle["RSI_3_1h"] < 60.0)
        and (last_candle["RSI_3_4h"] < 60.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 40.0)
      ):
        return True, f"exit_{mode_name}_d_2_119"
      elif (
        (last_candle["RSI_3"] > 52.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_1h"] < 40.0)
        and (last_candle["AROONU_14_4h"] > 75.0)
      ):
        return True, f"exit_{mode_name}_d_2_120"
      elif (
        (last_candle["RSI_3"] > 58.0)
        and (last_candle["RSI_14"] < 48.0)
        and (last_candle["RSI_3_1h"] < 50.0)
        and (last_candle["RSI_14_4h"] > 85.0)
      ):
        return True, f"exit_{mode_name}_d_2_121"
      elif (
        (last_candle["RSI_3"] > 56.0)
        and (last_candle["RSI_14"] < 46.0)
        and (last_candle["RSI_3_4h"] < 30.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_2_122"
      elif (
        (last_candle["RSI_3"] > 86.0)
        and (last_candle["WILLR_14"] > -6.0)
        and (last_candle["RSI_3_1h"] < 10.0)
        and (last_candle["RSI_3_1d"] < 30.0)
      ):
        return True, f"exit_{mode_name}_d_2_123"
      elif (
        (last_candle["RSI_3"] > 86.0)
        and (last_candle["RSI_3_1h"] < 15.0)
        and (
          isinstance(last_candle["STOCHRSIk_14_14_3_3_1d"], np.float64)
          and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 80.0)
        )
      ):
        return True, f"exit_{mode_name}_d_2_124"
      elif (
        (last_candle["RSI_3"] > 74.0)
        and (last_candle["WILLR_14"] > -6.0)
        and (last_candle["RSI_3_1h"] < 10.0)
        and (last_candle["RSI_3_4h"] < 40.0)
        and (last_candle["RSI_3_1d"] < 40.0)
        and (last_candle["close"] < (last_candle["high_max_30_1d"] * 0.50))
      ):
        return True, f"exit_{mode_name}_d_2_125"
      elif (
        (last_candle["RSI_3"] > 88.0)
        and (last_candle["RSI_3_1h"] < 15.0)
        and (last_candle["RSI_3_4h"] < 40.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_2_126"
      elif (
        (last_candle["RSI_3"] > 88.0)
        and (last_candle["RSI_3_1h"] < 10.0)
        and (last_candle["RSI_3_4h"] < 30.0)
        and (last_candle["RSI_3_1d"] < 40.0)
      ):
        return True, f"exit_{mode_name}_d_2_127"
      elif (last_candle["RSI_3"] > 92.0) and (last_candle["RSI_3_4h"] < 30.0) and (last_candle["AROONU_14_4h"] > 85.0):
        return True, f"exit_{mode_name}_d_2_128"
      elif (
        (last_candle["RSI_3"] > 84.0)
        and (last_candle["RSI_3_4h"] < 25.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 80.0))
      ):
        return True, f"exit_{mode_name}_d_2_129"
      elif (
        (last_candle["RSI_3"] > 72.0)
        and (last_candle["RSI_14_1h"] > 65.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 80.0)
        and (last_candle["CCI_20_change_pct_1h"] < -0.0)
      ):
        return True, f"exit_{mode_name}_d_2_130"
      elif (
        (last_candle["RSI_14"] < 40.0)
        and (last_candle["RSI_3_1h"] < 20.0)
        and (last_candle["RSI_3_4h"] < 30.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_2_131"
      elif (
        (last_candle["RSI_3"] > 78.0)
        and (last_candle["RSI_3_1h"] < 35.0)
        and (last_candle["RSI_3_4h"] < 35.0)
        and (last_candle["AROONU_14_1h"] > 50.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 40.0)
      ):
        return True, f"exit_{mode_name}_d_2_132"
      elif (
        (last_candle["RSI_3"] > 78.0)
        and (last_candle["AROONU_14_15m"] > 75.0)
        and (last_candle["AROONU_14_1h"] > 75.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 25.0))
      ):
        return True, f"exit_{mode_name}_d_2_133"
    elif 0.04 > current_profit >= 0.03:
      if (
        (last_candle["WILLR_14"] > -1.0)
        and (last_candle["RSI_14"] > 78.0)
        and (
          isinstance(last_candle["EMA_200_1h"], np.float64) and (last_candle["EMA_12_1h"] < last_candle["EMA_200_1h"])
        )
        and (
          isinstance(last_candle["EMA_200_4h"], np.float64) and (last_candle["EMA_12_4h"] < last_candle["EMA_200_4h"])
        )
        and (last_candle["KST_10_15_20_30_10_10_10_15_1h"] < last_candle["KSTs_9_1h"])
        and (last_candle["KST_10_15_20_30_10_10_10_15_4h"] < last_candle["KSTs_9_4h"])
      ):
        return True, f"exit_{mode_name}_d_3_1"
      elif (
        (last_candle["WILLR_14"] > -1.0)
        and (last_candle["RSI_14"] > 64.0)
        and (last_candle["CMF_20_1h"] < -0.0)
        and (
          isinstance(last_candle["EMA_200_1h"], np.float64) and (last_candle["EMA_12_1h"] < last_candle["EMA_200_1h"])
        )
        and (
          isinstance(last_candle["EMA_200_4h"], np.float64) and (last_candle["EMA_12_4h"] < last_candle["EMA_200_4h"])
        )
      ):
        return True, f"exit_{mode_name}_d_3_2"
      elif (
        (last_candle["WILLR_14"] > -20.0)
        and (last_candle["STOCHRSIk_14_14_3_3"] > 95.0)
        and (last_candle["CMF_20_1h"] < -0.0)
        and (last_candle["CMF_20_4h"] < -0.0)
        and (
          (last_candle["STOCHRSIk_14_14_3_3_4h"] > 20.0) and (last_candle["STOCHRSIk_14_14_3_3_change_pct_4h"] < -10.0)
        )
      ):
        return True, f"exit_{mode_name}_d_3_3"
      elif (
        (last_candle["WILLR_14"] > -30.0)
        and (last_candle["RSI_14"] > 65.0)
        and (last_candle["STOCHRSIk_14_14_3_3"] > 95.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 70.0)
        and (
          isinstance(last_candle["EMA_200_1h"], np.float64) and (last_candle["EMA_12_1h"] < last_candle["EMA_200_1h"])
        )
        and (
          isinstance(last_candle["EMA_200_4h"], np.float64) and (last_candle["EMA_12_4h"] < last_candle["EMA_200_4h"])
        )
      ):
        return True, f"exit_{mode_name}_d_3_4"
      elif (
        (last_candle["WILLR_14"] > -6.0)
        and (last_candle["RSI_14"] > 68.0)
        and (last_candle["ROC_9_1h"] < -5.0)
        and (last_candle["ROC_9_4h"] < -5.0)
      ):
        return True, f"exit_{mode_name}_d_3_5"
      elif (
        (last_candle["RSI_3"] > 70.0)
        and (last_candle["STOCHRSIk_14_14_3_3"] > 70.0)
        and (last_candle["RSI_14"] < 40.0)
        and (last_candle["ROC_9_1h"] < -10.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 50.0))
      ):
        return True, f"exit_{mode_name}_d_3_6"
      elif (
        (last_candle["RSI_14"] < 50.0)
        and (last_candle["STOCHRSIk_14_14_3_3"] > 70.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -40.0))
      ):
        return True, f"exit_{mode_name}_d_3_7"
      elif (
        (last_candle["WILLR_14"] > -6.0)
        and (last_candle["STOCHRSIk_14_14_3_3"] > 95.0)
        and (last_candle["CMF_20_1h"] < -0.1)
        and (last_candle["CMF_20_4h"] < -0.1)
        and (last_candle["change_pct_1d"] < -5.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 15.0))
      ):
        return True, f"exit_{mode_name}_d_3_8"
      elif (
        (last_candle["WILLR_14"] > -6.0)
        and (last_candle["RSI_3"] > 95.0)
        and (last_candle["change_pct_4h"] < -5.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 30.0))
      ):
        return True, f"exit_{mode_name}_d_3_9"
      elif (
        (last_candle["WILLR_14"] > -20.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["ROC_9_1h"] < -10.0)
        and (last_candle["ROC_9_4h"] < -10.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 10.0))
      ):
        return True, f"exit_{mode_name}_d_3_10"
      elif (
        (last_candle["RSI_3"] > 75.0)
        and (last_candle["RSI_14"] < 45.0)
        and (last_candle["ROC_9_15m"] < -10.0)
        and (last_candle["ROC_9_1h"] < -10.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -20.0))
      ):
        return True, f"exit_{mode_name}_d_3_11"
      elif (
        (last_candle["RSI_3"] > 70.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_4h"] < 10.0)
        and (last_candle["ROC_9_1h"] < -20.0)
        and (last_candle["ROC_9_4h"] < -20.0)
      ):
        return True, f"exit_{mode_name}_d_3_12"
      elif (last_candle["RSI_3"] > 80.0) and (last_candle["RSI_3_4h"] < 5.0) and (last_candle["ROC_9_4h"] < -25.0):
        return True, f"exit_{mode_name}_d_3_13"
      elif (
        (last_candle["RSI_3"] > 90.0)
        and (last_candle["WILLR_14"] > -8.0)
        and (last_candle["RSI_3_4h"] < 5.0)
        and (last_candle["AROONU_14_4h"] > 25.0)
      ):
        return True, f"exit_{mode_name}_d_3_14"
      elif (last_candle["RSI_3"] > 90.0) and (last_candle["RSI_14"] > 65.0) and (last_candle["ROC_9_4h"] < -30.0):
        return True, f"exit_{mode_name}_d_3_15"
      elif (
        (last_candle["RSI_3"] > 70.0)
        and (last_candle["AROONU_14_4h"] > 25.0)
        and (last_candle["ROC_9_4h"] < -25.0)
        and (last_candle["AROONU_14_1d"] > 50.0)
        and (last_candle["change_pct_1d"] < -15.0)
      ):
        return True, f"exit_{mode_name}_d_3_16"
      elif (
        (last_candle["RSI_3"] > 80.0)
        and (last_candle["WILLR_14"] > -25.0)
        and (last_candle["RSI_3_1h"] < 10.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 90.0)
        and (last_candle["ROC_9_4h"] > 30.0)
      ):
        return True, f"exit_{mode_name}_d_3_17"
      elif (
        (last_candle["RSI_3"] > 75.0)
        and (last_candle["RSI_14"] > 60.0)
        and (last_candle["RSI_3_4h"] < 20.0)
        and (last_candle["ROC_2_1d"] < -50.0)
      ):
        return True, f"exit_{mode_name}_d_3_18"
      elif (
        (last_candle["RSI_3"] > 88.0)
        and (last_candle["RSI_14"] > 68.0)
        and (last_candle["RSI_3_4h"] < 10.0)
        and (
          isinstance(last_candle["STOCHRSIk_14_14_3_3_1d"], np.float64)
          and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 70.0)
        )
      ):
        return True, f"exit_{mode_name}_d_3_19"
      elif (
        (last_candle["RSI_3"] > 46.0)
        and (last_candle["RSI_14"] < 44.0)
        and (last_candle["RSI_3_1h"] < 10.0)
        and (last_candle["AROONU_14_1h"] > 25.0)
      ):
        return True, f"exit_{mode_name}_d_3_20"
      elif (
        (last_candle["RSI_3"] > 60.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_1h"] < 20.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 90.0)
      ):
        return True, f"exit_{mode_name}_d_3_21"
      elif (
        (last_candle["RSI_3"] > 94.0)
        and (last_candle["WILLR_14"] > -6.0)
        and (last_candle["change_pct_4h"] < -5.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -30.0))
      ):
        return True, f"exit_{mode_name}_d_3_22"
      elif (
        (last_candle["RSI_3"] > 85.0)
        and (last_candle["WILLR_14"] > -20.0)
        and (last_candle["RSI_3_1h"] < 15.0)
        and (last_candle["RSI_3_1d"] < 5.0)
      ):
        return True, f"exit_{mode_name}_d_3_23"
      elif (
        (last_candle["RSI_3"] > 88.0)
        and (last_candle["RSI_14"] > 68.0)
        and (last_candle["WILLR_14"] > -25.0)
        and (last_candle["RSI_3_4h"] < 30.0)
        and (last_candle["AROONU_14_4h"] > 75.0)
      ):
        return True, f"exit_{mode_name}_d_3_24"
      elif (
        (last_candle["RSI_3"] > 80.0)
        and (last_candle["WILLR_14"] > -8.0)
        and (last_candle["RSI_3_4h"] < 10.0)
        and (last_candle["ROC_9_4h"] < -15.0)
        and (
          isinstance(last_candle["STOCHRSIk_14_14_3_3_1d"], np.float64)
          and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 50.0)
        )
      ):
        return True, f"exit_{mode_name}_d_3_25"
      elif (
        (last_candle["RSI_3"] > 75.0)
        and (last_candle["WILLR_14"] > -8.0)
        and (last_candle["RSI_3_4h"] < 15.0)
        and (last_candle["ROC_9_4h"] < -20.0)
      ):
        return True, f"exit_{mode_name}_d_3_26"
      elif (
        (last_candle["RSI_3"] > 65.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_1h"] < 20.0)
        and (last_candle["RSI_3_4h"] < 20.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 20.0)
      ):
        return True, f"exit_{mode_name}_d_3_27"
      elif (
        (last_candle["RSI_3"] > 70.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_15m"] < 10.0)
        and (last_candle["ROC_9_4h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_3_28"
      elif (
        (last_candle["RSI_3"] > 75.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_1h"] < 20.0)
        and (last_candle["RSI_3_4h"] < 20.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 30.0)
      ):
        return True, f"exit_{mode_name}_d_3_29"
      elif (
        (last_candle["RSI_3"] > 80.0)
        and (last_candle["RSI_3_1h"] < 25.0)
        and (last_candle["RSI_3_4h"] < 10.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 70.0)
      ):
        return True, f"exit_{mode_name}_d_3_30"
      elif (
        (last_candle["RSI_3"] > 70.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_1h"] < 15.0)
        and (last_candle["RSI_3_4h"] < 15.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 25.0)
      ):
        return True, f"exit_{mode_name}_d_3_31"
      elif (
        (last_candle["RSI_3"] > 80.0)
        and (last_candle["RSI_3_1h"] < 15.0)
        and (last_candle["ROC_2_4h"] < -30.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 30.0)
      ):
        return True, f"exit_{mode_name}_d_3_32"
      elif (
        (last_candle["RSI_3"] > 80.0)
        and (last_candle["WILLR_14"] > -6.0)
        and (last_candle["ROC_2_1h"] < -10.0)
        and (last_candle["ROC_9_1h"] > 30.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_3_33"
      elif (
        (last_candle["RSI_3"] > 65.0)
        and (last_candle["RSI_3_15m"] < 30.0)
        and (last_candle["RSI_14_1h"] > 80.0)
        and (last_candle["ROC_9_1h"] > 40.0)
      ):
        return True, f"exit_{mode_name}_d_3_34"
      elif (
        (last_candle["RSI_3"] > 84.0)
        and (last_candle["WILLR_14"] > -8.0)
        and (last_candle["RSI_3_1d"] < 25.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 75.0)
      ):
        return True, f"exit_{mode_name}_d_3_35"
      elif (
        (last_candle["RSI_3"] > 75.0)
        and (last_candle["WILLR_14"] > -25.0)
        and (last_candle["ROC_9_4h"] < -25.0)
        and (last_candle["RSI_3_1d"] < 25.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_3_36"
      elif (
        (last_candle["RSI_3"] > 78.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_1h"] < 20.0)
        and (last_candle["RSI_3_1d"] < 25.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_3_37"
      elif (
        (last_candle["RSI_3"] > 75.0)
        and (last_candle["WILLR_14"] > -25.0)
        and (last_candle["RSI_3_4h"] < 10.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 20.0)
      ):
        return True, f"exit_{mode_name}_d_3_38"
      elif (
        (last_candle["RSI_3"] > 93.0)
        and (last_candle["WILLR_14"] > -7.0)
        and (last_candle["CMF_20_4h"] < -0.0)
        and (last_candle["RSI_3_4h"] < 10.0)
      ):
        return True, f"exit_{mode_name}_d_3_39"
      elif (
        (last_candle["RSI_3"] > 75.0)
        and (last_candle["WILLR_14"] > -25.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 30.0)
        and (
          isinstance(last_candle["STOCHRSIk_14_14_3_3_1d"], np.float64)
          and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 90.0)
        )
      ):
        return True, f"exit_{mode_name}_d_3_40"
      elif (
        (last_candle["RSI_3"] > 85.0)
        and (last_candle["WILLR_14"] > -20.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 25.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 50.0))
      ):
        return True, f"exit_{mode_name}_d_3_41"
      elif (
        (last_candle["RSI_3"] > 80.0)
        and (last_candle["WILLR_14"] > -35.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 30.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 40.0))
        and (
          isinstance(last_candle["STOCHRSIk_14_14_3_3_1d"], np.float64)
          and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 70.0)
        )
      ):
        return True, f"exit_{mode_name}_d_3_42"
      elif (
        (last_candle["RSI_3"] > 80.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_1h"] < 15.0)
        and (last_candle["RSI_3_4h"] < 40.0)
        and (
          isinstance(last_candle["STOCHRSIk_14_14_3_3_1d"], np.float64)
          and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 90.0)
        )
      ):
        return True, f"exit_{mode_name}_d_3_43"
      elif (
        (last_candle["RSI_3"] > 55.0)
        and (last_candle["WILLR_14"] > -15.0)
        and (last_candle["RSI_3_4h"] < 30.0)
        and (last_candle["RSI_3_1d"] < 25.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -30.0))
      ):
        return True, f"exit_{mode_name}_d_3_44"
      elif (last_candle["RSI_3"] > 90.0) and (last_candle["WILLR_14"] > -10.0) and (last_candle["RSI_3_1h"] < 10.0):
        return True, f"exit_{mode_name}_d_3_45"
      elif (
        (last_candle["RSI_3"] > 70.0)
        and (last_candle["RSI_3_1h"] < 15.0)
        and (last_candle["RSI_3_4h"] < 10.0)
        and (last_candle["ROC_2_1d"] < -20.0)
      ):
        return True, f"exit_{mode_name}_d_3_46"
      elif (
        (last_candle["RSI_3"] > 82.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 80.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 40.0)
        and (last_candle["change_pct_1d"] < -5.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -5.0))
      ):
        return True, f"exit_{mode_name}_d_3_47"
      elif (
        (last_candle["RSI_3"] > 55.0)
        and (last_candle["RSI_14"] < 48.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (last_candle["RSI_3_4h"] < 20.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_3_48"
      elif (
        (last_candle["RSI_3"] > 80.0)
        and (last_candle["WILLR_14"] > -8.0)
        and (last_candle["RSI_3_4h"] < 20.0)
        and (last_candle["change_pct_1d"] < -5.0)
        and (
          isinstance(last_candle["STOCHRSIk_14_14_3_3_1d"], np.float64)
          and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 50.0)
        )
      ):
        return True, f"exit_{mode_name}_d_3_49"
      elif (
        (last_candle["RSI_3"] > 80.0)
        and (last_candle["WILLR_14"] > -8.0)
        and (last_candle["RSI_3_1d"] < 10.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 90.0)
      ):
        return True, f"exit_{mode_name}_d_3_50"
      elif (
        (last_candle["RSI_3"] > 62.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_4h"] < 20.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_3_51"
      elif (
        (last_candle["RSI_3"] > 76.0)
        and (last_candle["RSI_14"] > 56.0)
        and (last_candle["WILLR_14"] > -10.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 70.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -15.0))
      ):
        return True, f"exit_{mode_name}_d_3_52"
      elif (
        (last_candle["RSI_3"] > 70.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["WILLR_14"] > -25.0)
        and (last_candle["RSI_3_1h"] < 20.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
        and (
          isinstance(last_candle["STOCHRSIk_14_14_3_3_1d"], np.float64)
          and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 50.0)
        )
      ):
        return True, f"exit_{mode_name}_d_3_53"
      elif (
        (last_candle["RSI_3"] > 74.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
        and (last_candle["ROC_9_4h"] < -10.0)
        and (last_candle["change_pct_1d"] < -10.0)
      ):
        return True, f"exit_{mode_name}_d_3_54"
      elif (
        (last_candle["RSI_3"] > 90.0)
        and (last_candle["WILLR_14"] > -18.0)
        and (last_candle["ROC_9_4h"] < -5.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 10.0))
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_3_55"
      elif (
        (last_candle["RSI_3"] > 60.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (last_candle["RSI_3_4h"] < 25.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -30.0))
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 10.0)
      ):
        return True, f"exit_{mode_name}_d_3_56"
      elif (
        (last_candle["RSI_3"] > 50.0)
        and (last_candle["RSI_14"] < 40.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -30.0))
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 70.0)
      ):
        return True, f"exit_{mode_name}_d_3_57"
      elif (
        (last_candle["RSI_3"] > 70.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (last_candle["RSI_3_4h"] < 30.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -15.0))
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_3_58"
      elif (
        (last_candle["RSI_3"] > 85.0)
        and (last_candle["WILLR_14"] > -16.0)
        and (last_candle["RSI_3_4h"] < 25.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -15.0))
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 40.0)
      ):
        return True, f"exit_{mode_name}_d_3_59"
      elif (
        (last_candle["RSI_3"] > 65.0)
        and (last_candle["RSI_14"] < 44.0)
        and (last_candle["RSI_14_4h"] > 65.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_3_60"
      elif (
        (last_candle["RSI_3"] > 90.0)
        and (last_candle["WILLR_14"] > -25.0)
        and (last_candle["RSI_3_4h"] < 10.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 30.0)
      ):
        return True, f"exit_{mode_name}_d_3_61"
      elif (
        (last_candle["RSI_3"] > 82.0)
        and (last_candle["WILLR_14"] > -6.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (last_candle["RSI_3_4h"] < 20.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 20.0))
        and (last_candle["change_pct_1d"] < -5.0)
      ):
        return True, f"exit_{mode_name}_d_3_62"
      elif (
        (last_candle["RSI_3"] > 64.0)
        and (last_candle["RSI_3_1d"] < 25.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 80.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 30.0)
      ):
        return True, f"exit_{mode_name}_d_3_63"
      elif (
        (last_candle["RSI_3"] > 84.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (last_candle["RSI_3_4h"] < 30.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 30.0))
      ):
        return True, f"exit_{mode_name}_d_3_64"
      elif (
        (last_candle["RSI_3"] > 64.0)
        and (last_candle["RSI_14"] < 46.0)
        and (last_candle["RSI_3_1h"] < 20.0)
        and (last_candle["RSI_3_4h"] < 15.0)
      ):
        return True, f"exit_{mode_name}_d_3_65"
      elif (
        (last_candle["RSI_3"] > 78.0)
        and (last_candle["RSI_14"] < 52.0)
        and (last_candle["RSI_3_1h"] < 20.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_3_66"
      elif (
        (last_candle["RSI_3"] > 50.0)
        and (last_candle["RSI_14"] < 46.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 80.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -25.0))
      ):
        return True, f"exit_{mode_name}_d_3_67"
      elif (
        (last_candle["RSI_3"] > 80.0)
        and (last_candle["RSI_14"] < 52.0)
        and (last_candle["RSI_3_1h"] < 25.0)
        and (last_candle["ROC_2_4h"] < -30.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 25.0)
      ):
        return True, f"exit_{mode_name}_d_3_68"
      elif (
        (last_candle["RSI_3"] > 94.0)
        and (last_candle["ROC_9_4h"] > 20.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
        and (last_candle["change_pct_4h"] < -5.0)
      ):
        return True, f"exit_{mode_name}_d_3_69"
      elif (
        (last_candle["RSI_3"] > 62.0)
        and (last_candle["RSI_14"] < 44.0)
        and (last_candle["RSI_3_1h"] < 25.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 20.0)
      ):
        return True, f"exit_{mode_name}_d_3_70"
      elif (
        (last_candle["RSI_3"] > 60.0)
        and (last_candle["RSI_14"] < 48.0)
        and (last_candle["RSI_3_4h"] < 25.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 20.0)
      ):
        return True, f"exit_{mode_name}_d_3_71"
      elif (
        (last_candle["RSI_3"] > 74.0)
        and (last_candle["RSI_14"] < 46.0)
        and (last_candle["RSI_3_1h"] < 10.0)
        and (last_candle["AROONU_14_4h"] > 25.0)
      ):
        return True, f"exit_{mode_name}_d_3_72"
      elif (
        (last_candle["RSI_3"] > 74.0)
        and (last_candle["RSI_3_1h"] < 25.0)
        and (last_candle["RSI_3_4h"] < 15.0)
        and (last_candle["ROC_9_4h"] < -20.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -25.0))
      ):
        return True, f"exit_{mode_name}_d_3_73"
      elif (
        (last_candle["RSI_3"] > 96.0)
        and (last_candle["WILLR_14"] > -10.0)
        and (last_candle["RSI_3_4h"] < 25.0)
        and (last_candle["RSI_3_1d"] < 25.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_3_74"
      elif (
        (last_candle["RSI_3"] > 92.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (last_candle["RSI_3_4h"] < 20.0)
        and (
          isinstance(last_candle["STOCHRSIk_14_14_3_3_1d"], np.float64)
          and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 50.0)
        )
      ):
        return True, f"exit_{mode_name}_d_3_75"
      elif (
        (last_candle["RSI_3"] > 64.0)
        and (last_candle["RSI_14"] < 54.0)
        and (last_candle["ROC_9_1h"] > 80.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 80.0)
      ):
        return True, f"exit_{mode_name}_d_3_76"
      elif (
        (last_candle["RSI_3"] > 72.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 50.0))
      ):
        return True, f"exit_{mode_name}_d_3_77"
      elif (
        (last_candle["RSI_3"] > 82.0)
        and (last_candle["WILLR_14"] > -20.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (last_candle["RSI_3_4h"] < 20.0)
        and (last_candle["RSI_3_1d"] < 20.0)
      ):
        return True, f"exit_{mode_name}_d_3_78"
      elif (
        (last_candle["RSI_3"] > 88.0)
        and (last_candle["WILLR_14"] > -6.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (last_candle["RSI_3_4h"] < 10.0)
      ):
        return True, f"exit_{mode_name}_d_3_79"
      elif (
        (last_candle["RSI_3"] > 68.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 50.0))
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 25.0)
      ):
        return True, f"exit_{mode_name}_d_3_80"
      elif (
        (last_candle["RSI_3"] > 80.0)
        and (last_candle["WILLR_14"] > -14.0)
        and (last_candle["RSI_3_1h"] < 25.0)
        and (last_candle["RSI_3_4h"] < 25.0)
        and (isinstance(last_candle["RSI_14_1d"], np.float64) and (last_candle["RSI_14_1d"] > 50.0))
      ):
        return True, f"exit_{mode_name}_d_3_81"
      elif (
        (last_candle["RSI_3"] > 78.0)
        and (last_candle["WILLR_14"] > -14.0)
        and (last_candle["RSI_3_4h"] < 30.0)
        and (last_candle["RSI_3_1d"] < 15.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 40.0)
      ):
        return True, f"exit_{mode_name}_d_3_82"
      elif (
        (last_candle["RSI_3"] > 68.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_1h"] < 40.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 40.0)
      ):
        return True, f"exit_{mode_name}_d_3_83"
      elif (
        (last_candle["RSI_3"] > 86.0)
        and (last_candle["WILLR_14"] > -6.0)
        and (last_candle["RSI_3_4h"] < 30.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 20.0)
      ):
        return True, f"exit_{mode_name}_d_3_84"
      elif (
        (last_candle["RSI_3"] > 84.0)
        and (last_candle["WILLR_14"] > -12.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (last_candle["RSI_3_4h"] < 40.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_3_85"
      elif (
        (last_candle["RSI_3"] > 90.0)
        and (last_candle["RSI_14_4h"] > 80.0)
        and (last_candle["ROC_2_1h"] < -5.0)
        and (last_candle["ROC_9_1h"] > 5.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_3_86"
      elif (
        (last_candle["RSI_3"] > 62.0)
        and (last_candle["RSI_14"] < 48.0)
        and (last_candle["RSI_3_1h"] < 45.0)
        and (last_candle["RSI_3_4h"] < 50.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_3_87"
      elif (
        (last_candle["RSI_3"] > 84.0)
        and (last_candle["WILLR_14"] > -24.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 40.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
        and (last_candle["change_pct_1h"] < -2.0)
      ):
        return True, f"exit_{mode_name}_d_3_88"
      elif (
        (last_candle["RSI_3"] > 74.0)
        and (last_candle["RSI_14"] < 44.0)
        and (last_candle["ROC_9_1h"] < -5.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 25.0))
      ):
        return True, f"exit_{mode_name}_d_3_89"
      elif (
        (last_candle["RSI_3"] > 88.0)
        and (last_candle["WILLR_14"] > -25.0)
        and (last_candle["RSI_3_1h"] < 50.0)
        and (last_candle["RSI_3_4h"] < 30.0)
        and (last_candle["AROONU_14_4h"] > 50.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 40.0))
      ):
        return True, f"exit_{mode_name}_d_3_90"
      elif (
        (last_candle["RSI_3"] > 68.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_1h"] < 25.0)
        and (last_candle["RSI_3_4h"] < 25.0)
        and (last_candle["AROONU_14_4h"] > 50.0)
        and (
          isinstance(last_candle["STOCHRSIk_14_14_3_3_1d"], np.float64)
          and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 50.0)
        )
      ):
        return True, f"exit_{mode_name}_d_3_91"
      elif (
        (last_candle["RSI_3"] > 76.0)
        and (last_candle["RSI_14"] < 52.0)
        and (last_candle["RSI_3_1h"] < 40.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 25.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -25.0))
      ):
        return True, f"exit_{mode_name}_d_3_92"
      elif (
        (last_candle["RSI_3"] > 68.0)
        and (last_candle["RSI_14"] < 54.0)
        and (last_candle["RSI_3_15m"] < 50.0)
        and (last_candle["AROONU_14_1h"] > 75.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 70.0)
        and (last_candle["AROONU_14_4h"] > 50.0)
        and (
          isinstance(last_candle["STOCHRSIk_14_14_3_3_1d"], np.float64)
          and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 90.0)
        )
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 30.0))
      ):
        return True, f"exit_{mode_name}_d_3_93"
      elif (
        (last_candle["RSI_3"] > 76.0)
        and (last_candle["RSI_14"] < 54.0)
        and (last_candle["RSI_3_1h"] < 25.0)
        and (last_candle["RSI_3_4h"] < 45.0)
        and (last_candle["AROONU_14_1h"] > 75.0)
        and (
          isinstance(last_candle["STOCHRSIk_14_14_3_3_1d"], np.float64)
          and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 90.0)
        )
      ):
        return True, f"exit_{mode_name}_d_3_94"
      elif (
        (last_candle["RSI_3"] > 80.0)
        and (last_candle["WILLR_14"] > -16.0)
        and (last_candle["RSI_3_1h"] < 45.0)
        and (last_candle["RSI_3_4h"] < 40.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 10.0)
        and (isinstance(last_candle["AROONU_14_1d"], np.float64) and (last_candle["AROONU_14_1d"] > 75.0))
      ):
        return True, f"exit_{mode_name}_d_3_95"
      elif (
        (last_candle["RSI_3"] > 58.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_1h"] < 45.0)
        and (last_candle["RSI_3_1d"] < 45.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_3_96"
      elif (
        (last_candle["RSI_3"] > 80.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_1h"] < 35.0)
        and (last_candle["AROONU_14_4h"] > 50.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 30.0)
      ):
        return True, f"exit_{mode_name}_d_3_97"
      elif (
        (last_candle["RSI_3"] > 86.0)
        and (last_candle["RSI_3_15m"] > 68.0)
        and (last_candle["RSI_3_1h"] < 60.0)
        and (last_candle["RSI_3_4h"] < 60.0)
        and (last_candle["RSI_3_1d"] > 80.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_3_98"
      elif (
        (last_candle["RSI_3"] > 56.0)
        and (last_candle["RSI_14"] < 56.0)
        and (last_candle["RSI_3_1h"] < 65.0)
        and (last_candle["RSI_3_4h"] < 60.0)
        and (last_candle["AROONU_14_4h"] > 50.0)
        and (last_candle["STOCHk_14_3_3_4h"] > 40.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 80.0))
      ):
        return True, f"exit_{mode_name}_d_3_99"
      elif (
        (last_candle["RSI_3"] > 94.0)
        and (last_candle["RSI_14"] > 72.0)
        and (last_candle["RSI_3_15m"] > 70.0)
        and (last_candle["RSI_3_4h"] < 80.0)
      ):
        return True, f"exit_{mode_name}_d_3_100"
      elif (
        (last_candle["RSI_3"] > 80.0)
        and (last_candle["WILLR_14"] > -20.0)
        and (last_candle["RSI_3_1h"] < 50.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 40.0)
        and (isinstance(last_candle["ROC_9_4h"], np.float64) and (last_candle["ROC_9_4h"] > 40.0))
      ):
        return True, f"exit_{mode_name}_d_3_101"
      elif (
        (last_candle["RSI_3"] > 64.0)
        and (last_candle["RSI_14"] < 52.0)
        and (last_candle["RSI_3_1h"] < 60.0)
        and (last_candle["RSI_3_4h"] < 40.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 30.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 40.0))
      ):
        return True, f"exit_{mode_name}_d_3_102"
      elif (
        (last_candle["RSI_3"] > 74.0)
        and (last_candle["RSI_14"] < 60.0)
        and (last_candle["RSI_3_1h"] < 60.0)
        and (last_candle["RSI_14_4h"] > 70.0)
        and (isinstance(last_candle["ROC_9_4h"], np.float64) and (last_candle["ROC_9_4h"] > 80.0))
      ):
        return True, f"exit_{mode_name}_d_3_103"
      elif (
        (last_candle["RSI_3"] > 60.0)
        and (last_candle["RSI_14"] < 52.0)
        and (last_candle["RSI_3_1h"] < 60.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 40.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 90.0)
        and (last_candle["ROC_9_4h"] > 40.0)
      ):
        return True, f"exit_{mode_name}_d_3_104"
      elif (
        (last_candle["RSI_3"] > 74.0)
        and (last_candle["RSI_14"] < 52.0)
        and (last_candle["RSI_3_15m"] < 55.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 90.0)
        and (last_candle["ROC_9_4h"] > 25.0)
      ):
        return True, f"exit_{mode_name}_d_3_105"
      elif (
        (last_candle["RSI_3"] > 68.0)
        and (last_candle["RSI_14"] < 52.0)
        and (last_candle["RSI_3_1h"] < 50.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
        and (last_candle["RSI_14_4h"] > 70.0)
        and (last_candle["ROC_9_4h"] > 40.0)
      ):
        return True, f"exit_{mode_name}_d_3_106"
      elif (
        (last_candle["RSI_3"] > 70.0)
        and (last_candle["RSI_14"] < 52.0)
        and (last_candle["RSI_3_1h"] < 50.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 70.0)
        and (last_candle["RSI_14_4h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_3_107"
      elif (
        (last_candle["RSI_3"] > 52.0)
        and (last_candle["RSI_14"] < 52.0)
        and (last_candle["RSI_3_1h"] < 60.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 80.0)
      ):
        return True, f"exit_{mode_name}_d_3_108"
      elif (
        (last_candle["RSI_3"] > 72.0)
        and (last_candle["WILLR_14"] > -12.0)
        and (last_candle["RSI_3_1h"] < 50.0)
        and (last_candle["RSI_3_4h"] < 20.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 50.0))
      ):
        return True, f"exit_{mode_name}_d_3_109"
      elif (
        (last_candle["RSI_3"] > 68.0)
        and (last_candle["RSI_3_4h"] < 65.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
        and (last_candle["ROC_9_4h"] > 25.0)
      ):
        return True, f"exit_{mode_name}_d_3_110"
      elif (
        (last_candle["RSI_3"] > 46.0)
        and (last_candle["RSI_14"] < 48.0)
        and (last_candle["RSI_3_1h"] < 50.0)
        and (last_candle["RSI_14_4h"] > 70.0)
        and (last_candle["AROONU_14_1h"] > 75.0)
        and (last_candle["AROONU_14_4h"] > 75.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 20.0))
      ):
        return True, f"exit_{mode_name}_d_3_111"
      elif (
        (last_candle["RSI_3"] > 76.0)
        and (last_candle["WILLR_14"] > -35.0)
        and (last_candle["RSI_14"] < 56.0)
        and (last_candle["RSI_3_1h"] < 35.0)
        and (last_candle["RSI_3_4h"] < 35.0)
        and (last_candle["RSI_3_1d"] < 60.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 30.0))
      ):
        return True, f"exit_{mode_name}_d_3_112"
      elif (
        (last_candle["RSI_3"] > 80.0)
        and (last_candle["WILLR_14"] > -6.0)
        and (last_candle["RSI_3_1d"] < 30.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
        and (isinstance(last_candle["ROC_9_4h"], np.float64) and (last_candle["ROC_9_4h"] > 10.0))
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -10.0))
      ):
        return True, f"exit_{mode_name}_d_3_113"
      elif (
        (last_candle["RSI_3"] > 80.0)
        and (last_candle["RSI_14"] < 54.0)
        and (last_candle["RSI_3_1h"] < 20.0)
        and (last_candle["RSI_3_4h"] < 30.0)
        and (last_candle["RSI_3_1d"] < 30.0)
      ):
        return True, f"exit_{mode_name}_d_3_114"
      elif (
        (last_candle["RSI_3"] > 74.0)
        and (last_candle["RSI_14"] < 52.0)
        and (last_candle["RSI_3_15m"] < 30.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_3_115"
      elif (
        (last_candle["RSI_3"] > 86.0)
        and (last_candle["RSI_3_1h"] < 15.0)
        and (last_candle["RSI_3_4h"] < 40.0)
        and (last_candle["AROONU_14_4h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_3_116"
      elif (
        (last_candle["RSI_3"] > 82.0)
        and (last_candle["RSI_3_1h"] < 50.0)
        and (last_candle["AROONU_14_1h"] > 80.0)
        and (last_candle["AROONU_14_4h"] > 80.0)
      ):
        return True, f"exit_{mode_name}_d_3_117"
      elif (
        (last_candle["RSI_3"] > 86.0)
        and (last_candle["RSI_3_1h"] < 20.0)
        and (last_candle["RSI_3_4h"] < 60.0)
        and (last_candle["AROONU_14_4h"] > 40.0)
      ):
        return True, f"exit_{mode_name}_d_3_118"
      elif (
        (last_candle["RSI_3"] > 82.0)
        and (last_candle["WILLR_14"] > -20.0)
        and (last_candle["RSI_3_1h"] < 60.0)
        and (last_candle["RSI_3_4h"] < 60.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 40.0)
      ):
        return True, f"exit_{mode_name}_d_3_119"
      elif (
        (last_candle["RSI_3"] > 50.0)
        and (last_candle["RSI_14"] < 52.0)
        and (last_candle["RSI_3_1h"] < 40.0)
        and (last_candle["AROONU_14_4h"] > 75.0)
      ):
        return True, f"exit_{mode_name}_d_3_120"
      elif (
        (last_candle["RSI_3"] > 56.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_1h"] < 50.0)
        and (last_candle["RSI_14_4h"] > 85.0)
      ):
        return True, f"exit_{mode_name}_d_3_121"
      elif (
        (last_candle["RSI_3"] > 54.0)
        and (last_candle["RSI_14"] < 48.0)
        and (last_candle["RSI_3_4h"] < 30.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_3_122"
      elif (
        (last_candle["RSI_3"] > 84.0)
        and (last_candle["WILLR_14"] > -8.0)
        and (last_candle["RSI_3_1h"] < 10.0)
        and (last_candle["RSI_3_1d"] < 30.0)
      ):
        return True, f"exit_{mode_name}_d_3_123"
      elif (
        (last_candle["RSI_3"] > 84.0)
        and (last_candle["RSI_3_1h"] < 15.0)
        and (
          isinstance(last_candle["STOCHRSIk_14_14_3_3_1d"], np.float64)
          and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 80.0)
        )
      ):
        return True, f"exit_{mode_name}_d_3_124"
      elif (
        (last_candle["RSI_3"] > 72.0)
        and (last_candle["WILLR_14"] > -8.0)
        and (last_candle["RSI_3_1h"] < 10.0)
        and (last_candle["RSI_3_4h"] < 40.0)
        and (last_candle["RSI_3_1d"] < 40.0)
        and (last_candle["close"] < (last_candle["high_max_30_1d"] * 0.50))
      ):
        return True, f"exit_{mode_name}_d_3_125"
      elif (
        (last_candle["RSI_3"] > 86.0)
        and (last_candle["RSI_3_1h"] < 15.0)
        and (last_candle["RSI_3_4h"] < 40.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_3_126"
      elif (
        (last_candle["RSI_3"] > 86.0)
        and (last_candle["RSI_3_1h"] < 10.0)
        and (last_candle["RSI_3_4h"] < 30.0)
        and (last_candle["RSI_3_1d"] < 40.0)
      ):
        return True, f"exit_{mode_name}_d_3_127"
      elif (last_candle["RSI_3"] > 90.0) and (last_candle["RSI_3_4h"] < 30.0) and (last_candle["AROONU_14_4h"] > 85.0):
        return True, f"exit_{mode_name}_d_3_128"
      elif (
        (last_candle["RSI_3"] > 82.0)
        and (last_candle["RSI_3_4h"] < 25.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 80.0))
      ):
        return True, f"exit_{mode_name}_d_3_129"
      elif (
        (last_candle["RSI_3"] > 70.0)
        and (last_candle["RSI_14_1h"] > 65.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 80.0)
        and (last_candle["CCI_20_change_pct_1h"] < -0.0)
      ):
        return True, f"exit_{mode_name}_d_3_130"
      elif (
        (last_candle["RSI_14"] < 42.0)
        and (last_candle["RSI_3_1h"] < 20.0)
        and (last_candle["RSI_3_4h"] < 30.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_3_131"
      elif (
        (last_candle["RSI_3"] > 76.0)
        and (last_candle["RSI_3_1h"] < 35.0)
        and (last_candle["RSI_3_4h"] < 35.0)
        and (last_candle["AROONU_14_1h"] > 50.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 40.0)
      ):
        return True, f"exit_{mode_name}_d_3_132"
      elif (
        (last_candle["RSI_3"] > 76.0)
        and (last_candle["AROONU_14_15m"] > 75.0)
        and (last_candle["AROONU_14_1h"] > 75.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 25.0))
      ):
        return True, f"exit_{mode_name}_d_3_133"
    elif 0.05 > current_profit >= 0.04:
      if (
        (last_candle["WILLR_14"] > -1.0)
        and (last_candle["RSI_14"] > 78.0)
        and (
          isinstance(last_candle["EMA_200_1h"], np.float64) and (last_candle["EMA_12_1h"] < last_candle["EMA_200_1h"])
        )
        and (
          isinstance(last_candle["EMA_200_4h"], np.float64) and (last_candle["EMA_12_4h"] < last_candle["EMA_200_4h"])
        )
        and (last_candle["KST_10_15_20_30_10_10_10_15_1h"] < last_candle["KSTs_9_1h"])
        and (last_candle["KST_10_15_20_30_10_10_10_15_4h"] < last_candle["KSTs_9_4h"])
      ):
        return True, f"exit_{mode_name}_d_4_1"
      elif (
        (last_candle["WILLR_14"] > -1.0)
        and (last_candle["RSI_14"] > 62.0)
        and (last_candle["CMF_20_1h"] < -0.0)
        and (
          isinstance(last_candle["EMA_200_1h"], np.float64) and (last_candle["EMA_12_1h"] < last_candle["EMA_200_1h"])
        )
        and (
          isinstance(last_candle["EMA_200_4h"], np.float64) and (last_candle["EMA_12_4h"] < last_candle["EMA_200_4h"])
        )
      ):
        return True, f"exit_{mode_name}_d_4_2"
      elif (
        (last_candle["WILLR_14"] > -20.0)
        and (last_candle["STOCHRSIk_14_14_3_3"] > 95.0)
        and (last_candle["CMF_20_1h"] < -0.0)
        and (last_candle["CMF_20_4h"] < -0.0)
        and (
          (last_candle["STOCHRSIk_14_14_3_3_4h"] > 20.0) and (last_candle["STOCHRSIk_14_14_3_3_change_pct_4h"] < -10.0)
        )
      ):
        return True, f"exit_{mode_name}_d_4_3"
      elif (
        (last_candle["WILLR_14"] > -30.0)
        and (last_candle["RSI_14"] > 65.0)
        and (last_candle["STOCHRSIk_14_14_3_3"] > 95.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 70.0)
        and (
          isinstance(last_candle["EMA_200_1h"], np.float64) and (last_candle["EMA_12_1h"] < last_candle["EMA_200_1h"])
        )
        and (
          isinstance(last_candle["EMA_200_4h"], np.float64) and (last_candle["EMA_12_4h"] < last_candle["EMA_200_4h"])
        )
      ):
        return True, f"exit_{mode_name}_d_4_4"
      elif (
        (last_candle["WILLR_14"] > -8.0)
        and (last_candle["RSI_14"] > 66.0)
        and (last_candle["ROC_9_1h"] < -5.0)
        and (last_candle["ROC_9_4h"] < -5.0)
      ):
        return True, f"exit_{mode_name}_d_4_5"
      elif (
        (last_candle["RSI_3"] > 70.0)
        and (last_candle["STOCHRSIk_14_14_3_3"] > 70.0)
        and (last_candle["RSI_14"] < 40.0)
        and (last_candle["ROC_9_1h"] < -10.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 50.0))
      ):
        return True, f"exit_{mode_name}_d_4_6"
      elif (
        (last_candle["RSI_14"] < 50.0)
        and (last_candle["STOCHRSIk_14_14_3_3"] > 70.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -40.0))
      ):
        return True, f"exit_{mode_name}_d_4_7"
      elif (
        (last_candle["WILLR_14"] > -8.0)
        and (last_candle["STOCHRSIk_14_14_3_3"] > 95.0)
        and (last_candle["CMF_20_1h"] < -0.1)
        and (last_candle["CMF_20_4h"] < -0.1)
        and (last_candle["change_pct_1d"] < -5.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 15.0))
      ):
        return True, f"exit_{mode_name}_d_4_8"
      elif (
        (last_candle["WILLR_14"] > -7.0)
        and (last_candle["RSI_3"] > 95.0)
        and (last_candle["change_pct_4h"] < -5.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 30.0))
      ):
        return True, f"exit_{mode_name}_d_4_9"
      elif (
        (last_candle["WILLR_14"] > -20.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["ROC_9_1h"] < -10.0)
        and (last_candle["ROC_9_4h"] < -10.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 10.0))
      ):
        return True, f"exit_{mode_name}_d_4_10"
      elif (
        (last_candle["RSI_3"] > 75.0)
        and (last_candle["RSI_14"] < 45.0)
        and (last_candle["ROC_9_15m"] < -10.0)
        and (last_candle["ROC_9_1h"] < -10.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -20.0))
      ):
        return True, f"exit_{mode_name}_d_4_11"
      elif (
        (last_candle["RSI_3"] > 70.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_4h"] < 10.0)
        and (last_candle["ROC_9_1h"] < -20.0)
        and (last_candle["ROC_9_4h"] < -20.0)
      ):
        return True, f"exit_{mode_name}_d_4_12"
      elif (last_candle["RSI_3"] > 80.0) and (last_candle["RSI_3_4h"] < 5.0) and (last_candle["ROC_9_4h"] < -25.0):
        return True, f"exit_{mode_name}_d_4_13"
      elif (
        (last_candle["RSI_3"] > 90.0)
        and (last_candle["WILLR_14"] > -10.0)
        and (last_candle["RSI_3_4h"] < 5.0)
        and (last_candle["AROONU_14_4h"] > 25.0)
      ):
        return True, f"exit_{mode_name}_d_4_14"
      elif (last_candle["RSI_3"] > 88.0) and (last_candle["RSI_14"] > 60.0) and (last_candle["ROC_9_4h"] < -30.0):
        return True, f"exit_{mode_name}_d_4_15"
      elif (
        (last_candle["RSI_3"] > 70.0)
        and (last_candle["AROONU_14_4h"] > 25.0)
        and (last_candle["ROC_9_4h"] < -25.0)
        and (last_candle["AROONU_14_1d"] > 50.0)
        and (last_candle["change_pct_1d"] < -15.0)
      ):
        return True, f"exit_{mode_name}_d_4_16"
      elif (
        (last_candle["RSI_3"] > 80.0)
        and (last_candle["WILLR_14"] > -30.0)
        and (last_candle["RSI_3_1h"] < 10.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 90.0)
        and (last_candle["ROC_9_4h"] > 30.0)
      ):
        return True, f"exit_{mode_name}_d_4_17"
      elif (
        (last_candle["RSI_3"] > 75.0)
        and (last_candle["RSI_14"] > 60.0)
        and (last_candle["RSI_3_4h"] < 20.0)
        and (last_candle["ROC_2_1d"] < -50.0)
      ):
        return True, f"exit_{mode_name}_d_4_18"
      elif (
        (last_candle["RSI_3"] > 86.0)
        and (last_candle["RSI_14"] > 66.0)
        and (last_candle["RSI_3_4h"] < 10.0)
        and (
          isinstance(last_candle["STOCHRSIk_14_14_3_3_1d"], np.float64)
          and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 70.0)
        )
      ):
        return True, f"exit_{mode_name}_d_4_19"
      elif (
        (last_candle["RSI_3"] > 44.0)
        and (last_candle["RSI_14"] < 46.0)
        and (last_candle["RSI_3_1h"] < 10.0)
        and (last_candle["AROONU_14_1h"] > 25.0)
      ):
        return True, f"exit_{mode_name}_d_4_20"
      elif (
        (last_candle["RSI_3"] > 55.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_1h"] < 20.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 90.0)
      ):
        return True, f"exit_{mode_name}_d_4_21"
      elif (
        (last_candle["RSI_3"] > 92.0)
        and (last_candle["WILLR_14"] > -8.0)
        and (last_candle["change_pct_4h"] < -5.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -30.0))
      ):
        return True, f"exit_{mode_name}_d_4_22"
      elif (
        (last_candle["RSI_3"] > 80.0)
        and (last_candle["WILLR_14"] > -25.0)
        and (last_candle["RSI_3_1h"] < 15.0)
        and (last_candle["RSI_3_1d"] < 5.0)
      ):
        return True, f"exit_{mode_name}_d_4_23"
      elif (
        (last_candle["RSI_3"] > 86.0)
        and (last_candle["RSI_14"] > 66.0)
        and (last_candle["WILLR_14"] > -30.0)
        and (last_candle["RSI_3_4h"] < 30.0)
        and (last_candle["AROONU_14_4h"] > 75.0)
      ):
        return True, f"exit_{mode_name}_d_4_24"
      elif (
        (last_candle["RSI_3"] > 75.0)
        and (last_candle["WILLR_14"] > -10.0)
        and (last_candle["RSI_3_4h"] < 10.0)
        and (last_candle["ROC_9_4h"] < -15.0)
        and (
          isinstance(last_candle["STOCHRSIk_14_14_3_3_1d"], np.float64)
          and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 50.0)
        )
      ):
        return True, f"exit_{mode_name}_d_4_25"
      elif (
        (last_candle["RSI_3"] > 70.0)
        and (last_candle["WILLR_14"] > -10.0)
        and (last_candle["RSI_3_4h"] < 15.0)
        and (last_candle["ROC_9_4h"] < -20.0)
      ):
        return True, f"exit_{mode_name}_d_4_26"
      elif (
        (last_candle["RSI_3"] > 65.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_1h"] < 20.0)
        and (last_candle["RSI_3_4h"] < 20.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 20.0)
      ):
        return True, f"exit_{mode_name}_d_4_27"
      elif (
        (last_candle["RSI_3"] > 65.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_15m"] < 10.0)
        and (last_candle["ROC_9_4h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_4_28"
      elif (
        (last_candle["RSI_3"] > 75.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_1h"] < 20.0)
        and (last_candle["RSI_3_4h"] < 20.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 30.0)
      ):
        return True, f"exit_{mode_name}_d_4_29"
      elif (
        (last_candle["RSI_3"] > 75.0)
        and (last_candle["RSI_3_1h"] < 25.0)
        and (last_candle["RSI_3_4h"] < 10.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 70.0)
      ):
        return True, f"exit_{mode_name}_d_4_30"
      elif (
        (last_candle["RSI_3"] > 65.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_1h"] < 15.0)
        and (last_candle["RSI_3_4h"] < 15.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 25.0)
      ):
        return True, f"exit_{mode_name}_d_4_31"
      elif (
        (last_candle["RSI_3"] > 75.0)
        and (last_candle["RSI_3_1h"] < 15.0)
        and (last_candle["ROC_2_4h"] < -30.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 30.0)
      ):
        return True, f"exit_{mode_name}_d_4_32"
      elif (
        (last_candle["RSI_3"] > 75.0)
        and (last_candle["WILLR_14"] > -8.0)
        and (last_candle["ROC_2_1h"] < -10.0)
        and (last_candle["ROC_9_1h"] > 30.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_4_33"
      elif (
        (last_candle["RSI_3"] > 65.0)
        and (last_candle["RSI_3_15m"] < 30.0)
        and (last_candle["RSI_14_1h"] > 80.0)
        and (last_candle["ROC_9_1h"] > 40.0)
      ):
        return True, f"exit_{mode_name}_d_4_34"
      elif (
        (last_candle["RSI_3"] > 82.0)
        and (last_candle["WILLR_14"] > -9.0)
        and (last_candle["RSI_3_1d"] < 25.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 75.0)
      ):
        return True, f"exit_{mode_name}_d_4_35"
      elif (
        (last_candle["RSI_3"] > 70.0)
        and (last_candle["WILLR_14"] > -30.0)
        and (last_candle["ROC_9_4h"] < -25.0)
        and (last_candle["RSI_3_1d"] < 25.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_4_36"
      elif (
        (last_candle["RSI_3"] > 76.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_1h"] < 20.0)
        and (last_candle["RSI_3_1d"] < 25.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_4_37"
      elif (
        (last_candle["RSI_3"] > 70.0)
        and (last_candle["WILLR_14"] > -30.0)
        and (last_candle["RSI_3_4h"] < 10.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 20.0)
      ):
        return True, f"exit_{mode_name}_d_4_38"
      elif (
        (last_candle["RSI_3"] > 92.0)
        and (last_candle["WILLR_14"] > -8.0)
        and (last_candle["CMF_20_4h"] < -0.0)
        and (last_candle["RSI_3_4h"] < 10.0)
      ):
        return True, f"exit_{mode_name}_d_4_39"
      elif (
        (last_candle["RSI_3"] > 70.0)
        and (last_candle["WILLR_14"] > -30.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 30.0)
        and (
          isinstance(last_candle["STOCHRSIk_14_14_3_3_1d"], np.float64)
          and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 90.0)
        )
      ):
        return True, f"exit_{mode_name}_d_4_40"
      elif (
        (last_candle["RSI_3"] > 80.0)
        and (last_candle["WILLR_14"] > -25.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 25.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 50.0))
      ):
        return True, f"exit_{mode_name}_d_4_41"
      elif (
        (last_candle["RSI_3"] > 75.0)
        and (last_candle["WILLR_14"] > -40.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 30.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 40.0))
        and (
          isinstance(last_candle["STOCHRSIk_14_14_3_3_1d"], np.float64)
          and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 70.0)
        )
      ):
        return True, f"exit_{mode_name}_d_4_42"
      elif (
        (last_candle["RSI_3"] > 80.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_1h"] < 15.0)
        and (last_candle["RSI_3_4h"] < 40.0)
        and (
          isinstance(last_candle["STOCHRSIk_14_14_3_3_1d"], np.float64)
          and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 90.0)
        )
      ):
        return True, f"exit_{mode_name}_d_4_43"
      elif (
        (last_candle["RSI_3"] > 50.0)
        and (last_candle["WILLR_14"] > -20.0)
        and (last_candle["RSI_3_4h"] < 30.0)
        and (last_candle["RSI_3_1d"] < 25.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -30.0))
      ):
        return True, f"exit_{mode_name}_d_4_44"
      elif (last_candle["RSI_3"] > 88.0) and (last_candle["WILLR_14"] > -12.0) and (last_candle["RSI_3_1h"] < 10.0):
        return True, f"exit_{mode_name}_d_4_45"
      elif (
        (last_candle["RSI_3"] > 70.0)
        and (last_candle["RSI_3_1h"] < 15.0)
        and (last_candle["RSI_3_4h"] < 10.0)
        and (last_candle["ROC_2_1d"] < -20.0)
      ):
        return True, f"exit_{mode_name}_d_4_46"
      elif (
        (last_candle["RSI_3"] > 80.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 80.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 40.0)
        and (last_candle["change_pct_1d"] < -5.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -5.0))
      ):
        return True, f"exit_{mode_name}_d_4_47"
      elif (
        (last_candle["RSI_3"] > 50.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (last_candle["RSI_3_4h"] < 20.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_4_48"
      elif (
        (last_candle["RSI_3"] > 75.0)
        and (last_candle["WILLR_14"] > -10.0)
        and (last_candle["RSI_3_4h"] < 20.0)
        and (last_candle["change_pct_1d"] < -5.0)
        and (
          isinstance(last_candle["STOCHRSIk_14_14_3_3_1d"], np.float64)
          and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 50.0)
        )
      ):
        return True, f"exit_{mode_name}_d_4_49"
      elif (
        (last_candle["RSI_3"] > 80.0)
        and (last_candle["WILLR_14"] > -10.0)
        and (last_candle["RSI_3_1d"] < 10.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 90.0)
      ):
        return True, f"exit_{mode_name}_d_4_50"
      elif (
        (last_candle["RSI_3"] > 60.0)
        and (last_candle["RSI_14"] < 52.0)
        and (last_candle["RSI_3_4h"] < 20.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_4_51"
      elif (
        (last_candle["RSI_3"] > 74.0)
        and (last_candle["RSI_14"] > 54.0)
        and (last_candle["WILLR_14"] > -10.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 70.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -15.0))
      ):
        return True, f"exit_{mode_name}_d_4_52"
      elif (
        (last_candle["RSI_3"] > 70.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["WILLR_14"] > -25.0)
        and (last_candle["RSI_3_1h"] < 20.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
        and (
          isinstance(last_candle["STOCHRSIk_14_14_3_3_1d"], np.float64)
          and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 50.0)
        )
      ):
        return True, f"exit_{mode_name}_d_4_53"
      elif (
        (last_candle["RSI_3"] > 72.0)
        and (last_candle["RSI_14"] < 52.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
        and (last_candle["ROC_9_4h"] < -10.0)
        and (last_candle["change_pct_1d"] < -10.0)
      ):
        return True, f"exit_{mode_name}_d_4_54"
      elif (
        (last_candle["RSI_3"] > 88.0)
        and (last_candle["WILLR_14"] > -20.0)
        and (last_candle["ROC_9_4h"] < -5.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 10.0))
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_4_55"
      elif (
        (last_candle["RSI_3"] > 60.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (last_candle["RSI_3_4h"] < 25.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -30.0))
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 10.0)
      ):
        return True, f"exit_{mode_name}_d_4_56"
      elif (
        (last_candle["RSI_3"] > 50.0)
        and (last_candle["RSI_14"] < 42.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -30.0))
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 70.0)
      ):
        return True, f"exit_{mode_name}_d_4_57"
      elif (
        (last_candle["RSI_3"] > 70.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (last_candle["RSI_3_4h"] < 30.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -15.0))
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_4_58"
      elif (
        (last_candle["RSI_3"] > 85.0)
        and (last_candle["WILLR_14"] > -18.0)
        and (last_candle["RSI_3_4h"] < 25.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -15.0))
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 40.0)
      ):
        return True, f"exit_{mode_name}_d_4_59"
      elif (
        (last_candle["RSI_3"] > 65.0)
        and (last_candle["RSI_14"] < 46.0)
        and (last_candle["RSI_14_4h"] > 65.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_4_60"
      elif (
        (last_candle["RSI_3"] > 90.0)
        and (last_candle["WILLR_14"] > -25.0)
        and (last_candle["RSI_3_4h"] < 10.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 30.0)
      ):
        return True, f"exit_{mode_name}_d_4_61"
      elif (
        (last_candle["RSI_3"] > 80.0)
        and (last_candle["WILLR_14"] > -8.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (last_candle["RSI_3_4h"] < 20.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 20.0))
        and (last_candle["change_pct_1d"] < -5.0)
      ):
        return True, f"exit_{mode_name}_d_4_62"
      elif (
        (last_candle["RSI_3"] > 62.0)
        and (last_candle["RSI_3_1d"] < 25.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 80.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 30.0)
      ):
        return True, f"exit_{mode_name}_d_4_63"
      elif (
        (last_candle["RSI_3"] > 82.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (last_candle["RSI_3_4h"] < 30.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 30.0))
      ):
        return True, f"exit_{mode_name}_d_4_64"
      elif (
        (last_candle["RSI_3"] > 62.0)
        and (last_candle["RSI_14"] < 48.0)
        and (last_candle["RSI_3_1h"] < 20.0)
        and (last_candle["RSI_3_4h"] < 15.0)
      ):
        return True, f"exit_{mode_name}_d_4_65"
      elif (
        (last_candle["RSI_3"] > 76.0)
        and (last_candle["RSI_14"] < 54.0)
        and (last_candle["RSI_3_1h"] < 20.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_4_66"
      elif (
        (last_candle["RSI_3"] > 50.0)
        and (last_candle["RSI_14"] < 48.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 80.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -25.0))
      ):
        return True, f"exit_{mode_name}_d_4_67"
      elif (
        (last_candle["RSI_3"] > 78.0)
        and (last_candle["RSI_14"] < 54.0)
        and (last_candle["RSI_3_1h"] < 25.0)
        and (last_candle["ROC_2_4h"] < -30.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 25.0)
      ):
        return True, f"exit_{mode_name}_d_4_68"
      elif (
        (last_candle["RSI_3"] > 93.0)
        and (last_candle["ROC_9_4h"] > 20.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
        and (last_candle["change_pct_4h"] < -5.0)
      ):
        return True, f"exit_{mode_name}_d_4_69"
      elif (
        (last_candle["RSI_3"] > 60.0)
        and (last_candle["RSI_14"] < 46.0)
        and (last_candle["RSI_3_1h"] < 25.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 20.0)
      ):
        return True, f"exit_{mode_name}_d_4_70"
      elif (
        (last_candle["RSI_3"] > 58.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_4h"] < 25.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 20.0)
      ):
        return True, f"exit_{mode_name}_d_4_71"
      elif (
        (last_candle["RSI_3"] > 72.0)
        and (last_candle["RSI_14"] < 48.0)
        and (last_candle["RSI_3_1h"] < 10.0)
        and (last_candle["AROONU_14_4h"] > 25.0)
      ):
        return True, f"exit_{mode_name}_d_4_72"
      elif (
        (last_candle["RSI_3"] > 72.0)
        and (last_candle["RSI_3_1h"] < 25.0)
        and (last_candle["RSI_3_4h"] < 15.0)
        and (last_candle["ROC_9_4h"] < -20.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -25.0))
      ):
        return True, f"exit_{mode_name}_d_4_73"
      elif (
        (last_candle["RSI_3"] > 95.0)
        and (last_candle["WILLR_14"] > -10.0)
        and (last_candle["RSI_3_4h"] < 25.0)
        and (last_candle["RSI_3_1d"] < 25.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_4_74"
      elif (
        (last_candle["RSI_3"] > 90.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (last_candle["RSI_3_4h"] < 20.0)
        and (
          isinstance(last_candle["STOCHRSIk_14_14_3_3_1d"], np.float64)
          and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 50.0)
        )
      ):
        return True, f"exit_{mode_name}_d_4_75"
      elif (
        (last_candle["RSI_3"] > 62.0)
        and (last_candle["RSI_14"] < 56.0)
        and (last_candle["ROC_9_1h"] > 80.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 80.0)
      ):
        return True, f"exit_{mode_name}_d_4_76"
      elif (
        (last_candle["RSI_3"] > 70.0)
        and (last_candle["RSI_14"] < 52.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 50.0))
      ):
        return True, f"exit_{mode_name}_d_4_77"
      elif (
        (last_candle["RSI_3"] > 80.0)
        and (last_candle["WILLR_14"] > -22.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (last_candle["RSI_3_4h"] < 20.0)
        and (last_candle["RSI_3_1d"] < 20.0)
      ):
        return True, f"exit_{mode_name}_d_4_78"
      elif (
        (last_candle["RSI_3"] > 86.0)
        and (last_candle["WILLR_14"] > -8.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (last_candle["RSI_3_4h"] < 10.0)
      ):
        return True, f"exit_{mode_name}_d_4_79"
      elif (
        (last_candle["RSI_3"] > 66.0)
        and (last_candle["RSI_14"] < 52.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 50.0))
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 25.0)
      ):
        return True, f"exit_{mode_name}_d_4_80"
      elif (
        (last_candle["RSI_3"] > 78.0)
        and (last_candle["WILLR_14"] > -16.0)
        and (last_candle["RSI_3_1h"] < 25.0)
        and (last_candle["RSI_3_4h"] < 25.0)
        and (isinstance(last_candle["RSI_14_1d"], np.float64) and (last_candle["RSI_14_1d"] > 50.0))
      ):
        return True, f"exit_{mode_name}_d_4_81"
      elif (
        (last_candle["RSI_3"] > 76.0)
        and (last_candle["WILLR_14"] > -16.0)
        and (last_candle["RSI_3_4h"] < 30.0)
        and (last_candle["RSI_3_1d"] < 15.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 40.0)
      ):
        return True, f"exit_{mode_name}_d_4_82"
      elif (
        (last_candle["RSI_3"] > 66.0)
        and (last_candle["RSI_14"] < 52.0)
        and (last_candle["RSI_3_1h"] < 40.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 40.0)
      ):
        return True, f"exit_{mode_name}_d_4_83"
      elif (
        (last_candle["RSI_3"] > 84.0)
        and (last_candle["WILLR_14"] > -8.0)
        and (last_candle["RSI_3_4h"] < 30.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 20.0)
      ):
        return True, f"exit_{mode_name}_d_4_84"
      elif (
        (last_candle["RSI_3"] > 82.0)
        and (last_candle["WILLR_14"] > -14.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (last_candle["RSI_3_4h"] < 40.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_4_85"
      elif (
        (last_candle["RSI_3"] > 88.0)
        and (last_candle["RSI_14_4h"] > 80.0)
        and (last_candle["ROC_2_1h"] < -5.0)
        and (last_candle["ROC_9_1h"] > 5.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_4_86"
      elif (
        (last_candle["RSI_3"] > 60.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_1h"] < 45.0)
        and (last_candle["RSI_3_4h"] < 50.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_4_87"
      elif (
        (last_candle["RSI_3"] > 82.0)
        and (last_candle["WILLR_14"] > -26.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 40.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
        and (last_candle["change_pct_1h"] < -2.0)
      ):
        return True, f"exit_{mode_name}_d_4_88"
      elif (
        (last_candle["RSI_3"] > 72.0)
        and (last_candle["RSI_14"] < 46.0)
        and (last_candle["ROC_9_1h"] < -5.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 25.0))
      ):
        return True, f"exit_{mode_name}_d_4_89"
      elif (
        (last_candle["RSI_3"] > 86.0)
        and (last_candle["WILLR_14"] > -25.0)
        and (last_candle["RSI_3_1h"] < 50.0)
        and (last_candle["RSI_3_4h"] < 30.0)
        and (last_candle["AROONU_14_4h"] > 50.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 40.0))
      ):
        return True, f"exit_{mode_name}_d_4_90"
      elif (
        (last_candle["RSI_3"] > 66.0)
        and (last_candle["RSI_14"] < 52.0)
        and (last_candle["RSI_3_1h"] < 25.0)
        and (last_candle["RSI_3_4h"] < 25.0)
        and (last_candle["AROONU_14_4h"] > 50.0)
        and (
          isinstance(last_candle["STOCHRSIk_14_14_3_3_1d"], np.float64)
          and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 50.0)
        )
      ):
        return True, f"exit_{mode_name}_d_4_91"
      elif (
        (last_candle["RSI_3"] > 74.0)
        and (last_candle["RSI_14"] < 54.0)
        and (last_candle["RSI_3_1h"] < 40.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 25.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -25.0))
      ):
        return True, f"exit_{mode_name}_d_4_92"
      elif (
        (last_candle["RSI_3"] > 66.0)
        and (last_candle["RSI_14"] < 56.0)
        and (last_candle["RSI_3_15m"] < 50.0)
        and (last_candle["AROONU_14_1h"] > 75.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 70.0)
        and (last_candle["AROONU_14_4h"] > 50.0)
        and (
          isinstance(last_candle["STOCHRSIk_14_14_3_3_1d"], np.float64)
          and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 90.0)
        )
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 30.0))
      ):
        return True, f"exit_{mode_name}_d_4_93"
      elif (
        (last_candle["RSI_3"] > 74.0)
        and (last_candle["RSI_14"] < 56.0)
        and (last_candle["RSI_3_1h"] < 25.0)
        and (last_candle["RSI_3_4h"] < 45.0)
        and (last_candle["AROONU_14_1h"] > 75.0)
        and (
          isinstance(last_candle["STOCHRSIk_14_14_3_3_1d"], np.float64)
          and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 90.0)
        )
      ):
        return True, f"exit_{mode_name}_d_4_94"
      elif (
        (last_candle["RSI_3"] > 78.0)
        and (last_candle["WILLR_14"] > -18.0)
        and (last_candle["RSI_3_1h"] < 45.0)
        and (last_candle["RSI_3_4h"] < 40.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 10.0)
        and (isinstance(last_candle["AROONU_14_1d"], np.float64) and (last_candle["AROONU_14_1d"] > 75.0))
      ):
        return True, f"exit_{mode_name}_d_4_95"
      elif (
        (last_candle["RSI_3"] > 56.0)
        and (last_candle["RSI_14"] < 52.0)
        and (last_candle["RSI_3_1h"] < 45.0)
        and (last_candle["RSI_3_1d"] < 45.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_4_96"
      elif (
        (last_candle["RSI_3"] > 78.0)
        and (last_candle["RSI_14"] < 52.0)
        and (last_candle["RSI_3_1h"] < 35.0)
        and (last_candle["AROONU_14_4h"] > 50.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 30.0)
      ):
        return True, f"exit_{mode_name}_d_4_97"
      elif (
        (last_candle["RSI_3"] > 84.0)
        and (last_candle["RSI_3_15m"] > 66.0)
        and (last_candle["RSI_3_1h"] < 60.0)
        and (last_candle["RSI_3_4h"] < 60.0)
        and (last_candle["RSI_3_1d"] > 80.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_4_98"
      elif (
        (last_candle["RSI_3"] > 54.0)
        and (last_candle["RSI_14"] < 58.0)
        and (last_candle["RSI_3_1h"] < 65.0)
        and (last_candle["RSI_3_4h"] < 60.0)
        and (last_candle["AROONU_14_4h"] > 50.0)
        and (last_candle["STOCHk_14_3_3_4h"] > 40.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 80.0))
      ):
        return True, f"exit_{mode_name}_d_4_99"
      elif (
        (last_candle["RSI_3"] > 92.0)
        and (last_candle["RSI_14"] > 70.0)
        and (last_candle["RSI_3_15m"] > 70.0)
        and (last_candle["RSI_3_4h"] < 80.0)
      ):
        return True, f"exit_{mode_name}_d_4_100"
      elif (
        (last_candle["RSI_3"] > 78.0)
        and (last_candle["WILLR_14"] > -22.0)
        and (last_candle["RSI_3_1h"] < 50.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 40.0)
        and (isinstance(last_candle["ROC_9_4h"], np.float64) and (last_candle["ROC_9_4h"] > 40.0))
      ):
        return True, f"exit_{mode_name}_d_4_101"
      elif (
        (last_candle["RSI_3"] > 62.0)
        and (last_candle["RSI_14"] < 54.0)
        and (last_candle["RSI_3_1h"] < 60.0)
        and (last_candle["RSI_3_4h"] < 40.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 30.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 40.0))
      ):
        return True, f"exit_{mode_name}_d_4_102"
      elif (
        (last_candle["RSI_3"] > 72.0)
        and (last_candle["RSI_14"] < 62.0)
        and (last_candle["RSI_3_1h"] < 60.0)
        and (last_candle["RSI_14_4h"] > 70.0)
        and (isinstance(last_candle["ROC_9_4h"], np.float64) and (last_candle["ROC_9_4h"] > 80.0))
      ):
        return True, f"exit_{mode_name}_d_4_103"
      elif (
        (last_candle["RSI_3"] > 58.0)
        and (last_candle["RSI_14"] < 54.0)
        and (last_candle["RSI_3_1h"] < 60.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 40.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 90.0)
        and (last_candle["ROC_9_4h"] > 40.0)
      ):
        return True, f"exit_{mode_name}_d_4_104"
      elif (
        (last_candle["RSI_3"] > 72.0)
        and (last_candle["RSI_14"] < 54.0)
        and (last_candle["RSI_3_15m"] < 55.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 90.0)
        and (last_candle["ROC_9_4h"] > 25.0)
      ):
        return True, f"exit_{mode_name}_d_4_105"
      elif (
        (last_candle["RSI_3"] > 66.0)
        and (last_candle["RSI_14"] < 54.0)
        and (last_candle["RSI_3_1h"] < 50.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
        and (last_candle["RSI_14_4h"] > 70.0)
        and (last_candle["ROC_9_4h"] > 40.0)
      ):
        return True, f"exit_{mode_name}_d_4_106"
      elif (
        (last_candle["RSI_3"] > 68.0)
        and (last_candle["RSI_14"] < 54.0)
        and (last_candle["RSI_3_1h"] < 50.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 70.0)
        and (last_candle["RSI_14_4h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_4_107"
      elif (
        (last_candle["RSI_3"] > 50.0)
        and (last_candle["RSI_14"] < 54.0)
        and (last_candle["RSI_3_1h"] < 60.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 80.0)
      ):
        return True, f"exit_{mode_name}_d_4_108"
      elif (
        (last_candle["RSI_3"] > 70.0)
        and (last_candle["WILLR_14"] > -14.0)
        and (last_candle["RSI_3_1h"] < 50.0)
        and (last_candle["RSI_3_4h"] < 20.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 50.0))
      ):
        return True, f"exit_{mode_name}_d_4_109"
      elif (
        (last_candle["RSI_3"] > 66.0)
        and (last_candle["RSI_3_4h"] < 65.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
        and (last_candle["ROC_9_4h"] > 25.0)
      ):
        return True, f"exit_{mode_name}_d_4_110"
      elif (
        (last_candle["RSI_3"] > 44.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_1h"] < 50.0)
        and (last_candle["RSI_14_4h"] > 70.0)
        and (last_candle["AROONU_14_1h"] > 75.0)
        and (last_candle["AROONU_14_4h"] > 75.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 20.0))
      ):
        return True, f"exit_{mode_name}_d_4_111"
      elif (
        (last_candle["RSI_3"] > 74.0)
        and (last_candle["WILLR_14"] > -40.0)
        and (last_candle["RSI_14"] < 58.0)
        and (last_candle["RSI_3_1h"] < 35.0)
        and (last_candle["RSI_3_4h"] < 35.0)
        and (last_candle["RSI_3_1d"] < 60.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 30.0))
      ):
        return True, f"exit_{mode_name}_d_4_112"
      elif (
        (last_candle["RSI_3"] > 78.0)
        and (last_candle["WILLR_14"] > -8.0)
        and (last_candle["RSI_3_1d"] < 30.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
        and (isinstance(last_candle["ROC_9_4h"], np.float64) and (last_candle["ROC_9_4h"] > 10.0))
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -10.0))
      ):
        return True, f"exit_{mode_name}_d_4_113"
      elif (
        (last_candle["RSI_3"] > 78.0)
        and (last_candle["RSI_14"] < 56.0)
        and (last_candle["RSI_3_1h"] < 20.0)
        and (last_candle["RSI_3_4h"] < 30.0)
        and (last_candle["RSI_3_1d"] < 30.0)
      ):
        return True, f"exit_{mode_name}_d_4_114"
      elif (
        (last_candle["RSI_3"] > 72.0)
        and (last_candle["RSI_14"] < 54.0)
        and (last_candle["RSI_3_15m"] < 30.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_4_115"
      elif (
        (last_candle["RSI_3"] > 84.0)
        and (last_candle["RSI_3_1h"] < 15.0)
        and (last_candle["RSI_3_4h"] < 40.0)
        and (last_candle["AROONU_14_4h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_4_116"
      elif (
        (last_candle["RSI_3"] > 80.0)
        and (last_candle["RSI_3_1h"] < 50.0)
        and (last_candle["AROONU_14_1h"] > 80.0)
        and (last_candle["AROONU_14_4h"] > 80.0)
      ):
        return True, f"exit_{mode_name}_d_4_117"
      elif (
        (last_candle["RSI_3"] > 84.0)
        and (last_candle["RSI_3_1h"] < 20.0)
        and (last_candle["RSI_3_4h"] < 60.0)
        and (last_candle["AROONU_14_4h"] > 40.0)
      ):
        return True, f"exit_{mode_name}_d_4_118"
      elif (
        (last_candle["RSI_3"] > 80.0)
        and (last_candle["WILLR_14"] > -20.0)
        and (last_candle["RSI_3_1h"] < 60.0)
        and (last_candle["RSI_3_4h"] < 60.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 40.0)
      ):
        return True, f"exit_{mode_name}_d_4_119"
      elif (
        (last_candle["RSI_3"] > 48.0)
        and (last_candle["RSI_14"] < 54.0)
        and (last_candle["RSI_3_1h"] < 40.0)
        and (last_candle["AROONU_14_4h"] > 75.0)
      ):
        return True, f"exit_{mode_name}_d_4_120"
      elif (
        (last_candle["RSI_3"] > 54.0)
        and (last_candle["RSI_14"] < 52.0)
        and (last_candle["RSI_3_1h"] < 50.0)
        and (last_candle["RSI_14_4h"] > 85.0)
      ):
        return True, f"exit_{mode_name}_d_4_121"
      elif (
        (last_candle["RSI_3"] > 52.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_4h"] < 30.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_4_122"
      elif (
        (last_candle["RSI_3"] > 82.0)
        and (last_candle["WILLR_14"] > -10.0)
        and (last_candle["RSI_3_1h"] < 10.0)
        and (last_candle["RSI_3_1d"] < 30.0)
      ):
        return True, f"exit_{mode_name}_d_4_123"
      elif (
        (last_candle["RSI_3"] > 82.0)
        and (last_candle["RSI_3_1h"] < 15.0)
        and (
          isinstance(last_candle["STOCHRSIk_14_14_3_3_1d"], np.float64)
          and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 80.0)
        )
      ):
        return True, f"exit_{mode_name}_d_4_124"
      elif (
        (last_candle["RSI_3"] > 70.0)
        and (last_candle["WILLR_14"] > -10.0)
        and (last_candle["RSI_3_1h"] < 10.0)
        and (last_candle["RSI_3_4h"] < 40.0)
        and (last_candle["RSI_3_1d"] < 40.0)
        and (last_candle["close"] < (last_candle["high_max_30_1d"] * 0.50))
      ):
        return True, f"exit_{mode_name}_d_4_125"
      elif (
        (last_candle["RSI_3"] > 84.0)
        and (last_candle["RSI_3_1h"] < 15.0)
        and (last_candle["RSI_3_4h"] < 40.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_4_126"
      elif (
        (last_candle["RSI_3"] > 84.0)
        and (last_candle["RSI_3_1h"] < 10.0)
        and (last_candle["RSI_3_4h"] < 30.0)
        and (last_candle["RSI_3_1d"] < 40.0)
      ):
        return True, f"exit_{mode_name}_d_4_127"
      elif (last_candle["RSI_3"] > 88.0) and (last_candle["RSI_3_4h"] < 30.0) and (last_candle["AROONU_14_4h"] > 85.0):
        return True, f"exit_{mode_name}_d_4_128"
      elif (
        (last_candle["RSI_3"] > 80.0)
        and (last_candle["RSI_3_4h"] < 25.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 80.0))
      ):
        return True, f"exit_{mode_name}_d_4_129"
      elif (
        (last_candle["RSI_3"] > 68.0)
        and (last_candle["RSI_14_1h"] > 65.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 80.0)
        and (last_candle["CCI_20_change_pct_1h"] < -0.0)
      ):
        return True, f"exit_{mode_name}_d_4_130"
      elif (
        (last_candle["RSI_14"] < 44.0)
        and (last_candle["RSI_3_1h"] < 20.0)
        and (last_candle["RSI_3_4h"] < 30.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_4_131"
      elif (
        (last_candle["RSI_3"] > 74.0)
        and (last_candle["RSI_3_1h"] < 35.0)
        and (last_candle["RSI_3_4h"] < 35.0)
        and (last_candle["AROONU_14_1h"] > 50.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 40.0)
      ):
        return True, f"exit_{mode_name}_d_4_132"
      elif (
        (last_candle["RSI_3"] > 74.0)
        and (last_candle["AROONU_14_15m"] > 75.0)
        and (last_candle["AROONU_14_1h"] > 75.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 25.0))
      ):
        return True, f"exit_{mode_name}_d_4_133"
    elif 0.06 > current_profit >= 0.05:
      if (
        (last_candle["WILLR_14"] > -1.0)
        and (last_candle["RSI_14"] > 78.0)
        and (
          isinstance(last_candle["EMA_200_1h"], np.float64) and (last_candle["EMA_12_1h"] < last_candle["EMA_200_1h"])
        )
        and (
          isinstance(last_candle["EMA_200_4h"], np.float64) and (last_candle["EMA_12_4h"] < last_candle["EMA_200_4h"])
        )
        and (last_candle["KST_10_15_20_30_10_10_10_15_1h"] < last_candle["KSTs_9_1h"])
        and (last_candle["KST_10_15_20_30_10_10_10_15_4h"] < last_candle["KSTs_9_4h"])
      ):
        return True, f"exit_{mode_name}_d_5_1"
      elif (
        (last_candle["WILLR_14"] > -1.0)
        and (last_candle["RSI_14"] > 60.0)
        and (last_candle["CMF_20_1h"] < -0.0)
        and (
          isinstance(last_candle["EMA_200_1h"], np.float64) and (last_candle["EMA_12_1h"] < last_candle["EMA_200_1h"])
        )
        and (
          isinstance(last_candle["EMA_200_4h"], np.float64) and (last_candle["EMA_12_4h"] < last_candle["EMA_200_4h"])
        )
      ):
        return True, f"exit_{mode_name}_d_5_2"
      elif (
        (last_candle["WILLR_14"] > -20.0)
        and (last_candle["STOCHRSIk_14_14_3_3"] > 95.0)
        and (last_candle["CMF_20_1h"] < -0.0)
        and (last_candle["CMF_20_4h"] < -0.0)
        and (
          (last_candle["STOCHRSIk_14_14_3_3_4h"] > 20.0) and (last_candle["STOCHRSIk_14_14_3_3_change_pct_4h"] < -10.0)
        )
      ):
        return True, f"exit_{mode_name}_d_5_3"
      elif (
        (last_candle["WILLR_14"] > -30.0)
        and (last_candle["RSI_14"] > 65.0)
        and (last_candle["STOCHRSIk_14_14_3_3"] > 95.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 70.0)
        and (
          isinstance(last_candle["EMA_200_1h"], np.float64) and (last_candle["EMA_12_1h"] < last_candle["EMA_200_1h"])
        )
        and (
          isinstance(last_candle["EMA_200_4h"], np.float64) and (last_candle["EMA_12_4h"] < last_candle["EMA_200_4h"])
        )
      ):
        return True, f"exit_{mode_name}_d_5_4"
      elif (
        (last_candle["WILLR_14"] > -10.0)
        and (last_candle["RSI_14"] > 64.0)
        and (last_candle["ROC_9_1h"] < -5.0)
        and (last_candle["ROC_9_4h"] < -5.0)
      ):
        return True, f"exit_{mode_name}_d_5_5"
      elif (
        (last_candle["RSI_3"] > 70.0)
        and (last_candle["STOCHRSIk_14_14_3_3"] > 70.0)
        and (last_candle["RSI_14"] < 40.0)
        and (last_candle["ROC_9_1h"] < -10.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 50.0))
      ):
        return True, f"exit_{mode_name}_d_5_6"
      elif (
        (last_candle["RSI_14"] < 50.0)
        and (last_candle["STOCHRSIk_14_14_3_3"] > 70.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -40.0))
      ):
        return True, f"exit_{mode_name}_d_5_7"
      elif (
        (last_candle["WILLR_14"] > -10.0)
        and (last_candle["STOCHRSIk_14_14_3_3"] > 95.0)
        and (last_candle["CMF_20_1h"] < -0.1)
        and (last_candle["CMF_20_4h"] < -0.1)
        and (last_candle["change_pct_1d"] < -5.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 15.0))
      ):
        return True, f"exit_{mode_name}_d_5_8"
      elif (
        (last_candle["WILLR_14"] > -8.0)
        and (last_candle["RSI_3"] > 95.0)
        and (last_candle["change_pct_4h"] < -5.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 30.0))
      ):
        return True, f"exit_{mode_name}_d_5_9"
      elif (
        (last_candle["WILLR_14"] > -20.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["ROC_9_1h"] < -10.0)
        and (last_candle["ROC_9_4h"] < -10.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 10.0))
      ):
        return True, f"exit_{mode_name}_d_5_10"
      elif (
        (last_candle["RSI_3"] > 75.0)
        and (last_candle["RSI_14"] < 45.0)
        and (last_candle["ROC_9_15m"] < -10.0)
        and (last_candle["ROC_9_1h"] < -10.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -20.0))
      ):
        return True, f"exit_{mode_name}_d_5_11"
      elif (
        (last_candle["RSI_3"] > 70.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_4h"] < 10.0)
        and (last_candle["ROC_9_1h"] < -20.0)
        and (last_candle["ROC_9_4h"] < -20.0)
      ):
        return True, f"exit_{mode_name}_d_5_12"
      elif (last_candle["RSI_3"] > 80.0) and (last_candle["RSI_3_4h"] < 5.0) and (last_candle["ROC_9_4h"] < -25.0):
        return True, f"exit_{mode_name}_d_5_13"
      elif (
        (last_candle["RSI_3"] > 90.0)
        and (last_candle["WILLR_14"] > -12.0)
        and (last_candle["RSI_3_4h"] < 5.0)
        and (last_candle["AROONU_14_4h"] > 25.0)
      ):
        return True, f"exit_{mode_name}_d_5_14"
      elif (last_candle["RSI_3"] > 86.0) and (last_candle["RSI_14"] > 58.0) and (last_candle["ROC_9_4h"] < -30.0):
        return True, f"exit_{mode_name}_d_5_15"
      elif (
        (last_candle["RSI_3"] > 70.0)
        and (last_candle["AROONU_14_4h"] > 25.0)
        and (last_candle["ROC_9_4h"] < -25.0)
        and (last_candle["AROONU_14_1d"] > 50.0)
        and (last_candle["change_pct_1d"] < -15.0)
      ):
        return True, f"exit_{mode_name}_d_5_16"
      elif (
        (last_candle["RSI_3"] > 80.0)
        and (last_candle["WILLR_14"] > -35.0)
        and (last_candle["RSI_3_1h"] < 10.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 90.0)
        and (last_candle["ROC_9_4h"] > 30.0)
      ):
        return True, f"exit_{mode_name}_d_5_17"
      elif (
        (last_candle["RSI_3"] > 75.0)
        and (last_candle["RSI_14"] > 60.0)
        and (last_candle["RSI_3_4h"] < 20.0)
        and (last_candle["ROC_2_1d"] < -50.0)
      ):
        return True, f"exit_{mode_name}_d_5_18"
      elif (
        (last_candle["RSI_3"] > 84.0)
        and (last_candle["RSI_14"] > 64.0)
        and (last_candle["RSI_3_4h"] < 10.0)
        and (
          isinstance(last_candle["STOCHRSIk_14_14_3_3_1d"], np.float64)
          and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 70.0)
        )
      ):
        return True, f"exit_{mode_name}_d_5_19"
      elif (
        (last_candle["RSI_3"] > 42.0)
        and (last_candle["RSI_14"] < 48.0)
        and (last_candle["RSI_3_1h"] < 10.0)
        and (last_candle["AROONU_14_1h"] > 25.0)
      ):
        return True, f"exit_{mode_name}_d_5_20"
      elif (
        (last_candle["RSI_3"] > 50.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_1h"] < 20.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 90.0)
      ):
        return True, f"exit_{mode_name}_d_5_21"
      elif (
        (last_candle["RSI_3"] > 90.0)
        and (last_candle["WILLR_14"] > -10.0)
        and (last_candle["change_pct_4h"] < -5.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -30.0))
      ):
        return True, f"exit_{mode_name}_d_5_22"
      elif (
        (last_candle["RSI_3"] > 75.0)
        and (last_candle["WILLR_14"] > -30.0)
        and (last_candle["RSI_3_1h"] < 15.0)
        and (last_candle["RSI_3_1d"] < 5.0)
      ):
        return True, f"exit_{mode_name}_d_5_23"
      elif (
        (last_candle["RSI_3"] > 84.0)
        and (last_candle["RSI_14"] > 64.0)
        and (last_candle["WILLR_14"] > -35.0)
        and (last_candle["RSI_3_4h"] < 30.0)
        and (last_candle["AROONU_14_4h"] > 75.0)
      ):
        return True, f"exit_{mode_name}_d_5_24"
      elif (
        (last_candle["RSI_3"] > 70.0)
        and (last_candle["WILLR_14"] > -12.0)
        and (last_candle["RSI_3_4h"] < 10.0)
        and (last_candle["ROC_9_4h"] < -15.0)
        and (
          isinstance(last_candle["STOCHRSIk_14_14_3_3_1d"], np.float64)
          and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 50.0)
        )
      ):
        return True, f"exit_{mode_name}_d_5_25"
      elif (
        (last_candle["RSI_3"] > 65.0)
        and (last_candle["WILLR_14"] > -12.0)
        and (last_candle["RSI_3_4h"] < 15.0)
        and (last_candle["ROC_9_4h"] < -20.0)
      ):
        return True, f"exit_{mode_name}_d_5_26"
      elif (
        (last_candle["RSI_3"] > 65.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_1h"] < 20.0)
        and (last_candle["RSI_3_4h"] < 20.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 20.0)
      ):
        return True, f"exit_{mode_name}_d_5_27"
      elif (
        (last_candle["RSI_3"] > 60.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_15m"] < 10.0)
        and (last_candle["ROC_9_4h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_5_28"
      elif (
        (last_candle["RSI_3"] > 75.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_1h"] < 20.0)
        and (last_candle["RSI_3_4h"] < 20.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 30.0)
      ):
        return True, f"exit_{mode_name}_d_5_29"
      elif (
        (last_candle["RSI_3"] > 70.0)
        and (last_candle["RSI_3_1h"] < 25.0)
        and (last_candle["RSI_3_4h"] < 10.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 70.0)
      ):
        return True, f"exit_{mode_name}_d_5_30"
      elif (
        (last_candle["RSI_3"] > 60.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_1h"] < 15.0)
        and (last_candle["RSI_3_4h"] < 15.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 25.0)
      ):
        return True, f"exit_{mode_name}_d_5_31"
      elif (
        (last_candle["RSI_3"] > 70.0)
        and (last_candle["RSI_3_1h"] < 15.0)
        and (last_candle["ROC_2_4h"] < -30.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 30.0)
      ):
        return True, f"exit_{mode_name}_d_5_32"
      elif (
        (last_candle["RSI_3"] > 70.0)
        and (last_candle["WILLR_14"] > -10.0)
        and (last_candle["ROC_2_1h"] < -10.0)
        and (last_candle["ROC_9_1h"] > 30.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_5_33"
      elif (
        (last_candle["RSI_3"] > 65.0)
        and (last_candle["RSI_3_15m"] < 30.0)
        and (last_candle["RSI_14_1h"] > 80.0)
        and (last_candle["ROC_9_1h"] > 40.0)
      ):
        return True, f"exit_{mode_name}_d_5_34"
      elif (
        (last_candle["RSI_3"] > 80.0)
        and (last_candle["WILLR_14"] > -10.0)
        and (last_candle["RSI_3_1d"] < 25.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 75.0)
      ):
        return True, f"exit_{mode_name}_d_5_35"
      elif (
        (last_candle["RSI_3"] > 65.0)
        and (last_candle["WILLR_14"] > -35.0)
        and (last_candle["ROC_9_4h"] < -25.0)
        and (last_candle["RSI_3_1d"] < 25.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_5_36"
      elif (
        (last_candle["RSI_3"] > 74.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_1h"] < 20.0)
        and (last_candle["RSI_3_1d"] < 25.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_5_37"
      elif (
        (last_candle["RSI_3"] > 65.0)
        and (last_candle["WILLR_14"] > -35.0)
        and (last_candle["RSI_3_4h"] < 10.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 20.0)
      ):
        return True, f"exit_{mode_name}_d_5_38"
      elif (
        (last_candle["RSI_3"] > 91.0)
        and (last_candle["WILLR_14"] > -9.0)
        and (last_candle["CMF_20_4h"] < -0.0)
        and (last_candle["RSI_3_4h"] < 10.0)
      ):
        return True, f"exit_{mode_name}_d_5_39"
      elif (
        (last_candle["RSI_3"] > 65.0)
        and (last_candle["WILLR_14"] > -35.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 30.0)
        and (
          isinstance(last_candle["STOCHRSIk_14_14_3_3_1d"], np.float64)
          and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 90.0)
        )
      ):
        return True, f"exit_{mode_name}_d_5_40"
      elif (
        (last_candle["RSI_3"] > 75.0)
        and (last_candle["WILLR_14"] > -30.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 25.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 50.0))
      ):
        return True, f"exit_{mode_name}_d_5_41"
      elif (
        (last_candle["RSI_3"] > 70.0)
        and (last_candle["WILLR_14"] > -45.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 30.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 40.0))
        and (
          isinstance(last_candle["STOCHRSIk_14_14_3_3_1d"], np.float64)
          and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 70.0)
        )
      ):
        return True, f"exit_{mode_name}_d_5_42"
      elif (
        (last_candle["RSI_3"] > 80.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_1h"] < 15.0)
        and (last_candle["RSI_3_4h"] < 40.0)
        and (
          isinstance(last_candle["STOCHRSIk_14_14_3_3_1d"], np.float64)
          and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 90.0)
        )
      ):
        return True, f"exit_{mode_name}_d_5_43"
      elif (
        (last_candle["RSI_3"] > 50.0)
        and (last_candle["WILLR_14"] > -25.0)
        and (last_candle["RSI_3_4h"] < 30.0)
        and (last_candle["RSI_3_1d"] < 25.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -30.0))
      ):
        return True, f"exit_{mode_name}_d_5_44"
      elif (last_candle["RSI_3"] > 86.0) and (last_candle["WILLR_14"] > -14.0) and (last_candle["RSI_3_1h"] < 10.0):
        return True, f"exit_{mode_name}_d_5_45"
      elif (
        (last_candle["RSI_3"] > 70.0)
        and (last_candle["RSI_3_1h"] < 15.0)
        and (last_candle["RSI_3_4h"] < 10.0)
        and (last_candle["ROC_2_1d"] < -20.0)
      ):
        return True, f"exit_{mode_name}_d_5_46"
      elif (
        (last_candle["RSI_3"] > 78.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 80.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 40.0)
        and (last_candle["change_pct_1d"] < -5.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -5.0))
      ):
        return True, f"exit_{mode_name}_d_5_47"
      elif (
        (last_candle["RSI_3"] > 45.0)
        and (last_candle["RSI_14"] < 52.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (last_candle["RSI_3_4h"] < 20.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_5_48"
      elif (
        (last_candle["RSI_3"] > 70.0)
        and (last_candle["WILLR_14"] > -12.0)
        and (last_candle["RSI_3_4h"] < 20.0)
        and (last_candle["change_pct_1d"] < -5.0)
        and (
          isinstance(last_candle["STOCHRSIk_14_14_3_3_1d"], np.float64)
          and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 50.0)
        )
      ):
        return True, f"exit_{mode_name}_d_5_49"
      elif (
        (last_candle["RSI_3"] > 80.0)
        and (last_candle["WILLR_14"] > -12.0)
        and (last_candle["RSI_3_1d"] < 10.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 90.0)
      ):
        return True, f"exit_{mode_name}_d_5_50"
      elif (
        (last_candle["RSI_3"] > 58.0)
        and (last_candle["RSI_14"] < 54.0)
        and (last_candle["RSI_3_4h"] < 20.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_5_51"
      elif (
        (last_candle["RSI_3"] > 72.0)
        and (last_candle["RSI_14"] > 52.0)
        and (last_candle["WILLR_14"] > -10.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 70.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -15.0))
      ):
        return True, f"exit_{mode_name}_d_5_52"
      elif (
        (last_candle["RSI_3"] > 70.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["WILLR_14"] > -25.0)
        and (last_candle["RSI_3_1h"] < 20.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
        and (
          isinstance(last_candle["STOCHRSIk_14_14_3_3_1d"], np.float64)
          and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 50.0)
        )
      ):
        return True, f"exit_{mode_name}_d_5_53"
      elif (
        (last_candle["RSI_3"] > 70.0)
        and (last_candle["RSI_14"] < 54.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
        and (last_candle["ROC_9_4h"] < -10.0)
        and (last_candle["change_pct_1d"] < -10.0)
      ):
        return True, f"exit_{mode_name}_d_5_54"
      elif (
        (last_candle["RSI_3"] > 86.0)
        and (last_candle["WILLR_14"] > -22.0)
        and (last_candle["ROC_9_4h"] < -5.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 10.0))
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_5_55"
      elif (
        (last_candle["RSI_3"] > 60.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (last_candle["RSI_3_4h"] < 25.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -30.0))
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 10.0)
      ):
        return True, f"exit_{mode_name}_d_5_56"
      elif (
        (last_candle["RSI_3"] > 50.0)
        and (last_candle["RSI_14"] < 44.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -30.0))
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 70.0)
      ):
        return True, f"exit_{mode_name}_d_5_57"
      elif (
        (last_candle["RSI_3"] > 70.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (last_candle["RSI_3_4h"] < 30.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -15.0))
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_5_58"
      elif (
        (last_candle["RSI_3"] > 85.0)
        and (last_candle["WILLR_14"] > -20.0)
        and (last_candle["RSI_3_4h"] < 25.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -15.0))
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 40.0)
      ):
        return True, f"exit_{mode_name}_d_5_59"
      elif (
        (last_candle["RSI_3"] > 65.0)
        and (last_candle["RSI_14"] < 48.0)
        and (last_candle["RSI_14_4h"] > 65.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_5_60"
      elif (
        (last_candle["RSI_3"] > 90.0)
        and (last_candle["WILLR_14"] > -25.0)
        and (last_candle["RSI_3_4h"] < 10.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 30.0)
      ):
        return True, f"exit_{mode_name}_d_5_61"
      elif (
        (last_candle["RSI_3"] > 78.0)
        and (last_candle["WILLR_14"] > -10.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (last_candle["RSI_3_4h"] < 20.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 20.0))
        and (last_candle["change_pct_1d"] < -5.0)
      ):
        return True, f"exit_{mode_name}_d_5_62"
      elif (
        (last_candle["RSI_3"] > 60.0)
        and (last_candle["RSI_3_1d"] < 25.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 80.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 30.0)
      ):
        return True, f"exit_{mode_name}_d_5_63"
      elif (
        (last_candle["RSI_3"] > 80.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (last_candle["RSI_3_4h"] < 30.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 30.0))
      ):
        return True, f"exit_{mode_name}_d_5_64"
      elif (
        (last_candle["RSI_3"] > 60.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_1h"] < 20.0)
        and (last_candle["RSI_3_4h"] < 15.0)
      ):
        return True, f"exit_{mode_name}_d_5_65"
      elif (
        (last_candle["RSI_3"] > 74.0)
        and (last_candle["RSI_14"] < 56.0)
        and (last_candle["RSI_3_1h"] < 20.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_5_66"
      elif (
        (last_candle["RSI_3"] > 50.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 80.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -25.0))
      ):
        return True, f"exit_{mode_name}_d_5_67"
      elif (
        (last_candle["RSI_3"] > 76.0)
        and (last_candle["RSI_14"] < 56.0)
        and (last_candle["RSI_3_1h"] < 25.0)
        and (last_candle["ROC_2_4h"] < -30.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 25.0)
      ):
        return True, f"exit_{mode_name}_d_5_68"
      elif (
        (last_candle["RSI_3"] > 92.0)
        and (last_candle["ROC_9_4h"] > 20.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
        and (last_candle["change_pct_4h"] < -5.0)
      ):
        return True, f"exit_{mode_name}_d_5_69"
      elif (
        (last_candle["RSI_3"] > 58.0)
        and (last_candle["RSI_14"] < 48.0)
        and (last_candle["RSI_3_1h"] < 25.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 20.0)
      ):
        return True, f"exit_{mode_name}_d_5_70"
      elif (
        (last_candle["RSI_3"] > 56.0)
        and (last_candle["RSI_14"] < 52.0)
        and (last_candle["RSI_3_4h"] < 25.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 20.0)
      ):
        return True, f"exit_{mode_name}_d_5_71"
      elif (
        (last_candle["RSI_3"] > 70.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_1h"] < 10.0)
        and (last_candle["AROONU_14_4h"] > 25.0)
      ):
        return True, f"exit_{mode_name}_d_5_72"
      elif (
        (last_candle["RSI_3"] > 70.0)
        and (last_candle["RSI_3_1h"] < 25.0)
        and (last_candle["RSI_3_4h"] < 15.0)
        and (last_candle["ROC_9_4h"] < -20.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -25.0))
      ):
        return True, f"exit_{mode_name}_d_5_73"
      elif (
        (last_candle["RSI_3"] > 94.0)
        and (last_candle["WILLR_14"] > -10.0)
        and (last_candle["RSI_3_4h"] < 25.0)
        and (last_candle["RSI_3_1d"] < 25.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_5_74"
      elif (
        (last_candle["RSI_3"] > 88.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (last_candle["RSI_3_4h"] < 20.0)
        and (
          isinstance(last_candle["STOCHRSIk_14_14_3_3_1d"], np.float64)
          and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 50.0)
        )
      ):
        return True, f"exit_{mode_name}_d_5_75"
      elif (
        (last_candle["RSI_3"] > 60.0)
        and (last_candle["RSI_14"] < 58.0)
        and (last_candle["ROC_9_1h"] > 80.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 80.0)
      ):
        return True, f"exit_{mode_name}_d_5_76"
      elif (
        (last_candle["RSI_3"] > 68.0)
        and (last_candle["RSI_14"] < 54.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 50.0))
      ):
        return True, f"exit_{mode_name}_d_5_77"
      elif (
        (last_candle["RSI_3"] > 78.0)
        and (last_candle["WILLR_14"] > -24.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (last_candle["RSI_3_4h"] < 20.0)
        and (last_candle["RSI_3_1d"] < 20.0)
      ):
        return True, f"exit_{mode_name}_d_5_78"
      elif (
        (last_candle["RSI_3"] > 84.0)
        and (last_candle["WILLR_14"] > -10.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (last_candle["RSI_3_4h"] < 10.0)
      ):
        return True, f"exit_{mode_name}_d_5_79"
      elif (
        (last_candle["RSI_3"] > 64.0)
        and (last_candle["RSI_14"] < 54.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 50.0))
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 25.0)
      ):
        return True, f"exit_{mode_name}_d_5_80"
      elif (
        (last_candle["RSI_3"] > 76.0)
        and (last_candle["WILLR_14"] > -18.0)
        and (last_candle["RSI_3_1h"] < 25.0)
        and (last_candle["RSI_3_4h"] < 25.0)
        and (isinstance(last_candle["RSI_14_1d"], np.float64) and (last_candle["RSI_14_1d"] > 50.0))
      ):
        return True, f"exit_{mode_name}_d_5_81"
      elif (
        (last_candle["RSI_3"] > 74.0)
        and (last_candle["WILLR_14"] > -18.0)
        and (last_candle["RSI_3_4h"] < 30.0)
        and (last_candle["RSI_3_1d"] < 15.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 40.0)
      ):
        return True, f"exit_{mode_name}_d_5_82"
      elif (
        (last_candle["RSI_3"] > 64.0)
        and (last_candle["RSI_14"] < 54.0)
        and (last_candle["RSI_3_1h"] < 40.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 40.0)
      ):
        return True, f"exit_{mode_name}_d_5_83"
      elif (
        (last_candle["RSI_3"] > 82.0)
        and (last_candle["WILLR_14"] > -10.0)
        and (last_candle["RSI_3_4h"] < 30.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 20.0)
      ):
        return True, f"exit_{mode_name}_d_5_84"
      elif (
        (last_candle["RSI_3"] > 80.0)
        and (last_candle["WILLR_14"] > -16.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (last_candle["RSI_3_4h"] < 40.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_5_85"
      elif (
        (last_candle["RSI_3"] > 86.0)
        and (last_candle["RSI_14_4h"] > 80.0)
        and (last_candle["ROC_2_1h"] < -5.0)
        and (last_candle["ROC_9_1h"] > 5.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_5_86"
      elif (
        (last_candle["RSI_3"] > 58.0)
        and (last_candle["RSI_14"] < 52.0)
        and (last_candle["RSI_3_1h"] < 45.0)
        and (last_candle["RSI_3_4h"] < 50.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_5_87"
      elif (
        (last_candle["RSI_3"] > 80.0)
        and (last_candle["WILLR_14"] > -28.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 40.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
        and (last_candle["change_pct_1h"] < -2.0)
      ):
        return True, f"exit_{mode_name}_d_5_88"
      elif (
        (last_candle["RSI_3"] > 70.0)
        and (last_candle["RSI_14"] < 48.0)
        and (last_candle["ROC_9_1h"] < -5.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 25.0))
      ):
        return True, f"exit_{mode_name}_d_5_89"
      elif (
        (last_candle["RSI_3"] > 84.0)
        and (last_candle["WILLR_14"] > -25.0)
        and (last_candle["RSI_3_1h"] < 50.0)
        and (last_candle["RSI_3_4h"] < 30.0)
        and (last_candle["AROONU_14_4h"] > 50.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 40.0))
      ):
        return True, f"exit_{mode_name}_d_5_90"
      elif (
        (last_candle["RSI_3"] > 64.0)
        and (last_candle["RSI_14"] < 54.0)
        and (last_candle["RSI_3_1h"] < 25.0)
        and (last_candle["RSI_3_4h"] < 25.0)
        and (last_candle["AROONU_14_4h"] > 50.0)
        and (
          isinstance(last_candle["STOCHRSIk_14_14_3_3_1d"], np.float64)
          and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 50.0)
        )
      ):
        return True, f"exit_{mode_name}_d_5_91"
      elif (
        (last_candle["RSI_3"] > 72.0)
        and (last_candle["RSI_14"] < 56.0)
        and (last_candle["RSI_3_1h"] < 40.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 25.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -25.0))
      ):
        return True, f"exit_{mode_name}_d_5_92"
      elif (
        (last_candle["RSI_3"] > 64.0)
        and (last_candle["RSI_14"] < 58.0)
        and (last_candle["RSI_3_15m"] < 50.0)
        and (last_candle["AROONU_14_1h"] > 75.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 70.0)
        and (last_candle["AROONU_14_4h"] > 50.0)
        and (
          isinstance(last_candle["STOCHRSIk_14_14_3_3_1d"], np.float64)
          and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 90.0)
        )
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 30.0))
      ):
        return True, f"exit_{mode_name}_d_5_93"
      elif (
        (last_candle["RSI_3"] > 72.0)
        and (last_candle["RSI_14"] < 58.0)
        and (last_candle["RSI_3_1h"] < 25.0)
        and (last_candle["RSI_3_4h"] < 45.0)
        and (last_candle["AROONU_14_1h"] > 75.0)
        and (
          isinstance(last_candle["STOCHRSIk_14_14_3_3_1d"], np.float64)
          and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 90.0)
        )
      ):
        return True, f"exit_{mode_name}_d_5_94"
      elif (
        (last_candle["RSI_3"] > 76.0)
        and (last_candle["WILLR_14"] > -20.0)
        and (last_candle["RSI_3_1h"] < 45.0)
        and (last_candle["RSI_3_4h"] < 40.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 10.0)
        and (isinstance(last_candle["AROONU_14_1d"], np.float64) and (last_candle["AROONU_14_1d"] > 75.0))
      ):
        return True, f"exit_{mode_name}_d_5_95"
      elif (
        (last_candle["RSI_3"] > 54.0)
        and (last_candle["RSI_14"] < 54.0)
        and (last_candle["RSI_3_1h"] < 45.0)
        and (last_candle["RSI_3_1d"] < 45.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_5_96"
      elif (
        (last_candle["RSI_3"] > 76.0)
        and (last_candle["RSI_14"] < 54.0)
        and (last_candle["RSI_3_1h"] < 35.0)
        and (last_candle["AROONU_14_4h"] > 50.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 30.0)
      ):
        return True, f"exit_{mode_name}_d_5_97"
      elif (
        (last_candle["RSI_3"] > 82.0)
        and (last_candle["RSI_3_15m"] > 64.0)
        and (last_candle["RSI_3_1h"] < 60.0)
        and (last_candle["RSI_3_4h"] < 60.0)
        and (last_candle["RSI_3_1d"] > 80.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_5_98"
      elif (
        (last_candle["RSI_3"] > 52.0)
        and (last_candle["RSI_14"] < 60.0)
        and (last_candle["RSI_3_1h"] < 65.0)
        and (last_candle["RSI_3_4h"] < 60.0)
        and (last_candle["AROONU_14_4h"] > 50.0)
        and (last_candle["STOCHk_14_3_3_4h"] > 40.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 80.0))
      ):
        return True, f"exit_{mode_name}_d_5_99"
      elif (
        (last_candle["RSI_3"] > 90.0)
        and (last_candle["RSI_14"] > 68.0)
        and (last_candle["RSI_3_15m"] > 70.0)
        and (last_candle["RSI_3_4h"] < 80.0)
      ):
        return True, f"exit_{mode_name}_d_5_100"
      elif (
        (last_candle["RSI_3"] > 76.0)
        and (last_candle["WILLR_14"] > -24.0)
        and (last_candle["RSI_3_1h"] < 50.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 40.0)
        and (isinstance(last_candle["ROC_9_4h"], np.float64) and (last_candle["ROC_9_4h"] > 40.0))
      ):
        return True, f"exit_{mode_name}_d_5_101"
      elif (
        (last_candle["RSI_3"] > 60.0)
        and (last_candle["RSI_14"] < 56.0)
        and (last_candle["RSI_3_1h"] < 60.0)
        and (last_candle["RSI_3_4h"] < 40.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 30.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 40.0))
      ):
        return True, f"exit_{mode_name}_d_5_102"
      elif (
        (last_candle["RSI_3"] > 70.0)
        and (last_candle["RSI_14"] < 64.0)
        and (last_candle["RSI_3_1h"] < 60.0)
        and (last_candle["RSI_14_4h"] > 70.0)
        and (isinstance(last_candle["ROC_9_4h"], np.float64) and (last_candle["ROC_9_4h"] > 80.0))
      ):
        return True, f"exit_{mode_name}_d_5_103"
      elif (
        (last_candle["RSI_3"] > 56.0)
        and (last_candle["RSI_14"] < 56.0)
        and (last_candle["RSI_3_1h"] < 60.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 40.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 90.0)
        and (last_candle["ROC_9_4h"] > 40.0)
      ):
        return True, f"exit_{mode_name}_d_5_104"
      elif (
        (last_candle["RSI_3"] > 70.0)
        and (last_candle["RSI_14"] < 56.0)
        and (last_candle["RSI_3_15m"] < 55.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 90.0)
        and (last_candle["ROC_9_4h"] > 25.0)
      ):
        return True, f"exit_{mode_name}_d_5_105"
      elif (
        (last_candle["RSI_3"] > 64.0)
        and (last_candle["RSI_14"] < 56.0)
        and (last_candle["RSI_3_1h"] < 50.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
        and (last_candle["RSI_14_4h"] > 70.0)
        and (last_candle["ROC_9_4h"] > 40.0)
      ):
        return True, f"exit_{mode_name}_d_5_106"
      elif (
        (last_candle["RSI_3"] > 66.0)
        and (last_candle["RSI_14"] < 56.0)
        and (last_candle["RSI_3_1h"] < 50.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 70.0)
        and (last_candle["RSI_14_4h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_5_107"
      elif (
        (last_candle["RSI_3"] > 48.0)
        and (last_candle["RSI_14"] < 56.0)
        and (last_candle["RSI_3_1h"] < 60.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 80.0)
      ):
        return True, f"exit_{mode_name}_d_5_108"
      elif (
        (last_candle["RSI_3"] > 68.0)
        and (last_candle["WILLR_14"] > -16.0)
        and (last_candle["RSI_3_1h"] < 50.0)
        and (last_candle["RSI_3_4h"] < 20.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 50.0))
      ):
        return True, f"exit_{mode_name}_d_5_109"
      elif (
        (last_candle["RSI_3"] > 64.0)
        and (last_candle["RSI_3_4h"] < 65.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
        and (last_candle["ROC_9_4h"] > 25.0)
      ):
        return True, f"exit_{mode_name}_d_5_110"
      elif (
        (last_candle["RSI_3"] > 42.0)
        and (last_candle["RSI_14"] < 52.0)
        and (last_candle["RSI_3_1h"] < 50.0)
        and (last_candle["RSI_14_4h"] > 70.0)
        and (last_candle["AROONU_14_1h"] > 75.0)
        and (last_candle["AROONU_14_4h"] > 75.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 20.0))
      ):
        return True, f"exit_{mode_name}_d_5_111"
      elif (
        (last_candle["RSI_3"] > 72.0)
        and (last_candle["WILLR_14"] > -45.0)
        and (last_candle["RSI_14"] < 60.0)
        and (last_candle["RSI_3_1h"] < 35.0)
        and (last_candle["RSI_3_4h"] < 35.0)
        and (last_candle["RSI_3_1d"] < 60.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 30.0))
      ):
        return True, f"exit_{mode_name}_d_5_112"
      elif (
        (last_candle["RSI_3"] > 76.0)
        and (last_candle["WILLR_14"] > -10.0)
        and (last_candle["RSI_3_1d"] < 30.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
        and (isinstance(last_candle["ROC_9_4h"], np.float64) and (last_candle["ROC_9_4h"] > 10.0))
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -10.0))
      ):
        return True, f"exit_{mode_name}_d_5_113"
      elif (
        (last_candle["RSI_3"] > 76.0)
        and (last_candle["RSI_14"] < 58.0)
        and (last_candle["RSI_3_1h"] < 20.0)
        and (last_candle["RSI_3_4h"] < 30.0)
        and (last_candle["RSI_3_1d"] < 30.0)
      ):
        return True, f"exit_{mode_name}_d_5_114"
      elif (
        (last_candle["RSI_3"] > 70.0)
        and (last_candle["RSI_14"] < 56.0)
        and (last_candle["RSI_3_15m"] < 30.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_5_115"
      elif (
        (last_candle["RSI_3"] > 82.0)
        and (last_candle["RSI_3_1h"] < 15.0)
        and (last_candle["RSI_3_4h"] < 40.0)
        and (last_candle["AROONU_14_4h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_5_116"
      elif (
        (last_candle["RSI_3"] > 78.0)
        and (last_candle["RSI_3_1h"] < 50.0)
        and (last_candle["AROONU_14_1h"] > 80.0)
        and (last_candle["AROONU_14_4h"] > 80.0)
      ):
        return True, f"exit_{mode_name}_d_5_117"
      elif (
        (last_candle["RSI_3"] > 82.0)
        and (last_candle["RSI_3_1h"] < 20.0)
        and (last_candle["RSI_3_4h"] < 60.0)
        and (last_candle["AROONU_14_4h"] > 40.0)
      ):
        return True, f"exit_{mode_name}_d_5_118"
      elif (
        (last_candle["RSI_3"] > 78.0)
        and (last_candle["WILLR_14"] > -20.0)
        and (last_candle["RSI_3_1h"] < 60.0)
        and (last_candle["RSI_3_4h"] < 60.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 40.0)
      ):
        return True, f"exit_{mode_name}_d_5_119"
      elif (
        (last_candle["RSI_3"] > 46.0)
        and (last_candle["RSI_14"] < 56.0)
        and (last_candle["RSI_3_1h"] < 40.0)
        and (last_candle["AROONU_14_4h"] > 75.0)
      ):
        return True, f"exit_{mode_name}_d_5_120"
      elif (
        (last_candle["RSI_3"] > 52.0)
        and (last_candle["RSI_14"] < 54.0)
        and (last_candle["RSI_3_1h"] < 50.0)
        and (last_candle["RSI_14_4h"] > 85.0)
      ):
        return True, f"exit_{mode_name}_d_5_121"
      elif (
        (last_candle["RSI_3"] > 50.0)
        and (last_candle["RSI_14"] < 52.0)
        and (last_candle["RSI_3_4h"] < 30.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_5_122"
      elif (
        (last_candle["RSI_3"] > 80.0)
        and (last_candle["WILLR_14"] > -12.0)
        and (last_candle["RSI_3_1h"] < 10.0)
        and (last_candle["RSI_3_1d"] < 30.0)
      ):
        return True, f"exit_{mode_name}_d_5_123"
      elif (
        (last_candle["RSI_3"] > 80.0)
        and (last_candle["RSI_3_1h"] < 15.0)
        and (
          isinstance(last_candle["STOCHRSIk_14_14_3_3_1d"], np.float64)
          and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 80.0)
        )
      ):
        return True, f"exit_{mode_name}_d_5_124"
      elif (
        (last_candle["RSI_3"] > 68.0)
        and (last_candle["WILLR_14"] > -12.0)
        and (last_candle["RSI_3_1h"] < 10.0)
        and (last_candle["RSI_3_4h"] < 40.0)
        and (last_candle["RSI_3_1d"] < 40.0)
        and (last_candle["close"] < (last_candle["high_max_30_1d"] * 0.50))
      ):
        return True, f"exit_{mode_name}_d_5_125"
      elif (
        (last_candle["RSI_3"] > 82.0)
        and (last_candle["RSI_3_1h"] < 15.0)
        and (last_candle["RSI_3_4h"] < 40.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_5_126"
      elif (
        (last_candle["RSI_3"] > 82.0)
        and (last_candle["RSI_3_1h"] < 10.0)
        and (last_candle["RSI_3_4h"] < 30.0)
        and (last_candle["RSI_3_1d"] < 40.0)
      ):
        return True, f"exit_{mode_name}_d_5_127"
      elif (last_candle["RSI_3"] > 86.0) and (last_candle["RSI_3_4h"] < 30.0) and (last_candle["AROONU_14_4h"] > 85.0):
        return True, f"exit_{mode_name}_d_5_128"
      elif (
        (last_candle["RSI_3"] > 78.0)
        and (last_candle["RSI_3_4h"] < 25.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 80.0))
      ):
        return True, f"exit_{mode_name}_d_5_129"
      elif (
        (last_candle["RSI_3"] > 66.0)
        and (last_candle["RSI_14_1h"] > 65.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 80.0)
        and (last_candle["CCI_20_change_pct_1h"] < -0.0)
      ):
        return True, f"exit_{mode_name}_d_5_130"
      elif (
        (last_candle["RSI_14"] < 46.0)
        and (last_candle["RSI_3_1h"] < 20.0)
        and (last_candle["RSI_3_4h"] < 30.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_5_131"
      elif (
        (last_candle["RSI_3"] > 72.0)
        and (last_candle["RSI_3_1h"] < 35.0)
        and (last_candle["RSI_3_4h"] < 35.0)
        and (last_candle["AROONU_14_1h"] > 50.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 40.0)
      ):
        return True, f"exit_{mode_name}_d_5_132"
      elif (
        (last_candle["RSI_3"] > 72.0)
        and (last_candle["AROONU_14_15m"] > 75.0)
        and (last_candle["AROONU_14_1h"] > 75.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 25.0))
      ):
        return True, f"exit_{mode_name}_d_5_133"
    elif 0.07 > current_profit >= 0.06:
      if (
        (last_candle["WILLR_14"] > -1.0)
        and (last_candle["RSI_14"] > 78.0)
        and (
          isinstance(last_candle["EMA_200_1h"], np.float64) and (last_candle["EMA_12_1h"] < last_candle["EMA_200_1h"])
        )
        and (
          isinstance(last_candle["EMA_200_4h"], np.float64) and (last_candle["EMA_12_4h"] < last_candle["EMA_200_4h"])
        )
        and (last_candle["KST_10_15_20_30_10_10_10_15_1h"] < last_candle["KSTs_9_1h"])
        and (last_candle["KST_10_15_20_30_10_10_10_15_4h"] < last_candle["KSTs_9_4h"])
      ):
        return True, f"exit_{mode_name}_d_6_1"
      elif (
        (last_candle["WILLR_14"] > -1.0)
        and (last_candle["RSI_14"] > 62.0)
        and (last_candle["CMF_20_1h"] < -0.0)
        and (
          isinstance(last_candle["EMA_200_1h"], np.float64) and (last_candle["EMA_12_1h"] < last_candle["EMA_200_1h"])
        )
        and (
          isinstance(last_candle["EMA_200_4h"], np.float64) and (last_candle["EMA_12_4h"] < last_candle["EMA_200_4h"])
        )
      ):
        return True, f"exit_{mode_name}_d_6_2"
      elif (
        (last_candle["WILLR_14"] > -15.0)
        and (last_candle["STOCHRSIk_14_14_3_3"] > 98.0)
        and (last_candle["CMF_20_1h"] < -0.0)
        and (last_candle["CMF_20_4h"] < -0.0)
        and (
          (last_candle["STOCHRSIk_14_14_3_3_4h"] > 20.0) and (last_candle["STOCHRSIk_14_14_3_3_change_pct_4h"] < -10.0)
        )
      ):
        return True, f"exit_{mode_name}_d_6_3"
      elif (
        (last_candle["WILLR_14"] > -25.0)
        and (last_candle["RSI_14"] > 68.0)
        and (last_candle["STOCHRSIk_14_14_3_3"] > 95.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 70.0)
        and (
          isinstance(last_candle["EMA_200_1h"], np.float64) and (last_candle["EMA_12_1h"] < last_candle["EMA_200_1h"])
        )
        and (
          isinstance(last_candle["EMA_200_4h"], np.float64) and (last_candle["EMA_12_4h"] < last_candle["EMA_200_4h"])
        )
      ):
        return True, f"exit_{mode_name}_d_6_4"
      elif (
        (last_candle["WILLR_14"] > -8.0)
        and (last_candle["RSI_14"] > 66.0)
        and (last_candle["ROC_9_1h"] < -5.0)
        and (last_candle["ROC_9_4h"] < -5.0)
      ):
        return True, f"exit_{mode_name}_d_6_5"
      elif (
        (last_candle["RSI_3"] > 70.0)
        and (last_candle["STOCHRSIk_14_14_3_3"] > 70.0)
        and (last_candle["RSI_14"] < 40.0)
        and (last_candle["ROC_9_1h"] < -10.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 50.0))
      ):
        return True, f"exit_{mode_name}_d_6_6"
      elif (
        (last_candle["RSI_14"] < 50.0)
        and (last_candle["STOCHRSIk_14_14_3_3"] > 70.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -40.0))
      ):
        return True, f"exit_{mode_name}_d_6_7"
      elif (
        (last_candle["WILLR_14"] > -8.0)
        and (last_candle["STOCHRSIk_14_14_3_3"] > 95.0)
        and (last_candle["CMF_20_1h"] < -0.1)
        and (last_candle["CMF_20_4h"] < -0.1)
        and (last_candle["change_pct_1d"] < -5.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 15.0))
      ):
        return True, f"exit_{mode_name}_d_6_8"
      elif (
        (last_candle["WILLR_14"] > -7.0)
        and (last_candle["RSI_3"] > 95.0)
        and (last_candle["change_pct_4h"] < -5.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 30.0))
      ):
        return True, f"exit_{mode_name}_d_6_9"
      elif (
        (last_candle["WILLR_14"] > -15.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["ROC_9_1h"] < -10.0)
        and (last_candle["ROC_9_4h"] < -10.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 10.0))
      ):
        return True, f"exit_{mode_name}_d_6_10"
      elif (
        (last_candle["RSI_3"] > 80.0)
        and (last_candle["RSI_14"] < 45.0)
        and (last_candle["ROC_9_15m"] < -10.0)
        and (last_candle["ROC_9_1h"] < -10.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -20.0))
      ):
        return True, f"exit_{mode_name}_d_6_11"
      elif (
        (last_candle["RSI_3"] > 75.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_4h"] < 10.0)
        and (last_candle["ROC_9_1h"] < -20.0)
        and (last_candle["ROC_9_4h"] < -20.0)
      ):
        return True, f"exit_{mode_name}_d_6_12"
      elif (last_candle["RSI_3"] > 85.0) and (last_candle["RSI_3_4h"] < 5.0) and (last_candle["ROC_9_4h"] < -25.0):
        return True, f"exit_{mode_name}_d_6_13"
      elif (
        (last_candle["RSI_3"] > 90.0)
        and (last_candle["WILLR_14"] > -10.0)
        and (last_candle["RSI_3_4h"] < 5.0)
        and (last_candle["AROONU_14_4h"] > 25.0)
      ):
        return True, f"exit_{mode_name}_d_6_14"
      elif (last_candle["RSI_3"] > 88.0) and (last_candle["RSI_14"] > 60.0) and (last_candle["ROC_9_4h"] < -30.0):
        return True, f"exit_{mode_name}_d_6_15"
      elif (
        (last_candle["RSI_3"] > 75.0)
        and (last_candle["AROONU_14_4h"] > 25.0)
        and (last_candle["ROC_9_4h"] < -25.0)
        and (last_candle["AROONU_14_1d"] > 50.0)
        and (last_candle["change_pct_1d"] < -15.0)
      ):
        return True, f"exit_{mode_name}_d_6_16"
      elif (
        (last_candle["RSI_3"] > 85.0)
        and (last_candle["WILLR_14"] > -30.0)
        and (last_candle["RSI_3_1h"] < 10.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 90.0)
        and (last_candle["ROC_9_4h"] > 30.0)
      ):
        return True, f"exit_{mode_name}_d_6_17"
      elif (
        (last_candle["RSI_3"] > 80.0)
        and (last_candle["RSI_14"] > 65.0)
        and (last_candle["RSI_3_4h"] < 20.0)
        and (last_candle["ROC_2_1d"] < -50.0)
      ):
        return True, f"exit_{mode_name}_d_6_18"
      elif (
        (last_candle["RSI_3"] > 86.0)
        and (last_candle["RSI_14"] > 66.0)
        and (last_candle["RSI_3_4h"] < 10.0)
        and (
          isinstance(last_candle["STOCHRSIk_14_14_3_3_1d"], np.float64)
          and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 70.0)
        )
      ):
        return True, f"exit_{mode_name}_d_6_19"
      elif (
        (last_candle["RSI_3"] > 44.0)
        and (last_candle["RSI_14"] < 46.0)
        and (last_candle["RSI_3_1h"] < 10.0)
        and (last_candle["AROONU_14_1h"] > 25.0)
      ):
        return True, f"exit_{mode_name}_d_6_20"
      elif (
        (last_candle["RSI_3"] > 60.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_1h"] < 20.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 90.0)
      ):
        return True, f"exit_{mode_name}_d_6_21"
      elif (
        (last_candle["RSI_3"] > 92.0)
        and (last_candle["WILLR_14"] > -8.0)
        and (last_candle["change_pct_4h"] < -5.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -30.0))
      ):
        return True, f"exit_{mode_name}_d_6_22"
      elif (
        (last_candle["RSI_3"] > 80.0)
        and (last_candle["WILLR_14"] > -25.0)
        and (last_candle["RSI_3_1h"] < 15.0)
        and (last_candle["RSI_3_1d"] < 5.0)
      ):
        return True, f"exit_{mode_name}_d_6_23"
      elif (
        (last_candle["RSI_3"] > 86.0)
        and (last_candle["RSI_14"] > 66.0)
        and (last_candle["WILLR_14"] > -30.0)
        and (last_candle["RSI_3_4h"] < 30.0)
        and (last_candle["AROONU_14_4h"] > 75.0)
      ):
        return True, f"exit_{mode_name}_d_6_24"
      elif (
        (last_candle["RSI_3"] > 75.0)
        and (last_candle["WILLR_14"] > -10.0)
        and (last_candle["RSI_3_4h"] < 10.0)
        and (last_candle["ROC_9_4h"] < -15.0)
        and (
          isinstance(last_candle["STOCHRSIk_14_14_3_3_1d"], np.float64)
          and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 50.0)
        )
      ):
        return True, f"exit_{mode_name}_d_6_25"
      elif (
        (last_candle["RSI_3"] > 70.0)
        and (last_candle["WILLR_14"] > -10.0)
        and (last_candle["RSI_3_4h"] < 15.0)
        and (last_candle["ROC_9_4h"] < -20.0)
      ):
        return True, f"exit_{mode_name}_d_6_26"
      elif (
        (last_candle["RSI_3"] > 70.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_1h"] < 20.0)
        and (last_candle["RSI_3_4h"] < 20.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 20.0)
      ):
        return True, f"exit_{mode_name}_d_6_27"
      elif (
        (last_candle["RSI_3"] > 65.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_15m"] < 10.0)
        and (last_candle["ROC_9_4h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_6_28"
      elif (
        (last_candle["RSI_3"] > 80.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_1h"] < 20.0)
        and (last_candle["RSI_3_4h"] < 20.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 30.0)
      ):
        return True, f"exit_{mode_name}_d_6_29"
      elif (
        (last_candle["RSI_3"] > 75.0)
        and (last_candle["RSI_3_1h"] < 25.0)
        and (last_candle["RSI_3_4h"] < 10.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 70.0)
      ):
        return True, f"exit_{mode_name}_d_6_30"
      elif (
        (last_candle["RSI_3"] > 65.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_1h"] < 15.0)
        and (last_candle["RSI_3_4h"] < 15.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 25.0)
      ):
        return True, f"exit_{mode_name}_d_6_31"
      elif (
        (last_candle["RSI_3"] > 75.0)
        and (last_candle["RSI_3_1h"] < 15.0)
        and (last_candle["ROC_2_4h"] < -30.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 30.0)
      ):
        return True, f"exit_{mode_name}_d_6_32"
      elif (
        (last_candle["RSI_3"] > 75.0)
        and (last_candle["WILLR_14"] > -8.0)
        and (last_candle["ROC_2_1h"] < -10.0)
        and (last_candle["ROC_9_1h"] > 30.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_6_33"
      elif (
        (last_candle["RSI_3"] > 65.0)
        and (last_candle["RSI_3_15m"] < 30.0)
        and (last_candle["RSI_14_1h"] > 80.0)
        and (last_candle["ROC_9_1h"] > 40.0)
      ):
        return True, f"exit_{mode_name}_d_6_34"
      elif (
        (last_candle["RSI_3"] > 82.0)
        and (last_candle["WILLR_14"] > -9.0)
        and (last_candle["RSI_3_1d"] < 25.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 75.0)
      ):
        return True, f"exit_{mode_name}_d_6_35"
      elif (
        (last_candle["RSI_3"] > 70.0)
        and (last_candle["WILLR_14"] > -30.0)
        and (last_candle["ROC_9_4h"] < -25.0)
        and (last_candle["RSI_3_1d"] < 25.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_6_36"
      elif (
        (last_candle["RSI_3"] > 76.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_1h"] < 20.0)
        and (last_candle["RSI_3_1d"] < 25.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_6_37"
      elif (
        (last_candle["RSI_3"] > 70.0)
        and (last_candle["WILLR_14"] > -30.0)
        and (last_candle["RSI_3_4h"] < 10.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 20.0)
      ):
        return True, f"exit_{mode_name}_d_6_38"
      elif (
        (last_candle["RSI_3"] > 92.0)
        and (last_candle["WILLR_14"] > -8.0)
        and (last_candle["CMF_20_4h"] < -0.0)
        and (last_candle["RSI_3_4h"] < 10.0)
      ):
        return True, f"exit_{mode_name}_d_6_39"
      elif (
        (last_candle["RSI_3"] > 70.0)
        and (last_candle["WILLR_14"] > -30.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 30.0)
        and (
          isinstance(last_candle["STOCHRSIk_14_14_3_3_1d"], np.float64)
          and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 90.0)
        )
      ):
        return True, f"exit_{mode_name}_d_6_40"
      elif (
        (last_candle["RSI_3"] > 80.0)
        and (last_candle["WILLR_14"] > -25.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 25.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 50.0))
      ):
        return True, f"exit_{mode_name}_d_6_41"
      elif (
        (last_candle["RSI_3"] > 75.0)
        and (last_candle["WILLR_14"] > -40.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 30.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 40.0))
        and (
          isinstance(last_candle["STOCHRSIk_14_14_3_3_1d"], np.float64)
          and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 70.0)
        )
      ):
        return True, f"exit_{mode_name}_d_6_42"
      elif (
        (last_candle["RSI_3"] > 80.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_1h"] < 15.0)
        and (last_candle["RSI_3_4h"] < 40.0)
        and (
          isinstance(last_candle["STOCHRSIk_14_14_3_3_1d"], np.float64)
          and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 90.0)
        )
      ):
        return True, f"exit_{mode_name}_d_6_43"
      elif (
        (last_candle["RSI_3"] > 55.0)
        and (last_candle["WILLR_14"] > -20.0)
        and (last_candle["RSI_3_4h"] < 30.0)
        and (last_candle["RSI_3_1d"] < 25.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -30.0))
      ):
        return True, f"exit_{mode_name}_d_6_44"
      elif (last_candle["RSI_3"] > 88.0) and (last_candle["WILLR_14"] > -12.0) and (last_candle["RSI_3_1h"] < 10.0):
        return True, f"exit_{mode_name}_d_6_45"
      elif (
        (last_candle["RSI_3"] > 75.0)
        and (last_candle["RSI_3_1h"] < 15.0)
        and (last_candle["RSI_3_4h"] < 10.0)
        and (last_candle["ROC_2_1d"] < -20.0)
      ):
        return True, f"exit_{mode_name}_d_6_46"
      elif (
        (last_candle["RSI_3"] > 80.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 80.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 40.0)
        and (last_candle["change_pct_1d"] < -5.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -5.0))
      ):
        return True, f"exit_{mode_name}_d_6_47"
      elif (
        (last_candle["RSI_3"] > 50.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (last_candle["RSI_3_4h"] < 20.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_6_48"
      elif (
        (last_candle["RSI_3"] > 75.0)
        and (last_candle["WILLR_14"] > -10.0)
        and (last_candle["RSI_3_4h"] < 20.0)
        and (last_candle["change_pct_1d"] < -5.0)
        and (
          isinstance(last_candle["STOCHRSIk_14_14_3_3_1d"], np.float64)
          and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 50.0)
        )
      ):
        return True, f"exit_{mode_name}_d_6_49"
      elif (
        (last_candle["RSI_3"] > 80.0)
        and (last_candle["WILLR_14"] > -10.0)
        and (last_candle["RSI_3_1d"] < 10.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 90.0)
      ):
        return True, f"exit_{mode_name}_d_6_50"
      elif (
        (last_candle["RSI_3"] > 60.0)
        and (last_candle["RSI_14"] < 52.0)
        and (last_candle["RSI_3_4h"] < 20.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_6_51"
      elif (
        (last_candle["RSI_3"] > 74.0)
        and (last_candle["RSI_14"] > 54.0)
        and (last_candle["WILLR_14"] > -10.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 70.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -15.0))
      ):
        return True, f"exit_{mode_name}_d_6_52"
      elif (
        (last_candle["RSI_3"] > 70.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["WILLR_14"] > -25.0)
        and (last_candle["RSI_3_1h"] < 20.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
        and (
          isinstance(last_candle["STOCHRSIk_14_14_3_3_1d"], np.float64)
          and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 50.0)
        )
      ):
        return True, f"exit_{mode_name}_d_6_53"
      elif (
        (last_candle["RSI_3"] > 72.0)
        and (last_candle["RSI_14"] < 52.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
        and (last_candle["ROC_9_4h"] < -10.0)
        and (last_candle["change_pct_1d"] < -10.0)
      ):
        return True, f"exit_{mode_name}_d_6_54"
      elif (
        (last_candle["RSI_3"] > 88.0)
        and (last_candle["WILLR_14"] > -20.0)
        and (last_candle["ROC_9_4h"] < -5.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 10.0))
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_6_55"
      elif (
        (last_candle["RSI_3"] > 65.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (last_candle["RSI_3_4h"] < 25.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -30.0))
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 10.0)
      ):
        return True, f"exit_{mode_name}_d_6_56"
      elif (
        (last_candle["RSI_3"] > 50.0)
        and (last_candle["RSI_14"] < 42.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -30.0))
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 70.0)
      ):
        return True, f"exit_{mode_name}_d_6_57"
      elif (
        (last_candle["RSI_3"] > 75.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (last_candle["RSI_3_4h"] < 30.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -15.0))
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_6_58"
      elif (
        (last_candle["RSI_3"] > 85.0)
        and (last_candle["WILLR_14"] > -18.0)
        and (last_candle["RSI_3_4h"] < 25.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -15.0))
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 40.0)
      ):
        return True, f"exit_{mode_name}_d_6_59"
      elif (
        (last_candle["RSI_3"] > 65.0)
        and (last_candle["RSI_14"] < 46.0)
        and (last_candle["RSI_14_4h"] > 65.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_6_60"
      elif (
        (last_candle["RSI_3"] > 90.0)
        and (last_candle["WILLR_14"] > -25.0)
        and (last_candle["RSI_3_4h"] < 10.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 30.0)
      ):
        return True, f"exit_{mode_name}_d_6_61"
      elif (
        (last_candle["RSI_3"] > 80.0)
        and (last_candle["WILLR_14"] > -8.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (last_candle["RSI_3_4h"] < 20.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 20.0))
        and (last_candle["change_pct_1d"] < -5.0)
      ):
        return True, f"exit_{mode_name}_d_6_62"
      elif (
        (last_candle["RSI_3"] > 62.0)
        and (last_candle["RSI_3_1d"] < 25.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 80.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 30.0)
      ):
        return True, f"exit_{mode_name}_d_6_63"
      elif (
        (last_candle["RSI_3"] > 82.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (last_candle["RSI_3_4h"] < 30.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 30.0))
      ):
        return True, f"exit_{mode_name}_d_6_64"
      elif (
        (last_candle["RSI_3"] > 62.0)
        and (last_candle["RSI_14"] < 48.0)
        and (last_candle["RSI_3_1h"] < 20.0)
        and (last_candle["RSI_3_4h"] < 15.0)
      ):
        return True, f"exit_{mode_name}_d_6_65"
      elif (
        (last_candle["RSI_3"] > 76.0)
        and (last_candle["RSI_14"] < 54.0)
        and (last_candle["RSI_3_1h"] < 20.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_6_66"
      elif (
        (last_candle["RSI_3"] > 50.0)
        and (last_candle["RSI_14"] < 48.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 80.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -25.0))
      ):
        return True, f"exit_{mode_name}_d_6_67"
      elif (
        (last_candle["RSI_3"] > 78.0)
        and (last_candle["RSI_14"] < 54.0)
        and (last_candle["RSI_3_1h"] < 25.0)
        and (last_candle["ROC_2_4h"] < -30.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 25.0)
      ):
        return True, f"exit_{mode_name}_d_6_68"
      elif (
        (last_candle["RSI_3"] > 93.0)
        and (last_candle["ROC_9_4h"] > 20.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
        and (last_candle["change_pct_4h"] < -5.0)
      ):
        return True, f"exit_{mode_name}_d_6_69"
      elif (
        (last_candle["RSI_3"] > 60.0)
        and (last_candle["RSI_14"] < 46.0)
        and (last_candle["RSI_3_1h"] < 25.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 20.0)
      ):
        return True, f"exit_{mode_name}_d_6_70"
      elif (
        (last_candle["RSI_3"] > 58.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_4h"] < 25.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 20.0)
      ):
        return True, f"exit_{mode_name}_d_6_71"
      elif (
        (last_candle["RSI_3"] > 72.0)
        and (last_candle["RSI_14"] < 48.0)
        and (last_candle["RSI_3_1h"] < 10.0)
        and (last_candle["AROONU_14_4h"] > 25.0)
      ):
        return True, f"exit_{mode_name}_d_6_72"
      elif (
        (last_candle["RSI_3"] > 72.0)
        and (last_candle["RSI_3_1h"] < 25.0)
        and (last_candle["RSI_3_4h"] < 15.0)
        and (last_candle["ROC_9_4h"] < -20.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -25.0))
      ):
        return True, f"exit_{mode_name}_d_6_73"
      elif (
        (last_candle["RSI_3"] > 95.0)
        and (last_candle["WILLR_14"] > -10.0)
        and (last_candle["RSI_3_4h"] < 25.0)
        and (last_candle["RSI_3_1d"] < 25.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_6_74"
      elif (
        (last_candle["RSI_3"] > 90.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (last_candle["RSI_3_4h"] < 20.0)
        and (
          isinstance(last_candle["STOCHRSIk_14_14_3_3_1d"], np.float64)
          and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 50.0)
        )
      ):
        return True, f"exit_{mode_name}_d_6_75"
      elif (
        (last_candle["RSI_3"] > 62.0)
        and (last_candle["RSI_14"] < 56.0)
        and (last_candle["ROC_9_1h"] > 80.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 80.0)
      ):
        return True, f"exit_{mode_name}_d_6_76"
      elif (
        (last_candle["RSI_3"] > 70.0)
        and (last_candle["RSI_14"] < 52.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 50.0))
      ):
        return True, f"exit_{mode_name}_d_6_77"
      elif (
        (last_candle["RSI_3"] > 80.0)
        and (last_candle["WILLR_14"] > -22.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (last_candle["RSI_3_4h"] < 20.0)
        and (last_candle["RSI_3_1d"] < 20.0)
      ):
        return True, f"exit_{mode_name}_d_6_78"
      elif (
        (last_candle["RSI_3"] > 86.0)
        and (last_candle["WILLR_14"] > -8.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (last_candle["RSI_3_4h"] < 10.0)
      ):
        return True, f"exit_{mode_name}_d_6_79"
      elif (
        (last_candle["RSI_3"] > 66.0)
        and (last_candle["RSI_14"] < 52.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 50.0))
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 25.0)
      ):
        return True, f"exit_{mode_name}_d_6_80"
      elif (
        (last_candle["RSI_3"] > 78.0)
        and (last_candle["WILLR_14"] > -16.0)
        and (last_candle["RSI_3_1h"] < 25.0)
        and (last_candle["RSI_3_4h"] < 25.0)
        and (isinstance(last_candle["RSI_14_1d"], np.float64) and (last_candle["RSI_14_1d"] > 50.0))
      ):
        return True, f"exit_{mode_name}_d_6_81"
      elif (
        (last_candle["RSI_3"] > 76.0)
        and (last_candle["WILLR_14"] > -16.0)
        and (last_candle["RSI_3_4h"] < 30.0)
        and (last_candle["RSI_3_1d"] < 15.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 40.0)
      ):
        return True, f"exit_{mode_name}_d_6_82"
      elif (
        (last_candle["RSI_3"] > 66.0)
        and (last_candle["RSI_14"] < 52.0)
        and (last_candle["RSI_3_1h"] < 40.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 40.0)
      ):
        return True, f"exit_{mode_name}_d_6_83"
      elif (
        (last_candle["RSI_3"] > 84.0)
        and (last_candle["WILLR_14"] > -8.0)
        and (last_candle["RSI_3_4h"] < 30.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 20.0)
      ):
        return True, f"exit_{mode_name}_d_6_84"
      elif (
        (last_candle["RSI_3"] > 82.0)
        and (last_candle["WILLR_14"] > -14.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (last_candle["RSI_3_4h"] < 40.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_6_85"
      elif (
        (last_candle["RSI_3"] > 88.0)
        and (last_candle["RSI_14_4h"] > 80.0)
        and (last_candle["ROC_2_1h"] < -5.0)
        and (last_candle["ROC_9_1h"] > 5.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_6_86"
      elif (
        (last_candle["RSI_3"] > 60.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_1h"] < 45.0)
        and (last_candle["RSI_3_4h"] < 50.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_6_87"
      elif (
        (last_candle["RSI_3"] > 82.0)
        and (last_candle["WILLR_14"] > -26.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 40.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
        and (last_candle["change_pct_1h"] < -2.0)
      ):
        return True, f"exit_{mode_name}_d_6_88"
      elif (
        (last_candle["RSI_3"] > 72.0)
        and (last_candle["RSI_14"] < 46.0)
        and (last_candle["ROC_9_1h"] < -5.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 25.0))
      ):
        return True, f"exit_{mode_name}_d_6_89"
      elif (
        (last_candle["RSI_3"] > 86.0)
        and (last_candle["WILLR_14"] > -25.0)
        and (last_candle["RSI_3_1h"] < 50.0)
        and (last_candle["RSI_3_4h"] < 30.0)
        and (last_candle["AROONU_14_4h"] > 50.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 40.0))
      ):
        return True, f"exit_{mode_name}_d_6_90"
      elif (
        (last_candle["RSI_3"] > 66.0)
        and (last_candle["RSI_14"] < 52.0)
        and (last_candle["RSI_3_1h"] < 25.0)
        and (last_candle["RSI_3_4h"] < 25.0)
        and (last_candle["AROONU_14_4h"] > 50.0)
        and (
          isinstance(last_candle["STOCHRSIk_14_14_3_3_1d"], np.float64)
          and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 50.0)
        )
      ):
        return True, f"exit_{mode_name}_d_6_91"
      elif (
        (last_candle["RSI_3"] > 74.0)
        and (last_candle["RSI_14"] < 54.0)
        and (last_candle["RSI_3_1h"] < 40.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 25.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -25.0))
      ):
        return True, f"exit_{mode_name}_d_6_92"
      elif (
        (last_candle["RSI_3"] > 66.0)
        and (last_candle["RSI_14"] < 56.0)
        and (last_candle["RSI_3_15m"] < 50.0)
        and (last_candle["AROONU_14_1h"] > 75.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 70.0)
        and (last_candle["AROONU_14_4h"] > 50.0)
        and (
          isinstance(last_candle["STOCHRSIk_14_14_3_3_1d"], np.float64)
          and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 90.0)
        )
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 30.0))
      ):
        return True, f"exit_{mode_name}_d_6_93"
      elif (
        (last_candle["RSI_3"] > 74.0)
        and (last_candle["RSI_14"] < 56.0)
        and (last_candle["RSI_3_1h"] < 25.0)
        and (last_candle["RSI_3_4h"] < 45.0)
        and (last_candle["AROONU_14_1h"] > 75.0)
        and (
          isinstance(last_candle["STOCHRSIk_14_14_3_3_1d"], np.float64)
          and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 90.0)
        )
      ):
        return True, f"exit_{mode_name}_d_6_94"
      elif (
        (last_candle["RSI_3"] > 78.0)
        and (last_candle["WILLR_14"] > -18.0)
        and (last_candle["RSI_3_1h"] < 45.0)
        and (last_candle["RSI_3_4h"] < 40.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 10.0)
        and (isinstance(last_candle["AROONU_14_1d"], np.float64) and (last_candle["AROONU_14_1d"] > 75.0))
      ):
        return True, f"exit_{mode_name}_d_6_95"
      elif (
        (last_candle["RSI_3"] > 56.0)
        and (last_candle["RSI_14"] < 52.0)
        and (last_candle["RSI_3_1h"] < 45.0)
        and (last_candle["RSI_3_1d"] < 45.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_6_96"
      elif (
        (last_candle["RSI_3"] > 78.0)
        and (last_candle["RSI_14"] < 52.0)
        and (last_candle["RSI_3_1h"] < 35.0)
        and (last_candle["AROONU_14_4h"] > 50.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 30.0)
      ):
        return True, f"exit_{mode_name}_d_6_97"
      elif (
        (last_candle["RSI_3"] > 84.0)
        and (last_candle["RSI_3_15m"] > 66.0)
        and (last_candle["RSI_3_1h"] < 60.0)
        and (last_candle["RSI_3_4h"] < 60.0)
        and (last_candle["RSI_3_1d"] > 80.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_6_98"
      elif (
        (last_candle["RSI_3"] > 54.0)
        and (last_candle["RSI_14"] < 58.0)
        and (last_candle["RSI_3_1h"] < 65.0)
        and (last_candle["RSI_3_4h"] < 60.0)
        and (last_candle["AROONU_14_4h"] > 50.0)
        and (last_candle["STOCHk_14_3_3_4h"] > 40.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 80.0))
      ):
        return True, f"exit_{mode_name}_d_6_99"
      elif (
        (last_candle["RSI_3"] > 92.0)
        and (last_candle["RSI_14"] > 70.0)
        and (last_candle["RSI_3_15m"] > 70.0)
        and (last_candle["RSI_3_4h"] < 80.0)
      ):
        return True, f"exit_{mode_name}_d_6_100"
      elif (
        (last_candle["RSI_3"] > 78.0)
        and (last_candle["WILLR_14"] > -22.0)
        and (last_candle["RSI_3_1h"] < 50.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 40.0)
        and (isinstance(last_candle["ROC_9_4h"], np.float64) and (last_candle["ROC_9_4h"] > 40.0))
      ):
        return True, f"exit_{mode_name}_d_6_101"
      elif (
        (last_candle["RSI_3"] > 62.0)
        and (last_candle["RSI_14"] < 54.0)
        and (last_candle["RSI_3_1h"] < 60.0)
        and (last_candle["RSI_3_4h"] < 40.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 30.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 40.0))
      ):
        return True, f"exit_{mode_name}_d_6_102"
      elif (
        (last_candle["RSI_3"] > 72.0)
        and (last_candle["RSI_14"] < 62.0)
        and (last_candle["RSI_3_1h"] < 60.0)
        and (last_candle["RSI_14_4h"] > 70.0)
        and (isinstance(last_candle["ROC_9_4h"], np.float64) and (last_candle["ROC_9_4h"] > 80.0))
      ):
        return True, f"exit_{mode_name}_d_6_103"
      elif (
        (last_candle["RSI_3"] > 58.0)
        and (last_candle["RSI_14"] < 54.0)
        and (last_candle["RSI_3_1h"] < 60.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 40.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 90.0)
        and (last_candle["ROC_9_4h"] > 40.0)
      ):
        return True, f"exit_{mode_name}_d_6_104"
      elif (
        (last_candle["RSI_3"] > 72.0)
        and (last_candle["RSI_14"] < 54.0)
        and (last_candle["RSI_3_15m"] < 55.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 90.0)
        and (last_candle["ROC_9_4h"] > 25.0)
      ):
        return True, f"exit_{mode_name}_d_6_105"
      elif (
        (last_candle["RSI_3"] > 66.0)
        and (last_candle["RSI_14"] < 54.0)
        and (last_candle["RSI_3_1h"] < 50.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
        and (last_candle["RSI_14_4h"] > 70.0)
        and (last_candle["ROC_9_4h"] > 40.0)
      ):
        return True, f"exit_{mode_name}_d_6_106"
      elif (
        (last_candle["RSI_3"] > 68.0)
        and (last_candle["RSI_14"] < 54.0)
        and (last_candle["RSI_3_1h"] < 50.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 70.0)
        and (last_candle["RSI_14_4h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_6_107"
      elif (
        (last_candle["RSI_3"] > 50.0)
        and (last_candle["RSI_14"] < 54.0)
        and (last_candle["RSI_3_1h"] < 60.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 80.0)
      ):
        return True, f"exit_{mode_name}_d_6_108"
      elif (
        (last_candle["RSI_3"] > 70.0)
        and (last_candle["WILLR_14"] > -14.0)
        and (last_candle["RSI_3_1h"] < 50.0)
        and (last_candle["RSI_3_4h"] < 20.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 50.0))
      ):
        return True, f"exit_{mode_name}_d_6_109"
      elif (
        (last_candle["RSI_3"] > 66.0)
        and (last_candle["RSI_3_4h"] < 65.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
        and (last_candle["ROC_9_4h"] > 25.0)
      ):
        return True, f"exit_{mode_name}_d_6_110"
      elif (
        (last_candle["RSI_3"] > 44.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_1h"] < 50.0)
        and (last_candle["RSI_14_4h"] > 70.0)
        and (last_candle["AROONU_14_1h"] > 75.0)
        and (last_candle["AROONU_14_4h"] > 75.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 20.0))
      ):
        return True, f"exit_{mode_name}_d_6_111"
      elif (
        (last_candle["RSI_3"] > 74.0)
        and (last_candle["WILLR_14"] > -40.0)
        and (last_candle["RSI_14"] < 58.0)
        and (last_candle["RSI_3_1h"] < 35.0)
        and (last_candle["RSI_3_4h"] < 35.0)
        and (last_candle["RSI_3_1d"] < 60.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 30.0))
      ):
        return True, f"exit_{mode_name}_d_6_112"
      elif (
        (last_candle["RSI_3"] > 78.0)
        and (last_candle["WILLR_14"] > -8.0)
        and (last_candle["RSI_3_1d"] < 30.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
        and (isinstance(last_candle["ROC_9_4h"], np.float64) and (last_candle["ROC_9_4h"] > 10.0))
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -10.0))
      ):
        return True, f"exit_{mode_name}_d_6_113"
      elif (
        (last_candle["RSI_3"] > 78.0)
        and (last_candle["RSI_14"] < 56.0)
        and (last_candle["RSI_3_1h"] < 20.0)
        and (last_candle["RSI_3_4h"] < 30.0)
        and (last_candle["RSI_3_1d"] < 30.0)
      ):
        return True, f"exit_{mode_name}_d_6_114"
      elif (
        (last_candle["RSI_3"] > 72.0)
        and (last_candle["RSI_14"] < 54.0)
        and (last_candle["RSI_3_15m"] < 30.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_6_115"
      elif (
        (last_candle["RSI_3"] > 84.0)
        and (last_candle["RSI_3_1h"] < 15.0)
        and (last_candle["RSI_3_4h"] < 40.0)
        and (last_candle["AROONU_14_4h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_6_116"
      elif (
        (last_candle["RSI_3"] > 80.0)
        and (last_candle["RSI_3_1h"] < 50.0)
        and (last_candle["AROONU_14_1h"] > 80.0)
        and (last_candle["AROONU_14_4h"] > 80.0)
      ):
        return True, f"exit_{mode_name}_d_6_117"
      elif (
        (last_candle["RSI_3"] > 84.0)
        and (last_candle["RSI_3_1h"] < 20.0)
        and (last_candle["RSI_3_4h"] < 60.0)
        and (last_candle["AROONU_14_4h"] > 40.0)
      ):
        return True, f"exit_{mode_name}_d_6_118"
      elif (
        (last_candle["RSI_3"] > 80.0)
        and (last_candle["WILLR_14"] > -20.0)
        and (last_candle["RSI_3_1h"] < 60.0)
        and (last_candle["RSI_3_4h"] < 60.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 40.0)
      ):
        return True, f"exit_{mode_name}_d_6_119"
      elif (
        (last_candle["RSI_3"] > 48.0)
        and (last_candle["RSI_14"] < 54.0)
        and (last_candle["RSI_3_1h"] < 40.0)
        and (last_candle["AROONU_14_4h"] > 75.0)
      ):
        return True, f"exit_{mode_name}_d_6_120"
      elif (
        (last_candle["RSI_3"] > 54.0)
        and (last_candle["RSI_14"] < 52.0)
        and (last_candle["RSI_3_1h"] < 50.0)
        and (last_candle["RSI_14_4h"] > 85.0)
      ):
        return True, f"exit_{mode_name}_d_6_121"
      elif (
        (last_candle["RSI_3"] > 52.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_4h"] < 30.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_6_122"
      elif (
        (last_candle["RSI_3"] > 82.0)
        and (last_candle["WILLR_14"] > -10.0)
        and (last_candle["RSI_3_1h"] < 10.0)
        and (last_candle["RSI_3_1d"] < 30.0)
      ):
        return True, f"exit_{mode_name}_d_6_123"
      elif (
        (last_candle["RSI_3"] > 82.0)
        and (last_candle["RSI_3_1h"] < 15.0)
        and (
          isinstance(last_candle["STOCHRSIk_14_14_3_3_1d"], np.float64)
          and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 80.0)
        )
      ):
        return True, f"exit_{mode_name}_d_6_124"
      elif (
        (last_candle["RSI_3"] > 70.0)
        and (last_candle["WILLR_14"] > -10.0)
        and (last_candle["RSI_3_1h"] < 10.0)
        and (last_candle["RSI_3_4h"] < 40.0)
        and (last_candle["RSI_3_1d"] < 40.0)
        and (last_candle["close"] < (last_candle["high_max_30_1d"] * 0.50))
      ):
        return True, f"exit_{mode_name}_d_6_125"
      elif (
        (last_candle["RSI_3"] > 84.0)
        and (last_candle["RSI_3_1h"] < 15.0)
        and (last_candle["RSI_3_4h"] < 40.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_6_126"
      elif (
        (last_candle["RSI_3"] > 84.0)
        and (last_candle["RSI_3_1h"] < 10.0)
        and (last_candle["RSI_3_4h"] < 30.0)
        and (last_candle["RSI_3_1d"] < 40.0)
      ):
        return True, f"exit_{mode_name}_d_6_127"
      elif (last_candle["RSI_3"] > 88.0) and (last_candle["RSI_3_4h"] < 30.0) and (last_candle["AROONU_14_4h"] > 85.0):
        return True, f"exit_{mode_name}_d_6_128"
      elif (
        (last_candle["RSI_3"] > 80.0)
        and (last_candle["RSI_3_4h"] < 25.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 80.0))
      ):
        return True, f"exit_{mode_name}_d_6_129"
      elif (
        (last_candle["RSI_3"] > 68.0)
        and (last_candle["RSI_14_1h"] > 65.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 80.0)
        and (last_candle["CCI_20_change_pct_1h"] < -0.0)
      ):
        return True, f"exit_{mode_name}_d_6_130"
      elif (
        (last_candle["RSI_14"] < 44.0)
        and (last_candle["RSI_3_1h"] < 20.0)
        and (last_candle["RSI_3_4h"] < 30.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_6_131"
      elif (
        (last_candle["RSI_3"] > 74.0)
        and (last_candle["RSI_3_1h"] < 35.0)
        and (last_candle["RSI_3_4h"] < 35.0)
        and (last_candle["AROONU_14_1h"] > 50.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 40.0)
      ):
        return True, f"exit_{mode_name}_d_6_132"
      elif (
        (last_candle["RSI_3"] > 74.0)
        and (last_candle["AROONU_14_15m"] > 75.0)
        and (last_candle["AROONU_14_1h"] > 75.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 25.0))
      ):
        return True, f"exit_{mode_name}_d_6_133"
    elif 0.08 > current_profit >= 0.07:
      if (
        (last_candle["WILLR_14"] > -1.0)
        and (last_candle["RSI_14"] > 78.0)
        and (
          isinstance(last_candle["EMA_200_1h"], np.float64) and (last_candle["EMA_12_1h"] < last_candle["EMA_200_1h"])
        )
        and (
          isinstance(last_candle["EMA_200_4h"], np.float64) and (last_candle["EMA_12_4h"] < last_candle["EMA_200_4h"])
        )
        and (last_candle["KST_10_15_20_30_10_10_10_15_1h"] < last_candle["KSTs_9_1h"])
        and (last_candle["KST_10_15_20_30_10_10_10_15_4h"] < last_candle["KSTs_9_4h"])
      ):
        return True, f"exit_{mode_name}_d_7_1"
      elif (
        (last_candle["WILLR_14"] > -1.0)
        and (last_candle["RSI_14"] > 64.0)
        and (last_candle["CMF_20_1h"] < -0.0)
        and (
          isinstance(last_candle["EMA_200_1h"], np.float64) and (last_candle["EMA_12_1h"] < last_candle["EMA_200_1h"])
        )
        and (
          isinstance(last_candle["EMA_200_4h"], np.float64) and (last_candle["EMA_12_4h"] < last_candle["EMA_200_4h"])
        )
      ):
        return True, f"exit_{mode_name}_d_7_2"
      elif (
        (last_candle["WILLR_14"] > -10.0)
        and (last_candle["STOCHRSIk_14_14_3_3"] > 98.0)
        and (last_candle["CMF_20_1h"] < -0.0)
        and (last_candle["CMF_20_4h"] < -0.0)
        and (
          (last_candle["STOCHRSIk_14_14_3_3_4h"] > 20.0) and (last_candle["STOCHRSIk_14_14_3_3_change_pct_4h"] < -10.0)
        )
      ):
        return True, f"exit_{mode_name}_d_7_3"
      elif (
        (last_candle["WILLR_14"] > -20.0)
        and (last_candle["RSI_14"] > 70.0)
        and (last_candle["STOCHRSIk_14_14_3_3"] > 95.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 70.0)
        and (
          isinstance(last_candle["EMA_200_1h"], np.float64) and (last_candle["EMA_12_1h"] < last_candle["EMA_200_1h"])
        )
        and (
          isinstance(last_candle["EMA_200_4h"], np.float64) and (last_candle["EMA_12_4h"] < last_candle["EMA_200_4h"])
        )
      ):
        return True, f"exit_{mode_name}_d_7_4"
      elif (
        (last_candle["WILLR_14"] > -6.0)
        and (last_candle["RSI_14"] > 68.0)
        and (last_candle["ROC_9_1h"] < -5.0)
        and (last_candle["ROC_9_4h"] < -5.0)
      ):
        return True, f"exit_{mode_name}_d_7_5"
      elif (
        (last_candle["RSI_3"] > 70.0)
        and (last_candle["STOCHRSIk_14_14_3_3"] > 70.0)
        and (last_candle["RSI_14"] < 40.0)
        and (last_candle["ROC_9_1h"] < -10.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 50.0))
      ):
        return True, f"exit_{mode_name}_d_7_6"
      elif (
        (last_candle["RSI_14"] < 50.0)
        and (last_candle["STOCHRSIk_14_14_3_3"] > 70.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -40.0))
      ):
        return True, f"exit_{mode_name}_d_7_7"
      elif (
        (last_candle["WILLR_14"] > -6.0)
        and (last_candle["STOCHRSIk_14_14_3_3"] > 95.0)
        and (last_candle["CMF_20_1h"] < -0.1)
        and (last_candle["CMF_20_4h"] < -0.1)
        and (last_candle["change_pct_1d"] < -5.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 15.0))
      ):
        return True, f"exit_{mode_name}_d_7_8"
      elif (
        (last_candle["WILLR_14"] > -6.0)
        and (last_candle["RSI_3"] > 95.0)
        and (last_candle["change_pct_4h"] < -5.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 30.0))
      ):
        return True, f"exit_{mode_name}_d_7_9"
      elif (
        (last_candle["WILLR_14"] > -10.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["ROC_9_1h"] < -10.0)
        and (last_candle["ROC_9_4h"] < -10.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 10.0))
      ):
        return True, f"exit_{mode_name}_d_7_10"
      elif (
        (last_candle["RSI_3"] > 85.0)
        and (last_candle["RSI_14"] < 45.0)
        and (last_candle["ROC_9_15m"] < -10.0)
        and (last_candle["ROC_9_1h"] < -10.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -20.0))
      ):
        return True, f"exit_{mode_name}_d_7_11"
      elif (
        (last_candle["RSI_3"] > 80.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_4h"] < 10.0)
        and (last_candle["ROC_9_1h"] < -20.0)
        and (last_candle["ROC_9_4h"] < -20.0)
      ):
        return True, f"exit_{mode_name}_d_7_12"
      elif (last_candle["RSI_3"] > 90.0) and (last_candle["RSI_3_4h"] < 5.0) and (last_candle["ROC_9_4h"] < -25.0):
        return True, f"exit_{mode_name}_d_7_13"
      elif (
        (last_candle["RSI_3"] > 90.0)
        and (last_candle["WILLR_14"] > -8.0)
        and (last_candle["RSI_3_4h"] < 5.0)
        and (last_candle["AROONU_14_4h"] > 25.0)
      ):
        return True, f"exit_{mode_name}_d_7_14"
      elif (last_candle["RSI_3"] > 90.0) and (last_candle["RSI_14"] > 62.0) and (last_candle["ROC_9_4h"] < -30.0):
        return True, f"exit_{mode_name}_d_7_15"
      elif (
        (last_candle["RSI_3"] > 80.0)
        and (last_candle["AROONU_14_4h"] > 25.0)
        and (last_candle["ROC_9_4h"] < -25.0)
        and (last_candle["AROONU_14_1d"] > 50.0)
        and (last_candle["change_pct_1d"] < -15.0)
      ):
        return True, f"exit_{mode_name}_d_7_16"
      elif (
        (last_candle["RSI_3"] > 90.0)
        and (last_candle["WILLR_14"] > -25.0)
        and (last_candle["RSI_3_1h"] < 10.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 90.0)
        and (last_candle["ROC_9_4h"] > 30.0)
      ):
        return True, f"exit_{mode_name}_d_7_17"
      elif (
        (last_candle["RSI_3"] > 85.0)
        and (last_candle["RSI_14"] > 70.0)
        and (last_candle["RSI_3_4h"] < 20.0)
        and (last_candle["ROC_2_1d"] < -50.0)
      ):
        return True, f"exit_{mode_name}_d_7_18"
      elif (
        (last_candle["RSI_3"] > 88.0)
        and (last_candle["RSI_14"] > 68.0)
        and (last_candle["RSI_3_4h"] < 10.0)
        and (
          isinstance(last_candle["STOCHRSIk_14_14_3_3_1d"], np.float64)
          and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 70.0)
        )
      ):
        return True, f"exit_{mode_name}_d_7_19"
      elif (
        (last_candle["RSI_3"] > 46.0)
        and (last_candle["RSI_14"] < 44.0)
        and (last_candle["RSI_3_1h"] < 10.0)
        and (last_candle["AROONU_14_1h"] > 25.0)
      ):
        return True, f"exit_{mode_name}_d_7_20"
      elif (
        (last_candle["RSI_3"] > 70.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_1h"] < 20.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 90.0)
      ):
        return True, f"exit_{mode_name}_d_7_21"
      elif (
        (last_candle["RSI_3"] > 94.0)
        and (last_candle["WILLR_14"] > -6.0)
        and (last_candle["change_pct_4h"] < -5.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -30.0))
      ):
        return True, f"exit_{mode_name}_d_7_22"
      elif (
        (last_candle["RSI_3"] > 85.0)
        and (last_candle["WILLR_14"] > -20.0)
        and (last_candle["RSI_3_1h"] < 15.0)
        and (last_candle["RSI_3_1d"] < 5.0)
      ):
        return True, f"exit_{mode_name}_d_7_23"
      elif (
        (last_candle["RSI_3"] > 88.0)
        and (last_candle["RSI_14"] > 68.0)
        and (last_candle["WILLR_14"] > -25.0)
        and (last_candle["RSI_3_4h"] < 30.0)
        and (last_candle["AROONU_14_4h"] > 75.0)
      ):
        return True, f"exit_{mode_name}_d_7_24"
      elif (
        (last_candle["RSI_3"] > 80.0)
        and (last_candle["WILLR_14"] > -8.0)
        and (last_candle["RSI_3_4h"] < 10.0)
        and (last_candle["ROC_9_4h"] < -15.0)
        and (
          isinstance(last_candle["STOCHRSIk_14_14_3_3_1d"], np.float64)
          and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 50.0)
        )
      ):
        return True, f"exit_{mode_name}_d_7_25"
      elif (
        (last_candle["RSI_3"] > 75.0)
        and (last_candle["WILLR_14"] > -8.0)
        and (last_candle["RSI_3_4h"] < 15.0)
        and (last_candle["ROC_9_4h"] < -20.0)
      ):
        return True, f"exit_{mode_name}_d_7_26"
      elif (
        (last_candle["RSI_3"] > 75.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_1h"] < 20.0)
        and (last_candle["RSI_3_4h"] < 20.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 20.0)
      ):
        return True, f"exit_{mode_name}_d_7_27"
      elif (
        (last_candle["RSI_3"] > 70.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_15m"] < 10.0)
        and (last_candle["ROC_9_4h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_7_28"
      elif (
        (last_candle["RSI_3"] > 85.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_1h"] < 20.0)
        and (last_candle["RSI_3_4h"] < 20.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 30.0)
      ):
        return True, f"exit_{mode_name}_d_7_29"
      elif (
        (last_candle["RSI_3"] > 80.0)
        and (last_candle["RSI_3_1h"] < 25.0)
        and (last_candle["RSI_3_4h"] < 10.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 70.0)
      ):
        return True, f"exit_{mode_name}_d_7_30"
      elif (
        (last_candle["RSI_3"] > 70.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_1h"] < 15.0)
        and (last_candle["RSI_3_4h"] < 15.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 25.0)
      ):
        return True, f"exit_{mode_name}_d_7_31"
      elif (
        (last_candle["RSI_3"] > 80.0)
        and (last_candle["RSI_3_1h"] < 15.0)
        and (last_candle["ROC_2_4h"] < -30.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 30.0)
      ):
        return True, f"exit_{mode_name}_d_7_32"
      elif (
        (last_candle["RSI_3"] > 80.0)
        and (last_candle["WILLR_14"] > -6.0)
        and (last_candle["ROC_2_1h"] < -10.0)
        and (last_candle["ROC_9_1h"] > 30.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_7_33"
      elif (
        (last_candle["RSI_3"] > 65.0)
        and (last_candle["RSI_3_15m"] < 30.0)
        and (last_candle["RSI_14_1h"] > 80.0)
        and (last_candle["ROC_9_1h"] > 40.0)
      ):
        return True, f"exit_{mode_name}_d_7_34"
      elif (
        (last_candle["RSI_3"] > 84.0)
        and (last_candle["WILLR_14"] > -8.0)
        and (last_candle["RSI_3_1d"] < 25.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 75.0)
      ):
        return True, f"exit_{mode_name}_d_7_35"
      elif (
        (last_candle["RSI_3"] > 75.0)
        and (last_candle["WILLR_14"] > -25.0)
        and (last_candle["ROC_9_4h"] < -25.0)
        and (last_candle["RSI_3_1d"] < 25.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_7_36"
      elif (
        (last_candle["RSI_3"] > 78.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_1h"] < 20.0)
        and (last_candle["RSI_3_1d"] < 25.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_7_37"
      elif (
        (last_candle["RSI_3"] > 75.0)
        and (last_candle["WILLR_14"] > -25.0)
        and (last_candle["RSI_3_4h"] < 10.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 20.0)
      ):
        return True, f"exit_{mode_name}_d_7_38"
      elif (
        (last_candle["RSI_3"] > 93.0)
        and (last_candle["WILLR_14"] > -7.0)
        and (last_candle["CMF_20_4h"] < -0.0)
        and (last_candle["RSI_3_4h"] < 10.0)
      ):
        return True, f"exit_{mode_name}_d_7_39"
      elif (
        (last_candle["RSI_3"] > 75.0)
        and (last_candle["WILLR_14"] > -25.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 30.0)
        and (
          isinstance(last_candle["STOCHRSIk_14_14_3_3_1d"], np.float64)
          and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 90.0)
        )
      ):
        return True, f"exit_{mode_name}_d_7_40"
      elif (
        (last_candle["RSI_3"] > 85.0)
        and (last_candle["WILLR_14"] > -20.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 25.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 50.0))
      ):
        return True, f"exit_{mode_name}_d_7_41"
      elif (
        (last_candle["RSI_3"] > 80.0)
        and (last_candle["WILLR_14"] > -35.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 30.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 40.0))
        and (
          isinstance(last_candle["STOCHRSIk_14_14_3_3_1d"], np.float64)
          and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 70.0)
        )
      ):
        return True, f"exit_{mode_name}_d_7_42"
      elif (
        (last_candle["RSI_3"] > 80.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_1h"] < 15.0)
        and (last_candle["RSI_3_4h"] < 40.0)
        and (
          isinstance(last_candle["STOCHRSIk_14_14_3_3_1d"], np.float64)
          and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 90.0)
        )
      ):
        return True, f"exit_{mode_name}_d_7_43"
      elif (
        (last_candle["RSI_3"] > 60.0)
        and (last_candle["WILLR_14"] > -15.0)
        and (last_candle["RSI_3_4h"] < 30.0)
        and (last_candle["RSI_3_1d"] < 25.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -30.0))
      ):
        return True, f"exit_{mode_name}_d_7_44"
      elif (last_candle["RSI_3"] > 90.0) and (last_candle["WILLR_14"] > -10.0) and (last_candle["RSI_3_1h"] < 10.0):
        return True, f"exit_{mode_name}_d_7_45"
      elif (
        (last_candle["RSI_3"] > 80.0)
        and (last_candle["RSI_3_1h"] < 15.0)
        and (last_candle["RSI_3_4h"] < 10.0)
        and (last_candle["ROC_2_1d"] < -20.0)
      ):
        return True, f"exit_{mode_name}_d_7_46"
      elif (
        (last_candle["RSI_3"] > 82.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 80.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 40.0)
        and (last_candle["change_pct_1d"] < -5.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -5.0))
      ):
        return True, f"exit_{mode_name}_d_7_47"
      elif (
        (last_candle["RSI_3"] > 55.0)
        and (last_candle["RSI_14"] < 48.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (last_candle["RSI_3_4h"] < 20.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_7_48"
      elif (
        (last_candle["RSI_3"] > 80.0)
        and (last_candle["WILLR_14"] > -8.0)
        and (last_candle["RSI_3_4h"] < 20.0)
        and (last_candle["change_pct_1d"] < -5.0)
        and (
          isinstance(last_candle["STOCHRSIk_14_14_3_3_1d"], np.float64)
          and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 50.0)
        )
      ):
        return True, f"exit_{mode_name}_d_7_49"
      elif (
        (last_candle["RSI_3"] > 80.0)
        and (last_candle["WILLR_14"] > -8.0)
        and (last_candle["RSI_3_1d"] < 10.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 90.0)
      ):
        return True, f"exit_{mode_name}_d_7_50"
      elif (
        (last_candle["RSI_3"] > 62.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_4h"] < 20.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_7_51"
      elif (
        (last_candle["RSI_3"] > 76.0)
        and (last_candle["RSI_14"] > 56.0)
        and (last_candle["WILLR_14"] > -10.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 70.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -15.0))
      ):
        return True, f"exit_{mode_name}_d_7_52"
      elif (
        (last_candle["RSI_3"] > 70.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["WILLR_14"] > -25.0)
        and (last_candle["RSI_3_1h"] < 20.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
        and (
          isinstance(last_candle["STOCHRSIk_14_14_3_3_1d"], np.float64)
          and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 50.0)
        )
      ):
        return True, f"exit_{mode_name}_d_7_53"
      elif (
        (last_candle["RSI_3"] > 74.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
        and (last_candle["ROC_9_4h"] < -10.0)
        and (last_candle["change_pct_1d"] < -10.0)
      ):
        return True, f"exit_{mode_name}_d_7_54"
      elif (
        (last_candle["RSI_3"] > 90.0)
        and (last_candle["WILLR_14"] > -18.0)
        and (last_candle["ROC_9_4h"] < -5.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 10.0))
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_7_55"
      elif (
        (last_candle["RSI_3"] > 70.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (last_candle["RSI_3_4h"] < 25.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -30.0))
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 10.0)
      ):
        return True, f"exit_{mode_name}_d_7_56"
      elif (
        (last_candle["RSI_3"] > 50.0)
        and (last_candle["RSI_14"] < 40.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -30.0))
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 70.0)
      ):
        return True, f"exit_{mode_name}_d_7_57"
      elif (
        (last_candle["RSI_3"] > 80.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (last_candle["RSI_3_4h"] < 30.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -15.0))
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_7_58"
      elif (
        (last_candle["RSI_3"] > 85.0)
        and (last_candle["WILLR_14"] > -16.0)
        and (last_candle["RSI_3_4h"] < 25.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -15.0))
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 40.0)
      ):
        return True, f"exit_{mode_name}_d_7_59"
      elif (
        (last_candle["RSI_3"] > 65.0)
        and (last_candle["RSI_14"] < 44.0)
        and (last_candle["RSI_14_4h"] > 65.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_7_60"
      elif (
        (last_candle["RSI_3"] > 90.0)
        and (last_candle["WILLR_14"] > -25.0)
        and (last_candle["RSI_3_4h"] < 10.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 30.0)
      ):
        return True, f"exit_{mode_name}_d_7_61"
      elif (
        (last_candle["RSI_3"] > 82.0)
        and (last_candle["WILLR_14"] > -6.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (last_candle["RSI_3_4h"] < 20.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 20.0))
        and (last_candle["change_pct_1d"] < -5.0)
      ):
        return True, f"exit_{mode_name}_d_7_62"
      elif (
        (last_candle["RSI_3"] > 64.0)
        and (last_candle["RSI_3_1d"] < 25.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 80.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 30.0)
      ):
        return True, f"exit_{mode_name}_d_7_63"
      elif (
        (last_candle["RSI_3"] > 84.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (last_candle["RSI_3_4h"] < 30.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 30.0))
      ):
        return True, f"exit_{mode_name}_d_7_64"
      elif (
        (last_candle["RSI_3"] > 64.0)
        and (last_candle["RSI_14"] < 46.0)
        and (last_candle["RSI_3_1h"] < 20.0)
        and (last_candle["RSI_3_4h"] < 15.0)
      ):
        return True, f"exit_{mode_name}_d_7_65"
      elif (
        (last_candle["RSI_3"] > 78.0)
        and (last_candle["RSI_14"] < 52.0)
        and (last_candle["RSI_3_1h"] < 20.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_7_66"
      elif (
        (last_candle["RSI_3"] > 50.0)
        and (last_candle["RSI_14"] < 46.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 80.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -25.0))
      ):
        return True, f"exit_{mode_name}_d_7_67"
      elif (
        (last_candle["RSI_3"] > 80.0)
        and (last_candle["RSI_14"] < 52.0)
        and (last_candle["RSI_3_1h"] < 25.0)
        and (last_candle["ROC_2_4h"] < -30.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 25.0)
      ):
        return True, f"exit_{mode_name}_d_7_68"
      elif (
        (last_candle["RSI_3"] > 94.0)
        and (last_candle["ROC_9_4h"] > 20.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
        and (last_candle["change_pct_4h"] < -5.0)
      ):
        return True, f"exit_{mode_name}_d_7_69"
      elif (
        (last_candle["RSI_3"] > 62.0)
        and (last_candle["RSI_14"] < 44.0)
        and (last_candle["RSI_3_1h"] < 25.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 20.0)
      ):
        return True, f"exit_{mode_name}_d_7_70"
      elif (
        (last_candle["RSI_3"] > 60.0)
        and (last_candle["RSI_14"] < 48.0)
        and (last_candle["RSI_3_4h"] < 25.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 20.0)
      ):
        return True, f"exit_{mode_name}_d_7_71"
      elif (
        (last_candle["RSI_3"] > 74.0)
        and (last_candle["RSI_14"] < 46.0)
        and (last_candle["RSI_3_1h"] < 10.0)
        and (last_candle["AROONU_14_4h"] > 25.0)
      ):
        return True, f"exit_{mode_name}_d_7_72"
      elif (
        (last_candle["RSI_3"] > 74.0)
        and (last_candle["RSI_3_1h"] < 25.0)
        and (last_candle["RSI_3_4h"] < 15.0)
        and (last_candle["ROC_9_4h"] < -20.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -25.0))
      ):
        return True, f"exit_{mode_name}_d_7_73"
      elif (
        (last_candle["RSI_3"] > 96.0)
        and (last_candle["WILLR_14"] > -10.0)
        and (last_candle["RSI_3_4h"] < 25.0)
        and (last_candle["RSI_3_1d"] < 25.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_7_74"
      elif (
        (last_candle["RSI_3"] > 92.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (last_candle["RSI_3_4h"] < 20.0)
        and (
          isinstance(last_candle["STOCHRSIk_14_14_3_3_1d"], np.float64)
          and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 50.0)
        )
      ):
        return True, f"exit_{mode_name}_d_7_75"
      elif (
        (last_candle["RSI_3"] > 64.0)
        and (last_candle["RSI_14"] < 54.0)
        and (last_candle["ROC_9_1h"] > 80.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 80.0)
      ):
        return True, f"exit_{mode_name}_d_7_76"
      elif (
        (last_candle["RSI_3"] > 72.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 50.0))
      ):
        return True, f"exit_{mode_name}_d_7_77"
      elif (
        (last_candle["RSI_3"] > 82.0)
        and (last_candle["WILLR_14"] > -20.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (last_candle["RSI_3_4h"] < 20.0)
        and (last_candle["RSI_3_1d"] < 20.0)
      ):
        return True, f"exit_{mode_name}_d_7_78"
      elif (
        (last_candle["RSI_3"] > 88.0)
        and (last_candle["WILLR_14"] > -6.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (last_candle["RSI_3_4h"] < 10.0)
      ):
        return True, f"exit_{mode_name}_d_7_79"
      elif (
        (last_candle["RSI_3"] > 68.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 50.0))
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 25.0)
      ):
        return True, f"exit_{mode_name}_d_7_80"
      elif (
        (last_candle["RSI_3"] > 80.0)
        and (last_candle["WILLR_14"] > -14.0)
        and (last_candle["RSI_3_1h"] < 25.0)
        and (last_candle["RSI_3_4h"] < 25.0)
        and (isinstance(last_candle["RSI_14_1d"], np.float64) and (last_candle["RSI_14_1d"] > 50.0))
      ):
        return True, f"exit_{mode_name}_d_7_81"
      elif (
        (last_candle["RSI_3"] > 78.0)
        and (last_candle["WILLR_14"] > -14.0)
        and (last_candle["RSI_3_4h"] < 30.0)
        and (last_candle["RSI_3_1d"] < 15.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 40.0)
      ):
        return True, f"exit_{mode_name}_d_7_82"
      elif (
        (last_candle["RSI_3"] > 68.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_1h"] < 40.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 40.0)
      ):
        return True, f"exit_{mode_name}_d_7_83"
      elif (
        (last_candle["RSI_3"] > 86.0)
        and (last_candle["WILLR_14"] > -6.0)
        and (last_candle["RSI_3_4h"] < 30.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 20.0)
      ):
        return True, f"exit_{mode_name}_d_7_84"
      elif (
        (last_candle["RSI_3"] > 84.0)
        and (last_candle["WILLR_14"] > -12.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (last_candle["RSI_3_4h"] < 40.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_7_85"
      elif (
        (last_candle["RSI_3"] > 90.0)
        and (last_candle["RSI_14_4h"] > 80.0)
        and (last_candle["ROC_2_1h"] < -5.0)
        and (last_candle["ROC_9_1h"] > 5.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_7_86"
      elif (
        (last_candle["RSI_3"] > 62.0)
        and (last_candle["RSI_14"] < 48.0)
        and (last_candle["RSI_3_1h"] < 45.0)
        and (last_candle["RSI_3_4h"] < 50.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_7_87"
      elif (
        (last_candle["RSI_3"] > 84.0)
        and (last_candle["WILLR_14"] > -24.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 40.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
        and (last_candle["change_pct_1h"] < -2.0)
      ):
        return True, f"exit_{mode_name}_d_7_88"
      elif (
        (last_candle["RSI_3"] > 74.0)
        and (last_candle["RSI_14"] < 44.0)
        and (last_candle["ROC_9_1h"] < -5.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 25.0))
      ):
        return True, f"exit_{mode_name}_d_7_89"
      elif (
        (last_candle["RSI_3"] > 88.0)
        and (last_candle["WILLR_14"] > -25.0)
        and (last_candle["RSI_3_1h"] < 50.0)
        and (last_candle["RSI_3_4h"] < 30.0)
        and (last_candle["AROONU_14_4h"] > 50.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 40.0))
      ):
        return True, f"exit_{mode_name}_d_7_90"
      elif (
        (last_candle["RSI_3"] > 68.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_1h"] < 25.0)
        and (last_candle["RSI_3_4h"] < 25.0)
        and (last_candle["AROONU_14_4h"] > 50.0)
        and (
          isinstance(last_candle["STOCHRSIk_14_14_3_3_1d"], np.float64)
          and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 50.0)
        )
      ):
        return True, f"exit_{mode_name}_d_7_91"
      elif (
        (last_candle["RSI_3"] > 76.0)
        and (last_candle["RSI_14"] < 52.0)
        and (last_candle["RSI_3_1h"] < 40.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 25.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -25.0))
      ):
        return True, f"exit_{mode_name}_d_7_92"
      elif (
        (last_candle["RSI_3"] > 68.0)
        and (last_candle["RSI_14"] < 54.0)
        and (last_candle["RSI_3_15m"] < 50.0)
        and (last_candle["AROONU_14_1h"] > 75.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 70.0)
        and (last_candle["AROONU_14_4h"] > 50.0)
        and (
          isinstance(last_candle["STOCHRSIk_14_14_3_3_1d"], np.float64)
          and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 90.0)
        )
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 30.0))
      ):
        return True, f"exit_{mode_name}_d_7_93"
      elif (
        (last_candle["RSI_3"] > 76.0)
        and (last_candle["RSI_14"] < 54.0)
        and (last_candle["RSI_3_1h"] < 25.0)
        and (last_candle["RSI_3_4h"] < 45.0)
        and (last_candle["AROONU_14_1h"] > 75.0)
        and (
          isinstance(last_candle["STOCHRSIk_14_14_3_3_1d"], np.float64)
          and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 90.0)
        )
      ):
        return True, f"exit_{mode_name}_d_7_94"
      elif (
        (last_candle["RSI_3"] > 80.0)
        and (last_candle["WILLR_14"] > -16.0)
        and (last_candle["RSI_3_1h"] < 45.0)
        and (last_candle["RSI_3_4h"] < 40.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 10.0)
        and (isinstance(last_candle["AROONU_14_1d"], np.float64) and (last_candle["AROONU_14_1d"] > 75.0))
      ):
        return True, f"exit_{mode_name}_d_7_95"
      elif (
        (last_candle["RSI_3"] > 58.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_1h"] < 45.0)
        and (last_candle["RSI_3_1d"] < 45.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_7_96"
      elif (
        (last_candle["RSI_3"] > 80.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_1h"] < 35.0)
        and (last_candle["AROONU_14_4h"] > 50.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 30.0)
      ):
        return True, f"exit_{mode_name}_d_7_97"
      elif (
        (last_candle["RSI_3"] > 86.0)
        and (last_candle["RSI_3_15m"] > 68.0)
        and (last_candle["RSI_3_1h"] < 60.0)
        and (last_candle["RSI_3_4h"] < 60.0)
        and (last_candle["RSI_3_1d"] > 80.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_7_98"
      elif (
        (last_candle["RSI_3"] > 56.0)
        and (last_candle["RSI_14"] < 56.0)
        and (last_candle["RSI_3_1h"] < 65.0)
        and (last_candle["RSI_3_4h"] < 60.0)
        and (last_candle["AROONU_14_4h"] > 50.0)
        and (last_candle["STOCHk_14_3_3_4h"] > 40.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 80.0))
      ):
        return True, f"exit_{mode_name}_d_7_99"
      elif (
        (last_candle["RSI_3"] > 94.0)
        and (last_candle["RSI_14"] > 72.0)
        and (last_candle["RSI_3_15m"] > 70.0)
        and (last_candle["RSI_3_4h"] < 80.0)
      ):
        return True, f"exit_{mode_name}_d_7_100"
      elif (
        (last_candle["RSI_3"] > 80.0)
        and (last_candle["WILLR_14"] > -20.0)
        and (last_candle["RSI_3_1h"] < 50.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 40.0)
        and (isinstance(last_candle["ROC_9_4h"], np.float64) and (last_candle["ROC_9_4h"] > 40.0))
      ):
        return True, f"exit_{mode_name}_d_7_101"
      elif (
        (last_candle["RSI_3"] > 64.0)
        and (last_candle["RSI_14"] < 52.0)
        and (last_candle["RSI_3_1h"] < 60.0)
        and (last_candle["RSI_3_4h"] < 40.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 30.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 40.0))
      ):
        return True, f"exit_{mode_name}_d_7_102"
      elif (
        (last_candle["RSI_3"] > 74.0)
        and (last_candle["RSI_14"] < 60.0)
        and (last_candle["RSI_3_1h"] < 60.0)
        and (last_candle["RSI_14_4h"] > 70.0)
        and (isinstance(last_candle["ROC_9_4h"], np.float64) and (last_candle["ROC_9_4h"] > 80.0))
      ):
        return True, f"exit_{mode_name}_d_7_103"
      elif (
        (last_candle["RSI_3"] > 60.0)
        and (last_candle["RSI_14"] < 52.0)
        and (last_candle["RSI_3_1h"] < 60.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 40.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 90.0)
        and (last_candle["ROC_9_4h"] > 40.0)
      ):
        return True, f"exit_{mode_name}_d_7_104"
      elif (
        (last_candle["RSI_3"] > 74.0)
        and (last_candle["RSI_14"] < 52.0)
        and (last_candle["RSI_3_15m"] < 55.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 90.0)
        and (last_candle["ROC_9_4h"] > 25.0)
      ):
        return True, f"exit_{mode_name}_d_7_105"
      elif (
        (last_candle["RSI_3"] > 68.0)
        and (last_candle["RSI_14"] < 52.0)
        and (last_candle["RSI_3_1h"] < 50.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
        and (last_candle["RSI_14_4h"] > 70.0)
        and (last_candle["ROC_9_4h"] > 40.0)
      ):
        return True, f"exit_{mode_name}_d_7_106"
      elif (
        (last_candle["RSI_3"] > 70.0)
        and (last_candle["RSI_14"] < 52.0)
        and (last_candle["RSI_3_1h"] < 50.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 70.0)
        and (last_candle["RSI_14_4h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_7_107"
      elif (
        (last_candle["RSI_3"] > 52.0)
        and (last_candle["RSI_14"] < 52.0)
        and (last_candle["RSI_3_1h"] < 60.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 80.0)
      ):
        return True, f"exit_{mode_name}_d_7_108"
      elif (
        (last_candle["RSI_3"] > 72.0)
        and (last_candle["WILLR_14"] > -12.0)
        and (last_candle["RSI_3_1h"] < 50.0)
        and (last_candle["RSI_3_4h"] < 20.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 50.0))
      ):
        return True, f"exit_{mode_name}_d_7_109"
      elif (
        (last_candle["RSI_3"] > 68.0)
        and (last_candle["RSI_3_4h"] < 65.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
        and (last_candle["ROC_9_4h"] > 25.0)
      ):
        return True, f"exit_{mode_name}_d_7_110"
      elif (
        (last_candle["RSI_3"] > 46.0)
        and (last_candle["RSI_14"] < 48.0)
        and (last_candle["RSI_3_1h"] < 50.0)
        and (last_candle["RSI_14_4h"] > 70.0)
        and (last_candle["AROONU_14_1h"] > 75.0)
        and (last_candle["AROONU_14_4h"] > 75.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 20.0))
      ):
        return True, f"exit_{mode_name}_d_7_111"
      elif (
        (last_candle["RSI_3"] > 76.0)
        and (last_candle["WILLR_14"] > -35.0)
        and (last_candle["RSI_14"] < 56.0)
        and (last_candle["RSI_3_1h"] < 35.0)
        and (last_candle["RSI_3_4h"] < 35.0)
        and (last_candle["RSI_3_1d"] < 60.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 30.0))
      ):
        return True, f"exit_{mode_name}_d_7_112"
      elif (
        (last_candle["RSI_3"] > 80.0)
        and (last_candle["WILLR_14"] > -4.0)
        and (last_candle["RSI_3_1d"] < 30.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
        and (isinstance(last_candle["ROC_9_4h"], np.float64) and (last_candle["ROC_9_4h"] > 10.0))
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -10.0))
      ):
        return True, f"exit_{mode_name}_d_7_113"
      elif (
        (last_candle["RSI_3"] > 80.0)
        and (last_candle["RSI_14"] < 54.0)
        and (last_candle["RSI_3_1h"] < 20.0)
        and (last_candle["RSI_3_4h"] < 30.0)
        and (last_candle["RSI_3_1d"] < 30.0)
      ):
        return True, f"exit_{mode_name}_d_7_114"
      elif (
        (last_candle["RSI_3"] > 74.0)
        and (last_candle["RSI_14"] < 52.0)
        and (last_candle["RSI_3_15m"] < 30.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_7_115"
      elif (
        (last_candle["RSI_3"] > 86.0)
        and (last_candle["RSI_3_1h"] < 15.0)
        and (last_candle["RSI_3_4h"] < 40.0)
        and (last_candle["AROONU_14_4h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_7_116"
      elif (
        (last_candle["RSI_3"] > 82.0)
        and (last_candle["RSI_3_1h"] < 50.0)
        and (last_candle["AROONU_14_1h"] > 80.0)
        and (last_candle["AROONU_14_4h"] > 80.0)
      ):
        return True, f"exit_{mode_name}_d_7_117"
      elif (
        (last_candle["RSI_3"] > 86.0)
        and (last_candle["RSI_3_1h"] < 20.0)
        and (last_candle["RSI_3_4h"] < 60.0)
        and (last_candle["AROONU_14_4h"] > 40.0)
      ):
        return True, f"exit_{mode_name}_d_7_118"
      elif (
        (last_candle["RSI_3"] > 82.0)
        and (last_candle["WILLR_14"] > -20.0)
        and (last_candle["RSI_3_1h"] < 60.0)
        and (last_candle["RSI_3_4h"] < 60.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 40.0)
      ):
        return True, f"exit_{mode_name}_d_7_119"
      elif (
        (last_candle["RSI_3"] > 50.0)
        and (last_candle["RSI_14"] < 52.0)
        and (last_candle["RSI_3_1h"] < 40.0)
        and (last_candle["AROONU_14_4h"] > 75.0)
      ):
        return True, f"exit_{mode_name}_d_7_120"
      elif (
        (last_candle["RSI_3"] > 56.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_1h"] < 50.0)
        and (last_candle["RSI_14_4h"] > 85.0)
      ):
        return True, f"exit_{mode_name}_d_7_121"
      elif (
        (last_candle["RSI_3"] > 54.0)
        and (last_candle["RSI_14"] < 48.0)
        and (last_candle["RSI_3_4h"] < 30.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_7_122"
      elif (
        (last_candle["RSI_3"] > 84.0)
        and (last_candle["WILLR_14"] > -8.0)
        and (last_candle["RSI_3_1h"] < 10.0)
        and (last_candle["RSI_3_1d"] < 30.0)
      ):
        return True, f"exit_{mode_name}_d_7_123"
      elif (
        (last_candle["RSI_3"] > 84.0)
        and (last_candle["RSI_3_1h"] < 15.0)
        and (
          isinstance(last_candle["STOCHRSIk_14_14_3_3_1d"], np.float64)
          and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 80.0)
        )
      ):
        return True, f"exit_{mode_name}_d_7_124"
      elif (
        (last_candle["RSI_3"] > 72.0)
        and (last_candle["WILLR_14"] > -8.0)
        and (last_candle["RSI_3_1h"] < 10.0)
        and (last_candle["RSI_3_4h"] < 40.0)
        and (last_candle["RSI_3_1d"] < 40.0)
        and (last_candle["close"] < (last_candle["high_max_30_1d"] * 0.50))
      ):
        return True, f"exit_{mode_name}_d_7_125"
      elif (
        (last_candle["RSI_3"] > 86.0)
        and (last_candle["RSI_3_1h"] < 15.0)
        and (last_candle["RSI_3_4h"] < 40.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_7_126"
      elif (
        (last_candle["RSI_3"] > 86.0)
        and (last_candle["RSI_3_1h"] < 10.0)
        and (last_candle["RSI_3_4h"] < 30.0)
        and (last_candle["RSI_3_1d"] < 40.0)
      ):
        return True, f"exit_{mode_name}_d_7_127"
      elif (last_candle["RSI_3"] > 90.0) and (last_candle["RSI_3_4h"] < 30.0) and (last_candle["AROONU_14_4h"] > 85.0):
        return True, f"exit_{mode_name}_d_7_128"
      elif (
        (last_candle["RSI_3"] > 82.0)
        and (last_candle["RSI_3_4h"] < 25.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 80.0))
      ):
        return True, f"exit_{mode_name}_d_7_129"
      elif (
        (last_candle["RSI_3"] > 70.0)
        and (last_candle["RSI_14_1h"] > 65.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 80.0)
        and (last_candle["CCI_20_change_pct_1h"] < -0.0)
      ):
        return True, f"exit_{mode_name}_d_7_130"
      elif (
        (last_candle["RSI_14"] < 42.0)
        and (last_candle["RSI_3_1h"] < 20.0)
        and (last_candle["RSI_3_4h"] < 30.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_7_131"
      elif (
        (last_candle["RSI_3"] > 76.0)
        and (last_candle["RSI_3_1h"] < 35.0)
        and (last_candle["RSI_3_4h"] < 35.0)
        and (last_candle["AROONU_14_1h"] > 50.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 40.0)
      ):
        return True, f"exit_{mode_name}_d_7_132"
      elif (
        (last_candle["RSI_3"] > 76.0)
        and (last_candle["AROONU_14_15m"] > 75.0)
        and (last_candle["AROONU_14_1h"] > 75.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 25.0))
      ):
        return True, f"exit_{mode_name}_d_7_133"
    elif 0.09 > current_profit >= 0.08:
      if (
        (last_candle["WILLR_14"] > -1.0)
        and (last_candle["RSI_14"] > 78.0)
        and (
          isinstance(last_candle["EMA_200_1h"], np.float64) and (last_candle["EMA_12_1h"] < last_candle["EMA_200_1h"])
        )
        and (
          isinstance(last_candle["EMA_200_4h"], np.float64) and (last_candle["EMA_12_4h"] < last_candle["EMA_200_4h"])
        )
        and (last_candle["KST_10_15_20_30_10_10_10_15_1h"] < last_candle["KSTs_9_1h"])
        and (last_candle["KST_10_15_20_30_10_10_10_15_4h"] < last_candle["KSTs_9_4h"])
      ):
        return True, f"exit_{mode_name}_d_8_1"
      elif (
        (last_candle["WILLR_14"] > -1.0)
        and (last_candle["RSI_14"] > 66.0)
        and (last_candle["CMF_20_1h"] < -0.0)
        and (
          isinstance(last_candle["EMA_200_1h"], np.float64) and (last_candle["EMA_12_1h"] < last_candle["EMA_200_1h"])
        )
        and (
          isinstance(last_candle["EMA_200_4h"], np.float64) and (last_candle["EMA_12_4h"] < last_candle["EMA_200_4h"])
        )
      ):
        return True, f"exit_{mode_name}_d_8_2"
      elif (
        (last_candle["WILLR_14"] > -8.0)
        and (last_candle["STOCHRSIk_14_14_3_3"] > 98.0)
        and (last_candle["CMF_20_1h"] < -0.0)
        and (last_candle["CMF_20_4h"] < -0.0)
        and (
          (last_candle["STOCHRSIk_14_14_3_3_4h"] > 20.0) and (last_candle["STOCHRSIk_14_14_3_3_change_pct_4h"] < -10.0)
        )
      ):
        return True, f"exit_{mode_name}_d_8_3"
      elif (
        (last_candle["WILLR_14"] > -15.0)
        and (last_candle["RSI_14"] > 72.0)
        and (last_candle["STOCHRSIk_14_14_3_3"] > 95.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 70.0)
        and (
          isinstance(last_candle["EMA_200_1h"], np.float64) and (last_candle["EMA_12_1h"] < last_candle["EMA_200_1h"])
        )
        and (
          isinstance(last_candle["EMA_200_4h"], np.float64) and (last_candle["EMA_12_4h"] < last_candle["EMA_200_4h"])
        )
      ):
        return True, f"exit_{mode_name}_d_8_4"
      elif (
        (last_candle["WILLR_14"] > -4.0)
        and (last_candle["RSI_14"] > 70.0)
        and (last_candle["ROC_9_1h"] < -5.0)
        and (last_candle["ROC_9_4h"] < -5.0)
      ):
        return True, f"exit_{mode_name}_d_8_5"
      elif (
        (last_candle["RSI_3"] > 70.0)
        and (last_candle["STOCHRSIk_14_14_3_3"] > 70.0)
        and (last_candle["RSI_14"] < 40.0)
        and (last_candle["ROC_9_1h"] < -10.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 50.0))
      ):
        return True, f"exit_{mode_name}_d_8_6"
      elif (
        (last_candle["RSI_14"] < 50.0)
        and (last_candle["STOCHRSIk_14_14_3_3"] > 70.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -40.0))
      ):
        return True, f"exit_{mode_name}_d_8_7"
      elif (
        (last_candle["WILLR_14"] > -4.0)
        and (last_candle["STOCHRSIk_14_14_3_3"] > 95.0)
        and (last_candle["CMF_20_1h"] < -0.1)
        and (last_candle["CMF_20_4h"] < -0.1)
        and (last_candle["change_pct_1d"] < -5.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 15.0))
      ):
        return True, f"exit_{mode_name}_d_8_8"
      elif (
        (last_candle["WILLR_14"] > -5.0)
        and (last_candle["RSI_3"] > 95.0)
        and (last_candle["change_pct_4h"] < -5.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 30.0))
      ):
        return True, f"exit_{mode_name}_d_8_9"
      elif (
        (last_candle["WILLR_14"] > -8.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["ROC_9_1h"] < -10.0)
        and (last_candle["ROC_9_4h"] < -10.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 10.0))
      ):
        return True, f"exit_{mode_name}_d_8_10"
      elif (
        (last_candle["RSI_3"] > 90.0)
        and (last_candle["RSI_14"] < 45.0)
        and (last_candle["ROC_9_15m"] < -10.0)
        and (last_candle["ROC_9_1h"] < -10.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -20.0))
      ):
        return True, f"exit_{mode_name}_d_8_11"
      elif (
        (last_candle["RSI_3"] > 85.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_4h"] < 10.0)
        and (last_candle["ROC_9_1h"] < -20.0)
        and (last_candle["ROC_9_4h"] < -20.0)
      ):
        return True, f"exit_{mode_name}_d_8_12"
      elif (last_candle["RSI_3"] > 95.0) and (last_candle["RSI_3_4h"] < 5.0) and (last_candle["ROC_9_4h"] < -25.0):
        return True, f"exit_{mode_name}_d_8_13"
      elif (
        (last_candle["RSI_3"] > 90.0)
        and (last_candle["WILLR_14"] > -6.0)
        and (last_candle["RSI_3_4h"] < 5.0)
        and (last_candle["AROONU_14_4h"] > 25.0)
      ):
        return True, f"exit_{mode_name}_d_8_14"
      elif (last_candle["RSI_3"] > 92.0) and (last_candle["RSI_14"] > 64.0) and (last_candle["ROC_9_4h"] < -30.0):
        return True, f"exit_{mode_name}_d_8_15"
      elif (
        (last_candle["RSI_3"] > 85.0)
        and (last_candle["AROONU_14_4h"] > 25.0)
        and (last_candle["ROC_9_4h"] < -25.0)
        and (last_candle["AROONU_14_1d"] > 50.0)
        and (last_candle["change_pct_1d"] < -15.0)
      ):
        return True, f"exit_{mode_name}_d_8_16"
      elif (
        (last_candle["RSI_3"] > 95.0)
        and (last_candle["WILLR_14"] > -20.0)
        and (last_candle["RSI_3_1h"] < 10.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 90.0)
        and (last_candle["ROC_9_4h"] > 30.0)
      ):
        return True, f"exit_{mode_name}_d_8_17"
      elif (
        (last_candle["RSI_3"] > 90.0)
        and (last_candle["RSI_14"] > 72.0)
        and (last_candle["RSI_3_4h"] < 20.0)
        and (last_candle["ROC_2_1d"] < -50.0)
      ):
        return True, f"exit_{mode_name}_d_8_18"
      elif (
        (last_candle["RSI_3"] > 90.0)
        and (last_candle["RSI_14"] > 70.0)
        and (last_candle["RSI_3_4h"] < 10.0)
        and (
          isinstance(last_candle["STOCHRSIk_14_14_3_3_1d"], np.float64)
          and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 70.0)
        )
      ):
        return True, f"exit_{mode_name}_d_8_19"
      elif (
        (last_candle["RSI_3"] > 48.0)
        and (last_candle["RSI_14"] < 42.0)
        and (last_candle["RSI_3_1h"] < 10.0)
        and (last_candle["AROONU_14_1h"] > 25.0)
      ):
        return True, f"exit_{mode_name}_d_8_20"
      elif (
        (last_candle["RSI_3"] > 80.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_1h"] < 20.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 90.0)
      ):
        return True, f"exit_{mode_name}_d_8_21"
      elif (
        (last_candle["RSI_3"] > 96.0)
        and (last_candle["WILLR_14"] > -4.0)
        and (last_candle["change_pct_4h"] < -5.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -30.0))
      ):
        return True, f"exit_{mode_name}_d_8_22"
      elif (
        (last_candle["RSI_3"] > 90.0)
        and (last_candle["WILLR_14"] > -15.0)
        and (last_candle["RSI_3_1h"] < 15.0)
        and (last_candle["RSI_3_1d"] < 5.0)
      ):
        return True, f"exit_{mode_name}_d_8_23"
      elif (
        (last_candle["RSI_3"] > 90.0)
        and (last_candle["RSI_14"] > 70.0)
        and (last_candle["WILLR_14"] > -20.0)
        and (last_candle["RSI_3_4h"] < 30.0)
        and (last_candle["AROONU_14_4h"] > 75.0)
      ):
        return True, f"exit_{mode_name}_d_8_24"
      elif (
        (last_candle["RSI_3"] > 85.0)
        and (last_candle["WILLR_14"] > -6.0)
        and (last_candle["RSI_3_4h"] < 10.0)
        and (last_candle["ROC_9_4h"] < -15.0)
        and (
          isinstance(last_candle["STOCHRSIk_14_14_3_3_1d"], np.float64)
          and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 50.0)
        )
      ):
        return True, f"exit_{mode_name}_d_8_25"
      elif (
        (last_candle["RSI_3"] > 80.0)
        and (last_candle["WILLR_14"] > -6.0)
        and (last_candle["RSI_3_4h"] < 15.0)
        and (last_candle["ROC_9_4h"] < -20.0)
      ):
        return True, f"exit_{mode_name}_d_8_26"
      elif (
        (last_candle["RSI_3"] > 80.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_1h"] < 20.0)
        and (last_candle["RSI_3_4h"] < 20.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 20.0)
      ):
        return True, f"exit_{mode_name}_d_8_27"
      elif (
        (last_candle["RSI_3"] > 75.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_15m"] < 10.0)
        and (last_candle["ROC_9_4h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_8_28"
      elif (
        (last_candle["RSI_3"] > 90.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_1h"] < 20.0)
        and (last_candle["RSI_3_4h"] < 20.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 30.0)
      ):
        return True, f"exit_{mode_name}_d_8_29"
      elif (
        (last_candle["RSI_3"] > 85.0)
        and (last_candle["RSI_3_1h"] < 25.0)
        and (last_candle["RSI_3_4h"] < 10.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 70.0)
      ):
        return True, f"exit_{mode_name}_d_8_30"
      elif (
        (last_candle["RSI_3"] > 75.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_1h"] < 15.0)
        and (last_candle["RSI_3_4h"] < 15.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 25.0)
      ):
        return True, f"exit_{mode_name}_d_8_31"
      elif (
        (last_candle["RSI_3"] > 85.0)
        and (last_candle["RSI_3_1h"] < 15.0)
        and (last_candle["ROC_2_4h"] < -30.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 30.0)
      ):
        return True, f"exit_{mode_name}_d_8_32"
      elif (
        (last_candle["RSI_3"] > 85.0)
        and (last_candle["WILLR_14"] > -4.0)
        and (last_candle["ROC_2_1h"] < -10.0)
        and (last_candle["ROC_9_1h"] > 30.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_8_33"
      elif (
        (last_candle["RSI_3"] > 65.0)
        and (last_candle["RSI_3_15m"] < 30.0)
        and (last_candle["RSI_14_1h"] > 80.0)
        and (last_candle["ROC_9_1h"] > 40.0)
      ):
        return True, f"exit_{mode_name}_d_8_34"
      elif (
        (last_candle["RSI_3"] > 86.0)
        and (last_candle["WILLR_14"] > -7.0)
        and (last_candle["RSI_3_1d"] < 25.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 75.0)
      ):
        return True, f"exit_{mode_name}_d_8_35"
      elif (
        (last_candle["RSI_3"] > 80.0)
        and (last_candle["WILLR_14"] > -20.0)
        and (last_candle["ROC_9_4h"] < -25.0)
        and (last_candle["RSI_3_1d"] < 25.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_8_36"
      elif (
        (last_candle["RSI_3"] > 80.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_1h"] < 20.0)
        and (last_candle["RSI_3_1d"] < 25.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_8_37"
      elif (
        (last_candle["RSI_3"] > 80.0)
        and (last_candle["WILLR_14"] > -20.0)
        and (last_candle["RSI_3_4h"] < 10.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 20.0)
      ):
        return True, f"exit_{mode_name}_d_8_38"
      elif (
        (last_candle["RSI_3"] > 94.0)
        and (last_candle["WILLR_14"] > -6.0)
        and (last_candle["CMF_20_4h"] < -0.0)
        and (last_candle["RSI_3_4h"] < 10.0)
      ):
        return True, f"exit_{mode_name}_d_8_39"
      elif (
        (last_candle["RSI_3"] > 80.0)
        and (last_candle["WILLR_14"] > -20.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 30.0)
        and (
          isinstance(last_candle["STOCHRSIk_14_14_3_3_1d"], np.float64)
          and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 90.0)
        )
      ):
        return True, f"exit_{mode_name}_d_8_40"
      elif (
        (last_candle["RSI_3"] > 90.0)
        and (last_candle["WILLR_14"] > -15.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 25.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 50.0))
      ):
        return True, f"exit_{mode_name}_d_8_41"
      elif (
        (last_candle["RSI_3"] > 85.0)
        and (last_candle["WILLR_14"] > -30.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 30.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 40.0))
        and (
          isinstance(last_candle["STOCHRSIk_14_14_3_3_1d"], np.float64)
          and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 70.0)
        )
      ):
        return True, f"exit_{mode_name}_d_8_42"
      elif (
        (last_candle["RSI_3"] > 80.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_1h"] < 15.0)
        and (last_candle["RSI_3_4h"] < 40.0)
        and (
          isinstance(last_candle["STOCHRSIk_14_14_3_3_1d"], np.float64)
          and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 90.0)
        )
      ):
        return True, f"exit_{mode_name}_d_8_43"
      elif (
        (last_candle["RSI_3"] > 65.0)
        and (last_candle["WILLR_14"] > -10.0)
        and (last_candle["RSI_3_4h"] < 30.0)
        and (last_candle["RSI_3_1d"] < 25.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -30.0))
      ):
        return True, f"exit_{mode_name}_d_8_44"
      elif (last_candle["RSI_3"] > 92.0) and (last_candle["WILLR_14"] > -8.0) and (last_candle["RSI_3_1h"] < 10.0):
        return True, f"exit_{mode_name}_d_8_45"
      elif (
        (last_candle["RSI_3"] > 85.0)
        and (last_candle["RSI_3_1h"] < 15.0)
        and (last_candle["RSI_3_4h"] < 10.0)
        and (last_candle["ROC_2_1d"] < -20.0)
      ):
        return True, f"exit_{mode_name}_d_8_46"
      elif (
        (last_candle["RSI_3"] > 84.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 80.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 40.0)
        and (last_candle["change_pct_1d"] < -5.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -5.0))
      ):
        return True, f"exit_{mode_name}_d_8_47"
      elif (
        (last_candle["RSI_3"] > 60.0)
        and (last_candle["RSI_14"] < 46.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (last_candle["RSI_3_4h"] < 20.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_8_48"
      elif (
        (last_candle["RSI_3"] > 85.0)
        and (last_candle["WILLR_14"] > -6.0)
        and (last_candle["RSI_3_4h"] < 20.0)
        and (last_candle["change_pct_1d"] < -5.0)
        and (
          isinstance(last_candle["STOCHRSIk_14_14_3_3_1d"], np.float64)
          and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 50.0)
        )
      ):
        return True, f"exit_{mode_name}_d_8_49"
      elif (
        (last_candle["RSI_3"] > 80.0)
        and (last_candle["WILLR_14"] > -6.0)
        and (last_candle["RSI_3_1d"] < 10.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 90.0)
      ):
        return True, f"exit_{mode_name}_d_8_50"
      elif (
        (last_candle["RSI_3"] > 64.0)
        and (last_candle["RSI_14"] < 48.0)
        and (last_candle["RSI_3_4h"] < 20.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_8_51"
      elif (
        (last_candle["RSI_3"] > 78.0)
        and (last_candle["RSI_14"] > 58.0)
        and (last_candle["WILLR_14"] > -10.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 70.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -15.0))
      ):
        return True, f"exit_{mode_name}_d_8_52"
      elif (
        (last_candle["RSI_3"] > 70.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["WILLR_14"] > -25.0)
        and (last_candle["RSI_3_1h"] < 20.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
        and (
          isinstance(last_candle["STOCHRSIk_14_14_3_3_1d"], np.float64)
          and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 50.0)
        )
      ):
        return True, f"exit_{mode_name}_d_8_53"
      elif (
        (last_candle["RSI_3"] > 76.0)
        and (last_candle["RSI_14"] < 48.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
        and (last_candle["ROC_9_4h"] < -10.0)
        and (last_candle["change_pct_1d"] < -10.0)
      ):
        return True, f"exit_{mode_name}_d_8_54"
      elif (
        (last_candle["RSI_3"] > 92.0)
        and (last_candle["WILLR_14"] > -16.0)
        and (last_candle["ROC_9_4h"] < -5.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 10.0))
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_8_55"
      elif (
        (last_candle["RSI_3"] > 75.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (last_candle["RSI_3_4h"] < 25.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -30.0))
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 10.0)
      ):
        return True, f"exit_{mode_name}_d_8_56"
      elif (
        (last_candle["RSI_3"] > 50.0)
        and (last_candle["RSI_14"] < 38.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -30.0))
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 70.0)
      ):
        return True, f"exit_{mode_name}_d_8_57"
      elif (
        (last_candle["RSI_3"] > 85.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (last_candle["RSI_3_4h"] < 30.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -15.0))
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_8_58"
      elif (
        (last_candle["RSI_3"] > 85.0)
        and (last_candle["WILLR_14"] > -14.0)
        and (last_candle["RSI_3_4h"] < 25.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -15.0))
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 40.0)
      ):
        return True, f"exit_{mode_name}_d_8_59"
      elif (
        (last_candle["RSI_3"] > 70.0)
        and (last_candle["RSI_14"] < 42.0)
        and (last_candle["RSI_14_4h"] > 65.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_8_60"
      elif (
        (last_candle["RSI_3"] > 90.0)
        and (last_candle["WILLR_14"] > -25.0)
        and (last_candle["RSI_3_4h"] < 10.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 30.0)
      ):
        return True, f"exit_{mode_name}_d_8_61"
      elif (
        (last_candle["RSI_3"] > 84.0)
        and (last_candle["WILLR_14"] > -4.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (last_candle["RSI_3_4h"] < 20.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 20.0))
        and (last_candle["change_pct_1d"] < -5.0)
      ):
        return True, f"exit_{mode_name}_d_8_62"
      elif (
        (last_candle["RSI_3"] > 66.0)
        and (last_candle["RSI_3_1d"] < 25.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 80.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 30.0)
      ):
        return True, f"exit_{mode_name}_d_8_63"
      elif (
        (last_candle["RSI_3"] > 86.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (last_candle["RSI_3_4h"] < 30.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 30.0))
      ):
        return True, f"exit_{mode_name}_d_8_64"
      elif (
        (last_candle["RSI_3"] > 66.0)
        and (last_candle["RSI_14"] < 44.0)
        and (last_candle["RSI_3_1h"] < 20.0)
        and (last_candle["RSI_3_4h"] < 15.0)
      ):
        return True, f"exit_{mode_name}_d_8_65"
      elif (
        (last_candle["RSI_3"] > 80.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_1h"] < 20.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_8_66"
      elif (
        (last_candle["RSI_3"] > 50.0)
        and (last_candle["RSI_14"] < 44.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 80.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -25.0))
      ):
        return True, f"exit_{mode_name}_d_8_67"
      elif (
        (last_candle["RSI_3"] > 82.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_1h"] < 25.0)
        and (last_candle["ROC_2_4h"] < -30.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 25.0)
      ):
        return True, f"exit_{mode_name}_d_8_68"
      elif (
        (last_candle["RSI_3"] > 95.0)
        and (last_candle["ROC_9_4h"] > 20.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
        and (last_candle["change_pct_4h"] < -5.0)
      ):
        return True, f"exit_{mode_name}_d_8_69"
      elif (
        (last_candle["RSI_3"] > 64.0)
        and (last_candle["RSI_14"] < 42.0)
        and (last_candle["RSI_3_1h"] < 25.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 20.0)
      ):
        return True, f"exit_{mode_name}_d_8_70"
      elif (
        (last_candle["RSI_3"] > 62.0)
        and (last_candle["RSI_14"] < 46.0)
        and (last_candle["RSI_3_4h"] < 25.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 20.0)
      ):
        return True, f"exit_{mode_name}_d_8_71"
      elif (
        (last_candle["RSI_3"] > 76.0)
        and (last_candle["RSI_14"] < 44.0)
        and (last_candle["RSI_3_1h"] < 10.0)
        and (last_candle["AROONU_14_4h"] > 25.0)
      ):
        return True, f"exit_{mode_name}_d_8_72"
      elif (
        (last_candle["RSI_3"] > 76.0)
        and (last_candle["RSI_3_1h"] < 25.0)
        and (last_candle["RSI_3_4h"] < 15.0)
        and (last_candle["ROC_9_4h"] < -20.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -25.0))
      ):
        return True, f"exit_{mode_name}_d_8_73"
      elif (
        (last_candle["RSI_3"] > 97.0)
        and (last_candle["WILLR_14"] > -10.0)
        and (last_candle["RSI_3_4h"] < 25.0)
        and (last_candle["RSI_3_1d"] < 25.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_8_74"
      elif (
        (last_candle["RSI_3"] > 94.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (last_candle["RSI_3_4h"] < 20.0)
        and (
          isinstance(last_candle["STOCHRSIk_14_14_3_3_1d"], np.float64)
          and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 50.0)
        )
      ):
        return True, f"exit_{mode_name}_d_8_75"
      elif (
        (last_candle["RSI_3"] > 66.0)
        and (last_candle["RSI_14"] < 52.0)
        and (last_candle["ROC_9_1h"] > 80.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 80.0)
      ):
        return True, f"exit_{mode_name}_d_8_76"
      elif (
        (last_candle["RSI_3"] > 74.0)
        and (last_candle["RSI_14"] < 48.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 50.0))
      ):
        return True, f"exit_{mode_name}_d_8_77"
      elif (
        (last_candle["RSI_3"] > 84.0)
        and (last_candle["WILLR_14"] > -18.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (last_candle["RSI_3_4h"] < 20.0)
        and (last_candle["RSI_3_1d"] < 20.0)
      ):
        return True, f"exit_{mode_name}_d_8_78"
      elif (
        (last_candle["RSI_3"] > 90.0)
        and (last_candle["WILLR_14"] > -4.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (last_candle["RSI_3_4h"] < 10.0)
      ):
        return True, f"exit_{mode_name}_d_8_79"
      elif (
        (last_candle["RSI_3"] > 70.0)
        and (last_candle["RSI_14"] < 48.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 50.0))
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 25.0)
      ):
        return True, f"exit_{mode_name}_d_8_80"
      elif (
        (last_candle["RSI_3"] > 82.0)
        and (last_candle["WILLR_14"] > -12.0)
        and (last_candle["RSI_3_1h"] < 25.0)
        and (last_candle["RSI_3_4h"] < 25.0)
        and (isinstance(last_candle["RSI_14_1d"], np.float64) and (last_candle["RSI_14_1d"] > 50.0))
      ):
        return True, f"exit_{mode_name}_d_8_81"
      elif (
        (last_candle["RSI_3"] > 80.0)
        and (last_candle["WILLR_14"] > -12.0)
        and (last_candle["RSI_3_4h"] < 30.0)
        and (last_candle["RSI_3_1d"] < 15.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 40.0)
      ):
        return True, f"exit_{mode_name}_d_8_82"
      elif (
        (last_candle["RSI_3"] > 70.0)
        and (last_candle["RSI_14"] < 48.0)
        and (last_candle["RSI_3_1h"] < 40.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 40.0)
      ):
        return True, f"exit_{mode_name}_d_8_83"
      elif (
        (last_candle["RSI_3"] > 88.0)
        and (last_candle["WILLR_14"] > -4.0)
        and (last_candle["RSI_3_4h"] < 30.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 20.0)
      ):
        return True, f"exit_{mode_name}_d_8_84"
      elif (
        (last_candle["RSI_3"] > 86.0)
        and (last_candle["WILLR_14"] > -10.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (last_candle["RSI_3_4h"] < 40.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_8_85"
      elif (
        (last_candle["RSI_3"] > 92.0)
        and (last_candle["RSI_14_4h"] > 80.0)
        and (last_candle["ROC_2_1h"] < -5.0)
        and (last_candle["ROC_9_1h"] > 5.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_8_86"
      elif (
        (last_candle["RSI_3"] > 64.0)
        and (last_candle["RSI_14"] < 46.0)
        and (last_candle["RSI_3_1h"] < 45.0)
        and (last_candle["RSI_3_4h"] < 50.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_8_87"
      elif (
        (last_candle["RSI_3"] > 86.0)
        and (last_candle["WILLR_14"] > -22.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 40.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
        and (last_candle["change_pct_1h"] < -2.0)
      ):
        return True, f"exit_{mode_name}_d_8_88"
      elif (
        (last_candle["RSI_3"] > 76.0)
        and (last_candle["RSI_14"] < 42.0)
        and (last_candle["ROC_9_1h"] < -5.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 25.0))
      ):
        return True, f"exit_{mode_name}_d_8_89"
      elif (
        (last_candle["RSI_3"] > 90.0)
        and (last_candle["WILLR_14"] > -25.0)
        and (last_candle["RSI_3_1h"] < 50.0)
        and (last_candle["RSI_3_4h"] < 30.0)
        and (last_candle["AROONU_14_4h"] > 50.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 40.0))
      ):
        return True, f"exit_{mode_name}_d_8_90"
      elif (
        (last_candle["RSI_3"] > 70.0)
        and (last_candle["RSI_14"] < 48.0)
        and (last_candle["RSI_3_1h"] < 25.0)
        and (last_candle["RSI_3_4h"] < 25.0)
        and (last_candle["AROONU_14_4h"] > 50.0)
        and (
          isinstance(last_candle["STOCHRSIk_14_14_3_3_1d"], np.float64)
          and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 50.0)
        )
      ):
        return True, f"exit_{mode_name}_d_8_91"
      elif (
        (last_candle["RSI_3"] > 78.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_1h"] < 40.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 25.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -25.0))
      ):
        return True, f"exit_{mode_name}_d_8_92"
      elif (
        (last_candle["RSI_3"] > 70.0)
        and (last_candle["RSI_14"] < 52.0)
        and (last_candle["RSI_3_15m"] < 50.0)
        and (last_candle["AROONU_14_1h"] > 75.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 70.0)
        and (last_candle["AROONU_14_4h"] > 50.0)
        and (
          isinstance(last_candle["STOCHRSIk_14_14_3_3_1d"], np.float64)
          and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 90.0)
        )
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 30.0))
      ):
        return True, f"exit_{mode_name}_d_8_93"
      elif (
        (last_candle["RSI_3"] > 78.0)
        and (last_candle["RSI_14"] < 52.0)
        and (last_candle["RSI_3_1h"] < 25.0)
        and (last_candle["RSI_3_4h"] < 45.0)
        and (last_candle["AROONU_14_1h"] > 75.0)
        and (
          isinstance(last_candle["STOCHRSIk_14_14_3_3_1d"], np.float64)
          and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 90.0)
        )
      ):
        return True, f"exit_{mode_name}_d_8_94"
      elif (
        (last_candle["RSI_3"] > 82.0)
        and (last_candle["WILLR_14"] > -14.0)
        and (last_candle["RSI_3_1h"] < 45.0)
        and (last_candle["RSI_3_4h"] < 40.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 10.0)
        and (isinstance(last_candle["AROONU_14_1d"], np.float64) and (last_candle["AROONU_14_1d"] > 75.0))
      ):
        return True, f"exit_{mode_name}_d_8_95"
      elif (
        (last_candle["RSI_3"] > 60.0)
        and (last_candle["RSI_14"] < 48.0)
        and (last_candle["RSI_3_1h"] < 45.0)
        and (last_candle["RSI_3_1d"] < 45.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_8_96"
      elif (
        (last_candle["RSI_3"] > 82.0)
        and (last_candle["RSI_14"] < 48.0)
        and (last_candle["RSI_3_1h"] < 35.0)
        and (last_candle["AROONU_14_4h"] > 50.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 30.0)
      ):
        return True, f"exit_{mode_name}_d_8_97"
      elif (
        (last_candle["RSI_3"] > 88.0)
        and (last_candle["RSI_3_15m"] > 70.0)
        and (last_candle["RSI_3_1h"] < 60.0)
        and (last_candle["RSI_3_4h"] < 60.0)
        and (last_candle["RSI_3_1d"] > 80.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_8_98"
      elif (
        (last_candle["RSI_3"] > 58.0)
        and (last_candle["RSI_14"] < 54.0)
        and (last_candle["RSI_3_1h"] < 65.0)
        and (last_candle["RSI_3_4h"] < 60.0)
        and (last_candle["AROONU_14_4h"] > 50.0)
        and (last_candle["STOCHk_14_3_3_4h"] > 40.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 80.0))
      ):
        return True, f"exit_{mode_name}_d_8_99"
      elif (
        (last_candle["RSI_3"] > 96.0)
        and (last_candle["RSI_14"] > 74.0)
        and (last_candle["RSI_3_15m"] > 70.0)
        and (last_candle["RSI_3_4h"] < 80.0)
      ):
        return True, f"exit_{mode_name}_d_8_100"
      elif (
        (last_candle["RSI_3"] > 82.0)
        and (last_candle["WILLR_14"] > -18.0)
        and (last_candle["RSI_3_1h"] < 50.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 40.0)
        and (isinstance(last_candle["ROC_9_4h"], np.float64) and (last_candle["ROC_9_4h"] > 40.0))
      ):
        return True, f"exit_{mode_name}_d_8_101"
      elif (
        (last_candle["RSI_3"] > 66.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_1h"] < 60.0)
        and (last_candle["RSI_3_4h"] < 40.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 30.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 40.0))
      ):
        return True, f"exit_{mode_name}_d_8_102"
      elif (
        (last_candle["RSI_3"] > 76.0)
        and (last_candle["RSI_14"] < 58.0)
        and (last_candle["RSI_3_1h"] < 60.0)
        and (last_candle["RSI_14_4h"] > 70.0)
        and (isinstance(last_candle["ROC_9_4h"], np.float64) and (last_candle["ROC_9_4h"] > 80.0))
      ):
        return True, f"exit_{mode_name}_d_8_103"
      elif (
        (last_candle["RSI_3"] > 62.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_1h"] < 60.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 40.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 90.0)
        and (last_candle["ROC_9_4h"] > 40.0)
      ):
        return True, f"exit_{mode_name}_d_8_104"
      elif (
        (last_candle["RSI_3"] > 76.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_15m"] < 55.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 90.0)
        and (last_candle["ROC_9_4h"] > 25.0)
      ):
        return True, f"exit_{mode_name}_d_8_105"
      elif (
        (last_candle["RSI_3"] > 70.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_1h"] < 50.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
        and (last_candle["RSI_14_4h"] > 70.0)
        and (last_candle["ROC_9_4h"] > 40.0)
      ):
        return True, f"exit_{mode_name}_d_8_106"
      elif (
        (last_candle["RSI_3"] > 72.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_1h"] < 50.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 70.0)
        and (last_candle["RSI_14_4h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_8_107"
      elif (
        (last_candle["RSI_3"] > 54.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_1h"] < 60.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 80.0)
      ):
        return True, f"exit_{mode_name}_d_8_108"
      elif (
        (last_candle["RSI_3"] > 74.0)
        and (last_candle["WILLR_14"] > -10.0)
        and (last_candle["RSI_3_1h"] < 50.0)
        and (last_candle["RSI_3_4h"] < 20.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 50.0))
      ):
        return True, f"exit_{mode_name}_d_8_109"
      elif (
        (last_candle["RSI_3"] > 70.0)
        and (last_candle["RSI_3_4h"] < 65.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
        and (last_candle["ROC_9_4h"] > 25.0)
      ):
        return True, f"exit_{mode_name}_d_8_110"
      elif (
        (last_candle["RSI_3"] > 48.0)
        and (last_candle["RSI_14"] < 46.0)
        and (last_candle["RSI_3_1h"] < 50.0)
        and (last_candle["RSI_14_4h"] > 70.0)
        and (last_candle["AROONU_14_1h"] > 75.0)
        and (last_candle["AROONU_14_4h"] > 75.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 20.0))
      ):
        return True, f"exit_{mode_name}_d_8_111"
      elif (
        (last_candle["RSI_3"] > 78.0)
        and (last_candle["WILLR_14"] > -30.0)
        and (last_candle["RSI_14"] < 54.0)
        and (last_candle["RSI_3_1h"] < 35.0)
        and (last_candle["RSI_3_4h"] < 35.0)
        and (last_candle["RSI_3_1d"] < 60.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 30.0))
      ):
        return True, f"exit_{mode_name}_d_8_112"
      elif (
        (last_candle["RSI_3"] > 82.0)
        and (last_candle["WILLR_14"] > -2.0)
        and (last_candle["RSI_3_1d"] < 30.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
        and (isinstance(last_candle["ROC_9_4h"], np.float64) and (last_candle["ROC_9_4h"] > 10.0))
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -10.0))
      ):
        return True, f"exit_{mode_name}_d_8_113"
      elif (
        (last_candle["RSI_3"] > 82.0)
        and (last_candle["RSI_14"] < 52.0)
        and (last_candle["RSI_3_1h"] < 20.0)
        and (last_candle["RSI_3_4h"] < 30.0)
        and (last_candle["RSI_3_1d"] < 30.0)
      ):
        return True, f"exit_{mode_name}_d_8_114"
      elif (
        (last_candle["RSI_3"] > 76.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_15m"] < 30.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_8_115"
      elif (
        (last_candle["RSI_3"] > 88.0)
        and (last_candle["RSI_3_1h"] < 15.0)
        and (last_candle["RSI_3_4h"] < 40.0)
        and (last_candle["AROONU_14_4h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_8_116"
      elif (
        (last_candle["RSI_3"] > 84.0)
        and (last_candle["RSI_3_1h"] < 50.0)
        and (last_candle["AROONU_14_1h"] > 80.0)
        and (last_candle["AROONU_14_4h"] > 80.0)
      ):
        return True, f"exit_{mode_name}_d_8_117"
      elif (
        (last_candle["RSI_3"] > 88.0)
        and (last_candle["RSI_3_1h"] < 20.0)
        and (last_candle["RSI_3_4h"] < 60.0)
        and (last_candle["AROONU_14_4h"] > 40.0)
      ):
        return True, f"exit_{mode_name}_d_8_118"
      elif (
        (last_candle["RSI_3"] > 84.0)
        and (last_candle["WILLR_14"] > -20.0)
        and (last_candle["RSI_3_1h"] < 60.0)
        and (last_candle["RSI_3_4h"] < 60.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 40.0)
      ):
        return True, f"exit_{mode_name}_d_8_119"
      elif (
        (last_candle["RSI_3"] > 52.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_1h"] < 40.0)
        and (last_candle["AROONU_14_4h"] > 75.0)
      ):
        return True, f"exit_{mode_name}_d_8_120"
      elif (
        (last_candle["RSI_3"] > 58.0)
        and (last_candle["RSI_14"] < 48.0)
        and (last_candle["RSI_3_1h"] < 50.0)
        and (last_candle["RSI_14_4h"] > 85.0)
      ):
        return True, f"exit_{mode_name}_d_8_121"
      elif (
        (last_candle["RSI_3"] > 56.0)
        and (last_candle["RSI_14"] < 46.0)
        and (last_candle["RSI_3_4h"] < 30.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_8_122"
      elif (
        (last_candle["RSI_3"] > 86.0)
        and (last_candle["WILLR_14"] > -6.0)
        and (last_candle["RSI_3_1h"] < 10.0)
        and (last_candle["RSI_3_1d"] < 30.0)
      ):
        return True, f"exit_{mode_name}_d_8_123"
      elif (
        (last_candle["RSI_3"] > 86.0)
        and (last_candle["RSI_3_1h"] < 15.0)
        and (
          isinstance(last_candle["STOCHRSIk_14_14_3_3_1d"], np.float64)
          and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 80.0)
        )
      ):
        return True, f"exit_{mode_name}_d_8_124"
      elif (
        (last_candle["RSI_3"] > 74.0)
        and (last_candle["WILLR_14"] > -6.0)
        and (last_candle["RSI_3_1h"] < 10.0)
        and (last_candle["RSI_3_4h"] < 40.0)
        and (last_candle["RSI_3_1d"] < 40.0)
        and (last_candle["close"] < (last_candle["high_max_30_1d"] * 0.50))
      ):
        return True, f"exit_{mode_name}_d_8_125"
      elif (
        (last_candle["RSI_3"] > 88.0)
        and (last_candle["RSI_3_1h"] < 15.0)
        and (last_candle["RSI_3_4h"] < 40.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_8_126"
      elif (
        (last_candle["RSI_3"] > 88.0)
        and (last_candle["RSI_3_1h"] < 10.0)
        and (last_candle["RSI_3_4h"] < 30.0)
        and (last_candle["RSI_3_1d"] < 40.0)
      ):
        return True, f"exit_{mode_name}_d_8_127"
      elif (last_candle["RSI_3"] > 92.0) and (last_candle["RSI_3_4h"] < 30.0) and (last_candle["AROONU_14_4h"] > 85.0):
        return True, f"exit_{mode_name}_d_8_128"
      elif (
        (last_candle["RSI_3"] > 84.0)
        and (last_candle["RSI_3_4h"] < 25.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 80.0))
      ):
        return True, f"exit_{mode_name}_d_8_129"
      elif (
        (last_candle["RSI_3"] > 72.0)
        and (last_candle["RSI_14_1h"] > 65.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 80.0)
        and (last_candle["CCI_20_change_pct_1h"] < -0.0)
      ):
        return True, f"exit_{mode_name}_d_8_130"
      elif (
        (last_candle["RSI_14"] < 40.0)
        and (last_candle["RSI_3_1h"] < 20.0)
        and (last_candle["RSI_3_4h"] < 30.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_8_131"
      elif (
        (last_candle["RSI_3"] > 78.0)
        and (last_candle["RSI_3_1h"] < 35.0)
        and (last_candle["RSI_3_4h"] < 35.0)
        and (last_candle["AROONU_14_1h"] > 50.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 40.0)
      ):
        return True, f"exit_{mode_name}_d_8_132"
      elif (
        (last_candle["RSI_3"] > 78.0)
        and (last_candle["AROONU_14_15m"] > 75.0)
        and (last_candle["AROONU_14_1h"] > 75.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 25.0))
      ):
        return True, f"exit_{mode_name}_d_8_133"
    elif 0.1 > current_profit >= 0.09:
      if (
        (last_candle["WILLR_14"] > -1.0)
        and (last_candle["RSI_14"] > 78.0)
        and (
          isinstance(last_candle["EMA_200_1h"], np.float64) and (last_candle["EMA_12_1h"] < last_candle["EMA_200_1h"])
        )
        and (
          isinstance(last_candle["EMA_200_4h"], np.float64) and (last_candle["EMA_12_4h"] < last_candle["EMA_200_4h"])
        )
        and (last_candle["KST_10_15_20_30_10_10_10_15_1h"] < last_candle["KSTs_9_1h"])
        and (last_candle["KST_10_15_20_30_10_10_10_15_4h"] < last_candle["KSTs_9_4h"])
      ):
        return True, f"exit_{mode_name}_d_9_1"
      elif (
        (last_candle["WILLR_14"] > -1.0)
        and (last_candle["RSI_14"] > 68.0)
        and (last_candle["CMF_20_1h"] < -0.0)
        and (
          isinstance(last_candle["EMA_200_1h"], np.float64) and (last_candle["EMA_12_1h"] < last_candle["EMA_200_1h"])
        )
        and (
          isinstance(last_candle["EMA_200_4h"], np.float64) and (last_candle["EMA_12_4h"] < last_candle["EMA_200_4h"])
        )
      ):
        return True, f"exit_{mode_name}_d_9_2"
      elif (
        (last_candle["WILLR_14"] > -6.0)
        and (last_candle["STOCHRSIk_14_14_3_3"] > 98.0)
        and (last_candle["CMF_20_1h"] < -0.0)
        and (last_candle["CMF_20_4h"] < -0.0)
        and (
          (last_candle["STOCHRSIk_14_14_3_3_4h"] > 20.0) and (last_candle["STOCHRSIk_14_14_3_3_change_pct_4h"] < -10.0)
        )
      ):
        return True, f"exit_{mode_name}_d_9_3"
      elif (
        (last_candle["WILLR_14"] > -10.0)
        and (last_candle["RSI_14"] > 74.0)
        and (last_candle["STOCHRSIk_14_14_3_3"] > 95.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 70.0)
        and (
          isinstance(last_candle["EMA_200_1h"], np.float64) and (last_candle["EMA_12_1h"] < last_candle["EMA_200_1h"])
        )
        and (
          isinstance(last_candle["EMA_200_4h"], np.float64) and (last_candle["EMA_12_4h"] < last_candle["EMA_200_4h"])
        )
      ):
        return True, f"exit_{mode_name}_d_9_4"
      elif (
        (last_candle["WILLR_14"] > -2.0)
        and (last_candle["RSI_14"] > 72.0)
        and (last_candle["ROC_9_1h"] < -5.0)
        and (last_candle["ROC_9_4h"] < -5.0)
      ):
        return True, f"exit_{mode_name}_d_9_5"
      elif (
        (last_candle["RSI_3"] > 70.0)
        and (last_candle["STOCHRSIk_14_14_3_3"] > 70.0)
        and (last_candle["RSI_14"] < 40.0)
        and (last_candle["ROC_9_1h"] < -10.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 50.0))
      ):
        return True, f"exit_{mode_name}_d_9_6"
      elif (
        (last_candle["RSI_14"] < 50.0)
        and (last_candle["STOCHRSIk_14_14_3_3"] > 70.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -40.0))
      ):
        return True, f"exit_{mode_name}_d_9_7"
      elif (
        (last_candle["WILLR_14"] > -2.0)
        and (last_candle["STOCHRSIk_14_14_3_3"] > 95.0)
        and (last_candle["CMF_20_1h"] < -0.1)
        and (last_candle["CMF_20_4h"] < -0.1)
        and (last_candle["change_pct_1d"] < -5.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 15.0))
      ):
        return True, f"exit_{mode_name}_d_9_8"
      elif (
        (last_candle["WILLR_14"] > -4.0)
        and (last_candle["RSI_3"] > 95.0)
        and (last_candle["change_pct_4h"] < -5.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 30.0))
      ):
        return True, f"exit_{mode_name}_d_9_9"
      elif (
        (last_candle["WILLR_14"] > -6.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["ROC_9_1h"] < -10.0)
        and (last_candle["ROC_9_4h"] < -10.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 10.0))
      ):
        return True, f"exit_{mode_name}_d_9_10"
      elif (
        (last_candle["RSI_3"] > 92.0)
        and (last_candle["RSI_14"] < 45.0)
        and (last_candle["ROC_9_15m"] < -10.0)
        and (last_candle["ROC_9_1h"] < -10.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -20.0))
      ):
        return True, f"exit_{mode_name}_d_9_11"
      elif (
        (last_candle["RSI_3"] > 90.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_4h"] < 10.0)
        and (last_candle["ROC_9_1h"] < -20.0)
        and (last_candle["ROC_9_4h"] < -20.0)
      ):
        return True, f"exit_{mode_name}_d_9_12"
      elif (last_candle["RSI_3"] > 96.0) and (last_candle["RSI_3_4h"] < 5.0) and (last_candle["ROC_9_4h"] < -25.0):
        return True, f"exit_{mode_name}_d_9_13"
      elif (
        (last_candle["RSI_3"] > 90.0)
        and (last_candle["WILLR_14"] > -4.0)
        and (last_candle["RSI_3_4h"] < 5.0)
        and (last_candle["AROONU_14_4h"] > 25.0)
      ):
        return True, f"exit_{mode_name}_d_9_14"
      elif (last_candle["RSI_3"] > 94.0) and (last_candle["RSI_14"] > 66.0) and (last_candle["ROC_9_4h"] < -30.0):
        return True, f"exit_{mode_name}_d_9_15"
      elif (
        (last_candle["RSI_3"] > 90.0)
        and (last_candle["AROONU_14_4h"] > 25.0)
        and (last_candle["ROC_9_4h"] < -25.0)
        and (last_candle["AROONU_14_1d"] > 50.0)
        and (last_candle["change_pct_1d"] < -15.0)
      ):
        return True, f"exit_{mode_name}_d_9_16"
      elif (
        (last_candle["RSI_3"] > 96.0)
        and (last_candle["WILLR_14"] > -15.0)
        and (last_candle["RSI_3_1h"] < 10.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 90.0)
        and (last_candle["ROC_9_4h"] > 30.0)
      ):
        return True, f"exit_{mode_name}_d_9_17"
      elif (
        (last_candle["RSI_3"] > 92.0)
        and (last_candle["RSI_14"] > 74.0)
        and (last_candle["RSI_3_4h"] < 20.0)
        and (last_candle["ROC_2_1d"] < -50.0)
      ):
        return True, f"exit_{mode_name}_d_9_18"
      elif (
        (last_candle["RSI_3"] > 92.0)
        and (last_candle["RSI_14"] > 72.0)
        and (last_candle["RSI_3_4h"] < 10.0)
        and (
          isinstance(last_candle["STOCHRSIk_14_14_3_3_1d"], np.float64)
          and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 70.0)
        )
      ):
        return True, f"exit_{mode_name}_d_9_19"
      elif (
        (last_candle["RSI_3"] > 50.0)
        and (last_candle["RSI_14"] < 40.0)
        and (last_candle["RSI_3_1h"] < 10.0)
        and (last_candle["AROONU_14_1h"] > 25.0)
      ):
        return True, f"exit_{mode_name}_d_9_20"
      elif (
        (last_candle["RSI_3"] > 90.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_1h"] < 20.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 90.0)
      ):
        return True, f"exit_{mode_name}_d_9_21"
      elif (
        (last_candle["RSI_3"] > 98.0)
        and (last_candle["WILLR_14"] > -2.0)
        and (last_candle["change_pct_4h"] < -5.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -30.0))
      ):
        return True, f"exit_{mode_name}_d_9_22"
      elif (
        (last_candle["RSI_3"] > 92.0)
        and (last_candle["WILLR_14"] > -10.0)
        and (last_candle["RSI_3_1h"] < 15.0)
        and (last_candle["RSI_3_1d"] < 5.0)
      ):
        return True, f"exit_{mode_name}_d_9_23"
      elif (
        (last_candle["RSI_3"] > 92.0)
        and (last_candle["RSI_14"] > 72.0)
        and (last_candle["WILLR_14"] > -15.0)
        and (last_candle["RSI_3_4h"] < 30.0)
        and (last_candle["AROONU_14_4h"] > 75.0)
      ):
        return True, f"exit_{mode_name}_d_9_24"
      elif (
        (last_candle["RSI_3"] > 90.0)
        and (last_candle["WILLR_14"] > -4.0)
        and (last_candle["RSI_3_4h"] < 10.0)
        and (last_candle["ROC_9_4h"] < -15.0)
        and (
          isinstance(last_candle["STOCHRSIk_14_14_3_3_1d"], np.float64)
          and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 50.0)
        )
      ):
        return True, f"exit_{mode_name}_d_9_25"
      elif (
        (last_candle["RSI_3"] > 85.0)
        and (last_candle["WILLR_14"] > -4.0)
        and (last_candle["RSI_3_4h"] < 15.0)
        and (last_candle["ROC_9_4h"] < -20.0)
      ):
        return True, f"exit_{mode_name}_d_9_26"
      elif (
        (last_candle["RSI_3"] > 85.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_1h"] < 20.0)
        and (last_candle["RSI_3_4h"] < 20.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 20.0)
      ):
        return True, f"exit_{mode_name}_d_9_27"
      elif (
        (last_candle["RSI_3"] > 80.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_15m"] < 10.0)
        and (last_candle["ROC_9_4h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_9_28"
      elif (
        (last_candle["RSI_3"] > 95.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_1h"] < 20.0)
        and (last_candle["RSI_3_4h"] < 20.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 30.0)
      ):
        return True, f"exit_{mode_name}_d_9_29"
      elif (
        (last_candle["RSI_3"] > 90.0)
        and (last_candle["RSI_3_1h"] < 25.0)
        and (last_candle["RSI_3_4h"] < 10.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 70.0)
      ):
        return True, f"exit_{mode_name}_d_9_30"
      elif (
        (last_candle["RSI_3"] > 80.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_1h"] < 15.0)
        and (last_candle["RSI_3_4h"] < 15.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 25.0)
      ):
        return True, f"exit_{mode_name}_d_9_31"
      elif (
        (last_candle["RSI_3"] > 90.0)
        and (last_candle["RSI_3_1h"] < 15.0)
        and (last_candle["ROC_2_4h"] < -30.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 30.0)
      ):
        return True, f"exit_{mode_name}_d_9_32"
      elif (
        (last_candle["RSI_3"] > 90.0)
        and (last_candle["WILLR_14"] > -2.0)
        and (last_candle["ROC_2_1h"] < -10.0)
        and (last_candle["ROC_9_1h"] > 30.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_9_33"
      elif (
        (last_candle["RSI_3"] > 65.0)
        and (last_candle["RSI_3_15m"] < 30.0)
        and (last_candle["RSI_14_1h"] > 80.0)
        and (last_candle["ROC_9_1h"] > 40.0)
      ):
        return True, f"exit_{mode_name}_d_9_34"
      elif (
        (last_candle["RSI_3"] > 88.0)
        and (last_candle["WILLR_14"] > -6.0)
        and (last_candle["RSI_3_1d"] < 25.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 75.0)
      ):
        return True, f"exit_{mode_name}_d_9_35"
      elif (
        (last_candle["RSI_3"] > 85.0)
        and (last_candle["WILLR_14"] > -15.0)
        and (last_candle["ROC_9_4h"] < -25.0)
        and (last_candle["RSI_3_1d"] < 25.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_9_36"
      elif (
        (last_candle["RSI_3"] > 82.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_1h"] < 20.0)
        and (last_candle["RSI_3_1d"] < 25.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_9_37"
      elif (
        (last_candle["RSI_3"] > 85.0)
        and (last_candle["WILLR_14"] > -15.0)
        and (last_candle["RSI_3_4h"] < 10.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 20.0)
      ):
        return True, f"exit_{mode_name}_d_9_38"
      elif (
        (last_candle["RSI_3"] > 95.0)
        and (last_candle["WILLR_14"] > -5.0)
        and (last_candle["CMF_20_4h"] < -0.0)
        and (last_candle["RSI_3_4h"] < 10.0)
      ):
        return True, f"exit_{mode_name}_d_9_39"
      elif (
        (last_candle["RSI_3"] > 85.0)
        and (last_candle["WILLR_14"] > -15.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 30.0)
        and (
          isinstance(last_candle["STOCHRSIk_14_14_3_3_1d"], np.float64)
          and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 90.0)
        )
      ):
        return True, f"exit_{mode_name}_d_9_40"
      elif (
        (last_candle["RSI_3"] > 95.0)
        and (last_candle["WILLR_14"] > -10.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 25.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 50.0))
      ):
        return True, f"exit_{mode_name}_d_9_41"
      elif (
        (last_candle["RSI_3"] > 90.0)
        and (last_candle["WILLR_14"] > -25.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 30.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 40.0))
        and (
          isinstance(last_candle["STOCHRSIk_14_14_3_3_1d"], np.float64)
          and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 70.0)
        )
      ):
        return True, f"exit_{mode_name}_d_9_42"
      elif (
        (last_candle["RSI_3"] > 80.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_1h"] < 15.0)
        and (last_candle["RSI_3_4h"] < 40.0)
        and (
          isinstance(last_candle["STOCHRSIk_14_14_3_3_1d"], np.float64)
          and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 90.0)
        )
      ):
        return True, f"exit_{mode_name}_d_9_43"
      elif (
        (last_candle["RSI_3"] > 70.0)
        and (last_candle["WILLR_14"] > -5.0)
        and (last_candle["RSI_3_4h"] < 30.0)
        and (last_candle["RSI_3_1d"] < 25.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -30.0))
      ):
        return True, f"exit_{mode_name}_d_9_44"
      elif (last_candle["RSI_3"] > 94.0) and (last_candle["WILLR_14"] > -6.0) and (last_candle["RSI_3_1h"] < 10.0):
        return True, f"exit_{mode_name}_d_9_45"
      elif (
        (last_candle["RSI_3"] > 90.0)
        and (last_candle["RSI_3_1h"] < 15.0)
        and (last_candle["RSI_3_4h"] < 10.0)
        and (last_candle["ROC_2_1d"] < -20.0)
      ):
        return True, f"exit_{mode_name}_d_9_46"
      elif (
        (last_candle["RSI_3"] > 86.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 80.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 40.0)
        and (last_candle["change_pct_1d"] < -5.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -5.0))
      ):
        return True, f"exit_{mode_name}_d_9_47"
      elif (
        (last_candle["RSI_3"] > 65.0)
        and (last_candle["RSI_14"] < 44.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (last_candle["RSI_3_4h"] < 20.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_9_48"
      elif (
        (last_candle["RSI_3"] > 90.0)
        and (last_candle["WILLR_14"] > -4.0)
        and (last_candle["RSI_3_4h"] < 20.0)
        and (last_candle["change_pct_1d"] < -5.0)
        and (
          isinstance(last_candle["STOCHRSIk_14_14_3_3_1d"], np.float64)
          and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 50.0)
        )
      ):
        return True, f"exit_{mode_name}_d_9_49"
      elif (
        (last_candle["RSI_3"] > 80.0)
        and (last_candle["WILLR_14"] > -4.0)
        and (last_candle["RSI_3_1d"] < 10.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 90.0)
      ):
        return True, f"exit_{mode_name}_d_9_50"
      elif (
        (last_candle["RSI_3"] > 66.0)
        and (last_candle["RSI_14"] < 46.0)
        and (last_candle["RSI_3_4h"] < 20.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_9_51"
      elif (
        (last_candle["RSI_3"] > 80.0)
        and (last_candle["RSI_14"] > 60.0)
        and (last_candle["WILLR_14"] > -10.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 70.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -15.0))
      ):
        return True, f"exit_{mode_name}_d_9_52"
      elif (
        (last_candle["RSI_3"] > 70.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["WILLR_14"] > -25.0)
        and (last_candle["RSI_3_1h"] < 20.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
        and (
          isinstance(last_candle["STOCHRSIk_14_14_3_3_1d"], np.float64)
          and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 50.0)
        )
      ):
        return True, f"exit_{mode_name}_d_9_53"
      elif (
        (last_candle["RSI_3"] > 78.0)
        and (last_candle["RSI_14"] < 46.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
        and (last_candle["ROC_9_4h"] < -10.0)
        and (last_candle["change_pct_1d"] < -10.0)
      ):
        return True, f"exit_{mode_name}_d_9_54"
      elif (
        (last_candle["RSI_3"] > 94.0)
        and (last_candle["WILLR_14"] > -14.0)
        and (last_candle["ROC_9_4h"] < -5.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 10.0))
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_9_55"
      elif (
        (last_candle["RSI_3"] > 80.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (last_candle["RSI_3_4h"] < 25.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -30.0))
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 10.0)
      ):
        return True, f"exit_{mode_name}_d_9_56"
      elif (
        (last_candle["RSI_3"] > 50.0)
        and (last_candle["RSI_14"] < 36.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -30.0))
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 70.0)
      ):
        return True, f"exit_{mode_name}_d_9_57"
      elif (
        (last_candle["RSI_3"] > 90.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (last_candle["RSI_3_4h"] < 30.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -15.0))
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_9_58"
      elif (
        (last_candle["RSI_3"] > 85.0)
        and (last_candle["WILLR_14"] > -12.0)
        and (last_candle["RSI_3_4h"] < 25.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -15.0))
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 40.0)
      ):
        return True, f"exit_{mode_name}_d_9_59"
      elif (
        (last_candle["RSI_3"] > 75.0)
        and (last_candle["RSI_14"] < 40.0)
        and (last_candle["RSI_14_4h"] > 65.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_9_60"
      elif (
        (last_candle["RSI_3"] > 92.0)
        and (last_candle["WILLR_14"] > -20.0)
        and (last_candle["RSI_3_4h"] < 10.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 30.0)
      ):
        return True, f"exit_{mode_name}_d_9_61"
      elif (
        (last_candle["RSI_3"] > 86.0)
        and (last_candle["WILLR_14"] > -2.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (last_candle["RSI_3_4h"] < 20.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 20.0))
        and (last_candle["change_pct_1d"] < -5.0)
      ):
        return True, f"exit_{mode_name}_d_9_62"
      elif (
        (last_candle["RSI_3"] > 68.0)
        and (last_candle["RSI_3_1d"] < 25.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 80.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 30.0)
      ):
        return True, f"exit_{mode_name}_d_9_63"
      elif (
        (last_candle["RSI_3"] > 88.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (last_candle["RSI_3_4h"] < 30.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 30.0))
      ):
        return True, f"exit_{mode_name}_d_9_64"
      elif (
        (last_candle["RSI_3"] > 68.0)
        and (last_candle["RSI_14"] < 42.0)
        and (last_candle["RSI_3_1h"] < 20.0)
        and (last_candle["RSI_3_4h"] < 15.0)
      ):
        return True, f"exit_{mode_name}_d_9_65"
      elif (
        (last_candle["RSI_3"] > 82.0)
        and (last_candle["RSI_14"] < 48.0)
        and (last_candle["RSI_3_1h"] < 20.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_9_66"
      elif (
        (last_candle["RSI_3"] > 50.0)
        and (last_candle["RSI_14"] < 42.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 80.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -25.0))
      ):
        return True, f"exit_{mode_name}_d_9_67"
      elif (
        (last_candle["RSI_3"] > 84.0)
        and (last_candle["RSI_14"] < 48.0)
        and (last_candle["RSI_3_1h"] < 25.0)
        and (last_candle["ROC_2_4h"] < -30.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 25.0)
      ):
        return True, f"exit_{mode_name}_d_9_68"
      elif (
        (last_candle["RSI_3"] > 96.0)
        and (last_candle["ROC_9_4h"] > 20.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
        and (last_candle["change_pct_4h"] < -5.0)
      ):
        return True, f"exit_{mode_name}_d_9_69"
      elif (
        (last_candle["RSI_3"] > 66.0)
        and (last_candle["RSI_14"] < 40.0)
        and (last_candle["RSI_3_1h"] < 25.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 20.0)
      ):
        return True, f"exit_{mode_name}_d_9_70"
      elif (
        (last_candle["RSI_3"] > 64.0)
        and (last_candle["RSI_14"] < 44.0)
        and (last_candle["RSI_3_4h"] < 25.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 20.0)
      ):
        return True, f"exit_{mode_name}_d_9_71"
      elif (
        (last_candle["RSI_3"] > 78.0)
        and (last_candle["RSI_14"] < 42.0)
        and (last_candle["RSI_3_1h"] < 10.0)
        and (last_candle["AROONU_14_4h"] > 25.0)
      ):
        return True, f"exit_{mode_name}_d_9_72"
      elif (
        (last_candle["RSI_3"] > 78.0)
        and (last_candle["RSI_3_1h"] < 25.0)
        and (last_candle["RSI_3_4h"] < 15.0)
        and (last_candle["ROC_9_4h"] < -20.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -25.0))
      ):
        return True, f"exit_{mode_name}_d_9_73"
      elif (
        (last_candle["RSI_3"] > 98.0)
        and (last_candle["WILLR_14"] > -10.0)
        and (last_candle["RSI_3_4h"] < 25.0)
        and (last_candle["RSI_3_1d"] < 25.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_9_74"
      elif (
        (last_candle["RSI_3"] > 96.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (last_candle["RSI_3_4h"] < 20.0)
        and (
          isinstance(last_candle["STOCHRSIk_14_14_3_3_1d"], np.float64)
          and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 50.0)
        )
      ):
        return True, f"exit_{mode_name}_d_9_75"
      elif (
        (last_candle["RSI_3"] > 68.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["ROC_9_1h"] > 80.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 80.0)
      ):
        return True, f"exit_{mode_name}_d_9_76"
      elif (
        (last_candle["RSI_3"] > 76.0)
        and (last_candle["RSI_14"] < 46.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 50.0))
      ):
        return True, f"exit_{mode_name}_d_9_77"
      elif (
        (last_candle["RSI_3"] > 86.0)
        and (last_candle["WILLR_14"] > -16.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (last_candle["RSI_3_4h"] < 20.0)
        and (last_candle["RSI_3_1d"] < 20.0)
      ):
        return True, f"exit_{mode_name}_d_9_78"
      elif (
        (last_candle["RSI_3"] > 92.0)
        and (last_candle["WILLR_14"] > -2.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (last_candle["RSI_3_4h"] < 10.0)
      ):
        return True, f"exit_{mode_name}_d_9_79"
      elif (
        (last_candle["RSI_3"] > 72.0)
        and (last_candle["RSI_14"] < 46.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 50.0))
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 25.0)
      ):
        return True, f"exit_{mode_name}_d_9_80"
      elif (
        (last_candle["RSI_3"] > 84.0)
        and (last_candle["WILLR_14"] > -10.0)
        and (last_candle["RSI_3_1h"] < 25.0)
        and (last_candle["RSI_3_4h"] < 25.0)
        and (isinstance(last_candle["RSI_14_1d"], np.float64) and (last_candle["RSI_14_1d"] > 50.0))
      ):
        return True, f"exit_{mode_name}_d_9_81"
      elif (
        (last_candle["RSI_3"] > 82.0)
        and (last_candle["WILLR_14"] > -10.0)
        and (last_candle["RSI_3_4h"] < 30.0)
        and (last_candle["RSI_3_1d"] < 15.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 40.0)
      ):
        return True, f"exit_{mode_name}_d_9_82"
      elif (
        (last_candle["RSI_3"] > 72.0)
        and (last_candle["RSI_14"] < 46.0)
        and (last_candle["RSI_3_1h"] < 40.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 40.0)
      ):
        return True, f"exit_{mode_name}_d_9_83"
      elif (
        (last_candle["RSI_3"] > 90.0)
        and (last_candle["WILLR_14"] > -2.0)
        and (last_candle["RSI_3_4h"] < 30.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 20.0)
      ):
        return True, f"exit_{mode_name}_d_9_84"
      elif (
        (last_candle["RSI_3"] > 88.0)
        and (last_candle["WILLR_14"] > -8.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (last_candle["RSI_3_4h"] < 40.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_9_85"
      elif (
        (last_candle["RSI_3"] > 94.0)
        and (last_candle["RSI_14_4h"] > 80.0)
        and (last_candle["ROC_2_1h"] < -5.0)
        and (last_candle["ROC_9_1h"] > 5.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_9_86"
      elif (
        (last_candle["RSI_3"] > 66.0)
        and (last_candle["RSI_14"] < 44.0)
        and (last_candle["RSI_3_1h"] < 45.0)
        and (last_candle["RSI_3_4h"] < 50.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_9_87"
      elif (
        (last_candle["RSI_3"] > 88.0)
        and (last_candle["WILLR_14"] > -20.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 40.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
        and (last_candle["change_pct_1h"] < -2.0)
      ):
        return True, f"exit_{mode_name}_d_9_88"
      elif (
        (last_candle["RSI_3"] > 78.0)
        and (last_candle["RSI_14"] < 40.0)
        and (last_candle["ROC_9_1h"] < -5.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 25.0))
      ):
        return True, f"exit_{mode_name}_d_9_89"
      elif (
        (last_candle["RSI_3"] > 92.0)
        and (last_candle["WILLR_14"] > -25.0)
        and (last_candle["RSI_3_1h"] < 50.0)
        and (last_candle["RSI_3_4h"] < 30.0)
        and (last_candle["AROONU_14_4h"] > 50.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 40.0))
      ):
        return True, f"exit_{mode_name}_d_9_90"
      elif (
        (last_candle["RSI_3"] > 72.0)
        and (last_candle["RSI_14"] < 46.0)
        and (last_candle["RSI_3_1h"] < 25.0)
        and (last_candle["RSI_3_4h"] < 25.0)
        and (last_candle["AROONU_14_4h"] > 50.0)
        and (
          isinstance(last_candle["STOCHRSIk_14_14_3_3_1d"], np.float64)
          and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 50.0)
        )
      ):
        return True, f"exit_{mode_name}_d_9_91"
      elif (
        (last_candle["RSI_3"] > 80.0)
        and (last_candle["RSI_14"] < 48.0)
        and (last_candle["RSI_3_1h"] < 40.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 25.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -25.0))
      ):
        return True, f"exit_{mode_name}_d_9_92"
      elif (
        (last_candle["RSI_3"] > 72.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_15m"] < 50.0)
        and (last_candle["AROONU_14_1h"] > 75.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 70.0)
        and (last_candle["AROONU_14_4h"] > 50.0)
        and (
          isinstance(last_candle["STOCHRSIk_14_14_3_3_1d"], np.float64)
          and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 90.0)
        )
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 30.0))
      ):
        return True, f"exit_{mode_name}_d_9_93"
      elif (
        (last_candle["RSI_3"] > 80.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_1h"] < 25.0)
        and (last_candle["RSI_3_4h"] < 45.0)
        and (last_candle["AROONU_14_1h"] > 75.0)
        and (
          isinstance(last_candle["STOCHRSIk_14_14_3_3_1d"], np.float64)
          and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 90.0)
        )
      ):
        return True, f"exit_{mode_name}_d_9_94"
      elif (
        (last_candle["RSI_3"] > 84.0)
        and (last_candle["WILLR_14"] > -12.0)
        and (last_candle["RSI_3_1h"] < 45.0)
        and (last_candle["RSI_3_4h"] < 40.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 10.0)
        and (isinstance(last_candle["AROONU_14_1d"], np.float64) and (last_candle["AROONU_14_1d"] > 75.0))
      ):
        return True, f"exit_{mode_name}_d_9_95"
      elif (
        (last_candle["RSI_3"] > 62.0)
        and (last_candle["RSI_14"] < 46.0)
        and (last_candle["RSI_3_1h"] < 45.0)
        and (last_candle["RSI_3_1d"] < 45.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_9_96"
      elif (
        (last_candle["RSI_3"] > 84.0)
        and (last_candle["RSI_14"] < 46.0)
        and (last_candle["RSI_3_1h"] < 35.0)
        and (last_candle["AROONU_14_4h"] > 50.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 30.0)
      ):
        return True, f"exit_{mode_name}_d_9_97"
      elif (
        (last_candle["RSI_3"] > 90.0)
        and (last_candle["RSI_3_15m"] > 72.0)
        and (last_candle["RSI_3_1h"] < 60.0)
        and (last_candle["RSI_3_4h"] < 60.0)
        and (last_candle["RSI_3_1d"] > 80.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_9_98"
      elif (
        (last_candle["RSI_3"] > 60.0)
        and (last_candle["RSI_14"] < 52.0)
        and (last_candle["RSI_3_1h"] < 65.0)
        and (last_candle["RSI_3_4h"] < 60.0)
        and (last_candle["AROONU_14_4h"] > 50.0)
        and (last_candle["STOCHk_14_3_3_4h"] > 40.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 80.0))
      ):
        return True, f"exit_{mode_name}_d_9_99"
      elif (
        (last_candle["RSI_3"] > 98.0)
        and (last_candle["RSI_14"] > 76.0)
        and (last_candle["RSI_3_15m"] > 70.0)
        and (last_candle["RSI_3_4h"] < 80.0)
      ):
        return True, f"exit_{mode_name}_d_9_100"
      elif (
        (last_candle["RSI_3"] > 84.0)
        and (last_candle["WILLR_14"] > -16.0)
        and (last_candle["RSI_3_1h"] < 50.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 40.0)
        and (isinstance(last_candle["ROC_9_4h"], np.float64) and (last_candle["ROC_9_4h"] > 40.0))
      ):
        return True, f"exit_{mode_name}_d_9_101"
      elif (
        (last_candle["RSI_3"] > 68.0)
        and (last_candle["RSI_14"] < 48.0)
        and (last_candle["RSI_3_1h"] < 60.0)
        and (last_candle["RSI_3_4h"] < 40.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 30.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 40.0))
      ):
        return True, f"exit_{mode_name}_d_9_102"
      elif (
        (last_candle["RSI_3"] > 78.0)
        and (last_candle["RSI_14"] < 56.0)
        and (last_candle["RSI_3_1h"] < 60.0)
        and (last_candle["RSI_14_4h"] > 70.0)
        and (isinstance(last_candle["ROC_9_4h"], np.float64) and (last_candle["ROC_9_4h"] > 80.0))
      ):
        return True, f"exit_{mode_name}_d_9_103"
      elif (
        (last_candle["RSI_3"] > 64.0)
        and (last_candle["RSI_14"] < 48.0)
        and (last_candle["RSI_3_1h"] < 60.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 40.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 90.0)
        and (last_candle["ROC_9_4h"] > 40.0)
      ):
        return True, f"exit_{mode_name}_d_9_104"
      elif (
        (last_candle["RSI_3"] > 78.0)
        and (last_candle["RSI_14"] < 48.0)
        and (last_candle["RSI_3_15m"] < 55.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 90.0)
        and (last_candle["ROC_9_4h"] > 25.0)
      ):
        return True, f"exit_{mode_name}_d_9_105"
      elif (
        (last_candle["RSI_3"] > 72.0)
        and (last_candle["RSI_14"] < 48.0)
        and (last_candle["RSI_3_1h"] < 50.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
        and (last_candle["RSI_14_4h"] > 70.0)
        and (last_candle["ROC_9_4h"] > 40.0)
      ):
        return True, f"exit_{mode_name}_d_9_106"
      elif (
        (last_candle["RSI_3"] > 74.0)
        and (last_candle["RSI_14"] < 48.0)
        and (last_candle["RSI_3_1h"] < 50.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 70.0)
        and (last_candle["RSI_14_4h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_9_107"
      elif (
        (last_candle["RSI_3"] > 56.0)
        and (last_candle["RSI_14"] < 48.0)
        and (last_candle["RSI_3_1h"] < 60.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 80.0)
      ):
        return True, f"exit_{mode_name}_d_9_108"
      elif (
        (last_candle["RSI_3"] > 76.0)
        and (last_candle["WILLR_14"] > -8.0)
        and (last_candle["RSI_3_1h"] < 50.0)
        and (last_candle["RSI_3_4h"] < 20.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 50.0))
      ):
        return True, f"exit_{mode_name}_d_9_109"
      elif (
        (last_candle["RSI_3"] > 72.0)
        and (last_candle["RSI_3_4h"] < 65.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
        and (last_candle["ROC_9_4h"] > 25.0)
      ):
        return True, f"exit_{mode_name}_d_9_110"
      elif (
        (last_candle["RSI_3"] > 50.0)
        and (last_candle["RSI_14"] < 44.0)
        and (last_candle["RSI_3_1h"] < 50.0)
        and (last_candle["RSI_14_4h"] > 70.0)
        and (last_candle["AROONU_14_1h"] > 75.0)
        and (last_candle["AROONU_14_4h"] > 75.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 20.0))
      ):
        return True, f"exit_{mode_name}_d_9_111"
      elif (
        (last_candle["RSI_3"] > 80.0)
        and (last_candle["WILLR_14"] > -25.0)
        and (last_candle["RSI_14"] < 52.0)
        and (last_candle["RSI_3_1h"] < 35.0)
        and (last_candle["RSI_3_4h"] < 35.0)
        and (last_candle["RSI_3_1d"] < 60.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 30.0))
      ):
        return True, f"exit_{mode_name}_d_9_112"
      elif (
        (last_candle["RSI_3"] > 84.0)
        and (last_candle["WILLR_14"] > -1.0)
        and (last_candle["RSI_3_1d"] < 30.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
        and (isinstance(last_candle["ROC_9_4h"], np.float64) and (last_candle["ROC_9_4h"] > 10.0))
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -10.0))
      ):
        return True, f"exit_{mode_name}_d_9_113"
      elif (
        (last_candle["RSI_3"] > 84.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_1h"] < 20.0)
        and (last_candle["RSI_3_4h"] < 30.0)
        and (last_candle["RSI_3_1d"] < 30.0)
      ):
        return True, f"exit_{mode_name}_d_9_114"
      elif (
        (last_candle["RSI_3"] > 78.0)
        and (last_candle["RSI_14"] < 48.0)
        and (last_candle["RSI_3_15m"] < 30.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_9_115"
      elif (
        (last_candle["RSI_3"] > 90.0)
        and (last_candle["RSI_3_1h"] < 15.0)
        and (last_candle["RSI_3_4h"] < 40.0)
        and (last_candle["AROONU_14_4h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_9_116"
      elif (
        (last_candle["RSI_3"] > 86.0)
        and (last_candle["RSI_3_1h"] < 50.0)
        and (last_candle["AROONU_14_1h"] > 80.0)
        and (last_candle["AROONU_14_4h"] > 80.0)
      ):
        return True, f"exit_{mode_name}_d_9_117"
      elif (
        (last_candle["RSI_3"] > 90.0)
        and (last_candle["RSI_3_1h"] < 20.0)
        and (last_candle["RSI_3_4h"] < 60.0)
        and (last_candle["AROONU_14_4h"] > 40.0)
      ):
        return True, f"exit_{mode_name}_d_9_118"
      elif (
        (last_candle["RSI_3"] > 86.0)
        and (last_candle["WILLR_14"] > -20.0)
        and (last_candle["RSI_3_1h"] < 60.0)
        and (last_candle["RSI_3_4h"] < 60.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 40.0)
      ):
        return True, f"exit_{mode_name}_d_9_119"
      elif (
        (last_candle["RSI_3"] > 54.0)
        and (last_candle["RSI_14"] < 48.0)
        and (last_candle["RSI_3_1h"] < 40.0)
        and (last_candle["AROONU_14_4h"] > 75.0)
      ):
        return True, f"exit_{mode_name}_d_9_120"
      elif (
        (last_candle["RSI_3"] > 60.0)
        and (last_candle["RSI_14"] < 46.0)
        and (last_candle["RSI_3_1h"] < 50.0)
        and (last_candle["RSI_14_4h"] > 85.0)
      ):
        return True, f"exit_{mode_name}_d_9_121"
      elif (
        (last_candle["RSI_3"] > 58.0)
        and (last_candle["RSI_14"] < 44.0)
        and (last_candle["RSI_3_4h"] < 30.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_9_122"
      elif (
        (last_candle["RSI_3"] > 88.0)
        and (last_candle["WILLR_14"] > -4.0)
        and (last_candle["RSI_3_1h"] < 10.0)
        and (last_candle["RSI_3_1d"] < 30.0)
      ):
        return True, f"exit_{mode_name}_d_9_123"
      elif (
        (last_candle["RSI_3"] > 88.0)
        and (last_candle["RSI_3_1h"] < 15.0)
        and (
          isinstance(last_candle["STOCHRSIk_14_14_3_3_1d"], np.float64)
          and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 80.0)
        )
      ):
        return True, f"exit_{mode_name}_d_9_124"
      elif (
        (last_candle["RSI_3"] > 76.0)
        and (last_candle["WILLR_14"] > -4.0)
        and (last_candle["RSI_3_1h"] < 10.0)
        and (last_candle["RSI_3_4h"] < 40.0)
        and (last_candle["RSI_3_1d"] < 40.0)
        and (last_candle["close"] < (last_candle["high_max_30_1d"] * 0.50))
      ):
        return True, f"exit_{mode_name}_d_9_125"
      elif (
        (last_candle["RSI_3"] > 90.0)
        and (last_candle["RSI_3_1h"] < 15.0)
        and (last_candle["RSI_3_4h"] < 40.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_9_126"
      elif (
        (last_candle["RSI_3"] > 90.0)
        and (last_candle["RSI_3_1h"] < 10.0)
        and (last_candle["RSI_3_4h"] < 30.0)
        and (last_candle["RSI_3_1d"] < 40.0)
      ):
        return True, f"exit_{mode_name}_d_9_127"
      elif (last_candle["RSI_3"] > 94.0) and (last_candle["RSI_3_4h"] < 30.0) and (last_candle["AROONU_14_4h"] > 85.0):
        return True, f"exit_{mode_name}_d_9_128"
      elif (
        (last_candle["RSI_3"] > 86.0)
        and (last_candle["RSI_3_4h"] < 25.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 80.0))
      ):
        return True, f"exit_{mode_name}_d_9_129"
      elif (
        (last_candle["RSI_3"] > 74.0)
        and (last_candle["RSI_14_1h"] > 65.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 80.0)
        and (last_candle["CCI_20_change_pct_1h"] < -0.0)
      ):
        return True, f"exit_{mode_name}_d_9_130"
      elif (
        (last_candle["RSI_14"] < 38.0)
        and (last_candle["RSI_3_1h"] < 20.0)
        and (last_candle["RSI_3_4h"] < 30.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_9_131"
      elif (
        (last_candle["RSI_3"] > 80.0)
        and (last_candle["RSI_3_1h"] < 35.0)
        and (last_candle["RSI_3_4h"] < 35.0)
        and (last_candle["AROONU_14_1h"] > 50.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 40.0)
      ):
        return True, f"exit_{mode_name}_d_9_132"
      elif (
        (last_candle["RSI_3"] > 80.0)
        and (last_candle["AROONU_14_15m"] > 75.0)
        and (last_candle["AROONU_14_1h"] > 75.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 25.0))
      ):
        return True, f"exit_{mode_name}_d_9_133"
    elif 0.12 > current_profit >= 0.1:
      if (
        (last_candle["WILLR_14"] > -1.0)
        and (last_candle["RSI_14"] > 78.0)
        and (
          isinstance(last_candle["EMA_200_1h"], np.float64) and (last_candle["EMA_12_1h"] < last_candle["EMA_200_1h"])
        )
        and (
          isinstance(last_candle["EMA_200_4h"], np.float64) and (last_candle["EMA_12_4h"] < last_candle["EMA_200_4h"])
        )
        and (last_candle["KST_10_15_20_30_10_10_10_15_1h"] < last_candle["KSTs_9_1h"])
        and (last_candle["KST_10_15_20_30_10_10_10_15_4h"] < last_candle["KSTs_9_4h"])
      ):
        return True, f"exit_{mode_name}_d_10_1"
      elif (
        (last_candle["WILLR_14"] > -1.0)
        and (last_candle["RSI_14"] > 70.0)
        and (last_candle["CMF_20_1h"] < -0.0)
        and (
          isinstance(last_candle["EMA_200_1h"], np.float64) and (last_candle["EMA_12_1h"] < last_candle["EMA_200_1h"])
        )
        and (
          isinstance(last_candle["EMA_200_4h"], np.float64) and (last_candle["EMA_12_4h"] < last_candle["EMA_200_4h"])
        )
      ):
        return True, f"exit_{mode_name}_d_10_2"
      elif (
        (last_candle["WILLR_14"] > -4.0)
        and (last_candle["STOCHRSIk_14_14_3_3"] > 98.0)
        and (last_candle["CMF_20_1h"] < -0.0)
        and (last_candle["CMF_20_4h"] < -0.0)
        and (
          (last_candle["STOCHRSIk_14_14_3_3_4h"] > 20.0) and (last_candle["STOCHRSIk_14_14_3_3_change_pct_4h"] < -10.0)
        )
      ):
        return True, f"exit_{mode_name}_d_10_3"
      elif (
        (last_candle["WILLR_14"] > -5.0)
        and (last_candle["RSI_14"] > 76.0)
        and (last_candle["STOCHRSIk_14_14_3_3"] > 95.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 70.0)
        and (
          isinstance(last_candle["EMA_200_1h"], np.float64) and (last_candle["EMA_12_1h"] < last_candle["EMA_200_1h"])
        )
        and (
          isinstance(last_candle["EMA_200_4h"], np.float64) and (last_candle["EMA_12_4h"] < last_candle["EMA_200_4h"])
        )
      ):
        return True, f"exit_{mode_name}_d_10_4"
      elif (
        (last_candle["WILLR_14"] > -1.0)
        and (last_candle["RSI_14"] > 74.0)
        and (last_candle["ROC_9_1h"] < -5.0)
        and (last_candle["ROC_9_4h"] < -5.0)
      ):
        return True, f"exit_{mode_name}_d_10_5"
      elif (
        (last_candle["RSI_3"] > 70.0)
        and (last_candle["STOCHRSIk_14_14_3_3"] > 70.0)
        and (last_candle["RSI_14"] < 40.0)
        and (last_candle["ROC_9_1h"] < -10.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 50.0))
      ):
        return True, f"exit_{mode_name}_d_10_6"
      elif (
        (last_candle["RSI_14"] < 50.0)
        and (last_candle["STOCHRSIk_14_14_3_3"] > 70.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -40.0))
      ):
        return True, f"exit_{mode_name}_d_10_7"
      elif (
        (last_candle["WILLR_14"] > -1.0)
        and (last_candle["STOCHRSIk_14_14_3_3"] > 95.0)
        and (last_candle["CMF_20_1h"] < -0.1)
        and (last_candle["CMF_20_4h"] < -0.1)
        and (last_candle["change_pct_1d"] < -5.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 15.0))
      ):
        return True, f"exit_{mode_name}_d_10_8"
      elif (
        (last_candle["WILLR_14"] > -3.0)
        and (last_candle["RSI_3"] > 95.0)
        and (last_candle["change_pct_4h"] < -5.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 30.0))
      ):
        return True, f"exit_{mode_name}_d_10_9"
      elif (
        (last_candle["WILLR_14"] > -4.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["ROC_9_1h"] < -10.0)
        and (last_candle["ROC_9_4h"] < -10.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 10.0))
      ):
        return True, f"exit_{mode_name}_d_10_10"
      elif (
        (last_candle["RSI_3"] > 94.0)
        and (last_candle["RSI_14"] < 45.0)
        and (last_candle["ROC_9_15m"] < -10.0)
        and (last_candle["ROC_9_1h"] < -10.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -20.0))
      ):
        return True, f"exit_{mode_name}_d_10_11"
      elif (
        (last_candle["RSI_3"] > 95.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_4h"] < 10.0)
        and (last_candle["ROC_9_1h"] < -20.0)
        and (last_candle["ROC_9_4h"] < -20.0)
      ):
        return True, f"exit_{mode_name}_d_10_12"
      elif (last_candle["RSI_3"] > 96.0) and (last_candle["RSI_3_4h"] < 5.0) and (last_candle["ROC_9_4h"] < -25.0):
        return True, f"exit_{mode_name}_d_10_13"
      elif (
        (last_candle["RSI_3"] > 90.0)
        and (last_candle["WILLR_14"] > -2.0)
        and (last_candle["RSI_3_4h"] < 5.0)
        and (last_candle["AROONU_14_4h"] > 25.0)
      ):
        return True, f"exit_{mode_name}_d_10_14"
      elif (last_candle["RSI_3"] > 96.0) and (last_candle["RSI_14"] > 68.0) and (last_candle["ROC_9_4h"] < -30.0):
        return True, f"exit_{mode_name}_d_10_15"
      elif (
        (last_candle["RSI_3"] > 95.0)
        and (last_candle["AROONU_14_4h"] > 25.0)
        and (last_candle["ROC_9_4h"] < -25.0)
        and (last_candle["AROONU_14_1d"] > 50.0)
        and (last_candle["change_pct_1d"] < -15.0)
      ):
        return True, f"exit_{mode_name}_d_10_16"
      elif (
        (last_candle["RSI_3"] > 97.0)
        and (last_candle["WILLR_14"] > -10.0)
        and (last_candle["RSI_3_1h"] < 10.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 90.0)
        and (last_candle["ROC_9_4h"] > 30.0)
      ):
        return True, f"exit_{mode_name}_d_10_17"
      elif (
        (last_candle["RSI_3"] > 94.0)
        and (last_candle["RSI_14"] > 76.0)
        and (last_candle["RSI_3_4h"] < 20.0)
        and (last_candle["ROC_2_1d"] < -50.0)
      ):
        return True, f"exit_{mode_name}_d_10_18"
      elif (
        (last_candle["RSI_3"] > 94.0)
        and (last_candle["RSI_14"] > 74.0)
        and (last_candle["RSI_3_4h"] < 10.0)
        and (
          isinstance(last_candle["STOCHRSIk_14_14_3_3_1d"], np.float64)
          and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 70.0)
        )
      ):
        return True, f"exit_{mode_name}_d_10_19"
      elif (
        (last_candle["RSI_3"] > 60.0)
        and (last_candle["RSI_14"] < 40.0)
        and (last_candle["RSI_3_1h"] < 10.0)
        and (last_candle["AROONU_14_1h"] > 25.0)
      ):
        return True, f"exit_{mode_name}_d_10_20"
      elif (
        (last_candle["RSI_3"] > 95.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_1h"] < 20.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 90.0)
      ):
        return True, f"exit_{mode_name}_d_10_21"
      elif (
        (last_candle["RSI_3"] > 99.0)
        and (last_candle["WILLR_14"] > -1.0)
        and (last_candle["change_pct_4h"] < -5.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -30.0))
      ):
        return True, f"exit_{mode_name}_d_10_22"
      elif (
        (last_candle["RSI_3"] > 95.0)
        and (last_candle["WILLR_14"] > -5.0)
        and (last_candle["RSI_3_1h"] < 15.0)
        and (last_candle["RSI_3_1d"] < 5.0)
      ):
        return True, f"exit_{mode_name}_d_10_23"
      elif (
        (last_candle["RSI_3"] > 94.0)
        and (last_candle["RSI_14"] > 74.0)
        and (last_candle["WILLR_14"] > -10.0)
        and (last_candle["RSI_3_4h"] < 30.0)
        and (last_candle["AROONU_14_4h"] > 75.0)
      ):
        return True, f"exit_{mode_name}_d_10_24"
      elif (
        (last_candle["RSI_3"] > 95.0)
        and (last_candle["WILLR_14"] > -2.0)
        and (last_candle["RSI_3_4h"] < 10.0)
        and (last_candle["ROC_9_4h"] < -15.0)
        and (
          isinstance(last_candle["STOCHRSIk_14_14_3_3_1d"], np.float64)
          and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 50.0)
        )
      ):
        return True, f"exit_{mode_name}_d_10_25"
      elif (
        (last_candle["RSI_3"] > 90.0)
        and (last_candle["WILLR_14"] > -2.0)
        and (last_candle["RSI_3_4h"] < 15.0)
        and (last_candle["ROC_9_4h"] < -20.0)
      ):
        return True, f"exit_{mode_name}_d_10_26"
      elif (
        (last_candle["RSI_3"] > 90.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_1h"] < 20.0)
        and (last_candle["RSI_3_4h"] < 20.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 20.0)
      ):
        return True, f"exit_{mode_name}_d_10_27"
      elif (
        (last_candle["RSI_3"] > 85.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_15m"] < 10.0)
        and (last_candle["ROC_9_4h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_10_28"
      elif (
        (last_candle["RSI_3"] > 96.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_1h"] < 20.0)
        and (last_candle["RSI_3_4h"] < 20.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 30.0)
      ):
        return True, f"exit_{mode_name}_d_10_29"
      elif (
        (last_candle["RSI_3"] > 95.0)
        and (last_candle["RSI_3_1h"] < 25.0)
        and (last_candle["RSI_3_4h"] < 10.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 70.0)
      ):
        return True, f"exit_{mode_name}_d_10_30"
      elif (
        (last_candle["RSI_3"] > 85.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_1h"] < 15.0)
        and (last_candle["RSI_3_4h"] < 15.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 25.0)
      ):
        return True, f"exit_{mode_name}_d_10_31"
      elif (
        (last_candle["RSI_3"] > 95.0)
        and (last_candle["RSI_3_1h"] < 15.0)
        and (last_candle["ROC_2_4h"] < -30.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 30.0)
      ):
        return True, f"exit_{mode_name}_d_10_32"
      elif (
        (last_candle["RSI_3"] > 95.0)
        and (last_candle["WILLR_14"] > -1.0)
        and (last_candle["ROC_2_1h"] < -10.0)
        and (last_candle["ROC_9_1h"] > 30.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_10_33"
      elif (
        (last_candle["RSI_3"] > 65.0)
        and (last_candle["RSI_3_15m"] < 30.0)
        and (last_candle["RSI_14_1h"] > 80.0)
        and (last_candle["ROC_9_1h"] > 40.0)
      ):
        return True, f"exit_{mode_name}_d_10_34"
      elif (
        (last_candle["RSI_3"] > 90.0)
        and (last_candle["WILLR_14"] > -5.0)
        and (last_candle["RSI_3_1d"] < 25.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 75.0)
      ):
        return True, f"exit_{mode_name}_d_10_35"
      elif (
        (last_candle["RSI_3"] > 90.0)
        and (last_candle["WILLR_14"] > -10.0)
        and (last_candle["ROC_9_4h"] < -25.0)
        and (last_candle["RSI_3_1d"] < 25.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_10_36"
      elif (
        (last_candle["RSI_3"] > 84.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_1h"] < 20.0)
        and (last_candle["RSI_3_1d"] < 25.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_10_37"
      elif (
        (last_candle["RSI_3"] > 90.0)
        and (last_candle["WILLR_14"] > -10.0)
        and (last_candle["RSI_3_4h"] < 10.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 20.0)
      ):
        return True, f"exit_{mode_name}_d_10_38"
      elif (
        (last_candle["RSI_3"] > 96.0)
        and (last_candle["WILLR_14"] > -4.0)
        and (last_candle["CMF_20_4h"] < -0.0)
        and (last_candle["RSI_3_4h"] < 10.0)
      ):
        return True, f"exit_{mode_name}_d_10_39"
      elif (
        (last_candle["RSI_3"] > 90.0)
        and (last_candle["WILLR_14"] > -10.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 30.0)
        and (
          isinstance(last_candle["STOCHRSIk_14_14_3_3_1d"], np.float64)
          and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 90.0)
        )
      ):
        return True, f"exit_{mode_name}_d_10_40"
      elif (
        (last_candle["RSI_3"] > 96.0)
        and (last_candle["WILLR_14"] > -8.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 25.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 50.0))
      ):
        return True, f"exit_{mode_name}_d_10_41"
      elif (
        (last_candle["RSI_3"] > 95.0)
        and (last_candle["WILLR_14"] > -20.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 30.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 40.0))
        and (
          isinstance(last_candle["STOCHRSIk_14_14_3_3_1d"], np.float64)
          and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 70.0)
        )
      ):
        return True, f"exit_{mode_name}_d_10_42"
      elif (
        (last_candle["RSI_3"] > 85.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_1h"] < 15.0)
        and (last_candle["RSI_3_4h"] < 40.0)
        and (
          isinstance(last_candle["STOCHRSIk_14_14_3_3_1d"], np.float64)
          and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 90.0)
        )
      ):
        return True, f"exit_{mode_name}_d_10_43"
      elif (
        (last_candle["RSI_3"] > 75.0)
        and (last_candle["WILLR_14"] > -2.0)
        and (last_candle["RSI_3_4h"] < 30.0)
        and (last_candle["RSI_3_1d"] < 25.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -30.0))
      ):
        return True, f"exit_{mode_name}_d_10_44"
      elif (last_candle["RSI_3"] > 96.0) and (last_candle["WILLR_14"] > -4.0) and (last_candle["RSI_3_1h"] < 10.0):
        return True, f"exit_{mode_name}_d_10_45"
      elif (
        (last_candle["RSI_3"] > 92.0)
        and (last_candle["RSI_3_1h"] < 15.0)
        and (last_candle["RSI_3_4h"] < 10.0)
        and (last_candle["ROC_2_1d"] < -20.0)
      ):
        return True, f"exit_{mode_name}_d_10_46"
      elif (
        (last_candle["RSI_3"] > 88.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 80.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 40.0)
        and (last_candle["change_pct_1d"] < -5.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -5.0))
      ):
        return True, f"exit_{mode_name}_d_10_47"
      elif (
        (last_candle["RSI_3"] > 70.0)
        and (last_candle["RSI_14"] < 42.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (last_candle["RSI_3_4h"] < 20.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_10_48"
      elif (
        (last_candle["RSI_3"] > 95.0)
        and (last_candle["WILLR_14"] > -2.0)
        and (last_candle["RSI_3_4h"] < 20.0)
        and (last_candle["change_pct_1d"] < -5.0)
        and (
          isinstance(last_candle["STOCHRSIk_14_14_3_3_1d"], np.float64)
          and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 50.0)
        )
      ):
        return True, f"exit_{mode_name}_d_10_49"
      elif (
        (last_candle["RSI_3"] > 80.0)
        and (last_candle["WILLR_14"] > -2.0)
        and (last_candle["RSI_3_1d"] < 10.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 90.0)
      ):
        return True, f"exit_{mode_name}_d_10_50"
      elif (
        (last_candle["RSI_3"] > 68.0)
        and (last_candle["RSI_14"] < 44.0)
        and (last_candle["RSI_3_4h"] < 20.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_10_51"
      elif (
        (last_candle["RSI_3"] > 82.0)
        and (last_candle["RSI_14"] > 62.0)
        and (last_candle["WILLR_14"] > -10.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 70.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -15.0))
      ):
        return True, f"exit_{mode_name}_d_10_52"
      elif (
        (last_candle["RSI_3"] > 70.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["WILLR_14"] > -25.0)
        and (last_candle["RSI_3_1h"] < 20.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
        and (
          isinstance(last_candle["STOCHRSIk_14_14_3_3_1d"], np.float64)
          and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 50.0)
        )
      ):
        return True, f"exit_{mode_name}_d_10_53"
      elif (
        (last_candle["RSI_3"] > 80.0)
        and (last_candle["RSI_14"] < 44.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
        and (last_candle["ROC_9_4h"] < -10.0)
        and (last_candle["change_pct_1d"] < -10.0)
      ):
        return True, f"exit_{mode_name}_d_10_54"
      elif (
        (last_candle["RSI_3"] > 96.0)
        and (last_candle["WILLR_14"] > -12.0)
        and (last_candle["ROC_9_4h"] < -5.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 10.0))
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_10_55"
      elif (
        (last_candle["RSI_3"] > 85.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (last_candle["RSI_3_4h"] < 25.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -30.0))
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 10.0)
      ):
        return True, f"exit_{mode_name}_d_10_56"
      elif (
        (last_candle["RSI_3"] > 50.0)
        and (last_candle["RSI_14"] < 34.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -30.0))
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 70.0)
      ):
        return True, f"exit_{mode_name}_d_10_57"
      elif (
        (last_candle["RSI_3"] > 95.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (last_candle["RSI_3_4h"] < 30.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -15.0))
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_10_58"
      elif (
        (last_candle["RSI_3"] > 85.0)
        and (last_candle["WILLR_14"] > -10.0)
        and (last_candle["RSI_3_4h"] < 25.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -15.0))
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 40.0)
      ):
        return True, f"exit_{mode_name}_d_10_59"
      elif (
        (last_candle["RSI_3"] > 80.0)
        and (last_candle["RSI_14"] < 38.0)
        and (last_candle["RSI_14_4h"] > 65.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_10_60"
      elif (
        (last_candle["RSI_3"] > 94.0)
        and (last_candle["WILLR_14"] > -15.0)
        and (last_candle["RSI_3_4h"] < 10.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 30.0)
      ):
        return True, f"exit_{mode_name}_d_10_61"
      elif (
        (last_candle["RSI_3"] > 88.0)
        and (last_candle["WILLR_14"] > -2.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (last_candle["RSI_3_4h"] < 20.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 20.0))
        and (last_candle["change_pct_1d"] < -5.0)
      ):
        return True, f"exit_{mode_name}_d_10_62"
      elif (
        (last_candle["RSI_3"] > 70.0)
        and (last_candle["RSI_3_1d"] < 25.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 80.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 30.0)
      ):
        return True, f"exit_{mode_name}_d_10_63"
      elif (
        (last_candle["RSI_3"] > 90.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (last_candle["RSI_3_4h"] < 30.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 30.0))
      ):
        return True, f"exit_{mode_name}_d_10_64"
      elif (
        (last_candle["RSI_3"] > 70.0)
        and (last_candle["RSI_14"] < 40.0)
        and (last_candle["RSI_3_1h"] < 20.0)
        and (last_candle["RSI_3_4h"] < 15.0)
      ):
        return True, f"exit_{mode_name}_d_10_65"
      elif (
        (last_candle["RSI_3"] > 84.0)
        and (last_candle["RSI_14"] < 46.0)
        and (last_candle["RSI_3_1h"] < 20.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_10_66"
      elif (
        (last_candle["RSI_3"] > 50.0)
        and (last_candle["RSI_14"] < 40.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 80.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -25.0))
      ):
        return True, f"exit_{mode_name}_d_10_67"
      elif (
        (last_candle["RSI_3"] > 86.0)
        and (last_candle["RSI_14"] < 46.0)
        and (last_candle["RSI_3_1h"] < 25.0)
        and (last_candle["ROC_2_4h"] < -30.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 25.0)
      ):
        return True, f"exit_{mode_name}_d_10_68"
      elif (
        (last_candle["RSI_3"] > 97.0)
        and (last_candle["ROC_9_4h"] > 20.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
        and (last_candle["change_pct_4h"] < -5.0)
      ):
        return True, f"exit_{mode_name}_d_10_69"
      elif (
        (last_candle["RSI_3"] > 68.0)
        and (last_candle["RSI_14"] < 38.0)
        and (last_candle["RSI_3_1h"] < 25.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 20.0)
      ):
        return True, f"exit_{mode_name}_d_10_70"
      elif (
        (last_candle["RSI_3"] > 66.0)
        and (last_candle["RSI_14"] < 42.0)
        and (last_candle["RSI_3_4h"] < 25.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 20.0)
      ):
        return True, f"exit_{mode_name}_d_10_71"
      elif (
        (last_candle["RSI_3"] > 80.0)
        and (last_candle["RSI_14"] < 40.0)
        and (last_candle["RSI_3_1h"] < 10.0)
        and (last_candle["AROONU_14_4h"] > 25.0)
      ):
        return True, f"exit_{mode_name}_d_10_72"
      elif (
        (last_candle["RSI_3"] > 80.0)
        and (last_candle["RSI_3_1h"] < 25.0)
        and (last_candle["RSI_3_4h"] < 15.0)
        and (last_candle["ROC_9_4h"] < -20.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -25.0))
      ):
        return True, f"exit_{mode_name}_d_10_73"
      elif (
        (last_candle["RSI_3"] > 99.0)
        and (last_candle["WILLR_14"] > -10.0)
        and (last_candle["RSI_3_4h"] < 25.0)
        and (last_candle["RSI_3_1d"] < 25.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_10_74"
      elif (
        (last_candle["RSI_3"] > 98.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (last_candle["RSI_3_4h"] < 20.0)
        and (
          isinstance(last_candle["STOCHRSIk_14_14_3_3_1d"], np.float64)
          and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 50.0)
        )
      ):
        return True, f"exit_{mode_name}_d_10_75"
      elif (
        (last_candle["RSI_3"] > 70.0)
        and (last_candle["RSI_14"] < 48.0)
        and (last_candle["ROC_9_1h"] > 80.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 80.0)
      ):
        return True, f"exit_{mode_name}_d_10_76"
      elif (
        (last_candle["RSI_3"] > 78.0)
        and (last_candle["RSI_14"] < 44.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 50.0))
      ):
        return True, f"exit_{mode_name}_d_10_77"
      elif (
        (last_candle["RSI_3"] > 88.0)
        and (last_candle["WILLR_14"] > -14.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (last_candle["RSI_3_4h"] < 20.0)
        and (last_candle["RSI_3_1d"] < 20.0)
      ):
        return True, f"exit_{mode_name}_d_10_78"
      elif (
        (last_candle["RSI_3"] > 94.0)
        and (last_candle["WILLR_14"] > -1.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (last_candle["RSI_3_4h"] < 10.0)
      ):
        return True, f"exit_{mode_name}_d_10_79"
      elif (
        (last_candle["RSI_3"] > 74.0)
        and (last_candle["RSI_14"] < 44.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 50.0))
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 25.0)
      ):
        return True, f"exit_{mode_name}_d_10_80"
      elif (
        (last_candle["RSI_3"] > 86.0)
        and (last_candle["WILLR_14"] > -8.0)
        and (last_candle["RSI_3_1h"] < 25.0)
        and (last_candle["RSI_3_4h"] < 25.0)
        and (isinstance(last_candle["RSI_14_1d"], np.float64) and (last_candle["RSI_14_1d"] > 50.0))
      ):
        return True, f"exit_{mode_name}_d_10_81"
      elif (
        (last_candle["RSI_3"] > 84.0)
        and (last_candle["WILLR_14"] > -8.0)
        and (last_candle["RSI_3_4h"] < 30.0)
        and (last_candle["RSI_3_1d"] < 15.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 40.0)
      ):
        return True, f"exit_{mode_name}_d_10_82"
      elif (
        (last_candle["RSI_3"] > 74.0)
        and (last_candle["RSI_14"] < 44.0)
        and (last_candle["RSI_3_1h"] < 40.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 40.0)
      ):
        return True, f"exit_{mode_name}_d_10_83"
      elif (
        (last_candle["RSI_3"] > 92.0)
        and (last_candle["WILLR_14"] > -1.0)
        and (last_candle["RSI_3_4h"] < 30.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 20.0)
      ):
        return True, f"exit_{mode_name}_d_10_84"
      elif (
        (last_candle["RSI_3"] > 90.0)
        and (last_candle["WILLR_14"] > -6.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (last_candle["RSI_3_4h"] < 40.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_10_85"
      elif (
        (last_candle["RSI_3"] > 96.0)
        and (last_candle["RSI_14_4h"] > 80.0)
        and (last_candle["ROC_2_1h"] < -5.0)
        and (last_candle["ROC_9_1h"] > 5.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_10_86"
      elif (
        (last_candle["RSI_3"] > 68.0)
        and (last_candle["RSI_14"] < 42.0)
        and (last_candle["RSI_3_1h"] < 45.0)
        and (last_candle["RSI_3_4h"] < 50.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_10_87"
      elif (
        (last_candle["RSI_3"] > 90.0)
        and (last_candle["WILLR_14"] > -18.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 40.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
        and (last_candle["change_pct_1h"] < -2.0)
      ):
        return True, f"exit_{mode_name}_d_10_88"
      elif (
        (last_candle["RSI_3"] > 80.0)
        and (last_candle["RSI_14"] < 38.0)
        and (last_candle["ROC_9_1h"] < -5.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 25.0))
      ):
        return True, f"exit_{mode_name}_d_10_89"
      elif (
        (last_candle["RSI_3"] > 94.0)
        and (last_candle["WILLR_14"] > -25.0)
        and (last_candle["RSI_3_1h"] < 50.0)
        and (last_candle["RSI_3_4h"] < 30.0)
        and (last_candle["AROONU_14_4h"] > 50.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 40.0))
      ):
        return True, f"exit_{mode_name}_d_10_90"
      elif (
        (last_candle["RSI_3"] > 74.0)
        and (last_candle["RSI_14"] < 44.0)
        and (last_candle["RSI_3_1h"] < 25.0)
        and (last_candle["RSI_3_4h"] < 25.0)
        and (last_candle["AROONU_14_4h"] > 50.0)
        and (
          isinstance(last_candle["STOCHRSIk_14_14_3_3_1d"], np.float64)
          and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 50.0)
        )
      ):
        return True, f"exit_{mode_name}_d_10_91"
      elif (
        (last_candle["RSI_3"] > 82.0)
        and (last_candle["RSI_14"] < 46.0)
        and (last_candle["RSI_3_1h"] < 40.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 25.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -25.0))
      ):
        return True, f"exit_{mode_name}_d_10_92"
      elif (
        (last_candle["RSI_3"] > 74.0)
        and (last_candle["RSI_14"] < 48.0)
        and (last_candle["RSI_3_15m"] < 50.0)
        and (last_candle["AROONU_14_1h"] > 75.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 70.0)
        and (last_candle["AROONU_14_4h"] > 50.0)
        and (
          isinstance(last_candle["STOCHRSIk_14_14_3_3_1d"], np.float64)
          and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 90.0)
        )
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 30.0))
      ):
        return True, f"exit_{mode_name}_d_10_93"
      elif (
        (last_candle["RSI_3"] > 82.0)
        and (last_candle["RSI_14"] < 48.0)
        and (last_candle["RSI_3_1h"] < 25.0)
        and (last_candle["RSI_3_4h"] < 45.0)
        and (last_candle["AROONU_14_1h"] > 75.0)
        and (
          isinstance(last_candle["STOCHRSIk_14_14_3_3_1d"], np.float64)
          and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 90.0)
        )
      ):
        return True, f"exit_{mode_name}_d_10_94"
      elif (
        (last_candle["RSI_3"] > 86.0)
        and (last_candle["WILLR_14"] > -10.0)
        and (last_candle["RSI_3_1h"] < 45.0)
        and (last_candle["RSI_3_4h"] < 40.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 10.0)
        and (isinstance(last_candle["AROONU_14_1d"], np.float64) and (last_candle["AROONU_14_1d"] > 75.0))
      ):
        return True, f"exit_{mode_name}_d_10_95"
      elif (
        (last_candle["RSI_3"] > 64.0)
        and (last_candle["RSI_14"] < 44.0)
        and (last_candle["RSI_3_1h"] < 45.0)
        and (last_candle["RSI_3_1d"] < 45.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_10_96"
      elif (
        (last_candle["RSI_3"] > 86.0)
        and (last_candle["RSI_14"] < 44.0)
        and (last_candle["RSI_3_1h"] < 35.0)
        and (last_candle["AROONU_14_4h"] > 50.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 30.0)
      ):
        return True, f"exit_{mode_name}_d_10_97"
      elif (
        (last_candle["RSI_3"] > 92.0)
        and (last_candle["RSI_3_15m"] > 74.0)
        and (last_candle["RSI_3_1h"] < 60.0)
        and (last_candle["RSI_3_4h"] < 60.0)
        and (last_candle["RSI_3_1d"] > 80.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_10_98"
      elif (
        (last_candle["RSI_3"] > 62.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_1h"] < 65.0)
        and (last_candle["RSI_3_4h"] < 60.0)
        and (last_candle["AROONU_14_4h"] > 50.0)
        and (last_candle["STOCHk_14_3_3_4h"] > 40.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 80.0))
      ):
        return True, f"exit_{mode_name}_d_10_99"
      elif (
        (last_candle["RSI_3"] > 99.0)
        and (last_candle["RSI_14"] > 78.0)
        and (last_candle["RSI_3_15m"] > 70.0)
        and (last_candle["RSI_3_4h"] < 80.0)
      ):
        return True, f"exit_{mode_name}_d_10_100"
      elif (
        (last_candle["RSI_3"] > 86.0)
        and (last_candle["WILLR_14"] > -14.0)
        and (last_candle["RSI_3_1h"] < 50.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 40.0)
        and (isinstance(last_candle["ROC_9_4h"], np.float64) and (last_candle["ROC_9_4h"] > 40.0))
      ):
        return True, f"exit_{mode_name}_d_10_101"
      elif (
        (last_candle["RSI_3"] > 70.0)
        and (last_candle["RSI_14"] < 46.0)
        and (last_candle["RSI_3_1h"] < 60.0)
        and (last_candle["RSI_3_4h"] < 40.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 30.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 40.0))
      ):
        return True, f"exit_{mode_name}_d_10_102"
      elif (
        (last_candle["RSI_3"] > 80.0)
        and (last_candle["RSI_14"] < 54.0)
        and (last_candle["RSI_3_1h"] < 60.0)
        and (last_candle["RSI_14_4h"] > 70.0)
        and (isinstance(last_candle["ROC_9_4h"], np.float64) and (last_candle["ROC_9_4h"] > 80.0))
      ):
        return True, f"exit_{mode_name}_d_10_103"
      elif (
        (last_candle["RSI_3"] > 66.0)
        and (last_candle["RSI_14"] < 46.0)
        and (last_candle["RSI_3_1h"] < 60.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 40.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 90.0)
        and (last_candle["ROC_9_4h"] > 40.0)
      ):
        return True, f"exit_{mode_name}_d_10_104"
      elif (
        (last_candle["RSI_3"] > 80.0)
        and (last_candle["RSI_14"] < 46.0)
        and (last_candle["RSI_3_15m"] < 55.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 90.0)
        and (last_candle["ROC_9_4h"] > 25.0)
      ):
        return True, f"exit_{mode_name}_d_10_105"
      elif (
        (last_candle["RSI_3"] > 74.0)
        and (last_candle["RSI_14"] < 46.0)
        and (last_candle["RSI_3_1h"] < 50.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
        and (last_candle["RSI_14_4h"] > 70.0)
        and (last_candle["ROC_9_4h"] > 40.0)
      ):
        return True, f"exit_{mode_name}_d_10_106"
      elif (
        (last_candle["RSI_3"] > 76.0)
        and (last_candle["RSI_14"] < 46.0)
        and (last_candle["RSI_3_1h"] < 50.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 70.0)
        and (last_candle["RSI_14_4h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_10_107"
      elif (
        (last_candle["RSI_3"] > 58.0)
        and (last_candle["RSI_14"] < 46.0)
        and (last_candle["RSI_3_1h"] < 60.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 80.0)
      ):
        return True, f"exit_{mode_name}_d_10_108"
      elif (
        (last_candle["RSI_3"] > 78.0)
        and (last_candle["WILLR_14"] > -6.0)
        and (last_candle["RSI_3_1h"] < 50.0)
        and (last_candle["RSI_3_4h"] < 20.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 50.0))
      ):
        return True, f"exit_{mode_name}_d_10_109"
      elif (
        (last_candle["RSI_3"] > 74.0)
        and (last_candle["RSI_3_4h"] < 65.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
        and (last_candle["ROC_9_4h"] > 25.0)
      ):
        return True, f"exit_{mode_name}_d_10_110"
      elif (
        (last_candle["RSI_3"] > 52.0)
        and (last_candle["RSI_14"] < 42.0)
        and (last_candle["RSI_3_1h"] < 50.0)
        and (last_candle["RSI_14_4h"] > 70.0)
        and (last_candle["AROONU_14_1h"] > 75.0)
        and (last_candle["AROONU_14_4h"] > 75.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 20.0))
      ):
        return True, f"exit_{mode_name}_d_10_111"
      elif (
        (last_candle["RSI_3"] > 82.0)
        and (last_candle["WILLR_14"] > -20.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_1h"] < 35.0)
        and (last_candle["RSI_3_4h"] < 35.0)
        and (last_candle["RSI_3_1d"] < 60.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 30.0))
      ):
        return True, f"exit_{mode_name}_d_10_112"
      elif (
        (last_candle["RSI_3"] > 86.0)
        and (last_candle["WILLR_14"] > -1.0)
        and (last_candle["RSI_3_1d"] < 30.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
        and (isinstance(last_candle["ROC_9_4h"], np.float64) and (last_candle["ROC_9_4h"] > 10.0))
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -10.0))
      ):
        return True, f"exit_{mode_name}_d_10_113"
      elif (
        (last_candle["RSI_3"] > 86.0)
        and (last_candle["RSI_14"] < 48.0)
        and (last_candle["RSI_3_1h"] < 20.0)
        and (last_candle["RSI_3_4h"] < 30.0)
        and (last_candle["RSI_3_1d"] < 30.0)
      ):
        return True, f"exit_{mode_name}_d_10_114"
      elif (
        (last_candle["RSI_3"] > 80.0)
        and (last_candle["RSI_14"] < 46.0)
        and (last_candle["RSI_3_15m"] < 30.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_10_115"
      elif (
        (last_candle["RSI_3"] > 92.0)
        and (last_candle["RSI_3_1h"] < 15.0)
        and (last_candle["RSI_3_4h"] < 40.0)
        and (last_candle["AROONU_14_4h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_10_116"
      elif (
        (last_candle["RSI_3"] > 88.0)
        and (last_candle["RSI_3_1h"] < 50.0)
        and (last_candle["AROONU_14_1h"] > 80.0)
        and (last_candle["AROONU_14_4h"] > 80.0)
      ):
        return True, f"exit_{mode_name}_d_10_117"
      elif (
        (last_candle["RSI_3"] > 92.0)
        and (last_candle["RSI_3_1h"] < 20.0)
        and (last_candle["RSI_3_4h"] < 60.0)
        and (last_candle["AROONU_14_4h"] > 40.0)
      ):
        return True, f"exit_{mode_name}_d_10_118"
      elif (
        (last_candle["RSI_3"] > 88.0)
        and (last_candle["WILLR_14"] > -20.0)
        and (last_candle["RSI_3_1h"] < 60.0)
        and (last_candle["RSI_3_4h"] < 60.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 40.0)
      ):
        return True, f"exit_{mode_name}_d_10_119"
      elif (
        (last_candle["RSI_3"] > 56.0)
        and (last_candle["RSI_14"] < 46.0)
        and (last_candle["RSI_3_1h"] < 40.0)
        and (last_candle["AROONU_14_4h"] > 75.0)
      ):
        return True, f"exit_{mode_name}_d_10_120"
      elif (
        (last_candle["RSI_3"] > 62.0)
        and (last_candle["RSI_14"] < 44.0)
        and (last_candle["RSI_3_1h"] < 50.0)
        and (last_candle["RSI_14_4h"] > 85.0)
      ):
        return True, f"exit_{mode_name}_d_10_121"
      elif (
        (last_candle["RSI_3"] > 60.0)
        and (last_candle["RSI_14"] < 42.0)
        and (last_candle["RSI_3_4h"] < 30.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_10_122"
      elif (
        (last_candle["RSI_3"] > 90.0)
        and (last_candle["WILLR_14"] > -2.0)
        and (last_candle["RSI_3_1h"] < 10.0)
        and (last_candle["RSI_3_1d"] < 30.0)
      ):
        return True, f"exit_{mode_name}_d_10_123"
      elif (
        (last_candle["RSI_3"] > 90.0)
        and (last_candle["RSI_3_1h"] < 15.0)
        and (
          isinstance(last_candle["STOCHRSIk_14_14_3_3_1d"], np.float64)
          and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 80.0)
        )
      ):
        return True, f"exit_{mode_name}_d_10_124"
      elif (
        (last_candle["RSI_3"] > 78.0)
        and (last_candle["WILLR_14"] > -2.0)
        and (last_candle["RSI_3_1h"] < 10.0)
        and (last_candle["RSI_3_4h"] < 40.0)
        and (last_candle["RSI_3_1d"] < 40.0)
        and (last_candle["close"] < (last_candle["high_max_30_1d"] * 0.50))
      ):
        return True, f"exit_{mode_name}_d_10_125"
      elif (
        (last_candle["RSI_3"] > 92.0)
        and (last_candle["RSI_3_1h"] < 15.0)
        and (last_candle["RSI_3_4h"] < 40.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_10_126"
      elif (
        (last_candle["RSI_3"] > 92.0)
        and (last_candle["RSI_3_1h"] < 10.0)
        and (last_candle["RSI_3_4h"] < 30.0)
        and (last_candle["RSI_3_1d"] < 40.0)
      ):
        return True, f"exit_{mode_name}_d_10_127"
      elif (last_candle["RSI_3"] > 96.0) and (last_candle["RSI_3_4h"] < 30.0) and (last_candle["AROONU_14_4h"] > 85.0):
        return True, f"exit_{mode_name}_d_10_128"
      elif (
        (last_candle["RSI_3"] > 88.0)
        and (last_candle["RSI_3_4h"] < 25.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 80.0))
      ):
        return True, f"exit_{mode_name}_d_10_129"
      elif (
        (last_candle["RSI_3"] > 76.0)
        and (last_candle["RSI_14_1h"] > 65.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 80.0)
        and (last_candle["CCI_20_change_pct_1h"] < -0.0)
      ):
        return True, f"exit_{mode_name}_d_10_130"
      elif (
        (last_candle["RSI_14"] < 36.0)
        and (last_candle["RSI_3_1h"] < 20.0)
        and (last_candle["RSI_3_4h"] < 30.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_10_131"
      elif (
        (last_candle["RSI_3"] > 82.0)
        and (last_candle["RSI_3_1h"] < 35.0)
        and (last_candle["RSI_3_4h"] < 35.0)
        and (last_candle["AROONU_14_1h"] > 50.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 40.0)
      ):
        return True, f"exit_{mode_name}_d_10_132"
      elif (
        (last_candle["RSI_3"] > 82.0)
        and (last_candle["AROONU_14_15m"] > 75.0)
        and (last_candle["AROONU_14_1h"] > 75.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 25.0))
      ):
        return True, f"exit_{mode_name}_d_10_133"
    elif 0.2 > current_profit >= 0.12:
      if (
        (last_candle["WILLR_14"] > -1.0)
        and (last_candle["RSI_14"] > 78.0)
        and (
          isinstance(last_candle["EMA_200_1h"], np.float64) and (last_candle["EMA_12_1h"] < last_candle["EMA_200_1h"])
        )
        and (
          isinstance(last_candle["EMA_200_4h"], np.float64) and (last_candle["EMA_12_4h"] < last_candle["EMA_200_4h"])
        )
        and (last_candle["KST_10_15_20_30_10_10_10_15_1h"] < last_candle["KSTs_9_1h"])
        and (last_candle["KST_10_15_20_30_10_10_10_15_4h"] < last_candle["KSTs_9_4h"])
      ):
        return True, f"exit_{mode_name}_d_11_1"
      elif (
        (last_candle["WILLR_14"] > -1.0)
        and (last_candle["RSI_14"] > 74.0)
        and (last_candle["CMF_20_1h"] < -0.0)
        and (
          isinstance(last_candle["EMA_200_1h"], np.float64) and (last_candle["EMA_12_1h"] < last_candle["EMA_200_1h"])
        )
        and (
          isinstance(last_candle["EMA_200_4h"], np.float64) and (last_candle["EMA_12_4h"] < last_candle["EMA_200_4h"])
        )
      ):
        return True, f"exit_{mode_name}_d_11_2"
      elif (
        (last_candle["WILLR_14"] > -2.0)
        and (last_candle["STOCHRSIk_14_14_3_3"] > 99.0)
        and (last_candle["CMF_20_1h"] < -0.0)
        and (last_candle["CMF_20_4h"] < -0.0)
        and (
          (last_candle["STOCHRSIk_14_14_3_3_4h"] > 20.0) and (last_candle["STOCHRSIk_14_14_3_3_change_pct_4h"] < -10.0)
        )
      ):
        return True, f"exit_{mode_name}_d_11_3"
      elif (
        (last_candle["WILLR_14"] > -2.0)
        and (last_candle["RSI_14"] > 78.0)
        and (last_candle["STOCHRSIk_14_14_3_3"] > 95.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 70.0)
        and (
          isinstance(last_candle["EMA_200_1h"], np.float64) and (last_candle["EMA_12_1h"] < last_candle["EMA_200_1h"])
        )
        and (
          isinstance(last_candle["EMA_200_4h"], np.float64) and (last_candle["EMA_12_4h"] < last_candle["EMA_200_4h"])
        )
      ):
        return True, f"exit_{mode_name}_d_11_4"
      elif (
        (last_candle["WILLR_14"] > -1.0)
        and (last_candle["RSI_14"] > 76.0)
        and (last_candle["ROC_9_1h"] < -5.0)
        and (last_candle["ROC_9_4h"] < -5.0)
      ):
        return True, f"exit_{mode_name}_d_11_5"
      elif (
        (last_candle["RSI_3"] > 70.0)
        and (last_candle["STOCHRSIk_14_14_3_3"] > 70.0)
        and (last_candle["RSI_14"] < 40.0)
        and (last_candle["ROC_9_1h"] < -10.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 50.0))
      ):
        return True, f"exit_{mode_name}_d_11_6"
      elif (
        (last_candle["RSI_14"] < 50.0)
        and (last_candle["STOCHRSIk_14_14_3_3"] > 70.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -40.0))
      ):
        return True, f"exit_{mode_name}_d_11_7"
      elif (
        (last_candle["WILLR_14"] > -1.0)
        and (last_candle["STOCHRSIk_14_14_3_3"] > 98.0)
        and (last_candle["CMF_20_1h"] < -0.1)
        and (last_candle["CMF_20_4h"] < -0.1)
        and (last_candle["change_pct_1d"] < -5.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 15.0))
      ):
        return True, f"exit_{mode_name}_d_11_8"
      elif (
        (last_candle["WILLR_14"] > -2.0)
        and (last_candle["RSI_3"] > 95.0)
        and (last_candle["change_pct_4h"] < -5.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 30.0))
      ):
        return True, f"exit_{mode_name}_d_11_9"
      elif (
        (last_candle["WILLR_14"] > -2.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["ROC_9_1h"] < -10.0)
        and (last_candle["ROC_9_4h"] < -10.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 10.0))
      ):
        return True, f"exit_{mode_name}_d_11_10"
      elif (
        (last_candle["RSI_3"] > 96.0)
        and (last_candle["RSI_14"] < 45.0)
        and (last_candle["ROC_9_15m"] < -10.0)
        and (last_candle["ROC_9_1h"] < -10.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -20.0))
      ):
        return True, f"exit_{mode_name}_d_11_11"
      elif (
        (last_candle["RSI_3"] > 98.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_4h"] < 10.0)
        and (last_candle["ROC_9_1h"] < -20.0)
        and (last_candle["ROC_9_4h"] < -20.0)
      ):
        return True, f"exit_{mode_name}_d_11_12"
      elif (last_candle["RSI_3"] > 98.0) and (last_candle["RSI_3_4h"] < 5.0) and (last_candle["ROC_9_4h"] < -25.0):
        return True, f"exit_{mode_name}_d_11_13"
      elif (
        (last_candle["RSI_3"] > 95.0)
        and (last_candle["WILLR_14"] > -1.0)
        and (last_candle["RSI_3_4h"] < 5.0)
        and (last_candle["AROONU_14_4h"] > 25.0)
      ):
        return True, f"exit_{mode_name}_d_11_14"
      elif (last_candle["RSI_3"] > 98.0) and (last_candle["RSI_14"] > 70.0) and (last_candle["ROC_9_4h"] < -30.0):
        return True, f"exit_{mode_name}_d_11_15"
      elif (
        (last_candle["RSI_3"] > 98.0)
        and (last_candle["AROONU_14_4h"] > 25.0)
        and (last_candle["ROC_9_4h"] < -25.0)
        and (last_candle["AROONU_14_1d"] > 50.0)
        and (last_candle["change_pct_1d"] < -15.0)
      ):
        return True, f"exit_{mode_name}_d_11_16"
      elif (
        (last_candle["RSI_3"] > 98.0)
        and (last_candle["WILLR_14"] > -5.0)
        and (last_candle["RSI_3_1h"] < 10.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 90.0)
        and (last_candle["ROC_9_4h"] > 30.0)
      ):
        return True, f"exit_{mode_name}_d_11_17"
      elif (
        (last_candle["RSI_3"] > 96.0)
        and (last_candle["RSI_14"] > 78.0)
        and (last_candle["RSI_3_4h"] < 20.0)
        and (last_candle["ROC_2_1d"] < -50.0)
      ):
        return True, f"exit_{mode_name}_d_11_18"
      elif (
        (last_candle["RSI_3"] > 96.0)
        and (last_candle["RSI_14"] > 76.0)
        and (last_candle["RSI_3_4h"] < 10.0)
        and (
          isinstance(last_candle["STOCHRSIk_14_14_3_3_1d"], np.float64)
          and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 70.0)
        )
      ):
        return True, f"exit_{mode_name}_d_11_19"
      elif (
        (last_candle["RSI_3"] > 80.0)
        and (last_candle["RSI_14"] < 40.0)
        and (last_candle["RSI_3_1h"] < 10.0)
        and (last_candle["AROONU_14_1h"] > 25.0)
      ):
        return True, f"exit_{mode_name}_d_11_20"
      elif (
        (last_candle["RSI_3"] > 98.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_1h"] < 20.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 90.0)
      ):
        return True, f"exit_{mode_name}_d_11_21"
      elif (
        (last_candle["RSI_3"] > 99.0)
        and (last_candle["WILLR_14"] > -1.0)
        and (last_candle["change_pct_4h"] < -5.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -30.0))
      ):
        return True, f"exit_{mode_name}_d_11_22"
      elif (
        (last_candle["RSI_3"] > 98.0)
        and (last_candle["WILLR_14"] > -2.0)
        and (last_candle["RSI_3_1h"] < 15.0)
        and (last_candle["RSI_3_1d"] < 5.0)
      ):
        return True, f"exit_{mode_name}_d_11_23"
      elif (
        (last_candle["RSI_3"] > 96.0)
        and (last_candle["RSI_14"] > 76.0)
        and (last_candle["WILLR_14"] > -5.0)
        and (last_candle["RSI_3_4h"] < 30.0)
        and (last_candle["AROONU_14_4h"] > 75.0)
      ):
        return True, f"exit_{mode_name}_d_11_24"
      elif (
        (last_candle["RSI_3"] > 97.0)
        and (last_candle["WILLR_14"] > -1.0)
        and (last_candle["RSI_3_4h"] < 10.0)
        and (last_candle["ROC_9_4h"] < -15.0)
        and (
          isinstance(last_candle["STOCHRSIk_14_14_3_3_1d"], np.float64)
          and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 50.0)
        )
      ):
        return True, f"exit_{mode_name}_d_11_25"
      elif (
        (last_candle["RSI_3"] > 95.0)
        and (last_candle["WILLR_14"] > -1.0)
        and (last_candle["RSI_3_4h"] < 15.0)
        and (last_candle["ROC_9_4h"] < -20.0)
      ):
        return True, f"exit_{mode_name}_d_11_26"
      elif (
        (last_candle["RSI_3"] > 95.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_1h"] < 20.0)
        and (last_candle["RSI_3_4h"] < 20.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 20.0)
      ):
        return True, f"exit_{mode_name}_d_11_27"
      elif (
        (last_candle["RSI_3"] > 90.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_15m"] < 10.0)
        and (last_candle["ROC_9_4h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_11_28"
      elif (
        (last_candle["RSI_3"] > 98.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_1h"] < 20.0)
        and (last_candle["RSI_3_4h"] < 20.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 30.0)
      ):
        return True, f"exit_{mode_name}_d_11_29"
      elif (
        (last_candle["RSI_3"] > 98.0)
        and (last_candle["RSI_3_1h"] < 25.0)
        and (last_candle["RSI_3_4h"] < 10.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 70.0)
      ):
        return True, f"exit_{mode_name}_d_11_30"
      elif (
        (last_candle["RSI_3"] > 90.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_1h"] < 15.0)
        and (last_candle["RSI_3_4h"] < 15.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 25.0)
      ):
        return True, f"exit_{mode_name}_d_11_31"
      elif (
        (last_candle["RSI_3"] > 98.0)
        and (last_candle["RSI_3_1h"] < 15.0)
        and (last_candle["ROC_2_4h"] < -30.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 30.0)
      ):
        return True, f"exit_{mode_name}_d_11_32"
      elif (
        (last_candle["RSI_3"] > 98.0)
        and (last_candle["WILLR_14"] > -1.0)
        and (last_candle["ROC_2_1h"] < -10.0)
        and (last_candle["ROC_9_1h"] > 30.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_11_33"
      elif (
        (last_candle["RSI_3"] > 65.0)
        and (last_candle["RSI_3_15m"] < 30.0)
        and (last_candle["RSI_14_1h"] > 80.0)
        and (last_candle["ROC_9_1h"] > 40.0)
      ):
        return True, f"exit_{mode_name}_d_11_34"
      elif (
        (last_candle["RSI_3"] > 92.0)
        and (last_candle["WILLR_14"] > -4.0)
        and (last_candle["RSI_3_1d"] < 25.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 75.0)
      ):
        return True, f"exit_{mode_name}_d_11_35"
      elif (
        (last_candle["RSI_3"] > 95.0)
        and (last_candle["WILLR_14"] > -5.0)
        and (last_candle["ROC_9_4h"] < -25.0)
        and (last_candle["RSI_3_1d"] < 25.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_11_36"
      elif (
        (last_candle["RSI_3"] > 86.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_1h"] < 20.0)
        and (last_candle["RSI_3_1d"] < 25.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_11_37"
      elif (
        (last_candle["RSI_3"] > 95.0)
        and (last_candle["WILLR_14"] > -5.0)
        and (last_candle["RSI_3_4h"] < 10.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 20.0)
      ):
        return True, f"exit_{mode_name}_d_11_38"
      elif (
        (last_candle["RSI_3"] > 97.0)
        and (last_candle["WILLR_14"] > -3.0)
        and (last_candle["CMF_20_4h"] < -0.0)
        and (last_candle["RSI_3_4h"] < 10.0)
      ):
        return True, f"exit_{mode_name}_d_11_39"
      elif (
        (last_candle["RSI_3"] > 95.0)
        and (last_candle["WILLR_14"] > -5.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 30.0)
        and (
          isinstance(last_candle["STOCHRSIk_14_14_3_3_1d"], np.float64)
          and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 90.0)
        )
      ):
        return True, f"exit_{mode_name}_d_11_40"
      elif (
        (last_candle["RSI_3"] > 97.0)
        and (last_candle["WILLR_14"] > -4.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 25.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 50.0))
      ):
        return True, f"exit_{mode_name}_d_11_41"
      elif (
        (last_candle["RSI_3"] > 96.0)
        and (last_candle["WILLR_14"] > -15.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 30.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 40.0))
        and (
          isinstance(last_candle["STOCHRSIk_14_14_3_3_1d"], np.float64)
          and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 70.0)
        )
      ):
        return True, f"exit_{mode_name}_d_11_42"
      elif (
        (last_candle["RSI_3"] > 90.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_1h"] < 15.0)
        and (last_candle["RSI_3_4h"] < 40.0)
        and (
          isinstance(last_candle["STOCHRSIk_14_14_3_3_1d"], np.float64)
          and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 90.0)
        )
      ):
        return True, f"exit_{mode_name}_d_11_43"
      elif (
        (last_candle["RSI_3"] > 80.0)
        and (last_candle["WILLR_14"] > -2.0)
        and (last_candle["RSI_3_4h"] < 30.0)
        and (last_candle["RSI_3_1d"] < 25.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -30.0))
      ):
        return True, f"exit_{mode_name}_d_11_44"
      elif (last_candle["RSI_3"] > 98.0) and (last_candle["WILLR_14"] > -2.0) and (last_candle["RSI_3_1h"] < 10.0):
        return True, f"exit_{mode_name}_d_11_45"
      elif (
        (last_candle["RSI_3"] > 94.0)
        and (last_candle["RSI_3_1h"] < 15.0)
        and (last_candle["RSI_3_4h"] < 10.0)
        and (last_candle["ROC_2_1d"] < -20.0)
      ):
        return True, f"exit_{mode_name}_d_11_46"
      elif (
        (last_candle["RSI_3"] > 90.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 80.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 40.0)
        and (last_candle["change_pct_1d"] < -5.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -5.0))
      ):
        return True, f"exit_{mode_name}_d_11_47"
      elif (
        (last_candle["RSI_3"] > 75.0)
        and (last_candle["RSI_14"] < 40.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (last_candle["RSI_3_4h"] < 20.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_11_48"
      elif (
        (last_candle["RSI_3"] > 96.0)
        and (last_candle["WILLR_14"] > -2.0)
        and (last_candle["RSI_3_4h"] < 20.0)
        and (last_candle["change_pct_1d"] < -5.0)
        and (
          isinstance(last_candle["STOCHRSIk_14_14_3_3_1d"], np.float64)
          and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 50.0)
        )
      ):
        return True, f"exit_{mode_name}_d_11_49"
      elif (
        (last_candle["RSI_3"] > 85.0)
        and (last_candle["WILLR_14"] > -2.0)
        and (last_candle["RSI_3_1d"] < 10.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 90.0)
      ):
        return True, f"exit_{mode_name}_d_11_50"
      elif (
        (last_candle["RSI_3"] > 70.0)
        and (last_candle["RSI_14"] < 42.0)
        and (last_candle["RSI_3_4h"] < 20.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_11_51"
      elif (
        (last_candle["RSI_3"] > 84.0)
        and (last_candle["RSI_14"] > 64.0)
        and (last_candle["WILLR_14"] > -10.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 70.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -15.0))
      ):
        return True, f"exit_{mode_name}_d_11_52"
      elif (
        (last_candle["RSI_3"] > 70.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["WILLR_14"] > -25.0)
        and (last_candle["RSI_3_1h"] < 20.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
        and (
          isinstance(last_candle["STOCHRSIk_14_14_3_3_1d"], np.float64)
          and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 50.0)
        )
      ):
        return True, f"exit_{mode_name}_d_11_53"
      elif (
        (last_candle["RSI_3"] > 82.0)
        and (last_candle["RSI_14"] < 42.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
        and (last_candle["ROC_9_4h"] < -10.0)
        and (last_candle["change_pct_1d"] < -10.0)
      ):
        return True, f"exit_{mode_name}_d_11_54"
      elif (
        (last_candle["RSI_3"] > 98.0)
        and (last_candle["WILLR_14"] > -10.0)
        and (last_candle["ROC_9_4h"] < -5.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 10.0))
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_11_55"
      elif (
        (last_candle["RSI_3"] > 90.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (last_candle["RSI_3_4h"] < 25.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -30.0))
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 10.0)
      ):
        return True, f"exit_{mode_name}_d_11_56"
      elif (
        (last_candle["RSI_3"] > 50.0)
        and (last_candle["RSI_14"] < 32.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -30.0))
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 70.0)
      ):
        return True, f"exit_{mode_name}_d_11_57"
      elif (
        (last_candle["RSI_3"] > 98.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (last_candle["RSI_3_4h"] < 30.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -15.0))
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_11_58"
      elif (
        (last_candle["RSI_3"] > 90.0)
        and (last_candle["WILLR_14"] > -8.0)
        and (last_candle["RSI_3_4h"] < 25.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -15.0))
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 40.0)
      ):
        return True, f"exit_{mode_name}_d_11_59"
      elif (
        (last_candle["RSI_3"] > 85.0)
        and (last_candle["RSI_14"] < 36.0)
        and (last_candle["RSI_14_4h"] > 65.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_11_60"
      elif (
        (last_candle["RSI_3"] > 96.0)
        and (last_candle["WILLR_14"] > -10.0)
        and (last_candle["RSI_3_4h"] < 10.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 30.0)
      ):
        return True, f"exit_{mode_name}_d_11_61"
      elif (
        (last_candle["RSI_3"] > 90.0)
        and (last_candle["WILLR_14"] > -2.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (last_candle["RSI_3_4h"] < 20.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 20.0))
        and (last_candle["change_pct_1d"] < -5.0)
      ):
        return True, f"exit_{mode_name}_d_11_62"
      elif (
        (last_candle["RSI_3"] > 72.0)
        and (last_candle["RSI_3_1d"] < 25.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 80.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 30.0)
      ):
        return True, f"exit_{mode_name}_d_11_63"
      elif (
        (last_candle["RSI_3"] > 92.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (last_candle["RSI_3_4h"] < 30.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 30.0))
      ):
        return True, f"exit_{mode_name}_d_11_64"
      elif (
        (last_candle["RSI_3"] > 72.0)
        and (last_candle["RSI_14"] < 38.0)
        and (last_candle["RSI_3_1h"] < 20.0)
        and (last_candle["RSI_3_4h"] < 15.0)
      ):
        return True, f"exit_{mode_name}_d_11_65"
      elif (
        (last_candle["RSI_3"] > 86.0)
        and (last_candle["RSI_14"] < 44.0)
        and (last_candle["RSI_3_1h"] < 20.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_11_66"
      elif (
        (last_candle["RSI_3"] > 50.0)
        and (last_candle["RSI_14"] < 38.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 80.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -25.0))
      ):
        return True, f"exit_{mode_name}_d_11_67"
      elif (
        (last_candle["RSI_3"] > 88.0)
        and (last_candle["RSI_14"] < 44.0)
        and (last_candle["RSI_3_1h"] < 25.0)
        and (last_candle["ROC_2_4h"] < -30.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 25.0)
      ):
        return True, f"exit_{mode_name}_d_11_68"
      elif (
        (last_candle["RSI_3"] > 98.0)
        and (last_candle["ROC_9_4h"] > 20.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
        and (last_candle["change_pct_4h"] < -5.0)
      ):
        return True, f"exit_{mode_name}_d_11_69"
      elif (
        (last_candle["RSI_3"] > 70.0)
        and (last_candle["RSI_14"] < 36.0)
        and (last_candle["RSI_3_1h"] < 25.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 20.0)
      ):
        return True, f"exit_{mode_name}_d_11_70"
      elif (
        (last_candle["RSI_3"] > 68.0)
        and (last_candle["RSI_14"] < 40.0)
        and (last_candle["RSI_3_4h"] < 25.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 20.0)
      ):
        return True, f"exit_{mode_name}_d_11_71"
      elif (
        (last_candle["RSI_3"] > 82.0)
        and (last_candle["RSI_14"] < 38.0)
        and (last_candle["RSI_3_1h"] < 10.0)
        and (last_candle["AROONU_14_4h"] > 25.0)
      ):
        return True, f"exit_{mode_name}_d_11_72"
      elif (
        (last_candle["RSI_3"] > 82.0)
        and (last_candle["RSI_3_1h"] < 25.0)
        and (last_candle["RSI_3_4h"] < 15.0)
        and (last_candle["ROC_9_4h"] < -20.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -25.0))
      ):
        return True, f"exit_{mode_name}_d_11_73"
      elif (
        (last_candle["RSI_3"] > 99.0)
        and (last_candle["WILLR_14"] > -10.0)
        and (last_candle["RSI_3_4h"] < 25.0)
        and (last_candle["RSI_3_1d"] < 25.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_11_74"
      elif (
        (last_candle["RSI_3"] > 98.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (last_candle["RSI_3_4h"] < 20.0)
        and (
          isinstance(last_candle["STOCHRSIk_14_14_3_3_1d"], np.float64)
          and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 50.0)
        )
      ):
        return True, f"exit_{mode_name}_d_11_75"
      elif (
        (last_candle["RSI_3"] > 72.0)
        and (last_candle["RSI_14"] < 46.0)
        and (last_candle["ROC_9_1h"] > 80.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 80.0)
      ):
        return True, f"exit_{mode_name}_d_11_76"
      elif (
        (last_candle["RSI_3"] > 80.0)
        and (last_candle["RSI_14"] < 42.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 50.0))
      ):
        return True, f"exit_{mode_name}_d_11_77"
      elif (
        (last_candle["RSI_3"] > 90.0)
        and (last_candle["WILLR_14"] > -12.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (last_candle["RSI_3_4h"] < 20.0)
        and (last_candle["RSI_3_1d"] < 20.0)
      ):
        return True, f"exit_{mode_name}_d_11_78"
      elif (
        (last_candle["RSI_3"] > 96.0)
        and (last_candle["WILLR_14"] > -1.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (last_candle["RSI_3_4h"] < 10.0)
      ):
        return True, f"exit_{mode_name}_d_11_79"
      elif (
        (last_candle["RSI_3"] > 76.0)
        and (last_candle["RSI_14"] < 42.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 50.0))
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 25.0)
      ):
        return True, f"exit_{mode_name}_d_11_80"
      elif (
        (last_candle["RSI_3"] > 88.0)
        and (last_candle["WILLR_14"] > -6.0)
        and (last_candle["RSI_3_1h"] < 25.0)
        and (last_candle["RSI_3_4h"] < 25.0)
        and (isinstance(last_candle["RSI_14_1d"], np.float64) and (last_candle["RSI_14_1d"] > 50.0))
      ):
        return True, f"exit_{mode_name}_d_11_81"
      elif (
        (last_candle["RSI_3"] > 86.0)
        and (last_candle["WILLR_14"] > -6.0)
        and (last_candle["RSI_3_4h"] < 30.0)
        and (last_candle["RSI_3_1d"] < 15.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 40.0)
      ):
        return True, f"exit_{mode_name}_d_11_82"
      elif (
        (last_candle["RSI_3"] > 76.0)
        and (last_candle["RSI_14"] < 42.0)
        and (last_candle["RSI_3_1h"] < 40.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 40.0)
      ):
        return True, f"exit_{mode_name}_d_11_83"
      elif (
        (last_candle["RSI_3"] > 94.0)
        and (last_candle["WILLR_14"] > -1.0)
        and (last_candle["RSI_3_4h"] < 30.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 20.0)
      ):
        return True, f"exit_{mode_name}_d_11_84"
      elif (
        (last_candle["RSI_3"] > 92.0)
        and (last_candle["WILLR_14"] > -4.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (last_candle["RSI_3_4h"] < 40.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_11_85"
      elif (
        (last_candle["RSI_3"] > 98.0)
        and (last_candle["RSI_14_4h"] > 80.0)
        and (last_candle["ROC_2_1h"] < -5.0)
        and (last_candle["ROC_9_1h"] > 5.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_11_86"
      elif (
        (last_candle["RSI_3"] > 70.0)
        and (last_candle["RSI_14"] < 40.0)
        and (last_candle["RSI_3_1h"] < 45.0)
        and (last_candle["RSI_3_4h"] < 50.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_11_87"
      elif (
        (last_candle["RSI_3"] > 92.0)
        and (last_candle["WILLR_14"] > -16.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 40.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
        and (last_candle["change_pct_1h"] < -2.0)
      ):
        return True, f"exit_{mode_name}_d_11_88"
      elif (
        (last_candle["RSI_3"] > 82.0)
        and (last_candle["RSI_14"] < 36.0)
        and (last_candle["ROC_9_1h"] < -5.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 25.0))
      ):
        return True, f"exit_{mode_name}_d_11_89"
      elif (
        (last_candle["RSI_3"] > 96.0)
        and (last_candle["WILLR_14"] > -25.0)
        and (last_candle["RSI_3_1h"] < 50.0)
        and (last_candle["RSI_3_4h"] < 30.0)
        and (last_candle["AROONU_14_4h"] > 50.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 40.0))
      ):
        return True, f"exit_{mode_name}_d_11_90"
      elif (
        (last_candle["RSI_3"] > 76.0)
        and (last_candle["RSI_14"] < 42.0)
        and (last_candle["RSI_3_1h"] < 25.0)
        and (last_candle["RSI_3_4h"] < 25.0)
        and (last_candle["AROONU_14_4h"] > 50.0)
        and (
          isinstance(last_candle["STOCHRSIk_14_14_3_3_1d"], np.float64)
          and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 50.0)
        )
      ):
        return True, f"exit_{mode_name}_d_11_91"
      elif (
        (last_candle["RSI_3"] > 84.0)
        and (last_candle["RSI_14"] < 44.0)
        and (last_candle["RSI_3_1h"] < 40.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 25.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -25.0))
      ):
        return True, f"exit_{mode_name}_d_11_92"
      elif (
        (last_candle["RSI_3"] > 76.0)
        and (last_candle["RSI_14"] < 46.0)
        and (last_candle["RSI_3_15m"] < 50.0)
        and (last_candle["AROONU_14_1h"] > 75.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 70.0)
        and (last_candle["AROONU_14_4h"] > 50.0)
        and (
          isinstance(last_candle["STOCHRSIk_14_14_3_3_1d"], np.float64)
          and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 90.0)
        )
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 30.0))
      ):
        return True, f"exit_{mode_name}_d_11_93"
      elif (
        (last_candle["RSI_3"] > 84.0)
        and (last_candle["RSI_14"] < 46.0)
        and (last_candle["RSI_3_1h"] < 25.0)
        and (last_candle["RSI_3_4h"] < 45.0)
        and (last_candle["AROONU_14_1h"] > 75.0)
        and (
          isinstance(last_candle["STOCHRSIk_14_14_3_3_1d"], np.float64)
          and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 90.0)
        )
      ):
        return True, f"exit_{mode_name}_d_11_94"
      elif (
        (last_candle["RSI_3"] > 88.0)
        and (last_candle["WILLR_14"] > -8.0)
        and (last_candle["RSI_3_1h"] < 45.0)
        and (last_candle["RSI_3_4h"] < 40.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 10.0)
        and (isinstance(last_candle["AROONU_14_1d"], np.float64) and (last_candle["AROONU_14_1d"] > 75.0))
      ):
        return True, f"exit_{mode_name}_d_11_95"
      elif (
        (last_candle["RSI_3"] > 66.0)
        and (last_candle["RSI_14"] < 42.0)
        and (last_candle["RSI_3_1h"] < 45.0)
        and (last_candle["RSI_3_1d"] < 45.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_11_96"
      elif (
        (last_candle["RSI_3"] > 88.0)
        and (last_candle["RSI_14"] < 42.0)
        and (last_candle["RSI_3_1h"] < 35.0)
        and (last_candle["AROONU_14_4h"] > 50.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 30.0)
      ):
        return True, f"exit_{mode_name}_d_11_97"
      elif (
        (last_candle["RSI_3"] > 94.0)
        and (last_candle["RSI_3_15m"] > 76.0)
        and (last_candle["RSI_3_1h"] < 60.0)
        and (last_candle["RSI_3_4h"] < 60.0)
        and (last_candle["RSI_3_1d"] > 80.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_11_98"
      elif (
        (last_candle["RSI_3"] > 64.0)
        and (last_candle["RSI_14"] < 48.0)
        and (last_candle["RSI_3_1h"] < 65.0)
        and (last_candle["RSI_3_4h"] < 60.0)
        and (last_candle["AROONU_14_4h"] > 50.0)
        and (last_candle["STOCHk_14_3_3_4h"] > 40.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 80.0))
      ):
        return True, f"exit_{mode_name}_d_11_99"
      elif (
        (last_candle["RSI_3"] > 99.0)
        and (last_candle["RSI_14"] > 80.0)
        and (last_candle["RSI_3_15m"] > 70.0)
        and (last_candle["RSI_3_4h"] < 80.0)
      ):
        return True, f"exit_{mode_name}_d_11_100"
      elif (
        (last_candle["RSI_3"] > 88.0)
        and (last_candle["WILLR_14"] > -12.0)
        and (last_candle["RSI_3_1h"] < 50.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 40.0)
        and (isinstance(last_candle["ROC_9_4h"], np.float64) and (last_candle["ROC_9_4h"] > 40.0))
      ):
        return True, f"exit_{mode_name}_d_11_101"
      elif (
        (last_candle["RSI_3"] > 72.0)
        and (last_candle["RSI_14"] < 44.0)
        and (last_candle["RSI_3_1h"] < 60.0)
        and (last_candle["RSI_3_4h"] < 40.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 30.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 40.0))
      ):
        return True, f"exit_{mode_name}_d_11_102"
      elif (
        (last_candle["RSI_3"] > 82.0)
        and (last_candle["RSI_14"] < 52.0)
        and (last_candle["RSI_3_1h"] < 60.0)
        and (last_candle["RSI_14_4h"] > 70.0)
        and (isinstance(last_candle["ROC_9_4h"], np.float64) and (last_candle["ROC_9_4h"] > 80.0))
      ):
        return True, f"exit_{mode_name}_d_11_103"
      elif (
        (last_candle["RSI_3"] > 68.0)
        and (last_candle["RSI_14"] < 44.0)
        and (last_candle["RSI_3_1h"] < 60.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 40.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 90.0)
        and (last_candle["ROC_9_4h"] > 40.0)
      ):
        return True, f"exit_{mode_name}_d_11_104"
      elif (
        (last_candle["RSI_3"] > 82.0)
        and (last_candle["RSI_14"] < 44.0)
        and (last_candle["RSI_3_15m"] < 55.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 90.0)
        and (last_candle["ROC_9_4h"] > 25.0)
      ):
        return True, f"exit_{mode_name}_d_11_105"
      elif (
        (last_candle["RSI_3"] > 76.0)
        and (last_candle["RSI_14"] < 44.0)
        and (last_candle["RSI_3_1h"] < 50.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
        and (last_candle["RSI_14_4h"] > 70.0)
        and (last_candle["ROC_9_4h"] > 40.0)
      ):
        return True, f"exit_{mode_name}_d_11_106"
      elif (
        (last_candle["RSI_3"] > 78.0)
        and (last_candle["RSI_14"] < 44.0)
        and (last_candle["RSI_3_1h"] < 50.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 70.0)
        and (last_candle["RSI_14_4h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_11_107"
      elif (
        (last_candle["RSI_3"] > 60.0)
        and (last_candle["RSI_14"] < 44.0)
        and (last_candle["RSI_3_1h"] < 60.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 80.0)
      ):
        return True, f"exit_{mode_name}_d_11_108"
      elif (
        (last_candle["RSI_3"] > 80.0)
        and (last_candle["WILLR_14"] > -4.0)
        and (last_candle["RSI_3_1h"] < 50.0)
        and (last_candle["RSI_3_4h"] < 20.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 50.0))
      ):
        return True, f"exit_{mode_name}_d_11_109"
      elif (
        (last_candle["RSI_3"] > 76.0)
        and (last_candle["RSI_3_4h"] < 65.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
        and (last_candle["ROC_9_4h"] > 25.0)
      ):
        return True, f"exit_{mode_name}_d_11_110"
      elif (
        (last_candle["RSI_3"] > 54.0)
        and (last_candle["RSI_14"] < 40.0)
        and (last_candle["RSI_3_1h"] < 50.0)
        and (last_candle["RSI_14_4h"] > 70.0)
        and (last_candle["AROONU_14_1h"] > 75.0)
        and (last_candle["AROONU_14_4h"] > 75.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 20.0))
      ):
        return True, f"exit_{mode_name}_d_11_111"
      elif (
        (last_candle["RSI_3"] > 84.0)
        and (last_candle["WILLR_14"] > -15.0)
        and (last_candle["RSI_14"] < 48.0)
        and (last_candle["RSI_3_1h"] < 35.0)
        and (last_candle["RSI_3_4h"] < 35.0)
        and (last_candle["RSI_3_1d"] < 60.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 30.0))
      ):
        return True, f"exit_{mode_name}_d_11_112"
      elif (
        (last_candle["RSI_3"] > 88.0)
        and (last_candle["WILLR_14"] > -1.0)
        and (last_candle["RSI_3_1d"] < 30.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
        and (isinstance(last_candle["ROC_9_4h"], np.float64) and (last_candle["ROC_9_4h"] > 10.0))
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -10.0))
      ):
        return True, f"exit_{mode_name}_d_11_113"
      elif (
        (last_candle["RSI_3"] > 88.0)
        and (last_candle["RSI_14"] < 46.0)
        and (last_candle["RSI_3_1h"] < 20.0)
        and (last_candle["RSI_3_4h"] < 30.0)
        and (last_candle["RSI_3_1d"] < 30.0)
      ):
        return True, f"exit_{mode_name}_d_11_114"
      elif (
        (last_candle["RSI_3"] > 82.0)
        and (last_candle["RSI_14"] < 44.0)
        and (last_candle["RSI_3_15m"] < 30.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_11_115"
      elif (
        (last_candle["RSI_3"] > 94.0)
        and (last_candle["RSI_3_1h"] < 15.0)
        and (last_candle["RSI_3_4h"] < 40.0)
        and (last_candle["AROONU_14_4h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_11_116"
      elif (
        (last_candle["RSI_3"] > 90.0)
        and (last_candle["RSI_3_1h"] < 50.0)
        and (last_candle["AROONU_14_1h"] > 80.0)
        and (last_candle["AROONU_14_4h"] > 80.0)
      ):
        return True, f"exit_{mode_name}_d_11_117"
      elif (
        (last_candle["RSI_3"] > 94.0)
        and (last_candle["RSI_3_1h"] < 20.0)
        and (last_candle["RSI_3_4h"] < 60.0)
        and (last_candle["AROONU_14_4h"] > 40.0)
      ):
        return True, f"exit_{mode_name}_d_11_118"
      elif (
        (last_candle["RSI_3"] > 90.0)
        and (last_candle["WILLR_14"] > -20.0)
        and (last_candle["RSI_3_1h"] < 60.0)
        and (last_candle["RSI_3_4h"] < 60.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 40.0)
      ):
        return True, f"exit_{mode_name}_d_11_119"
      elif (
        (last_candle["RSI_3"] > 58.0)
        and (last_candle["RSI_14"] < 44.0)
        and (last_candle["RSI_3_1h"] < 40.0)
        and (last_candle["AROONU_14_4h"] > 75.0)
      ):
        return True, f"exit_{mode_name}_d_11_120"
      elif (
        (last_candle["RSI_3"] > 64.0)
        and (last_candle["RSI_14"] < 42.0)
        and (last_candle["RSI_3_1h"] < 50.0)
        and (last_candle["RSI_14_4h"] > 85.0)
      ):
        return True, f"exit_{mode_name}_d_11_121"
      elif (
        (last_candle["RSI_3"] > 62.0)
        and (last_candle["RSI_14"] < 40.0)
        and (last_candle["RSI_3_4h"] < 30.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_11_122"
      elif (
        (last_candle["RSI_3"] > 92.0)
        and (last_candle["WILLR_14"] > -1.0)
        and (last_candle["RSI_3_1h"] < 10.0)
        and (last_candle["RSI_3_1d"] < 30.0)
      ):
        return True, f"exit_{mode_name}_d_11_123"
      elif (
        (last_candle["RSI_3"] > 92.0)
        and (last_candle["RSI_3_1h"] < 15.0)
        and (
          isinstance(last_candle["STOCHRSIk_14_14_3_3_1d"], np.float64)
          and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 80.0)
        )
      ):
        return True, f"exit_{mode_name}_d_11_124"
      elif (
        (last_candle["RSI_3"] > 80.0)
        and (last_candle["WILLR_14"] > -1.0)
        and (last_candle["RSI_3_1h"] < 10.0)
        and (last_candle["RSI_3_4h"] < 40.0)
        and (last_candle["RSI_3_1d"] < 40.0)
        and (last_candle["close"] < (last_candle["high_max_30_1d"] * 0.50))
      ):
        return True, f"exit_{mode_name}_d_11_125"
      elif (
        (last_candle["RSI_3"] > 94.0)
        and (last_candle["RSI_3_1h"] < 15.0)
        and (last_candle["RSI_3_4h"] < 40.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_11_126"
      elif (
        (last_candle["RSI_3"] > 94.0)
        and (last_candle["RSI_3_1h"] < 10.0)
        and (last_candle["RSI_3_4h"] < 30.0)
        and (last_candle["RSI_3_1d"] < 40.0)
      ):
        return True, f"exit_{mode_name}_d_11_127"
      elif (last_candle["RSI_3"] > 98.0) and (last_candle["RSI_3_4h"] < 30.0) and (last_candle["AROONU_14_4h"] > 85.0):
        return True, f"exit_{mode_name}_d_11_128"
      elif (
        (last_candle["RSI_3"] > 90.0)
        and (last_candle["RSI_3_4h"] < 25.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 80.0))
      ):
        return True, f"exit_{mode_name}_d_11_129"
      elif (
        (last_candle["RSI_3"] > 78.0)
        and (last_candle["RSI_14_1h"] > 65.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 80.0)
        and (last_candle["CCI_20_change_pct_1h"] < -0.0)
      ):
        return True, f"exit_{mode_name}_d_11_130"
      elif (
        (last_candle["RSI_14"] < 34.0)
        and (last_candle["RSI_3_1h"] < 20.0)
        and (last_candle["RSI_3_4h"] < 30.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_11_131"
      elif (
        (last_candle["RSI_3"] > 84.0)
        and (last_candle["RSI_3_1h"] < 35.0)
        and (last_candle["RSI_3_4h"] < 35.0)
        and (last_candle["AROONU_14_1h"] > 50.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 40.0)
      ):
        return True, f"exit_{mode_name}_d_11_132"
      elif (
        (last_candle["RSI_3"] > 84.0)
        and (last_candle["AROONU_14_15m"] > 75.0)
        and (last_candle["AROONU_14_1h"] > 75.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 25.0))
      ):
        return True, f"exit_{mode_name}_d_11_133"
    elif current_profit >= 0.2:
      if (
        (last_candle["WILLR_14"] > -1.0)
        and (last_candle["RSI_14"] > 78.0)
        and (
          isinstance(last_candle["EMA_200_1h"], np.float64) and (last_candle["EMA_12_1h"] < last_candle["EMA_200_1h"])
        )
        and (
          isinstance(last_candle["EMA_200_4h"], np.float64) and (last_candle["EMA_12_4h"] < last_candle["EMA_200_4h"])
        )
        and (last_candle["KST_10_15_20_30_10_10_10_15_1h"] < last_candle["KSTs_9_1h"])
        and (last_candle["KST_10_15_20_30_10_10_10_15_4h"] < last_candle["KSTs_9_4h"])
      ):
        return True, f"exit_{mode_name}_d_12_1"
      elif (
        (last_candle["WILLR_14"] > -1.0)
        and (last_candle["RSI_14"] > 78.0)
        and (last_candle["CMF_20_1h"] < -0.0)
        and (
          isinstance(last_candle["EMA_200_1h"], np.float64) and (last_candle["EMA_12_1h"] < last_candle["EMA_200_1h"])
        )
        and (
          isinstance(last_candle["EMA_200_4h"], np.float64) and (last_candle["EMA_12_4h"] < last_candle["EMA_200_4h"])
        )
      ):
        return True, f"exit_{mode_name}_d_12_2"
      elif (
        (last_candle["WILLR_14"] > -1.0)
        and (last_candle["STOCHRSIk_14_14_3_3"] > 99.0)
        and (last_candle["CMF_20_1h"] < -0.0)
        and (last_candle["CMF_20_4h"] < -0.0)
        and (
          (last_candle["STOCHRSIk_14_14_3_3_4h"] > 20.0) and (last_candle["STOCHRSIk_14_14_3_3_change_pct_4h"] < -10.0)
        )
      ):
        return True, f"exit_{mode_name}_d_12_3"
      elif (
        (last_candle["WILLR_14"] > -1.0)
        and (last_candle["RSI_14"] > 80.0)
        and (last_candle["STOCHRSIk_14_14_3_3"] > 95.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 70.0)
        and (
          isinstance(last_candle["EMA_200_1h"], np.float64) and (last_candle["EMA_12_1h"] < last_candle["EMA_200_1h"])
        )
        and (
          isinstance(last_candle["EMA_200_4h"], np.float64) and (last_candle["EMA_12_4h"] < last_candle["EMA_200_4h"])
        )
      ):
        return True, f"exit_{mode_name}_d_12_4"
      elif (
        (last_candle["WILLR_14"] > -1.0)
        and (last_candle["RSI_14"] > 78.0)
        and (last_candle["ROC_9_1h"] < -5.0)
        and (last_candle["ROC_9_4h"] < -5.0)
      ):
        return True, f"exit_{mode_name}_d_12_5"
      elif (
        (last_candle["RSI_3"] > 70.0)
        and (last_candle["STOCHRSIk_14_14_3_3"] > 70.0)
        and (last_candle["RSI_14"] < 40.0)
        and (last_candle["ROC_9_1h"] < -10.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 50.0))
      ):
        return True, f"exit_{mode_name}_d_12_6"
      elif (
        (last_candle["RSI_14"] < 50.0)
        and (last_candle["STOCHRSIk_14_14_3_3"] > 95.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -40.0))
      ):
        return True, f"exit_{mode_name}_d_12_7"
      elif (
        (last_candle["WILLR_14"] > -1.0)
        and (last_candle["STOCHRSIk_14_14_3_3"] > 99.0)
        and (last_candle["CMF_20_1h"] < -0.1)
        and (last_candle["CMF_20_4h"] < -0.1)
        and (last_candle["change_pct_1d"] < -5.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 15.0))
      ):
        return True, f"exit_{mode_name}_d_12_8"
      elif (
        (last_candle["WILLR_14"] > -1.0)
        and (last_candle["RSI_3"] > 99.0)
        and (last_candle["change_pct_4h"] < -5.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 30.0))
      ):
        return True, f"exit_{mode_name}_d_12_9"
      elif (
        (last_candle["WILLR_14"] > -1.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["ROC_9_1h"] < -10.0)
        and (last_candle["ROC_9_4h"] < -10.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 10.0))
      ):
        return True, f"exit_{mode_name}_d_12_10"
      elif (
        (last_candle["RSI_3"] > 99.0)
        and (last_candle["RSI_14"] < 45.0)
        and (last_candle["ROC_9_15m"] < -10.0)
        and (last_candle["ROC_9_1h"] < -10.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -20.0))
      ):
        return True, f"exit_{mode_name}_d_12_11"
      elif (
        (last_candle["RSI_3"] > 99.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_4h"] < 10.0)
        and (last_candle["ROC_9_1h"] < -20.0)
        and (last_candle["ROC_9_4h"] < -20.0)
      ):
        return True, f"exit_{mode_name}_d_12_12"
      elif (last_candle["RSI_3"] > 99.0) and (last_candle["RSI_3_4h"] < 5.0) and (last_candle["ROC_9_4h"] < -25.0):
        return True, f"exit_{mode_name}_d_12_13"
      elif (
        (last_candle["RSI_3"] > 99.0)
        and (last_candle["WILLR_14"] > -1.0)
        and (last_candle["RSI_3_4h"] < 5.0)
        and (last_candle["AROONU_14_4h"] > 25.0)
      ):
        return True, f"exit_{mode_name}_d_12_14"
      elif (last_candle["RSI_3"] > 99.0) and (last_candle["RSI_14"] > 75.0) and (last_candle["ROC_9_4h"] < -30.0):
        return True, f"exit_{mode_name}_d_12_15"
      elif (
        (last_candle["RSI_3"] > 99.0)
        and (last_candle["AROONU_14_4h"] > 25.0)
        and (last_candle["ROC_9_4h"] < -25.0)
        and (last_candle["AROONU_14_1d"] > 50.0)
        and (last_candle["change_pct_1d"] < -15.0)
      ):
        return True, f"exit_{mode_name}_d_12_16"
      elif (
        (last_candle["RSI_3"] > 99.0)
        and (last_candle["WILLR_14"] > -1.0)
        and (last_candle["RSI_3_1h"] < 10.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 90.0)
        and (last_candle["ROC_9_4h"] > 30.0)
      ):
        return True, f"exit_{mode_name}_d_12_17"
      elif (
        (last_candle["RSI_3"] > 99.0)
        and (last_candle["RSI_14"] > 80.0)
        and (last_candle["RSI_3_4h"] < 20.0)
        and (last_candle["ROC_2_1d"] < -50.0)
      ):
        return True, f"exit_{mode_name}_d_12_18"
      elif (
        (last_candle["RSI_3"] > 99.0)
        and (last_candle["RSI_14"] > 78.0)
        and (last_candle["RSI_3_4h"] < 10.0)
        and (
          isinstance(last_candle["STOCHRSIk_14_14_3_3_1d"], np.float64)
          and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 70.0)
        )
      ):
        return True, f"exit_{mode_name}_d_12_19"
      elif (
        (last_candle["RSI_3"] > 90.0)
        and (last_candle["RSI_14"] < 40.0)
        and (last_candle["RSI_3_1h"] < 10.0)
        and (last_candle["AROONU_14_1h"] > 25.0)
      ):
        return True, f"exit_{mode_name}_d_12_20"
      elif (
        (last_candle["RSI_3"] > 99.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_1h"] < 20.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 90.0)
      ):
        return True, f"exit_{mode_name}_d_12_21"
      elif (
        (last_candle["RSI_3"] > 99.0)
        and (last_candle["WILLR_14"] > -1.0)
        and (last_candle["change_pct_4h"] < -5.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -30.0))
      ):
        return True, f"exit_{mode_name}_d_12_22"
      elif (
        (last_candle["RSI_3"] > 99.0)
        and (last_candle["WILLR_14"] > -1.0)
        and (last_candle["RSI_3_1h"] < 15.0)
        and (last_candle["RSI_3_1d"] < 5.0)
      ):
        return True, f"exit_{mode_name}_d_12_23"
      elif (
        (last_candle["RSI_3"] > 98.0)
        and (last_candle["RSI_14"] > 78.0)
        and (last_candle["WILLR_14"] > -1.0)
        and (last_candle["RSI_3_4h"] < 30.0)
        and (last_candle["AROONU_14_4h"] > 75.0)
      ):
        return True, f"exit_{mode_name}_d_12_24"
      elif (
        (last_candle["RSI_3"] > 99.0)
        and (last_candle["WILLR_14"] > -1.0)
        and (last_candle["RSI_3_4h"] < 10.0)
        and (last_candle["ROC_9_4h"] < -15.0)
        and (
          isinstance(last_candle["STOCHRSIk_14_14_3_3_1d"], np.float64)
          and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 50.0)
        )
      ):
        return True, f"exit_{mode_name}_d_12_25"
      elif (
        (last_candle["RSI_3"] > 99.0)
        and (last_candle["WILLR_14"] > -1.0)
        and (last_candle["RSI_3_4h"] < 15.0)
        and (last_candle["ROC_9_4h"] < -20.0)
      ):
        return True, f"exit_{mode_name}_d_12_26"
      elif (
        (last_candle["RSI_3"] > 99.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_1h"] < 20.0)
        and (last_candle["RSI_3_4h"] < 20.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 20.0)
      ):
        return True, f"exit_{mode_name}_d_12_27"
      elif (
        (last_candle["RSI_3"] > 95.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_15m"] < 10.0)
        and (last_candle["ROC_9_4h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_12_28"
      elif (
        (last_candle["RSI_3"] > 99.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_1h"] < 20.0)
        and (last_candle["RSI_3_4h"] < 20.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 30.0)
      ):
        return True, f"exit_{mode_name}_d_12_29"
      elif (
        (last_candle["RSI_3"] > 99.0)
        and (last_candle["RSI_3_1h"] < 25.0)
        and (last_candle["RSI_3_4h"] < 10.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 70.0)
      ):
        return True, f"exit_{mode_name}_d_12_30"
      elif (
        (last_candle["RSI_3"] > 95.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_1h"] < 15.0)
        and (last_candle["RSI_3_4h"] < 15.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 25.0)
      ):
        return True, f"exit_{mode_name}_d_12_31"
      elif (
        (last_candle["RSI_3"] > 99.0)
        and (last_candle["RSI_3_1h"] < 15.0)
        and (last_candle["ROC_2_4h"] < -30.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 30.0)
      ):
        return True, f"exit_{mode_name}_d_12_32"
      elif (
        (last_candle["RSI_3"] > 99.0)
        and (last_candle["WILLR_14"] > -1.0)
        and (last_candle["ROC_2_1h"] < -10.0)
        and (last_candle["ROC_9_1h"] > 30.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_12_33"
      elif (
        (last_candle["RSI_3"] > 65.0)
        and (last_candle["RSI_3_15m"] < 30.0)
        and (last_candle["RSI_14_1h"] > 80.0)
        and (last_candle["ROC_9_1h"] > 40.0)
      ):
        return True, f"exit_{mode_name}_d_12_34"
      elif (
        (last_candle["RSI_3"] > 94.0)
        and (last_candle["WILLR_14"] > -2.0)
        and (last_candle["RSI_3_1d"] < 25.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 75.0)
      ):
        return True, f"exit_{mode_name}_d_12_35"
      elif (
        (last_candle["RSI_3"] > 99.0)
        and (last_candle["WILLR_14"] > -1.0)
        and (last_candle["ROC_9_4h"] < -25.0)
        and (last_candle["RSI_3_1d"] < 25.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_12_36"
      elif (
        (last_candle["RSI_3"] > 88.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_1h"] < 20.0)
        and (last_candle["RSI_3_1d"] < 25.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_12_37"
      elif (
        (last_candle["RSI_3"] > 99.0)
        and (last_candle["WILLR_14"] > -1.0)
        and (last_candle["RSI_3_4h"] < 10.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 20.0)
      ):
        return True, f"exit_{mode_name}_d_12_38"
      elif (
        (last_candle["RSI_3"] > 98.0)
        and (last_candle["WILLR_14"] > -2.0)
        and (last_candle["CMF_20_4h"] < -0.0)
        and (last_candle["RSI_3_4h"] < 10.0)
      ):
        return True, f"exit_{mode_name}_d_12_39"
      elif (
        (last_candle["RSI_3"] > 98.0)
        and (last_candle["WILLR_14"] > -2.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 30.0)
        and (
          isinstance(last_candle["STOCHRSIk_14_14_3_3_1d"], np.float64)
          and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 90.0)
        )
      ):
        return True, f"exit_{mode_name}_d_12_40"
      elif (
        (last_candle["RSI_3"] > 98.0)
        and (last_candle["WILLR_14"] > -2.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 25.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 50.0))
      ):
        return True, f"exit_{mode_name}_d_12_41"
      elif (
        (last_candle["RSI_3"] > 98.0)
        and (last_candle["WILLR_14"] > -10.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 30.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 40.0))
        and (
          isinstance(last_candle["STOCHRSIk_14_14_3_3_1d"], np.float64)
          and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 70.0)
        )
      ):
        return True, f"exit_{mode_name}_d_12_42"
      elif (
        (last_candle["RSI_3"] > 95.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_1h"] < 15.0)
        and (last_candle["RSI_3_4h"] < 40.0)
        and (
          isinstance(last_candle["STOCHRSIk_14_14_3_3_1d"], np.float64)
          and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 90.0)
        )
      ):
        return True, f"exit_{mode_name}_d_12_43"
      elif (
        (last_candle["RSI_3"] > 85.0)
        and (last_candle["WILLR_14"] > -2.0)
        and (last_candle["RSI_3_4h"] < 30.0)
        and (last_candle["RSI_3_1d"] < 25.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -30.0))
      ):
        return True, f"exit_{mode_name}_d_12_44"
      elif (last_candle["RSI_3"] > 99.0) and (last_candle["WILLR_14"] > -1.0) and (last_candle["RSI_3_1h"] < 10.0):
        return True, f"exit_{mode_name}_d_12_45"
      elif (
        (last_candle["RSI_3"] > 96.0)
        and (last_candle["RSI_3_1h"] < 15.0)
        and (last_candle["RSI_3_4h"] < 10.0)
        and (last_candle["ROC_2_1d"] < -20.0)
      ):
        return True, f"exit_{mode_name}_d_12_46"
      elif (
        (last_candle["RSI_3"] > 98.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 80.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 40.0)
        and (last_candle["change_pct_1d"] < -5.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -5.0))
      ):
        return True, f"exit_{mode_name}_d_12_47"
      elif (
        (last_candle["RSI_3"] > 80.0)
        and (last_candle["RSI_14"] < 38.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (last_candle["RSI_3_4h"] < 20.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_12_48"
      elif (
        (last_candle["RSI_3"] > 98.0)
        and (last_candle["WILLR_14"] > -2.0)
        and (last_candle["RSI_3_4h"] < 20.0)
        and (last_candle["change_pct_1d"] < -5.0)
        and (
          isinstance(last_candle["STOCHRSIk_14_14_3_3_1d"], np.float64)
          and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 50.0)
        )
      ):
        return True, f"exit_{mode_name}_d_12_49"
      elif (
        (last_candle["RSI_3"] > 90.0)
        and (last_candle["WILLR_14"] > -2.0)
        and (last_candle["RSI_3_1d"] < 10.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 90.0)
      ):
        return True, f"exit_{mode_name}_d_12_50"
      elif (
        (last_candle["RSI_3"] > 72.0)
        and (last_candle["RSI_14"] < 40.0)
        and (last_candle["RSI_3_4h"] < 20.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_12_51"
      elif (
        (last_candle["RSI_3"] > 86.0)
        and (last_candle["RSI_14"] > 66.0)
        and (last_candle["WILLR_14"] > -10.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 70.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -15.0))
      ):
        return True, f"exit_{mode_name}_d_12_52"
      elif (
        (last_candle["RSI_3"] > 70.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["WILLR_14"] > -25.0)
        and (last_candle["RSI_3_1h"] < 20.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
        and (
          isinstance(last_candle["STOCHRSIk_14_14_3_3_1d"], np.float64)
          and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 50.0)
        )
      ):
        return True, f"exit_{mode_name}_d_12_53"
      elif (
        (last_candle["RSI_3"] > 84.0)
        and (last_candle["RSI_14"] < 40.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
        and (last_candle["ROC_9_4h"] < -10.0)
        and (last_candle["change_pct_1d"] < -10.0)
      ):
        return True, f"exit_{mode_name}_d_12_54"
      elif (
        (last_candle["RSI_3"] > 99.0)
        and (last_candle["WILLR_14"] > -8.0)
        and (last_candle["ROC_9_4h"] < -5.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 10.0))
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_12_55"
      elif (
        (last_candle["RSI_3"] > 95.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (last_candle["RSI_3_4h"] < 25.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -30.0))
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 10.0)
      ):
        return True, f"exit_{mode_name}_d_12_56"
      elif (
        (last_candle["RSI_3"] > 50.0)
        and (last_candle["RSI_14"] < 30.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -30.0))
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 70.0)
      ):
        return True, f"exit_{mode_name}_d_12_57"
      elif (
        (last_candle["RSI_3"] > 99.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (last_candle["RSI_3_4h"] < 30.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -15.0))
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_12_58"
      elif (
        (last_candle["RSI_3"] > 95.0)
        and (last_candle["WILLR_14"] > -6.0)
        and (last_candle["RSI_3_4h"] < 25.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -15.0))
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 40.0)
      ):
        return True, f"exit_{mode_name}_d_12_59"
      elif (
        (last_candle["RSI_3"] > 90.0)
        and (last_candle["RSI_14"] < 34.0)
        and (last_candle["RSI_14_4h"] > 65.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_12_60"
      elif (
        (last_candle["RSI_3"] > 98.0)
        and (last_candle["WILLR_14"] > -5.0)
        and (last_candle["RSI_3_4h"] < 10.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 30.0)
      ):
        return True, f"exit_{mode_name}_d_12_61"
      elif (
        (last_candle["RSI_3"] > 92.0)
        and (last_candle["WILLR_14"] > -2.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (last_candle["RSI_3_4h"] < 20.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 20.0))
        and (last_candle["change_pct_1d"] < -5.0)
      ):
        return True, f"exit_{mode_name}_d_12_62"
      elif (
        (last_candle["RSI_3"] > 74.0)
        and (last_candle["RSI_3_1d"] < 25.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 80.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 30.0)
      ):
        return True, f"exit_{mode_name}_d_12_63"
      elif (
        (last_candle["RSI_3"] > 94.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (last_candle["RSI_3_4h"] < 30.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 30.0))
      ):
        return True, f"exit_{mode_name}_d_12_64"
      elif (
        (last_candle["RSI_3"] > 74.0)
        and (last_candle["RSI_14"] < 36.0)
        and (last_candle["RSI_3_1h"] < 20.0)
        and (last_candle["RSI_3_4h"] < 15.0)
      ):
        return True, f"exit_{mode_name}_d_12_65"
      elif (
        (last_candle["RSI_3"] > 88.0)
        and (last_candle["RSI_14"] < 42.0)
        and (last_candle["RSI_3_1h"] < 20.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_12_66"
      elif (
        (last_candle["RSI_3"] > 50.0)
        and (last_candle["RSI_14"] < 36.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 80.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -25.0))
      ):
        return True, f"exit_{mode_name}_d_12_67"
      elif (
        (last_candle["RSI_3"] > 90.0)
        and (last_candle["RSI_14"] < 42.0)
        and (last_candle["RSI_3_1h"] < 25.0)
        and (last_candle["ROC_2_4h"] < -30.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 25.0)
      ):
        return True, f"exit_{mode_name}_d_12_68"
      elif (
        (last_candle["RSI_3"] > 99.0)
        and (last_candle["ROC_9_4h"] > 20.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
        and (last_candle["change_pct_4h"] < -5.0)
      ):
        return True, f"exit_{mode_name}_d_12_69"
      elif (
        (last_candle["RSI_3"] > 72.0)
        and (last_candle["RSI_14"] < 34.0)
        and (last_candle["RSI_3_1h"] < 25.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 20.0)
      ):
        return True, f"exit_{mode_name}_d_12_70"
      elif (
        (last_candle["RSI_3"] > 70.0)
        and (last_candle["RSI_14"] < 38.0)
        and (last_candle["RSI_3_4h"] < 25.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 20.0)
      ):
        return True, f"exit_{mode_name}_d_12_71"
      elif (
        (last_candle["RSI_3"] > 84.0)
        and (last_candle["RSI_14"] < 36.0)
        and (last_candle["RSI_3_1h"] < 10.0)
        and (last_candle["AROONU_14_4h"] > 25.0)
      ):
        return True, f"exit_{mode_name}_d_12_72"
      elif (
        (last_candle["RSI_3"] > 84.0)
        and (last_candle["RSI_3_1h"] < 25.0)
        and (last_candle["RSI_3_4h"] < 15.0)
        and (last_candle["ROC_9_4h"] < -20.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -25.0))
      ):
        return True, f"exit_{mode_name}_d_12_73"
      elif (
        (last_candle["RSI_3"] > 99.0)
        and (last_candle["WILLR_14"] > -10.0)
        and (last_candle["RSI_3_4h"] < 25.0)
        and (last_candle["RSI_3_1d"] < 25.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_12_74"
      elif (
        (last_candle["RSI_3"] > 98.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (last_candle["RSI_3_4h"] < 20.0)
        and (
          isinstance(last_candle["STOCHRSIk_14_14_3_3_1d"], np.float64)
          and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 50.0)
        )
      ):
        return True, f"exit_{mode_name}_d_12_75"
      elif (
        (last_candle["RSI_3"] > 74.0)
        and (last_candle["RSI_14"] < 44.0)
        and (last_candle["ROC_9_1h"] > 80.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 80.0)
      ):
        return True, f"exit_{mode_name}_d_12_76"
      elif (
        (last_candle["RSI_3"] > 82.0)
        and (last_candle["RSI_14"] < 40.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 50.0))
      ):
        return True, f"exit_{mode_name}_d_12_77"
      elif (
        (last_candle["RSI_3"] > 92.0)
        and (last_candle["WILLR_14"] > -10.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (last_candle["RSI_3_4h"] < 20.0)
        and (last_candle["RSI_3_1d"] < 20.0)
      ):
        return True, f"exit_{mode_name}_d_12_78"
      elif (
        (last_candle["RSI_3"] > 98.0)
        and (last_candle["WILLR_14"] > -1.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (last_candle["RSI_3_4h"] < 10.0)
      ):
        return True, f"exit_{mode_name}_d_12_79"
      elif (
        (last_candle["RSI_3"] > 78.0)
        and (last_candle["RSI_14"] < 40.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 50.0))
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 25.0)
      ):
        return True, f"exit_{mode_name}_d_12_80"
      elif (
        (last_candle["RSI_3"] > 90.0)
        and (last_candle["WILLR_14"] > -4.0)
        and (last_candle["RSI_3_1h"] < 25.0)
        and (last_candle["RSI_3_4h"] < 25.0)
        and (isinstance(last_candle["RSI_14_1d"], np.float64) and (last_candle["RSI_14_1d"] > 50.0))
      ):
        return True, f"exit_{mode_name}_d_12_81"
      elif (
        (last_candle["RSI_3"] > 88.0)
        and (last_candle["WILLR_14"] > -4.0)
        and (last_candle["RSI_3_4h"] < 30.0)
        and (last_candle["RSI_3_1d"] < 15.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 40.0)
      ):
        return True, f"exit_{mode_name}_d_12_82"
      elif (
        (last_candle["RSI_3"] > 78.0)
        and (last_candle["RSI_14"] < 40.0)
        and (last_candle["RSI_3_1h"] < 40.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 40.0)
      ):
        return True, f"exit_{mode_name}_d_12_83"
      elif (
        (last_candle["RSI_3"] > 96.0)
        and (last_candle["WILLR_14"] > -1.0)
        and (last_candle["RSI_3_4h"] < 30.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 20.0)
      ):
        return True, f"exit_{mode_name}_d_12_84"
      elif (
        (last_candle["RSI_3"] > 94.0)
        and (last_candle["WILLR_14"] > -2.0)
        and (last_candle["RSI_3_1h"] < 30.0)
        and (last_candle["RSI_3_4h"] < 40.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_12_85"
      elif (
        (last_candle["RSI_3"] > 99.0)
        and (last_candle["RSI_14_4h"] > 80.0)
        and (last_candle["ROC_2_1h"] < -5.0)
        and (last_candle["ROC_9_1h"] > 5.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_12_86"
      elif (
        (last_candle["RSI_3"] > 72.0)
        and (last_candle["RSI_14"] < 38.0)
        and (last_candle["RSI_3_1h"] < 45.0)
        and (last_candle["RSI_3_4h"] < 50.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_12_87"
      elif (
        (last_candle["RSI_3"] > 94.0)
        and (last_candle["WILLR_14"] > -14.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 40.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
        and (last_candle["change_pct_1h"] < -2.0)
      ):
        return True, f"exit_{mode_name}_d_12_88"
      elif (
        (last_candle["RSI_3"] > 84.0)
        and (last_candle["RSI_14"] < 34.0)
        and (last_candle["ROC_9_1h"] < -5.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 25.0))
      ):
        return True, f"exit_{mode_name}_d_12_89"
      elif (
        (last_candle["RSI_3"] > 98.0)
        and (last_candle["WILLR_14"] > -25.0)
        and (last_candle["RSI_3_1h"] < 50.0)
        and (last_candle["RSI_3_4h"] < 30.0)
        and (last_candle["AROONU_14_4h"] > 50.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 40.0))
      ):
        return True, f"exit_{mode_name}_d_12_90"
      elif (
        (last_candle["RSI_3"] > 78.0)
        and (last_candle["RSI_14"] < 40.0)
        and (last_candle["RSI_3_1h"] < 25.0)
        and (last_candle["RSI_3_4h"] < 25.0)
        and (last_candle["AROONU_14_4h"] > 50.0)
        and (
          isinstance(last_candle["STOCHRSIk_14_14_3_3_1d"], np.float64)
          and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 50.0)
        )
      ):
        return True, f"exit_{mode_name}_d_12_91"
      elif (
        (last_candle["RSI_3"] > 86.0)
        and (last_candle["RSI_14"] < 42.0)
        and (last_candle["RSI_3_1h"] < 40.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 25.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -25.0))
      ):
        return True, f"exit_{mode_name}_d_12_92"
      elif (
        (last_candle["RSI_3"] > 78.0)
        and (last_candle["RSI_14"] < 44.0)
        and (last_candle["RSI_3_15m"] < 50.0)
        and (last_candle["AROONU_14_1h"] > 75.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 70.0)
        and (last_candle["AROONU_14_4h"] > 50.0)
        and (
          isinstance(last_candle["STOCHRSIk_14_14_3_3_1d"], np.float64)
          and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 90.0)
        )
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 30.0))
      ):
        return True, f"exit_{mode_name}_d_12_93"
      elif (
        (last_candle["RSI_3"] > 86.0)
        and (last_candle["RSI_14"] < 44.0)
        and (last_candle["RSI_3_1h"] < 25.0)
        and (last_candle["RSI_3_4h"] < 45.0)
        and (last_candle["AROONU_14_1h"] > 75.0)
        and (
          isinstance(last_candle["STOCHRSIk_14_14_3_3_1d"], np.float64)
          and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 90.0)
        )
      ):
        return True, f"exit_{mode_name}_d_12_94"
      elif (
        (last_candle["RSI_3"] > 90.0)
        and (last_candle["WILLR_14"] > -6.0)
        and (last_candle["RSI_3_1h"] < 45.0)
        and (last_candle["RSI_3_4h"] < 40.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 10.0)
        and (isinstance(last_candle["AROONU_14_1d"], np.float64) and (last_candle["AROONU_14_1d"] > 75.0))
      ):
        return True, f"exit_{mode_name}_d_12_95"
      elif (
        (last_candle["RSI_3"] > 68.0)
        and (last_candle["RSI_14"] < 40.0)
        and (last_candle["RSI_3_1h"] < 45.0)
        and (last_candle["RSI_3_1d"] < 45.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_12_96"
      elif (
        (last_candle["RSI_3"] > 90.0)
        and (last_candle["RSI_14"] < 40.0)
        and (last_candle["RSI_3_1h"] < 35.0)
        and (last_candle["AROONU_14_4h"] > 50.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 30.0)
      ):
        return True, f"exit_{mode_name}_d_12_97"
      elif (
        (last_candle["RSI_3"] > 96.0)
        and (last_candle["RSI_3_15m"] > 78.0)
        and (last_candle["RSI_3_1h"] < 60.0)
        and (last_candle["RSI_3_4h"] < 60.0)
        and (last_candle["RSI_3_1d"] > 80.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_12_98"
      elif (
        (last_candle["RSI_3"] > 66.0)
        and (last_candle["RSI_14"] < 46.0)
        and (last_candle["RSI_3_1h"] < 65.0)
        and (last_candle["RSI_3_4h"] < 60.0)
        and (last_candle["AROONU_14_4h"] > 50.0)
        and (last_candle["STOCHk_14_3_3_4h"] > 40.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 80.0))
      ):
        return True, f"exit_{mode_name}_d_12_99"
      elif (
        (last_candle["RSI_3"] > 99.0)
        and (last_candle["RSI_14"] > 82.0)
        and (last_candle["RSI_3_15m"] > 70.0)
        and (last_candle["RSI_3_4h"] < 80.0)
      ):
        return True, f"exit_{mode_name}_d_12_100"
      elif (
        (last_candle["RSI_3"] > 90.0)
        and (last_candle["WILLR_14"] > -10.0)
        and (last_candle["RSI_3_1h"] < 50.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 40.0)
        and (isinstance(last_candle["ROC_9_4h"], np.float64) and (last_candle["ROC_9_4h"] > 40.0))
      ):
        return True, f"exit_{mode_name}_d_12_101"
      elif (
        (last_candle["RSI_3"] > 74.0)
        and (last_candle["RSI_14"] < 42.0)
        and (last_candle["RSI_3_1h"] < 60.0)
        and (last_candle["RSI_3_4h"] < 40.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 30.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 40.0))
      ):
        return True, f"exit_{mode_name}_d_12_102"
      elif (
        (last_candle["RSI_3"] > 84.0)
        and (last_candle["RSI_14"] < 50.0)
        and (last_candle["RSI_3_1h"] < 60.0)
        and (last_candle["RSI_14_4h"] > 70.0)
        and (isinstance(last_candle["ROC_9_4h"], np.float64) and (last_candle["ROC_9_4h"] > 80.0))
      ):
        return True, f"exit_{mode_name}_d_12_103"
      elif (
        (last_candle["RSI_3"] > 70.0)
        and (last_candle["RSI_14"] < 42.0)
        and (last_candle["RSI_3_1h"] < 60.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 40.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 90.0)
        and (last_candle["ROC_9_4h"] > 40.0)
      ):
        return True, f"exit_{mode_name}_d_12_104"
      elif (
        (last_candle["RSI_3"] > 84.0)
        and (last_candle["RSI_14"] < 42.0)
        and (last_candle["RSI_3_15m"] < 55.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 90.0)
        and (last_candle["ROC_9_4h"] > 25.0)
      ):
        return True, f"exit_{mode_name}_d_12_105"
      elif (
        (last_candle["RSI_3"] > 78.0)
        and (last_candle["RSI_14"] < 42.0)
        and (last_candle["RSI_3_1h"] < 50.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
        and (last_candle["RSI_14_4h"] > 70.0)
        and (last_candle["ROC_9_4h"] > 40.0)
      ):
        return True, f"exit_{mode_name}_d_12_106"
      elif (
        (last_candle["RSI_3"] > 80.0)
        and (last_candle["RSI_14"] < 42.0)
        and (last_candle["RSI_3_1h"] < 50.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 70.0)
        and (last_candle["RSI_14_4h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_12_107"
      elif (
        (last_candle["RSI_3"] > 62.0)
        and (last_candle["RSI_14"] < 42.0)
        and (last_candle["RSI_3_1h"] < 60.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 80.0)
      ):
        return True, f"exit_{mode_name}_d_12_108"
      elif (
        (last_candle["RSI_3"] > 82.0)
        and (last_candle["WILLR_14"] > -2.0)
        and (last_candle["RSI_3_1h"] < 50.0)
        and (last_candle["RSI_3_4h"] < 20.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 50.0))
      ):
        return True, f"exit_{mode_name}_d_12_109"
      elif (
        (last_candle["RSI_3"] > 78.0)
        and (last_candle["RSI_3_4h"] < 65.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
        and (last_candle["ROC_9_4h"] > 25.0)
      ):
        return True, f"exit_{mode_name}_d_12_110"
      elif (
        (last_candle["RSI_3"] > 56.0)
        and (last_candle["RSI_14"] < 38.0)
        and (last_candle["RSI_3_1h"] < 50.0)
        and (last_candle["RSI_14_4h"] > 70.0)
        and (last_candle["AROONU_14_1h"] > 75.0)
        and (last_candle["AROONU_14_4h"] > 75.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 20.0))
      ):
        return True, f"exit_{mode_name}_d_12_111"
      elif (
        (last_candle["RSI_3"] > 86.0)
        and (last_candle["WILLR_14"] > -10.0)
        and (last_candle["RSI_14"] < 46.0)
        and (last_candle["RSI_3_1h"] < 35.0)
        and (last_candle["RSI_3_4h"] < 35.0)
        and (last_candle["RSI_3_1d"] < 60.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 30.0))
      ):
        return True, f"exit_{mode_name}_d_12_112"
      elif (
        (last_candle["RSI_3"] > 90.0)
        and (last_candle["WILLR_14"] > -1.0)
        and (last_candle["RSI_3_1d"] < 30.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
        and (isinstance(last_candle["ROC_9_4h"], np.float64) and (last_candle["ROC_9_4h"] > 10.0))
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] < -10.0))
      ):
        return True, f"exit_{mode_name}_d_12_113"
      elif (
        (last_candle["RSI_3"] > 90.0)
        and (last_candle["RSI_14"] < 44.0)
        and (last_candle["RSI_3_1h"] < 20.0)
        and (last_candle["RSI_3_4h"] < 30.0)
        and (last_candle["RSI_3_1d"] < 30.0)
      ):
        return True, f"exit_{mode_name}_d_12_114"
      elif (
        (last_candle["RSI_3"] > 84.0)
        and (last_candle["RSI_14"] < 42.0)
        and (last_candle["RSI_3_15m"] < 30.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_12_115"
      elif (
        (last_candle["RSI_3"] > 96.0)
        and (last_candle["RSI_3_1h"] < 15.0)
        and (last_candle["RSI_3_4h"] < 40.0)
        and (last_candle["AROONU_14_4h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_12_116"
      elif (
        (last_candle["RSI_3"] > 92.0)
        and (last_candle["RSI_3_1h"] < 50.0)
        and (last_candle["AROONU_14_1h"] > 80.0)
        and (last_candle["AROONU_14_4h"] > 80.0)
      ):
        return True, f"exit_{mode_name}_d_12_117"
      elif (
        (last_candle["RSI_3"] > 96.0)
        and (last_candle["RSI_3_1h"] < 20.0)
        and (last_candle["RSI_3_4h"] < 60.0)
        and (last_candle["AROONU_14_4h"] > 40.0)
      ):
        return True, f"exit_{mode_name}_d_12_118"
      elif (
        (last_candle["RSI_3"] > 92.0)
        and (last_candle["WILLR_14"] > -20.0)
        and (last_candle["RSI_3_1h"] < 60.0)
        and (last_candle["RSI_3_4h"] < 60.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 40.0)
      ):
        return True, f"exit_{mode_name}_d_12_119"
      elif (
        (last_candle["RSI_3"] > 60.0)
        and (last_candle["RSI_14"] < 42.0)
        and (last_candle["RSI_3_1h"] < 40.0)
        and (last_candle["AROONU_14_4h"] > 75.0)
      ):
        return True, f"exit_{mode_name}_d_12_120"
      elif (
        (last_candle["RSI_3"] > 66.0)
        and (last_candle["RSI_14"] < 40.0)
        and (last_candle["RSI_3_1h"] < 50.0)
        and (last_candle["RSI_14_4h"] > 85.0)
      ):
        return True, f"exit_{mode_name}_d_12_121"
      elif (
        (last_candle["RSI_3"] > 64.0)
        and (last_candle["RSI_14"] < 38.0)
        and (last_candle["RSI_3_4h"] < 30.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_12_122"
      elif (
        (last_candle["RSI_3"] > 94.0)
        and (last_candle["WILLR_14"] > -1.0)
        and (last_candle["RSI_3_1h"] < 10.0)
        and (last_candle["RSI_3_1d"] < 30.0)
      ):
        return True, f"exit_{mode_name}_d_12_123"
      elif (
        (last_candle["RSI_3"] > 94.0)
        and (last_candle["RSI_3_1h"] < 15.0)
        and (
          isinstance(last_candle["STOCHRSIk_14_14_3_3_1d"], np.float64)
          and (last_candle["STOCHRSIk_14_14_3_3_1d"] > 80.0)
        )
      ):
        return True, f"exit_{mode_name}_d_12_124"
      elif (
        (last_candle["RSI_3"] > 82.0)
        and (last_candle["WILLR_14"] > -1.0)
        and (last_candle["RSI_3_1h"] < 10.0)
        and (last_candle["RSI_3_4h"] < 40.0)
        and (last_candle["RSI_3_1d"] < 40.0)
        and (last_candle["close"] < (last_candle["high_max_30_1d"] * 0.50))
      ):
        return True, f"exit_{mode_name}_d_12_125"
      elif (
        (last_candle["RSI_3"] > 96.0)
        and (last_candle["RSI_3_1h"] < 15.0)
        and (last_candle["RSI_3_4h"] < 40.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_12_126"
      elif (
        (last_candle["RSI_3"] > 96.0)
        and (last_candle["RSI_3_1h"] < 10.0)
        and (last_candle["RSI_3_4h"] < 30.0)
        and (last_candle["RSI_3_1d"] < 40.0)
      ):
        return True, f"exit_{mode_name}_d_12_127"
      elif (last_candle["RSI_3"] > 99.0) and (last_candle["RSI_3_4h"] < 30.0) and (last_candle["AROONU_14_4h"] > 85.0):
        return True, f"exit_{mode_name}_d_12_128"
      elif (
        (last_candle["RSI_3"] > 92.0)
        and (last_candle["RSI_3_4h"] < 25.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 80.0))
      ):
        return True, f"exit_{mode_name}_d_12_129"
      elif (
        (last_candle["RSI_3"] > 80.0)
        and (last_candle["RSI_14_1h"] > 65.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 80.0)
        and (last_candle["CCI_20_change_pct_1h"] < -0.0)
      ):
        return True, f"exit_{mode_name}_d_12_130"
      elif (
        (last_candle["RSI_14"] < 32.0)
        and (last_candle["RSI_3_1h"] < 20.0)
        and (last_candle["RSI_3_4h"] < 30.0)
        and (last_candle["STOCHRSIk_14_14_3_3_4h"] > 50.0)
      ):
        return True, f"exit_{mode_name}_d_12_131"
      elif (
        (last_candle["RSI_3"] > 86.0)
        and (last_candle["RSI_3_1h"] < 35.0)
        and (last_candle["RSI_3_4h"] < 35.0)
        and (last_candle["AROONU_14_1h"] > 50.0)
        and (last_candle["STOCHRSIk_14_14_3_3_1h"] > 40.0)
      ):
        return True, f"exit_{mode_name}_d_12_132"
      elif (
        (last_candle["RSI_3"] > 86.0)
        and (last_candle["AROONU_14_15m"] > 75.0)
        and (last_candle["AROONU_14_1h"] > 75.0)
        and (isinstance(last_candle["ROC_9_1d"], np.float64) and (last_candle["ROC_9_1d"] > 25.0))
      ):
        return True, f"exit_{mode_name}_d_12_133"

    #  Here ends exit signal conditions for long_exit_dec

    return False, None

