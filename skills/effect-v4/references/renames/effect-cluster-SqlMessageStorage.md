<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/cluster/SqlMessageStorage` v3 → v4

- `SqlMessageStorage.layer` -> `effect/cluster/SqlMessageStorage#layer`: Moved
  into core Effect. V4 adds a Crypto.Crypto requirement for hashing long
  deduplication keys.
- `SqlMessageStorage.layerWith` ->
  `effect/cluster/SqlMessageStorage#layerWith`: Moved into core Effect with the
  same optional table prefix; v4 additionally requires Crypto.Crypto.
- `SqlMessageStorage.make` -> `effect/cluster/SqlMessageStorage#make`: Moved
  into core Effect with the same prefix option; v4 additionally requires
  Crypto.Crypto.
