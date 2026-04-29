param(
    [string]$FtUserDataRoot = "D:\test\ft_userdata",
    [string]$SmokeTimerange = "20260401-20260403",
    [string]$HalfyearTimerange = "20251016-20260415",
    [switch]$RunHalfyear,
    [switch]$SkipExchangePreflight
)

$ErrorActionPreference = "Stop"

$repoRoot = Split-Path -Parent $PSScriptRoot
$composeFile = Join-Path $FtUserDataRoot "docker-compose.yml"
$targetStrategyDir = Join-Path $FtUserDataRoot "user_data\strategies"
$configName = "config.backtest.dynamic.top40.302u.max2.halfyear.balanced.json"
$expectedHalfyearTrades = 61
$expectedHalfyearProfit = "1757.800"
$expectedHalfyearReturn = "580.9"
$expectedHalfyearWinrate = "100"

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

function Format-CommandFailure {
    param(
        [string]$Message,
        [object[]]$Output,
        [int]$TailLines = 80
    )

    $tail = $Output | Select-Object -Last $TailLines
    return ($Message + [Environment]::NewLine + ($tail -join [Environment]::NewLine))
}

function Invoke-FreqtradePython {
    param([string[]]$Args)

    $previousErrorActionPreference = $ErrorActionPreference
    $ErrorActionPreference = "Continue"
    try {
        $output = docker compose -f $composeFile run --rm --entrypoint python `
            -v "${repoRoot}:/work" `
            freqtrade @Args 2>&1
    }
    finally {
        $ErrorActionPreference = $previousErrorActionPreference
    }

    $exitCode = $LASTEXITCODE
    $output = $output | ForEach-Object { $_.ToString() }
    Write-Output $output
    if ($exitCode -ne 0) {
        throw (Format-CommandFailure "Freqtrade python command failed with exit code $exitCode." $output)
    }
}

function Invoke-DockerPythonInline {
    param([string]$Code)

    $encodedCode = [Convert]::ToBase64String([System.Text.Encoding]::UTF8.GetBytes($Code))
    $runnerCode = "import base64; exec(base64.b64decode('$encodedCode').decode('utf-8'))"

    $previousErrorActionPreference = $ErrorActionPreference
    $ErrorActionPreference = "Continue"
    try {
        $output = docker compose -f $composeFile run --rm --entrypoint python freqtrade -c $runnerCode 2>&1
    }
    finally {
        $ErrorActionPreference = $previousErrorActionPreference
    }

    $exitCode = $LASTEXITCODE
    $output = $output | ForEach-Object { $_.ToString() }
    Write-Output $output
    if ($exitCode -ne 0) {
        throw (Format-CommandFailure "Docker python inline command failed with exit code $exitCode." $output)
    }
}

function Test-BinanceExchangeInfo {
    $code = @'
import urllib.request

endpoints = [
    "https://api.binance.com/api/v3/exchangeInfo",
    "https://dapi.binance.com/dapi/v1/exchangeInfo",
]

for url in endpoints:
    try:
        with urllib.request.urlopen(url, timeout=15) as response:
            status = response.status
            if status != 200:
                raise RuntimeError(f"HTTP {status}")
            first_bytes = response.read(128)
            if not first_bytes:
                raise RuntimeError("empty response")
            print(f"OK {url} status={status}")
    except Exception as exc:
        raise SystemExit(f"FAILED {url}: {exc.__class__.__name__}: {exc}")
'@

    try {
        Invoke-DockerPythonInline $code
    }
    catch {
        throw ("Binance exchange preflight failed. Freqtrade backtests need Binance exchangeInfo before local historical data can run." + [Environment]::NewLine + $_.Exception.Message)
    }
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

    $previousErrorActionPreference = $ErrorActionPreference
    $ErrorActionPreference = "Continue"
    try {
        $output = docker compose -f $composeFile run --rm freqtrade @args 2>&1
    }
    finally {
        $ErrorActionPreference = $previousErrorActionPreference
    }

    $exitCode = $LASTEXITCODE
    $output = $output | ForEach-Object { $_.ToString() }
    Write-Output $output
    if ($exitCode -ne 0) {
        throw (Format-CommandFailure "Freqtrade backtest command failed with exit code $exitCode." $output)
    }
}

function Assert-HalfyearParity {
    param([string]$BacktestText)

    $totalLine = ($BacktestText -split "`r?`n" | Where-Object {
        $_ -match "\bTOTAL\b" -and $_ -match [regex]::Escape($expectedHalfyearProfit)
    } | Select-Object -First 1)

    if (-not $totalLine) {
        throw "Halfyear parity changed: TOTAL line not found."
    }
    if ($totalLine -notmatch "\bTOTAL\b.*\b$expectedHalfyearTrades\b") {
        throw "Halfyear parity changed: expected $expectedHalfyearTrades trades. TOTAL line: $totalLine"
    }
    if ($totalLine -notmatch [regex]::Escape($expectedHalfyearProfit)) {
        throw "Halfyear parity changed: expected +$expectedHalfyearProfit USDT profit. TOTAL line: $totalLine"
    }
    if ($totalLine -notmatch [regex]::Escape($expectedHalfyearReturn)) {
        throw "Halfyear parity changed: expected +$expectedHalfyearReturn% return. TOTAL line: $totalLine"
    }
    if ($totalLine -notmatch "\b$expectedHalfyearWinrate\b") {
        throw "Halfyear parity changed: expected $expectedHalfyearWinrate% win rate. TOTAL line: $totalLine"
    }
}

Write-Host "NFI refactor regression baseline:"
Write-Host "  Smoke timerange: $SmokeTimerange -> expected no trades"
if ($RunHalfyear) {
    Write-Host "  Halfyear timerange: $HalfyearTimerange"
    Write-Host "  Expected: $expectedHalfyearTrades trades / +$expectedHalfyearProfit USDT / +$expectedHalfyearReturn% / $expectedHalfyearWinrate% winrate"
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
    $previousErrorActionPreference = $ErrorActionPreference
    $ErrorActionPreference = "Continue"
    try {
        $output = powershell -ExecutionPolicy Bypass -File `
            (Join-Path $repoRoot "scripts\sync_strategy_to_ft_userdata.ps1") `
            -TargetStrategyDir $targetStrategyDir 2>&1
    }
    finally {
        $ErrorActionPreference = $previousErrorActionPreference
    }

    $exitCode = $LASTEXITCODE
    $output = $output | ForEach-Object { $_.ToString() }
    Write-Output $output
    if ($exitCode -ne 0) {
        throw (Format-CommandFailure "Strategy sync failed with exit code $exitCode." $output)
    }
}

if (-not $SkipExchangePreflight) {
    Invoke-Step "Binance exchange preflight" {
        Test-BinanceExchangeInfo
    }
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

        Assert-HalfyearParity -BacktestText $halfyearText
    }
}

Write-Host ""
Write-Host "Regression checks completed."
