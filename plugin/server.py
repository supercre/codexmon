from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse
from pathlib import Path

app = FastAPI(title="Codex 플러그인")


@app.get("/", response_class=HTMLResponse)
def index():
    """플러그인과 상호 작용할 수 있는 간단한 GUI 제공"""
    html_path = Path(__file__).with_name("index.html")
    return html_path.read_text(encoding="utf-8")

@app.get("/instructions")
def get_instructions():
    """사용 방법을 반환합니다."""
    return {"instructions": ["POST /execute 엔드포인트에 'command' 문자열을 보내 Codex 동작을 실행합니다."]}

@app.post("/execute")
def execute_command(command: str = Body(..., embed=True)):
    """Codex 동작을 실행합니다."""
    # 실제 Codex 연동 부분은 추후 구현
    return {"output": f"Codex 명령 실행: {command}"}

@app.get("/legal")
def legal():
    return {"message": "사용에 따른 책임은 본인에게 있습니다."}
