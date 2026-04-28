"""Detailed position-adjustment routing extracted from NFI."""

from dataclasses import dataclass


@dataclass
class AdjustmentCallContext:
  trade: object
  enter_tags: list
  current_time: object
  current_rate: float
  current_profit: float
  min_stake: object
  max_stake: float
  current_entry_rate: float
  current_exit_rate: float
  current_entry_profit: float
  current_exit_profit: float


def call_adjustment_handler(adjustment_func, context: AdjustmentCallContext):
  return adjustment_func(
    context.trade,
    context.enter_tags,
    context.current_time,
    context.current_rate,
    context.current_profit,
    context.min_stake,
    context.max_stake,
    context.current_entry_rate,
    context.current_exit_rate,
    context.current_entry_profit,
    context.current_exit_profit,
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
  context: AdjustmentCallContext,
  is_system_v3_family,
):
  if not context.trade.is_short and matches_long_rebuy_adjustment(strategy, context.enter_tags):
    adjustment_func = strategy.long_rebuy_adjust_trade_position_v3 if is_system_v3_family else strategy.long_rebuy_adjust_trade_position
    return True, call_adjustment_handler(adjustment_func, context)

  if context.trade.is_short and matches_short_rebuy_adjustment(strategy, context.enter_tags):
    adjustment_func = strategy.short_rebuy_adjust_trade_position_v3 if is_system_v3_family else strategy.short_rebuy_adjust_trade_position
    return True, call_adjustment_handler(adjustment_func, context)

  return False, None


def route_long_grind_adjustment(
  strategy,
  context: AdjustmentCallContext,
  is_long_grind_mode,
  is_long_btc_mode,
  is_v2_date,
  is_system_v3_family,
):
  if not is_long_grind_mode and not is_long_btc_mode and is_system_v3_family:
    if matches_long_grind_adjustment_v2_or_v3(strategy, context.enter_tags):
      return call_adjustment_handler(strategy.long_grind_adjust_trade_position_v3, context)
  elif is_long_grind_mode or is_long_btc_mode or not is_v2_date:
    return call_adjustment_handler(strategy.long_grind_adjust_trade_position, context)
  elif matches_long_grind_adjustment_v2_or_v3(strategy, context.enter_tags):
    return call_adjustment_handler(strategy.long_grind_adjust_trade_position_v2, context)

  return None


def route_short_grind_adjustment(
  strategy,
  context: AdjustmentCallContext,
  is_short_grind_mode,
  is_v2_date,
  is_system_v3_family,
):
  if not is_short_grind_mode and is_system_v3_family:
    if matches_short_grind_adjustment_v2_or_v3(strategy, context.enter_tags):
      return call_adjustment_handler(strategy.short_grind_adjust_trade_position_v3, context)
  elif is_short_grind_mode or not is_v2_date:
    return call_adjustment_handler(strategy.short_grind_adjust_trade_position, context)
  elif matches_short_grind_adjustment_v2_or_v3(strategy, context.enter_tags):
    return call_adjustment_handler(strategy.short_grind_adjust_trade_position_v2, context)

  return None
