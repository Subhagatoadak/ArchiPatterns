# Real-Time + Rich Frontend

Support live updates with WebSockets/SSE alongside REST/GraphQL. Use BFFs to tailor payloads and keep stateful connections close to clients.

## Suggested stack
- Deploy: microservices or monolith with realtime node
- Internals: clean/hexagonal; CQRS projections for dashboards
- Edge: REST/GraphQL + WebSockets/SSE; BFF per client
- Data: outbox + event streaming for fan-out

## Layout hint
- Combine `../../bff-and-micro-frontends` with `../../microservices` or `../../api-monolith` depending on scale.
