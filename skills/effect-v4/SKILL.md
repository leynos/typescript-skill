---
name: effect-v4
description: Write, review, debug and migrate TypeScript code that uses Effect 4.x (the `effect` npm package, v4.0.0 stable and later, plus matching `@effect/*` packages). Use this skill whenever the task touches Effect — `Effect.gen`, `Effect.fn`, `Layer`, `Context.Service`, `Schema`, `Stream`, `Schedule`, typed errors, fibers, `effect/http`, `effect/http-api`, `effect/cli`, `effect/sql`, `effect/ai`, `@effect/platform-node`, `@effect/vitest` — or when someone asks to upgrade from Effect 3, fix Effect type errors, or design services and layers in an Effect codebase. Trigger even when the user just says "Effect" or "effect-ts" in a TypeScript context, because model training data is dominated by v3 APIs that no longer exist in v4.
metadata:
  globs: "**/*.ts, **/*.tsx, **/*.mts, **/*.cts, **/package.json"
---

# Effect 4.x

Effect 4.0.0 shipped as stable on 1 October 2026, after a long beta
(`effect-smol`) and release-candidate series. The programming model is the one
you know from v3 — `Effect<A, E, R>`, generators, layers, schemas, streams —
but a large fraction of the **names** changed, several modules moved into the
core package, and a handful of semantics shifted. Your priors are mostly v3.
Treat any API name you recall from memory as suspect until something in this
skill or the installed type declarations confirms it.

## Step 1 — establish which Effect you face

Read the installed version before writing a line:

```bash
node -p "require('effect/package.json').version" 2>/dev/null || grep -E '"effect"' package.json
```

- **3.x** — this skill's idioms do not apply. Write v3 code, or follow
  `references/migration.md` if the user wants to upgrade.
- **4.0.0-beta.\* / 4.0.0-rc.\*** — pre-release names drifted. Early betas used
  `ServiceMap.Service` (now `Context.Service`), `effect/unstable/<area>` import
  paths (now `effect/<area>`), `Schema.TaggedErrorClass` (now
  `Schema.TaggedError`). Prefer whatever the installed `.d.ts` files export,
  and recommend upgrading to stable.
- **4.x stable** — follow this skill.

Every `effect` and `@effect/*` package must share one exact version in v4. A
mismatch (e.g. `effect@4.0.5` with `@effect/platform-node@4.0.2`) produces
baffling type errors; check this first when types look impossible.

## Step 2 — trust the installed code over memory

Order of authority: installed `node_modules/effect/dist/*.d.ts` → this skill's
references → your memory. Before using an API you are not certain of, confirm
it exists:

```bash
python3 <skill-dir>/scripts/has_export.py Effect.catchAll Layer.scoped Schema.TaggedError
```

The script resolves each `Module.member` against the installed package, prints
the declaration (with its JSDoc `@since`/`@stability`), and, for misses,
suggests the v4 replacement from the bundled rename tables. When the project
has no `node_modules`, grep the rename tables directly:
`grep -rn "Effect.catchAll" <skill-dir>/references/renames/`.

