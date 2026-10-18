<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/opentelemetry/OtlpLogger` v3 → v4

- `OtlpLogger.layer` -> `OtlpLogger.layer`: Moved to
  effect/observability/OtlpLogger; use mergeWithExisting instead of passing
  replaceLogger.
- `OtlpLogger.make` -> `OtlpLogger.make`: The constructor remains in the module
  moved to effect/observability/OtlpLogger.
