# Teams 保持在线

一款轻量级 Windows 小工具，用于防止 Microsoft Teams 在约 5 分钟无操作后自动变为 **离开（Away / Be right back）**。通过 **系统级鼠标移动** 更新“最后输入时间”，让系统和 Teams 认为你仍在活动。

**语言:** [English](README.md) · [日本語](README.ja.md) · [中文](README.zh-CN.md) · [한국어](README.ko.md)

---

## 快速开始（推荐）

**本仓库已包含构建好的 .exe 文件。** 无需安装 Python 或自行构建。

1. **克隆或下载** 本仓库。
2. 打开 **dist** 文件夹，运行 **TeamsKeepAlive.exe**（双击或在终端中运行）。
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

若维护者发布了 [Releases](https://github.com/YOUR_USERNAME/SNS_status_active/releases)，可从该页下载 **TeamsKeepAlive.exe**，无需克隆完整仓库即可运行。

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
| `build.ps1` | 构建 .exe 用 PowerShell 脚本 |

---

## 许可证

本项目采用 **MIT 许可证**。完整条文见 [LICENSE](LICENSE)。
