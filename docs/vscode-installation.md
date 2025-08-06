# Visual Studio Code 설치 및 개발 환경 설정 (Python + GitHub Copilot)

이 문서는 Windows 기준으로 VSCode 설치, Python 개발 환경 구성, GitHub Copilot 연결까지의 전체 과정을 설명합니다.

---

## 1. VSCode 설치

### 설치 파일 다운로드

- 공식 웹사이트: https://code.visualstudio.com/
- "Download for Windows" 클릭 후 설치 파일 실행

### 설치 중 추천 옵션

- Add to PATH
- Register Code as editor for supported file types
- "Open with Code" 옵션 체크 시 탐색기 우클릭 메뉴에서 코드 열기 가능

---

## 2. 확장 프로그램 설치

VSCode 실행 후 좌측 Extensions 탭에서 아래 확장들을 설치합니다.

- Python
- Jupyter (노트북 사용 시)
- Pylance
- GitHub Copilot
- GitHub Copilot Chat (선택)
- Code Runner (선택)

---

## 3. Python 인터프리터 설정

### 인터프리터 선택 방법

1. Ctrl + Shift + P → "Python: Select Interpreter"
2. 설치된 Python 버전 선택 (예: Python 3.11.5 64-bit)
3. 가상환경을 사용하는 경우 해당 가상환경을 선택

```bash
# 가상환경 생성
python -m venv venv

# 가상환경 활성화 (Windows)
venv\Scripts\activate
```

---

## 4. 코드 실행 방법

### Run 버튼 사용

- 상단 "Run Python File" 버튼 클릭
- 또는 단축키 Ctrl + F5

### 터미널에서 직접 실행

```bash
python my_script.py
```

---

## 5. 프로젝트 설정 자동화 (.vscode/settings.json)

프로젝트 루트에 `.vscode/settings.json` 파일을 만들고 다음 내용을 입력합니다.

```json
{
  "python.pythonPath": "venv/Scripts/python.exe",
  "python.formatting.provider": "black",
  "editor.formatOnSave": true,
  "python.linting.enabled": true,
  "python.linting.pylintEnabled": true
}
```

---

## 6. GitHub Copilot 연결

### 로그인 및 활성화

1. 좌측 하단 계정 아이콘 클릭 → "Sign in to GitHub"
2. 브라우저에서 인증 완료
3. "Copilot ready" 메시지가 우측 하단에 표시되면 사용 준비 완료

### 사용 방법

- 주석을 입력하면 자동으로 코드 제안이 표시됨
- Tab 키를 눌러 제안을 수락

### Copilot Chat (선택)

- Ctrl + Shift + I 를 눌러 대화창을 열고, 자연어로 코드 요청 가능

---

## 7. Git 및 GitHub 연동 (선택)

### Git 초기화 및 첫 커밋

```bash
git init
git add .
git commit -m "Initial commit"
```

### GitHub 원격 저장소 연결

```bash
git remote add origin https://github.com/username/repo.git
git push -u origin main
```

VSCode 내 Source Control 탭에서 변경 사항을 시각적으로 확인하고 커밋, 푸시 가능

---

## 요약

- VSCode 설치 및 Python 개발 환경 구성 완료
- 확장 설치: Python, Pylance, Copilot 등
- 가상환경 생성 및 설정 연동
- GitHub Copilot 로그인 및 사용 가능
- GitHub 연동을 통한 소스 버전 관리 가능

이제 VSCode는 Python과 AI 개발을 위한 통합 환경으로 활용할 수 있습니다.
