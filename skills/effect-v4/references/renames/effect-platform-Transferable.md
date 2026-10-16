<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/platform/Transferable` v3 → v4

- `Transferable.CollectorService` -> `Transferable.Collector["Service"]`: The
  collector interface is now the service type of the Transferable.Collector
  Context.Service class.
- `Transferable.Uint8Array` -> `Transferable.Uint8Array`: The transferable
  Uint8Array schema remains in the moved module.
- `Transferable.schema` -> `Transferable.schema`: The schema wrapper moved to
  effect/workers/Transferable and uses the v4 Schema model.
- `Transferable.unsafeMakeCollector` -> `Transferable.makeCollectorUnsafe`: The
  unsafe collector constructor was renamed.
