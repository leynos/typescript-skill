<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/experimental/Persistence` v3 → v4

- `Persistence.BackingPersistence` ->
  `effect/persistence/Persistence#BackingPersistence`: Use the v4
  BackingPersistence Context.Service class.
- `Persistence.BackingPersistenceTypeId` -> `none`: The BackingPersistence
  brand is no longer publicly exported in v4.
- `Persistence.ErrorTypeId` -> `none`: The v4 persistence error identifier is
  private; narrow with the exported error classes.
- `Persistence.PersistenceBackingError` ->
  `effect/persistence/Persistence#PersistenceError`: PersistenceError now
  represents failures from the backing persistence implementation.
- `Persistence.PersistenceError` ->
  `effect/persistence/Persistence#PersistenceError | effect/Schema#SchemaError`:
  The old combined alias was split into backing PersistenceError and schema
  SchemaError.
- `Persistence.PersistenceParseError` -> `effect/Schema#SchemaError`:
  Persistence parsing failures now use the core SchemaError type.
- `Persistence.ResultPersistence` ->
  `effect/persistence/Persistence#Persistence`: ResultPersistence was renamed
  to Persistence and is now a Context.Service class.
- `Persistence.ResultPersistence.Key` ->
  `effect/persistence/Persistable#Persistable`: Persistable is the v4
  schema-backed persistence key contract.
- `Persistence.ResultPersistence.KeyAny` ->
  `effect/persistence/Persistable#Any`: Use Persistable.Any for an arbitrary v4
  persistence key contract.
- `Persistence.ResultPersistence.TimeToLiveArgs` ->
  `Parameters<effect/persistence/Persistable#TimeToLiveFn<K>>`: Derive the
  tuple from TimeToLiveFn; its order is now exit then request.
- `Persistence.ResultPersistenceStore` ->
  `effect/persistence/Persistence#PersistenceStore`: ResultPersistenceStore was
  renamed to PersistenceStore.
- `Persistence.ResultPersistenceTypeId` -> `none`: The ResultPersistence brand
  is no longer publicly exported in v4.
- `Persistence.layerKeyValueStore` ->
  `effect/persistence/Persistence#layerBackingKvs`: The KeyValueStore backing
  layer was renamed to layerBackingKvs.
- `Persistence.layerMemory` ->
  `effect/persistence/Persistence#layerBackingMemory`: Use layerBackingMemory
  for the old backing service; v4 layerMemory creates the higher-level
  Persistence service.
- `Persistence.layerResult` -> `effect/persistence/Persistence#layer`: The
  ResultPersistence service layer was renamed to layer.
- `Persistence.layerResultKeyValueStore` ->
  `effect/persistence/Persistence#layerKvs`: The combined KeyValueStore-backed
  result layer was renamed to layerKvs.
- `Persistence.layerResultMemory` ->
  `effect/persistence/Persistence#layerMemory`: The combined memory-backed
  result layer was renamed to layerMemory.
