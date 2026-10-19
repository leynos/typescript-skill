<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/experimental/DevTools/Domain` v3 → v4

- `Domain.ExternalSpanFrom` ->
  `effect/Schema#Codec.Encoded<typeof effect/devtools/DevToolsSchema#ExternalSpan>`:
  The named encoded alias was removed; derive it with Schema.Codec.Encoded
  from ExternalSpan.
- `Domain.MetricFrom` ->
  `effect/Schema#Codec.Encoded<typeof effect/devtools/DevToolsSchema#Metric>`:
  The named encoded alias was removed; derive it with Schema.Codec.Encoded from
  Metric.
- `Domain.MetricsSnapshotFrom` ->
  `effect/Schema#Codec.Encoded<typeof effect/devtools/DevToolsSchema#MetricsSnapshot>`:
  The named encoded alias was removed; derive it with Schema.Codec.Encoded
  from MetricsSnapshot.
- `Domain.ParentSpanFrom` ->
  `effect/Schema#Codec.Encoded<typeof effect/devtools/DevToolsSchema#ParentSpan>`:
  The named encoded alias was removed; derive it with Schema.Codec.Encoded
  from ParentSpan.
- `Domain.SpanFrom` ->
  `effect/Schema#Codec.Encoded<typeof effect/devtools/DevToolsSchema#Span>`:
  The named encoded alias was removed; derive it with Schema.Codec.Encoded from
  Span.
- `Domain.metric` -> `none`: The metric schema helper is private in v4; use the
  exported Counter, Frequency, Gauge, Histogram, Summary, or Metric schemas, or
  build a Schema.Struct.
