<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/platform/WorkerError` v3 → v4

- `WorkerError.WorkerErrorFrom` -> `WorkerError.WorkerError`: The old
  serializable reason object was replaced by WorkerError wrapping dedicated
  spawn, send, receive, or unknown reason classes.
- `WorkerError.WorkerErrorTypeId` -> `WorkerError.TypeId`: The type-level
  worker error marker was shortened to TypeId in the moved module.
