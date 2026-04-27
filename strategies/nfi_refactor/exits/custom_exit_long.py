"""Long-side custom exit routing extracted from NFI."""


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
    sell, signal_name = strategy.long_exit_normal(
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
    if sell and (signal_name is not None):
      return f"{signal_name} ( {enter_tag})"

  # Long Pump mode
  if any(c in strategy.long_pump_mode_tags for c in enter_tags):
    sell, signal_name = strategy.long_exit_pump(
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
    if sell and (signal_name is not None):
      return f"{signal_name} ( {enter_tag})"

  # Long Quick mode
  if any(c in strategy.long_quick_mode_tags for c in enter_tags):
    sell, signal_name = strategy.long_exit_quick(
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
    if sell and (signal_name is not None):
      return f"{signal_name} ( {enter_tag})"

  # Long Rebuy mode
  if all(c in strategy.long_rebuy_mode_tags for c in enter_tags) or (
    any(c in strategy.long_rebuy_mode_tags for c in enter_tags)
    and all(c in (strategy.long_rebuy_mode_tags + strategy.long_grind_mode_tags) for c in enter_tags)
  ):
    sell, signal_name = strategy.long_exit_rebuy(
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
    if sell and (signal_name is not None):
      return f"{signal_name} ( {enter_tag})"

  # Long high profit mode
  if any(c in strategy.long_high_profit_mode_tags for c in enter_tags):
    sell, signal_name = strategy.long_exit_high_profit(
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
    if sell and (signal_name is not None):
      return f"{signal_name} ( {enter_tag})"

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
    sell, signal_name = strategy.long_exit_rapid(
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
    if sell and (signal_name is not None):
      return f"{signal_name} ( {enter_tag})"

  # Long grind mode
  if all(c in strategy.long_grind_mode_tags for c in enter_tags):
    sell, signal_name = strategy.long_exit_grind(
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
    if sell and (signal_name is not None):
      return f"{signal_name} ( {enter_tag})"

  # Long btc mode
  if all(c in strategy.long_btc_mode_tags for c in enter_tags):
    sell, signal_name = strategy.long_exit_btc(
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
    if sell and (signal_name is not None):
      return f"{signal_name} ( {enter_tag})"

  # Long Top Coins mode
  if any(c in strategy.long_top_coins_mode_tags for c in enter_tags):
    sell, signal_name = strategy.long_exit_top_coins(
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
    if sell and (signal_name is not None):
      return f"{signal_name} ( {enter_tag})"

  # Long scalp mode
  if all(c in strategy.long_scalp_mode_tags for c in enter_tags) or (
    any(c in strategy.long_scalp_mode_tags for c in enter_tags)
    and all(
      c in (strategy.long_scalp_mode_tags + strategy.long_rebuy_mode_tags + strategy.long_grind_mode_tags) for c in enter_tags
    )
  ):
    sell, signal_name = strategy.long_exit_scalp(
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
    if sell and (signal_name is not None):
      return f"{signal_name} ( {enter_tag})"
