from fastapi import FastAPI

app = FastAPI(title="gRPC-friendly API")


@app.get("/health")
def health() -> dict:
    return {"status": "ok", "grpc": "add gRPC server alongside FastAPI"}
