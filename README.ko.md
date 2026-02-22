# 绿灯侠 (녹등협 · 초록불 히어로)

**상태 등이 계속 초록색이도록.** Microsoft Teams가 5분만 무작동해도 **자리 비움(Away / Be right back)** 으로 바뀌는 걸 막는 경량 Windows 도구입니다.

젊은 직장인을 위한 **작은 수호자**. 가볍고, 재밌고, **과한 내전은 거부**. 당신의 초록불, 당신이 정해요.

**언어:** [English](README.md) · [日本語](README.ja.md) · [中文](README.zh-CN.md) · [한국어](README.ko.md)

> **왜 「绿灯侠」?** “초록불을 지켜 주는 히어로.” 상태 등이 초록색으로 남아 있게 해서, 과한 ‘보여주기 출근’ 없이 일할 수 있게 해 주는 작은 도우미예요.

---

## 빠른 시작 (권장)

**이 리포지토리에는 빌드된 실행 파일이 포함되어 있습니다(Windows용).** Windows에서는 Python이 필요 없습니다. **macOS**에서는 `python3 main.py`로 실행하거나, Mac에서 `./build.sh`로 macOS용 바이너리를 빌드하세요(「macOS용 빌드」 참고).

1. 이 리포지토리를 **클론 또는 다운로드**합니다.
2. **Windows:** **dist** 폴더에서 **TeamsKeepAlive.exe** 실행(더블클릭 또는 터미널). **macOS:** 위 참고.
3. 콘솔 창이 열리고 **4분마다** `Keep-alive sent (mouse 1px move)` 가 출력됩니다.
4. **종료:** 해당 창에서 **Ctrl+C**를 누르거나 창을 닫습니다.

이대로 사용할 수 있습니다. 회사 PC에서 .exe 실행만 허용되면 사용 가능합니다.

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

## 그 외 실행 방법

### Releases에서 .exe 받기

관리자가 [Releases](https://github.com/shen341/Teams_status_active/releases)를 올려 두었다면, 여기서 **TeamsKeepAlive.exe**만 받아 전체 리포지토리 클론 없이 실행할 수 있습니다.

### Python 스크립트로 실행 (Python이 있는 경우)

1. 의존성 설치:
   ```bash
   pip install -r requirements.txt
   ```
2. 실행:
   ```bash
   python main.py
   ```
3. **Ctrl+C**로 종료합니다.

### 소스에서 .exe 빌드 (배포자 또는 바이너리를 직접 확인하고 싶은 경우)

빌드하는 PC에 **Python 3.7 이상**이 필요합니다.

**간단 빌드 (Windows):** **build.bat**을 더블클릭하거나, PowerShell에서 `.\build.ps1` 실행.  
실행 정책으로 차단되면 한 번만 `Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned` 실행 후 다시 `.\build.ps1` 실행합니다.

**수동 빌드:**

```batch
pip install -r requirements.txt -r requirements-build.txt
python -m PyInstaller --clean --noconfirm TeamsKeepAlive.spec
```

생성된 .exe는 **`dist\TeamsKeepAlive.exe`** 입니다. 이 파일만 다른 사용자에게 배포해도 됩니다.

### macOS용 빌드 (Mac에서 실행)

macOS용 바이너리는 **Mac에서 빌드**해야 합니다. PyInstaller는 실행한 OS에 맞는 바이너리를 만듭니다.

**간단 빌드:**

```bash
chmod +x build.sh
./build.sh
```

**수동 빌드:**

```bash
pip install -r requirements.txt -r requirements-build.txt
python3 -m PyInstaller --clean --noconfirm TeamsKeepAlive.mac.spec
```

출력은 **`dist/TeamsKeepAlive`** (확장자 없음)입니다. `./dist/TeamsKeepAlive`로 실행합니다. 이 한 파일만 macOS 사용자에게 배포하면 됩니다(Python 불필요).

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
[2025-02-22 10:00:00] Teams Keep-Alive started (Ctrl+C to stop)
[2025-02-22 10:00:00] Interval: 240 sec (4 min)
[2025-02-22 10:00:00] Keep-alive sent (mouse 1px move)
[2025-02-22 10:04:00] Keep-alive sent (mouse 1px move)
...
^C
[2025-02-22 10:05:30] Stopped.
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
| `dist\TeamsKeepAlive.exe` | 미리 빌드된 실행 파일 (그대로 실행 가능) |
| `requirements.txt` | 실행 시 의존성 (pynput) |
| `requirements-build.txt` | 빌드 시 의존성 (PyInstaller) |
| `TeamsKeepAlive.spec` | PyInstaller 단일 .exe 설정 |
| `build.bat` | .exe 빌드용 배치 |
| `build.ps1` | Windows .exe 빌드용 PowerShell |
| `build.sh` | macOS 빌드 (Mac에서 실행) |
| `TeamsKeepAlive.mac.spec` | PyInstaller spec (macOS) |

---

## GitHub Release 만들기 (관리자)

Releases 페이지에서 404가 나오면 아직 릴리스가 없는 상태입니다. 아래 순서대로 **TeamsKeepAlive.exe**를 GitHub Releases에 올리면, 사용자가 저장소를 클론하지 않고도 다운로드할 수 있습니다.

1. **저장소 준비**  
   저장소 URL: **https://github.com/shen341/Teams_status_active**. 이름이 아직 `SNS_status_active`이면 **Settings → General → Repository name**에서 `Teams_status_active`로 변경 후 **Rename**. `dist\TeamsKeepAlive.exe`를 커밋해 두거나, 4단계에서 직접 업로드합니다.

2. **Releases 열기**  
   저장소 페이지에서 **Releases** 클릭, 또는 **https://github.com/shen341/Teams_status_active/releases** 접속 후 **Create a new release** 클릭.

3. **릴리스 정보 입력**  
   **Choose a tag**에서 버전(예: `v1.0.0`) 입력 후 **Create new tag: v1.0.0 on publish** 선택. **Release title** 예: `v1.0.0 - 绿灯侠`. **Description**에 간단한 설명과 README 링크 작성.

4. **.exe 첨부 후 배포**  
   **Attach binaries**에 로컬 **dist\TeamsKeepAlive.exe**를 끌어다 놓거나 선택. **Set as the latest release** 체크(첫 릴리스인 경우) 후 **Publish release** 클릭.

이후 **https://github.com/shen341/Teams_status_active/releases**에서 릴리스가 보이고, 사용자가 여기서 .exe를 받을 수 있습니다. 수정 시 해당 릴리스 → **Edit**에서 새 .exe를 올리거나 설명을 수정한 뒤 **Update release**하면 됩니다. 자세한 단계는 [README.md](README.md#creating-a-github-release-for-maintainers) 참고.

---

## 라이선스

이 프로젝트는 **MIT 라이선스**로 제공됩니다. 전문은 [LICENSE](LICENSE)를 참조하세요.
