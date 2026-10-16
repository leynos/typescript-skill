<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `effect/Iterable` v3 → v4

- `Iterable.flatMapNullable` -> `Iterable.flatMapNullishOr`: Direct
  nullish-terminology rename; it remains lazy and drops null or undefined
  mapper results.
- `Iterable.getLefts` -> `Iterable.getFailures`: Either became Result; this
  lazily extracts failure payloads.
- `Iterable.getRights` -> `Iterable.getSuccesses`: Either became Result; this
  lazily extracts success payloads.
- `Iterable.unsafeHead` -> `Iterable.headUnsafe`: Direct word-order rename; it
  still throws on an empty Iterable.
