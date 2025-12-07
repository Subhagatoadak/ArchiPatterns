# BFF & Micro Frontends (FastAPI BFFs + frontend shells)

Client-specific backends paired with thin frontends. Ships two FastAPI BFFs, shared APIs, and placeholder web/mobile frontend shells.

## When to use
- Distinct client needs (web vs mobile) needing tailored APIs
- Teams own vertical slices (frontend + BFF) with independent deploys
- Need edge composition for micro frontends

## Layout
- `bff/web-bff`, `bff/mobile-bff`: FastAPI BFFs
- `services/shared-apis`: shared backend surface
- `frontends/web`, `frontends/mobile`: placeholder shells (swap with SPA/SSR builds)
- Root `docker-compose.yml`: runs BFFs + frontends locally
- Helm chart `helm/`: deploys all components from `values.yaml`

## Quickstart
- Local stack: `docker-compose up`
- Per-service: `cd bff/web-bff && docker-compose up`
- Helm: `helm upgrade --install bff-stack ./helm --set services[0].image=...`

## Use cases
Products with multiple clients needing differentiated payloads, or organizations aligning teams by vertical slices with independent delivery.
