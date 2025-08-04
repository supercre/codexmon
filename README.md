# Codex 플러그인 예제

이 저장소는 OpenAPI로 구축된 간단한 ChatGPT 플러그인 예제입니다. 플러그인은 기본적인 Codex 명령을 실행할 수 있는 몇 가지 엔드포인트를 제공합니다.

## 파일 구성

- `plugin/server.py` – 플러그인 API를 구현한 FastAPI 애플리케이션
- `plugin/openapi.yaml` – 엔드포인트를 설명하는 OpenAPI 스펙
- `plugin/ai-plugin.json` – ChatGPT에서 사용하는 플러그인 매니페스트
- `plugin/index.html` – 플러그인과 상호 작용할 수 있는 간단한 웹 인터페이스

## 실행 방법

1. 의존성 설치

```bash
pip install fastapi uvicorn
```

2. 서버 실행

```bash
uvicorn plugin.server:app --reload
```

API는 `http://localhost:8000` 에서 제공되며 OpenAPI 문서는 `http://localhost:8000/openapi.yaml` 에서 확인할 수 있습니다.

3. 브라우저에서 `http://localhost:8000/` 주소로 접속해 GUI를 확인합니다.

ChatGPT에서 플러그인을 설정할 때 `plugin/ai-plugin.json` 파일을 사용하세요.
