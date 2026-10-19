<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/experimental/EventJournal` v3 → v4

- `EventJournal.EntryIdTypeId` -> `effect/eventlog/EventJournal#EntryIdTypeId`:
  Import EntryIdTypeId from the v4 EventJournal module; it is now a string
  brand.
- `EventJournal.ErrorTypeId` -> `none`: The v4 error marker is private; narrow
  with EventJournalError instead.
- `EventJournal.RemoteIdTypeId` ->
  `effect/eventlog/EventJournal#RemoteIdTypeId`: Import RemoteIdTypeId from the
  v4 EventJournal module; it is now a string brand.
- `EventJournal.makeEntryId` ->
  `effect/eventlog/EventJournal#makeEntryIdUnsafe`: The unchecked EntryId
  constructor was renamed to makeEntryIdUnsafe.
- `EventJournal.makeMemory` -> `effect/eventlog/EventJournal#makeMemory`: The
  in-memory constructor moved into core Effect and now returns the
  Context.Service implementation through its Service projection.
- `EventJournal.makeRemoteId` ->
  `effect/eventlog/EventJournal#makeRemoteIdUnsafe`: The unchecked RemoteId
  constructor was renamed to makeRemoteIdUnsafe.
