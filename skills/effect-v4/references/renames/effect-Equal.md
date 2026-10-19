<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `effect/Equal` v3 → v4

- `Equal.equivalence` -> `Equal.asEquivalence`: Direct rename. The returned
  equivalence now follows v4 structural equality, including NaN equality and
  cached comparisons for immutable objects.
