# 绿灯侠 · Green Light Hero

**Keep your status green.** A small Windows tool that stops Microsoft Teams from flipping to **Away** after ~5 minutes of inactivity—so you can step away without the “Be right back” guilt.

For the young-at-work generation: a little **guardian** for your presence, a bit of **fun**, and zero **hustle culture**. Your green light, your rules.

**Languages:** [English](README.md) · [日本語](README.ja.md) · [中文](README.zh-CN.md) · [한국어](README.ko.md)

> **Why “Green Light Hero”?** 绿灯侠 (lǜdēng xiá)—“the one who keeps the light green.” Your status stays green so you can breathe. No performative presence, just a little nudge when the system needs it.

---

## Quick start (recommended)

**A pre-built executable is included in this repository.** No Python or build step required.

- **Windows:** Open the `dist` folder and run **TeamsKeepAlive.exe** (double-click or from a terminal).
- **macOS:** The repo contains a Windows .exe only. On a Mac, either run `python3 main.py` (see “Run the Python script” below) or build a Mac binary on a Mac with `./build.sh` (see “Build for macOS”).
3. A console window opens. Every **4 minutes** you’ll see: `Keep-alive sent (mouse 1px move)`.
4. To stop: press **Ctrl+C** (or **Ctrl+C** in Terminal on Mac) or close the window.

That’s it. On Windows, works as long as running .exe files is allowed.

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

If the maintainer publishes [Releases](https://github.com/shen341/Teams_status_active/releases), you can download **TeamsKeepAlive.exe** from there and run it without cloning the full repo.

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

### Build for macOS (on a Mac)

You must run the build **on a Mac**; PyInstaller produces a native binary for the system where it runs.

**Quick build:**

```bash
chmod +x build.sh
./build.sh
```

**Manual build:**

```bash
pip install -r requirements.txt -r requirements-build.txt
python3 -m PyInstaller --clean --noconfirm TeamsKeepAlive.mac.spec
```

The output is **`dist/TeamsKeepAlive`** (no file extension). Run it with `./dist/TeamsKeepAlive`. You can share this single file with macOS users; they do not need Python installed.

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
| `build.bat` | Build for Windows (batch) |
| `build.ps1` | Build for Windows (PowerShell) |
| `build.sh` | Build for macOS (run on a Mac) |
| `TeamsKeepAlive.mac.spec` | PyInstaller spec for macOS |

---

## Creating a GitHub Release (for maintainers)

If the Releases page shows 404, no release has been created yet. Follow these steps to publish **TeamsKeepAlive.exe** on GitHub Releases so users can download it without cloning the repo.

### 1. Push your code and ensure the repo exists

- Repository URL: **https://github.com/shen341/Teams_status_active**
- If the repo name is still `SNS_status_active`, rename it: **Settings → General → Repository name** → change to `Teams_status_active` → **Rename**.
- Ensure `dist\TeamsKeepAlive.exe` is committed and pushed (or you will upload it in step 4).

### 2. Open the Releases section

- On the repo page, click **Releases** (right-hand side), or go to:  
  **https://github.com/shen341/Teams_status_active/releases**
- Click **Create a new release**.

### 3. Fill in the release details

- **Choose a tag:** Click **Choose tag**, type a version (e.g. `v1.0.0`), select **Create new tag: v1.0.0 on publish**.
- **Release title:** e.g. `v1.0.0 - 绿灯侠 (Green Light Hero)`.
- **Description:** You can paste a short description and link to the README. Example:
  ```text
  Pre-built **TeamsKeepAlive.exe** for Windows. No Python required.
  See [README](https://github.com/shen341/Teams_status_active#quick-start-recommended) for usage.
  ```

### 4. Attach the .exe and publish

- In **Attach binaries**, drag and drop **TeamsKeepAlive.exe** (from your local `dist` folder), or click to select the file.
- Leave **Set as the latest release** checked if this is your first release.
- Click **Publish release**.

After that, **https://github.com/shen341/Teams_status_active/releases** will show the release and users can download the .exe from there.

### Updating a release later

- Go to **Releases** → click the existing release (e.g. v1.0.0) → **Edit**.
- Upload a new .exe or add release notes, then **Update release**.

---

## License

This project is licensed under the **MIT License**. See [LICENSE](LICENSE) for the full text.
