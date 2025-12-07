from fastapi import FastAPI

app = FastAPI(title="web-frontend shell")


@app.get("/")
def index() -> dict:
    return {"frontend": "web", "message": "Replace with your SPA/SSR app"}


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}
