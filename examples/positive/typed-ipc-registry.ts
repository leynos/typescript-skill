/**
 * @file Positive fixture for a typed IPC channel registry without a schema
 * library: parsers restore types on both sides of an untrusted boundary and
 * the transport owns cancellation. Compiled by `make examples` to evidence the
 * Electron skill.
 */
// Linked from skills/electron-and-ipc/SKILL.md.
//
// A typed channel registry with no schema library and no Electron import, so
// the typing can be read on its own. Each channel names a parse function for
// its request and a parse function for its response; `satisfies` checks every
// entry has both while keeping the literal channel names.

type Parser<T> = (raw: unknown) => T;

interface Channel<Req, Res> {
  readonly request: Parser<Req>;
  readonly response: Parser<Res>;
}

// Arrays are objects too; a boundary guard that admits `[]` as `{}` would let
// a malformed request pass as the advertised empty object.
function isRecord(raw: unknown): raw is Record<string, unknown> {
  return typeof raw === "object" && raw !== null && !Array.isArray(raw);
}

const parseShellRun: Parser<{ readonly command: "git" | "ls"; readonly args: readonly string[] }> = (raw) => {
  if (!isRecord(raw)) throw new TypeError("shell:run request must be an object");
  const { command, args } = raw;
  if (command !== "git" && command !== "ls") throw new TypeError("command not allowed");
  // `every` skips holes, so a sparse array such as `Array(1)` would pass; walk
  // every index instead and copy into a dense array.
  if (!Array.isArray(args)) throw new TypeError("args must be an array");
  const dense: string[] = [];
  for (let index = 0; index < args.length; index += 1) {
    const value: unknown = args[index];
    if (typeof value !== "string") throw new TypeError("args must be strings");
    dense.push(value);
  }
  return { command, args: dense };
};

const parseShellResult: Parser<{ readonly code: number; readonly stdout: string }> = (raw) => {
  if (!isRecord(raw)) throw new TypeError("shell:run response must be an object");
  const { code, stdout } = raw;
  if (typeof code !== "number" || typeof stdout !== "string") {
    throw new TypeError("shell:run response shape");
  }
  return { code, stdout };
};

const parseEmpty: Parser<Record<string, never>> = (raw) => {
  if (!isRecord(raw) || Object.keys(raw).length > 0) throw new TypeError("expected {}");
  return {};
};

const parseConfig: Parser<{ readonly fontSize: number }> = (raw) => {
  if (!isRecord(raw) || typeof raw["fontSize"] !== "number") throw new TypeError("config shape");
  return { fontSize: raw["fontSize"] };
};

export const commands = {
  "shell:run": { request: parseShellRun, response: parseShellResult },
  "config:read": { request: parseEmpty, response: parseConfig },
} satisfies Record<string, Channel<unknown, unknown>>;

export type CommandName = keyof typeof commands;
export type Request<C extends CommandName> = ReturnType<(typeof commands)[C]["request"]>;
export type Response<C extends CommandName> = ReturnType<(typeof commands)[C]["response"]>;

// A transport is whatever carries the message: ipcRenderer.invoke, a
// MessagePort, a test double. It is untyped on purpose; typing is restored by
// the parsers on each side. The transport owns cancellation: an AbortSignal
// does not cross IPC, so an Electron transport allocates a request identifier,
// sends a cancel message for it when the signal aborts, and rejects promptly
// with the signal's reason rather than waiting for the privileged operation.
export interface Transport {
  readonly invoke: (channel: string, payload: unknown, signal?: AbortSignal) => Promise<unknown>;
}

export function createInvoker(transport: Transport) {
  return async function invoke<C extends CommandName>(
    channel: C,
    request: Request<C>,
    signal?: AbortSignal,
  ): Promise<Response<C>> {
    signal?.throwIfAborted();
    const raw = await transport.invoke(channel, request, signal);
    signal?.throwIfAborted();
    return commands[channel].response(raw) as Response<C>;
  };
}

// On the main side, a handler registry has the mirror shape: validate the
// request before the handler runs, and type the handler by channel.
export type Handler<C extends CommandName> = (request: Request<C>) => Promise<Response<C>>;

export function guard<C extends CommandName>(channel: C, handler: Handler<C>) {
  return async (raw: unknown): Promise<Response<C>> => {
    const request = commands[channel].request(raw) as Request<C>;
    return handler(request);
  };
}
