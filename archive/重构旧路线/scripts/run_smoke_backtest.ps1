param(
    [string]$FtUserDataRoot = "D:\test\ft_userdata",
    [string]$Timerange = "20260401-20260410"
)

$ErrorActionPreference = "Stop"

$repoRoot = Split-Path -Parent $PSScriptRoot
$targetStrategyDir = Join-Path $FtUserDataRoot "user_data\strategies"
$targetConfig = Join-Path $FtUserDataRoot "user_data\config.backtest.alpha.futures.smoke.json"
$sourceConfig = Join-Path $repoRoot "configs\config.backtest.alpha.futures.smoke.json"

powershell -ExecutionPolicy Bypass -File (Join-Path $repoRoot "scripts\sync_strategy_to_ft_userdata.ps1") -TargetStrategyDir $targetStrategyDir
Copy-Item -LiteralPath $sourceConfig -Destination $targetConfig -Force

docker compose run --rm freqtrade backtesting `
    --config /freqtrade/user_data/config.backtest.alpha.futures.smoke.json `
    --strategy-path /freqtrade/user_data/strategies `
    --strategy AlphaRegimeStrategy `
    --timerange $Timerange `
    --timeframe 5m

