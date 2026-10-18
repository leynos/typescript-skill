<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `effect/MetricKey` v3 → v4

- `MetricKey.MetricKey` -> `Metric.Metric`: Key identity, metadata, and
  operations are combined in Metric\<Input, State\>.
- `MetricKey.MetricKey.Untyped` -> `Metric.Metric<any, any>`: The separate
  untyped key alias was removed; use an untyped complete Metric only where
  required.
- `MetricKey.MetricKey.Variance` -> `Metric.Metric`: There is no separate key
  variance interface; variance is carried by Metric's Input and State phantom
  fields.
- `MetricKey.MetricKeyTypeId` -> `none`: The key brand was removed; Metric's
  protocol key is internal.
- `MetricKey.counter` -> `Metric.counter`: The key and key type were merged
  into the complete Metric.counter constructor.
- `MetricKey.frequency` -> `Metric.frequency`: The key and key type were merged
  into the complete Metric.frequency constructor.
- `MetricKey.gauge` -> `Metric.gauge`: The key and key type were merged into
  the complete Metric.gauge constructor.
- `MetricKey.histogram` -> `Metric.histogram`: The key and key type were merged
  into the complete Metric.histogram constructor.
- `MetricKey.isMetricKey` -> `Metric.isMetric`: Keys became complete metrics;
  use the complete-metric runtime guard.
- `MetricKey.summary` -> `Metric.summary`: The key and key type were merged
  into the complete Metric.summary constructor.
- `MetricKey.taggedWithLabels` -> `Metric.withAttributes`: Labels became
  attributes. Pass a string record or array of string tuples.
