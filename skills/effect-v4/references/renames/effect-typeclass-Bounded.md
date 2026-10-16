<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/typeclass/Bounded` v3 → v4

- `Bounded.Bounded` -> `none`: V4 removed Bounded dictionaries. Keep the Order
  and minimum/maximum bounds as separate application values.
- `Bounded.BoundedTypeLambda` -> `none`: V4 removed the @effect/typeclass
  higher-kinded Bounded instance machinery.
- `Bounded.between` -> `Order.isBetween(B.compare)`: Use the v4 Order predicate
  with { minimum: B.minBound, maximum: B.maxBound }; the Bounded dictionary
  itself was removed.
- `Bounded.clamp` -> `Order.clamp(B.compare)`: Use the v4 Order combinator with
  { minimum: B.minBound, maximum: B.maxBound }; the Bounded dictionary itself
  was removed.
- `Bounded.max` -> `Reducer.make(Combiner.max(B.compare).combine, B.minBound)`:
  V4 removed Bounded dictionaries. Build the maximum Reducer from the
  separately retained Order and minimum bound.
- `Bounded.min` -> `Reducer.make(Combiner.min(B.compare).combine, B.maxBound)`:
  V4 removed Bounded dictionaries. Build the minimum Reducer from the
  separately retained Order and maximum bound.
- `Bounded.reverse` -> `Order.flip(B.compare)`: Flip the Order and swap the
  separately stored minimum and maximum bounds; v4 has no bundled Bounded
  dictionary.
