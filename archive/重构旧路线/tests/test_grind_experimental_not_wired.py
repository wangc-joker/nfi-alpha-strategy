import ast
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
STRATEGY_PATH = ROOT / "strategies" / "NFIRefactorStrategy.py"


class GrindExperimentalNotWiredTest(unittest.TestCase):
  def setUp(self):
    self.source = STRATEGY_PATH.read_text(encoding="utf-8")
    self.tree = ast.parse(self.source)

  def get_refactor_strategy_class(self):
    for node in self.tree.body:
      if isinstance(node, ast.ClassDef) and node.name == "NFIRefactorStrategy":
        return node
    self.fail("NFIRefactorStrategy class not found")

  def test_experimental_grind_adjustment_module_is_not_imported_by_strategy(self):
    self.assertNotIn("from nfi_refactor.position import grind_adjustment", self.source)
    self.assertNotIn("from nfi_refactor.position.grind_adjustment", self.source)
    self.assertNotIn("import nfi_refactor.position.grind_adjustment", self.source)

  def test_original_grind_adjustment_methods_remain_inherited(self):
    strategy_class = self.get_refactor_strategy_class()
    method_names = {
      node.name
      for node in strategy_class.body
      if isinstance(node, ast.FunctionDef)
    }

    self.assertNotIn("long_grind_adjust_trade_position_v2", method_names)
    self.assertNotIn("long_grind_adjust_trade_position_v3", method_names)
    self.assertNotIn("short_grind_adjust_trade_position_v2", method_names)
    self.assertNotIn("short_grind_adjust_trade_position_v3", method_names)


if __name__ == "__main__":
  unittest.main()
