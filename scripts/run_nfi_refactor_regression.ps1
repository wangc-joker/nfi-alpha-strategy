param(
    [string]$FtUserDataRoot = "D:\test\ft_userdata",
    [string]$SmokeTimerange = "20260401-20260403",
    [string]$HalfyearTimerange = "20251016-20260415",
    [switch]$RunHalfyear
)

$ErrorActionPreference = "Stop"

$repoRoot = Split-Path -Parent $PSScriptRoot
$composeFile = Join-Path $FtUserDataRoot "docker-compose.yml"
$targetStrategyDir = Join-Path $FtUserDataRoot "user_data\strategies"
$configName = "config.backtest.dynamic.top40.302u.max2.halfyear.balanced.json"

function Invoke-Step {
    param(
        [string]$Name,
        [scriptblock]$Command
    )

    Write-Host ""
    Write-Host "==> $Name"
    & $Command
    Write-Host "OK: $Name"
}

function Invoke-FreqtradePython {
    param([string[]]$Args)

    docker compose -f $composeFile run --rm --entrypoint python `
        -v "${repoRoot}:/work" `
        freqtrade @Args
}

function Invoke-Backtest {
    param(
        [string]$Timerange,
        [switch]$NoCache
    )

    $args = @(
        "backtesting",
        "--userdir", "/freqtrade/user_data",
        "--strategy-path", "/freqtrade/user_data/strategies",
        "--config", "/freqtrade/user_data/$configName",
        "--strategy", "NFIRefactorStrategy",
        "--timerange", $Timerange,
        "--export", "none"
    )

    if ($NoCache) {
        $args += @("--cache", "none")
    }

    docker compose -f $composeFile run --rm freqtrade @args
}

Invoke-Step "Unit tests" {
    Invoke-FreqtradePython @(
        "-m", "unittest",
        "discover",
        "-s", "/work/tests",
        "-p", "test_*.py"
    )
}

Invoke-Step "Compile NFI refactor files" {
    Invoke-FreqtradePython @(
        "-m", "py_compile",
        "/work/strategies/NFIRefactorStrategy.py",
        "/work/strategies/nfi_refactor/position/adjustment.py",
        "/work/strategies/nfi_refactor/position/adjustment_context.py",
        "/work/strategies/nfi_refactor/position/adjustment_execution.py",
        "/work/strategies/nfi_refactor/position/adjustment_grind_route.py",
        "/work/strategies/nfi_refactor/position/adjustment_grind_selectors.py",
        "/work/strategies/nfi_refactor/position/adjustment_grind_tags.py",
        "/work/strategies/nfi_refactor/position/adjustment_rebuy_route.py",
        "/work/strategies/nfi_refactor/position/adjustment_rebuy_selectors.py",
        "/work/strategies/nfi_refactor/position/adjustment_rebuy_tags.py"
    )
}

Invoke-Step "Sync strategy to ft_userdata" {
    powershell -ExecutionPolicy Bypass -File `
        (Join-Path $repoRoot "scripts\sync_strategy_to_ft_userdata.ps1") `
        -TargetStrategyDir $targetStrategyDir
}

Invoke-Step "Smoke backtest $SmokeTimerange" {
    $smokeOutput = Invoke-Backtest -Timerange $SmokeTimerange
    $smokeText = $smokeOutput -join [Environment]::NewLine
    Write-Output $smokeOutput

    if ($smokeText -notmatch "No trades made") {
        throw "Smoke backtest changed: expected no trades for $SmokeTimerange."
    }
}

if ($RunHalfyear) {
    Invoke-Step "Halfyear no-cache parity backtest $HalfyearTimerange" {
        $halfyearOutput = Invoke-Backtest -Timerange $HalfyearTimerange -NoCache
        $halfyearText = $halfyearOutput -join [Environment]::NewLine
        Write-Output $halfyearOutput

        if ($halfyearText -notmatch "TOTAL\s+.*\s61\s+") {
            throw "Halfyear parity changed: expected 61 trades."
        }
        if ($halfyearText -notmatch "1757\.800") {
            throw "Halfyear parity changed: expected +1757.800 USDT profit."
        }
        if ($halfyearText -notmatch "580\.9") {
            throw "Halfyear parity changed: expected +580.90% return."
        }
        if ($halfyearText -notmatch "100") {
            throw "Halfyear parity changed: expected 100% win rate marker."
        }
    }
}

Write-Host ""
Write-Host "Regression checks completed."
