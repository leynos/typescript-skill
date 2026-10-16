<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `effect/Ordering` v3 → v4

- `Ordering.combineAll` -> `Ordering.Reducer.combineAll`: The combination
  operation moved to the exported Reducer; first-nonzero and empty-input
  behavior are unchanged.
- `Ordering.combineMany` ->
  `Ordering.Reducer.combineAll(Iterable.prepend(collection, self))`: Prepend
  the initial ordering before reducing to preserve v3 short-circuiting without
  consuming collection when self is nonzero.
