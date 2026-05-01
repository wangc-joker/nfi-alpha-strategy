param(
    [Parameter(Mandatory = $true)]
    [string]$BacktestZip,

    [string]$Strategy,

    [int]$TopWorstMae = 5
)

$ErrorActionPreference = "Stop"

if (-not (Test-Path -LiteralPath $BacktestZip -PathType Leaf)) {
    throw "Backtest zip not found: $BacktestZip"
}

$workDir = Join-Path ([System.IO.Path]::GetTempPath()) ("nfi-risk-" + [System.Guid]::NewGuid().ToString("N"))
New-Item -ItemType Directory -Path $workDir | Out-Null

try {
    tar -xf $BacktestZip -C $workDir
    $jsonFile = Get-ChildItem -LiteralPath $workDir -Filter "*.json" |
        Where-Object { $_.Name -notlike "*_config.json" -and $_.Name -notlike "*.meta.json" } |
        Select-Object -First 1

    if (-not $jsonFile) {
        throw "No result json found in $BacktestZip"
    }

    $result = Get-Content -LiteralPath $jsonFile.FullName -Raw | ConvertFrom-Json

    if (-not $Strategy) {
        $Strategy = ($result.strategy.PSObject.Properties | Select-Object -First 1).Name
    }

    $strategyResult = $result.strategy.$Strategy
    if (-not $strategyResult) {
        throw "Strategy '$Strategy' not found in $BacktestZip"
    }

    $trades = @($strategyResult.trades)
    $maeRows = foreach ($trade in $trades) {
        $leverage = [double]$trade.leverage
        if ($leverage -eq 0) {
            $leverage = 1
        }

        $openRate = [double]$trade.open_rate
        if ($trade.is_short) {
            $worstRate = [double]$trade.max_rate
            $rawMove = ($openRate / $worstRate) - 1
        }
        else {
            $worstRate = [double]$trade.min_rate
            $rawMove = ($worstRate / $openRate) - 1
        }

        $maeRatio = $rawMove * $leverage
        $duration = [TimeSpan]::FromMinutes([double]$trade.trade_duration)

        [pscustomobject]@{
            pair = $trade.pair
            enter_tag = ([string]$trade.enter_tag).Trim()
            open_date = $trade.open_date
            close_date = $trade.close_date
            duration = "{0}d {1}h {2}m" -f $duration.Days, $duration.Hours, $duration.Minutes
            open_rate = [math]::Round($openRate, 8)
            worst_rate = [math]::Round($worstRate, 8)
            leverage = $leverage
            mae_pct = [math]::Round($maeRatio * 100, 2)
            mae_abs_initial_stake = [math]::Round(([double]$trade.stake_amount * $maeRatio), 3)
            mae_abs_max_stake = [math]::Round(([double]$trade.max_stake_amount * $maeRatio), 3)
            final_profit_pct = [math]::Round(([double]$trade.profit_ratio * 100), 2)
            final_profit_abs = [math]::Round([double]$trade.profit_abs, 3)
            exit_reason = $trade.exit_reason
            is_open = $trade.is_open
        }
    }

    $worstMae = @($maeRows | Sort-Object mae_pct | Select-Object -First $TopWorstMae)
    $longestTrade = @($trades | Sort-Object trade_duration -Descending | Select-Object -First 1)

    $longestDuration = "0d 0h 0m"
    if ($longestTrade.Count -gt 0) {
        $duration = [TimeSpan]::FromMinutes([double]$longestTrade[0].trade_duration)
        $longestDuration = "{0}d {1}h {2}m" -f $duration.Days, $duration.Hours, $duration.Minutes
    }

    $summary = [pscustomobject]@{
        strategy = $Strategy
        trades = $trades.Count
        profit_usdt = [math]::Round([double]$strategyResult.profit_total_abs, 3)
        profit_pct = [math]::Round([double]$strategyResult.profit_total * 100, 2)
        winrate_pct = [math]::Round([double]$strategyResult.winrate * 100, 2)
        drawdown_usdt = [math]::Round([double]$strategyResult.max_drawdown_abs, 3)
        drawdown_pct = [math]::Round([double]$strategyResult.max_drawdown_account * 100, 2)
        longest_pair = if ($longestTrade.Count -gt 0) { $longestTrade[0].pair } else { "" }
        longest_duration = $longestDuration
        worst_mae_pct = if ($worstMae.Count -gt 0) { $worstMae[0].mae_pct } else { 0 }
        worst_mae_pair = if ($worstMae.Count -gt 0) { $worstMae[0].pair } else { "" }
        worst_mae_tag = if ($worstMae.Count -gt 0) { $worstMae[0].enter_tag } else { "" }
    }

    $output = [pscustomobject]@{
        summary = $summary
        worst_mae_trades = $worstMae
    }

    $output | ConvertTo-Json -Depth 8
}
finally {
    if (Test-Path -LiteralPath $workDir) {
        Remove-Item -LiteralPath $workDir -Recurse -Force
    }
}
