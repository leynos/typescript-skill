<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/platform-bun/BunStream` v3 → v4

- `BunStream.FromReadableOptions` ->
  `Pick<Parameters<typeof BunStream.fromReadable>[0], "chunkSize" | "closeOnDone">`:
  The named interface was inlined into the constructor options; chunkSize is
  now a number and the full options also contain evaluate and onError. The
  ignored bufferSize option was removed.
- `BunStream.FromWritableOptions` ->
  `Pick<Parameters<typeof BunSink.fromWritable>[0], "endOnDone" | "encoding">`:
  The named interface was inlined into BunSink.fromWritable and duplex
  constructor options.
- `BunStream.stderr` -> `stdio.stderr() from Stdio.Stdio`: Standard error is
  correctly modeled as a Sink in v4. Explicitly adapt process.stderr with
  BunStream.fromReadable only to preserve the old unusual read behavior.
- `BunStream.stdin` -> `stdio.stdin from Stdio.Stdio`: Standard input moved to
  the Stdio service; provide BunStdio.layer. Its stream exposes PlatformError
  instead of dying.
- `BunStream.stdout` -> `stdio.stdout() from Stdio.Stdio`: Standard output is
  correctly modeled as a Sink in v4. Explicitly adapt process.stdout with
  BunStream.fromReadable only to preserve the old unusual read behavior.
