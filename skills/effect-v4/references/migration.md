# Migrating a codebase from Effect 3 to Effect 4

The core programming model survives; names, package layout and a few semantics
do not. Migrate mechanically first, then review the semantic changes by hand.

## Procedure

1. **Inventory.** Run `python3 <skill-dir>/scripts/check_v3_patterns.py src/`
   to list every v3-only import and API with its replacement. Record the
   counts; they are your progress meter.
2. **Align versions.** Set `effect` and every `@effect/*` dependency to the
   same exact 4.x version. Remove packages that merged into `effect`:
   `@effect/platform`, `@effect/rpc`, `@effect/cluster`, `@effect/cli`,
   `@effect/ai`, `@effect/sql`, `@effect/workflow`, `@effect/experimental`,
   `@effect/typeclass`. Keep platform, driver and provider packages
   (`@effect/platform-node`, `@effect/sql-pg`, `@effect/ai-openai`, …) at the
   same version. Require TypeScript ≥ 5.9 (7 recommended) and, for
   `@effect/vitest`, Vitest 5.
3. **Rewrite imports.** `@effect/platform/HttpClient` → `effect/http`;
   `@effect/platform/HttpApi*` and `OpenApi` → `effect/http-api`;
   `@effect/platform/FileSystem|Path|Terminal` → `effect`;
   `@effect/platform/Command|CommandExecutor` → `effect/process`
   (`ChildProcess`, `ChildProcessSpawner`); `@effect/cli/*` → `effect/cli`
   (`Options`→`Flag`, `Args`→`Argument`); `@effect/sql` → `effect/sql`;
   `effect/Either` → `effect/Result`; `effect/TestClock` → `effect/testing`;
   `effect/FiberRef` → `effect/References`; `effect/ParseResult` →
   `effect/SchemaIssue` / `effect/SchemaParser`; `effect/T*` (STM) →
   `effect/Tx*`. Beta-era `effect/unstable/<area>` → `effect/<area>`. The
   complete import map, plus modules with no counterpart and removed modules,
   is in `renames/_imports.md`.
4. **Services.** Convert every `Context.Tag`, `Context.GenericTag`,
   `Effect.Tag` and `Effect.Service` to `Context.Service`. Replace generated
   `.Default` layers with an explicit
   `static readonly layer = Layer.effect(this, this.make).pipe(Layer.provide(...deps))`.
   Replace accessor calls (`Svc.method(...)`) with `yield* Svc` or
   `Svc.use(...)`. Rename `Layer.scoped` → `Layer.effect`. See
   `upstream/migration/services.md`.
5. **Mechanical renames.** `catchAll*`, `fork`/`forkDaemon`, `either`, `async`,
   `zipRight/zipLeft`, `tapErrorCause`, `Cause.*Exception`, `Scope.extend`,
   `Effect.locally`, and the rest of the table in `SKILL.md`. For anything
   else, grep `renames/`.
6. **De-yield non-effects.** `yield* ref|deferred|fiber|option|either` no longer
   compiles; use `Ref.get`, `Deferred.await`, `Fiber.join`, `Effect.fromOption`,
   `Effect.fromResult`. `Config` values and services remain yieldable.
7. **Schema.** Work through `references/schema.md` §8 and
   `upstream/migration/schema.md`. Prioritize `Schema.Date` (silent meaning
   change), variadic → array constructors, `transform*` → `decodeTo`,
   `optionalWith` → `optionalKey`/`withDecodingDefault*`.
8. **Cause handling.** Rewrite tree walks over `Sequential`/`Parallel` into
   iteration over `cause.reasons`.
9. **Runtime.** Replace `Runtime<R>` plumbing with `Context<R>` and
   `Effect.run*With`; `ManagedRuntime` is unchanged in spirit.
10. **Compile, test, re-scan.** `tsc --noEmit`, the test suite, and
    `check_v3_patterns.py` should all come back clean.

## Semantic changes to review by hand

These compile and still change behaviour:

| Change                                                                                | What to look for                                                                                                                                             |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Structural `Equal.equals` (plain objects, arrays, Map, Set, Date; `NaN` equals `NaN`) | Dedup/caching keyed on object identity; `HashSet`/`HashMap` of plain objects now collapse duplicates. Use `Equal.byReference` to restore identity semantics. |
| Layer memoization across nested `provide` calls                                       | Code that relied on a fresh instance per `provide` (tests, per-request pools). See `core.md` §3 for the observed matrix.                                     |
| `Schema.Date` now means `Date` → `Date`                                               | Any API boundary that decoded ISO strings. Use `Schema.DateFromString`.                                                                                      |
| Keep-alive in the core runtime                                                        | Scripts that relied on the process exiting while fibers wait now hang until those fibers finish; interrupt or scope them.                                    |
| `Effect.partition` returns `[passes, fails]`                                          | v3 returned `[failures, successes]` — swapped tuple order.                                                                                                   |
| `Stream.scan`/`runFold` initial value is a thunk                                      | `Stream.scan(0, f)` → `Stream.scan(() => 0, f)`.                                                                                                             |
| `Cause` flattening loses sequential/parallel structure                                | Error reporters that rendered the tree.                                                                                                                      |
| `Effect.race*` interrupts losers that are still starting                              | Side effects in racing effects' setup.                                                                                                                       |

## Reviewing v4 code (checklist)

- No v3 names (`check_v3_patterns.py` clean).
- Every reusable effectful function uses `Effect.fn("Name")`; no
  `(...) => Effect.gen` wrappers.
- Failures use `return yield* new Err(...)`.
- Errors are `Schema.TaggedError` (or `Data.TaggedError` when never
  serialized); foreign exceptions are wrapped with `cause: Schema.Defect()`,
  not stringified.
- Services are `Context.Service` classes with
  `layer`/`layerTest`/`layerNoDeps`; no service reads another service at call
  time without it appearing in `R`.
- Resources are acquired with `acquireRelease` inside `Layer.effect` or
  `Effect.scoped`.
- Concurrency is explicit (`concurrency` option on `all`/`forEach`/`mapEffect`).
- Untrusted input is decoded with `Schema`; no hand-rolled `typeof` guards (use
  `Predicate`).
- Time and randomness go through `Clock`/`DateTime`/`Random`.
- `effect/<unstable area>` dependencies are pinned to exact versions.
- `tsc --noEmit` passes with `strict` on.
