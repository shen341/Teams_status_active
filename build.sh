#!/usr/bin/env bash
# Build 绿灯侠 (Green Light Hero) for macOS
# Run on a Mac: ./build.sh
# Output: dist/TeamsKeepAlive (single executable, no .app)

set -e
cd "$(dirname "$0")"

echo "========================================"
echo " TeamsKeepAlive - Build for macOS"
echo "========================================"
echo ""

echo "[1/3] Installing build dependencies..."
pip install -r requirements.txt -r requirements-build.txt
echo ""

echo "[2/3] Building executable..."
python3 -m PyInstaller --clean --noconfirm TeamsKeepAlive.mac.spec
echo ""

echo "[3/3] Done."
echo ""
echo "Output: dist/TeamsKeepAlive"
echo "Run with: ./dist/TeamsKeepAlive"
echo "Share this file with macOS users (no Python required)."
