# Routing scenarios

The router's evaluation set. Each row is a request drawn from the estate, the
primary skill the router should load, the companion it should usually add, and
what the answer looks like. `tests/test_routing_scenarios.py` checks that every
cell names a shipped skill and that the six scenarios the design brief used
keep their route.

## Scenarios

| Scenario                                                                         | Primary skill                          | Companion skill                        | Shape of the answer                                                                                                                                 |
| -------------------------------------------------------------------------------- | -------------------------------------- | -------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| Parsing a large GeoJSON payload freezes Wildside                                 | `browser-main-thread-performance`      | `typescript-async-and-concurrency`     | Name the number (long task), check elimination (do we need all features now?), then a worker with transfer and a stale-result guard                 |
| Make Simulacat's ESM/CJS exports pass consumer checks                            | `typescript-modules-and-packaging`     | `arch-typescript-package-design`       | Add `types` to each condition block, keep `development` out of the published map, run `publint`, `attw`, and a packed install                       |
| Prove DigitalPuddle never applies a transition before its virtual timestamp      | `typescript-verification`              | `fast-check`                           | Model-based commands over schedule and advance; escalate to `lemmascript` only if the drain is a pure kernel and the cost of a miss is severe       |
| Add a privileged Velocetty command                                               | `electron-and-ipc`                     | `typescript-boundaries-and-validation` | A shared request and response schema, validation and sender check in main, an allowlist for the dangerous arguments, a bridge method in preload     |
| Introduce exact optional properties into Velocetty                               | `typescript-types-and-apis`            | None                                   | Brownfield mode: a per-directory ratchet starting with `frontend/`, `backend/`, and `shared/`, never a repository-wide flip                         |
| Prevent direct style toggles in Wildside                                         | `typescript-quality-tools`             | `browser-main-thread-performance`      | `prefer-css-state` in the browser preset as a warning, with the reference mockups excluded and the geometry adapters allowed                        |
| A split-pane drag writes `left` on every pointer move                            | `browser-main-thread-performance`      | None                                   | Keep the imperative write but through a `--split-position` custom property the stylesheet consumes; it is a named exception, not a violation        |
| Corbusier navigates one frame after closing a dialog                             | `react-and-accessible-ui`              | None                                   | Leave it; a one-shot `requestAnimationFrame` before navigation is an interoperability fix, not an animation loop                                    |
| Velocetty's PTY output stutters the terminal                                     | `electron-and-ipc`                     | `browser-main-thread-performance`      | Batch in main by time and size, coalesce per frame in the renderer, add acknowledgement-based backpressure if the source can pause                  |
| Simulacat's generated resolver types are both ignored and tracked                | `typescript-modules-and-packaging`     | None                                   | Pick tracked-and-never-edited with a `generate:check` diff in CI, and fix the index                                                                 |
| DigitalPuddle's store calls `new Date()` in a transition                         | `typescript-data-and-state`            | `typescript-testing`                   | Inject a `Clock` port, add the same-seed double-run gate                                                                                            |
| Velocetty's main handler passes a shell command through unvalidated              | `electron-and-ipc`                     | `typescript-boundaries-and-validation` | Request schema with an enum of allowed commands, sender check, log the decision                                                                     |
| Corbusier's fixture data is parsed with valibot but `localStorage` is not        | `typescript-boundaries-and-validation` | `typescript-data-and-state`            | A versioned schema for the stored shape; discard and reset on failure                                                                               |
| Velocetty runs type checks through a January native-preview build                | `typescript-7-transition`              | `typescript-modules-and-packaging`     | Move to the released compiler, alias the 6.0 package for the library consumers, replace `moduleResolution: node` in the Electron main configuration |
| Simulacat keeps `ignoreDeprecations: "6.0"` after upgrading                      | `typescript-7-transition`              | None                                   | Find what it silences, fix the option, delete the setting                                                                                           |
| A transition table in a test keeps gaining rows that vary only in attempt count  | `fast-check`                           | `typescript-testing`                   | Keep the table for the meaningful cells; move "attempts never exceed three" to a property                                                           |
| A new `.test-d.ts` file is added outside the type-check `include` (hypothetical) | `typescript-testing`                   | `typescript-types-and-apis`            | Include it in the type-check configuration so the `@ts-expect-error` markers are compiled                                                           |
| Velocetty's `catch` blocks log at every layer                                    | `typescript-errors-and-outcomes`       | None                                   | One classified log at the entry point; libraries throw or return                                                                                    |
| A Node service does not exit on `SIGTERM` in the container                       | `node-bun-and-processes`               | `typescript-async-and-concurrency`     | Signal handler aborts a root signal, drains with a deadline, sets the exit code                                                                     |
| Simulacat's Biome config turns `noExplicitAny` off while `tsc` is strict         | `typescript-quality-tools`             | `typescript-types-and-apis`            | One owner for `any`: let the compiler's `noImplicitAny` and a suppression count carry it, and re-enable the lint rule per directory                 |
| Wildside's semantic CI step is commented out                                     | `typescript-quality-tools`             | None                                   | Re-enable with the noisy rule as a warning, or delete the job and the config                                                                        |
| A team wants to introduce Effect to fix one retry loop                           | `typescript-errors-and-outcomes`       | `typescript-async-and-concurrency`     | Decline the framework for one path; classify the error and bound the retry. `effect-v4` is for codebases already on Effect                          |

_Table 1: Estate scenarios, the route the router should take, and the shape of
the answer._

## Reading the table

- The primary skill is the one whose decision surface explains the pressure.
  The companion is the usual second load; `None` means the primary carries the
  whole answer.
- Where a scenario could plausibly route two ways, the table records the
  choice and the reason sits in the last column. A reviewer who disagrees edits
  the row and the pinned test together.
- Scenarios are drawn from
  [the source inventory](source-inventory.md); a scenario that no longer
  matches the estate should be retired rather than kept for symmetry.
