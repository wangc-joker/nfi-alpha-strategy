"""Short-side custom exit routing extracted from NFI."""

from nfi_refactor.exits.custom_exit_call import call_custom_exit_mode, route_custom_exit_modes
from nfi_refactor.exits.custom_exit_long_match import matches_any_long_mode
from nfi_refactor.exits.custom_exit_short_match import (
  matches_any_short_mode,
  matches_short_high_profit,
  matches_short_normal,
  matches_short_pump,
  matches_short_quick,
  matches_short_rapid,
  matches_short_rebuy,
  matches_short_scalp,
)


def route_short_custom_exit(
  strategy,
  pair: str,
  trade,
  current_time,
  current_rate: float,
  enter_tag,
  enter_tags,
  filled_entries,
  filled_exits,
  profit_stake,
  profit_ratio,
  profit_current_stake_ratio,
  profit_init_ratio,
  max_profit,
  max_loss,
  last_candle,
  previous_candle_1,
  previous_candle_2,
  previous_candle_3,
  previous_candle_4,
  previous_candle_5,
):
  rules = (
    (matches_short_normal, strategy.short_exit_normal),
    (matches_short_pump, strategy.short_exit_pump),
    (matches_short_quick, strategy.short_exit_quick),
    (matches_short_rebuy, strategy.short_exit_rebuy),
    (matches_short_high_profit, strategy.short_exit_high_profit),
    (matches_short_rapid, strategy.short_exit_rapid),
    (matches_short_scalp, strategy.short_exit_scalp),
  )

  exit_reason = route_custom_exit_modes(
    rules,
    strategy,
    enter_tag,
    enter_tags,
    pair,
    current_rate,
    profit_stake,
    profit_ratio,
    profit_current_stake_ratio,
    profit_init_ratio,
    max_profit,
    max_loss,
    filled_entries,
    filled_exits,
    last_candle,
    previous_candle_1,
    previous_candle_2,
    previous_candle_3,
    previous_candle_4,
    previous_candle_5,
    trade,
    current_time,
  )
  if exit_reason is not None:
    return exit_reason

  # Trades not opened by X7 use normal mode for their side.
  fallback_exit_func = None
  if not trade.is_short and (not matches_any_long_mode(strategy, enter_tags)):
    fallback_exit_func = strategy.long_exit_normal
  if trade.is_short and (not matches_any_short_mode(strategy, enter_tags)):
    fallback_exit_func = strategy.short_exit_normal

  if fallback_exit_func is None:
    return None

  return call_custom_exit_mode(
    fallback_exit_func,
    enter_tag,
    pair,
    current_rate,
    profit_stake,
    profit_ratio,
    profit_current_stake_ratio,
    profit_init_ratio,
    max_profit,
    max_loss,
    filled_entries,
    filled_exits,
    last_candle,
    previous_candle_1,
    previous_candle_2,
    previous_candle_3,
    previous_candle_4,
    previous_candle_5,
    trade,
    current_time,
    enter_tags,
  )