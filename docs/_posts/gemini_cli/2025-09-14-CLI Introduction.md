---
layout: post
title: "CLI Introduction"
date: 2025-09-14
categories: [Gemini_CLI]
---

# Gemini CLI
Gemini CLI에서 `packages/cli`는 사용자가 Gemini AI 모델 및 관련 도구와 프롬프트를 주고받을 수 있는 프런트엔드 역할을 합니다.  
Gemini CLI의 전체 개요는 메인 문서 페이지를 참고하세요.

---

## 이 섹션 탐색
- **Authentication**: Google의 AI 서비스 인증 설정 가이드  
- **Commands**: Gemini CLI 명령어 참조 (예: `/help`, `/tools`, `/theme`)  
- **Configuration**: 설정 파일을 이용한 Gemini CLI 동작 사용자화 가이드  
- **Enterprise**: 엔터프라이즈 구성 가이드  
- **Token Caching**: 토큰 캐싱을 통한 API 비용 최적화  
- **Themes**: 다양한 테마를 이용해 CLI 외관을 커스터마이징하는 가이드  
- **Tutorials**: 개발 작업을 자동화하기 위해 Gemini CLI를 사용하는 튜토리얼  

---

## 비대화형 모드 (Non-interactive mode)
Gemini CLI는 비대화형 모드에서 실행할 수 있으며, 이는 스크립팅과 자동화에 유용합니다.  
이 모드에서는 입력을 CLI에 파이프로 전달하면, 명령을 실행하고 종료합니다.

예시: 터미널에서 명령어를 파이프로 전달  
```bash
echo "What is fine tuning?" | gemini
```

Gemini CLI는 명령을 실행하고 결과를 터미널에 출력합니다.  
동일한 동작은 `--prompt` 또는 `-p` 플래그를 사용해도 가능합니다.  

```bash
gemini -p "What is fine tuning?"
```

---

## 구조화된 출력 (JSON)
스크립팅과 자동화를 위해 비대화형 모드에서 구조화된 출력을 사용할 수 있습니다.  
`--output-format json` 플래그를 이용하면 JSON 형식으로 응답을 받을 수 있습니다.

예시: JSON 출력 받기  
```bash
gemini -p "What is fine tuning?" --output-format json
```

출력 예시:
```json
{
  "response": "Fine tuning is...",
  "stats": {
    "models": { "gemini-2.5-flash": { "tokens": {"total": 45} } }
  },
  "error": null
}
```
