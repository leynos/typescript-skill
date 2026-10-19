---
name: browser-main-thread-performance
description: Use for browser main-thread responsiveness in TypeScript and JavaScript, including interaction latency and frame budgets, work elimination, CSS and compositor delegation, layout read and write phasing, yielding and prioritized scheduling, visibility, worker offload, and the latency versus throughput trade-off.
metadata:
  globs: "**/*.ts, **/*.tsx, **/*.js, **/*.jsx, **/*.mjs, **/*.css, **/*.scss"
---

# Browser main-thread performance

Use this when a page stutters, an interaction lags, or a stream of updates
outruns the frame budget. The main thread runs script, style, layout, and paint
in one queue; anything that holds it holds the user. This skill is a decision
sequence, not a tutorial on any one API.

## Working stance

- Name the unhealthy number first: interaction latency, frame duration or
  dropped frames, total throughput, queue age or backlog depth, memory,
  startup, or durability across process death. Each has a different fix and the
  fixes trade against each other.
- Latency and throughput pull apart. Yielding makes the page responsive and
  makes the whole job finish later; batching does the reverse. Choose, and
  record the choice.
- JavaScript chooses semantic state; CSS decides how that state is presented.
  That membrane is the default, with named exceptions, not a slogan.
- Eliminating work beats scheduling it, scheduling beats offloading it, and
  offloading beats buying a bigger device. Walk the sequence in that order.
- Measure on a representative device with traces and frame timing before and
  after. Static analysis points the torch; it cannot swear the dragon is there.

## Decision sequence

1. **State the objective.** Which number, measured how, on which device, with
   what budget. A 60 Hz frame leaves roughly 10 ms for application work after
   the browser's own share; an interaction should respond within 200 ms. See
   [objective-and-elimination.md](references/objective-and-elimination.md).
2. **Eliminate work.** Can updates be dropped (only the present matters),
   coalesced (only the final state matters), deduplicated or memoized, skipped
   while hidden or off-screen, or deferred until the route or component is
   needed? A high-rate stream needs a stated degradation policy; "process
   everything eventually" is not one.
3. **Hand presentation to CSS or another browser subsystem.** Express state as
   a semantic class, a `data-*` attribute, ARIA state where it is genuinely
   semantic, or a CSS custom property for a dynamic scalar. Animate `transform`
   and `opacity`; move layout-changing geometry with a FLIP sequence rather
   than animating `top`, `left`, `width`, or `height`. Named exceptions are in
   [css-state-membrane.md](references/css-state-membrane.md).
4. **Shape unavoidable main-thread work.** Collect layout reads, then perform
   writes. Batch semantic updates. Use `requestAnimationFrame` only for work
   coupled to the next frame. Yield long, splittable, non-frame work through a
   project-level scheduler abstraction with feature detection and a fallback,
   because `scheduler.yield` and `scheduler.postTask` are not Baseline. Stop
   continuous work when the document is hidden. Attach cancellation and drop
   stale results. See
   [main-thread-shaping.md](references/main-thread-shaping.md) and the
   [scheduler example](../../examples/positive/yielding-scheduler.ts).
5. **Move coarse CPU work off-thread.** Only when the work is DOM-independent,
   large enough to amortize startup and messaging, coarse-grained, bounded in
   queue depth, cancellable, transfer-friendly, and safe against stale results.
   The abstraction matrix (raw worker, Comlink, `workerpool`, Piscina, durable
   queue) lives in
   [the async skill's workers reference](../typescript-async-and-concurrency/references/workers-and-pools.md).
6. **Keep the vocabulary.** An event-loop task, an application scheduler, a
   logical worker that owns orchestration, a Web Worker, a worker thread, a
   process, and a durable job are different things. A deterministic
   orchestration loop called "the worker" is not evidence that a thread is
   needed.

## Red flags

- `element.style.display`, `.opacity`, or `.transform` set to a static value
  from application code outside a documented adapter.
- A `requestAnimationFrame` loop that keeps running while the tab is hidden,
  or that performs work unrelated to the next frame.
- A layout read (`getBoundingClientRect`, `offsetWidth`, `getComputedStyle`)
  interleaved with writes inside one loop.
- `setTimeout(fn, 0)` sprinkled through components as the yielding strategy,
  with no shared abstraction and no fallback plan.
- A worker introduced for a 5 ms task, or a `JSON.parse` of a multi-megabyte
  payload left on the main thread because "it only happens once".
- A stream handler that appends every arrival to state with no drop, coalesce,
  or batch policy.
- A performance claim with no trace, no frame timing, and no device named.
- A lint rule asked to decide whether a calculation is heavy enough for a
  worker.

## Three rings of enforcement

High-confidence static policy (a `prefer-css-state` rule, a Stylelint
animation-property rule) belongs in the linter. Conservative structural rules
(read/write interleaving, repeated layout animation) are prototypes until real
fixtures exist. Whether a calculation is heavy, a queue needs dropping, or an
animation drops frames is runtime evidence and must never be pretended into a
lint rule. Route the tooling question to `typescript-quality-tools`.

## Pairing

- Pair with `typescript-async-and-concurrency` for backpressure policies,
  cancellation, and the worker threshold.
- Pair with `react-and-accessible-ui` when the scheduling decision lives
  inside a component or a framework's own scheduler.
- Pair with `electron-and-ipc` when the renderer is an Electron window and
  the main process is the other half of the queue.
- Pair with `typescript-quality-tools` to turn a settled policy into a rule.
