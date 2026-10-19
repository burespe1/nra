# Builds the test repository with the history v2.0.0 -> v2.1.0 -> v2.2.0 (draft branch)
# from the existing files in ..\model and ..\reports, and pushes it to GitHub.
# Run in this folder:  powershell -ExecutionPolicy Bypass -File .\init-repo.ps1
param([string]$Remote = "https://github.com/burespe1/nra.git")
$ErrorActionPreference = "Stop"
$src = Resolve-Path "..\model"
$rep = Resolve-Path "..\reports"

$py = $null
foreach ($c in "python", "py", "python3") { if (Get-Command $c -ErrorAction SilentlyContinue) { $py = $c; break } }
if (-not $py) { Write-Warning "Python not found - export/ will be missing. Install Python 3 and run: python tools\export.py" }

git init -b main
git lfs install
git config core.hooksPath tools/hooks
New-Item -ItemType Directory -Force model, docs | Out-Null

function Snapshot($file, $msg, $tag) {
  Copy-Item (Join-Path $src $file) model\NRA.qea -Force
  Set-ItemProperty model\NRA.qea -Name IsReadOnly -Value $false
  if ($py) { & $py tools\export.py model\NRA.qea export }
  git add -A
  git commit -m $msg
  if ($tag) { git tag -a $tag -m $msg }
}

Snapshot "NRA_20250704-clean.qea" "NRA v2.0.0 - baseline 2025-07-04" "v2.0.0"

Copy-Item (Join-Path $src "NRA_2.1.0_Changelog.docx") docs\ -Force
Copy-Item (Join-Path $rep "National Access Point Reference Architecture - 2.1.0.docx") "docs\NRA-2.1.0.docx" -Force
Snapshot "NRA_20261020_UPDATE.qea" "NRA v2.1.0 - Organisational View (WG 4.6.3), consistency and documentation fixes" "v2.1.0"

git switch -c release/2.2.0
Copy-Item (Join-Path $src "NRA_2.2.0_Changelog.docx") docs\ -Force
Snapshot "NRA_20261020_02_UPDATE.qea" "NRA v2.2.0 draft - resolve unresolved requirements" $null
git switch main

git remote add origin $Remote
git push -u origin main --tags
git push -u origin release/2.2.0
Write-Host "`nDone. Open a pull request release/2.2.0 -> main on GitHub to see the change report."
