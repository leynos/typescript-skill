<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/typeclass/Monoid` v3 → v4

- `Monoid.Monoid` -> `Reducer.Reducer`: Reducer replaces Monoid in v4; empty is
  renamed initialValue and combineAll remains available.
- `Monoid.array` -> `Array.makeReducerConcat`: Use the v4 array concatenation
  Reducer; Reducer replaces Monoid and names the identity initialValue.
- `Monoid.fromSemigroup` -> `Reducer.make(S.combine, empty)`: Construct a v4
  Reducer from the replacement Combiner operation and identity value.
- `Monoid.max` -> `Reducer.make(Combiner.max(B.compare).combine, B.minBound)`:
  Reducer replaces Monoid. Build it from the v4 maximum Combiner and the
  bounded order's minimum value.
- `Monoid.min` -> `Reducer.make(Combiner.min(B.compare).combine, B.maxBound)`:
  Reducer replaces Monoid. Build it from the v4 minimum Combiner and the
  bounded order's maximum value.
- `Monoid.reverse` -> `Reducer.flip`: Use the v4 Reducer combinator; it
  preserves initialValue and reverses combine argument order.
- `Monoid.struct` -> `Struct.makeReducer`: Pass a record of v4 Reducers to
  derive a field-wise Reducer.
- `Monoid.tuple` -> `Tuple.makeReducer`: Pass one array of v4 Reducers instead
  of rest Monoid arguments.
