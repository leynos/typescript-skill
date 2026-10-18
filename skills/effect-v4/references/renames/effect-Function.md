<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `effect/Function` v3 → v4

- `Function.FunctionN` -> `Function.FunctionN`: No call-site migration; v4
  keeps the same function shape as a type alias.
- `Function.LazyArg` -> `Function.LazyArg`: No call-site migration; v4 keeps
  the same lazy function shape as a type alias.
- `Function.isFunction` -> `Predicate.isFunction`: The function refinement
  moved to Predicate.
- `Function.unsafeCoerce` -> `Function.cast`: Renamed type-only cast; runtime
  behavior remains identity with no validation.
