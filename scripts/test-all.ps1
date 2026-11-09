# Awesome Plugins DSH Harness Verification Script

$RepoRoot = Split-Path $PSScriptRoot -Parent
$BridgeScript = Join-Path $RepoRoot "plugins\cli-bridge\bridge.py"

Write-Host "==========================================================" -ForegroundColor Cyan
Write-Host "  Testing Awesome Plugins for DeepSeek Harness" -ForegroundColor Cyan
Write-Host "==========================================================" -ForegroundColor Cyan

# 1. Test CLI Bridge status
Write-Host "`n[1] Testing CLI Bridge Available Engines..." -ForegroundColor Yellow
py $BridgeScript status

# 2. Test Subscription Gateway
Write-Host "`n[2] Testing Subscription Bridge Models Endpoint (Port 5288)..." -ForegroundColor Yellow
try {
    $resp = Invoke-RestMethod -Uri "http://127.0.0.1:5288/v1/models" -TimeoutSec 3
    Write-Host "Gateway is LIVE! Available Models:" -ForegroundColor Green
    $resp.data | ForEach-Object { Write-Host "  - $($_.id) ($($_.owned_by))" -ForegroundColor Gray }
} catch {
    Write-Host "Gateway not running on 5288. You can start it using:" -ForegroundColor Yellow
    Write-Host "  pwsh .\plugins\subscription-bridge\start-gateway.ps1" -ForegroundColor Yellow
}
