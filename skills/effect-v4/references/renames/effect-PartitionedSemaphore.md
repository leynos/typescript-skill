<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `effect/PartitionedSemaphore` v3 → v4

- `PartitionedSemaphore.PartitionedSemaphore` ->
  `PartitionedSemaphore.PartitionedSemaphore`: The model remains and now also
  exposes capacity, available, take, release, withPermit, and conditional
  permit operations.
- `PartitionedSemaphore.TypeId` -> `PartitionedSemaphore.PartitionedTypeId`:
  The public type id was renamed to distinguish it from the regular Semaphore
  type id.
