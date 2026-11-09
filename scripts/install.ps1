# Awesome Plugins DSH Harness Installer
# Installs plugins and skills into DeepSeek Harness (~/.dsh)

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
New-Item -ItemType Directory -Path (Join-Path $PluginsTarget "subscription-bridge") -Force | Out-Null
New-Item -ItemType Directory -Path (Join-Path $PluginsTarget "cli-bridge") -Force | Out-Null
New-Item -ItemType Directory -Path (Join-Path $SkillsTarget "subscription-bridge") -Force | Out-Null
New-Item -ItemType Directory -Path (Join-Path $SkillsTarget "cli-bridge") -Force | Out-Null

# 2. Copy Plugin Files
Write-Host "[1/3] Copying plugins to $PluginsTarget..." -ForegroundColor Green
Copy-Item (Join-Path $RepoRoot "plugins\subscription-bridge\*") (Join-Path $PluginsTarget "subscription-bridge\") -Recurse -Force
Copy-Item (Join-Path $RepoRoot "plugins\cli-bridge\*") (Join-Path $PluginsTarget "cli-bridge\") -Recurse -Force

# 3. Copy Skill Files
Write-Host "[2/3] Registering skills in $SkillsTarget..." -ForegroundColor Green
Copy-Item (Join-Path $RepoRoot "skills\subscription-bridge\SKILL.md") (Join-Path $SkillsTarget "subscription-bridge\SKILL.md") -Force
Copy-Item (Join-Path $RepoRoot "skills\cli-bridge\SKILL.md") (Join-Path $SkillsTarget "cli-bridge\SKILL.md") -Force

# Also mirror to unified ~/.agents/skills
$AgentsSkills = Join-Path $env:USERPROFILE ".agents\skills\cli-bridge"
New-Item -ItemType Directory -Path $AgentsSkills -Force | Out-Null
Copy-Item (Join-Path $RepoRoot "skills\cli-bridge\SKILL.md") (Join-Path $AgentsSkills "SKILL.md") -Force

Write-Host "[3/3] Installation complete!" -ForegroundColor Green
Write-Host "To test the installation, run:" -ForegroundColor Yellow
Write-Host "  pwsh .\scripts\test-all.ps1" -ForegroundColor Yellow
