# Virtual time and deterministic schedulers

## Two kinds of clock

| Clock                 | Controls                                                    | Use for                                       |
| --------------------- | ----------------------------------------------------------- | --------------------------------------------- |
| Runner fake timers    | `setTimeout`, `setInterval`, `Date.now` in the test process | Debounce, retry backoff, timeouts in adapters |
| Injected `Clock` port | Only code that reads the port                               | Domain logic, transition scheduling, journals |

_Table 1: Fake timers versus an injected clock._

Fake timers reach everything in the process, including libraries, which is
convenient and dangerous: a library that polls with `setInterval` stalls. An
injected clock reaches only code that asked for it, which is what domain code
should do. Use both: the port for the core, fake timers for the adapter that
turns port time into real time.

## A clock port

```ts
export interface Clock {
  readonly now: () => number;
  readonly sleep: (ms: number, signal?: AbortSignal) => Promise<void>;
}

export class VirtualClock implements Clock {
  #now = 0;
  readonly #sleepers: Array<{ readonly at: number; readonly wake: () => void }> = [];

  now = (): number => this.#now;

  sleep = (ms: number): Promise<void> =>
    new Promise((wake) => {
      this.#sleepers.push({ at: this.#now + ms, wake });
    });

  advance(ms: number): void {
    const target = this.#now + ms;
    for (const sleeper of [...this.#sleepers].sort((a, b) => a.at - b.at)) {
      if (sleeper.at <= target) {
        this.#now = sleeper.at;
        this.#sleepers.splice(this.#sleepers.indexOf(sleeper), 1);
        sleeper.wake();
      }
    }
    this.#now = target;
  }
}
```

Wake sleepers in time order, setting `now` to each wake time before waking, so
code that reads the clock inside a woken continuation sees the scheduled time
rather than the target. Microtasks must drain between wakes for continuations
to run; a `await Promise.resolve()` after each wake, or a `drain()` helper that
loops until no sleeper is due, keeps the order honest.

## Testing a scheduler

A logical worker that drains transitions in virtual-time order:

```ts
test("applies a transition only once the clock reaches it", async () => {
  const clock = new VirtualClock();
  const worker = new Worker({ clock, ids: seededIds(1701), journal });
  worker.schedule({ at: 250, event: { type: "opened", socketId: "s1" } });

  clock.advance(249);
  await worker.drain();
  expect(journal.entries).toHaveLength(0);

  clock.advance(1);
  await worker.drain();
  expect(journal.entries).toEqual([
    {
      virtualTime: 250,
      event: { type: "opened", socketId: "s1" },
      state: { kind: "open", socketId: "s1" },
    },
  ]);
});
```

Two rows, one either side of the boundary, document the contract. "Never
applies a transition before its virtual timestamp" over all schedules is a
property: route to `typescript-verification`, which will pick model-based
`fast-check` or a proof.

## Determinism gate

The same seed and the same event sequence must produce byte-identical journals.
Run the scenario twice in one test and compare serialized journals; run it once
more with a different seed and assert the journals differ in identifiers only.
This gate catches an accidental `Date.now()` or `Math.random()` in the core
faster than any review.

## Fake timers in adapters

```ts
test("flushes a partial batch after 16 ms", () => {
  vi.useFakeTimers();
  const emitted: string[] = [];
  const batcher = new DataBatcher((chunk) => emitted.push(chunk));
  batcher.write("abc");
  vi.advanceTimersByTime(15);
  expect(emitted).toEqual([]);
  vi.advanceTimersByTime(1);
  expect(emitted).toEqual(["abc"]);
  vi.useRealTimers();
});
```

Restore real timers in a `finally` or an `afterEach`; a leaked fake clock makes
the next suite hang.

## Async ordering

- `await` a `Promise` the code under test returns rather than polling.
- To assert on ordering between two async paths, use the `fast-check`
  scheduler, which explores interleavings, rather than a single hand-written
  sequence.
- Never assert that something did _not_ happen by waiting a fixed time; assert
  that a later observable event happened and the forbidden one has not.
