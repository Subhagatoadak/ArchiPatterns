from fastapi import FastAPI

app = FastAPI(title="reporting-service service")


@app.get("/health")
def health() -> dict:
    return {"service": "reporting-service", "status": "ok"}
