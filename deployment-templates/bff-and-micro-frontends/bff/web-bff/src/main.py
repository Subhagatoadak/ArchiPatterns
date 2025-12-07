from fastapi import FastAPI

app = FastAPI(title="web-bff")


@app.get("/health")
def health() -> dict:
    return {"service": "web-bff", "status": "ok"}
