---
name: typescript-async-and-concurrency
description: Use for asynchronous ownership and concurrency in TypeScript and JavaScript, including promise ownership, structured lifetime, AbortSignal, bounded fan-out, backpressure, event-loop scheduling, Web Workers, worker threads, worker pools, and the line between a logical worker and a durable job.
metadata:
  globs: "**/*.ts, **/*.tsx, **/*.mts, **/*.cts, **/*.js, **/*.jsx, **/*.mjs, **/*.cjs"
---

# TypeScript async and concurrency

Use this when the question is who owns a piece of asynchronous work: who
started it, who can stop it, who is waiting for it, how many can run at once,
and on which thread or process it runs.

## Working stance

- Every promise has an owner. The owner awaits it, cancels it, or hands it to
  something that will. A promise with no owner is a leak that reports its
  failure as an unhandled rejection at an unrelated moment.
- Lifetime is structured. Child work ends when its parent ends. Pass an
  `AbortSignal` down, and abort it when the parent scope closes.
- Fan-out is bounded. `Promise.all` over a list whose length comes from input
  is an unbounded resource request.
- Arrival rate versus service rate is a design decision. When producers can
  outpace consumers, choose a policy: bound the queue, drop, coalesce, or apply
  backpressure. "Process everything eventually" is not a policy.
- A single-threaded event loop is a scheduler. CPU work on it blocks input,
  rendering, and timers; the fix is to yield, batch, or move it, in that order
  of cost.
- Keep the vocabulary straight. An event-loop task, an application scheduler,
  a logical worker that owns orchestration, a Web Worker, a worker thread, a
  process, and a durable distributed job are seven different things. See
  [vocabulary.md](references/vocabulary.md).

## Decision surface

- **Ownership.** `void promise` is a decision to orphan work; write it only
  with a comment and a rejection handler. Prefer returning the promise, or
  registering it with a scope that awaits or aborts it on close. See
  [promise-ownership.md](references/promise-ownership.md).
- **Cancellation.** Accept `signal: AbortSignal` on every async function that
  does I/O or loops. Combine caller signals and deadlines with
  `AbortSignal.any`. Route what the rejection means to
  `typescript-errors-and-outcomes`.
- **Bounded concurrency.** Use a limiter (`p-limit` or a small semaphore) with
  a stated limit, or process in chunks with `Promise.allSettled` per chunk and
  a policy for partial failure. See
  [bounded-concurrency-and-backpressure.md](references/bounded-concurrency-and-backpressure.md).
- **Backpressure.** Streams carry it natively (`pipeline`, `for await`, web
  streams with `highWaterMark`); event emitters and ad hoc queues do not. When
  the source cannot be paused, choose drop, coalesce, or sample, and state the
  bound.
- **Yield versus batch.** Yielding (`scheduler.yield`, `setTimeout`,
  `MessageChannel`) improves responsiveness and makes total completion slower.
  Batching improves throughput and makes latency worse. Pick by which number is
  unhealthy; the browser skill owns the measurement.
- **Off-thread work.** Move work to a Web Worker or worker thread when it is
  independent of the DOM, large enough to amortize startup and messaging,
  coarse-grained, bounded in queue depth, explicitly cancellable, and cannot
  overwrite newer state with a stale result. Transfer large buffers; do not
  copy them. See [workers-and-pools.md](references/workers-and-pools.md) for
  the raw worker, Comlink, `workerpool`, Piscina, and durable-queue matrix.
- **Durable work.** When the work must survive a tab, process, deployment, or
  machine failure, no in-process abstraction suffices. That is a job queue or
  workflow engine with idempotency, retries, and observability.

## Red flags

- `Promise.all(items.map(fetchOne))` with `items` from input.
- An `async` function called without `await`, `.catch`, or `void`.
- `setTimeout(fn, 0)` used to "wait for things to settle".
- A worker created per request, or a pool with an infinite queue.
- A worker that receives a request after the UI has moved on and whose
  result overwrites the current state.
- A `for await` loop that pushes into an array without a bound.
- A shared mutable object updated from two awaits with no ordering guarantee.
- A "worker" directory that is an orchestration loop, discussed as if it
  needed a thread.
- CPU work moved to a worker thread because a worker existed, when the work
  was async I/O that Node already parallelizes.

## Pairing

- Pair with `typescript-errors-and-outcomes` for cancellation semantics.
- Pair with `browser-main-thread-performance` when the thread in question
  is the browser main thread.
- Pair with `node-bun-and-processes` for process lifecycle, signals, and
  worker threads in a server or CLI.
- Pair with `electron-and-ipc` when work crosses the main and renderer
  boundary.
- Pair with `typescript-testing` for virtual time and deterministic
  schedulers in tests.
