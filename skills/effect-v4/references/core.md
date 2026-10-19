# Core Effect 4 patterns

Every TypeScript block in this file compiles against `effect@4.0.5` with
`strict` and `exactOptionalPropertyTypes`. Copy the shapes, not just the names.

## Contents

1. Writing effects: `Effect.gen`, `Effect.fn`, constructors
2. Typed errors, defects, and `Cause`
3. Services and layers
4. Resources and scopes
5. Concurrency: fibers, `all`/`forEach`, races, coordination primitives
6. Retries, repetition, timeouts
7. Configuration
8. `Option`, `Result`, `Exit`
9. Fiber-local state: `Context.Reference` and `References`
10. Logging and tracing
11. Running programs and integrating with non-Effect code

______________________________________________________________________

## 1. Writing effects

```ts
import { Effect, Schema } from "effect"

class InvalidPayload extends Schema.TaggedError<InvalidPayload>()("InvalidPayload", {
  input: Schema.String,
  cause: Schema.Defect()
}) {}

// Values you already have
export const fromValue = Effect.succeed({ retries: 3 })

// Synchronous side effects that must not throw
export const now = Effect.sync(() => performance.now())

// Synchronous code that may throw: map the throw into a typed error
export const parse = Effect.fn("parse")((input: string) =>
  Effect.try({
    try: () => JSON.parse(input) as unknown,
    catch: (cause) => new InvalidPayload({ input, cause })
  })
)

// Promise APIs; the AbortSignal fires on interruption
export const download = Effect.fn("download")((url: string) =>
  Effect.tryPromise({
    try: (signal) => fetch(url, { signal }).then((r) => r.text()),
    catch: (cause) => new InvalidPayload({ input: url, cause })
  })
)

// Callback APIs: return a finalizer so interruption cancels the source
export const tick = Effect.callback<number>((resume) => {
  const handle = setTimeout(() => resume(Effect.succeed(200)), 10)
  return Effect.sync(() => clearTimeout(handle))
})

// Nullable values
export const header = (headers: Map<string, string>) =>
  Effect.fromNullishOr(headers.get("x-request-id"))
```

`Effect.fn` variants:

```ts
import { Effect, Schema } from "effect"

class TooSmall extends Schema.TaggedError<TooSmall>()("TooSmall", { n: Schema.Number }) {}

// Named: span + stack frame. Annotate the return type with Effect.fn.Return<A, E, R>.
export const double = Effect.fn("double")(
  function*(n: number): Effect.fn.Return<number, TooSmall> {
    if (n < 1) return yield* new TooSmall({ n })
    yield* Effect.logDebug("doubling", n)
    return n * 2
  },
  // extra arguments post-process the resulting effect — use these, not .pipe
  Effect.annotateLogs({ fn: "double" })
)

// Untraced: for library internals and hot loops
export const clamp = Effect.fnUntraced(function*(n: number) {
  return Math.max(0, Math.min(100, n))
})

// Anonymous Effect.fn is fine for handlers passed inline
export const handlers = { run: Effect.fn(function*(n: number) { return yield* double(n) }) }
```

Inside classes, bind `this` with an options object:
`Effect.gen({ self: this }, function*() {…})`.

Sequencing helpers you will reach for: `Effect.map`, `Effect.flatMap`,
`Effect.andThen` (accepts a value, function or effect), `Effect.tap`,
`Effect.as`, `Effect.asVoid`, `Effect.zip`, `Effect.zipWith`, `Effect.when`,
`Effect.suspend`. Removed: `zipLeft`, `zipRight`, `if`, `unless`, `iterate`,
`loop` — write an ordinary loop in `Effect.gen`.

## 2. Typed errors, defects, and Cause

Three ways to declare an error class:

```ts
import { Data, Effect, Schema } from "effect"

// Preferred: schema-backed, serializable over RPC/HTTP, yieldable
export class NotFound extends Schema.TaggedError<NotFound>()("NotFound", {
  id: Schema.String
}) {}

// Untagged schema error (no _tag; name is the identifier)
export class SmtpError extends Schema.Error<SmtpError>("SmtpError")({
  cause: Schema.Defect()
}) {}

// Lightweight, not serializable — fine for purely internal errors
export class CacheMiss extends Data.TaggedError("CacheMiss")<{ readonly key: string }> {}

export const program = Effect.gen(function*() {
  const hit = false
  if (!hit) return yield* new CacheMiss({ key: "k" })
  return "value"
})
```

