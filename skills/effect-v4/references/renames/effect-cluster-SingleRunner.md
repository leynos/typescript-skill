<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/cluster/SingleRunner` v3 → v4

- `SingleRunner.layer` -> `effect/cluster/SingleRunner#layer`: Moved into core
  Effect. V4 additionally requires Crypto.Crypto because SQL message storage
  hashes long deduplication keys.
