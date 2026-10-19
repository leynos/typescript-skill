<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `effect/TSemaphore` v3 → v4

- `TSemaphore.TSemaphore` -> `TxSemaphore.TxSemaphore`: Rename the type and
  import from "effect/TxSemaphore". V4 Tx operations return ordinary Effects;
  compose multiple operations under one outer Effect.tx to keep them atomic.
- `TSemaphore.TSemaphore.Proto` -> `none`: The public prototype interface was
  removed.
- `TSemaphore.TSemaphoreTypeId` -> `TxSemaphore.isTxSemaphore`: The type id is
  internal in v4; use the public runtime guard.
- `TSemaphore.available` -> `TxSemaphore.available`: Import TxSemaphore from
  "effect/TxSemaphore"; the operation keeps its name. V4 Tx operations return
  ordinary Effects; compose multiple operations under one outer Effect.tx to
  keep them atomic.
- `TSemaphore.make` -> `TxSemaphore.make`: Import TxSemaphore from
  "effect/TxSemaphore"; the operation keeps its name. V4 Tx operations return
  ordinary Effects; compose multiple operations under one outer Effect.tx to
  keep them atomic.
- `TSemaphore.release` -> `TxSemaphore.release`: Import TxSemaphore from
  "effect/TxSemaphore"; the operation keeps its name. V4 Tx operations return
  ordinary Effects; compose multiple operations under one outer Effect.tx to
  keep them atomic.
- `TSemaphore.unsafeMake` -> `none`: The unsafe constructor was removed; use
  TxSemaphore.make.
- `TSemaphore.withPermit` -> `TxSemaphore.withPermit`: The helper remains, but
  data-first calls now pass the semaphore before the Effect.
- `TSemaphore.withPermits` -> `TxSemaphore.withPermits`: The helper remains,
  but data-first calls now pass semaphore, permit count, then Effect.
- `TSemaphore.withPermitsScoped` ->
  `TxSemaphore.acquireN + Effect.addFinalizer(TxSemaphore.releaseN)`: No scoped
  multi-permit helper remains; acquire and register release explicitly in a
  Scope.
