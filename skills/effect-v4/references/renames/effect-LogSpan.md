<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `effect/LogSpan` v3 → v4

- `LogSpan.LogSpan` -> `readonly [label: string, timestamp: number]`: The
  module was removed. Active log spans are tuples in
  References.CurrentLogSpans; ordinary callers should prefer Effect.withLogSpan.
- `LogSpan.make` -> `[label, startTime] as const`: Construct the tuple
  directly, or use Effect.withLogSpan so Effect obtains the timestamp and
  scopes the span.
- `LogSpan.render` -> `custom tuple formatter`: No public standalone renderer
  remains. Built-in loggers format span tuples internally; custom formatters
  can render label and elapsed milliseconds themselves.
