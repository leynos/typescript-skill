<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/experimental/EventLog` v3 → v4

- `EventLog.Handlers` -> `effect/eventlog/EventLog#Handlers`: Import Handlers
  from the v4 EventLog module; handlers now also receive storeId.
- `EventLog.HandlersTypeId` -> `effect/eventlog/EventLog#HandlersTypeId`:
  Import HandlersTypeId from the v4 EventLog module.
- `EventLog.SchemaTypeId` -> `effect/eventlog/EventLog#SchemaTypeId`: Import
  SchemaTypeId from the v4 EventLog module.
- `EventLog.group` -> `effect/eventlog/EventLog#group`: Import group from the
  v4 EventLog module; it now requires the shared Registry service.
- `EventLog.layer` -> `effect/eventlog/EventLog#layer`: The v4 layer takes both
  the schema and handler layer; use layerEventLog for runtime only.
- `EventLog.layerIdentityKvs` -> `none`: Compose KeyValueStore.toSchemaStore,
  EventLog.IdentitySchema, EventLog.makeIdentity, and Layer.effect manually.
