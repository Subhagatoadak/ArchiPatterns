from fastapi import FastAPI

app = FastAPI(title="Service Mesh Demo App")


@app.get("/health")
def health() -> dict:
    return {"status": "ok", "mesh": "configure mTLS/retries in mesh"}
