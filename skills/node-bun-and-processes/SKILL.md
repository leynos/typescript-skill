---
name: node-bun-and-processes
description: Use for Node and Bun process code in TypeScript and JavaScript, including process lifecycle, signals and shutdown, streams, bounded concurrency, child processes, worker threads, native modules, CLI behaviour, Node and Bun compatibility, and persistent background work.
metadata:
  globs: "**/*.ts, **/*.mts, **/*.cts, **/*.js, **/*.mjs, **/*.cjs, **/bunfig.toml, **/package.json"
---

# Node, Bun, and processes

Use this when the code is a process: a server, a CLI, a worker, a build script,
or a daemon. The questions are how it starts, how it stops, how it talks to the
operating system and to child processes, and which runtime semantics it may
rely on.

## Working stance

- A process has a lifecycle: start, serve, drain, exit. Each phase is explicit
  code, and the exit code says what happened.
- Shutdown is a feature. `SIGTERM` and `SIGINT` stop accepting work, abort a
  root signal, wait for in-flight work with a deadline, flush logs, and exit. A
  process that is killed because it did not exit is a process with a bug.
- Streams carry backpressure; buffers do not. Pipe with `pipeline`, iterate
  with `for await`, and never collect an unbounded stream into an array.
- Child processes and worker threads are owned like promises: started with a
  signal, awaited or terminated, and never left to outlive their parent.
- Node and Bun agree on most of the standard library and disagree at the
  edges. Pin the runtime a package supports and test on it; do not assume.
- A CLI is a user interface. Exit codes, stderr versus stdout, `--help`, and
  machine-readable output are its contract.

## Decision surface

- **Lifecycle.** One entry point installs signal handlers, creates the root
  `AbortController`, starts the server or job, and owns the final `catch`.
  Libraries never call `process.exit`. See
  [process-lifecycle-and-signals.md](references/process-lifecycle-and-signals.md).
- **Unhandled failures.** `unhandledRejection` and `uncaughtException` handlers
  log once and exit non-zero; they do not keep a corrupted process alive. Route
  the error classification to `typescript-errors-and-outcomes`.
- **Streams.** `node:stream/promises` `pipeline` for Node streams, web streams
  where the API is web-shaped (`fetch`, `Response`), and an explicit
  `highWaterMark` when memory matters. Convert at one boundary, not everywhere.
  See
  [streams-and-child-processes.md](references/streams-and-child-processes.md).
- **Child processes.** `spawn` with an argument array, never a shell string
  built from input. Pass `signal`, consume `stdout` and `stderr` as streams,
  await `close` not `exit`, and classify the exit code and signal.
- **Worker threads.** For CPU-bound work only; Node already parallelizes I/O.
  Use a pool with a bounded queue (Piscina or `workerpool`), transfer large
  buffers, and terminate on shutdown. The threshold and matrix are in the
  [async skill](../typescript-async-and-concurrency/references/workers-and-pools.md).
- **Native modules.** Wrap each in one adapter that handles load failure with
  a clear message, validates results, and documents the rebuild step. Pin the
  runtime ABI the binary was built for.
- **Node versus Bun.** Prefer `node:` APIs that both support; isolate
  runtime-specific APIs (`Bun.serve`, `Bun.file`, `node:cluster`) behind one
  adapter. Watch the known divergences in
  [node-bun-compatibility.md](references/node-bun-compatibility.md).
- **CLI behaviour.** Parse arguments with a typed parser, print usage on
  misuse to stderr with exit code 2, write results to stdout and diagnostics to
  stderr, support `--json` or similar for machines, and respect `NO_COLOR` and
  a non-TTY stdout. See [cli-behaviour.md](references/cli-behaviour.md).
- **Persistent background work.** In-process timers and loops die with the
  process. If the work must survive, it belongs in a durable queue; if it must
  merely continue while the process lives, it is a logical worker with a scope
  tied to the lifecycle.

## Red flags

- `process.exit()` inside a library, a handler, or a `catch` that is not the
  entry point.
- No `SIGTERM` handler, or a handler that calls `process.exit` immediately
  without draining.
- `exec` or `execSync` with a template string that includes user input.
- `child.stdout.on("data", push)` into an array with no bound.
- A worker thread doing `fetch` or database calls.
- `fs.readFileSync` of a large file on a server's request path.
- A native module whose load failure produces a stack trace instead of a
  message naming the rebuild command.
- A CLI that prints errors to stdout, or exits zero after a failure.
- `#!/usr/bin/env node` on a `bin` that only runs under Bun, or the reverse.

## Pairing

- Pair with `typescript-async-and-concurrency` for ownership, bounding, and
  the worker threshold.
- Pair with `typescript-errors-and-outcomes` for exit codes and the final
  `catch`.
- Pair with `typescript-modules-and-packaging` for `bin` entries, `exports`,
  and runtime resolution differences.
- Pair with `electron-and-ipc` when the process is an Electron main process.
