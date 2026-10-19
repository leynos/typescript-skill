# Workers and pools

## Threshold for leaving the thread

Move work off the hosting thread when all of these hold:

- the work does not touch the DOM or other thread-affine state;
- it is large enough to amortize worker startup and message serialization;
- the API can be coarse-grained: one message in, one result out, not a chatty
  call per element;
- queue depth is bounded and the policy for a full queue is stated;
- cancellation and worker termination are explicit;
- large buffers are transferred, not copied;
- a stale result cannot overwrite newer state (carry a request identifier and
  drop results for superseded requests).

The threshold is semantic, not a millisecond count. A 5 ms task that runs ten
thousand times is a batching problem; a 300 ms `JSON.parse` that runs once per
navigation is a worker problem; a 300 ms task that runs once per session may
not be worth a worker at all.

## Abstraction matrix

| Abstraction            | Best fit                                                  | Required warning                                                                                                                                      |
| ---------------------- | --------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| Raw Web Worker         | Precise protocol control or a very small worker surface   | The application owns request identifiers, errors, cancellation, transfer, shutdown, and bundler wiring.                                               |
| Comlink                | A coarse async object or RPC API in a browser worker      | It removes `postMessage` plumbing but must not make remote calls look cheap. Every call is a message; it supplies no pool.                            |
| `workerpool`           | A local executor across browser and Node                  | Set a finite `maxQueueSize`; the default is `Infinity`. Pin `workerType` rather than relying on `auto`; `transfer` is unsupported for `process` type. |
| Piscina                | Node CPU-bound worker-thread pools                        | Do not move async I/O into a worker; Node already parallelizes it. Set `maxQueue`; it is unlimited by default. Abortable tasks cannot share a thread. |
| Durable queue/workflow | Work that must survive a tab, process, deploy, or machine | Requires idempotency, persistence, retry policy, deduplication, versioning, observability, and poison-job handling.                                   |

_Table 1: Off-thread abstractions, their fit, and the warning each carries._

Versions checked on 2026-10-16: Comlink 4.4.2, `workerpool` 10.0.3, Piscina
5.3.2. Recheck the defaults when the major version changes.

## Protocol shape for a raw worker

```ts
type Request = { readonly id: number; readonly kind: "parse"; readonly buffer: ArrayBuffer };
type Response =
  | { readonly id: number; readonly ok: true; readonly result: Parsed }
  | { readonly id: number; readonly ok: false; readonly error: ErrorDto };
```

Validate on receipt on both sides, carry the `id`, transfer the buffer
(`worker.postMessage(request, [request.buffer])`), and keep a
`Map<id, { resolve, reject, signal }>` on the main side so an aborted request
drops its result. Terminate the worker on scope close.

## Durable options

A reference inventory rather than a recommendation. Choose by the guarantees
required, not by popularity.

| Option          | Backing store   | Guarantee shape                                  |
| --------------- | --------------- | ------------------------------------------------ |
| BullMQ          | Redis           | Queues, delayed and repeatable jobs, flows       |
| pg-boss         | PostgreSQL      | Queues with transactional enqueue, retries, cron |
| Graphile Worker | PostgreSQL      | Lightweight tasks, `LISTEN`/`NOTIFY` wake-up     |
| Temporal        | Its own service | Durable workflows with replayed code and timers  |

_Table 2: Durable job and workflow options and their guarantee shapes._

Every durable option assumes idempotent handlers: a job will run more than once
under failure. Design the handler for that before choosing the store.
