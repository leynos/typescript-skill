# Streams and child processes

## Streams

```ts
import { pipeline } from "node:stream/promises";
import { createReadStream, createWriteStream } from "node:fs";
import { createGzip } from "node:zlib";

await pipeline(
  createReadStream(input),
  createGzip(),
  createWriteStream(output),
  { signal },
);
```

`pipeline` propagates errors, destroys every stage on failure, and honours
backpressure. Manual `.pipe()` does none of the first two.

- Iterate a readable with `for await (const chunk of stream)`; it pulls one
  chunk at a time.
- Set `highWaterMark` when the default (16 KiB for byte streams, 16 objects for
  object mode) is wrong for the workload.
- Convert between Node and web streams once, at the boundary where the
  web-shaped API lives (`Readable.toWeb`, `Readable.fromWeb`).
- Decode bytes to text with a `TextDecoder` or `StringDecoder` that carries
  state across chunks; a multi-byte character split across two chunks is
  otherwise corrupted.

## Child processes

```ts
import { spawn } from "node:child_process";

const maxOutputBytes = 8 * 1024 * 1024; // the budget is stated, not implied
const killGraceMs = 2_000; // how long a child may ignore SIGTERM

export async function run(
  command: string,
  args: readonly string[],
  signal: AbortSignal,
): Promise<{ readonly code: number | null; readonly signal: NodeJS.Signals | null; readonly stdout: string }> {
  const child = spawn(command, args, { stdio: ["ignore", "pipe", "pipe"], signal });
  const stdout: Buffer[] = [];
  const stderr: Buffer[] = [];
  let retained = 0;
  let escalation: ReturnType<typeof setTimeout> | undefined;
  const terminate = () => {
    if (escalation !== undefined) return; // SIGTERM already sent
    child.kill("SIGTERM");
    escalation = setTimeout(() => child.kill("SIGKILL"), killGraceMs);
  };
  const collect = (into: Buffer[]) => (chunk: Buffer) => {
    retained += chunk.byteLength;
    if (retained > maxOutputBytes) {
      terminate(); // the bound is enforced here, not after the fact
      return;
    }
    into.push(chunk);
  };
  child.stdout.on("data", collect(stdout));
  child.stderr.on("data", collect(stderr));
  const [code, exitSignal] = await new Promise<[number | null, NodeJS.Signals | null]>(
    (resolve, reject) => {
      child.once("error", reject);
      child.once("close", (c, s) => resolve([c, s]));
    },
  ).finally(() => clearTimeout(escalation));
  if (retained > maxOutputBytes) {
    throw new AppError("child-output-exceeded", `${command} exceeded ${maxOutputBytes} bytes`, {
      data: { command, maxOutputBytes },
    });
  }
  if (code !== 0) {
    throw new AppError("child-failed", Buffer.concat(stderr).toString("utf8"), {
      data: { command, code, signal: exitSignal },
    });
  }
  return { code, signal: exitSignal, stdout: Buffer.concat(stdout).toString("utf8") };
}
```

- Argument array, never a shell string. `shell: true` with interpolated input
  is a command injection.
- `signal` kills the child when the parent scope closes.
- Await `close`, which fires after stdio has drained; `exit` can fire first.
- Bound the collected output, or stream it, when the child can be verbose.
- A child may ignore `SIGTERM`. Escalate to `SIGKILL` after a stated grace
  period, and clear the timer once `close` fires, or the wait never settles.
- Classify by exit code and signal; a `null` code with a signal means the
  child was killed.

## Long-lived children

A PTY, a language server, a database: the child outlives one request. Own it in
a scope tied to the process lifecycle, restart it with a backoff on unexpected
exit, and batch its output with a time-and-size policy before forwarding it to
a renderer or a socket. A `StringDecoder` that is reset before each emit keeps
the batcher re-entrant.

## Worker threads

- Only for CPU-bound work. I/O inside a worker gains nothing and complicates
  cancellation.
- Pool with a bound (`maxQueue` in Piscina, `maxQueueSize` in `workerpool`);
  both default to unlimited.
- Transfer `ArrayBuffer`s; clone small objects; never pass functions.
- Pass `resourceLimits` when untrusted input can inflate memory.
- Terminate the pool on shutdown and wait for it.
