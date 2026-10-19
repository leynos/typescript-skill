<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/workflow/DurableQueue` v3 → v4

- `DurableQueue.TypeId` -> `effect/workflow/DurableQueue#TypeId`: Moved into
  core Effect; the marker literal changed to \~effect/workflow/DurableQueue.
  Use typeof DurableQueue.TypeId in type position.
- `DurableQueue.make` -> `effect/workflow/DurableQueue#make`: Moved into core
  Effect; queue persistence now comes from effect/persistence.
