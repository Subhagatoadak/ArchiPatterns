from fastapi import FastAPI

app = FastAPI(title="shared-apis")


@app.get("/health")
def health() -> dict:
    return {"service": "shared-apis", "status": "ok"}
