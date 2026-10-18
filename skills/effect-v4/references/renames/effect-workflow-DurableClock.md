<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/workflow/DurableClock` v3 → v4

- `DurableClock.TypeId` -> `none`: The durable-clock marker is private in v4.
  Use DurableClock values structurally.
- `DurableClock.make` -> `effect/workflow/DurableClock#make`: Moved into core
  Effect; Duration.DurationInput is now Duration.Input.
