<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `effect/MetricBoundaries` v3 → v4

- `MetricBoundaries.MetricBoundaries` -> `ReadonlyArray<number>`: The wrapper
  was removed; Metric.histogram accepts plain boundaries in its options.
- `MetricBoundaries.MetricBoundariesTypeId` -> `none`: Boundaries are unbranded
  arrays, so the guard and public type-id symbol have no replacement.
- `MetricBoundaries.exponential` -> `Metric.exponentialBoundaries`: Moved into
  effect/Metric and now returns ReadonlyArray\<number\>. V4 also filters
  non-positive boundaries.
- `MetricBoundaries.fromIterable` -> `Metric.boundariesFromIterable`: Moved
  into effect/Metric and now returns an unbranded ReadonlyArray\<number\>; v4
  removes non-positive values before appending Infinity.
- `MetricBoundaries.isMetricBoundaries` -> `none`: Boundaries are unbranded
  arrays, so the guard and public type-id symbol have no replacement.
- `MetricBoundaries.linear` -> `Metric.linearBoundaries`: Moved into
  effect/Metric and now returns ReadonlyArray\<number\>. The v4 implementation
  keeps the v3 formula start + i \* width for i below count - 1, filters
  non-positive values, and appends Infinity.
