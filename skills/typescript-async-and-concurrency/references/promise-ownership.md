# Promise ownership and structured lifetime

## The owner rule

A promise is owned by whichever code will observe its settlement. Observing
means one of:

- `await`, so the caller's control flow depends on it;
- returning it, so the caller becomes the owner;
- registering it with a scope that will await or abort it on close;
- `void promise` with a `.catch` attached and a comment saying why the result
  is not needed.

An `async` function invoked as a statement with none of these is an orphan. Its
rejection surfaces as `unhandledrejection`, in Node as a process-level event
that may terminate the process, at a time unrelated to the call site.

## A scope

```ts
export class Scope {
  readonly #controller = new AbortController();
  readonly #pending = new Set<Promise<unknown>>();

  get signal(): AbortSignal {
    return this.#controller.signal;
  }

  spawn<T>(work: (signal: AbortSignal) => Promise<T>): Promise<T> {
    const promise = work(this.signal);
    this.#pending.add(promise);
    promise.finally(() => this.#pending.delete(promise)).catch(() => undefined);
    return promise;
  }

  async close(reason?: unknown): Promise<void> {
    this.#controller.abort(reason);
    await Promise.allSettled(this.#pending);
  }
}
```

A component, request, session, or command creates a scope; everything it starts
goes through `spawn`; `close` aborts and then waits. Nothing outlives its
parent by accident. The `.catch(() => undefined)` on the bookkeeping chain is
deliberate: the caller still holds the original promise and observes the
rejection there.

## Awaiting correctly

- `await` inside a loop serializes; that is often right for ordering and
  usually wrong for throughput. Choose, then say so in a comment.
- `Promise.all` fails fast and leaves the other promises running. Pair it with
  a signal so they stop, or use `allSettled` when partial results matter.
- `Promise.race` leaves the losers running. Prefer a signal-based timeout.
- `return await` inside `try` is required to catch; `return promise` without
  `await` escapes the `try`.

## Fire-and-forget that is actually fine

Analytics beacons, best-effort cache warming, and log flushing can be orphaned
on purpose. Write it as:

```ts
void warmCache(signal).catch((error: unknown) => {
  log.debug("cache warm failed", { error });
});
```

The `void` says the result is unwanted; the `.catch` says the failure is
observed; the signal says it stops with its parent.

## React and lifecycles

An effect that starts async work must return a cleanup that aborts it. The
cleanup runs on unmount and on dependency change, so a stale result cannot set
state on a component that has moved on. Route component-specific ownership to
`react-and-accessible-ui`.
