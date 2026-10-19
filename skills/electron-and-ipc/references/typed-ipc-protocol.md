# Typed IPC protocol

## The shared module

```ts
// shared/protocol.ts
import { z } from "zod";

// Privileged operations are named individually. An allowlist of command names
// alone does not confine `git`: it takes `-c` configuration, aliases that run
// shell commands, and subcommands with their own side effects.
export const commands = {
  "shell:run": {
    request: z.discriminatedUnion("operation", [
      z.object({ operation: z.literal("git-status"), cwd: z.string().max(4096) }),
      z.object({
        operation: z.literal("git-log"),
        cwd: z.string().max(4096),
        limit: z.number().int().min(1).max(500),
      }),
      z.object({ operation: z.literal("list-directory"), cwd: z.string().max(4096) }),
    ]),
    response: z.object({ code: z.number().int(), stdout: z.string() }),
  },
  "config:read": {
    request: z.object({}),
    response: ConfigSchema,
  },
} satisfies Record<string, { request: z.ZodType; response: z.ZodType }>;

export type CommandName = keyof typeof commands;
export type Request<C extends CommandName> = z.input<(typeof commands)[C]["request"]>;
export type Response<C extends CommandName> = z.output<(typeof commands)[C]["response"]>;

// Every message carries a request identifier so cancellation can find it, and
// every reply is a discriminated payload: Electron forwards only `message`
// from a thrown error, so a thrown `ErrorDto` would lose its code and cause.
export const Envelope = z.object({ id: z.string().uuid(), payload: z.unknown() });
export type Reply<T> =
  | { readonly ok: true; readonly value: T }
  | { readonly ok: false; readonly error: ErrorDto };
```

The handler maps each `operation` to a fixed argument vector
(`["status", "--porcelain"]`, `["log", "--max-count", String(limit)]`) and
authorizes `cwd` against the directories the window may touch before anything
runs. The `satisfies` keeps the literal channel names while checking every
entry has both schemas. The
[typed-ipc-registry.ts](../../../examples/positive/typed-ipc-registry.ts)
example shows the same shape without a schema library, so the typing can be
read on its own.

## Main side

```ts
import { ipcMain } from "electron";

const inFlight = new Map<string, AbortController>();

export function handle<C extends CommandName>(
  channel: C,
  handler: (
    request: Request<C>,
    context: { readonly sender: WebFrameMain; readonly signal: AbortSignal },
  ) => Promise<Response<C>>,
): void {
  ipcMain.handle(channel, async (event, raw: unknown): Promise<Reply<Response<C>>> => {
    const envelope = Envelope.safeParse(raw);
    if (!envelope.success) {
      return { ok: false, error: toErrorDto(new ProtocolError("invalid-envelope", channel)) };
    }
    const parsed = commands[channel].request.safeParse(envelope.data.payload);
    if (!parsed.success) {
      return {
        ok: false,
        error: toErrorDto(new ProtocolError("invalid-request", channel, parsed.error.issues)),
      };
    }
    if (!isTrustedSender(event.senderFrame)) {
      return { ok: false, error: toErrorDto(new ProtocolError("untrusted-sender", channel)) };
    }
    const controller = new AbortController();
    inFlight.set(envelope.data.id, controller);
    try {
      const value = await handler(parsed.data, {
        sender: event.senderFrame,
        signal: controller.signal,
      });
      return { ok: true, value };
    } catch (error: unknown) {
      return { ok: false, error: toErrorDto(error) }; // serializable, no stack
    } finally {
      inFlight.delete(envelope.data.id);
    }
  });
}

ipcMain.on("request:cancel", (event, id: unknown) => {
  if (typeof id === "string" && isTrustedSender(event.senderFrame)) {
    inFlight.get(id)?.abort();
  }
});
```

- Validate the envelope, then the payload, before touching the request. Zod
  object parsing strips unknown keys, so `id` lives in the envelope rather than
  beside the payload's fields.
- Check the sender frame: `senderFrame.url` against the application's own
  origin, and for per-window channels, that the frame belongs to that window.
- Return the error as data. Electron serializes a thrown `Error` from a handler
  as a plain `Error` carrying only `message`, so a thrown `ErrorDto` arrives
  without its `code` or `cause`.
- Register the `AbortController` before the handler starts and remove it when
  the handler settles, so a cancel message can always find a running operation
  and a late cancel finds nothing.

## Renderer side

```ts
export async function invoke<C extends CommandName>(
  channel: C,
  request: Request<C>,
  signal?: AbortSignal,
): Promise<Response<C>> {
  signal?.throwIfAborted();
  const id = crypto.randomUUID();
  const raw: unknown = await cancellable(
    signal,
    id,
    window.app.invoke(channel, { id, payload: request }),
  );
  const reply = replySchema(commands[channel].response).safeParse(raw);
  if (!reply.success) {
    throw new ProtocolError("invalid-response", channel, reply.error.issues);
  }
  if (!reply.data.ok) {
    throw fromErrorDto(reply.data.error);
  }
  return reply.data.value;
}
```

`replySchema(response)` is
`z.discriminatedUnion("ok", [{ ok: true, value:
response }, { ok: false, error: ErrorDtoSchema }])`.
Response validation protects the renderer from a main process on a different
version (after an update with a cached renderer) and from a bug in a handler.
It is cheap relative to the IPC itself.

## Cancellation

An `AbortSignal` does not cross IPC. Carry the request identifier, send a
cancel message when the signal aborts, and reject at once rather than waiting
for main to finish the privileged operation. Checking `signal.aborted` only
before and after the `await` is not cancellation: the operation runs to
completion and the caller merely learns late.

```ts
function cancellable<T>(
  signal: AbortSignal | undefined,
  id: string,
  result: Promise<T>,
): Promise<T> {
  if (!signal) return result;
  return new Promise<T>((resolve, reject) => {
    const onAbort = () => {
      window.app.cancel(id);
      reject(signal.reason);
    };
    signal.addEventListener("abort", onAbort, { once: true });
    result.then(
      (value) => {
        signal.removeEventListener("abort", onAbort);
        resolve(value);
      },
      (error: unknown) => {
        signal.removeEventListener("abort", onAbort);
        reject(error);
      },
    );
  });
}
```

The listener is removed in both branches of `then` rather than in a trailing
`finally`: `finally` returns a new promise, and when `result` rejects that
promise rejects too, unobserved, which is an unhandled rejection even though
the caller handled `cancellable(...)`. Main aborts the registered controller on
`request:cancel` and the handler observes `context.signal`. Late results for
cancelled identifiers are dropped on both sides. The
[typed-ipc-registry.ts](../../../examples/positive/typed-ipc-registry.ts)
example keeps the same contract one level down: its `Transport` receives the
signal, and an Electron-backed transport implements it this way.

## Events from main

Push channels (`webContents.send`) carry a payload schema too. The renderer
validates each event and ignores unknown event types with a debug log, so a
newer main can add events without breaking an older renderer.

## Versioning

Add `protocolVersion` to the handshake once main and renderer can diverge.
Reject with a message that names both versions; do not attempt to translate.
