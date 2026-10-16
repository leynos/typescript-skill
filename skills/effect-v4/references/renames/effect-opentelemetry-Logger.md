<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/opentelemetry/Logger` v3 → v4

- `Logger.layerLoggerAdd` -> `OtelLogger.layer({ mergeWithExisting: true })`:
  The Logger module was renamed to OtelLogger; logger installation is now one
  configurable layer, with true preserving the v3 additive behavior.
- `Logger.layerLoggerReplace` ->
  `OtelLogger.layer({ mergeWithExisting: false })`: The Logger module was
  renamed to OtelLogger; logger installation is now one configurable layer,
  with false replacing existing loggers.
- `Logger.make` -> `OtelLogger.make`: The constructor remains in the renamed
  OtelLogger module.
