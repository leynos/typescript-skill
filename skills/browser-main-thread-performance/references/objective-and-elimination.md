# Objective and elimination

## Name the number

| Objective           | Measure                                                     | Typical budget                        |
| ------------------- | ----------------------------------------------------------- | ------------------------------------- |
| Interaction latency | Interaction to Next Paint (INP), event-to-paint in a trace  | Under 200 ms at the 75th percentile   |
| Frame duration      | Long frames, dropped frames, `requestAnimationFrame` deltas | About 10 ms of script per 60 Hz frame |
| Total throughput    | Items processed per second, time to drain a known backlog   | Set by the feature                    |
| Queue age and depth | Oldest pending item, items waiting                          | Bounded, with a policy when hit       |
| Memory              | Heap after steady state, retained after navigation          | No growth under steady load           |
| Startup             | Time to first interaction, bundle size on the critical path | Set by the product                    |
| Durability          | Work survives tab close, reload, or crash                   | Yes or no; nothing in between         |

_Table 1: Performance objectives, how each is measured, and typical budgets._

Pick one objective per change. A fix that yields more often improves the first
two rows and worsens the third; a fix that batches does the reverse. Write the
chosen objective in the pull request so the trade is visible.

## The frame

At 60 Hz each frame is about 16.7 ms. The browser spends part of it on style,
layout, paint, and compositing, so application script has roughly 10 ms. A task
longer than 50 ms is a long task and blocks input for its duration. A single
synchronous call (`JSON.parse` on a large payload, a big sort) cannot be split;
it can only be made smaller, made rarer, or moved.

## Eliminate before scheduling

Ask these in order; each one removes work rather than rearranging it.

| Question                                   | Mechanism                                                 |
| ------------------------------------------ | --------------------------------------------------------- |
| Does only the present matter?              | Drop arrivals older than the latest                       |
| Does only the final state matter?          | Coalesce: keep the last update per key                    |
| Is the same input computed twice?          | Memoize by structural key                                 |
| Is the element hidden or off-screen?       | Skip; resume on `visibilitychange` or intersection        |
| Is this route or component not yet needed? | Defer with lazy import and an idle or interaction trigger |
| Is the data larger than the view?          | Virtualize; render only what is visible                   |
| Is the work the same on every frame?       | Compute once; let CSS animate the result                  |

_Table 2: Elimination questions and the mechanism each implies._

## Degradation policy for high-rate streams

A terminal, a map tile stream, a live log, a sensor feed: arrivals can exceed
what one thread can render. The policy has to be chosen, bounded, and tested:

- **Batch** by time and size (flush every 16 ms or at 200 KiB, whichever is
  first), so a burst cannot starve the frame and a trickle cannot wait.
- **Coalesce** per key when later updates supersede earlier ones.
- **Drop** with a counter when the consumer is behind, and show the counter.
- **Backpressure** the producer when it can be paused (streams, IPC with
  acknowledgements), and prefer that over the other three when it is available.

Route the general shape to the async skill's
[backpressure reference](../../typescript-async-and-concurrency/references/bounded-concurrency-and-backpressure.md).

## Evidence

- A performance trace from the browser's profiler on a representative device,
  before and after, with the long task or dropped frames marked.
- Frame timing from a `requestAnimationFrame` sampler or the Long Animation
  Frames API, recorded only while the document is visible.
- Queue metrics (depth, age) logged in development builds.
- A benchmark script with a synthetic load and a threshold (long-frame ratio,
  p95 input latency) that CI can run against a headless build.

Without one of these, a performance change is a hypothesis.
