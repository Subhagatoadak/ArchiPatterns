# Service Mesh Template

Sidecar-based networking for mTLS, retries, timeouts, and observability between services.

## When to use
- Many services needing consistent traffic policy
- You want retries/timeouts/mTLS without duplicating code
- Standardized telemetry and zero-trust networking

## Quickstart
- Sample app: `uvicorn src.main:app --reload`
- Docker: `docker build -t service-mesh-app . && docker run -p 8000:8000 service-mesh-app`
- Compose: `docker-compose up`
- Helm: `helm upgrade --install service-mesh-app ./helm --set image.repository=your-registry/service-mesh`
- Mesh configs: start from `mesh/config` and `mesh/policies`

## Layout
- `mesh/config`: base mesh/sidecar config
- `mesh/policies`: traffic/routing/security policies
- `mesh/examples`: sample manifests with mesh annotations
- `src/main.py`: tiny FastAPI app to pair with sidecar for testing

## Use cases
Production microservices with standardized networking, mTLS by default, and enforced traffic policies.
