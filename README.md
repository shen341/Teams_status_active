# Teams Keep-Alive

A small Windows tool that prevents Microsoft Teams from switching to **Away** (or "Be right back") after about 5 minutes of inactivity. It uses **OS-level mouse movement** so the system—and Teams—thinks you are still active.

**Languages:** [English](README.md) · [日本語](README.ja.md) · [中文](README.zh-CN.md) · [한국어](README.ko.md)

---

## How it works (principle)

- **Why Teams goes Away:** Teams uses Windows’ **system idle detection** (e.g. `GetLastInputInfo`) to decide if you are active. After roughly 5 minutes with no mouse or keyboard input, it marks you as Away.
- **What this tool does:** It **moves the mouse by 1 pixel** (then back) at a fixed interval (default **every 4 minutes**). That counts as real user input, so Windows updates “last input time” and Teams keeps showing you as **Available**.
- **No Teams hacking:** It does not inject into or modify the Teams process. It only simulates normal OS input, like moving the mouse slightly.

---

## Security

- **Local only:** No network access, no telemetry, no phone-home. Everything runs on your PC.
- **No keylogging or screenshots:** The program only moves the mouse by 1 pixel at a time. It does not read keystrokes, clipboard, or screen.
- **Open source:** You can read [main.py](main.py) and the build scripts. For maximum trust, you can build the .exe yourself from source (see “Build from source” below).

---

## How to use

### Option 1: Run the .exe (no Python needed) — recommended for most users

1. Get **TeamsKeepAlive.exe** (from [Releases](https://github.com/YOUR_USERNAME/SNS_status_active/releases) or from someone who built it).
2. Put it in any folder. Double-click to run.
3. A console window opens. Every **4 minutes** you’ll see a line like: `キープアライブ送信（マウス 1px 移動）` (or similar).
4. To stop: press **Ctrl+C** in that window or close the window.

No installation or Python required. Works on company PCs as long as running .exe files is allowed.

### Option 2: Run the Python script (if you have Python)

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run:
   ```bash
   python main.py
   ```
3. Stop with **Ctrl+C**.

### Option 3: Build the .exe from source (for distributors or if you want to verify the binary)

You need **Python 3.7+** on your machine.

**Quick build (Windows):**

- Double-click **build.bat**, or in PowerShell run:
  ```powershell
  .\build.ps1
  ```
- If PowerShell blocks the script, run once:  
  `Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned`

**Manual build:**

```batch
pip install -r requirements.txt -r requirements-build.txt
python -m PyInstaller --clean --noconfirm TeamsKeepAlive.spec
```

The built .exe is in **`dist\TeamsKeepAlive.exe`**. You can share only this file with others.

---

## Change the interval

Edit **main.py**, line with `INTERVAL_SEC`:

```python
INTERVAL_SEC = 4 * 60   # 4 minutes. Examples: 2*60 = 2 min, 5*60 = 5 min
```

Then run the script again, or rebuild the .exe with the steps above.

---

## Example output

```
[2025-02-22 10:00:00] Teams キープアライブを開始しました（Ctrl+C で停止）
[2025-02-22 10:00:00] 間隔: 240 秒 (4 分)
[2025-02-22 10:00:00] キープアライブ送信（マウス 1px 移動）
[2025-02-22 10:04:00] キープアライブ送信（マウス 1px 移動）
...
^C
[2025-02-22 10:05:30] 終了しました。
```

---

## Notes

- Use in line with your organization’s IT and usage policies.
- Other apps (Slack, Zoom, etc.) that use system idle may also stay “active” while this runs.

---

## Project files

| File | Description |
|------|-------------|
| `main.py` | Main script (single file to run) |
| `requirements.txt` | Runtime dependency (pynput) |
| `requirements-build.txt` | Build dependency (PyInstaller) |
| `TeamsKeepAlive.spec` | PyInstaller spec for single .exe |
| `build.bat` | Build .exe (batch) |
| `build.ps1` | Build .exe (PowerShell) |

Distribute only **`dist\TeamsKeepAlive.exe`** to end users if you build it yourself.

> **Note for repo owners:** Replace `YOUR_USERNAME` in the Releases link with your GitHub username (or your org name) so the link points to your repository’s Releases page.
