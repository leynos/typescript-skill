<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `effect/GlobalValue` v3 → v4

- `GlobalValue.globalValue` -> `module-scoped const`: The global registry
  helper was removed; use a module singleton, or explicitly own a globalThis
  and Symbol.for registry when cross-bundle identity is required.
