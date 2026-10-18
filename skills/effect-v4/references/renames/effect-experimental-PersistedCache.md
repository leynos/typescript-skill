<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/experimental/PersistedCache` v3 → v4

- `PersistedCache.make` -> `effect/persistence/PersistedCache#make`: Pass
  lookup as the first argument and options second; timeToLive now receives exit
  before request and the service is Persistence.Persistence.
