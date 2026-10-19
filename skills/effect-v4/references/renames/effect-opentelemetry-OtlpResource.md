<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/opentelemetry/OtlpResource` v3 → v4

- `OtlpResource.make` -> `OtlpResource.make`: The constructor remains in the
  module moved to effect/observability/OtlpResource.
- `OtlpResource.unsafeServiceName` -> `OtlpResource.serviceNameUnsafe`: Moved
  to effect/observability/OtlpResource and renamed to follow the v4
  unsafe-suffix convention.
