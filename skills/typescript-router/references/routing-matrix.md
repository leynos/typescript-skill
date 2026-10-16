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
