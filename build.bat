@echo off
setlocal
cd /d "%~dp0"

echo ========================================
echo  TeamsKeepAlive - Build .exe
echo ========================================
echo.

REM Install build dependencies
echo [1/3] Installing build dependencies...
pip install -r requirements.txt -r requirements-build.txt
if errorlevel 1 (
    echo ERROR: pip install failed. Check Python installation.
    exit /b 1
)
echo.

REM Build .exe (use python -m so PyInstaller works when Scripts is not in PATH)
echo [2/3] Building .exe...
python -m PyInstaller --clean --noconfirm TeamsKeepAlive.spec
if errorlevel 1 (
    echo ERROR: PyInstaller build failed.
    exit /b 1
)
echo.

echo [3/3] Done.
echo.
echo Output: dist\TeamsKeepAlive.exe
echo Share only this file with end users (no Python required).
echo.
pause
