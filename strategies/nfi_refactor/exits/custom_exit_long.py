"""Long-side custom exit routing extracted from NFI."""

from nfi_refactor.exits.custom_exit_call import call_custom_exit_mode


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
  if any(c in strategy.long_normal_mode_tags for c in enter_tags):
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
  if any(c in strategy.long_pump_mode_tags for c in enter_tags):
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
  if any(c in strategy.long_quick_mode_tags for c in enter_tags):
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
  if all(c in strategy.long_rebuy_mode_tags for c in enter_tags) or (
    any(c in strategy.long_rebuy_mode_tags for c in enter_tags)
    and all(c in (strategy.long_rebuy_mode_tags + strategy.long_grind_mode_tags) for c in enter_tags)
  ):
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
  if any(c in strategy.long_high_profit_mode_tags for c in enter_tags):
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
  if all(c in strategy.long_rapid_mode_tags for c in enter_tags) or (
    any(c in strategy.long_rapid_mode_tags for c in enter_tags)
    and all(
      c
      in (
        strategy.long_rapid_mode_tags + strategy.long_rebuy_mode_tags + strategy.long_grind_mode_tags + strategy.long_scalp_mode_tags
      )
      for c in enter_tags
    )
  ):
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
  if all(c in strategy.long_grind_mode_tags for c in enter_tags):
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
  if all(c in strategy.long_btc_mode_tags for c in enter_tags):
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
  if any(c in strategy.long_top_coins_mode_tags for c in enter_tags):
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
  if all(c in strategy.long_scalp_mode_tags for c in enter_tags) or (
    any(c in strategy.long_scalp_mode_tags for c in enter_tags)
    and all(
      c in (strategy.long_scalp_mode_tags + strategy.long_rebuy_mode_tags + strategy.long_grind_mode_tags) for c in enter_tags
    )
  ):
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
