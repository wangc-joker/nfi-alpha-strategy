"""Detailed position-adjustment routing extracted from NFI."""


def call_adjustment_handler(
  adjustment_func,
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
):
  return adjustment_func(
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


def matches_long_rebuy_adjustment(strategy, enter_tags):
  return all(c in strategy.long_rebuy_mode_tags for c in enter_tags) or (
    any(c in strategy.long_rebuy_mode_tags for c in enter_tags)
    and all(c in (strategy.long_rebuy_mode_tags + strategy.long_grind_mode_tags) for c in enter_tags)
  )


def matches_short_rebuy_adjustment(strategy, enter_tags):
  return all(c in strategy.short_rebuy_mode_tags for c in enter_tags) or (
    any(c in strategy.short_rebuy_mode_tags for c in enter_tags)
    and all(c in (strategy.short_rebuy_mode_tags + strategy.short_grind_mode_tags) for c in enter_tags)
  )


def matches_long_grind_adjustment_v2_or_v3(strategy, enter_tags):
  return any(
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
  )


def matches_short_grind_adjustment_v2_or_v3(strategy, enter_tags):
  return any(
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
  )


def route_rebuy_adjustment(
  strategy,
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
  is_system_v3_family,
):
  if not trade.is_short and matches_long_rebuy_adjustment(strategy, enter_tags):
    adjustment_func = strategy.long_rebuy_adjust_trade_position_v3 if is_system_v3_family else strategy.long_rebuy_adjust_trade_position
    return True, call_adjustment_handler(
      adjustment_func,
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

  if trade.is_short and matches_short_rebuy_adjustment(strategy, enter_tags):
    adjustment_func = strategy.short_rebuy_adjust_trade_position_v3 if is_system_v3_family else strategy.short_rebuy_adjust_trade_position
    return True, call_adjustment_handler(
      adjustment_func,
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

  return False, None


def route_long_grind_adjustment(
  strategy,
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
  is_long_grind_mode,
  is_long_btc_mode,
  is_v2_date,
  is_system_v3_family,
):
  if not is_long_grind_mode and not is_long_btc_mode and is_system_v3_family:
    if matches_long_grind_adjustment_v2_or_v3(strategy, enter_tags):
      return call_adjustment_handler(
        strategy.long_grind_adjust_trade_position_v3,
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
    return call_adjustment_handler(
      strategy.long_grind_adjust_trade_position,
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
  elif matches_long_grind_adjustment_v2_or_v3(strategy, enter_tags):
    return call_adjustment_handler(
      strategy.long_grind_adjust_trade_position_v2,
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


def route_short_grind_adjustment(
  strategy,
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
  is_short_grind_mode,
  is_v2_date,
  is_system_v3_family,
):
  if not is_short_grind_mode and is_system_v3_family:
    if matches_short_grind_adjustment_v2_or_v3(strategy, enter_tags):
      return call_adjustment_handler(
        strategy.short_grind_adjust_trade_position_v3,
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
    return call_adjustment_handler(
      strategy.short_grind_adjust_trade_position,
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
  elif matches_short_grind_adjustment_v2_or_v3(strategy, enter_tags):
    return call_adjustment_handler(
      strategy.short_grind_adjust_trade_position_v2,
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
