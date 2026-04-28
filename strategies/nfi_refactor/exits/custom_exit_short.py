"""Short-side custom exit routing extracted from NFI."""

from nfi_refactor.exits.custom_exit_call import call_custom_exit_mode
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

  # Short normal mode
  if matches_short_normal(strategy, enter_tags):
    exit_reason = call_custom_exit_mode(
      strategy.short_exit_normal,
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
    if exit_reason is not None:
      return exit_reason

  # Short Pump mode
  if matches_short_pump(strategy, enter_tags):
    exit_reason = call_custom_exit_mode(
      strategy.short_exit_pump,
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
    if exit_reason is not None:
      return exit_reason

  # Short Quick mode
  if matches_short_quick(strategy, enter_tags):
    exit_reason = call_custom_exit_mode(
      strategy.short_exit_quick,
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
    if exit_reason is not None:
      return exit_reason

  # Short Rebuy mode
  if matches_short_rebuy(strategy, enter_tags):
    exit_reason = call_custom_exit_mode(
      strategy.short_exit_rebuy,
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
    if exit_reason is not None:
      return exit_reason

  # Short high profit mode
  if matches_short_high_profit(strategy, enter_tags):
    exit_reason = call_custom_exit_mode(
      strategy.short_exit_high_profit,
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
    if exit_reason is not None:
      return exit_reason

  # Short rapid mode
  if matches_short_rapid(strategy, enter_tags):
    exit_reason = call_custom_exit_mode(
      strategy.short_exit_rapid,
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
    if exit_reason is not None:
      return exit_reason

  # Short scalp mode
  if matches_short_scalp(strategy, enter_tags):
    exit_reason = call_custom_exit_mode(
      strategy.short_exit_scalp,
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
    if exit_reason is not None:
      return exit_reason

  # Trades not opened by X7
  if not trade.is_short and (not matches_any_long_mode(strategy, enter_tags)):
    # use normal mode for such trades
    exit_reason = call_custom_exit_mode(
      strategy.long_exit_normal,
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
    if exit_reason is not None:
      return exit_reason

  # Trades not opened by X7
  if trade.is_short and (not matches_any_short_mode(strategy, enter_tags)):
    # use normal mode for such trades
    exit_reason = call_custom_exit_mode(
      strategy.short_exit_normal,
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
    if exit_reason is not None:
      return exit_reason

