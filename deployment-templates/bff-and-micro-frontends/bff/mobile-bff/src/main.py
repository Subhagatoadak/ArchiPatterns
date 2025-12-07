from fastapi import FastAPI

app = FastAPI(title="mobile-bff")


@app.get("/health")
def health() -> dict:
    return {"service": "mobile-bff", "status": "ok"}
