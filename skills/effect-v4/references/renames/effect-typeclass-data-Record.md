<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/typeclass/data/Record` v3 → v4

- `Record.Covariant` -> `effect/Record`: The @effect/typeclass package and its
  Record instance dictionaries were removed in v4. Use the concrete
  effect/Record operations directly.
- `Record.Filterable` -> `effect/Record`: The @effect/typeclass package and its
  Record instance dictionaries were removed in v4. Use the concrete
  effect/Record operations directly.
- `Record.Invariant` -> `effect/Record`: The @effect/typeclass package and its
  Record instance dictionaries were removed in v4. Use the concrete
  effect/Record operations directly.
- `Record.Traversable` -> `effect/Record`: The @effect/typeclass package and
  its Record instance dictionaries were removed in v4. Use the concrete
  effect/Record operations directly.
- `Record.TraversableFilterable` -> `effect/Record`: The @effect/typeclass
  package and its Record instance dictionaries were removed in v4. Use the
  concrete effect/Record operations directly.
- `Record.getCovariant` -> `effect/Record`: The @effect/typeclass package and
  its Record instance dictionaries were removed in v4. Use the concrete
  effect/Record operations directly.
- `Record.getFilterable` -> `effect/Record`: The @effect/typeclass package and
  its Record instance dictionaries were removed in v4. Use the concrete
  effect/Record operations directly.
- `Record.getInvariant` -> `effect/Record`: The @effect/typeclass package and
  its Record instance dictionaries were removed in v4. Use the concrete
  effect/Record operations directly.
- `Record.getMonoidUnion` -> `Record.makeReducerUnion`: Pass the replacement
  value Combiner; the v4 Reducer uses an empty record as initialValue.
- `Record.getSemigroupIntersection` -> `Record.makeReducerIntersection`: Pass
  the replacement value Combiner and use the returned Reducer's combine
  operation for pairwise intersection.
- `Record.getSemigroupUnion` -> `Record.makeReducerUnion`: The v4 Reducer is
  also a Combiner and preserves pairwise union semantics.
- `Record.getTraversable` -> `effect/Record`: The @effect/typeclass package and
  its Record instance dictionaries were removed in v4. Use the concrete
  effect/Record operations directly.
- `Record.getTraversableFilterable` -> `effect/Record`: The @effect/typeclass
  package and its Record instance dictionaries were removed in v4. Use the
  concrete effect/Record operations directly.
