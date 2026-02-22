# -*- mode: python ; coding: utf-8 -*-
# PyInstaller spec for macOS (single executable)
# Build on a Mac: pyinstaller --clean --noconfirm TeamsKeepAlive.mac.spec
# Output: dist/TeamsKeepAlive (no extension)

block_cipher = None

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[
        'pynput',
        'pynput.mouse',
        'pynput.mouse._darwin',
        'pynput._util',
        'pynput._util.darwin',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='TeamsKeepAlive',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
)
