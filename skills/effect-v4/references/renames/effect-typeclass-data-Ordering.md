<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/typeclass/data/Ordering` v3 → v4

- `Ordering.Monoid` -> `Ordering.Reducer`: Renamed and moved to the concrete v4
  Ordering module.
- `Ordering.Semigroup` -> `Ordering.Reducer`: The v4 Reducer is also a Combiner
  and preserves Ordering combination semantics.
