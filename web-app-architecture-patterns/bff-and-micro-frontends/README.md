# BFF & Micro Frontends Template

Client-specific backends (BFFs) paired with vertically sliced frontends. Good for multi-client products and team-aligned ownership.

## Layout
- bff/web-bff: web-specific API aggregation, session management
- bff/mobile-bff: mobile-friendly APIs, pagination/payload tuning
- frontends/web: web SPA/SSR shell + feature modules
- frontends/mobile: mobile app shell or PWA modules
- services/shared-apis: shared backend services consumed by BFFs
- ops: gateway/edge configs, CI/CD, contract tests between BFFs and services

## Notes
- Keep contracts explicit (OpenAPI/GraphQL schema) between BFFs and frontends.
- Favor independent deploys per slice; use composition at the edge for micro frontends.
