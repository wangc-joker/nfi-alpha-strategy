"""Advanced exit mode compatibility module.

The mode-level routers live in smaller mode-specific modules so this file can
remain a stable import surface for the strategy adapter.
"""

from nfi_refactor.exits.mode_high_profit import long_exit_high_profit, short_exit_high_profit
from nfi_refactor.exits.mode_normal import long_exit_normal, short_exit_normal
from nfi_refactor.exits.mode_pump import long_exit_pump, short_exit_pump
from nfi_refactor.exits.mode_quick import long_exit_quick, short_exit_quick
from nfi_refactor.exits.mode_rapid import long_exit_rapid, short_exit_rapid
from nfi_refactor.exits.mode_rebuy import long_exit_rebuy, short_exit_rebuy

__all__ = [
    "long_exit_high_profit",
    "short_exit_high_profit",
    "long_exit_normal",
    "short_exit_normal",
    "long_exit_pump",
    "short_exit_pump",
    "long_exit_quick",
    "short_exit_quick",
    "long_exit_rapid",
    "short_exit_rapid",
    "long_exit_rebuy",
    "short_exit_rebuy",
]
