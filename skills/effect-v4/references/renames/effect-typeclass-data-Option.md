<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/typeclass/data/Option` v3 → v4

- `Option.Alternative` -> `effect/Option`: The @effect/typeclass package and
  its Option instance dictionaries were removed in v4. Use the concrete
  effect/Option operations directly.
- `Option.Applicative` -> `effect/Option`: The @effect/typeclass package and
  its Option instance dictionaries were removed in v4. Use the concrete
  effect/Option operations directly.
- `Option.Chainable` -> `effect/Option`: The @effect/typeclass package and its
  Option instance dictionaries were removed in v4. Use the concrete
  effect/Option operations directly.
- `Option.Coproduct` -> `effect/Option`: The @effect/typeclass package and its
  Option instance dictionaries were removed in v4. Use the concrete
  effect/Option operations directly.
- `Option.Covariant` -> `effect/Option`: The @effect/typeclass package and its
  Option instance dictionaries were removed in v4. Use the concrete
  effect/Option operations directly.
- `Option.Filterable` -> `effect/Option`: The @effect/typeclass package and its
  Option instance dictionaries were removed in v4. Use the concrete
  effect/Option operations directly.
- `Option.FlatMap` -> `effect/Option`: The @effect/typeclass package and its
  Option instance dictionaries were removed in v4. Use the concrete
  effect/Option operations directly.
- `Option.Foldable` -> `effect/Option`: The @effect/typeclass package and its
  Option instance dictionaries were removed in v4. Use the concrete
  effect/Option operations directly.
- `Option.Invariant` -> `effect/Option`: The @effect/typeclass package and its
  Option instance dictionaries were removed in v4. Use the concrete
  effect/Option operations directly.
- `Option.Monad` -> `effect/Option`: The @effect/typeclass package and its
  Option instance dictionaries were removed in v4. Use the concrete
  effect/Option operations directly.
- `Option.Of` -> `effect/Option`: The @effect/typeclass package and its Option
  instance dictionaries were removed in v4. Use the concrete effect/Option
  operations directly.
- `Option.Pointed` -> `effect/Option`: The @effect/typeclass package and its
  Option instance dictionaries were removed in v4. Use the concrete
  effect/Option operations directly.
- `Option.Product` -> `effect/Option`: The @effect/typeclass package and its
  Option instance dictionaries were removed in v4. Use the concrete
  effect/Option operations directly.
- `Option.SemiAlternative` -> `effect/Option`: The @effect/typeclass package
  and its Option instance dictionaries were removed in v4. Use the concrete
  effect/Option operations directly.
- `Option.SemiApplicative` -> `effect/Option`: The @effect/typeclass package
  and its Option instance dictionaries were removed in v4. Use the concrete
  effect/Option operations directly.
- `Option.SemiCoproduct` -> `effect/Option`: The @effect/typeclass package and
  its Option instance dictionaries were removed in v4. Use the concrete
  effect/Option operations directly.
- `Option.SemiProduct` -> `effect/Option`: The @effect/typeclass package and
  its Option instance dictionaries were removed in v4. Use the concrete
  effect/Option operations directly.
- `Option.Traversable` -> `effect/Option`: The @effect/typeclass package and
  its Option instance dictionaries were removed in v4. Use the concrete
  effect/Option operations directly.
- `Option.getOptionalMonoid` -> `Option.makeReducer`: Pass the replacement
  Combiner; the v4 Reducer uses None as initialValue and combines two Some
  values.
