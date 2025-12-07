# Growing Product (Multiple Teams)

Split into mini-services or microservices with an API Gateway. Use hexagonal/clean inside each service and move critical domains to CQRS as needed.

## Suggested stack
- Deploy: service-based or microservices + gateway
- Internals: hexagonal/clean per service
- Edge: REST or GraphQL; add service mesh for retries/mTLS
- Data: outbox per service, CQRS for hot paths

## Layout hint
- Use `../../service-based` or `../../microservices`; add contract tests between services and gateway.
