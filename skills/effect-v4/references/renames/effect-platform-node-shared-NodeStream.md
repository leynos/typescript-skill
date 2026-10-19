<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/platform-node-shared/NodeStream` v3 → v4

- `NodeStream.FromReadableOptions` ->
  `{ readonly chunkSize?: number; readonly closeOnDone?: boolean }`: The named
  interface was removed and its fields were inlined into readable constructor
  options; chunkSize narrowed from SizeInput to number.
- `NodeStream.FromWritableOptions` ->
  `{ readonly endOnDone?: boolean; readonly encoding?: BufferEncoding }`: The
  named interface was removed and its fields were inlined into NodeSink and
  duplex constructor options.
- `NodeStream.stderr` ->
  `NodeStream.fromReadable({ evaluate: () => process.stderr, closeOnDone: false }).pipe(Stream.orDie)`:
  This preserves the unusual v3 read behavior and works only when fd 2 is a
  TTY or pipe (a Duplex socket); when fd 2 is redirected to a file,
  process.stderr is write-only and the stream fails. For normal error output
  use the stdio.stderr() Sink from effect/Stdio.
- `NodeStream.stdin` -> `stdio.stdin from Stdio.Stdio`: Standard input moved to
  effect/Stdio; provide NodeStdio.layer or NodeServices.layer. The service
  stream exposes PlatformError instead of dying.
- `NodeStream.stdout` ->
  `NodeStream.fromReadable({ evaluate: () => process.stdout, closeOnDone: false }).pipe(Stream.orDie)`:
  This preserves the unusual v3 read behavior and works only when fd 1 is a
  TTY or pipe (a Duplex socket); when fd 1 is redirected to a file,
  process.stdout is write-only and the stream fails. For normal output use the
  stdio.stdout() Sink from effect/Stdio.
