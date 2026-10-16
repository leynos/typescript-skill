# Testing Effect 4 code

`@effect/vitest@4.x` requires **Vitest 5** (`>=5 <6`) and the identical
`effect` version. Test services (`TestClock`, `TestConsole`) moved to
`effect/testing`; `effect/FastCheck` is gone in favour of native
`effect/Arbitrary` and `it.effect.prop`.

Blocks compile against `effect@4.0.5`, `@effect/vitest@4.0.5`, `vitest@5.0.4`.

## The test variants

| API                                                | Runs with                                                                              |
| -------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `it.effect(name, () => fx)`                        | Scoped, `TestClock` + `TestConsole` provided (time does not pass unless you adjust it) |
| `it.live(name, () => fx)`                          | Scoped, real clock/console                                                             |
| `it.effect.each(cases)(name, (c) => fx)`           | Parameterized                                                                          |
| `it.effect.prop(name, [schemas…], ([a, …]) => fx)` | Property test with arbitraries derived from schemas                                    |
| `it.flakyTest(fx, timeout?)`                       | Retries an intermittently failing effect                                               |
| `layer(L)(name, (it) => {...})`                    | One layer instance shared across a describe block                                      |

There is no `it.scoped` any more: every `it.effect` body already runs in a
scope.

```ts
import { assert, describe, it } from "@effect/vitest"
import { Effect, Fiber, Schema } from "effect"
import { TestClock } from "effect/testing"

describe("basics", () => {
  it.effect("asserts inside Effect.gen", () =>
    Effect.gen(function*() {
      const n = yield* Effect.succeed(21).pipe(Effect.map((x) => x * 2))
      assert.strictEqual(n, 42)
    }))

  it.effect("controls virtual time", () =>
    Effect.gen(function*() {
      const fiber = yield* Effect.forkChild(Effect.sleep("1 minute").pipe(Effect.as("done")))
      yield* TestClock.adjust("1 minute")
      assert.strictEqual(yield* Fiber.join(fiber), "done")
    }))

  it.effect("expects a typed failure", () =>
    Effect.gen(function*() {
      const result = yield* Effect.result(Effect.fail("nope"))
      assert.isTrue(result._tag === "Failure")
    }))

  it.effect.prop("reverse twice is identity", [Schema.String], ([s]) =>
    Effect.gen(function*() {
      assert.strictEqual([...s].reverse().reverse().join(""), s)
    }))
})
```

## Test doubles through layers

Give each service a `layerTest` (or build one ad hoc with `Layer.succeed` /
`Layer.mock`) and provide it per test, or share it with `layer(...)`.

```ts
import { assert, describe, it, layer } from "@effect/vitest"
import { Context, Effect, Layer, Ref } from "effect"

class Mailer extends Context.Service<Mailer, {
  send(to: string): Effect.Effect<void>
}>()("app/Mailer") {}

// A recording fake whose state the test can inspect
class Outbox extends Context.Service<Outbox, Ref.Ref<ReadonlyArray<string>>>()("test/Outbox") {
  static readonly layer = Layer.effect(Outbox, Ref.make<ReadonlyArray<string>>([]))
}
const MailerFake = Layer.effect(
  Mailer,
  Effect.gen(function*() {
    const outbox = yield* Outbox
    return Mailer.of({ send: (to) => Ref.update(outbox, (xs) => [...xs, to]) })
  })
).pipe(Layer.provideMerge(Outbox.layer))

const signup = Effect.fn("signup")(function*(email: string) {
  const mailer = yield* Mailer
  yield* mailer.send(email)
})

describe("signup", () => {
  it.effect("sends a welcome email", () =>
    Effect.gen(function*() {
      yield* signup("ada@example.com")
      const sent = yield* Ref.get(yield* Outbox)
      assert.deepStrictEqual(sent, ["ada@example.com"])
    }).pipe(Effect.provide(MailerFake)))
})

// Shared instance: state carries over between tests in this block
layer(MailerFake)("shared mailer", (it) => {
  it.effect("first", () => signup("a@x").pipe(Effect.asVoid))
  it.effect("second sees the first", () =>
    Effect.gen(function*() {
      yield* signup("b@x")
      assert.strictEqual((yield* Ref.get(yield* Outbox)).length, 2)
    }))
})
```

Isolation caveat: v4 reuses a layer instance when an `Effect.provide` is nested
inside another provide of the same layer value. Separate tests each get their
own instance, but inside one test an inner provide silently shares the outer
one; use `Layer.fresh(layer)` or put `{ local: true }` on the *inner* provide
when it must not.

`Layer.mock(Service, { method: ... })` builds a partial implementation whose
missing methods die when called — handy when a test touches only one method of
a wide service.

For HTTP APIs, `HttpApiTest` (in `effect/http-api`) gives an in-memory typed
client; for GraphQL, `GraphQLClient.layerTest`. Worked examples:
`upstream/examples/09_testing/`,
`upstream/examples/51_http-server/20_testing.ts`.

Vitest config: nothing Effect-specific is required; `@effect/vitest` exports
`addEqualityTesters()` if you want `expect(...).toEqual` to honour `Equal`.
