"""Rebuy position-adjustment handlers extracted from NFI."""

import logging
from datetime import datetime
from typing import Optional

from freqtrade.persistence import Trade


log = logging.getLogger(__name__)

def long_rebuy_adjust_trade_position(
  strategy,
  trade: Trade,
  enter_tags,
  current_time: datetime,
  current_rate: float,
  current_profit: float,
  min_stake: Optional[float],
  max_stake: float,
  current_entry_rate: float,
  current_exit_rate: float,
  current_entry_profit: float,
  current_exit_profit: float,
  **kwargs,
) -> Optional[float]:
  # min/max stakes include leverage. The return amounts is before leverage.
  min_stake /= trade.leverage
  max_stake /= trade.leverage
  df, _ = strategy.dp.get_analyzed_dataframe(trade.pair, strategy.timeframe)
  if len(df) < 2:
    return None
  last_candle = df.iloc[-1].squeeze()
  previous_candle = df.iloc[-2].squeeze()

  # we already waiting for an order to get filled
  if trade.has_open_orders:
    return None

  filled_orders = trade.select_filled_orders()
  filled_entries = trade.select_filled_orders(trade.entry_side)
  filled_exits = trade.select_filled_orders(trade.exit_side)
  count_of_entries = trade.nr_of_successful_entries
  count_of_exits = trade.nr_of_successful_exits

  if count_of_entries == 0:
    return None

  has_order_tags = False
  if hasattr(filled_orders[0], "ft_order_tag"):
    has_order_tags = True

  # The first exit is de-risk (providing the trade is still open)
  if (count_of_exits > 0) and (filled_exits[0].ft_order_tag in ["derisk_level_3"]):
    return strategy.long_grind_adjust_trade_position_v2(
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

  exit_rate = current_rate
  if strategy.dp.runmode.value in ("live", "dry_run"):
    ticker = strategy.dp.ticker(trade.pair)
    if ("bid" in ticker) and ("ask" in ticker):
      if trade.is_short:
        if strategy.config["exit_pricing"]["price_side"] in ["ask", "other"]:
          if ticker["ask"] is not None:
            exit_rate = ticker["ask"]
      else:
        if strategy.config["exit_pricing"]["price_side"] in ["bid", "other"]:
          if ticker["bid"] is not None:
            exit_rate = ticker["bid"]

  profit_stake, profit_ratio, profit_current_stake_ratio, profit_init_ratio = strategy.calc_total_profit(
    trade, filled_entries, filled_exits, exit_rate
  )

  slice_amount = filled_entries[0].cost
  slice_profit = (exit_rate - filled_orders[-1].safe_price) / filled_orders[-1].safe_price
  slice_profit_entry = (exit_rate - filled_entries[-1].safe_price) / filled_entries[-1].safe_price
  slice_profit_exit = (
    ((exit_rate - filled_exits[-1].safe_price) / filled_exits[-1].safe_price) if count_of_exits > 0 else 0.0
  )

  current_stake_amount = trade.amount * current_rate

  rebuy_mode_stakes = strategy.rebuy_mode_stakes_futures if strategy.is_futures_mode else strategy.rebuy_mode_stakes_spot
  max_sub_grinds = len(rebuy_mode_stakes)
  rebuy_mode_sub_thresholds = (
    strategy.rebuy_mode_thresholds_futures if strategy.is_futures_mode else strategy.rebuy_mode_thresholds_spot
  )
  partial_sell = False
  sub_grind_count = 0
  total_amount = 0.0
  total_cost = 0.0
  current_open_rate = 0.0
  current_grind_stake = 0.0
  current_grind_stake_profit = 0.0
  for order in reversed(filled_orders):
    if (order.ft_order_side == "buy") and (order is not filled_orders[0]):
      sub_grind_count += 1
      total_amount += order.safe_filled
      total_cost += order.safe_filled * order.safe_price
    elif order.ft_order_side == "sell":
      if (order.safe_remaining * exit_rate / (trade.leverage if strategy.is_futures_mode else 1.0)) > min_stake:
        partial_sell = True
      break
  if sub_grind_count > 0:
    current_open_rate = total_cost / total_amount
    current_grind_stake = total_amount * exit_rate * (1 - trade.fee_close)
    current_grind_stake_profit = current_grind_stake - total_cost

  if (not partial_sell) and (sub_grind_count < max_sub_grinds):
    if (
      ((0 <= sub_grind_count < max_sub_grinds) and (slice_profit_entry < rebuy_mode_sub_thresholds[sub_grind_count]))
      # and (
      #   (last_candle["close"] > (last_candle["close_max_12"] * 0.94))
      #   and (last_candle["close"] > (last_candle["close_max_24"] * 0.92))
      #   and (last_candle["close"] > (last_candle["close_max_48"] * 0.90))
      #   and (last_candle["close"] > (last_candle["high_max_24_1h"] * 0.88))
      #   and (last_candle["close"] > (last_candle["high_max_48_1h"] * 0.86))
      #   and (last_candle["btc_pct_close_max_72_5m"] < 0.03)
      #   and (last_candle["btc_pct_close_max_24_5m"] < 0.03)
      # )
      and (
        (last_candle["RSI_3"] > 10.0)
        and (last_candle["RSI_3_15m"] > 10.0)
        # and (last_candle["RSI_3_1h"] > 10.0)
        # and (last_candle["RSI_3_4h"] > 10.0)
        and (last_candle["RSI_14"] < 40.0)
        and (last_candle["ROC_2"] > -0.0)
        and (last_candle["close"] < (last_candle["EMA_26"] * 0.988))
      )
    ):
      buy_amount = slice_amount * rebuy_mode_stakes[sub_grind_count] / trade.leverage
      if buy_amount < (min_stake * 1.5):
        buy_amount = min_stake * 1.5
      if buy_amount > max_stake:
        return None
      strategy.dp.send_msg(
        strategy.notification_msg(
          "rebuy",
          tag="r",
          pair=trade.pair,
          rate=current_rate,
          stake_amount=buy_amount,
          profit_stake=profit_stake,
          profit_ratio=profit_ratio,
          stake_currency=strategy.config["stake_currency"],
        )
      )
      log.info(
        f"Rebuy (r) [{current_time}] [{trade.pair}] | Rate: {current_rate} | Stake amount: {buy_amount} | Profit (stake): {profit_stake} | Profit: {(profit_ratio * 100.0):.2f}%"
      )
      if has_order_tags:
        return buy_amount, "r"
      else:
        return buy_amount

  if strategy.derisk_enable and (
    profit_stake
    < (
      slice_amount * (strategy.rebuy_mode_derisk_futures if strategy.is_futures_mode else strategy.rebuy_mode_derisk_spot)
      # / (trade.leverage if strategy.is_futures_mode else 1.0)
    )
  ):
    sell_amount = trade.amount * exit_rate / trade.leverage - (min_stake * 1.55)
    ft_sell_amount = sell_amount * trade.leverage * (trade.stake_amount / trade.amount) / exit_rate
    if sell_amount > min_stake and ft_sell_amount > min_stake:
      grind_profit = 0.0
      strategy.dp.send_msg(
        f"❌​​ ​**Rebuy De-risk:** `Level 3`\n"
        f"🪙​ **Pair:** `{trade.pair}`\n"
        f"〽️​ **Rate:** `{exit_rate}`\n"
        f"💰 **Stake amount:** `{sell_amount}`\n"
        f"💵​ **Profit (stake):** `{profit_stake}`\n"
        f"💸 **Profit (percent):** `{(profit_ratio * 100.0):.2f}%`"
      )
      log.info(
        f"Rebuy De-risk Level 3 [{current_time}] [{trade.pair}] | Rate: {exit_rate} | Stake amount: {sell_amount} | Profit (stake): {profit_stake} | Profit: {(profit_ratio * 100.0):.2f}%"
      )
      if has_order_tags:
        return -ft_sell_amount, "derisk_level_3"
      else:
        return -ft_sell_amount

  return None

# Long Rebuy Adjust Trade Position v3
# ---------------------------------------------------------------------------------------------

def long_rebuy_adjust_trade_position_v3(
  strategy,
  trade: Trade,
  enter_tags,
  current_time: datetime,
  current_rate: float,
  current_profit: float,
  min_stake: Optional[float],
  max_stake: float,
  current_entry_rate: float,
  current_exit_rate: float,
  current_entry_profit: float,
  current_exit_profit: float,
  **kwargs,
) -> Optional[float]:
  # min/max stakes include leverage. The return amounts is before leverage.
  min_stake /= trade.leverage
  max_stake /= trade.leverage
  df, _ = strategy.dp.get_analyzed_dataframe(trade.pair, strategy.timeframe)
  if len(df) < 2:
    return None
  last_candle = df.iloc[-1].squeeze()
  previous_candle = df.iloc[-2].squeeze()

  # we already waiting for an order to get filled
  if trade.has_open_orders:
    return None

  filled_orders = trade.select_filled_orders()
  filled_entries = trade.select_filled_orders(trade.entry_side)
  filled_exits = trade.select_filled_orders(trade.exit_side)
  count_of_entries = trade.nr_of_successful_entries
  count_of_exits = trade.nr_of_successful_exits

  if count_of_entries == 0:
    return None

  has_order_tags = False
  if hasattr(filled_orders[0], "ft_order_tag"):
    has_order_tags = True

  exit_rate = current_rate
  if strategy.dp.runmode.value in ("live", "dry_run"):
    ticker = strategy.dp.ticker(trade.pair)
    if ("bid" in ticker) and ("ask" in ticker):
      if trade.is_short:
        if strategy.config["exit_pricing"]["price_side"] in ["ask", "other"]:
          if ticker["ask"] is not None:
            exit_rate = ticker["ask"]
      else:
        if strategy.config["exit_pricing"]["price_side"] in ["bid", "other"]:
          if ticker["bid"] is not None:
            exit_rate = ticker["bid"]

  profit_stake, profit_ratio, profit_current_stake_ratio, profit_init_ratio = strategy.calc_total_profit(
    trade, filled_entries, filled_exits, exit_rate
  )

  slice_amount = filled_entries[0].cost
  slice_profit = (exit_rate - filled_orders[-1].safe_price) / filled_orders[-1].safe_price
  slice_profit_entry = (exit_rate - filled_entries[-1].safe_price) / filled_entries[-1].safe_price
  slice_profit_exit = (
    ((exit_rate - filled_exits[-1].safe_price) / filled_exits[-1].safe_price) if count_of_exits > 0 else 0.0
  )

  current_stake_amount = trade.amount * current_rate

  rebuy_mode_stakes = (
    strategy.system_v3_rebuy_mode_stakes_futures if strategy.is_futures_mode else strategy.system_v3_rebuy_mode_stakes_spot
  )
  max_sub_grinds = len(rebuy_mode_stakes)
  rebuy_mode_sub_thresholds = (
    strategy.system_v3_rebuy_mode_thresholds_futures
    if strategy.is_futures_mode
    else strategy.system_v3_rebuy_mode_thresholds_spot
  )
  partial_sell = False
  sub_grind_count = 0
  total_amount = 0.0
  total_cost = 0.0
  current_open_rate = 0.0
  current_grind_stake = 0.0
  current_grind_stake_profit = 0.0
  for order in reversed(filled_orders):
    if (order.ft_order_side == "buy") and (order is not filled_orders[0]):
      sub_grind_count += 1
      total_amount += order.safe_filled
      total_cost += order.safe_filled * order.safe_price
    elif order.ft_order_side == "sell":
      if (order.safe_remaining * exit_rate / (trade.leverage if strategy.is_futures_mode else 1.0)) > min_stake:
        partial_sell = True
      break
  if sub_grind_count > 0:
    current_open_rate = total_cost / total_amount
    current_grind_stake = total_amount * exit_rate * (1 - trade.fee_close)
    current_grind_stake_profit = current_grind_stake - total_cost

  if (not partial_sell) and (sub_grind_count < max_sub_grinds):
    if (
      ((0 <= sub_grind_count < max_sub_grinds) and (slice_profit_entry < rebuy_mode_sub_thresholds[sub_grind_count]))
      and (last_candle["protections_long_global"] == True)
      and (
        (last_candle["RSI_3"] > 10.0)
        and (last_candle["RSI_3_15m"] > 10.0)
        and (last_candle["AROONU_14"] < 30.0)
        and (last_candle["AROONU_14_15m"] < 30.0)
        and (last_candle["close"] < (last_candle["EMA_26"] * 0.988))
      )
    ):
      buy_amount = slice_amount * rebuy_mode_stakes[sub_grind_count] / trade.leverage
      if buy_amount < (min_stake * 1.5):
        buy_amount = min_stake * 1.5
      if buy_amount > max_stake:
        return None
      strategy.dp.send_msg(
        strategy.notification_msg(
          "rebuy",
          tag="r",
          pair=trade.pair,
          rate=current_rate,
          stake_amount=buy_amount,
          profit_stake=profit_stake,
          profit_ratio=profit_ratio,
          stake_currency=strategy.config["stake_currency"],
        )
      )
      log.info(
        f"Rebuy (r) [{current_time}] [{trade.pair}] | Rate: {current_rate} | Stake amount: {buy_amount} | Profit (stake): {profit_stake} | Profit: {(profit_ratio * 100.0):.2f}%"
      )
      if has_order_tags:
        return buy_amount, "r"
      else:
        return buy_amount

  return None

def short_rebuy_adjust_trade_position(
  strategy,
  trade: Trade,
  enter_tags,
  current_time: datetime,
  current_rate: float,
  current_profit: float,
  min_stake: Optional[float],
  max_stake: float,
  current_entry_rate: float,
  current_exit_rate: float,
  current_entry_profit: float,
  current_exit_profit: float,
  **kwargs,
) -> Optional[float]:
  # min/max stakes include leverage. The return amounts is before leverage.
  min_stake /= trade.leverage
  max_stake /= trade.leverage
  df, _ = strategy.dp.get_analyzed_dataframe(trade.pair, strategy.timeframe)
  if len(df) < 2:
    return None
  last_candle = df.iloc[-1].squeeze()
  previous_candle = df.iloc[-2].squeeze()

  # we already waiting for an order to get filled
  if trade.has_open_orders:
    return None

  filled_orders = trade.select_filled_orders()
  filled_entries = trade.select_filled_orders(trade.entry_side)
  filled_exits = trade.select_filled_orders(trade.exit_side)
  count_of_entries = trade.nr_of_successful_entries
  count_of_exits = trade.nr_of_successful_exits

  if count_of_entries == 0:
    return None

  has_order_tags = False
  if hasattr(filled_orders[0], "ft_order_tag"):
    has_order_tags = True

  # The first exit is de-risk (providing the trade is still open)
  if (count_of_exits > 0) and (filled_exits[0].ft_order_tag in ["derisk_level_3"]):
    return strategy.short_grind_adjust_trade_position_v2(
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

  exit_rate = current_rate
  if strategy.dp.runmode.value in ("live", "dry_run"):
    ticker = strategy.dp.ticker(trade.pair)
    if ("bid" in ticker) and ("ask" in ticker):
      if trade.is_short:
        if strategy.config["exit_pricing"]["price_side"] in ["ask", "other"]:
          if ticker["ask"] is not None:
            exit_rate = ticker["ask"]
      else:
        if strategy.config["exit_pricing"]["price_side"] in ["bid", "other"]:
          if ticker["bid"] is not None:
            exit_rate = ticker["bid"]

  profit_stake, profit_ratio, profit_current_stake_ratio, profit_init_ratio = strategy.calc_total_profit(
    trade, filled_entries, filled_exits, exit_rate
  )

  slice_amount = filled_entries[0].cost
  slice_profit = (exit_rate - filled_orders[-1].safe_price) / filled_orders[-1].safe_price
  slice_profit_entry = (exit_rate - filled_entries[-1].safe_price) / filled_entries[-1].safe_price
  slice_profit_exit = (
    ((exit_rate - filled_exits[-1].safe_price) / filled_exits[-1].safe_price) if count_of_exits > 0 else 0.0
  )

  current_stake_amount = trade.amount * current_rate

  rebuy_mode_stakes = strategy.rebuy_mode_stakes_futures if strategy.is_futures_mode else strategy.rebuy_mode_stakes_spot
  max_sub_grinds = len(rebuy_mode_stakes)
  rebuy_mode_sub_thresholds = (
    strategy.rebuy_mode_thresholds_futures if strategy.is_futures_mode else strategy.rebuy_mode_thresholds_spot
  )
  partial_sell = False
  sub_grind_count = 0
  total_amount = 0.0
  total_cost = 0.0
  current_open_rate = 0.0
  current_grind_stake = 0.0
  current_grind_stake_profit = 0.0
  for order in reversed(filled_orders):
    if (order.ft_order_side == "sell") and (order is not filled_orders[0]):
      sub_grind_count += 1
      total_amount += order.safe_filled
      total_cost += order.safe_filled * order.safe_price
    elif order.ft_order_side == "buy":
      if (order.safe_remaining * exit_rate / (trade.leverage if strategy.is_futures_mode else 1.0)) > min_stake:
        partial_sell = True
      break
  if sub_grind_count > 0:
    current_open_rate = total_cost / total_amount
    current_grind_stake = total_amount * exit_rate * (1 - trade.fee_close)
    current_grind_stake_profit = current_grind_stake - total_cost

  if (not partial_sell) and (sub_grind_count < max_sub_grinds):
    if (
      (0 <= sub_grind_count < max_sub_grinds) and (-slice_profit_entry < rebuy_mode_sub_thresholds[sub_grind_count])
    ) and (
      (last_candle["RSI_3"] < 90.0)
      and (last_candle["RSI_3_15m"] < 90.0)
      # and (last_candle["RSI_3_1h"] < 90.0)
      # and (last_candle["RSI_3_4h"] < 90.0)
      and (last_candle["RSI_14"] > 60.0)
      and (last_candle["ROC_2"] < 0.0)
      and (last_candle["close"] > (last_candle["EMA_26"] * 1.012))
    ):
      buy_amount = slice_amount * rebuy_mode_stakes[sub_grind_count] / trade.leverage
      if buy_amount < (min_stake * 1.5):
        buy_amount = min_stake * 1.5
      if buy_amount > max_stake:
        return None
      strategy.dp.send_msg(
        strategy.notification_msg(
          "rebuy",
          tag="r",
          pair=trade.pair,
          rate=current_rate,
          stake_amount=buy_amount,
          profit_stake=profit_stake,
          profit_ratio=profit_ratio,
          stake_currency=strategy.config["stake_currency"],
        )
      )
      log.info(
        f"Rebuy (r) [{current_time}] [{trade.pair}] | Rate: {current_rate} | Stake amount: {buy_amount} | Profit (stake): {profit_stake} | Profit: {(profit_ratio * 100.0):.2f}%"
      )
      if has_order_tags:
        return buy_amount, "r"
      else:
        return buy_amount

  if strategy.derisk_enable and (
    profit_stake
    < (
      slice_amount * (strategy.rebuy_mode_derisk_futures if strategy.is_futures_mode else strategy.rebuy_mode_derisk_spot)
      # / (trade.leverage if strategy.is_futures_mode else 1.0)
    )
  ):
    sell_amount = trade.amount * exit_rate / trade.leverage - (min_stake * 1.55)
    ft_sell_amount = sell_amount * trade.leverage * (trade.stake_amount / trade.amount) / exit_rate
    if sell_amount > min_stake and ft_sell_amount > min_stake:
      grind_profit = 0.0
      strategy.dp.send_msg(
        f"❌​​ ​**Rebuy De-risk:** `Level 3`\n"
        f"🪙​ **Pair:** `{trade.pair}`\n"
        f"〽️​ **Rate:** `{exit_rate}`\n"
        f"💰 **Stake amount:** `{sell_amount}`\n"
        f"💵​ **Profit (stake):** `{profit_stake}`\n"
        f"💸 **Profit (percent):** `{(profit_ratio * 100.0):.2f}%`"
      )
      log.info(
        f"Rebuy De-risk Level 3 [{current_time}] [{trade.pair}] | Rate: {exit_rate} | Stake amount: {sell_amount} | Profit (stake): {profit_stake} | Profit: {(profit_ratio * 100.0):.2f}%"
      )
      if has_order_tags:
        return -ft_sell_amount, "derisk_level_3"
      else:
        return -ft_sell_amount

  return None

# Short Rebuy Adjust Trade Position v3
# ---------------------------------------------------------------------------------------------

def short_rebuy_adjust_trade_position_v3(
  strategy,
  trade: Trade,
  enter_tags,
  current_time: datetime,
  current_rate: float,
  current_profit: float,
  min_stake: Optional[float],
  max_stake: float,
  current_entry_rate: float,
  current_exit_rate: float,
  current_entry_profit: float,
  current_exit_profit: float,
  **kwargs,
) -> Optional[float]:
  # min/max stakes include leverage. The return amounts is before leverage.
  min_stake /= trade.leverage
  max_stake /= trade.leverage
  df, _ = strategy.dp.get_analyzed_dataframe(trade.pair, strategy.timeframe)
  if len(df) < 2:
    return None
  last_candle = df.iloc[-1].squeeze()
  previous_candle = df.iloc[-2].squeeze()

  # we already waiting for an order to get filled
  if trade.has_open_orders:
    return None

  filled_orders = trade.select_filled_orders()
  filled_entries = trade.select_filled_orders(trade.entry_side)
  filled_exits = trade.select_filled_orders(trade.exit_side)
  count_of_entries = trade.nr_of_successful_entries
  count_of_exits = trade.nr_of_successful_exits

  if count_of_entries == 0:
    return None

  has_order_tags = False
  if hasattr(filled_orders[0], "ft_order_tag"):
    has_order_tags = True

  exit_rate = current_rate
  if strategy.dp.runmode.value in ("live", "dry_run"):
    ticker = strategy.dp.ticker(trade.pair)
    if ("bid" in ticker) and ("ask" in ticker):
      if trade.is_short:
        if strategy.config["exit_pricing"]["price_side"] in ["ask", "other"]:
          if ticker["ask"] is not None:
            exit_rate = ticker["ask"]
      else:
        if strategy.config["exit_pricing"]["price_side"] in ["bid", "other"]:
          if ticker["bid"] is not None:
            exit_rate = ticker["bid"]

  profit_stake, profit_ratio, profit_current_stake_ratio, profit_init_ratio = strategy.calc_total_profit(
    trade, filled_entries, filled_exits, exit_rate
  )

  slice_amount = filled_entries[0].cost
  slice_profit = (exit_rate - filled_orders[-1].safe_price) / filled_orders[-1].safe_price
  slice_profit_entry = (exit_rate - filled_entries[-1].safe_price) / filled_entries[-1].safe_price
  slice_profit_exit = (
    ((exit_rate - filled_exits[-1].safe_price) / filled_exits[-1].safe_price) if count_of_exits > 0 else 0.0
  )

  current_stake_amount = trade.amount * current_rate

  rebuy_mode_stakes = (
    strategy.system_v3_rebuy_mode_stakes_futures if strategy.is_futures_mode else strategy.system_v3_rebuy_mode_stakes_spot
  )
  max_sub_grinds = len(rebuy_mode_stakes)
  rebuy_mode_sub_thresholds = (
    strategy.system_v3_rebuy_mode_thresholds_futures
    if strategy.is_futures_mode
    else strategy.system_v3_rebuy_mode_thresholds_spot
  )
  partial_sell = False
  sub_grind_count = 0
  total_amount = 0.0
  total_cost = 0.0
  current_open_rate = 0.0
  current_grind_stake = 0.0
  current_grind_stake_profit = 0.0
  for order in reversed(filled_orders):
    if (order.ft_order_side == "sell") and (order is not filled_orders[0]):
      sub_grind_count += 1
      total_amount += order.safe_filled
      total_cost += order.safe_filled * order.safe_price
    elif order.ft_order_side == "buy":
      if (order.safe_remaining * exit_rate / (trade.leverage if strategy.is_futures_mode else 1.0)) > min_stake:
        partial_sell = True
      break
  if sub_grind_count > 0:
    current_open_rate = total_cost / total_amount
    current_grind_stake = total_amount * exit_rate * (1 - trade.fee_close)
    current_grind_stake_profit = current_grind_stake - total_cost

  if (not partial_sell) and (sub_grind_count < max_sub_grinds):
    if (
      (
        (0 <= sub_grind_count < max_sub_grinds)
        and (-slice_profit_entry < rebuy_mode_sub_thresholds[sub_grind_count])
      )
      and (last_candle["protections_long_global"] == True)
      and (
        (last_candle["RSI_3"] < 90.0)
        and (last_candle["RSI_3_15m"] < 90.0)
        and (last_candle["AROOND_14"] < 30.0)
        and (last_candle["AROOND_14_15m"] < 30.0)
        and (last_candle["close"] < (last_candle["EMA_26"] * 1.012))
      )
    ):
      buy_amount = slice_amount * rebuy_mode_stakes[sub_grind_count] / trade.leverage
      if buy_amount < (min_stake * 1.5):
        buy_amount = min_stake * 1.5
      if buy_amount > max_stake:
        return None
      strategy.dp.send_msg(
        strategy.notification_msg(
          "rebuy",
          tag="r",
          pair=trade.pair,
          rate=current_rate,
          stake_amount=buy_amount,
          profit_stake=profit_stake,
          profit_ratio=profit_ratio,
          stake_currency=strategy.config["stake_currency"],
        )
      )
      log.info(
        f"Rebuy (r) [{current_time}] [{trade.pair}] | Rate: {current_rate} | Stake amount: {buy_amount} | Profit (stake): {profit_stake} | Profit: {(profit_ratio * 100.0):.2f}%"
      )
      if has_order_tags:
        return buy_amount, "r"
      else:
        return buy_amount

  return None

