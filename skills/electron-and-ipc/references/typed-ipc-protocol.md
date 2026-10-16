# Typed IPC protocol

## The shared module

```ts
// shared/protocol.ts
import { z } from "zod";

export const commands = {
  "shell:run": {
    request: z.object({
      command: z.enum(["git", "ls", "pwd"]),
      args: z.array(z.string().max(256)).max(32),
      cwd: z.string().max(4096),
    }),
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
```

The `satisfies` keeps the literal channel names while checking every entry has
both schemas. The
[typed-ipc-registry.ts](../../../examples/positive/typed-ipc-registry.ts)
example shows the same shape without a schema library, so the typing can be
read on its own.

## Main side

```ts
import { ipcMain } from "electron";

export function handle<C extends CommandName>(
  channel: C,
  handler: (request: Response<C> extends never ? never : Request<C>, sender: WebFrameMain) => Promise<Response<C>>,
): void {
  ipcMain.handle(channel, async (event, raw: unknown) => {
    const parsed = commands[channel].request.safeParse(raw);
    if (!parsed.success) {
      throw new ProtocolError("invalid-request", channel, parsed.error.issues);
    }
    if (!isTrustedSender(event.senderFrame)) {
      throw new ProtocolError("untrusted-sender", channel);
    }
    try {
      return await handler(parsed.data, event.senderFrame);
    } catch (error: unknown) {
      throw toIpcError(error); // serializable, no stack
    }
  });
}
```

- Validate before touching the request.
- Check the sender frame: `senderFrame.url` against the application's own
  origin, and for per-window channels, that the frame belongs to that window.
- Electron serializes a thrown `Error` from a handler as a plain `Error` with
  only `message`; throw a serializable shape and re-wrap on the renderer side.

## Renderer side

```ts
export async function invoke<C extends CommandName>(
  channel: C,
  request: Request<C>,
  signal?: AbortSignal,
): Promise<Response<C>> {
  signal?.throwIfAborted();
  const raw: unknown = await window.app.invoke(channel, request);
  const parsed = commands[channel].response.safeParse(raw);
  if (!parsed.success) {
    throw new ProtocolError("invalid-response", channel, parsed.error.issues);
  }
  return parsed.data;
}
```

Response validation protects the renderer from a main process on a different
version (after an update with a cached renderer) and from a bug in a handler.
It is cheap relative to the IPC itself.

## Cancellation

An `AbortSignal` does not cross IPC. Carry a request identifier and send a
cancel message:

```ts
const id = nextRequestId();
signal?.addEventListener("abort", () => window.app.cancel(id), { once: true });
const raw = await window.app.invoke(channel, { id, ...request });
```

Main keeps a `Map<id, AbortController>` and aborts the controller on cancel.
Late results for cancelled identifiers are dropped on both sides.

## Events from main

Push channels (`webContents.send`) carry a payload schema too. The renderer
validates each event and ignores unknown event types with a debug log, so a
newer main can add events without breaking an older renderer.

## Versioning

Add `protocolVersion` to the handshake once main and renderer can diverge.
Reject with a message that names both versions; do not attempt to translate.
