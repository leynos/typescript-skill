<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/sql/SqlEventJournal` v3 → v4

- `SqlEventJournal.layer` -> `effect/eventlog/SqlEventJournal#layer`: Moved;
  rename the eventLogTable layer option to entryTable.
- `SqlEventJournal.make` -> `effect/eventlog/SqlEventJournal#make`: Moved with
  the same entryTable and remotesTable options.
