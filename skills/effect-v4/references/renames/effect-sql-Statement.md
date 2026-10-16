<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/sql/Statement` v3 → v4

- `Statement.FragmentId` -> `none`: The v4 fragment brand is private; use
  Fragment, fragment, and isFragment instead of direct type-id access.
- `Statement.Statement` -> `effect/sql/Statement#Statement`: Moved; the nested
  Transformer type is now top-level and its callback receives Fiber.Fiber
  rather than FiberRefs.FiberRefs.
- `Statement.currentTransformer` -> `effect/sql/Statement#CurrentTransformer`:
  Capitalized and changed from FiberRef\<Option\<Transformer\>\> to
  Context.Reference\<Transformer | undefined\>.
- `Statement.custom` -> `effect/sql/Statement#custom`: Retained, but returns a
  Custom segment and uses paramA/paramB/paramC; wrap it with Statement.fragment
  when a Fragment is required.
- `Statement.defaultEscape` -> `effect/sql/Statement#defaultEscape`: Moved with
  the same signature.
- `Statement.join` -> `effect/sql/Statement#join`: Moved with the same empty,
  single, and multiple-clause behavior.
- `Statement.make` -> `effect/sql/Statement#make`: Moved with the same
  constructor inputs.
- `Statement.makeCompiler` -> `effect/sql/Statement#makeCompiler`: Moved to
  core Effect; the constructor options are exposed as Statement.CompilerOptions
  and retain the dialect-specific callbacks.
- `Statement.setTransformer` ->
  `Layer.succeed(Statement.CurrentTransformer, transformer)`: The helper was
  removed; provide the CurrentTransformer reference as a layer.
- `Statement.unsafeFragment` ->
  `Statement.fragment([Statement.literal(sql, params)])`: The helper was
  removed; construct the low-level fragment explicitly, or use the active
  constructor's sql.unsafe for an executable statement.
- `Statement.withTransformer` ->
  `Effect.provideService(Statement.CurrentTransformer, transformer)`: The
  helper was removed; locally provide the transformer reference around the
  effect.
- `Statement.withTransformerDisabled` ->
  `Effect.provideService(Statement.CurrentTransformer, undefined)`: The helper
  was removed; locally provide undefined for the transformer reference.
