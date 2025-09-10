---
layout: post
title: "Gemini CLI Execution and Deployment"
date: 2025-09-10
---
# Gemini CLI 실행 및 배포 아키텍처

## Gemini CLI 실행하기
Gemini CLI를 실행하는 방법에는 여러 가지가 있습니다. 선택하는 방식은 사용 목적에 따라 달라집니다.

### 1. 표준 설치 (일반 사용자 권장)
가장 권장되는 설치 방법으로, NPM 레지스트리에서 Gemini CLI 패키지를 다운로드하여 설치합니다.

- **글로벌 설치**
```bash
npm install -g @google/gemini-cli
```
어디서든 CLI 실행:
```bash
gemini
```

- **NPX 실행**
```bash
# 글로벌 설치 없이 NPM에서 최신 버전 실행
npx @google/gemini-cli
```

### 2. 샌드박스 실행 (Docker/Podman)
보안 및 격리를 위해 Gemini CLI를 컨테이너 내에서 실행할 수 있습니다. 이는 부작용이 있을 수 있는 도구 실행 시 기본 방식입니다.

- **레지스트리에서 직접 실행**
```bash
docker run --rm -it us-docker.pkg.dev/gemini-code-dev/gemini-cli/sandbox:0.1.1
```

- **--sandbox 플래그 사용**
```bash
gemini --sandbox -y -p "your prompt here"
```

### 3. 소스 코드 실행 (프로젝트 기여자 권장)
프로젝트 기여자는 소스 코드에서 직접 CLI를 실행할 수 있습니다.

- **개발 모드 (핫 리로딩 지원)**
```bash
npm run start
```

- **프로덕션 유사 모드 (Linked package)**
```bash
# 로컬 cli 패키지를 글로벌 node_modules에 연결
npm link packages/cli

# 이제 `gemini` 명령으로 실행 가능
gemini
```

### 4. GitHub 최신 커밋 실행
GitHub 저장소의 최신 커밋 버전을 바로 실행할 수 있습니다.

```bash
npx https://github.com/google-gemini/gemini-cli
```

---

## 배포 아키텍처
위 실행 방식들은 다음과 같은 아키텍처 구성 요소와 프로세스로 가능해집니다.

### NPM 패키지
Gemini CLI 프로젝트는 모노레포 구조이며, 두 개의 핵심 패키지를 NPM에 배포합니다.

- `@google/gemini-cli-core`: 백엔드, 로직 및 도구 실행 처리
- `@google/gemini-cli`: 사용자용 프런트엔드

### 빌드 및 패키징 프로세스
배포 채널에 따라 두 가지 빌드 프로세스를 사용합니다.

- **NPM 배포**  
  TypeScript 소스를 `tsc`로 컴파일하여 `dist/` 디렉토리에 생성 후 배포.

- **GitHub npx 실행**  
  `package.json`의 `prepare` 스크립트가 `esbuild`를 사용해 전체 앱과 의존성을 하나의 self-contained JS 파일로 번들링.

### Docker 샌드박스 이미지
`gemini-cli-sandbox` 컨테이너 이미지로 제공되며, 글로벌 설치된 Gemini CLI가 포함됨.

### 릴리즈 프로세스
GitHub Actions를 통해 자동화되며, 다음을 수행합니다:

1. `tsc`로 NPM 패키지 빌드  
2. 아티팩트 레지스트리에 NPM 패키지 배포  
3. GitHub 릴리즈 생성 및 번들 자산 업로드  

출처 : https://github.com/google-gemini/gemini-cli/blob/main/docs/deployment.md
