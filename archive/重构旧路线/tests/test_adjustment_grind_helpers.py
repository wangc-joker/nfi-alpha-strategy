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
from nfi_refactor.position.adjustment_grind_route import (  # noqa: E402
  route_long_grind_adjustment,
  route_short_grind_adjustment,
  select_grind_route_func,
)
from nfi_refactor.position.adjustment_grind_selectors import (  # noqa: E402
  select_long_grind_adjustment_func,
  select_short_grind_adjustment_func,
)
from nfi_refactor.position.adjustment_grind_tags import (  # noqa: E402
  get_long_grind_v2_or_v3_known_tags,
  get_long_grind_v2_or_v3_trigger_tags,
  get_short_grind_v2_or_v3_known_tags,
  get_short_grind_v2_or_v3_trigger_tags,
  matches_long_grind_adjustment_v2_or_v3,
  matches_short_grind_adjustment_v2_or_v3,
)


class AdjustmentGrindHelpersTest(unittest.TestCase):
  def setUp(self):
    self.strategy = SimpleNamespace(
      long_normal_mode_tags=["ln"],
      long_pump_mode_tags=["lp"],
      long_quick_mode_tags=["lq"],
      long_high_profit_mode_tags=["lh"],
      long_rapid_mode_tags=["lr"],
      long_top_coins_mode_tags=["lt"],
      long_scalp_mode_tags=["ls"],
      long_rebuy_mode_tags=["lrb"],
      long_grind_mode_tags=["lg"],
      long_btc_mode_tags=["lbtc"],
      short_normal_mode_tags=["sn"],
      short_pump_mode_tags=["sp"],
      short_quick_mode_tags=["sq"],
      short_high_profit_mode_tags=["sh"],
      short_rapid_mode_tags=["sr"],
      short_top_coins_mode_tags=["st"],
      short_scalp_mode_tags=["ss"],
      short_rebuy_mode_tags=["srb"],
      short_grind_mode_tags=["sg"],
    )
    self.strategy.long_grind_adjust_trade_position = lambda *args: "long_default"
    self.strategy.long_grind_adjust_trade_position_v2 = lambda *args: "long_v2"
    self.strategy.long_grind_adjust_trade_position_v3 = lambda *args: "long_v3"
    self.strategy.short_grind_adjust_trade_position = lambda *args: "short_default"
    self.strategy.short_grind_adjust_trade_position_v2 = lambda *args: "short_v2"
    self.strategy.short_grind_adjust_trade_position_v3 = lambda *args: "short_v3"

  def make_context(self, enter_tags=None, is_short=False):
    return AdjustmentCallContext(
      trade=SimpleNamespace(is_short=is_short),
      enter_tags=enter_tags or [],
      current_time=None,
      current_rate=0.0,
      current_profit=0.0,
      min_stake=None,
      max_stake=0.0,
      current_entry_rate=0.0,
      current_exit_rate=0.0,
      current_entry_profit=0.0,
      current_exit_profit=0.0,
    )

  def make_state(
    self,
    is_long_grind_mode=False,
    is_long_btc_mode=False,
    is_short_grind_mode=False,
    is_v2_date=True,
    is_system_v3_family=False,
  ):
    return AdjustmentModeState(
      is_long_grind_mode=is_long_grind_mode,
      is_long_btc_mode=is_long_btc_mode,
      is_short_grind_mode=is_short_grind_mode,
      is_v2_date=is_v2_date,
      is_system_v3_family=is_system_v3_family,
    )

  def test_long_grind_tag_sets_keep_original_order(self):
    self.assertEqual(
      get_long_grind_v2_or_v3_trigger_tags(self.strategy),
      ["ln", "lp", "lq", "lh", "lr", "lt", "ls"],
    )
    self.assertEqual(
      get_long_grind_v2_or_v3_known_tags(self.strategy),
      ["ln", "lp", "lq", "lh", "lr", "lt", "ls", "lrb", "lg", "lbtc"],
    )

  def test_short_grind_tag_sets_keep_original_order(self):
    self.assertEqual(
      get_short_grind_v2_or_v3_trigger_tags(self.strategy),
      ["sn", "sp", "sq", "sh", "sr", "st", "ss"],
    )
    self.assertEqual(
      get_short_grind_v2_or_v3_known_tags(self.strategy),
      ["sn", "sp", "sq", "sh", "sr", "st", "ss", "srb", "sg"],
    )

  def test_grind_v2_or_v3_matching_preserves_unknown_tag_fallback(self):
    self.assertTrue(matches_long_grind_adjustment_v2_or_v3(self.strategy, ["ln"]))
    self.assertTrue(matches_long_grind_adjustment_v2_or_v3(self.strategy, ["unknown"]))
    self.assertFalse(matches_long_grind_adjustment_v2_or_v3(self.strategy, ["lg"]))
    self.assertTrue(matches_short_grind_adjustment_v2_or_v3(self.strategy, ["sn"]))
    self.assertTrue(matches_short_grind_adjustment_v2_or_v3(self.strategy, ["unknown"]))
    self.assertFalse(matches_short_grind_adjustment_v2_or_v3(self.strategy, ["sg"]))

  def test_select_grind_route_func_uses_trade_direction(self):
    self.assertIs(select_grind_route_func(self.make_context(is_short=False)), route_long_grind_adjustment)
    self.assertIs(select_grind_route_func(self.make_context(is_short=True)), route_short_grind_adjustment)

  def test_long_selector_preserves_v3_default_and_v2_order(self):
    context = self.make_context(["ln"], is_short=False)
    self.assertIs(
      select_long_grind_adjustment_func(
        self.strategy,
        context,
        self.make_state(is_system_v3_family=True),
      ),
      self.strategy.long_grind_adjust_trade_position_v3,
    )
    self.assertIs(
      select_long_grind_adjustment_func(
        self.strategy,
        context,
        self.make_state(is_system_v3_family=False, is_v2_date=True),
      ),
      self.strategy.long_grind_adjust_trade_position_v2,
    )
    self.assertIs(
      select_long_grind_adjustment_func(
        self.strategy,
        context,
        self.make_state(is_long_grind_mode=True),
      ),
      self.strategy.long_grind_adjust_trade_position,
    )

  def test_short_selector_preserves_v3_default_and_v2_order(self):
    context = self.make_context(["sn"], is_short=True)
    self.assertIs(
      select_short_grind_adjustment_func(
        self.strategy,
        context,
        self.make_state(is_system_v3_family=True),
      ),
      self.strategy.short_grind_adjust_trade_position_v3,
    )
    self.assertIs(
      select_short_grind_adjustment_func(
        self.strategy,
        context,
        self.make_state(is_system_v3_family=False, is_v2_date=True),
      ),
      self.strategy.short_grind_adjust_trade_position_v2,
    )
    self.assertIs(
      select_short_grind_adjustment_func(
        self.strategy,
        context,
        self.make_state(is_short_grind_mode=True),
      ),
      self.strategy.short_grind_adjust_trade_position,
    )


if __name__ == "__main__":
  unittest.main()
