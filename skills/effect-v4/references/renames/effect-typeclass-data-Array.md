<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/typeclass/data/Array` v3 → v4

- `Array.Applicative` -> `effect/Array`: The @effect/typeclass package and its
  Array instance dictionaries were removed in v4. Use the concrete effect/Array
  operations directly.
- `Array.Chainable` -> `effect/Array`: The @effect/typeclass package and its
  Array instance dictionaries were removed in v4. Use the concrete effect/Array
  operations directly.
- `Array.Covariant` -> `effect/Array`: The @effect/typeclass package and its
  Array instance dictionaries were removed in v4. Use the concrete effect/Array
  operations directly.
- `Array.Filterable` -> `effect/Array`: The @effect/typeclass package and its
  Array instance dictionaries were removed in v4. Use the concrete effect/Array
  operations directly.
- `Array.FlatMap` -> `effect/Array`: The @effect/typeclass package and its
  Array instance dictionaries were removed in v4. Use the concrete effect/Array
  operations directly.
- `Array.Foldable` -> `effect/Array`: The @effect/typeclass package and its
  Array instance dictionaries were removed in v4. Use the concrete effect/Array
  operations directly.
- `Array.Invariant` -> `effect/Array`: The @effect/typeclass package and its
  Array instance dictionaries were removed in v4. Use the concrete effect/Array
  operations directly.
- `Array.Monad` -> `effect/Array`: The @effect/typeclass package and its Array
  instance dictionaries were removed in v4. Use the concrete effect/Array
  operations directly.
- `Array.Of` -> `effect/Array`: The @effect/typeclass package and its Array
  instance dictionaries were removed in v4. Use the concrete effect/Array
  operations directly.
- `Array.Pointed` -> `effect/Array`: The @effect/typeclass package and its
  Array instance dictionaries were removed in v4. Use the concrete effect/Array
  operations directly.
- `Array.Product` -> `effect/Array`: The @effect/typeclass package and its
  Array instance dictionaries were removed in v4. Use the concrete effect/Array
  operations directly.
- `Array.SemiApplicative` -> `effect/Array`: The @effect/typeclass package and
  its Array instance dictionaries were removed in v4. Use the concrete
  effect/Array operations directly.
- `Array.SemiProduct` -> `effect/Array`: The @effect/typeclass package and its
  Array instance dictionaries were removed in v4. Use the concrete effect/Array
  operations directly.
- `Array.Traversable` -> `effect/Array`: The @effect/typeclass package and its
  Array instance dictionaries were removed in v4. Use the concrete effect/Array
  operations directly.
- `Array.TraversableFilterable` -> `effect/Array`: The @effect/typeclass
  package and its Array instance dictionaries were removed in v4. Use the
  concrete effect/Array operations directly.
- `Array.getMonoid` -> `Array.makeReducerConcat`: Use the v4 concatenation
  Reducer; Reducer replaces Monoid.
- `Array.getSemigroup` -> `Array.makeReducerConcat`: The v4 concatenation
  Reducer is also a Combiner and replaces this Semigroup.
