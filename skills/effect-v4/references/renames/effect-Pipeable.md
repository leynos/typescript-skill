<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `effect/Pipeable` v3 → v4

- `Pipeable.PipeableConstructor` -> `Pipeable.PipeableConstructor`: Still
  exported; its rest arguments are ReadonlyArray\<any\> in v4, so make explicit
  constructor typings readonly-compatible.
