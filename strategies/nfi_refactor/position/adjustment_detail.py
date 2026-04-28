"""Detailed position-adjustment routing extracted from NFI."""

from dataclasses import dataclass
from datetime import datetime


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


@dataclass
class AdjustmentModeState:
  is_long_grind_mode: bool
  is_long_btc_mode: bool
  is_short_grind_mode: bool
  is_v2_date: bool
  is_system_v3_family: bool


def get_adjustment_enter_tags(trade) -> list:
  enter_tag = "empty"
  if hasattr(trade, "enter_tag") and trade.enter_tag is not None:
    enter_tag = trade.enter_tag
  return enter_tag.split()


def build_adjustment_call_context(
  trade,
  enter_tags,
  current_time,
  current_rate: float,
  current_profit: float,
  min_stake,
  max_stake: float,
  current_entry_rate: float,
  current_exit_rate: float,
  current_entry_profit: float,
  current_exit_profit: float,
) -> AdjustmentCallContext:
  return AdjustmentCallContext(
    trade=trade,
    enter_tags=enter_tags,
    current_time=current_time,
    current_rate=current_rate,
    current_profit=current_profit,
    min_stake=min_stake,
    max_stake=max_stake,
    current_entry_rate=current_entry_rate,
    current_exit_rate=current_exit_rate,
    current_entry_profit=current_entry_profit,
    current_exit_profit=current_exit_profit,
  )


def build_adjustment_mode_state(strategy, trade, enter_tags) -> AdjustmentModeState:
  is_backtest = strategy.is_backtest_mode()
  return AdjustmentModeState(
    is_long_grind_mode=all(c in strategy.long_grind_mode_tags for c in enter_tags),
    is_long_btc_mode=all(c in strategy.long_btc_mode_tags for c in enter_tags),
    is_short_grind_mode=all(c in strategy.short_grind_mode_tags for c in enter_tags),
    is_v2_date=trade.open_date_utc.replace(tzinfo=None) >= datetime(2025, 2, 13) or is_backtest,
    is_system_v3_family=strategy.is_system_v3(trade)
    or strategy.is_system_v3_1(trade)
    or strategy.is_system_v3_2(trade),
  )


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
  state: AdjustmentModeState,
):
  if not context.trade.is_short and matches_long_rebuy_adjustment(strategy, context.enter_tags):
    adjustment_func = (
      strategy.long_rebuy_adjust_trade_position_v3
      if state.is_system_v3_family
      else strategy.long_rebuy_adjust_trade_position
    )
    return True, call_adjustment_handler(adjustment_func, context)

  if context.trade.is_short and matches_short_rebuy_adjustment(strategy, context.enter_tags):
    adjustment_func = (
      strategy.short_rebuy_adjust_trade_position_v3
      if state.is_system_v3_family
      else strategy.short_rebuy_adjust_trade_position
    )
    return True, call_adjustment_handler(adjustment_func, context)

  return False, None


def route_long_grind_adjustment(
  strategy,
  context: AdjustmentCallContext,
  state: AdjustmentModeState,
):
  if not state.is_long_grind_mode and not state.is_long_btc_mode and state.is_system_v3_family:
    if matches_long_grind_adjustment_v2_or_v3(strategy, context.enter_tags):
      return call_adjustment_handler(strategy.long_grind_adjust_trade_position_v3, context)
  elif state.is_long_grind_mode or state.is_long_btc_mode or not state.is_v2_date:
    return call_adjustment_handler(strategy.long_grind_adjust_trade_position, context)
  elif matches_long_grind_adjustment_v2_or_v3(strategy, context.enter_tags):
    return call_adjustment_handler(strategy.long_grind_adjust_trade_position_v2, context)

  return None


def route_short_grind_adjustment(
  strategy,
  context: AdjustmentCallContext,
  state: AdjustmentModeState,
):
  if not state.is_short_grind_mode and state.is_system_v3_family:
    if matches_short_grind_adjustment_v2_or_v3(strategy, context.enter_tags):
      return call_adjustment_handler(strategy.short_grind_adjust_trade_position_v3, context)
  elif state.is_short_grind_mode or not state.is_v2_date:
    return call_adjustment_handler(strategy.short_grind_adjust_trade_position, context)
  elif matches_short_grind_adjustment_v2_or_v3(strategy, context.enter_tags):
    return call_adjustment_handler(strategy.short_grind_adjust_trade_position_v2, context)

  return None
