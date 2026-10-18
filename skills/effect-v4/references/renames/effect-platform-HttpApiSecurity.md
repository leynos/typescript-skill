<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/platform/HttpApiSecurity` v3 → v4

- `HttpApiSecurity.Bearer` -> `effect/http-api/HttpApiSecurity#Http`: Bearer
  was generalized to Http with scheme Bearer; the value-level bearer singleton
  remains.
- `HttpApiSecurity.TypeId` -> `none`: The marker is private; use the public
  union or specific Http, ApiKey, and Basic types.
- `HttpApiSecurity.annotate` -> `effect/http-api/HttpApiSecurity#annotate`: The
  combinator remains; its key is now the v4 Context.Key abstraction.
- `HttpApiSecurity.annotateContext` ->
  `effect/http-api/HttpApiSecurity#annotateMerge`: Renamed; it still merges a
  Context into existing OpenAPI annotations.
