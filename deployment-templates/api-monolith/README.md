# API Monolith (FastAPI)

Single deployable serving HTTP APIs, optional web UI assets, and background jobs.

## When to use
- Early-stage product, single team, simple deployments
- Unified codebase for API + SSR/static web + jobs
- You want fast local dev with minimal infra pieces

## Layout
- `src/main.py`: FastAPI entrypoint
- `src/api`: HTTP routes/controllers
- `src/web`: place SSR templates or static assets
- `src/jobs`: background workers registration
- `infra`: add DB/cache/queue manifests as needed

## Quickstart
- Local: `uvicorn src.main:app --reload`
- Docker: `docker build -t api-monolith . && docker run -p 8000:8000 api-monolith`
- Compose: `docker-compose up` (maps 8000)
- Helm: `helm upgrade --install api-monolith ./helm --set image.repository=your-registry/api-monolith`

## Use cases
Admin consoles, internal tools, or early products where deployment speed and debugging simplicity trump strict isolation.
