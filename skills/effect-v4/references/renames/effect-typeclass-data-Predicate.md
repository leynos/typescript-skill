<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/typeclass/data/Predicate` v3 → v4

- `Predicate.Contravariant` -> `effect/Predicate`: The @effect/typeclass
  package and its Predicate instance dictionaries were removed in v4. Use the
  concrete effect/Predicate operations directly.
- `Predicate.Invariant` -> `effect/Predicate`: The @effect/typeclass package
  and its Predicate instance dictionaries were removed in v4. Use the concrete
  effect/Predicate operations directly.
- `Predicate.Of` -> `effect/Predicate`: The @effect/typeclass package and its
  Predicate instance dictionaries were removed in v4. Use the concrete
  effect/Predicate operations directly.
- `Predicate.Product` -> `effect/Predicate`: The @effect/typeclass package and
  its Predicate instance dictionaries were removed in v4. Use the concrete
  effect/Predicate operations directly.
- `Predicate.SemiProduct` -> `effect/Predicate`: The @effect/typeclass package
  and its Predicate instance dictionaries were removed in v4. Use the concrete
  effect/Predicate operations directly.
- `Predicate.getMonoidEqv` ->
  `Reducer.make(Predicate.eqv, Predicate.isUnknown)`: Rebuild the removed
  predicate instance as a v4 Reducer with the always-true predicate as
  initialValue.
- `Predicate.getMonoidEvery` ->
  `Reducer.make(Predicate.and, Predicate.isUnknown)`: Rebuild the removed
  predicate instance as a v4 Reducer with the always-true predicate as
  initialValue.
- `Predicate.getMonoidSome` -> `Reducer.make(Predicate.or, Predicate.isNever)`:
  Rebuild the removed predicate instance as a v4 Reducer with the always-false
  predicate as initialValue.
- `Predicate.getMonoidXor` -> `Reducer.make(Predicate.xor, Predicate.isNever)`:
  Rebuild the removed predicate instance as a v4 Reducer with the always-false
  predicate as initialValue.
- `Predicate.getSemigroupEqv` -> `Combiner.make(Predicate.eqv)`: Rebuild the
  removed predicate instance as a v4 Combiner.
- `Predicate.getSemigroupEvery` -> `Combiner.make(Predicate.and)`: Rebuild the
  removed predicate instance as a v4 Combiner.
- `Predicate.getSemigroupSome` -> `Combiner.make(Predicate.or)`: Rebuild the
  removed predicate instance as a v4 Combiner.
- `Predicate.getSemigroupXor` -> `Combiner.make(Predicate.xor)`: Rebuild the
  removed predicate instance as a v4 Combiner.
