<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/typeclass/data/Duration` v3 → v4

- `Duration.Bounded` -> `none`: V4 has no Bounded dictionary; use
  Duration.Order with Duration.zero and Duration.infinity as separate bounds.
- `Duration.MonoidMax` -> `Reducer.make(Duration.max, Duration.zero)`: Rebuild
  the removed maximum Monoid as a v4 Reducer with the same identity.
- `Duration.MonoidMin` -> `Reducer.make(Duration.min, Duration.infinity)`:
  Rebuild the removed minimum Monoid as a v4 Reducer with the same identity.
- `Duration.MonoidSum` -> `Duration.ReducerSum`: Renamed and moved to the
  concrete v4 Duration module.
- `Duration.SemigroupMax` -> `Duration.CombinerMax`: Renamed and moved to the
  concrete v4 Duration module.
- `Duration.SemigroupMin` -> `Duration.CombinerMin`: Renamed and moved to the
  concrete v4 Duration module.
- `Duration.SemigroupSum` -> `Duration.ReducerSum`: The v4 Reducer is also a
  Combiner and preserves Duration.sum combine semantics.
