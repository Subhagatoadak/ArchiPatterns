from fastapi import FastAPI

app = FastAPI(title="mobile-frontend shell")


@app.get("/")
def index() -> dict:
    return {"frontend": "mobile", "message": "Replace with your mobile/PWA shell"}


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}
