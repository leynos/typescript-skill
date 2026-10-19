<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/ai/McpSchema` v3 → v4

- `McpSchema.ContentBlock` -> `McpSchema.ContentBlock`: Moved to
  effect/ai/McpSchema. It remains the MCP content-block union, but v4 exports
  it as a const schema rather than a Schema.Union subclass. Binary image,
  audio, and blob data still use Uint8Array values with base64 wire encoding.
- `McpSchema.ElicitResult` -> `McpSchema.ElicitResult`: Moved to
  effect/ai/McpSchema. It remains discriminated by action, but accepted content
  is now optional and, when present, is a record of strings, finite numbers,
  booleans, or string arrays; declined and canceled responses still omit
  content.
- `McpSchema.McpError` -> `McpSchema.McpError`: Moved, but changed from a
  constructable base class to a union schema of standard tagged protocol errors
  plus McpErrorBase. Use McpErrorBase to construct a generic MCP error.
- `McpSchema.ParamAnnotation` -> `McpSchema.isParam / Param.name`: The public
  symbol annotation was removed. Detect parameter wrappers with
  McpSchema.isParam and read the narrowed Param.name instead of inspecting AST
  annotations.
- `McpSchema.param` -> `McpSchema.param`: Moved to effect/ai/McpSchema. V4
  wraps the schema and exposes Param.name and Param.schema instead of attaching
  a public symbol annotation.
