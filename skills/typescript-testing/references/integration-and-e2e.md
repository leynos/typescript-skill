# Integration, end-to-end, and packed-package tests

These tests leave the hierarchy because the failure they catch depends on a
real boundary: a service, a process, a browser, or a consumer's install.

## Integration

| Boundary        | Realistic double                                                                  | Tag and cadence                |
| --------------- | --------------------------------------------------------------------------------- | ------------------------------ |
| Database        | Real engine in a container, or an in-process engine (SQLite) with the same schema | `integration`; pull requests   |
| HTTP dependency | A recorded fixture server, or a stateful mock engine                              | `integration`; pull requests   |
| File system     | A temporary directory                                                             | Fast enough for the unit loop  |
| Child process   | The real binary with a fixture input                                              | `integration`; pull requests   |
| Message queue   | A real broker in a container                                                      | `integration`; nightly if slow |

_Table 1: Integration boundaries and the double for each._

One real boundary per test. Two real boundaries in one test is an end-to-end
test with a worse name.

## Stateful mock engines

A stateful mock of a remote API (a simulated cloud provider, a fake Git host)
is a product in its own right: it has entities, commands, a store, and a
capability manifest saying which operations are handled, worker-backed,
fixture-only, or not implemented. Test such an engine with:

- named examples per operation;
- fast-check properties for store invariants (keys are unique, relays preserve
  order);
- a compile-time test for the capability vocabulary;
- a determinism gate when it has a virtual clock.

## End-to-end

- **Browser.** Playwright on one representative viewport per class (a phone,
  a desktop), Chromium by default, more browsers when a defect demands it. An
  accessibility scan (`@axe-core/playwright`) on each key screen, excluding
  only elements with a stated reason, and accessibility-tree snapshots so a
  regression in names or roles is a visible diff.
- **Electron.** Playwright's Electron support launches the packaged or
  development build, drives the renderer, and can call into main. A fast smoke
  (launch, open a window, run a command, quit cleanly) runs on every push; the
  deep suite runs on pull requests with one worker.
- **Flakes.** Quarantine with an issue and a `fixme` annotation; do not raise
  retries. A flaky end-to-end test is a bug in the application, the test, or
  the environment, and each has an owner.
- **Containers.** When the host cannot run browsers, a container with the
  Playwright image runs the suite with the repository mounted; the script that
  chooses between host and container is part of the repository.

## Packed-package tests

For a published package, the artefact is the product. `npm pack`, install the
tarball into a scratch project, import from ESM, CJS, and TypeScript, run the
`bin`, and type-check a consumer fixture. Route the details to
`typescript-modules-and-packaging`.

## Benchmarks

A benchmark is a test whose assertion is a threshold on a measurement. Keep:

- a synthetic, deterministic load;
- a headless or representative environment named in the script;
- thresholds with units (long-frame ratio below 0.05, p95 input latency below
  24 ms);
- a baseline recorded in the repository so a change is a diff.

Run on a schedule or on demand; variance makes them poor pull-request gates
unless the margin is wide.

## Tagging and cadence

| Suite                                        | Trigger                | Budget   |
| -------------------------------------------- | ---------------------- | -------- |
| Unit, compile-time                           | Every save, every push | Seconds  |
| Properties (default runs)                    | Every push             | Seconds  |
| Integration                                  | Pull request           | Minutes  |
| End-to-end smoke                             | Every push             | A minute |
| End-to-end deep                              | Pull request           | Minutes  |
| Properties (long runs), mutation, benchmarks | Nightly                | Hours    |

_Table 2: Suites, when they run, and how long they may take._
