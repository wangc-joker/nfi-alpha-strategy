param(
    [string]$MainCoinsPath = "",
    [string]$OutputDir = "",
    [int]$TargetCount = 30,
    [int]$RequestDelaySeconds = 2
)

$ErrorActionPreference = "Stop"
[Console]::OutputEncoding = [System.Text.UTF8Encoding]::new()

$repoRoot = Split-Path -Parent $PSScriptRoot
if ([string]::IsNullOrWhiteSpace($MainCoinsPath)) {
    $MainCoinsPath = Join-Path $repoRoot "configs\main_coins.nfi_top_coins.json"
}
if ([string]::IsNullOrWhiteSpace($OutputDir)) {
    $OutputDir = Join-Path $repoRoot "generated"
}

$pairsPath = Join-Path $OutputDir "pairs.alpha.dynamic.top30.json"
$reportPath = Join-Path $OutputDir "pairs.alpha.dynamic.top30.report.json"
$quoteAsset = "USDT"
$script:lastRequestAt = $null

function Get-Json {
    param([string]$Uri)

    if ($null -ne $script:lastRequestAt) {
        $elapsedSeconds = ((Get-Date) - $script:lastRequestAt).TotalSeconds
        $remainingSeconds = $RequestDelaySeconds - $elapsedSeconds
        if ($remainingSeconds -gt 0) {
            Start-Sleep -Seconds ([int][math]::Ceiling($remainingSeconds))
        }
    }

    try {
        return Invoke-RestMethod -Uri $Uri -Method Get -TimeoutSec 60
    }
    finally {
        $script:lastRequestAt = Get-Date
    }
}

function Get-PerpetualUsdtSymbolMapBySymbol {
    param([object]$ExchangeInfo)

    $map = @{}
    foreach ($symbolInfo in @($ExchangeInfo.symbols)) {
        if ($symbolInfo.quoteAsset -ne "USDT") { continue }
        if ($symbolInfo.status -ne "TRADING") { continue }
        if ($symbolInfo.contractType -ne "PERPETUAL") { continue }
        if ([string]::IsNullOrWhiteSpace($symbolInfo.baseAsset)) { continue }
        if ([string]::IsNullOrWhiteSpace($symbolInfo.symbol)) { continue }

        $symbol = ([string]$symbolInfo.symbol).ToUpperInvariant()
        $map[$symbol] = $symbolInfo
    }

    return $map
}

if (-not (Test-Path -LiteralPath $MainCoinsPath -PathType Leaf)) {
    throw "Main coin file not found: $MainCoinsPath"
}

New-Item -ItemType Directory -Force -Path $OutputDir | Out-Null

$mainCoinJson = Get-Content -Raw -LiteralPath $MainCoinsPath | ConvertFrom-Json
$mainCoins = foreach ($coin in @($mainCoinJson)) {
    ([string]$coin).ToUpperInvariant()
}
$mainCoinSet = @{}
foreach ($coin in $mainCoins) {
    $mainCoinSet[$coin] = $true
}

$exchangeInfo = Get-Json "https://fapi.binance.com/fapi/v1/exchangeInfo"
$tickersResponse = Get-Json "https://fapi.binance.com/fapi/v1/ticker/24hr"
$tickers = @($tickersResponse | ForEach-Object { $_ })
$symbolMap = Get-PerpetualUsdtSymbolMapBySymbol -ExchangeInfo $exchangeInfo

$candidateList = New-Object System.Collections.Generic.List[object]
$seenBaseAssets = @{}
foreach ($ticker in @($tickers)) {
    $symbol = ([string]$ticker.symbol).ToUpperInvariant()
    if (-not $symbolMap.ContainsKey($symbol)) { continue }

    $meta = $symbolMap[$symbol]
    $baseAsset = ([string]$meta.baseAsset).ToUpperInvariant()
    if (-not $mainCoinSet.ContainsKey($baseAsset)) { continue }
    if ($seenBaseAssets.ContainsKey($baseAsset)) { continue }

    $seenBaseAssets[$baseAsset] = $true
    $candidateList.Add([pscustomobject]@{
        symbol = $meta.symbol
        baseAsset = $meta.baseAsset
        pair = ("{0}/{1}:{1}" -f $meta.baseAsset, $quoteAsset)
        currentQuoteVolume24h = [double]$ticker.quoteVolume
        currentVolume24h = [double]$ticker.volume
        weightedAvgPrice24h = [double]$ticker.weightedAvgPrice
        count24h = [int64]$ticker.count
        lastPrice = [double]$ticker.lastPrice
        priceChangePercent24h = [double]$ticker.priceChangePercent
    })
}

$rankedCandidates = @($candidateList | Sort-Object currentQuoteVolume24h -Descending)
$selected = @($rankedCandidates | Select-Object -First $TargetCount)
$missingFromExchange = @($mainCoins | Where-Object { -not $seenBaseAssets.ContainsKey($_) })

if ($selected.Count -eq 0) {
    throw "No Binance Futures symbols could be selected from the main coin pool."
}

[System.IO.File]::WriteAllText(
    $pairsPath,
    (@($selected.pair) | ConvertTo-Json -Depth 4),
    [System.Text.UTF8Encoding]::new($false)
)

$report = [pscustomobject]@{
    generated_at = (Get-Date).ToString("yyyy-MM-dd HH:mm:ss zzz")
    source = "Binance Futures 24h ticker quoteVolume"
    main_coins_path = $MainCoinsPath
    target_count = $TargetCount
    main_coin_count = $mainCoins.Count
    eligible_candidate_count = $rankedCandidates.Count
    selected_count = $selected.Count
    request_delay_seconds = $RequestDelaySeconds
    missing_from_binance_futures = @($missingFromExchange)
    pairs = @($selected)
}

[System.IO.File]::WriteAllText(
    $reportPath,
    ($report | ConvertTo-Json -Depth 16),
    [System.Text.UTF8Encoding]::new($false)
)

Write-Host ""
Write-Host "Alpha dynamic Top30 pairlist updated." -ForegroundColor Green
Write-Host ("Pairs  : {0}" -f $pairsPath)
Write-Host ("Report : {0}" -f $reportPath)
Write-Host ("Main coins          : {0}" -f $mainCoins.Count)
Write-Host ("Eligible candidates : {0}" -f $rankedCandidates.Count)
Write-Host ("Selected count      : {0}" -f $selected.Count)
Write-Host ""
Write-Host "Selected pairs:" -ForegroundColor Cyan
@($selected.pair) | ForEach-Object { Write-Host $_ }
