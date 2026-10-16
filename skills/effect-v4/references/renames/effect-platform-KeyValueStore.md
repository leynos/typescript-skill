<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/platform/KeyValueStore` v3 → v4

- `KeyValueStore.KeyValueStore` -> `KeyValueStore.KeyValueStore`: The service
  moved to effect/persistence/KeyValueStore; missing values now use undefined
  and operations fail with KeyValueStoreError.
- `KeyValueStore.KeyValueStore.AnyStore` ->
  `KeyValueStore.KeyValueStore | KeyValueStore.SchemaStore<Schema.Constraint>`:
  The convenience namespace alias was removed; write the store union explicitly
  when needed.
- `KeyValueStore.SchemaStoreTypeId` -> `none`: The v4 SchemaStore has no public
  type-id alias; use the SchemaStore interface.
- `KeyValueStore.TypeId` -> `none`: The KeyValueStore runtime marker is
  internal in v4; use the service and interface.
- `KeyValueStore.layerSchema` -> `KeyValueStore.toSchemaStore`: Schema stores
  are now derived with toSchemaStore; define the desired Context.Service and
  layer explicitly.
- `KeyValueStore.make` -> `KeyValueStore.make`: The constructor remains in the
  moved module with v4 MakeOptions.
- `KeyValueStore.prefix` -> `KeyValueStore.prefix`: The prefixed-store
  combinator remains in the moved module.
