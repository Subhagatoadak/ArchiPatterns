from fastapi import FastAPI, WebSocket

app = FastAPI(title="WebSockets/SSE")


@app.websocket("/ws")
async def websocket_endpoint(socket: WebSocket):
    await socket.accept()
    await socket.send_json({"message": "connected"})
    await socket.close()


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}
