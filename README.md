# Teams Keep-Alive

A small Windows tool that prevents Microsoft Teams from switching to **Away** (or "Be right back") after about 5 minutes of inactivity. It uses **OS-level mouse movement** so the system—and Teams—thinks you are still active.

**Languages:** [English](README.md) · [日本語](README.ja.md) · [中文](README.zh-CN.md) · [한국어](README.ko.md)

---

## Quick start (recommended)

**A pre-built .exe is included in this repository.** No Python or build step required.

1. **Clone or download** this repository.
2. Open the `dist` folder and run **TeamsKeepAlive.exe** (double-click or from a terminal).
3. A console window opens. Every **4 minutes** you’ll see: `Keep-alive sent (mouse 1px move)`.
4. To stop: press **Ctrl+C** or close the window.

That’s it. Works on company PCs as long as running .exe files is allowed.

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

## Other ways to run

### Get the .exe from Releases

If the maintainer publishes [Releases](https://github.com/YOUR_USERNAME/SNS_status_active/releases), you can download **TeamsKeepAlive.exe** from there and run it without cloning the full repo.

### Run the Python script (if you have Python)

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run:
   ```bash
   python main.py
   ```
3. Stop with **Ctrl+C**.

### Build the .exe from source (for distributors or to verify the binary)

You need **Python 3.7+** on your machine.

**Quick build (Windows):** Double-click **build.bat**, or in PowerShell run `.\build.ps1`.  
If PowerShell blocks the script, run once: `Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned`

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
[2025-02-22 10:00:00] Teams Keep-Alive started (Ctrl+C to stop)
[2025-02-22 10:00:00] Interval: 240 sec (4 min)
[2025-02-22 10:00:00] Keep-alive sent (mouse 1px move)
[2025-02-22 10:04:00] Keep-alive sent (mouse 1px move)
...
^C
[2025-02-22 10:05:30] Stopped.
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
| `dist\TeamsKeepAlive.exe` | Pre-built executable (ready to run) |
| `requirements.txt` | Runtime dependency (pynput) |
| `requirements-build.txt` | Build dependency (PyInstaller) |
| `TeamsKeepAlive.spec` | PyInstaller spec for single .exe |
| `build.bat` | Build .exe (batch) |
| `build.ps1` | Build .exe (PowerShell) |

---

## License

This project is licensed under the **MIT License**. See [LICENSE](LICENSE) for the full text.

> **Note for repo owners:** Replace `YOUR_USERNAME` in the Releases link with your GitHub username (or your org name) so the link points to your repository’s Releases page.
