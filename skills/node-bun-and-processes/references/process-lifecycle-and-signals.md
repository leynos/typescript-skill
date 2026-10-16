# Process lifecycle and signals

## The entry point

```ts
async function main(): Promise<number> {
  const root = new AbortController();
  const shutdown = (signal: NodeJS.Signals) => {
    log.info("shutting down", { signal });
    root.abort(new ShutdownSignal(signal));
  };
  process.once("SIGTERM", shutdown);
  process.once("SIGINT", shutdown);

  const server = await startServer({ signal: root.signal });
  await server.closed; // resolves after drain or deadline
  return server.drainedCleanly ? 0 : 1;
}

process.on("unhandledRejection", (reason) => {
  log.fatal("unhandled rejection", { error: classify(reason) });
  process.exitCode = 70;
  process.exit();
});

main().then(
  (code) => {
    process.exitCode = code;
  },
  (error: unknown) => {
    log.fatal("startup failed", { error: classify(error) });
    process.exitCode = 1;
  },
);
```

- The entry point is the only place that reads signals, sets `exitCode`, and
  calls `process.exit`.
- Setting `process.exitCode` and returning lets pending I/O (log flush) finish;
  `process.exit()` is for the cases where the process must not continue.
- `once`, not `on`: a second signal during shutdown should fall through to the
  default behaviour (terminate), which is what an operator sending it twice
  expects.

## Draining

1. Stop accepting new work: `server.close()`, stop consuming the queue,
   unsubscribe from the message bus.
2. Abort the root signal so in-flight work stops at its next check.
3. Wait for in-flight work with a deadline (`AbortSignal.timeout`), then
   proceed regardless.
4. Flush logs and metrics, close database pools, remove temporary files.
5. Exit with a code that says whether the drain completed.

Container orchestrators typically allow 30 s between `SIGTERM` and `SIGKILL`.
Budget the drain inside that, and make the deadline configurable.

## Exit codes

| Code  | Meaning                                                                                                                 |
| ----- | ----------------------------------------------------------------------------------------------------------------------- |
| 0     | Success                                                                                                                 |
| 1     | Generic failure                                                                                                         |
| 2     | Usage error (bad arguments)                                                                                             |
| 64–78 | BSD `sysexits` values, if the project uses them (`70` software error, `75` temporary failure, `78` configuration error) |
| 130   | Terminated by `SIGINT` (128 + 2)                                                                                        |
| 143   | Terminated by `SIGTERM` (128 + 15)                                                                                      |

_Table 1: Exit codes and their conventional meanings._

Pick a scheme, document it in the CLI's help, and test it.

## Unhandled rejections and exceptions

Node's default since version 15 is to terminate on an unhandled rejection. Keep
that behaviour: log once with the classified error, set a non-zero code, exit.
A handler that swallows the event keeps a process alive in an unknown state.
`uncaughtException` is the same: log, exit. Any cleanup here must be
synchronous and quick.

## Timers and keep-alive

A process stays alive while a timer, socket, or handle is referenced. Use
`timer.unref()` for background timers that should not hold the process open,
and track every interval so shutdown can clear it. A process that "hangs on
exit" has an unreferenced handle somewhere; `process.getActiveResourcesInfo()`
names it.

## Health and readiness

A server exposes readiness (can accept work) separately from liveness (is
running). During drain, readiness goes false first so the load balancer stops
routing, then connections close. Both endpoints read state owned by the
lifecycle code, not by handlers.
