# Streams, queues and pub/sub in Effect 4

`Stream<A, E, R>` is pull-based and lazy, as in v3. The structural change:
**`Chunk` left the public stream API.** Batches are `NonEmptyReadonlyArray<A>`,
every `*Chunk*` operator became `*Array*`, and `runCollect` yields a plain
`Array<A>`. End-of-stream is signalled with `Cause.Done` rather than
`Option<E>` encodings.

Blocks compile against `effect@4.0.5`.

## Creating streams

```ts
import { Array, Effect, Option, Queue, Schedule, Schema, Stream } from "effect"

export const numbers = Stream.fromIterable([1, 2, 3])
export const literal = Stream.make("a", "b", "c")
export const counting = Stream.range(1, 100)
export const once = Stream.fromEffect(Effect.succeed(42))
export const polled = Stream.fromEffectSchedule(Effect.succeed(3), Schedule.spaced("30 seconds")) // was repeatEffectWithSchedule
export const forever = Stream.fromEffectRepeat(Effect.sync(() => performance.now()))           // was repeatEffect

// Cursor pagination: each step returns [batch, Option<nextCursor>]
export const pages = Stream.paginate(0, (page: number) =>
  Effect.succeed([Array.range(page * 10, page * 10 + 9), page < 3 ? Option.some(page + 1) : Option.none()] as const)
)

class SourceError extends Schema.TaggedError<SourceError>()("SourceError", { cause: Schema.Defect() }) {}
async function* lines() { yield "x"; yield "y" }
export const fromAsync = Stream.fromAsyncIterable(lines(), (cause) => new SourceError({ cause }))

// Any callback API (was Stream.async / asyncScoped / asyncPush)
declare const emitter: { on(cb: (n: number) => void): () => void }
export const pushed = Stream.callback<number>(Effect.fn(function*(queue) {
  yield* Effect.acquireRelease(
    Effect.sync(() => emitter.on((n) => Queue.offerUnsafe(queue, n))),
    (off) => Effect.sync(off)
  )
}))
```

Also: `Stream.fromQueue`, `fromPubSub`, `fromReadableStream`,
`fromEventListener`, `unfold` (effectful; return `undefined` to stop), `tick`,
`fromSchedule`. For Node streams use `NodeStream.fromReadable` from
`@effect/platform-node`.

## Transforming and consuming

```ts
import { Effect, Sink, Stream } from "effect"

declare const enrich: (n: number) => Effect.Effect<{ readonly n: number; readonly big: boolean }>

const pipeline = Stream.range(1, 1_000).pipe(
  Stream.filter((n) => n % 3 === 0),
  Stream.mapEffect(enrich, { concurrency: 8 }),       // bounded parallel, order preserved
  Stream.tap((x) => Effect.logDebug("item", x.n)),
  Stream.take(50)
)

export const all = Stream.runCollect(pipeline)                       // Effect<Array<…>>
export const count = Stream.runCount(pipeline)
export const total = pipeline.pipe(Stream.map((x) => x.n), Stream.runFold(() => 0, (acc: number, n) => acc + n))
export const viaSink = pipeline.pipe(Stream.map((x) => x.n), Stream.run(Sink.sum))
export const first = Stream.runHead(pipeline)                        // Effect<Option<…>>
export const each = pipeline.pipe(Stream.runForEach((x) => Effect.log(x)))
export const batches = pipeline.pipe(Stream.grouped(10), Stream.runForEach((batch) => Effect.log(batch.length)))
export const windows = pipeline.pipe(Stream.groupedWithin(100, "1 second"), Stream.runDrain)
```

Renames to remember: `mapChunks`→`mapArray`, `flattenChunks`→`flattenArray`,
`mapConcat`→`map`+`flattenIterable`, `catchAll`→`catch`, `either`→`result`,
`repeatEffect`→`fromEffectRepeat`, `runForEachChunk`→`runForEachArray`,
`run*Scoped`→plain `run*` (scope handled internally), `zipAll*` removed, `scan`
takes a thunk for its initial state (`Stream.scan(() => 0, f)`),
`onDone`→`onEnd`. Look up anything else in `renames/effect-Stream.md`.

Text and framing: `Stream.decodeText`, `Stream.encodeText`,
`Stream.splitLines`; NDJSON and MessagePack-style codecs live in
`effect/encoding` (`Ndjson`, `SchemaBinary`, `Sse`) and plug in with
`Stream.pipeThroughChannel(...)`:

```ts
import { Schema, Stream } from "effect"
import { Ndjson } from "effect/encoding"

class Entry extends Schema.Class<Entry>("Entry")({
  level: Schema.Literals(["info", "error"]),
  message: Schema.String
}) {}

export const decoded = Stream.make('{"level":"info","message":"start"}\n').pipe(
  Stream.pipeThroughChannel(Ndjson.decodeSchemaString(Entry)()),
  Stream.runCollect
)
```

## Queues, PubSub, and services that stream

```ts
import { Context, Effect, Layer, PubSub, Queue, Stream } from "effect"

export type OrderEvent = { readonly _tag: "Placed" | "Shipped"; readonly id: string }

export class OrderEvents extends Context.Service<OrderEvents, {
  publish(e: OrderEvent): Effect.Effect<void>
  readonly subscribe: Stream.Stream<OrderEvent>
}>()("myapp/OrderEvents") {
  static readonly layer = Layer.effect(
    OrderEvents,
    Effect.gen(function*() {
      const hub = yield* PubSub.bounded<OrderEvent>({ capacity: 256, replay: 16 })
      yield* Effect.addFinalizer(() => PubSub.shutdown(hub))
      return OrderEvents.of({
        publish: (e) => PubSub.publish(hub, e).pipe(Effect.asVoid),
        subscribe: Stream.fromPubSub(hub)
      })
    })
  )
}

export const workQueue = Effect.gen(function*() {
  const q = yield* Queue.bounded<number>(100)          // also: unbounded, dropping, sliding
  yield* Effect.forkChild(Stream.range(1, 10).pipe(Stream.runForEach((n) => Queue.offer(q, n))))
  return yield* Queue.take(q)
})
```

`Queue` in v4 merges v3's `Queue` and `Mailbox`: it carries an error type and
can be ended (`Queue.end`, `Queue.fail`), which `Stream.fromQueue` translates
into stream completion or failure.
