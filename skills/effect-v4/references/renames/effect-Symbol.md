<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `effect/Symbol` v3 → v4

- `Symbol.Equivalence` -> `Equivalence.strictEqual<symbol>()`: The dedicated
  symbol instance was removed; it used strict equality.
