<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/platform-node-shared/NodeSink` v3 → v4

- `NodeSink.stderr` -> `stdio.stderr() from Stdio.Stdio`: Standard error moved
  to effect/Stdio; provide NodeStdio.layer or NodeServices.layer.
- `NodeSink.stdin` ->
  `NodeSink.fromWritable({ evaluate: () => process.stdin, onError: ... })`:
  There is no Stdio sink because stdin is a readable stream in v4; use a manual
  adapter only if writing to process.stdin was intentional.
- `NodeSink.stdout` -> `stdio.stdout() from Stdio.Stdio`: Standard output moved
  to effect/Stdio; provide NodeStdio.layer or NodeServices.layer.
