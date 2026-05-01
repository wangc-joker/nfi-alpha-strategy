param(
    [string]$TargetStrategyDir = "D:\test\ft_userdata\user_data\strategies"
)

$ErrorActionPreference = "Stop"

$repoRoot = Split-Path -Parent $PSScriptRoot
$sourceStrategy = Join-Path $repoRoot "strategies\AlphaRegimeStrategy.py"
$sourceNfiRefactorStrategy = Join-Path $repoRoot "strategies\NFIRefactorStrategy.py"
$sourceNfiRiskDurationStrategy = Join-Path $repoRoot "strategies\NFIRiskDurationStrategy.py"
$sourceModules = Join-Path $repoRoot "strategies\alpha_modules"
$sourceNfiRefactorModules = Join-Path $repoRoot "strategies\nfi_refactor"
$targetModules = Join-Path $TargetStrategyDir "alpha_modules"
$targetNfiRefactorModules = Join-Path $TargetStrategyDir "nfi_refactor"

if (-not (Test-Path -LiteralPath $sourceStrategy -PathType Leaf)) {
    throw "Strategy file not found: $sourceStrategy"
}

New-Item -ItemType Directory -Force -Path $TargetStrategyDir | Out-Null
Copy-Item -LiteralPath $sourceStrategy -Destination (Join-Path $TargetStrategyDir "AlphaRegimeStrategy.py") -Force
if (Test-Path -LiteralPath $sourceNfiRefactorStrategy -PathType Leaf) {
    Copy-Item -LiteralPath $sourceNfiRefactorStrategy -Destination (Join-Path $TargetStrategyDir "NFIRefactorStrategy.py") -Force
}
if (Test-Path -LiteralPath $sourceNfiRiskDurationStrategy -PathType Leaf) {
    Copy-Item -LiteralPath $sourceNfiRiskDurationStrategy -Destination (Join-Path $TargetStrategyDir "NFIRiskDurationStrategy.py") -Force
}

if (Test-Path -LiteralPath $targetModules) {
    Remove-Item -LiteralPath $targetModules -Recurse -Force
}
Copy-Item -LiteralPath $sourceModules -Destination $targetModules -Recurse -Force

if (Test-Path -LiteralPath $sourceNfiRefactorModules) {
    if (Test-Path -LiteralPath $targetNfiRefactorModules) {
        Remove-Item -LiteralPath $targetNfiRefactorModules -Recurse -Force
    }
    Copy-Item -LiteralPath $sourceNfiRefactorModules -Destination $targetNfiRefactorModules -Recurse -Force
}

Write-Host "Strategy synced to $TargetStrategyDir"
