# API Gateway Template (FastAPI stub)

Single entry point for routing, auth, rate limiting, logging, and protocol translation.

## When to use
- Multiple downstream services needing unified edge policies
- Protocol bridging (REST ↔ gRPC), request shaping, or aggregation
- Centralized observability and security controls

## Quickstart
- Local: `uvicorn src.main:app --reload`
- Docker: `docker build -t api-gateway . && docker run -p 8000:8000 api-gateway`
- Compose: `docker-compose up`
- Helm: `helm upgrade --install api-gateway ./helm --set image.repository=your-registry/api-gateway`

## Layout
- `gateway/routes|plugins|policies`: config stubs for routing and edge rules
- `src/main.py`: FastAPI placeholder (swap with Kong/Traefik/Envoy config if preferred)

## Use cases
Edge entrypoint in front of microservices/BFFs, enforcing auth/rate limits and handling versioning/routing concerns.
