<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `effect/Pretty` v3 → v4

- `Pretty.Pretty` -> `Formatter.Formatter`: The formatter function type is now
  exported by Formatter.
- `Pretty.PrettyAnnotation` -> `Schema.Annotations.ToFormatter.Declaration`:
  Custom declaration formatter annotations now use the toFormatter key in
  Schema.Annotations.
- `Pretty.match` -> `Schema.toFormatter`: The compiler match table was removed;
  customize traversal with the toFormatter onBefore option.
