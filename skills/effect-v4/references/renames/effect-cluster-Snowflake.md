<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/cluster/Snowflake` v3 → v4

- `Snowflake.Generator` -> `effect/cluster/Snowflake#Generator`: Moved into
  core Effect and changed to Context.Service; its unsafeNext method was renamed
  to nextUnsafe.
- `Snowflake.TypeId` -> `effect/cluster/Snowflake#TypeId`: Moved into core
  Effect; the public marker is now the string literal
  \~effect/cluster/Snowflake.
