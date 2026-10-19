# Bounded concurrency and backpressure

## Bounding fan-out

```ts
import pLimit from "p-limit";

const limit = pLimit(8);

export async function fetchAll(urls: readonly string[], signal: AbortSignal) {
  return Promise.all(urls.map((url) => limit(() => fetchJson(url, signal))));
}
```

The limit is a stated resource budget: sockets, file descriptors, memory,
remote rate limit. Pick it from the constraint and write that reason next to
the number. A small semaphore does the same job without a dependency:

```ts
export function semaphore(permits: number) {
  let available = permits;
  const waiters: Array<() => void> = [];
  return async function run<T>(work: () => Promise<T>): Promise<T> {
    if (available > 0) {
      available -= 1;
    } else {
      // The permit is handed straight to this waiter on release, so a caller
      // arriving in between cannot take it first.
      await new Promise<void>((resolve) => waiters.push(resolve));
    }
    try {
      return await work();
    } finally {
      const next = waiters.shift();
      if (next === undefined) {
        available += 1;
      } else {
        next();
      }
    }
  };
}
```

Release transfers the permit to a waiter directly rather than incrementing the
count and waking it: between the increment and the waiter's continuation, a new
caller could otherwise take the permit, and the limit would be exceeded by one.

## Partial failure

With a bound in place, decide what one failure means:

| Policy             | Mechanism                                        | Use when                               |
| ------------------ | ------------------------------------------------ | -------------------------------------- |
| Fail fast          | `Promise.all` plus abort the signal              | Results are useless unless all succeed |
| Collect everything | `Promise.allSettled`, then classify              | Each item is independent and reported  |
| First success      | `Promise.any` plus abort the rest                | Redundant sources                      |
| Chunked            | Loop over chunks with one of the above per chunk | Memory bound on results matters        |

_Table 1: Partial-failure policies for bounded fan-out._

## Backpressure

Backpressure is the consumer telling the producer to slow down. It exists
natively in:

- Node streams via `pipeline` and `highWaterMark`;
- web streams via `ReadableStream` and `WritableStream` with queuing
  strategies;
- `for await` over an async iterator, which pulls one item at a time.

It does not exist in event emitters, `addEventListener`, WebSocket `message`
events, PTY output, or any callback-based source. For those, choose:

| Policy   | Behaviour                                        | Fits                                       |
| -------- | ------------------------------------------------ | ------------------------------------------ |
| Bound    | Queue up to N, then reject or block the producer | Producer can be told to stop               |
| Drop     | Discard arrivals beyond the bound                | Only the recent present matters            |
| Coalesce | Keep the latest, merge updates                   | Only the final state matters               |
| Sample   | Keep every k-th or one per interval              | Trends matter, not every point             |
| Batch    | Buffer for T ms or N bytes, then flush           | Per-item cost dominates; latency has slack |

_Table 2: Degradation policies when the source cannot be paused._

Batching with both a time and a size bound is the standard shape for high-rate
byte streams such as terminal output: flush every 16 ms or at 200 KiB,
whichever comes first, so a burst cannot starve rendering and a trickle cannot
sit unflushed.

## Queue health

Measure queue depth and queue age, not only throughput. A queue whose depth
grows without bound under steady load has an arrival rate above its service
rate, and no amount of yielding fixes that; only a policy from the table does.
