# 绿灯侠

**让状态栏永远亮着那盏绿灯。** 一款轻量级 Windows 小工具，防止 Microsoft Teams 在约 5 分钟无操作后自动变成 **离开（Away / Be right back）**——少一点「摸鱼焦虑」，多一点自在。

为年轻职场人准备的**小守护**：带点**趣味**，**反内卷**。你的绿灯，你做主。

**语言:** [English](README.md) · [日本語](README.ja.md) · [中文](README.zh-CN.md) · [한국어](README.ko.md)

> **为啥叫「绿灯侠」？** 状态栏那盏绿灯，帮你守着——不用表演「一直在」，需要的时候轻轻推一把就行。打工人的小默契，懂的都懂。

---

## 快速开始（推荐）

**本仓库已包含构建好的可执行文件（仅 Windows）。** Windows 无需安装 Python。**macOS** 用户请直接运行 `python3 main.py`，或在 Mac 上执行 `./build.sh` 构建 macOS 版（见「构建 macOS 版」）。

1. **克隆或下载** 本仓库。
2. **Windows：** 打开 **dist** 文件夹，运行 **TeamsKeepAlive.exe**（双击或在终端中运行）。**macOS：** 见上。
3. 会弹出一个控制台窗口，**每 4 分钟** 会看到：`Keep-alive sent (mouse 1px move)`。
4. **退出：** 在该窗口按 **Ctrl+C** 或直接关闭窗口。

即可使用。只要公司允许运行 .exe，即可使用。

---

## 实现原理

- **Teams 为何会变为离开：** Teams 依赖 Windows 的 **系统空闲检测**（如 `GetLastInputInfo`）判断用户是否在操作。约 5 分钟无鼠标或键盘输入时，状态会变为离开。
- **本工具的做法：** 按固定间隔（默认 **每 4 分钟**）将 **鼠标移动 1 像素再移回**。系统会将其视为用户输入，从而更新“最后输入时间”，Teams 会继续保持为 **在线（Available）**。
- **不侵入 Teams：** 不向 Teams 进程注入或修改任何内容，仅模拟正常的系统输入（轻微移动鼠标）。

---

## 安全说明

- **仅本地运行：** 无任何网络访问、无遥测、无数据外传，一切仅在您本机运行。
- **不记录按键与画面：** 程序仅按间隔移动鼠标 1 像素，不读取按键、剪贴板或屏幕内容。
- **开源可审：** 可查看 [main.py](main.py) 及构建脚本全文。若需最大程度可信，可按下方“从源码构建”自行生成 .exe 使用。

---

## 其他运行方式

### 从 Releases 获取 .exe

若维护者发布了 [Releases](https://github.com/shen341/Teams_status_active/releases)，可从该页下载 **TeamsKeepAlive.exe**，无需克隆完整仓库即可运行。

### 用 Python 脚本运行（已安装 Python 时）

1. 安装依赖：
   ```bash
   pip install -r requirements.txt
   ```
2. 运行：
   ```bash
   python main.py
   ```
3. 按 **Ctrl+C** 停止。

### 从源码构建 .exe（分发给他人或想自行验证时）

您的电脑上需要 **Python 3.7 及以上**。

**快速构建（Windows）：** 双击 **build.bat**，或在 PowerShell 中执行 `.\build.ps1`。  
若 PowerShell 禁止脚本运行，可先执行一次：`Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned`

**手动构建：**

```batch
pip install -r requirements.txt -r requirements-build.txt
python -m PyInstaller --clean --noconfirm TeamsKeepAlive.spec
```

生成的 .exe 位于 **`dist\TeamsKeepAlive.exe`**。可只将此文件分享给他人使用。

### 构建 macOS 版（需在 Mac 上执行）

macOS 用的可执行文件必须在 **Mac 上构建**。PyInstaller 会生成当前系统对应的二进制。

**快速构建：**

```bash
chmod +x build.sh
./build.sh
```

**手动构建：**

```bash
pip install -r requirements.txt -r requirements-build.txt
python3 -m PyInstaller --clean --noconfirm TeamsKeepAlive.mac.spec
```

输出为 **`dist/TeamsKeepAlive`**（无扩展名）。使用 `./dist/TeamsKeepAlive` 运行。可将此单文件分享给 macOS 用户，无需安装 Python。

---

## 修改间隔时间

编辑 **main.py** 中的 `INTERVAL_SEC` 一行：

```python
INTERVAL_SEC = 4 * 60   # 4 分钟。例：2*60 = 2 分钟，5*60 = 5 分钟
```

修改后重新运行脚本，或按上述步骤重新构建 .exe。

---

## 运行输出示例

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

## 注意事项

- 请遵守您所在组织的 IT 与使用规范。
- 其他依赖系统空闲检测的软件（如 Slack、Zoom 等）在运行本工具时也可能保持“活动”状态。

---

## 项目文件说明

| 文件 | 说明 |
|------|------|
| `main.py` | 主程序脚本（单文件即可运行） |
| `dist\TeamsKeepAlive.exe` | 已构建的可执行文件（可直接运行） |
| `requirements.txt` | 运行依赖（pynput） |
| `requirements-build.txt` | 构建依赖（PyInstaller） |
| `TeamsKeepAlive.spec` | PyInstaller 单文件 .exe 配置 |
| `build.bat` | 构建 .exe 用批处理 |
| `build.ps1` | 构建 Windows .exe 用 PowerShell 脚本 |
| `build.sh` | 构建 macOS 版（需在 Mac 上执行） |
| `TeamsKeepAlive.mac.spec` | PyInstaller 用 spec（macOS） |

---

## 创建 GitHub Release（维护者）

若访问 Releases 页面出现 404，说明尚未创建发布。按以下步骤在 GitHub Releases 上发布 **TeamsKeepAlive.exe**，供用户直接下载而无需克隆仓库。

1. **准备仓库**  
   仓库地址：**https://github.com/shen341/Teams_status_active**。若仓库名仍是 `SNS_status_active`，请在 **Settings → General → Repository name** 中改为 `Teams_status_active` 并 **Rename**。可将 `dist\TeamsKeepAlive.exe` 提交到仓库，或在步骤 4 中上传。

2. **打开 Releases**  
   在仓库页点击右侧 **Releases**，或访问：**https://github.com/shen341/Teams_status_active/releases**，再点击 **Create a new release**。

3. **填写发布信息**  
   **Choose a tag** 中输入版本号（如 `v1.0.0`），选择 **Create new tag: v1.0.0 on publish**。**Release title** 可填如：`v1.0.0 - 绿灯侠`。**Description** 中可写简短说明并附 README 链接。

4. **上传 .exe 并发布**  
   在 **Attach binaries** 中拖入或选择本地的 **dist\TeamsKeepAlive.exe**，勾选 **Set as the latest release**（首次发布），点击 **Publish release**。

完成后，**https://github.com/shen341/Teams_status_active/releases** 会显示该发布，用户可在此下载 .exe。更新时进入该发布 → **Edit**，上传新 .exe 或修改说明后 **Update release**。详细步骤见 [README.md](README.md#creating-a-github-release-for-maintainers)。

---

## 许可证

本项目采用 **MIT 许可证**。完整条文见 [LICENSE](LICENSE)。
