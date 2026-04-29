import sys
import unittest
from pathlib import Path
from types import SimpleNamespace


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "strategies"))

from nfi_refactor.position.adjustment_context import (  # noqa: E402
  AdjustmentCallContext,
  AdjustmentModeState,
)
from nfi_refactor.position.adjustment_rebuy_route import (  # noqa: E402
  matches_long_rebuy_adjustment,
  matches_short_rebuy_adjustment,
  route_rebuy_adjustment,
  select_long_rebuy_adjustment_func,
  select_short_rebuy_adjustment_func,
)


class AdjustmentRebuyRouteTest(unittest.TestCase):
  def setUp(self):
    self.strategy = SimpleNamespace(
      long_rebuy_mode_tags=["lr"],
      long_grind_mode_tags=["lg"],
      short_rebuy_mode_tags=["sr"],
      short_grind_mode_tags=["sg"],
    )
    self.strategy.long_rebuy_adjust_trade_position = lambda *args: ("long_default", args)
    self.strategy.long_rebuy_adjust_trade_position_v3 = lambda *args: ("long_v3", args)
    self.strategy.short_rebuy_adjust_trade_position = lambda *args: ("short_default", args)
    self.strategy.short_rebuy_adjust_trade_position_v3 = lambda *args: ("short_v3", args)

  def make_context(self, enter_tags=None, is_short=False):
    return AdjustmentCallContext(
      trade=SimpleNamespace(is_short=is_short),
      enter_tags=enter_tags or [],
      current_time="time",
      current_rate=1.1,
      current_profit=2.2,
      min_stake=3.3,
      max_stake=4.4,
      current_entry_rate=5.5,
      current_exit_rate=6.6,
      current_entry_profit=7.7,
      current_exit_profit=8.8,
    )

  def make_state(self, is_system_v3_family=False):
    return AdjustmentModeState(
      is_long_grind_mode=False,
      is_long_btc_mode=False,
      is_short_grind_mode=False,
      is_v2_date=True,
      is_system_v3_family=is_system_v3_family,
    )

  def assert_handler_args_match_context(self, args, context):
    self.assertEqual(
      args,
      (
        context.trade,
        context.enter_tags,
        "time",
        1.1,
        2.2,
        3.3,
        4.4,
        5.5,
        6.6,
        7.7,
        8.8,
      ),
    )

  def test_long_rebuy_matching_accepts_rebuy_and_rebuy_grind_tags(self):
    self.assertTrue(matches_long_rebuy_adjustment(self.strategy, ["lr"]))
    self.assertTrue(matches_long_rebuy_adjustment(self.strategy, ["lr", "lg"]))
    self.assertFalse(matches_long_rebuy_adjustment(self.strategy, ["lg"]))
    self.assertFalse(matches_long_rebuy_adjustment(self.strategy, ["unknown"]))
    self.assertFalse(matches_long_rebuy_adjustment(self.strategy, ["lr", "unknown"]))

  def test_short_rebuy_matching_accepts_rebuy_and_rebuy_grind_tags(self):
    self.assertTrue(matches_short_rebuy_adjustment(self.strategy, ["sr"]))
    self.assertTrue(matches_short_rebuy_adjustment(self.strategy, ["sr", "sg"]))
    self.assertFalse(matches_short_rebuy_adjustment(self.strategy, ["sg"]))
    self.assertFalse(matches_short_rebuy_adjustment(self.strategy, ["unknown"]))
    self.assertFalse(matches_short_rebuy_adjustment(self.strategy, ["sr", "unknown"]))

  def test_long_rebuy_selector_preserves_default_and_v3_choice(self):
    self.assertIs(
      select_long_rebuy_adjustment_func(self.strategy, self.make_state()),
      self.strategy.long_rebuy_adjust_trade_position,
    )
    self.assertIs(
      select_long_rebuy_adjustment_func(
        self.strategy,
        self.make_state(is_system_v3_family=True),
      ),
      self.strategy.long_rebuy_adjust_trade_position_v3,
    )

  def test_short_rebuy_selector_preserves_default_and_v3_choice(self):
    self.assertIs(
      select_short_rebuy_adjustment_func(self.strategy, self.make_state()),
      self.strategy.short_rebuy_adjust_trade_position,
    )
    self.assertIs(
      select_short_rebuy_adjustment_func(
        self.strategy,
        self.make_state(is_system_v3_family=True),
      ),
      self.strategy.short_rebuy_adjust_trade_position_v3,
    )

  def test_route_rebuy_adjustment_executes_long_default_handler(self):
    context = self.make_context(["lr"], is_short=False)
    handled, adjustment = route_rebuy_adjustment(self.strategy, context, self.make_state())

    self.assertTrue(handled)
    self.assertEqual(adjustment[0], "long_default")
    self.assert_handler_args_match_context(adjustment[1], context)

  def test_route_rebuy_adjustment_executes_short_v3_handler(self):
    context = self.make_context(["sr"], is_short=True)
    handled, adjustment = route_rebuy_adjustment(
      self.strategy,
      context,
      self.make_state(is_system_v3_family=True),
    )

    self.assertTrue(handled)
    self.assertEqual(adjustment[0], "short_v3")
    self.assert_handler_args_match_context(adjustment[1], context)

  def test_route_rebuy_adjustment_returns_unhandled_for_unmatched_tags(self):
    self.assertEqual(
      route_rebuy_adjustment(
        self.strategy,
        self.make_context(["unknown"], is_short=False),
        self.make_state(),
      ),
      (False, None),
    )
    self.assertEqual(
      route_rebuy_adjustment(
        self.strategy,
        self.make_context(["unknown"], is_short=True),
        self.make_state(),
      ),
      (False, None),
    )


if __name__ == "__main__":
  unittest.main()
