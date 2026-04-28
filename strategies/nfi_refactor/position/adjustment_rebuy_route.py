"""Rebuy position-adjustment routing helpers."""

from nfi_refactor.position.adjustment_context import (
  AdjustmentCallContext,
  AdjustmentModeState,
  all_tags_in,
  any_tags_in,
)
from nfi_refactor.position.adjustment_execution import call_adjustment_handler


def matches_long_rebuy_adjustment(strategy, enter_tags):
  return all_tags_in(enter_tags, strategy.long_rebuy_mode_tags) or (
    any_tags_in(enter_tags, strategy.long_rebuy_mode_tags)
    and all_tags_in(enter_tags, strategy.long_rebuy_mode_tags + strategy.long_grind_mode_tags)
  )


def matches_short_rebuy_adjustment(strategy, enter_tags):
  return all_tags_in(enter_tags, strategy.short_rebuy_mode_tags) or (
    any_tags_in(enter_tags, strategy.short_rebuy_mode_tags)
    and all_tags_in(enter_tags, strategy.short_rebuy_mode_tags + strategy.short_grind_mode_tags)
  )


def select_long_rebuy_adjustment_func(strategy, state: AdjustmentModeState):
  return (
    strategy.long_rebuy_adjust_trade_position_v3
    if state.is_system_v3_family
    else strategy.long_rebuy_adjust_trade_position
  )


def select_short_rebuy_adjustment_func(strategy, state: AdjustmentModeState):
  return (
    strategy.short_rebuy_adjust_trade_position_v3
    if state.is_system_v3_family
    else strategy.short_rebuy_adjust_trade_position
  )


def route_rebuy_adjustment(
  strategy,
  context: AdjustmentCallContext,
  state: AdjustmentModeState,
):
  if not context.trade.is_short and matches_long_rebuy_adjustment(strategy, context.enter_tags):
    adjustment_func = select_long_rebuy_adjustment_func(strategy, state)
    return True, call_adjustment_handler(adjustment_func, context)

  if context.trade.is_short and matches_short_rebuy_adjustment(strategy, context.enter_tags):
    adjustment_func = select_short_rebuy_adjustment_func(strategy, state)
    return True, call_adjustment_handler(adjustment_func, context)

  return False, None
