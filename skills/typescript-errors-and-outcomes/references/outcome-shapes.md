# Outcome shapes

## A minimal result type

```ts
export type Result<T, E> =
  | { readonly ok: true; readonly value: T }
  | { readonly ok: false; readonly error: E };

export const ok = <T>(value: T): Result<T, never> => ({ ok: true, value });
export const err = <E>(error: E): Result<never, E> => ({ ok: false, error });
```

Use it when the failure is part of the contract and the caller must branch. Keep
`E` a discriminated union, never `string`:

```ts
type ParseError =
  | { readonly code: "empty" }
  | { readonly code: "invalid-field"; readonly path: readonly string[]; readonly reason: string };
```

The code is what callers switch on; the rest is what humans read.

## When to throw instead

- The failure means the program is wrong, not the input: a missing
  dependency, an impossible state, a violated invariant.
- No caller can recover, so a result would be unwrapped and rethrown at every
  level anyway.
- The function is deep inside an operation that a boundary already wraps, and
  the boundary classifies by `code`.

```ts
export class AppError extends Error {
  override readonly name = "AppError";
  constructor(
    readonly code: AppErrorCode,
    message: string,
    options?: { readonly cause?: unknown; readonly data?: Record<string, unknown> },
  ) {
    super(message, { cause: options?.cause });
    this.data = options?.data;
  }
  readonly data: Record<string, unknown> | undefined;
}
```

One class per package, discriminated by `code`. The `cause` carries the foreign
error; the `data` carries structured context a log line can render.

## Classifying `unknown`

```ts
export function classify(error: unknown): AppError {
  if (error instanceof AppError) return error;
  if (isAbortError(error)) return new AppError("cancelled", "operation cancelled", { cause: error });
  if (error instanceof Error) return new AppError("unexpected", error.message, { cause: error });
  return new AppError("unexpected", String(error), { data: { thrown: error } });
}
```

Call it once at the boundary that owns the `catch`. `isAbortError` checks
`name === "AbortError"` rather than `instanceof DOMException`, because the
class differs between runtimes and realms.

## Result or exception at a boundary

| Situation                                  | Shape                            |
| ------------------------------------------ | -------------------------------- |
| Parsing untrusted input                    | `Result` with issue list         |
| Lookup that may miss                       | `T \| undefined`                 |
| Operation that may be cancelled            | Rejection with the abort reason  |
| Operation that may time out                | Rejection with `TimeoutError`    |
| Violated invariant                         | Throw `AppError("invariant")`    |
| Network or I/O failure inside a retry loop | Throw; the loop classifies       |
| Network or I/O failure at the top level    | Return `Result` to the caller UI |

_Table 1: Which outcome shape fits which situation._

## Libraries

`neverthrow`, `true-myth`, `effect`, and others ship a `Result`. Use one if the
codebase already has it; the ten-line type above is otherwise enough, and it
keeps the vocabulary local.
