<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `effect/MetricLabel` v3 → v4

- `MetricLabel.MetricLabel` -> `[string, string]`: A label is now an ordinary
  attribute tuple; collections are Metric.Metric.Attributes or
  Metric.Metric.AttributeSet.
- `MetricLabel.MetricLabelTypeId` -> `none`: Attributes are plain tuples or
  records, so there is no branded guard or type-id symbol.
- `MetricLabel.isMetricLabel` -> `none`: Attributes are plain tuples or
  records, so there is no branded guard or type-id symbol.
- `MetricLabel.make` -> `[key, value]`: Construct an ordinary tuple, or place
  the pair in an attribute record passed to Metric.withAttributes or a metric
  constructor.
