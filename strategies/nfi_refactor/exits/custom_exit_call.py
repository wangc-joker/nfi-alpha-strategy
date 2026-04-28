"""Shared custom-exit mode invocation helper."""

from nfi_refactor.exits.custom_exit_result import format_exit_reason


def call_custom_exit_mode(
  exit_func,
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
):
  exit_result = exit_func(
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
  return format_exit_reason(exit_result, enter_tag)
