#!/usr/bin/env python3
"""
Teams Keep-Alive: prevents Away / Be right back after ~5 min inactivity.

Moves the mouse by 1 pixel (then back) so the system's "last input" time is updated.
Teams uses Windows idle detection (e.g. GetLastInputInfo), so this keeps you active.

Stop: Ctrl+C
"""

import signal
import sys
import time
from datetime import datetime

try:
    from pynput.mouse import Controller as MouseController
except ImportError:
    print("Error: pynput is not installed.")
    print("Run: pip install -r requirements.txt")
    sys.exit(1)

# Interval: 4 min (before Teams' ~5 min idle threshold)
INTERVAL_SEC = 4 * 60
# Mouse movement: 1 pixel there and back (no cursor drift)
MOVE_PIXEL = 1


def log(msg: str) -> None:
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{ts}] {msg}", flush=True)


def keep_alive(mouse: MouseController) -> None:
    """Move mouse 1px to update system 'last input' time."""
    mouse.move(MOVE_PIXEL, 0)
    time.sleep(0.05)
    mouse.move(-MOVE_PIXEL, 0)


def main() -> None:
    mouse = MouseController()
    log("Teams Keep-Alive started (Ctrl+C to stop)")
    log(f"Interval: {INTERVAL_SEC} sec ({INTERVAL_SEC // 60} min)")

    running = True

    def on_signal(_sig, _frame):
        nonlocal running
        running = False

    signal.signal(signal.SIGINT, on_signal)
    if hasattr(signal, "SIGBREAK"):
        signal.signal(signal.SIGBREAK, on_signal)

    try:
        while running:
            keep_alive(mouse)
            log("Keep-alive sent (mouse 1px move)")
            # Sleep 1 sec at a time so Ctrl+C exits promptly
            for _ in range(INTERVAL_SEC):
                if not running:
                    break
                time.sleep(1)
    except KeyboardInterrupt:
        pass

    log("Stopped.")


if __name__ == "__main__":
    main()
