# Serverless Web APIs (FastAPI + functions)

Function-per-endpoint/API pattern backed by an HTTP gateway; container entrypoint provided for local/dev.

## When to use
- Spiky/low-traffic workloads, POCs, internal tools
- Pay-per-use and minimal ops, but still want FastAPI DX locally
- Event-driven flows (queues, cron, webhooks) alongside HTTP routes

## Layout
- `functions/http`: FastAPI entrypoint (works with Mangum/Lambda)
- `functions/events`: event handlers/placeholders
- `infra`: IaC (SAM/CDK/Terraform) hooks
- Docker/Compose for local dev, Helm for optional containerized deploy

## Quickstart
- Local: `uvicorn functions.http.main:app --reload`
- Docker: `docker build -t serverless-web-apis . && docker run -p 8000:8000 serverless-web-apis`
- Compose: `docker-compose up`
- Helm: `helm upgrade --install serverless-web-apis ./helm --set image.repository=your-registry/serverless-web-apis`

## Use cases
Internal tools, webhooks, and bursty APIs where cold-start tradeoffs are acceptable and per-function scaling matters.
