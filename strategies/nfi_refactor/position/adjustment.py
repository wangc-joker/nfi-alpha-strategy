from datetime import datetime
from typing import Optional

from freqtrade.persistence import Trade

from nfi_refactor.position.adjustment_detail import (
  build_adjustment_call_context,
  build_adjustment_mode_state,
  get_adjustment_enter_tags,
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

  enter_tags = get_adjustment_enter_tags(trade)
  context = build_adjustment_call_context(
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
  state = build_adjustment_mode_state(strategy, trade, enter_tags)

  handled, adjustment = route_rebuy_adjustment(
    strategy,
    context,
    state,
  )
  if handled:
    return adjustment

  if not trade.is_short:
    return route_long_grind_adjustment(
      strategy,
      context,
      state,
    )

  if trade.is_short:
    return route_short_grind_adjustment(
      strategy,
      context,
      state,
    )

  return None
