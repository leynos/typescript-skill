# Vocabulary

Seven things that are routinely called "a worker" or "a task". Keep them apart;
each has a different owner, lifetime, and failure mode.

| Term                  | What it is                                                                  | Owner                   | Dies when                           |
| --------------------- | --------------------------------------------------------------------------- | ----------------------- | ----------------------------------- |
| Event-loop task       | One unit of work the runtime runs to completion on a thread                 | The runtime             | It returns                          |
| Microtask             | A continuation (promise reaction) run before the next task                  | The runtime             | It returns                          |
| Application scheduler | Code that decides which pending work runs next and when it yields           | The application         | The scope that created it closes    |
| Logical worker        | An orchestration owner: drains a queue of transitions, owns side effects    | The application         | The scope that created it closes    |
| Web Worker            | A separate JavaScript thread in a browser, with no DOM, talking by messages | The script that made it | `terminate()` or the page unloads   |
| Worker thread         | A separate JavaScript thread in Node or Bun, talking by messages            | The process             | `terminate()` or the process exits  |
| Process               | An operating-system process with its own memory and event loop              | The parent or the OS    | It exits or is signalled            |
| Durable job           | A unit of work recorded in a store and executed by any available runner     | The queue               | It completes, or is marked poisoned |

_Table 1: Terms that are easily conflated, with owner and lifetime._

## Why it matters

- A logical worker with virtual time, queued transitions, and drain-to-idle
  is evidence of good orchestration design. It is not evidence that a thread is
  needed. The question "should this be a Web Worker" is answered by the
  threshold in [workers-and-pools.md](workers-and-pools.md), not by the name.
- An application scheduler that batches and prioritizes on the main thread is
  often the whole fix for responsiveness. Introducing a thread adds
  serialization cost and a second failure domain.
- A durable job is the only one of these that survives a crash. Everything
  else is lost with its owner, and the design has to accept that or move up the
  table.

## Phrasing to use

- "Drain the queue" for a logical worker; "post a message" for a thread.
- "Yield" for giving the event loop a turn; "offload" for moving to a thread;
  "enqueue" for handing to a durable store.
- "Scope" for the thing that owns lifetime; "signal" for the thing that
  carries cancellation.
