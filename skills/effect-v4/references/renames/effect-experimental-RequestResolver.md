<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/experimental/RequestResolver` v3 → v4

- `RequestResolver.PersistedRequest` ->
  `effect/Request#Request & effect/persistence/Persistable#Persistable`:
  Intersect a Request with Persistable or define it with Persistable.Class;
  there is no combined named export.
- `RequestResolver.PersistedRequest.Any` ->
  `effect/Request#Any & effect/persistence/Persistable#Any`: Intersect the
  Request and Persistable helper types for an arbitrary persisted request.
- `RequestResolver.dataLoader` ->
  `effect/RequestResolver#setDelay + effect/RequestResolver#batchN`: Pipe the
  resolver through setDelay(options.window) and batchN(options.maxBatchSize ??
  Infinity); the transformation is now pure.
- `RequestResolver.persisted` -> `effect/RequestResolver#persisted`: Retained
  after moving to core RequestResolver; requests now implement Persistable and
  use Persistence.Persistence, timeToLive is optional, and staleWhileRevalidate
  is supported.
