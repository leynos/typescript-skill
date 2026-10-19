<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/platform/Terminal` v3 → v4

- `Terminal.QuitException` -> `Terminal.QuitError`: The quit sentinel was
  renamed and moved to effect/Terminal.
- `Terminal.isQuitException` -> `Terminal.isQuitError`: The quit sentinel was
  renamed from QuitException to QuitError.
