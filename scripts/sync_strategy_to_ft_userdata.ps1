param(
    [string]$TargetStrategyDir = "D:\test\ft_userdata\user_data\strategies"
)

$ErrorActionPreference = "Stop"

$repoRoot = Split-Path -Parent $PSScriptRoot
$sourceNfiRefactorStrategy = Join-Path $repoRoot "strategies\NFIRefactorStrategy.py"
$sourceNfiAlphaHybridStrategy = Join-Path $repoRoot "strategies\NFIAlphaHybridStrategy.py"
$sourceNfiRefactorModules = Join-Path $repoRoot "strategies\nfi_refactor"
$targetNfiRefactorModules = Join-Path $TargetStrategyDir "nfi_refactor"
$obsoleteAlphaStrategy = Join-Path $TargetStrategyDir "AlphaRegimeStrategy.py"
$obsoleteAlphaModules = Join-Path $TargetStrategyDir "alpha_modules"

New-Item -ItemType Directory -Force -Path $TargetStrategyDir | Out-Null
if (Test-Path -LiteralPath $sourceNfiRefactorStrategy -PathType Leaf) {
    Copy-Item -LiteralPath $sourceNfiRefactorStrategy -Destination (Join-Path $TargetStrategyDir "NFIRefactorStrategy.py") -Force
}
if (Test-Path -LiteralPath $sourceNfiAlphaHybridStrategy -PathType Leaf) {
    Copy-Item -LiteralPath $sourceNfiAlphaHybridStrategy -Destination (Join-Path $TargetStrategyDir "NFIAlphaHybridStrategy.py") -Force
}

if (Test-Path -LiteralPath $obsoleteAlphaStrategy -PathType Leaf) {
    Remove-Item -LiteralPath $obsoleteAlphaStrategy -Force
}
if (Test-Path -LiteralPath $obsoleteAlphaModules) {
    Remove-Item -LiteralPath $obsoleteAlphaModules -Recurse -Force
}

if (Test-Path -LiteralPath $sourceNfiRefactorModules) {
    if (Test-Path -LiteralPath $targetNfiRefactorModules) {
        Remove-Item -LiteralPath $targetNfiRefactorModules -Recurse -Force
    }
    Copy-Item -LiteralPath $sourceNfiRefactorModules -Destination $targetNfiRefactorModules -Recurse -Force
}

Write-Host "Strategy synced to $TargetStrategyDir"
