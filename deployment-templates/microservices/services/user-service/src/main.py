from fastapi import FastAPI

app = FastAPI(title="user-service service")


@app.get("/health")
def health() -> dict:
    return {"service": "user-service", "status": "ok"}