Handling, from narrow to broad:

```ts
import { Effect, Schema } from "effect"

class ParseError extends Schema.TaggedError<ParseError>()("ParseError", { input: Schema.String }) {}
class ReservedPort extends Schema.TaggedError<ReservedPort>()("ReservedPort", { port: Schema.Int }) {}
declare const loadPort: (s: string) => Effect.Effect<number, ParseError | ReservedPort>

export const one = loadPort("80").pipe(Effect.catchTag("ReservedPort", () => Effect.succeed(3000)))
export const several = loadPort("80").pipe(Effect.catchTag(["ParseError", "ReservedPort"], () => Effect.succeed(3000)))
export const byCase = loadPort("80").pipe(
  Effect.catchTags({
    ParseError: (e) => Effect.succeed(e.input.length),
    ReservedPort: (e) => Effect.succeed(e.port + 1000)
  })
)
export const everything = loadPort("80").pipe(Effect.catch(() => Effect.succeed(3000)))
export const conditional = loadPort("80").pipe(
  Effect.catchIf((e) => e._tag === "ReservedPort", () => Effect.succeed(3000))
)
export const mapped = loadPort("80").pipe(Effect.mapError((e) => new Error(e._tag)))
export const asDefect = loadPort("80").pipe(Effect.orDie) // E becomes never
export const observed = loadPort("80").pipe(Effect.tapError((e) => Effect.logWarning(e._tag)))
export const asResult = Effect.result(loadPort("80")) // Effect<Result<number, ParseError | ReservedPort>>
```

**Reason errors.** When one service-level error carries many causes, put a
tagged union in a `reason` field. Callers handle reasons without widening the
error channel:

```ts
import { Effect, Schema } from "effect"

class RateLimited extends Schema.TaggedError<RateLimited>()("RateLimited", { retryAfter: Schema.Finite }) {}
class QuotaExceeded extends Schema.TaggedError<QuotaExceeded>()("QuotaExceeded", { limit: Schema.Int }) {}
class ApiError extends Schema.TaggedError<ApiError>()("ApiError", {
  reason: Schema.Union([RateLimited, QuotaExceeded])
}) {}
declare const call: Effect.Effect<string, ApiError>

// handle one reason; the optional 4th argument handles every other reason
export const a = call.pipe(
  Effect.catchReason("ApiError", "RateLimited", (r) => Effect.succeed(`wait ${r.retryAfter}s`))
)
export const b = call.pipe(
  Effect.catchReasons("ApiError", { QuotaExceeded: (r) => Effect.succeed(`limit ${r.limit}`) })
)
// lift the reasons into the error channel and use ordinary catchTags
export const c = call.pipe(
  Effect.unwrapReason("ApiError"),
  Effect.catchTags({
    RateLimited: () => Effect.succeed("later"),
    QuotaExceeded: () => Effect.succeed("never")
  })
)
```

**Defects** (`Effect.die`, thrown exceptions inside `sync`) do not appear in
`E`. Recover with `Effect.catchDefect`, observe with `Effect.tapDefect`.
`Effect.catchCause` sees everything, including interruption.

**Cause is flat in v4**: `cause.reasons: ReadonlyArray<Fail | Die | Interrupt>`.

```ts
import { Cause, Effect } from "effect"

export const describe = <E>(cause: Cause.Cause<E>): string =>
  cause.reasons.map((r) =>
    Cause.isFailReason(r) ? `fail: ${String(r.error)}`
    : Cause.isDieReason(r) ? `die: ${String(r.defect)}`
    : "interrupted"
  ).join("; ")

export const logged = Effect.fail("boom").pipe(
  Effect.catchCause((cause) =>
    Cause.hasInterruptsOnly(cause) ? Effect.interrupt : Effect.logError(Cause.pretty(cause))
  )
)
```

Built-in errors: `Cause.NoSuchElementError`, `Cause.TimeoutError`,
`Cause.IllegalArgumentError`, `Cause.ExceededCapacityError`,
`Cause.UnknownError` (thrown by the one-argument `Effect.try(() => …)`
overload).

## 3. Services and layers

