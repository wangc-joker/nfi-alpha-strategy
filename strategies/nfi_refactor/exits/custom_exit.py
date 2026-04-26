"""Custom exit orchestration extracted from NostalgiaForInfinityX7.

This function routes an open trade to the original long/short mode-specific exit
handlers and preserves NFI's exit reason text exactly.
"""


def custom_exit(
  strategy, pair: str, trade: "Trade", current_time: "datetime", current_rate: float, current_profit: float, **kwargs
):
  df, _ = strategy.dp.get_analyzed_dataframe(pair, strategy.timeframe)
  last_candle = df.iloc[-1].squeeze()
  previous_candle_1 = df.iloc[-2].squeeze()
  previous_candle_2 = df.iloc[-3].squeeze()
  previous_candle_3 = df.iloc[-4].squeeze()
  previous_candle_4 = df.iloc[-5].squeeze()
  previous_candle_5 = df.iloc[-6].squeeze()

  enter_tag = "empty"
  if hasattr(trade, "enter_tag") and trade.enter_tag is not None:
    enter_tag = trade.enter_tag
  enter_tags = enter_tag.split()

  filled_entries = trade.select_filled_orders(trade.entry_side)
  filled_exits = trade.select_filled_orders(trade.exit_side)

  profit_stake = 0.0
  profit_ratio = 0.0
  profit_current_stake_ratio = 0.0
  profit_init_ratio = 0.0
  profit_stake, profit_ratio, profit_current_stake_ratio, profit_init_ratio = strategy.calc_total_profit(
    trade, filled_entries, filled_exits, current_rate
  )

  max_profit = 0.0
  max_loss = 0.0

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

  # Short normal mode
  if any(c in strategy.short_normal_mode_tags for c in enter_tags):
    sell, signal_name = strategy.short_exit_normal(
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

  # Short Pump mode
  if any(c in strategy.short_pump_mode_tags for c in enter_tags):
    sell, signal_name = strategy.short_exit_pump(
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

  # Short Quick mode
  if any(c in strategy.short_quick_mode_tags for c in enter_tags):
    sell, signal_name = strategy.short_exit_quick(
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

  # Short Rebuy mode
  if all(c in strategy.short_rebuy_mode_tags for c in enter_tags):
    sell, signal_name = strategy.short_exit_rebuy(
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

  # Short high profit mode
  if any(c in strategy.short_high_profit_mode_tags for c in enter_tags):
    sell, signal_name = strategy.short_exit_high_profit(
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

  # Short rapid mode
  if any(c in strategy.short_rapid_mode_tags for c in enter_tags):
    sell, signal_name = strategy.short_exit_rapid(
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

  # Short scalp mode
  if all(c in strategy.short_scalp_mode_tags for c in enter_tags) or (
    any(c in strategy.short_scalp_mode_tags for c in enter_tags)
    and all(
      c in (strategy.short_scalp_mode_tags + strategy.short_rebuy_mode_tags + strategy.short_grind_mode_tags) for c in enter_tags
    )
  ):
    sell, signal_name = strategy.short_exit_scalp(
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
    sell, signal_name = strategy.short_exit_normal(
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

  return None

# Custom Stake Amount
# ---------------------------------------------------------------------------------------------
