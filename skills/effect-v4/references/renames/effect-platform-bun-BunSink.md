<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/platform-bun/BunSink` v3 → v4

- `BunSink.stderr` -> `stdio.stderr() from Stdio.Stdio`: Process stdio moved
  behind effect/Stdio; provide BunStdio.layer. stderr remains a Sink and can be
  configured with endOnDone.
- `BunSink.stdin` -> `stdio.stdin from Stdio.Stdio`: Standard input is
  correctly modeled as a Stream in v4, not a writable Sink; manually adapt
  process.stdin only if writing to it was intentional.
- `BunSink.stdout` -> `stdio.stdout() from Stdio.Stdio`: Process stdio moved
  behind effect/Stdio; provide BunStdio.layer. stdout remains a Sink.
