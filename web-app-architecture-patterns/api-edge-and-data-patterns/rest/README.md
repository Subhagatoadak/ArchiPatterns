# RESTful API Template (FastAPI)

Resource-oriented HTTP API with conventional verbs/status codes.

## When to use
- Standard CRUD/business APIs for browsers/mobile
- Backends that benefit from caching, proxies, and clear versioning
- Teams aligned on HTTP semantics and OpenAPI contracts

## Quickstart
- Local: `uvicorn src.main:app --reload`
- Docker: `docker build -t rest-api . && docker run -p 8000:8000 rest-api`
- Compose: `docker-compose up`
- Helm: `helm upgrade --install rest-api ./helm --set image.repository=your-registry/rest`

## Layout
- `src/routes`: route definitions & versioning
- `src/controllers`: handlers mapping to use cases
- `src/middleware`: auth/validation/caching hooks

## Use cases
Public/private REST APIs, integrations with API gateways, and clients needing stable resource contracts.
