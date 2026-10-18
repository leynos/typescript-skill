<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/platform/Error` v3 → v4

- `Error.Module` -> `string`: The closed module-name Schema was removed;
  PlatformError reason records accept any module string.
- `Error.PlatformError` -> `PlatformError.PlatformError`: The module moved to
  effect/PlatformError and PlatformError became a wrapper class around
  BadArgument or SystemError.
- `Error.SystemErrorReason` -> `PlatformError.SystemErrorTag`: The normalized
  system-error reason union was renamed.
- `Error.TypeId` -> `none`: The PlatformError runtime marker is internal in v4;
  use the PlatformError class/tag.
- `Error.TypeIdError` -> `Data.TaggedError or Schema.Error`: The
  platform-specific error-class factory was removed; define tagged data errors
  or schema-backed error classes directly.
