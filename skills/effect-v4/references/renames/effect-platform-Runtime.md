<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/platform/Runtime` v3 → v4

- `Runtime.RunMain` -> `ReturnType<typeof Runtime.makeRunMain>`: The standalone
  interface was removed; derive the runner type from
  effect/Runtime.makeRunMain. disablePrettyLogger is no longer an option.
