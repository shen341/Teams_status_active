# 绿灯侠（グリーンライトヒーロー）

**ステータスをずっと「緑」のままに。** 約5分の無操作で Teams が **Away（離席・Be right back）** になるのを防ぐ、軽量ツールです。

若手社会人のための、ちょっとした**守り**と**ユーモア**。過度な「見せかけ在席」競争はナシ。あなたの緑ランプは、あなたのペースで。

**言語:** [English](README.md) · [日本語](README.ja.md) · [中文](README.zh-CN.md) · [한국어](README.ko.md)

> **「绿灯侠」って？** 中国語で「緑のランプを守るヒーロー」。ステータスを緑のままにして、肩の力を抜いて働けるようにする、ちょっとした味方です。見せかけの在席じゃなく、必要なときだけそっと押してくれるだけ。

---

## クイックスタート（推奨）

**リポジトリにビルド済み実行ファイルが含まれています（Windows 用）。** Windows では Python 不要です。**macOS** の場合は `python3 main.py` で実行するか、Mac 上で `./build.sh` により macOS 用バイナリをビルドしてください（「macOS 用にビルドする」参照）。

1. このリポジトリを **クローンまたはダウンロード** する。
2. **Windows:** **dist** フォルダを開き、**TeamsKeepAlive.exe** を実行（ダブルクリックまたはターミナルから）。**macOS:** 上記のとおり。
3. コンソール画面が開き、**4 分ごと**に `Keep-alive sent (mouse 1px move)` と表示されます。
4. **終了:** その画面で **Ctrl+C** を押すか、ウィンドウを閉じます。

これだけで利用できます。会社 PC で .exe の実行が許可されていれば利用可能です。

---

## 実現原理（どう動くか）

- **Teams が離席になる理由:** Teams は Windows の **システムのアイドル検知**（`GetLastInputInfo` など）を使って「操作があったか」を判断しています。マウスやキーボードの入力が約5分ないと、Away になります。
- **このツールのやること:** 一定間隔（デフォルト **4 分ごと**）に、**マウスを 1 ピクセルだけ動かしてすぐ戻す**だけです。これが「ユーザー入力」として扱われるため、Windows の「最後の入力時刻」が更新され、Teams は **在席（Available）** のままになります。
- **Teams を直接いじらない:** Teams のプロセスに注入したり改変したりはしません。OS 標準の「マウスが少し動いた」という入力シミュレーションだけです。

---

## セキュリティ

- **ローカルのみ:** ネットワーク通信・テレメトリ・外部送信は一切ありません。すべてお使いの PC 上だけで動作します。
- **キー入力や画面の取得なし:** マウスを 1 ピクセル動かすだけです。キー入力の記録・クリップボード・画面キャプチャ等は行いません。
- **オープンソース:** [main.py](main.py) とビルドスクリプトはすべてソースで公開されています。信頼性を最大にするには、以下「ソースからビルド」の手順でご自身で .exe をビルドして利用できます。

---

## その他の実行方法

### Releases から .exe を取得する