```ts
import { Config, Context, Effect, Layer, Schema } from "effect"

export class DatabaseError extends Schema.TaggedError<DatabaseError>()("DatabaseError", {
  cause: Schema.Defect()
}) {}

// Class syntax: <Self, Shape>() then the identifier. Use "package/path/Name" ids.
export class Database extends Context.Service<Database, {
  query(sql: string): Effect.Effect<ReadonlyArray<unknown>, DatabaseError>
}>()("myapp/db/Database") {
  static readonly layer = Layer.effect(
    Database,
    Effect.gen(function*() {
      const url = yield* Config.Redacted("DATABASE_URL")
      const query = Effect.fn("Database.query")(function*(sql: string) {
        yield* Effect.logDebug("sql", sql, url)
        return [] as ReadonlyArray<unknown>
      })
      return Database.of({ query })
    })
  )

  // In-memory variant for tests; Layer.succeed takes a ready value
  static readonly layerTest = Layer.succeed(Database, Database.of({ query: () => Effect.succeed([]) }))
}

// The service type, should you need it
export type DatabaseShape = Database["Service"]

// A service that depends on another
export class Users extends Context.Service<Users, {
  count: Effect.Effect<number, DatabaseError>
}>()("myapp/Users") {
  static readonly layerNoDeps = Layer.effect(
    Users,
    Effect.gen(function*() {
      const db = yield* Database
      return Users.of({ count: Effect.map(db.query("select 1"), (rows) => rows.length) })
    })
  )
  // provide: hide Database from consumers. provideMerge: expose both.
  static readonly layer = this.layerNoDeps.pipe(Layer.provide(Database.layer))
  static readonly layerWithDb = this.layerNoDeps.pipe(Layer.provideMerge(Database.layer))
}
```

Constructor-on-the-class form (replaces v3 `Effect.Service`). `make` is stored
on the class; you still write the layer yourself and wire dependencies with
`Layer.provide`:

```ts
import { Context, Effect, Layer } from "effect"

class Prefix extends Context.Service<Prefix, { readonly value: string }>()("Prefix") {
  static readonly layer = Layer.succeed(Prefix, { value: "app" })
}

export class Greeter extends Context.Service<Greeter>()("Greeter", {
  make: Effect.gen(function*() {
    const prefix = yield* Prefix
    return { greet: (name: string) => Effect.log(`[${prefix.value}] hello ${name}`) }
  })
}) {
  static readonly layer = Layer.effect(this, this.make).pipe(Layer.provide(Prefix.layer))
}
```

Function syntax when a class is overkill:
`const Port = Context.Service<number>("Port")`.

Layer toolkit (all verified exports): `Layer.effect`, `Layer.succeed`,
`Layer.sync`, `Layer.effectDiscard` (run for side effects, e.g. a background
fiber), `Layer.unwrap` (choose a layer from an effect/config), `Layer.merge`,
`Layer.mergeAll`, `Layer.provide`, `Layer.provideMerge`, `Layer.fresh`,
`Layer.mock`, `Layer.launch`, `Layer.orDie`, `Layer.catchTag`, `Layer.tap*`,
`Layer.withSpan`. `Layer.provide` and `Effect.provide` accept an array of
layers.

```ts
import { Config, Context, Effect, Layer } from "effect"

class Store extends Context.Service<Store, { put(v: string): Effect.Effect<void> }>()("Store") {
  static readonly layerMemory = Layer.sync(Store, () => {
    const items: Array<string> = []
    return Store.of({ put: (v) => Effect.sync(() => { items.push(v) }) })
  })
  static readonly layerRemote = (url: URL) =>
    Layer.succeed(Store, Store.of({ put: (v) => Effect.log(`PUT ${url.href} ${v}`) }))

  // choose implementation from configuration at build time
  static readonly layer = Layer.unwrap(Effect.gen(function*() {
    const inMemory = yield* Config.Boolean("STORE_IN_MEMORY").pipe(Config.withDefault(false))
    return inMemory ? Store.layerMemory : Store.layerRemote(yield* Config.URL("STORE_URL"))
  }))
}

// A layer that only runs a background task for as long as it is alive
export const Heartbeat = Layer.effectDiscard(
  Effect.forkScoped(Effect.forever(Effect.log("tick").pipe(Effect.delay("5 seconds"))))
)
```

Memoization (new in v4): an `Effect.provide` nested inside another provide of
the same layer *value* reuses the enclosing instance. Observed on 4.0.5:

