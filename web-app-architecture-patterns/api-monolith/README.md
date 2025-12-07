# API Monolith Template

Single deployable that ships API, web UI, and background jobs together. Start here for a single team or early-stage product.

## Layout
- src/api: HTTP controllers/routes (REST/GraphQL/gRPC)
- src/web: SSR/static assets or SPA bundler output
- src/jobs: background workers / schedulers
- infra: docker-compose, DB migrations, cache/queue config

## Notes
- Keep domain boundaries inside `src` with clear modules to avoid sprawl.
- Shared DTOs/contracts live in `src/api` and are reused by jobs.
- Add an API gateway later only if clients proliferate.
