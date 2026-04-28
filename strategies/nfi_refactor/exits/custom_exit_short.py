"""Short-side custom exit routing extracted from NFI."""

from nfi_refactor.exits.custom_exit_result import format_exit_reason


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
  if any(c in strategy.short_normal_mode_tags for c in enter_tags):
    exit_reason = format_exit_reason(strategy.short_exit_normal(
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
    ), enter_tag)
    if exit_reason is not None:
      return exit_reason

  # Short Pump mode
  if any(c in strategy.short_pump_mode_tags for c in enter_tags):
    exit_reason = format_exit_reason(strategy.short_exit_pump(
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
    ), enter_tag)
    if exit_reason is not None:
      return exit_reason

  # Short Quick mode
  if any(c in strategy.short_quick_mode_tags for c in enter_tags):
    exit_reason = format_exit_reason(strategy.short_exit_quick(
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
    ), enter_tag)
    if exit_reason is not None:
      return exit_reason

  # Short Rebuy mode
  if all(c in strategy.short_rebuy_mode_tags for c in enter_tags):
    exit_reason = format_exit_reason(strategy.short_exit_rebuy(
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
    ), enter_tag)
    if exit_reason is not None:
      return exit_reason

  # Short high profit mode
  if any(c in strategy.short_high_profit_mode_tags for c in enter_tags):
    exit_reason = format_exit_reason(strategy.short_exit_high_profit(
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
    ), enter_tag)
    if exit_reason is not None:
      return exit_reason

  # Short rapid mode
  if any(c in strategy.short_rapid_mode_tags for c in enter_tags):
    exit_reason = format_exit_reason(strategy.short_exit_rapid(
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
    ), enter_tag)
    if exit_reason is not None:
      return exit_reason

  # Short scalp mode
  if all(c in strategy.short_scalp_mode_tags for c in enter_tags) or (
    any(c in strategy.short_scalp_mode_tags for c in enter_tags)
    and all(
      c in (strategy.short_scalp_mode_tags + strategy.short_rebuy_mode_tags + strategy.short_grind_mode_tags) for c in enter_tags
    )
  ):
    exit_reason = format_exit_reason(strategy.short_exit_scalp(
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
    ), enter_tag)
    if exit_reason is not None:
      return exit_reason

  # Trades not opened by X7
  if not trade.is_short and (
    not any(
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
    )
  ):
    # use normal mode for such trades
    exit_reason = format_exit_reason(strategy.long_exit_normal(
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
    ), enter_tag)
    if exit_reason is not None:
      return exit_reason

  # Trades not opened by X7
  if trade.is_short and (
    not any(
      c
      in (
        strategy.short_normal_mode_tags
        + strategy.short_pump_mode_tags
        + strategy.short_quick_mode_tags
        + strategy.short_rebuy_mode_tags
        + strategy.short_high_profit_mode_tags
        + strategy.short_rapid_mode_tags
        + strategy.short_grind_mode_tags
        + strategy.short_scalp_mode_tags
      )
      for c in enter_tags
    )
  ):
    # use normal mode for such trades
    exit_reason = format_exit_reason(strategy.short_exit_normal(
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
    ), enter_tag)
    if exit_reason is not None:
      return exit_reason

