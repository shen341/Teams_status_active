# Teams Keep-Alive (팀즈 자리 비움 방지)

Microsoft Teams가 약 5분 동안 무작동 시 **자리 비움(Away / Be right back)** 으로 바뀌는 것을 막는 경량 Windows 도구입니다. **OS 수준의 마우스 이동**으로 "마지막 입력"을 갱신하여 Teams가 사용자를 계속 활성으로 인식하게 합니다.

**언어:** [English](README.md) · [日本語](README.ja.md) · [中文](README.zh-CN.md) · [한국어](README.ko.md)

---

## 동작 원리

- **Teams가 자리 비움으로 바뀌는 이유:** Teams는 Windows의 **시스템 유휴 감지**(예: `GetLastInputInfo`)를 사용해 사용자 활동 여부를 판단합니다. 마우스·키보드 입력이 약 5분 없으면 자리 비움으로 표시됩니다.
- **이 도구가 하는 일:** 일정 간격(기본 **4분마다**)으로 **마우스를 1픽셀만 움직였다가 되돌립니다**. 이게 사용자 입력으로 처리되어 Windows의 "마지막 입력 시각"이 갱신되고, Teams는 **사용 가능(Available)** 상태를 유지합니다.
- **Teams 프로세스를 건드리지 않음:** Teams 프로세스에 주입하거나 수정하지 않습니다. OS 표준의 "마우스가 조금 움직였다"는 입력만 시뮬레이션합니다.

---

## 보안

- **로컬 전용:** 네트워크 접속·원격 수집·전송 없음. 모든 동작은 사용자 PC에서만 이루어집니다.
- **키 입력·화면 수집 없음:** 마우스만 1픽셀씩 움직입니다. 키 입력 기록, 클립보드, 화면 캡처 등을 하지 않습니다.
- **오픈 소스:** [main.py](main.py)와 빌드 스크립트 전체가 소스로 공개되어 있습니다. 신뢰를 위해 아래 "소스에서 빌드" 절차대로 직접 .exe를 빌드해 사용할 수 있습니다.

---

## 사용 방법

### 방법 1: .exe 실행 (Python 불필요) — 대부분의 사용자 권장

1. **TeamsKeepAlive.exe**를 준비합니다 ([Releases](https://github.com/YOUR_USERNAME/SNS_status_active/releases) 또는 빌드한 분에게 받음).
2. 아무 폴더에 넣고 **더블클릭**으로 실행합니다.
3. 검은 콘솔 창이 뜨고 **4분마다** "キープアライブ送信（マウス 1px 移動）" 같은 로그가 출력됩니다.
4. **종료:** 해당 창에서 **Ctrl+C**를 누르거나 창을 닫습니다.

설치·Python 불필요입니다. 회사 PC에서 .exe 실행만 허용되면 사용 가능합니다.

### 방법 2: Python 스크립트로 실행 (Python이 있는 경우)

1. 의존성 설치:
   ```bash
   pip install -r requirements.txt
   ```
2. 실행:
   ```bash
   python main.py
   ```
3. **Ctrl+C**로 종료합니다.

### 방법 3: 소스에서 .exe 빌드 (배포자 또는 바이너리를 직접 확인하고 싶은 경우)

빌드하는 PC에 **Python 3.7 이상**이 필요합니다.

**간단 빌드 (Windows):**

- **build.bat**을 더블클릭하거나, PowerShell에서:
  ```powershell
  .\build.ps1
  ```
- 실행 정책으로 차단되면 한 번만:  
  `Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned` 실행 후 다시 `.\build.ps1` 실행합니다.

**수동 빌드:**

```batch
pip install -r requirements.txt -r requirements-build.txt
python -m PyInstaller --clean --noconfirm TeamsKeepAlive.spec
```

생성된 .exe는 **`dist\TeamsKeepAlive.exe`** 입니다. 이 파일만 다른 사용자에게 배포해도 됩니다.

---

## 간격 변경

**main.py**의 `INTERVAL_SEC`를 수정합니다.

```python
INTERVAL_SEC = 4 * 60   # 4분. 예: 2*60 = 2분, 5*60 = 5분
```

수정 후 스크립트를 다시 실행하거나, 위 절차로 .exe를 다시 빌드합니다.

---

## 출력 예시

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

## 참고 사항

- 소속 조직의 이용 규정·IT 정책을 준수해 사용하세요.
- Slack, Zoom 등 시스템 유휴를 쓰는 다른 앱도 이 도구 실행 중에는 "활성"으로 보일 수 있습니다.

---

## 프로젝트 파일

| 파일 | 설명 |
|------|------|
| `main.py` | 메인 스크립트 (이 한 파일만으로 실행 가능) |
| `requirements.txt` | 실행 시 의존성 (pynput) |
| `requirements-build.txt` | 빌드 시 의존성 (PyInstaller) |
| `TeamsKeepAlive.spec` | PyInstaller 단일 .exe 설정 |
| `build.bat` | .exe 빌드용 배치 |
| `build.ps1` | .exe 빌드용 PowerShell |

배포 시에는 빌드로 생성된 **`dist\TeamsKeepAlive.exe`** 만 전달하면 됩니다.
