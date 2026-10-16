<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/typeclass/data/String` v3 → v4

- `String.Monoid` -> `String.ReducerConcat`: Renamed and moved to the concrete
  v4 String module.
- `String.Semigroup` -> `String.ReducerConcat`: The v4 Reducer is also a
  Combiner and preserves string concatenation.
