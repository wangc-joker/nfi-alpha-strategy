"""Long-side custom exit routing extracted from NFI."""

from nfi_refactor.exits.custom_exit_call import call_custom_exit_mode
from nfi_refactor.exits.custom_exit_long_match import (
  matches_long_btc,
  matches_long_grind,
  matches_long_high_profit,
  matches_long_normal,
  matches_long_pump,
  matches_long_quick,
  matches_long_rapid,
  matches_long_rebuy,
  matches_long_scalp,
  matches_long_top_coins,
)


def route_long_custom_exit(
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

  # Long Normal mode
  if matches_long_normal(strategy, enter_tags):
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

  # Long Pump mode
  if matches_long_pump(strategy, enter_tags):
    exit_reason = call_custom_exit_mode(
      strategy.long_exit_pump,
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

  # Long Quick mode
  if matches_long_quick(strategy, enter_tags):
    exit_reason = call_custom_exit_mode(
      strategy.long_exit_quick,
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

  # Long Rebuy mode
  if matches_long_rebuy(strategy, enter_tags):
    exit_reason = call_custom_exit_mode(
      strategy.long_exit_rebuy,
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

  # Long high profit mode
  if matches_long_high_profit(strategy, enter_tags):
    exit_reason = call_custom_exit_mode(
      strategy.long_exit_high_profit,
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

  # Long rapid mode
  if matches_long_rapid(strategy, enter_tags):
    exit_reason = call_custom_exit_mode(
      strategy.long_exit_rapid,
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

  # Long grind mode
  if matches_long_grind(strategy, enter_tags):
    exit_reason = call_custom_exit_mode(
      strategy.long_exit_grind,
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

  # Long btc mode
  if matches_long_btc(strategy, enter_tags):
    exit_reason = call_custom_exit_mode(
      strategy.long_exit_btc,
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

  # Long Top Coins mode
  if matches_long_top_coins(strategy, enter_tags):
    exit_reason = call_custom_exit_mode(
      strategy.long_exit_top_coins,
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

  # Long scalp mode
  if matches_long_scalp(strategy, enter_tags):
    exit_reason = call_custom_exit_mode(
      strategy.long_exit_scalp,
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
