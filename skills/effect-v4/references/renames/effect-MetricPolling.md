<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `effect/MetricPolling` v3 → v4

- `MetricPolling.MetricPolling` -> `local { metric, poll } record`: The module
  was removed. Keep a local record pairing a Metric with its polling Effect
  when this abstraction is still useful.
- `MetricPolling.MetricPollingTypeId` -> `none`: The polling wrapper and its
  brand were removed.
- `MetricPolling.collectAll` -> `Effect.forEach + Metric.update/value`: No
  combined metric replacement exists. Poll records, update each metric, and
  collect states explicitly.
- `MetricPolling.launch` -> `Effect.repeat + Effect.forkScoped`: Repeat
  polling, updating, and reading with the schedule, then forkScoped.
- `MetricPolling.make` -> `({ metric, poll })`: No public constructor remains;
  use the local record directly.
- `MetricPolling.poll` -> `self.poll`: Access the polling Effect from the local
  record.
- `MetricPolling.pollAndUpdate` ->
  `Effect.flatMap(self.poll, input => Metric.update(self.metric, input))`:
  Compose polling and metric update directly.
- `MetricPolling.retry` -> `Effect.retry`: Retry the poll Effect and retain the
  same metric in the local record.
