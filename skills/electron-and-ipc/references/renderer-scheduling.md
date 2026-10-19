# Renderer scheduling

The renderer is a browser window with one extra pressure: a main process that
can produce data faster than any frame budget. The general sequence in
`browser-main-thread-performance` applies; these are the Electron specifics.

## Batch in main, coalesce in the renderer

| Stage              | Mechanism                                                 | Bound                         |
| ------------------ | --------------------------------------------------------- | ----------------------------- |
| Source             | PTY, log tail, progress events                            | Unbounded by nature           |
| Main batcher       | Flush every 16 ms or at 200 KiB, whichever first          | One message per frame at most |
| IPC                | `webContents.send` per batch                              | Payload size from the batcher |
| Renderer coalescer | One `requestAnimationFrame` per frame applies all pending | One DOM update per frame      |
| Renderer           | Terminal emulator writes, virtualized list, canvas        | Frame budget                  |

_Table 1: The stages between a high-rate source in main and the screen._

Backpressure across IPC is not automatic. If the renderer falls behind, main
cannot tell unless the renderer acknowledges batches. For sources that can be
paused (a PTY can), implement an acknowledgement: the renderer reports how many
bytes it has applied, and main pauses the source when the gap exceeds a bound.

## Frame timing in production

A self-rescheduling `requestAnimationFrame` sampler that records frame
durations and reports long frames is useful telemetry. Keep it honest:

- Run only while `document.visibilityState === "visible"`; stop on
  `visibilitychange` and resume on return.
- Cancel on window unload and on the `shutdown` event from main.
- Report through the same IPC protocol as everything else, batched.
- Define a long frame once (16 ms at 60 Hz) and a threshold for alerting (a
  long-frame ratio over a window, a p95 input latency).

Pair it with a benchmark script that drives a synthetic PTY load against a
headless window and asserts the thresholds, so a regression fails CI rather
than waiting for a user.

## WebGL and canvas

A terminal or a map in the renderer owns its drawing surface. The adapter
component creates the renderer addon, handles `onContextLoss` by falling back
to canvas, disables WebGL when the window is transparent (compositing cost),
and bounds the number of live contexts with a small pool, because browsers
limit WebGL contexts per page.

## Imperative DOM in the renderer

The CSS membrane still applies. Geometry measured during a drag (a split pane)
is written through a CSS custom property that the stylesheet consumes, not
through `left` or `top` directly. Padding passed to a terminal emulator goes
through the emulator's theme or options API, not `element.style.padding`.
`!important` from script means the cascade is wrong; fix the stylesheet.

## Multiple windows

Each window has its own renderer process and its own frame budget. Shared state
lives in main, and windows subscribe to the slices they display. A window that
is hidden or minimized should receive no high-rate data; main checks
`win.isVisible()` and `win.isMinimized()` before sending, or the renderer
unsubscribes on `visibilitychange`.
