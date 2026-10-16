<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/sql/SqlEventLogServer` v3 → v4

- `SqlEventLogServer.layerStorage` ->
  `effect/eventlog/SqlEventLogServerEncrypted#layerStorage`: Moved to the
  encrypted server module with the same options and EventLogEncryption
  requirement.
- `SqlEventLogServer.makeStorage` ->
  `effect/eventlog/SqlEventLogServerEncrypted#makeStorage`: Moved to the
  encrypted server module with the same SQL, encryption, and scope requirements.
