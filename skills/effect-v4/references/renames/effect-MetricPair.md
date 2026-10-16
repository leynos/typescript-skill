<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `effect/MetricPair` v3 → v4

- `MetricPair.MetricPair` -> `Metric.Metric.Snapshot`: Registry key/state pairs
  became discriminated snapshots containing id, type, description, attributes,
  and state.
- `MetricPair.MetricPair.Untyped` -> `Metric.Metric.Snapshot`: Registry
  key/state pairs became discriminated snapshots containing id, type,
  description, attributes, and state.
- `MetricPair.MetricPair.Variance` -> `none`: Snapshots are structural, so the
  pair variance helper and brand symbol were removed.
- `MetricPair.MetricPairTypeId` -> `none`: Snapshots are structural, so the
  pair variance helper and brand symbol were removed.
- `MetricPair.make` -> `Metric.snapshot`: There is no pair constructor. Obtain
  snapshots with Metric.snapshot or Metric.snapshotUnsafe; manually constructed
  data can satisfy Metric.Metric.SnapshotProto.
- `MetricPair.unsafeMake` -> `Metric.snapshot`: There is no pair constructor.
  Obtain snapshots with Metric.snapshot or Metric.snapshotUnsafe; manually
  constructed data can satisfy Metric.Metric.SnapshotProto.
