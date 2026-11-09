# Awesome Plugins DSH Harness Installer
# Installs all plugins and skills into DeepSeek Harness (~/.dsh) and ~/.agents

$ErrorActionPreference = "Stop"

$DshRoot = Join-Path $env:USERPROFILE ".dsh"
$PluginsTarget = Join-Path $DshRoot "plugins"
$SkillsTarget = Join-Path $DshRoot "skills"
$RepoRoot = Split-Path $PSScriptRoot -Parent

Write-Host "==========================================================" -ForegroundColor Cyan
Write-Host "  Awesome Plugins for DeepSeek Harness (DSH) Installer" -ForegroundColor Cyan
Write-Host "  Author: Dr. Eng. Hossam Zein" -ForegroundColor Cyan
Write-Host "==========================================================" -ForegroundColor Cyan

# 1. Ensure target directories
$pluginList = @("subscription-bridge", "cli-bridge", "delegation-bridge")
foreach ($p in $pluginList) {
    New-Item -ItemType Directory -Path (Join-Path $PluginsTarget $p) -Force | Out-Null
    New-Item -ItemType Directory -Path (Join-Path $SkillsTarget $p) -Force | Out-Null
}

# 2. Copy Plugin Files
Write-Host "[1/3] Copying plugins to $PluginsTarget..." -ForegroundColor Green
foreach ($p in $pluginList) {
    Copy-Item (Join-Path $RepoRoot "plugins\$p\*") (Join-Path $PluginsTarget "$p\") -Recurse -Force
}

# 3. Copy Skill Files
Write-Host "[2/3] Registering skills in $SkillsTarget..." -ForegroundColor Green
foreach ($p in $pluginList) {
    Copy-Item (Join-Path $RepoRoot "skills\$p\SKILL.md") (Join-Path $SkillsTarget "$p\SKILL.md") -Force
    
    # Also mirror to unified ~/.agents/skills
    $AgentsSkills = Join-Path $env:USERPROFILE ".agents\skills\$p"
    New-Item -ItemType Directory -Path $AgentsSkills -Force | Out-Null
    Copy-Item (Join-Path $RepoRoot "skills\$p\SKILL.md") (Join-Path $AgentsSkills "SKILL.md") -Force
}

Write-Host "[3/3] Installation complete!" -ForegroundColor Green
Write-Host "To test the installation, run:" -ForegroundColor Yellow
Write-Host "  pwsh .\scripts\test-all.ps1" -ForegroundColor Yellow
