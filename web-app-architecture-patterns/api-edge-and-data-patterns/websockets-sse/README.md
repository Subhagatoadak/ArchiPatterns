# WebSockets / SSE Template (FastAPI)

Real-time push endpoints for notifications, dashboards, and collaboration.

## When to use
- Live updates with many concurrent connections
- Dashboards, chat, collaboration, presence
- Need graceful fallback to polling when websockets are blocked

## Quickstart
- Local: `uvicorn src.main:app --reload`
- Docker: `docker build -t websockets-sse . && docker run -p 8000:8000 websockets-sse`
- Compose: `docker-compose up`
- Helm: `helm upgrade --install websockets-sse ./helm --set image.repository=your-registry/websockets-sse`

## Layout
- `src/http`: upgrade endpoints/HTTP handlers
- `src/realtime`: socket/SSE handlers
- `src/subscriptions`: pub/sub wiring

## Use cases
Real-time features layered next to your REST/GraphQL APIs, scaling via Redis/pubsub fan-out.
