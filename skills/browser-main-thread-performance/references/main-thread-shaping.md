# Shaping main-thread work

## Read, then write

Interleaving a layout read with a layout-invalidating write forces the browser
to recompute layout for each read. Collect reads, then perform writes:

```ts
// Reads
const heights = rows.map((row) => row.getBoundingClientRect().height);
// Writes
rows.forEach((row, i) => row.style.setProperty("--row-height", `${heights[i]}px`));
```

Reads: `getBoundingClientRect`, `offsetWidth`, `clientHeight`, `scrollTop`,
`getComputedStyle`, `focus()` in some cases. Writes: setting classes,
attributes, styles, text, or structure.

A small measure/mutate queue that runs all queued reads then all queued writes
once per frame is the conceptual model. FastDOM is the reference
implementation; it suits direct-DOM code and imperative adapters, and is not a
blanket dependency for a React application, where the framework already batches
DOM writes per commit. The useful idea is the two-phase discipline, not the
library.

## Which timer

| Need                                         | Mechanism                                                          |
| -------------------------------------------- | ------------------------------------------------------------------ |
| Work coupled to the next frame               | `requestAnimationFrame`, one callback per frame, coalesced         |
| Yield between chunks of long, non-frame work | `scheduler.yield()` with a fallback                                |
| Run a task at a stated priority              | `scheduler.postTask(fn, { priority })` with a fallback             |
| Low-priority work when the browser is idle   | `requestIdleCallback` with a timeout, or `postTask` `"background"` |
| Yield without the `setTimeout` clamp         | `MessageChannel` port message                                      |
| Run after the current task's microtasks      | `queueMicrotask` (does not yield to input or rendering)            |

_Table 1: Scheduling needs and the mechanism that fits each._

`scheduler.yield` and `scheduler.postTask` are available in Chromium browsers
and Firefox but not Safari, and are not Baseline. A continuation after
`scheduler.yield` is prioritized ahead of other queued tasks of the same
priority, which a `setTimeout` continuation is not. Feature detect and fall
back; never sprinkle the detection through components. The
[yielding-scheduler.ts](../../../examples/positive/yielding-scheduler.ts)
example is a project-level abstraction with a `setTimeout` fallback and
cancellation.

## A chunked loop

```ts
export async function processAll<T>(
  items: readonly T[],
  handle: (item: T) => void,
  scheduler: Scheduler,
  signal: AbortSignal,
): Promise<void> {
  const deadline = 8; // ms of work before yielding
  let start = performance.now();
  for (const item of items) {
    signal.throwIfAborted();
    handle(item);
    if (performance.now() - start > deadline) {
      await scheduler.yield();
      start = performance.now();
    }
  }
}
```

Yield by elapsed time, not by item count, so the chunk adapts to the device.
Expect the total to take longer than the unchunked loop; that is the trade.

## Visibility

Continuous work (frame timing samplers, polling, animations driven by script)
stops when `document.visibilityState` is `"hidden"` and resumes on
`visibilitychange`. Browsers throttle timers in hidden tabs anyway; code that
assumes a steady cadence while hidden computes garbage.

## Stale results

Any deferred or offloaded computation can complete after the state it was
computed for has moved on. Carry a request identifier or a generation counter,
compare on completion, and drop results that no longer match. Cancellation
through `AbortSignal` is the complement: stop the work, not only the result.

## Framework schedulers

React batches state updates and commits DOM writes in one pass; its
`startTransition` marks updates as interruptible. Those are the right tools
inside a component tree. The project scheduler above is for work outside the
tree (parsing, indexing, layout measurement in adapters) and for frameworks
without their own scheduler. Route the React specifics to
`react-and-accessible-ui`.
