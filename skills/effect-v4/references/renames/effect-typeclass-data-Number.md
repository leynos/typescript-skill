<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/typeclass/data/Number` v3 → v4

- `Number.Bounded` -> `none`: V4 has no Bounded dictionary; use Number.Order
  with -Infinity and Infinity as separate bounds.
- `Number.MonoidMax` -> `Number.ReducerMax`: Renamed and moved to the concrete
  v4 Number module.
- `Number.MonoidMin` -> `Number.ReducerMin`: Renamed and moved to the concrete
  v4 Number module.
- `Number.MonoidMultiply` -> `Number.ReducerMultiply`: Renamed and moved to the
  concrete v4 Number module.
- `Number.MonoidSum` -> `Number.ReducerSum`: Renamed and moved to the concrete
  v4 Number module.
- `Number.SemigroupMax` -> `Number.ReducerMax`: The v4 Reducer is also a
  Combiner and preserves maximum combine semantics.
- `Number.SemigroupMin` -> `Number.ReducerMin`: The v4 Reducer is also a
  Combiner and preserves minimum combine semantics.
- `Number.SemigroupMultiply` -> `Number.ReducerMultiply`: The v4 Reducer is
  also a Combiner and preserves multiplication combine semantics.
- `Number.SemigroupSum` -> `Number.ReducerSum`: The v4 Reducer is also a
  Combiner and preserves addition combine semantics.