管理者が [Releases](https://github.com/shen341/Teams_status_active/releases) を公開している場合は、そこから **TeamsKeepAlive.exe** をダウンロードし、リポジトリ全体をクローンせずに実行できます。

### Python スクリプトで実行する（Python がある場合）

1. 依存関係をインストール:
   ```bash
   pip install -r requirements.txt
   ```
2. 実行:
   ```bash
   python main.py
   ```
3. 終了は **Ctrl+C**。

### ソースから .exe をビルドする（配布する方・中身を確認したい方）

ビルドする PC には **Python 3.7 以上**が必要です。

**手早くビルド（Windows）:** **build.bat** をダブルクリックするか、PowerShell で `.\build.ps1` を実行。  
実行ポリシーでブロックされる場合は、一度だけ `Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned` を実行してから再度 `.\build.ps1` を実行してください。

**手動でビルド:**

```batch
pip install -r requirements.txt -r requirements-build.txt
python -m PyInstaller --clean --noconfirm TeamsKeepAlive.spec
```

生成される .exe は **`dist\TeamsKeepAlive.exe`** です。この 1 ファイルだけを配布して構いません。

### macOS 用にビルドする（Mac 上で実行）

macOS 用のバイナリは **Mac 上でビルド**する必要があります。PyInstaller は実行した OS 向けのバイナリを出力します。

**手早くビルド:**

```bash
chmod +x build.sh
./build.sh
```

**手動でビルド:**

```bash
pip install -r requirements.txt -r requirements-build.txt
python3 -m PyInstaller --clean --noconfirm TeamsKeepAlive.mac.spec
```

出力は **`dist/TeamsKeepAlive`**（拡張子なし）です。`./dist/TeamsKeepAlive` で実行できます。この 1 ファイルを macOS ユーザーに配布できます（Python 不要）。

---

## 間隔を変えたい場合

**main.py** の `INTERVAL_SEC` を編集します。

```python
INTERVAL_SEC = 4 * 60   # 4分。例: 2*60 = 2分、5*60 = 5分
```

編集後はスクリプトを再実行するか、上記手順で .exe を再ビルドしてください。

---

## 出力例

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

## 注意事項

- 所属組織の利用規約・IT ポリシーに従ってご利用ください。
- 他のアプリ（Slack、Zoom 等）もシステムのアイドルで判定している場合は、同様にアクティブと見なされる可能性があります。

---

## プロジェクト内の主なファイル

| ファイル | 説明 |
|----------|------|
| `main.py` | メインスクリプト（この1本で実行可能） |
| `dist\TeamsKeepAlive.exe` | ビルド済み実行ファイル（そのまま実行可能） |
| `requirements.txt` | 実行時依存（pynput） |
| `requirements-build.txt` | ビルド時依存（PyInstaller） |
| `TeamsKeepAlive.spec` | PyInstaller 用 spec（単一 .exe） |
| `build.bat` | .exe ビルド用バッチ |
| `build.ps1` | .exe ビルド用 PowerShell（Windows） |
| `build.sh` | macOS 用ビルド（Mac 上で実行） |
| `TeamsKeepAlive.mac.spec` | PyInstaller 用 spec（macOS） |

---

## GitHub Release の作成と設定（管理者向け）

Releases ページで 404 が出る場合は、まだリリースが作成されていません。以下の手順で **TeamsKeepAlive.exe** を GitHub Releases に公開し、ユーザーがリポジトリをクローンせずにダウンロードできるようにします。

### 1. リポジトリの準備

- リポジトリ URL: **https://github.com/shen341/Teams_status_active**
- リポジトリ名がまだ `SNS_status_active` の場合は変更: **Settings → General → Repository name** を `Teams_status_active` に変更 → **Rename**。
- `dist\TeamsKeepAlive.exe` をコミット・プッシュしておく（または手順 4 でアップロード）。

### 2. Releases を開く

- リポジトリページで **Releases**（右側）をクリックするか、  
  **https://github.com/shen341/Teams_status_active/releases** にアクセス。
- **Create a new release** をクリック。

### 3. リリース情報を入力

- **Choose a tag:** **Choose tag** をクリックし、バージョン（例: `v1.0.0`）を入力 → **Create new tag: v1.0.0 on publish** を選択。
- **Release title:** 例: `v1.0.0 - 绿灯侠 (Green Light Hero)`。
- **Description:** 簡単な説明や README へのリンクを記入。例:
  ```text
  Windows 用ビルド済み **TeamsKeepAlive.exe**。Python 不要。
  使い方は [README](https://github.com/shen341/Teams_status_active#クイックスタート推奨) を参照。
  ```

### 4. .exe を添付して公開

- **Attach binaries** に、ローカルの **dist** フォルダ内の **TeamsKeepAlive.exe** をドラッグ＆ドロップするか、クリックして選択。
- 初回リリースの場合は **Set as the latest release** にチェックを入れたままにする。
- **Publish release** をクリック。

これで **https://github.com/shen341/Teams_status_active/releases** にリリースが表示され、ユーザーはここから .exe をダウンロードできます。

### 既存リリースの更新

- **Releases** → 該当リリース（例: v1.0.0）をクリック → **Edit**。
- 新しい .exe をアップロードするか説明を編集 → **Update release**。

---

## ライセンス

本プロジェクトは **MIT ライセンス** の下で提供されています。全文は [LICENSE](LICENSE) を参照してください。
