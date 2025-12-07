from fastapi import FastAPI

app = FastAPI(title="API Gateway Stub")


@app.get("/health")
def health() -> dict:
    return {"status": "ok", "gateway": True}


@app.get("/proxy")
def proxy_example() -> dict:
    return {"message": "route to internal services from here"}
