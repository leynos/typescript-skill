<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/ai/IdGenerator` v3 → v4

- `IdGenerator.make` -> `IdGenerator.make`: Moved to effect/ai/IdGenerator with
  the same configurable alphabet, prefix, separator, and size behavior. Invalid
  configuration now fails with Cause.IllegalArgumentError.
