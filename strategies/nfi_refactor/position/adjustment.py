from datetime import datetime
from typing import Optional

from freqtrade.persistence import Trade

def adjust_trade_position(
  strategy,
  trade: Trade,
  current_time: datetime,
  current_rate: float,
  current_profit: float,
  min_stake: Optional[float],
  max_stake: float,
  current_entry_rate: float,
  current_exit_rate: float,
  current_entry_profit: float,
  current_exit_profit: float,
  **kwargs,
):
  if strategy.position_adjustment_enable == False:
    return None

  enter_tag = "empty"
  if hasattr(trade, "enter_tag") and trade.enter_tag is not None:
    enter_tag = trade.enter_tag
  enter_tags = enter_tag.split()

  is_backtest = strategy.is_backtest_mode()
  is_long_grind_mode = all(c in strategy.long_grind_mode_tags for c in enter_tags)
  is_long_btc_mode = all(c in strategy.long_btc_mode_tags for c in enter_tags)
  is_short_grind_mode = all(c in strategy.short_grind_mode_tags for c in enter_tags)
  is_v2_date = trade.open_date_utc.replace(tzinfo=None) >= datetime(2025, 2, 13) or is_backtest
  is_system_v3 = strategy.is_system_v3(trade)
  is_system_v3_1 = strategy.is_system_v3_1(trade)
  is_system_v3_2 = strategy.is_system_v3_2(trade)

  # Rebuy mode
  if not trade.is_short and (
    all(c in strategy.long_rebuy_mode_tags for c in enter_tags)
    or (
      any(c in strategy.long_rebuy_mode_tags for c in enter_tags)
      and all(c in (strategy.long_rebuy_mode_tags + strategy.long_grind_mode_tags) for c in enter_tags)
    )
  ):
    if is_system_v3 or is_system_v3_1 or is_system_v3_2:
      return strategy.long_rebuy_adjust_trade_position_v3(
        trade,
        enter_tags,
        current_time,
        current_rate,
        current_profit,
        min_stake,
        max_stake,
        current_entry_rate,
        current_exit_rate,
        current_entry_profit,
        current_exit_profit,
      )
    else:
      return strategy.long_rebuy_adjust_trade_position(
        trade,
        enter_tags,
        current_time,
        current_rate,
        current_profit,
        min_stake,
        max_stake,
        current_entry_rate,
        current_exit_rate,
        current_entry_profit,
        current_exit_profit,
      )
  elif trade.is_short and (
    all(c in strategy.short_rebuy_mode_tags for c in enter_tags)
    or (
      any(c in strategy.short_rebuy_mode_tags for c in enter_tags)
      and all(c in (strategy.short_rebuy_mode_tags + strategy.short_grind_mode_tags) for c in enter_tags)
    )
  ):
    if is_system_v3 or is_system_v3_1 or is_system_v3_2:
      return strategy.short_rebuy_adjust_trade_position_v3(
        trade,
        enter_tags,
        current_time,
        current_rate,
        current_profit,
        min_stake,
        max_stake,
        current_entry_rate,
        current_exit_rate,
        current_entry_profit,
        current_exit_profit,
      )
    else:
      return strategy.short_rebuy_adjust_trade_position(
        trade,
        enter_tags,
        current_time,
        current_rate,
        current_profit,
        min_stake,
        max_stake,
        current_entry_rate,
        current_exit_rate,
        current_entry_profit,
        current_exit_profit,
      )

  # Grinding
  elif not trade.is_short:
    if not is_long_grind_mode and not is_long_btc_mode and (is_system_v3 or is_system_v3_1 or is_system_v3_2):
      if any(
        c
        in (
          strategy.long_normal_mode_tags
          + strategy.long_pump_mode_tags
          + strategy.long_quick_mode_tags
          + strategy.long_high_profit_mode_tags
          + strategy.long_rapid_mode_tags
          + strategy.long_top_coins_mode_tags
          + strategy.long_scalp_mode_tags
        )
        for c in enter_tags
      ) or not any(
        c
        in (
          strategy.long_normal_mode_tags
          + strategy.long_pump_mode_tags
          + strategy.long_quick_mode_tags
          + strategy.long_rebuy_mode_tags
          + strategy.long_high_profit_mode_tags
          + strategy.long_rapid_mode_tags
          + strategy.long_grind_mode_tags
          + strategy.long_btc_mode_tags
          + strategy.long_top_coins_mode_tags
          + strategy.long_scalp_mode_tags
        )
        for c in enter_tags
      ):
        return strategy.long_grind_adjust_trade_position_v3(
          trade,
          enter_tags,
          current_time,
          current_rate,
          current_profit,
          min_stake,
          max_stake,
          current_entry_rate,
          current_exit_rate,
          current_entry_profit,
          current_exit_profit,
        )
    elif is_long_grind_mode or is_long_btc_mode or not is_v2_date:
      return strategy.long_grind_adjust_trade_position(
        trade,
        enter_tags,
        current_time,
        current_rate,
        current_profit,
        min_stake,
        max_stake,
        current_entry_rate,
        current_exit_rate,
        current_entry_profit,
        current_exit_profit,
      )
    elif any(
      c
      in (
        strategy.long_normal_mode_tags
        + strategy.long_pump_mode_tags
        + strategy.long_quick_mode_tags
        + strategy.long_high_profit_mode_tags
        + strategy.long_rapid_mode_tags
        + strategy.long_top_coins_mode_tags
        + strategy.long_scalp_mode_tags
      )
      for c in enter_tags
    ) or not any(
      c
      in (
        strategy.long_normal_mode_tags
        + strategy.long_pump_mode_tags
        + strategy.long_quick_mode_tags
        + strategy.long_rebuy_mode_tags
        + strategy.long_high_profit_mode_tags
        + strategy.long_rapid_mode_tags
        + strategy.long_grind_mode_tags
        + strategy.long_btc_mode_tags
        + strategy.long_top_coins_mode_tags
        + strategy.long_scalp_mode_tags
      )
      for c in enter_tags
    ):
      return strategy.long_grind_adjust_trade_position_v2(
        trade,
        enter_tags,
        current_time,
        current_rate,
        current_profit,
        min_stake,
        max_stake,
        current_entry_rate,
        current_exit_rate,
        current_entry_profit,
        current_exit_profit,
      )

  elif trade.is_short:
    if not is_short_grind_mode and (is_system_v3 or is_system_v3_1 or is_system_v3_2):
      if any(
        c
        in (
          strategy.short_normal_mode_tags
          + strategy.short_pump_mode_tags
          + strategy.short_quick_mode_tags
          + strategy.short_high_profit_mode_tags
          + strategy.short_rapid_mode_tags
          + strategy.short_top_coins_mode_tags
          + strategy.short_scalp_mode_tags
        )
        for c in enter_tags
      ) or not any(
        c
        in (
          strategy.short_normal_mode_tags
          + strategy.short_pump_mode_tags
          + strategy.short_quick_mode_tags
          + strategy.short_rebuy_mode_tags
          + strategy.short_high_profit_mode_tags
          + strategy.short_rapid_mode_tags
          + strategy.short_grind_mode_tags
          + strategy.short_top_coins_mode_tags
          + strategy.short_scalp_mode_tags
        )
        for c in enter_tags
      ):
        return strategy.short_grind_adjust_trade_position_v3(
          trade,
          enter_tags,
          current_time,
          current_rate,
          current_profit,
          min_stake,
          max_stake,
          current_entry_rate,
          current_exit_rate,
          current_entry_profit,
          current_exit_profit,
        )
    elif is_short_grind_mode or not is_v2_date:
      return strategy.short_grind_adjust_trade_position(
        trade,
        enter_tags,
        current_time,
        current_rate,
        current_profit,
        min_stake,
        max_stake,
        current_entry_rate,
        current_exit_rate,
        current_entry_profit,
        current_exit_profit,
      )
    else:
      if any(
        c
        in (
          strategy.short_normal_mode_tags
          + strategy.short_pump_mode_tags
          + strategy.short_quick_mode_tags
          + strategy.short_high_profit_mode_tags
          + strategy.short_rapid_mode_tags
          + strategy.short_top_coins_mode_tags
          + strategy.short_scalp_mode_tags
        )
        for c in enter_tags
      ) or not any(
        c
        in (
          strategy.short_normal_mode_tags
          + strategy.short_pump_mode_tags
          + strategy.short_quick_mode_tags
          + strategy.short_rebuy_mode_tags
          + strategy.short_high_profit_mode_tags
          + strategy.short_rapid_mode_tags
          + strategy.short_grind_mode_tags
          + strategy.short_top_coins_mode_tags
          + strategy.short_scalp_mode_tags
        )
        for c in enter_tags
      ):
        return strategy.short_grind_adjust_trade_position_v2(
          trade,
          enter_tags,
          current_time,
          current_rate,
          current_profit,
          min_stake,
          max_stake,
          current_entry_rate,
          current_exit_rate,
          current_entry_profit,
          current_exit_profit,
        )

  return None


