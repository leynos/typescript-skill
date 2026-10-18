<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/typeclass/data/BigInt` v3 → v4

- `BigInt.MonoidMultiply` -> `BigInt.ReducerMultiply`: Renamed and moved to the
  concrete v4 BigInt module.
- `BigInt.MonoidSum` -> `BigInt.ReducerSum`: Renamed and moved to the concrete
  v4 BigInt module.
- `BigInt.SemigroupMax` -> `BigInt.CombinerMax`: Renamed and moved to the
  concrete v4 BigInt module.
- `BigInt.SemigroupMin` -> `BigInt.CombinerMin`: Renamed and moved to the
  concrete v4 BigInt module.
- `BigInt.SemigroupMultiply` -> `BigInt.ReducerMultiply`: The v4 Reducer is
  also a Combiner and preserves multiplication combine semantics.
- `BigInt.SemigroupSum` -> `BigInt.ReducerSum`: The v4 Reducer is also a
  Combiner and preserves addition combine semantics.