| Pipeline                                                                                     | Builds                                            |
| -------------------------------------------------------------------------------------------- | ------------------------------------------------- |
| `fx.pipe(Effect.provide(L), Effect.provide(L))`                                              | 1                                                 |
| `fx1.pipe(Effect.provide(L))` then later `fx2.pipe(Effect.provide(L))`                       | 2                                                 |
| `Effect.all([fx1.pipe(Effect.provide(L)), fx2.pipe(Effect.provide(L))], { concurrency: 2 })` | 2                                                 |
| `fx.pipe(Effect.provide(L, { local: true }), Effect.provide(L))`                             | 2                                                 |
| `fx.pipe(Effect.provide(L), Effect.provide(L, { local: true }))`                             | 1 — inner provide reuses the outer local instance |
| `fx.pipe(Effect.provide(Layer.fresh(L)))`                                                    | always a new build                                |

Put `{ local: true }` on the innermost provide, or use `Layer.fresh`, when you
need isolation. Two separately constructed layer values (e.g. `makeLayer()`
called twice) are distinct keys and never share. Still prefer composing one app
layer and providing it once — it keeps the dependency graph legible.

For keyed, dynamically built resources (per-tenant pools), use
`LayerMap.Service`; see
`upstream/examples/01_effect/05_resources/30_layer-map.ts`.

## 4. Resources and scopes

```ts
import { Context, Effect, Layer } from "effect"

interface Conn { readonly close: () => void; readonly send: (s: string) => void }
declare const openConn: () => Conn

export class Socket extends Context.Service<Socket, { send(s: string): Effect.Effect<void> }>()("Socket") {
  // Layer.effect provides a Scope: the finalizer runs when the layer is torn down
  static readonly layer = Layer.effect(
    Socket,
    Effect.gen(function*() {
      const conn = yield* Effect.acquireRelease(
        Effect.sync(openConn),
        (c) => Effect.sync(() => c.close())
      )
      yield* Effect.addFinalizer(() => Effect.log("socket layer closed"))
      return Socket.of({ send: (s) => Effect.sync(() => conn.send(s)) })
    })
  )
}

// At a call site, Effect.scoped closes the scope when the block finishes
export const once = Effect.scoped(
  Effect.gen(function*() {
    const conn = yield* Effect.acquireRelease(Effect.sync(openConn), (c) => Effect.sync(() => c.close()))
    conn.send("hi")
  })
)

// Bracket in one call
export const bracket = Effect.acquireUseRelease(
  Effect.sync(openConn),
  (c) => Effect.sync(() => c.send("hi")),
  (c) => Effect.sync(() => c.close())
)
```

`Effect.ensuring(finalizer)`, `Effect.onExit`, `Effect.onError`,
`Effect.onInterrupt` attach cleanup to a single effect. Manual scopes:
`Scope.make()`, `Scope.provide(scope)` (was `Scope.extend`),
`Scope.close(scope, exit)`. `Effect.acquireRelease` takes
`{ interruptible: true }` in place of v3's `acquireReleaseInterruptible`.

## 5. Concurrency

```ts
import { Deferred, Effect, Fiber, Latch, Queue, Ref, Semaphore } from "effect"

declare const fetchUser: (id: number) => Effect.Effect<string>

// Bounded parallelism; results keep input order
export const users = Effect.forEach([1, 2, 3, 4], fetchUser, { concurrency: 2 })
export const pair = Effect.all([fetchUser(1), fetchUser(2)], { concurrency: "unbounded" })
export const record = Effect.all({ a: fetchUser(1), b: fetchUser(2) }, { concurrency: 2 })
// Keep going on failure and collect Results instead of short-circuiting
export const settled = Effect.all([fetchUser(1), Effect.fail("x")], { mode: "result" })

export const fibers = Effect.gen(function*() {
  const child = yield* Effect.forkChild(fetchUser(1))     // dies with the parent
  const detached = yield* Effect.forkDetach(fetchUser(2)) // outlives the parent (was forkDaemon)
  const a = yield* Fiber.join(child)                      // fibers are not effects: join explicitly
  const exit = yield* Fiber.await(detached)               // Exit without rethrowing
  yield* Fiber.interrupt(detached)
  return [a, exit] as const
})

export const fastest = Effect.race(fetchUser(1), fetchUser(2)) // loser is interrupted
export const firstOfMany = Effect.raceAll([fetchUser(1), fetchUser(2), fetchUser(3)])

export const coordination = Effect.gen(function*() {
  const counter = yield* Ref.make(0)
  yield* Ref.update(counter, (n) => n + 1)
  const n = yield* Ref.get(counter) // Ref is no longer yieldable itself

  const ready = yield* Deferred.make<string>()
  yield* Effect.forkChild(Deferred.succeed(ready, "go"))
  const signal = yield* Deferred.await(ready)

  const sem = yield* Semaphore.make(3)
  yield* sem.withPermits(1)(Effect.log("guarded"))

  const gate = yield* Latch.make()
  yield* Effect.forkChild(gate.open)
  yield* gate.await

  const q = yield* Queue.bounded<number>(16)
  yield* Queue.offer(q, n)
  const item = yield* Queue.take(q)
  return { signal, item }
})
```

