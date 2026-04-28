from datetime import datetime
from typing import Optional

from freqtrade.persistence import Trade

from nfi_refactor.position.adjustment_detail import (
  AdjustmentCallContext,
  route_long_grind_adjustment,
  route_rebuy_adjustment,
  route_short_grind_adjustment,
)


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
  is_system_v3_family = strategy.is_system_v3(trade) or strategy.is_system_v3_1(trade) or strategy.is_system_v3_2(trade)

  context = AdjustmentCallContext(
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

  handled, adjustment = route_rebuy_adjustment(
    strategy,
    context,
    is_system_v3_family,
  )
  if handled:
    return adjustment

  if not trade.is_short:
    return route_long_grind_adjustment(
      strategy,
      context,
      is_long_grind_mode,
      is_long_btc_mode,
      is_v2_date,
      is_system_v3_family,
    )

  if trade.is_short:
    return route_short_grind_adjustment(
      strategy,
      context,
      is_short_grind_mode,
      is_v2_date,
      is_system_v3_family,
    )

  return None
