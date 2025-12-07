from fastapi import FastAPI

app = FastAPI(title="api-gateway service")


@app.get("/health")
def health() -> dict:
    return {"service": "api-gateway", "status": "ok"}
