from NostalgiaForInfinityX7 import NostalgiaForInfinityX7


class NFIRefactorStrategy(NostalgiaForInfinityX7):
    """
    Parity adapter for the NFI modular refactor.

    This first version intentionally inherits the original strategy behavior.
    We will move logic into modules step by step, with backtest parity checks
    after each extraction.
    """

    def version(self) -> str:
        return "nfi-refactor-parity-adapter-0.1.0"
