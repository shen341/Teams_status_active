#!/usr/bin/env python3
"""
Teams離席状態（5分無操作での Away / Be right back）を防ぐキープアライブスクリプト。

OS標準の入力としてマウスを1ピクセルだけ動かし、システムの「最後の入力時刻」を更新します。
TeamsはWindowsのGetLastInputInfo等でアイドルを検知するため、これでアクティブと認識されます。

停止: Ctrl+C
"""

import signal
import sys
import time
from datetime import datetime

try:
    from pynput.mouse import Controller as MouseController
except ImportError:
    print("エラー: pynput がインストールされていません。")
    print("次のコマンドを実行してください: pip install -r requirements.txt")
    sys.exit(1)

# 設定（4分 = 5分の無操作になる前に1回実行）
INTERVAL_SEC = 4 * 60
# マウスを動かす量（1ピクセル。往復で元の位置に戻すためドリフトなし）
MOVE_PIXEL = 1


def log(msg: str) -> None:
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{ts}] {msg}", flush=True)


def keep_alive(mouse: MouseController) -> None:
    """マウスを1px動かしてシステムの「最後の入力」を更新する。"""
    mouse.move(MOVE_PIXEL, 0)
    time.sleep(0.05)
    mouse.move(-MOVE_PIXEL, 0)


def main() -> None:
    mouse = MouseController()
    log("Teams キープアライブを開始しました（Ctrl+C で停止）")
    log(f"間隔: {INTERVAL_SEC} 秒 ({INTERVAL_SEC // 60} 分)")

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
            log("キープアライブ送信（マウス 1px 移動）")
            # 間隔まで1秒ずつスリープ（Ctrl+C で早めに抜けられる）
            for _ in range(INTERVAL_SEC):
                if not running:
                    break
                time.sleep(1)
    except KeyboardInterrupt:
        pass

    log("終了しました。")


if __name__ == "__main__":
    main()
