<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `effect/MetricRegistry` v3 → v4

- `MetricRegistry.MetricRegistry` -> `Metric.MetricRegistry`: The
  method-bearing registry became a Context.Reference whose service is a Map.
  Metrics register metadata and hooks lazily.
- `MetricRegistry.MetricRegistryTypeId` -> `none`: The registry service is an
  ordinary Map behind a Context.Reference and has no public brand.
- `MetricRegistry.make` ->
  `new Map<string, Metric.Metric.Metadata<any, any>>()`: Provide a fresh Map to
  Metric.MetricRegistry for isolation. Read it through Metric.snapshot or
  snapshotUnsafe.
