# TeamsKeepAlive - Build .exe (PowerShell)
# Run: .\build.ps1
# If execution policy blocks: Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
# Messages in English to avoid encoding issues in any locale.

$ErrorActionPreference = "Stop"
Set-Location $PSScriptRoot

Write-Host "========================================"
Write-Host " TeamsKeepAlive - Build .exe"
Write-Host "========================================"
Write-Host ""

Write-Host "[1/3] Installing build dependencies..."
pip install -r requirements.txt -r requirements-build.txt
if ($LASTEXITCODE -ne 0) {
    Write-Host "ERROR: pip install failed. Check Python installation." -ForegroundColor Red
    exit 1
}
Write-Host ""

Write-Host "[2/3] Building .exe..."
python -m PyInstaller --clean --noconfirm TeamsKeepAlive.spec
if ($LASTEXITCODE -ne 0) {
    Write-Host "ERROR: PyInstaller build failed." -ForegroundColor Red
    exit 1
}
Write-Host ""

Write-Host "[3/3] Done." -ForegroundColor Green
Write-Host ""
Write-Host "Output: dist\TeamsKeepAlive.exe"
Write-Host "Share only this file with end users (no Python required)."