Fork options (all `fork*` variants):
`{ startImmediately?: boolean, uninterruptible?: boolean | "inherit" }`.
`Effect.forkScoped` ties a fiber to the surrounding `Scope` (the right choice
inside a `Layer.effect`). `Effect.forkIn(scope)` targets a specific scope.
`FiberSet`, `FiberMap` and `FiberHandle` manage dynamic groups of fibers.
`Effect.awaitAllChildren` waits for structured children. `forkAll` and
`forkWithErrorHandler` are gone.

Transactional memory uses the `Tx*` modules (`TxRef`, `TxHashMap`, `TxQueue`,
`TxSemaphore`, …) — the `STM`/`T*` names do not exist.

## 6. Retries, repetition, timeouts

```ts
import { Effect, Schedule, Schema } from "effect"

class HttpError extends Schema.TaggedError<HttpError>()("HttpError", {
  status: Schema.Int,
  retryable: Schema.Boolean
}) {}
declare const request: Effect.Effect<string, HttpError>

// Options form
export const simple = request.pipe(Effect.retry({ times: 3 }))
export const guarded = request.pipe(
  Effect.retry({ schedule: Schedule.exponential("100 millis"), times: 5, while: (e) => e.retryable })
)

// Schedule form: exponential backoff capped at 10 s between attempts, jittered, only for retryable errors
export const backoff = Schedule.min([Schedule.exponential("250 millis"), Schedule.spaced("10 seconds")]).pipe(
  Schedule.jittered,
  Schedule.setInputType<HttpError>(),
  Schedule.while(({ input }) => input.retryable)
)
export const robust = request.pipe(Effect.retry(backoff))

// Builder form infers the input type for you
export const inferred = request.pipe(
  Effect.retry(($) => $(Schedule.spaced("1 second")).pipe(Schedule.while(({ input }) => input.retryable)))
)

export const polled = Effect.log("poll").pipe(Effect.repeat(Schedule.spaced("30 seconds")))
export const thrice = Effect.log("hi").pipe(Effect.repeat({ times: 3 })) // was repeatN

// Timeouts: timeout fails with Cause.TimeoutError
export const bounded = request.pipe(Effect.timeout("2 seconds"))
export const withFallback = request.pipe(
  Effect.timeoutOrElse({ duration: "2 seconds", orElse: () => Effect.succeed("cached") })
)
export const maybe = request.pipe(Effect.timeoutOption("2 seconds")) // Option on timeout
```

Schedule combinators: `Schedule.recurs(n)`, `spaced`, `fixed`, `exponential`,
`fibonacci`, `cron`, `jittered`, `min([...])` (continues while any schedule
continues; shorter delay wins — was `union`), `max([...])` (continues only
while all continue; longer delay wins — was `intersect`), `while`, `tap`,
`setInputType`. Durations accept `"5 seconds"`, `"250 millis"`, numbers
(milliseconds) or `Duration` values.

## 7. Configuration

`Config` values are effects: `yield*` them anywhere.

```ts
import { Config, ConfigProvider, Effect, Redacted } from "effect"

export const settings = Effect.gen(function*() {
  const port = yield* Config.Port("PORT").pipe(Config.withDefault(3000))
  const host = yield* Config.String("HOST").pipe(Config.withDefault("0.0.0.0"))
  const debug = yield* Config.Boolean("DEBUG").pipe(Config.withDefault(false))
  const token = yield* Config.Redacted("API_TOKEN") // Redacted<string>: hidden from logs
  const url = yield* Config.URL("UPSTREAM_URL")
  return { port, host, debug, url, auth: `Bearer ${Redacted.value(token)}` }
})

// Supply config explicitly (tests, non-env sources)
export const testRun = settings.pipe(
  Effect.provideService(
    ConfigProvider.ConfigProvider,
    ConfigProvider.fromUnknown({ API_TOKEN: "t", UPSTREAM_URL: "https://example.com" })
  )
)
```

