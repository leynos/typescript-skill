<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/platform/FileSystem` v3 → v4

- `FileSystem.AccessFileOptions` ->
  `NonNullable<Parameters<FileSystem.FileSystem["access"]>[1]>`: Operation
  option interfaces are inline in the v4 FileSystem service.
- `FileSystem.CopyOptions` ->
  `NonNullable<Parameters<FileSystem.FileSystem["copy"]>[2]>`: Operation option
  interfaces are inline in the v4 FileSystem service.
- `FileSystem.File.Descriptor` -> `none`: Native file descriptors are no longer
  part of the portable File interface; use the File methods and keep any
  platform handle private in custom implementations.
- `FileSystem.FileDescriptor` -> `none`: The descriptor branding constructor
  was removed with the public fd field; use File operations instead of exposing
  a native descriptor.
- `FileSystem.FileTypeId` -> `typeof FileSystem.FileTypeId`: The runtime marker
  remains exported, but the separate type alias was removed.
- `FileSystem.GiB` -> `ByteSize.gibibytes`: Use the ByteSize binary unit
  constructor.
- `FileSystem.KiB` -> `ByteSize.kibibytes`: Use the ByteSize binary unit
  constructor.
- `FileSystem.MakeDirectoryOptions` ->
  `NonNullable<Parameters<FileSystem.FileSystem["makeDirectory"]>[1]>`:
  Operation option interfaces are inline in the v4 FileSystem service.
- `FileSystem.MakeTempDirectoryOptions` ->
  `NonNullable<Parameters<FileSystem.FileSystem["makeTempDirectory"]>[0]>`:
  Operation option interfaces are inline in the v4 FileSystem service.
- `FileSystem.MakeTempFileOptions` ->
  `NonNullable<Parameters<FileSystem.FileSystem["makeTempFile"]>[0]>`:
  Operation option interfaces are inline in the v4 FileSystem service.
- `FileSystem.MiB` -> `ByteSize.mebibytes`: Use the ByteSize binary unit
  constructor.
- `FileSystem.OpenFileOptions` ->
  `NonNullable<Parameters<FileSystem.FileSystem["open"]>[1]>`: Operation option
  interfaces are inline in the v4 FileSystem service.
- `FileSystem.PiB` -> `ByteSize.pebibytes`: Use the ByteSize binary unit
  constructor.
- `FileSystem.ReadDirectoryOptions` ->
  `NonNullable<Parameters<FileSystem.FileSystem["readDirectory"]>[1]>`:
  Operation option interfaces are inline in the v4 FileSystem service.
- `FileSystem.RemoveOptions` ->
  `NonNullable<Parameters<FileSystem.FileSystem["remove"]>[1]>`: Operation
  option interfaces are inline in the v4 FileSystem service.
- `FileSystem.SinkOptions` ->
  `NonNullable<Parameters<FileSystem.FileSystem["sink"]>[1]>`: Operation option
  interfaces are inline in the v4 FileSystem service.
- `FileSystem.Size` -> `ByteSize.ByteSize`: Use ByteSize.bytes or unit
  constructors for file sizes. Truncation lengths, buffer sizes, and read/write
  counts use number. File.seek takes and returns signed bigint positions; it
  can fail with PlatformError, including BadArgument when seeking before the
  start.
- `FileSystem.SizeInput` -> `ByteSize.Input`: File-size and path-backed range
  inputs use ByteSize.Input. String inputs must be non-negative decimal
  integers without leading zeros, followed by a canonical unit symbol or
  lowercase unit name, with at most one separating space. Parse external
  strings or fractional quantities with ByteSize.fromString (Option) or
  ByteSize.fromStringUnsafe (throws), then pass the resulting ByteSize.
  Truncation lengths, Web File ranges, and buffer sizes use number.
- `FileSystem.StreamOptions` ->
  `NonNullable<Parameters<FileSystem.FileSystem["stream"]>[1]>`: Stream options
  are inline; bufferSize was removed, bytesToRead and offset accept ByteSize
  inputs, and chunkSize uses number.
- `FileSystem.TiB` -> `ByteSize.tebibytes`: Use the ByteSize binary unit
  constructor.
- `FileSystem.WatchEventCreate` -> `FileSystem.WatchEvent.Create`: The
  constructor was removed; construct a tagged object with \_tag: "Create" and
  path.
- `FileSystem.WatchEventRemove` -> `FileSystem.WatchEvent.Remove`: The
  constructor was removed; construct a tagged object with \_tag: "Remove" and
  path.
- `FileSystem.WatchEventUpdate` -> `FileSystem.WatchEvent.Update`: The
  constructor was removed; construct a tagged object with \_tag: "Update" and
  path.
- `FileSystem.WatchOptions` -> `FileSystem.WatchOptions`: Retained after moving
  the module to effect/FileSystem; pass `{ recursive: true }` as the optional
  second argument to FileSystem.watch.
- `FileSystem.WriteFileOptions` ->
  `NonNullable<Parameters<FileSystem.FileSystem["writeFile"]>[2]>`: Operation
  option interfaces are inline in the v4 FileSystem service.
- `FileSystem.WriteFileStringOptions` ->
  `NonNullable<Parameters<FileSystem.FileSystem["writeFileString"]>[2]>`:
  Operation option interfaces are inline in the v4 FileSystem service.
- `FileSystem.layerNoop` -> `FileSystem.layerNoop`: The helper remains after
  moving the module to effect/FileSystem.
- `FileSystem.make` -> `FileSystem.make`: The constructor remains after moving
  the module to effect/FileSystem; adapt the implementation to the v4 service
  shape.