After writing code, run `npx tsc --noEmit` (or the project's check script) —
Effect's types catch most misremembered APIs, and an unchecked Effect file is
an unfinished one.

## Core idioms (the v4 house style)

These come from the upstream `LLMS.md` and the migration guides; the reasons
matter because they tell you how to extend the pattern to cases not listed.

1. **`Effect.gen` for inline code, `Effect.fn("Name.method")` for reusable
   functions.** `Effect.fn` adds a tracing span and better stack traces; pass
   post-processing combinators as extra arguments
   (`Effect.fn("x")(function*(){…}, Effect.catch(…))`) rather than `.pipe` on
   the result. Use `Effect.fnUntraced` in library hot paths. Never write
   `const f = (x) => Effect.gen(…)` wrappers — that is what `Effect.fn` is for.
2. **Fail with `return yield* new MyError({...})`.** The `return` tells
   TypeScript the branch ends. Errors are yieldable.
3. **Errors are `Schema.TaggedError` classes** (serializable, schema-validated)
   or `Data.TaggedError` when you never cross a boundary. Wrap foreign
   exceptions in a `cause: Schema.Defect()` field. Nest a tagged union in a
   `reason` field when a service has many failure modes, then use
   `Effect.catchReason(s)`.
4. **Services are `Context.Service` classes with a static `layer`.** Build them
   with `Layer.effect(Self, Effect.gen(…))` and return `Self.of({...})`. Name
   the primary layer `layer`, variants `layerTest`, `layerConfig`, and the
   dependency-free one `layerNoDeps`. There are no accessors and no
   auto-generated `Default` layer. Access a service by `yield* Service` —
   prefer that to `Service.use(...)` because it keeps dependencies visible.
5. **Resources live in scopes, and `Layer.effect` already provides one.** Use
   `Effect.acquireRelease` inside `Layer.effect` (there is no `Layer.scoped`);
   use `Effect.scoped` at call sites; `Effect.addFinalizer` for ad-hoc cleanup.
6. **Parse untrusted data with `Schema`**, never with hand-written predicates;
   use the `Predicate` module for runtime type guards instead of writing
   `isRecord` helpers.
7. **Use `DateTime`/`Clock`, not `Date.now()`, and `Random`, not
   `Math.random()`,** in effectful code, so `TestClock` and deterministic tests
   work.
8. **Run at the edge only.** `NodeRuntime.runMain(program)` or
   `Layer.launch(appLayer).pipe(NodeRuntime.runMain)` for processes;
   `ManagedRuntime.make(layer)` to call Effect from a framework (Hono, Express,
   Next).
9. **Concurrency is explicit.** Pass `{ concurrency: n | "unbounded" }` to
   `Effect.all`/`forEach`/`Stream.mapEffect`; ambient `withConcurrency` is gone.

## Canonical shape

```ts
import { NodeRuntime } from "@effect/platform-node"
import { Config, Context, Effect, Layer, Schema } from "effect"

export class UserNotFound extends Schema.TaggedError<UserNotFound>()("UserNotFound", {
  id: Schema.String
}) {}

export class Users extends Context.Service<Users, {
  readonly find: (id: string) => Effect.Effect<{ readonly id: string; readonly name: string }, UserNotFound>
}>()("myapp/Users") {
  static readonly layer = Layer.effect(
    Users,
    Effect.gen(function*() {
      const prefix = yield* Config.String("USER_PREFIX").pipe(Config.withDefault("user"))
      const find = Effect.fn("Users.find")(function*(id: string) {
        if (id === "") return yield* new UserNotFound({ id })
        return { id, name: `${prefix}-${id}` }
      })
      return Users.of({ find })
    })
  )
}

const program = Effect.gen(function*() {
  const users = yield* Users
  const user = yield* users.find("42")
  yield* Effect.log("found", user)
}).pipe(
  Effect.catchTag("UserNotFound", (e) => Effect.logWarning(`no user ${e.id}`)),
  Effect.provide(Users.layer)
)

NodeRuntime.runMain(program)
```

## v3 reflexes that break in v4

The commonest failures, in rough order of frequency. The full per-module tables
live in `references/renames/` (generated from the upstream migration reference).

| You will be tempted to write (v3)                                     | Write instead (v4)                                                                                  |
| --------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| `Context.Tag("X")<X, S>()`                                            | `Context.Service<X, S>()("X")`                                                                      |
| `Effect.Tag` / `Effect.Service` + `.Default`                          | `Context.Service` (+ `{ make }`), explicit `static layer = Layer.effect(...)`                       |
| `X.method(...)` static accessors                                      | `yield* X` then call, or `X.use((x) => x.method(...))`                                              |
| `Layer.scoped(...)`                                                   | `Layer.effect(...)` (scoped automatically)                                                          |
| `Effect.catchAll` / `catchAllCause` / `catchAllDefect`                | `Effect.catch` / `catchCause` / `catchDefect`                                                       |
| `Effect.catchSome`                                                    | `Effect.catchFilter` (with `Filter`) or `Effect.catchIf`                                            |
| `Effect.either`, `Either.*`                                           | `Effect.result`, `Result.*` (`effect/Result`)                                                       |
| `Effect.fork` / `forkDaemon`                                          | `Effect.forkChild` / `forkDetach`                                                                   |
| `yield* fiber` / `yield* ref` / `yield* deferred` / `yield* option`   | `Fiber.join` / `Ref.get` / `Deferred.await` / `Effect.fromOption`                                   |
| `Effect.async`                                                        | `Effect.callback`                                                                                   |
| `Effect.zipRight` / `zipLeft`                                         | `Effect.andThen` / `Effect.tap`                                                                     |
| `Effect.tapErrorCause`                                                | `Effect.tapCause`                                                                                   |
| `Effect.timeoutFail`                                                  | `Effect.timeoutOrElse`                                                                              |
| `Effect.repeatN(n)`                                                   | `Effect.repeat({ times: n })`                                                                       |
| `Effect.fromNullable`                                                 | `Effect.fromNullishOr`                                                                              |
| `Effect.locally(fx, FiberRef.x, v)`                                   | `Effect.provideService(fx, References.X, v)`                                                        |
| `Effect.runtime<R>()` + `Runtime.runFork`                             | `Effect.context<R>()` + `Effect.runForkWith(ctx)`                                                   |
| `Effect.makeSemaphore` / `makeLatch`                                  | `Semaphore.make` / `Latch.make`                                                                     |
| `Effect.gen(this, function*…)`                                        | `Effect.gen({ self: this }, function*…)`                                                            |
| `Scope.extend`                                                        | `Scope.provide`                                                                                     |
| `Cause.isFailure`, `Cause.failureOption`                              | `Cause.hasFails`, `Cause.findErrorOption` (Cause is a flat `reasons` array)                         |
| `*Exception` (`NoSuchElementException`, `TimeoutException`)           | `*Error` (`Cause.NoSuchElementError`, `Cause.TimeoutError`)                                         |
| `Schema.Union(A, B)`, `Schema.Literal("a","b")`, `Schema.Tuple(A, B)` | `Schema.Union([A, B])`, `Schema.Literals(["a","b"])`, `Schema.Tuple([A, B])`                        |
| `Schema.decodeUnknown` / `decode` / `decodeUnknownEither`             | `Schema.decodeUnknownEffect` / `decodeEffect` / `decodeUnknownExit`                                 |
| `Schema.transform` / `transformOrFail`                                | `from.pipe(Schema.decodeTo(to, SchemaTransformation.transform({...})))`                             |
| `Schema.filter(p)`, `Schema.pattern(r)`, `Schema.int()`               | `.check(Schema.makeFilter(p))`, `Schema.check(Schema.isPattern(r))`, `Schema.check(Schema.isInt())` |
| `Schema.Date` (ISO string → Date)                                     | `Schema.DateFromString` (`Schema.Date` now means a `Date` value)                                    |
| `ParseResult.*`, `ParseError`                                         | `SchemaIssue.*` / `SchemaParser.*`; decode failures are `Schema.SchemaError`                        |
| `import … from "@effect/platform/HttpClient"`                         | `import { HttpClient } from "effect/http"`                                                          |
| `import … from "effect/unstable/http"` (beta)                         | `import … from "effect/http"`                                                                       |
| `TRef`, `TMap`, `STM.*`                                               | `TxRef`, `TxHashMap`, transactional `Tx*` modules                                                   |
| `Equal.equals({a:1},{a:1}) === false`                                 | now `true` — equality is structural by default                                                      |

Two semantic changes produce no type errors, so watch for them in review:

- **Layers memoize across nested `Effect.provide` calls.** An inner `provide`
  of a layer value that an enclosing `provide` already built reuses that
  instance instead of building a second (v3 built two). Sibling provides —
  sequential or concurrent — still build their own instances. For isolation use
  `Layer.fresh(layer)`, or `Effect.provide(layer, { local: true })` on the
  *innermost* provide: `local` builds in a private memo map that inner provides
  then share, so an outer `local` does not isolate an inner provide. (Verified
  against 4.0.5; the upstream migration guide's `local` example shows the
  opposite ordering and is wrong.)
- **`Equal.equals` is structural** for plain objects, arrays, `Map`, `Set`,
  `Date`, and `NaN === NaN`. Code that relied on reference identity (dedup by
  object) changes behaviour; wrap with `Equal.byReference` to restore it.

## Package and import map

`@effect/platform`, `@effect/rpc`, `@effect/cluster`, `@effect/cli`,
`@effect/ai`, `@effect/sql`, `@effect/workflow`, `@effect/experimental` were
merged into `effect`. Separate packages remain only for platforms
(`@effect/platform-node|bun|browser|deno`), SQL drivers (`@effect/sql-pg`,
`@effect/sql-sqlite-node`, …), AI providers (`@effect/ai-openai`,
`@effect/ai-anthropic`, …), atom bindings (`@effect/atom-react`),
`@effect/opentelemetry`, and `@effect/vitest`.

| Area                     | v4 import                                                           |
| ------------------------ | ------------------------------------------------------------------- |
| HTTP client/server       | `effect/http` (`HttpClient`, `HttpRouter`, `FetchHttpClient`…)      |
| Schema-first APIs        | `effect/http-api` (`HttpApi`, `HttpApiEndpoint`, `HttpApiBuilder`…) |
| CLI                      | `effect/cli` (`Command`, `Flag`, `Argument`)                        |
| SQL                      | `effect/sql` (`SqlClient`, `Model`, `SqlError`) + driver package    |
| AI                       | `effect/ai` (`LanguageModel`, `Tool`, `Toolkit`, `Chat`)            |
| RPC / cluster / workflow | `effect/rpc`, `effect/cluster`, `effect/workflow`                   |
| Child processes          | `effect/process` (`ChildProcess`, `ChildProcessSpawner`)            |
| OTLP export              | `effect/observability` (`OtlpTracer`, `OtlpLogger`)                 |
| Test services            | `effect/testing` (`TestClock`, `TestConsole`)                       |
| FileSystem / Path        | `effect` (core) with `NodeServices.layer` / `NodeFileSystem.layer`  |

Modules under these area paths are `@stability unstable` (breaking changes
allowed in minor releases); `@stability experimental` allows breaks in patches.
Core modules (`Effect`, `Layer`, `Schema`, `Stream`, …) follow semver. Pin
exact versions when you depend on unstable areas, and mention this when
advising on production use.

## Reference map — read only what the task needs

| Read this                        | When                                                                                                                                         |
| -------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| `references/core.md`             | Writing effects, errors, services, layers, resources, concurrency, scheduling, running, config, logging                                      |
| `references/schema.md`           | Defining or migrating schemas, classes, brands, transformations, defaults, JSON                                                              |
| `references/streams.md`          | `Stream`, `Sink`, `Queue`, `PubSub` pipelines                                                                                                |
| `references/platform.md`         | HTTP client, `HttpApi` servers, CLI, SQL, child processes, AI                                                                                |
| `references/testing.md`          | `@effect/vitest`, `TestClock`, layer-based test doubles                                                                                      |
| `references/migration.md`        | Upgrading a v3 codebase; review checklist                                                                                                    |
| `references/renames/<module>.md` | Exact v3→v4 fate of a specific API (grep, don't read whole)                                                                                  |
| `references/upstream/`           | Verbatim official migration guides, `LLMS.md`, and the curated example programs (`examples/`) — the ground-truth idioms from the Effect team |

## Tooling in `scripts/`

- `has_export.py Module.member …` — existence check against installed `effect`,
  with v4 replacement hints for misses.
- `check_v3_patterns.py <path>` — scans `.ts/.tsx` files for v3-only APIs and
  imports, printing `file:line`, the offending pattern, and the v4 replacement.
  Run it on any file you migrate or review, and on your own output before
  handing it back.
