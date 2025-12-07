from fastapi import FastAPI

app = FastAPI(title="web-api service")


@app.get("/health")
def health() -> dict:
    return {"service": "web-api", "status": "ok"}
