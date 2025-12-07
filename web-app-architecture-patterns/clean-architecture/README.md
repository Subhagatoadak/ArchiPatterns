# Clean Architecture (FastAPI)

Concentric layers with clear dependency rules: entities -> use cases -> interface adapters -> frameworks/drivers.

## When to use
- Domain-heavy systems with long lifespan
- You want strict boundaries and testability without framework coupling
- Teams comfortable with explicit DTOs and adapters

## Layout
- `src/domain/entities`: enterprise rules
- `src/use_cases`: application rules
- `src/interface_adapters`: controllers/presenters/gateways
- `src/frameworks`: web/ORM/message-bus setup
- Deployment: Dockerfile, docker-compose, Helm chart

## Quickstart
- Local: `uvicorn src.main:app --reload`
- Docker: `docker build -t clean-architecture . && docker run -p 8000:8000 clean-architecture`
- Compose: `docker-compose up`
- Helm: `helm upgrade --install clean-architecture ./helm --set image.repository=your-registry/clean-architecture`

## Use cases
Complex business logic that must stay framework-agnostic (payments, risk, compliance) and applications expected to evolve over years.
