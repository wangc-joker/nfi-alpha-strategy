param(
    [string]$TargetStrategyDir = "D:\test\ft_userdata\user_data\strategies",
    [string]$UpstreamNfiFile = "D:\test\NostalgiaForInfinity\NostalgiaForInfinityX7.py"
)

$ErrorActionPreference = "Stop"

$repoRoot = Split-Path -Parent $PSScriptRoot
$wrapperStrategy = Join-Path $repoRoot "strategies\NFIRiskDurationStrategy.py"

if (-not (Test-Path -LiteralPath $UpstreamNfiFile -PathType Leaf)) {
    throw "Upstream NFI file not found: $UpstreamNfiFile"
}

if (-not (Test-Path -LiteralPath $wrapperStrategy -PathType Leaf)) {
    throw "Wrapper strategy file not found: $wrapperStrategy"
}

New-Item -ItemType Directory -Force -Path $TargetStrategyDir | Out-Null

Copy-Item -LiteralPath $UpstreamNfiFile -Destination (Join-Path $TargetStrategyDir "NostalgiaForInfinityX7.py") -Force
Copy-Item -LiteralPath $wrapperStrategy -Destination (Join-Path $TargetStrategyDir "NFIRiskDurationStrategy.py") -Force

Write-Host "RecoveryCutGentle wrapper synced to $TargetStrategyDir"
Write-Host "Copied: NostalgiaForInfinityX7.py"
Write-Host "Copied: NFIRiskDurationStrategy.py"
