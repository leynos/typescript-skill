# Cancellation, timeout, and failure

Three outcomes that reach a `catch` and need three different responses.

| Outcome      | Who decided                    | Signal                                                     | Response                                  |
| ------------ | ------------------------------ | ---------------------------------------------------------- | ----------------------------------------- |
| Cancellation | The caller                     | `AbortSignal` aborted; rejection with reason               | Clean up, stay silent, do not retry       |
| Timeout      | The code that set the deadline | `TimeoutError` from `AbortSignal.timeout` or a local timer | Clean up, maybe retry, report once        |
| Failure      | The operation                  | Any other rejection                                        | Classify, retry if retryable, report once |

_Table 1: The three outcomes and their responses._

## Propagating cancellation

```ts
export async function fetchJson(url: string, signal: AbortSignal): Promise<unknown> {
  signal.throwIfAborted();
  const response = await fetch(url, { signal });
  if (!response.ok) {
    throw new AppError("http", `${response.status} from ${url}`);
  }
  return response.json();
}
```

- Accept a `signal` parameter on every async function that does I/O or loops.
- Pass it through to every primitive that accepts one (`fetch`, timers via
  `AbortSignal.any`, streams, child processes).
- Check `signal.aborted` between chunks of CPU work.
- Reject with `signal.reason`, not a fresh error, so the caller sees its own
  reason come back.

Combine a caller's signal with a deadline using
`AbortSignal.any([signal, AbortSignal.timeout(ms)])`. The rejection's `name`
then tells you which one fired: `AbortError` for the caller, `TimeoutError` for
the deadline.

## Timeouts that clean up

`Promise.race([work, delay(ms)])` leaves `work` running after the race is lost.
Prefer a signal-based timeout so the underlying operation is told to stop.
Where the primitive cannot be aborted, document that the timeout only abandons
the result, and make sure the abandoned promise has a rejection handler so it
does not become an unhandled rejection later.

## Shutdown

During shutdown every in-flight operation is cancelled. Errors that arrive
after the shutdown signal are expected and should be logged at debug level or
not at all. The entry point sets a flag or aborts a root signal; handlers check
it before reporting.

## Retry classification

Retry only what is retryable: timeouts, connection resets, 429 and 503 with a
`Retry-After`, lock contention. Never retry cancellation, validation failures,
or 4xx responses other than 408 and 429. Make the classification a function of
the error's `code` and keep it beside the error class so the two evolve
together.
