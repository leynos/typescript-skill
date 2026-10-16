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

function isRecord(raw: unknown): raw is Record<string, unknown> {
  return typeof raw === "object" && raw !== null;
}

const parseShellRun: Parser<{ readonly command: "git" | "ls"; readonly args: readonly string[] }> = (raw) => {
  if (!isRecord(raw)) throw new TypeError("shell:run request must be an object");
  const { command, args } = raw;
  if (command !== "git" && command !== "ls") throw new TypeError("command not allowed");
  if (!Array.isArray(args) || !args.every((a) => typeof a === "string")) {
    throw new TypeError("args must be strings");
  }
  return { command, args };
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
// the parsers on each side.
export interface Transport {
  readonly invoke: (channel: string, payload: unknown) => Promise<unknown>;
}

export function createInvoker(transport: Transport) {
  return async function invoke<C extends CommandName>(
    channel: C,
    request: Request<C>,
    signal?: AbortSignal,
  ): Promise<Response<C>> {
    signal?.throwIfAborted();
    const raw = await transport.invoke(channel, request);
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
