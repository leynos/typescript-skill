<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/platform-browser/Clipboard` v3 → v4

- `Clipboard.Clipboard` -> `Clipboard.Clipboard`: The service remains, now as a
  Context.Service with a private brand; normal access and provision are
  unchanged.
- `Clipboard.ErrorTypeId` -> `none`: The error marker is private in v4;
  discriminate ClipboardError by its \_tag instead.
- `Clipboard.TypeId` -> `none`: The service brand is private in v4; use the
  Clipboard Context.Service value.