`Config.schema(schema, "NAME")` decodes a value through any `Schema`.

## 8. Option, Result, Exit

`Option` and `Result` (v3's `Either`, with `Result.succeed`/`Result.fail`,
`Result.isSuccess`/`isFailure`) are plain data, **not effects**. Convert
explicitly:

```ts
import { Effect, Exit, Option, Result } from "effect"

export const fromOpt = Effect.fromOption(Option.some(1))                   // fails NoSuchElementError on None
export const custom = Effect.fromOption(Option.none<number>(), () => "missing" as const)
export const fromRes = Effect.fromResult(Result.fail("bad"))

export const inspect = Effect.gen(function*() {
  const r = yield* Effect.result(Effect.fail("x"))
  const msg = Result.match(r, { onSuccess: (a) => `ok ${a}`, onFailure: (e) => `err ${e}` })
  const exit = yield* Effect.exit(Effect.succeed(1))
  return Exit.isSuccess(exit) ? msg : "failed"
})

// Pure generator syntax for Option/Result themselves
export const sum = Option.gen(function*() {
  const a = yield* Option.some(1)
  const b = yield* Option.some(2)
  return a + b
})
```

## 9. Fiber-local state

`FiberRef` is gone. Built-in knobs are `Context.Reference` values in
`References`; set them for a region with `Effect.provideService`.

```ts
import { Context, Effect, References } from "effect"

export const FeatureFlag = Context.Reference<boolean>("myapp/FeatureFlag", { defaultValue: () => false })

export const quiet = Effect.logDebug("hidden").pipe(
  Effect.provideService(References.MinimumLogLevel, "Info")
)

export const flagged = Effect.gen(function*() {
  const on = yield* FeatureFlag // default when not provided
  return on
}).pipe(Effect.provideService(FeatureFlag, true))
```

## 10. Logging and tracing

```ts
import { Effect, Layer, Logger, References } from "effect"

export const JsonLogs = Logger.layer([Logger.consoleJson])
export const WarnAndAbove = Layer.succeed(References.MinimumLogLevel, "Warn")

export const checkout = Effect.gen(function*() {
  yield* Effect.logInfo("validating cart", { items: 3 })
  yield* Effect.annotateCurrentSpan({ "cart.items": 3 })
}).pipe(
  Effect.annotateLogs({ route: "POST /checkout" }),
  Effect.withLogSpan("checkout"),
  Effect.withSpan("checkout")
)
```

Log levels: `"Trace" | "Debug" | "Info" | "Warn" | "Error" | "Fatal"`. For OTLP
export use `OtlpTracer.layer` / `OtlpLogger.layer` from `effect/observability`
with `OtlpSerialization.layerJson` and an `HttpClient` layer; reach for
`@effect/opentelemetry` only when joining an existing OpenTelemetry SDK setup.

## 11. Running programs

```ts
import { NodeRuntime } from "@effect/platform-node"
import { Context, Effect, Layer, ManagedRuntime } from "effect"

class Clock2 extends Context.Service<Clock2, { readonly now: Effect.Effect<number> }>()("Clock2") {
  static readonly layer = Layer.succeed(Clock2, { now: Effect.sync(() => performance.now()) })
}

const main = Effect.gen(function*() {
  const clock = yield* Clock2
  yield* Effect.log("started at", yield* clock.now)
}).pipe(Effect.provide(Clock2.layer))

// Process entrypoint: signal handling, exit codes, error reporting
NodeRuntime.runMain(main)

// Long-running servers/workers: build the app as a layer and launch it
// NodeRuntime.runMain(Layer.launch(AppLayer))

// Bridging into callback/promise frameworks
export const runtime = ManagedRuntime.make(Clock2.layer)
export const handler = async () => runtime.runPromise(Clock2.use((c) => c.now))
// on shutdown: await runtime.dispose()

// Low-level runners (scripts, tests): Effect.runPromise, runPromiseExit, runSync,
// runSyncExit, runFork, runCallback. With a captured context: run*With(context).
export const capture = Effect.gen(function*() {
  const ctx = yield* Effect.context<Clock2>()
  return Effect.runForkWith(ctx)(Clock2.use((c) => c.now))
})
```

The v4 runtime keeps the process alive while fibers wait on asynchronous work,
so a bare `Effect.runPromise` no longer exits early on `Deferred.await`;
`runMain` is still preferred for signal handling and exit codes. `Runtime<R>`
no longer exists.
