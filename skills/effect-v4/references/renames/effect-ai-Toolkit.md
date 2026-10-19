<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/ai/Toolkit` v3 → v4

- `Toolkit.HandlersFrom` -> `Toolkit.HandlersFrom`: Moved to effect/ai/Toolkit.
  V4 handlers receive a HandlerContext argument and may fail with the declared
  failure, AiError, or AiErrorReason while requiring Tool.HandlerServices.
- `Toolkit.TypeId` -> `Toolkit.Toolkit / Toolkit.Any`: The toolkit nominal id
  is private in v4. Use Toolkit.Toolkit or Toolkit.Any for typing instead of
  importing or inspecting the marker.
