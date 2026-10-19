<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `effect/Scope` v3 → v4

- `Scope.CloseableScope` -> `Scope.Closeable`: Use the renamed type and close
  it with Scope.close(scope, exit).
- `Scope.CloseableScopeTypeId` -> `none`: The closeable-scope marker is private
  in v4.
- `Scope.Scope` -> `Scope.Scope`: The type remains; use module functions
  instead of the removed instance methods.
- `Scope.Scope.Closeable` -> `Scope.Closeable`: The nested alias is now the
  top-level Closeable interface.
- `Scope.Scope.Finalizer` ->
  `(exit: Exit.Exit<any, any>) => Effect.Effect<unknown>`: No alias is
  exported; inline the Scope.addFinalizerExit callback type.
- `Scope.ScopeTypeId` -> `none`: The Scope marker is private in v4 and has no
  public guard.
- `Scope.extend` -> `Scope.provide`: The operation was renamed with the same
  data-first and curried forms.
