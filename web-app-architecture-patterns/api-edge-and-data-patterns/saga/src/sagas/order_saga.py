def execute_order_saga() -> dict:
    steps = ["reserve", "charge", "notify"]
    return {"saga": "order", "steps": steps, "status": "completed"}
