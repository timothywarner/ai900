---
applyTo: "bicep/**/*.bicep"
---

# Bicep Module Conventions

- Follow CAF naming: `{type}-{project}-{env}-{suffix}` (e.g., `cog-ai900-dev-001`)
- All modules use managed identities and RBAC -- no access keys in outputs
- Enforce TLS 1.2 minimum, disable public blob access on storage
- Tag every resource with `project`, `environment`, and `createdBy`
- Use `@secure()` decorator on all secret parameters
- Development SKUs by default (S0, Basic) with optional overrides for production
