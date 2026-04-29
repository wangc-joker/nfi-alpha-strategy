def global_loss_exit(strategy, trade, current_profit: float):
    """Return an exit reason when a trade breaches the configured loss cap."""

    if not strategy.alpha_global_loss_stop_enabled:
        return None

    if current_profit <= -abs(strategy.alpha_global_loss_ratio):
        return "alpha_global_loss_stop_5pct"

    return None
