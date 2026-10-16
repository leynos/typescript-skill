---
name: typescript-errors-and-outcomes
description: Use for failure handling in TypeScript and JavaScript, including thrown errors versus explicit outcomes, unknown catches, error causes, cancellation versus timeout versus failure, cross-process error serialization, and which layer logs.
metadata:
  globs: "**/*.ts, **/*.tsx, **/*.mts, **/*.cts, **/*.js, **/*.mjs, **/*.cjs"
---

# TypeScript errors and outcomes

Use this when the question is what happens when something goes wrong: how the
failure is represented, who classifies it, who reports it, and whether "wrong"
was a failure at all.

## Working stance

- Distinguish three things that `catch` lumps together: expected outcomes a
  caller must handle, programmer errors that should crash loudly, and
  interruptions such as cancellation and timeout that are neither.
- Expected outcomes are values. Return them. A parse that can fail returns a
  result; a lookup that can miss returns `undefined` or a variant.
- Programmer errors throw. A violated invariant, an impossible state, a
  missing dependency: throw an `Error` with a message that names the invariant,
  and let it crash the unit of work.
- Catch at the boundary that can do something: retry, translate, report, or
  degrade. Every other layer lets errors pass. Catch-log-rethrow at each layer
  produces one failure logged five times.
- `catch (error: unknown)` is the only honest signature. Classify before use.
- Cancellation is not failure. A rejected promise whose reason is an
  `AbortError` means "the caller changed its mind", and no alarm should sound.

## Decision surface

- **Thrown versus returned.** Return an outcome when the caller is expected to
  branch on it and the failure is part of the function's contract. Throw when
  the caller cannot reasonably continue. A function that returns `Result` for
  one failure and throws for another documents both. See
  [outcome-shapes.md](references/outcome-shapes.md).
- **Error classes.** One base error per package with a `code` discriminant and
  a `cause`. Subclass sparingly; a `code` union carries more information than a
  class hierarchy and survives serialization. Wrap foreign errors with
  `new AppError("code", { cause })` so the chain is preserved.
- **Causes.** `Error.prototype.cause` is standard; set it. Never string-
  concatenate the inner message into the outer one; loggers print the chain.
- **Cancellation, timeout, failure.** Three distinct outcomes with three
  distinct handlers. Cancellation propagates `AbortSignal.reason`; timeout is a
  `TimeoutError` created by the code that set the deadline; failure is
  everything else. See
  [cancellation-timeout-failure.md](references/cancellation-timeout-failure.md).
- **Serialization.** An `Error` crosses JSON as `{}`. Define a wire shape
  `{ name, code, message, cause?, data? }`, serialize at the sending edge, and
  re-wrap on receipt. Never send stack traces to an untrusted peer. See
  [serializing-errors.md](references/serializing-errors.md).
- **Logging ownership.** The layer that handles an error logs it, once, with
  the chain. Libraries do not log; they return or throw. Entry points (request
  handlers, command handlers, message loops) own the final `catch` and the log
  line.
- **Effect.** When a codebase has adopted Effect, errors are typed in the
  effect's signature and the choices above are made by the library. Route to
  [`effect-v4`](../effect-v4/SKILL.md) for Effect-specific error design; do not
  introduce Effect to fix one error path.

## Red flags

- `catch (e) { console.log(e) }` with no rethrow and no return.
- `catch (e: any)` or `e.message` on an unclassified catch variable.
- `throw "string"` or `throw { code: 1 }`; only `Error` instances carry
  stacks and causes.
- The same failure logged at more than one layer.
- A timeout implemented as `Promise.race` with no cleanup of the loser.
- An `AbortError` reported as a crash, or a crash swallowed because it
  happened during shutdown.
- A `Result` type whose error branch is `string`.
- `error instanceof MyError` across a realm, worker, or IPC boundary, where
  the class identity does not survive.
- An error serializer that includes the stack in a response body.

## Pairing

- Pair with `typescript-boundaries-and-validation` for what a failed parse
  returns.
- Pair with `typescript-async-and-concurrency` when cancellation and
  `AbortSignal` propagation are the question.
- Pair with `electron-and-ipc` or `node-bun-and-processes` for where the
  final `catch` and the exit code live.
