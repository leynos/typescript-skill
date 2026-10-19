<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/typeclass/data/Boolean` v3 → v4

- `Boolean.MonoidEqv` -> `Reducer.make(Boolean.eqv, true)`: Rebuild the removed
  instance with the v4 boolean operation and its identity.
- `Boolean.MonoidEvery` -> `Boolean.ReducerAnd`: Renamed and moved to the
  concrete v4 Boolean module.
- `Boolean.MonoidSome` -> `Boolean.ReducerOr`: Renamed and moved to the
  concrete v4 Boolean module.
- `Boolean.MonoidXor` -> `Reducer.make(Boolean.xor, false)`: Rebuild the
  removed instance with the v4 boolean operation and its identity.
- `Boolean.SemigroupEqv` -> `Combiner.make(Boolean.eqv)`: Rebuild the removed
  instance as a v4 Combiner.
- `Boolean.SemigroupEvery` -> `Boolean.ReducerAnd`: The v4 Reducer is also a
  Combiner and preserves logical-AND combine semantics.
- `Boolean.SemigroupSome` -> `Boolean.ReducerOr`: The v4 Reducer is also a
  Combiner and preserves logical-OR combine semantics.
- `Boolean.SemigroupXor` -> `Combiner.make(Boolean.xor)`: Rebuild the removed
  instance as a v4 Combiner.
