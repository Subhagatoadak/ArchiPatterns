from fastapi import FastAPI

app = FastAPI(title="reporting service")


@app.get("/health")
def health() -> dict:
    return {"service": "reporting", "status": "ok"}
