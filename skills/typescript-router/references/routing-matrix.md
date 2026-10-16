# TypeScript routing matrix

Use this when the router's question list does not resolve to one skill. Each
row names a symptom or task, the skill to load first, and the usual companion.
`None` means the primary skill carries its own decision surface.

| Symptom or task                                                    | Primary skill                          | Common pair                            |
| ------------------------------------------------------------------ | -------------------------------------- | -------------------------------------- |
| `any` or `as` silences a checker complaint                         | `typescript-types-and-apis`            | None                                   |
| A `switch` over a union has no exhaustive default                  | `typescript-types-and-apis`            | `typescript-data-and-state`            |
| Public function accepts `string` where an identifier is meant      | `typescript-types-and-apis`            | None                                   |
| Enabling `exactOptionalPropertyTypes` floods an old codebase       | `typescript-types-and-apis`            | None                                   |
| Two optional fields are never both set                             | `typescript-data-and-state`            | `typescript-types-and-apis`            |
| State updates mutate shared objects and tests flake                | `typescript-data-and-state`            | None                                   |
| Transport type leaks `Date` or `Map` into JSON                     | `typescript-data-and-state`            | `typescript-boundaries-and-validation` |
| JSON from `fetch` is cast with `as`                                | `typescript-boundaries-and-validation` | `typescript-errors-and-outcomes`       |
| `process.env` read scattered through modules                       | `typescript-boundaries-and-validation` | None                                   |
| Generated client types trusted as runtime truth                    | `typescript-boundaries-and-validation` | `typescript-modules-and-packaging`     |
| `catch (e)` logs and rethrows at every layer                       | `typescript-errors-and-outcomes`       | None                                   |
| Cancellation reported as failure                                   | `typescript-errors-and-outcomes`       | `typescript-async-and-concurrency`     |
| Error object crosses a process or worker boundary                  | `typescript-errors-and-outcomes`       | `typescript-boundaries-and-validation` |
| `Promise.all` over an unbounded list                               | `typescript-async-and-concurrency`     | None                                   |
| Fire-and-forget promise with no owner                              | `typescript-async-and-concurrency`     | `typescript-errors-and-outcomes`       |
| Queue grows faster than it drains                                  | `typescript-async-and-concurrency`     | None                                   |
| Deciding between a Web Worker, a worker thread, and a durable job  | `typescript-async-and-concurrency`     | None                                   |
| `ERR_REQUIRE_ESM` or dual-package hazard                           | `typescript-modules-and-packaging`     | None                                   |
| Declarations resolve for ESM consumers but not CJS                 | `typescript-modules-and-packaging`     | `typescript-types-and-apis`            |
| `exports` map edited without a consumer check                      | `typescript-modules-and-packaging`     | None                                   |
| Generated code is both ignored and tracked                         | `typescript-modules-and-packaging`     | None                                   |
| Zod 3 idioms in a Zod 4 project, or `zod/mini` versus classic      | `zod4-typescript`                      | `typescript-boundaries-and-validation` |
| `Effect.catchAll` or `Context.Tag` fails to type-check on Effect 4 | `effect-v4`                            | None                                   |
| Parsing a large payload freezes the page                           | `browser-main-thread-performance`      | `typescript-async-and-concurrency`     |
| Animation stutters while script runs                               | `browser-main-thread-performance`      | None                                   |
| A stream of updates outruns the frame budget                       | `browser-main-thread-performance`      | `typescript-async-and-concurrency`     |
| `useEffect` sets state from values already in scope                | `react-and-accessible-ui`              | None                                   |
| A `div` with `onClick` and no role or keyboard handler             | `react-and-accessible-ui`              | None                                   |
| A map or terminal component leaks its instance on unmount          | `react-and-accessible-ui`              | `browser-main-thread-performance`      |
| Process does not exit on `SIGTERM`                                 | `node-bun-and-processes`               | `typescript-async-and-concurrency`     |
| Child process spawned with a shell string from input               | `node-bun-and-processes`               | `typescript-boundaries-and-validation` |
| Package behaves differently under Bun and Node                     | `node-bun-and-processes`               | `typescript-modules-and-packaging`     |
| Renderer needs a privileged operation                              | `electron-and-ipc`                     | `typescript-boundaries-and-validation` |
| Window still runs with `nodeIntegration: true`                     | `electron-and-ipc`                     | None                                   |
| PTY output floods the renderer                                     | `electron-and-ipc`                     | `browser-main-thread-performance`      |
| Core package imports `electron` or `node:fs`                       | `arch-typescript-package-design`       | None                                   |
| Plugins receive the host's store by reference                      | `arch-typescript-package-design`       | `typescript-boundaries-and-validation` |
| Deciding what a published package should export                    | `arch-typescript-package-design`       | `typescript-modules-and-packaging`     |
| One named regression or exact output                               | `typescript-testing`                   | None                                   |
| Public type vocabulary must reject a shape                         | `typescript-testing`                   | `typescript-types-and-apis`            |
| Case table keeps growing to sample one invariant                   | `fast-check`                           | `typescript-testing`                   |
| Encoder and decoder must round-trip                                | `fast-check`                           | `typescript-data-and-state`            |
| Bug depends on a sequence of operations or an interleaving         | `fast-check`                           | `typescript-verification`              |
| Invariant must hold for every input, not sampled ones              | `typescript-verification`              | `lemmascript`                          |
| Tests pass, but a deliberate mutation survives                     | `typescript-verification`              | `typescript-testing`                   |
| Test needs `setTimeout` to settle                                  | `typescript-testing`                   | `typescript-async-and-concurrency`     |
| A scheduler must never apply a transition early                    | `typescript-verification`              | `fast-check`                           |

_Table 1: Symptoms and tasks, the skill to load, and its common pair._

## Anti-routing

- Do not load `typescript-types-and-apis` to explain a runtime `undefined`;
  the value exists at runtime, so `typescript-data-and-state` or
  `typescript-boundaries-and-validation` owns it.
- Do not load `typescript-boundaries-and-validation` for data that never
  leaves the process and was constructed by typed code; validation at an
  internal call is ceremony.
- Do not load `typescript-async-and-concurrency` for a single awaited call
  with no fan-out, cancellation, or shared state.
- Do not load `typescript-modules-and-packaging` for an application that is
  bundled and never published; only its `module` settings matter, and the types
  skill covers those.
- Do not load `effect-v4` to introduce Effect into a codebase that does not
  use it; `typescript-errors-and-outcomes` and
  `typescript-async-and-concurrency` answer the underlying question.
- Do not load `zod4-typescript` to decide where a boundary belongs; load it
  once `typescript-boundaries-and-validation` has placed the boundary and the
  question is about Zod itself.
- Do not load `react-and-accessible-ui` because the project uses React; load
  it when the pressure is component ownership, accessibility, or component
  tests. A frame-budget problem in a React application starts at
  `browser-main-thread-performance`.
- Do not load `electron-and-ipc` for renderer code that never crosses the
  bridge; it is browser code and routes as such.
- Do not load `browser-main-thread-performance` to decide whether a
  calculation is heavy enough for a worker without a trace; the skill will send
  you to measure first.
- Do not route an obvious single invariant through `typescript-verification`;
  load `fast-check` directly. The exception is an invariant of a pure function
  where a counter-example would be costly: that goes on to `lemmascript`, as
  the router's testing hierarchy says.
- Do not load `lemmascript` for what a union or a compile-time test can
  enforce, or to "prove" timeouts, cancellation, or scheduling; those belong to
  the type system and to conformance tests.
