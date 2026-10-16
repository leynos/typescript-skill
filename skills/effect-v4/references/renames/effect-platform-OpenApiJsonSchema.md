<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/platform/OpenApiJsonSchema` v3 → v4

- `OpenApiJsonSchema.Any` -> `effect/JsonSchema#JsonSchema`: The narrow node
  interfaces were consolidated into the open, dialect-neutral JSON Schema
  object model.
- `OpenApiJsonSchema.AnyObject` -> `effect/JsonSchema#JsonSchema`: The narrow
  node interfaces were consolidated; construct the required object directly.
- `OpenApiJsonSchema.AnyOf` -> `effect/JsonSchema#JsonSchema`: The narrow node
  interfaces were consolidated into the general object model.
- `OpenApiJsonSchema.Array` -> `effect/JsonSchema#JsonSchema`: The narrow node
  interfaces were consolidated into the general object model.
- `OpenApiJsonSchema.Boolean` -> `effect/JsonSchema#JsonSchema`: The narrow
  boolean interface was consolidated into the open, dialect-neutral JSON Schema
  object model.
- `OpenApiJsonSchema.Empty` -> `effect/JsonSchema#JsonSchema`: The narrow node
  interfaces and special id shapes were removed.
- `OpenApiJsonSchema.Enum` -> `effect/JsonSchema#JsonSchema`: The narrow node
  interfaces were consolidated into the general object model.
- `OpenApiJsonSchema.Enums` -> `effect/JsonSchema#JsonSchema`: The
  Effect-specific comment enum shape has no named v4 interface; use the general
  object model.
- `OpenApiJsonSchema.Integer` -> `effect/JsonSchema#JsonSchema`: The narrow
  numeric interfaces were consolidated into the general object model.
- `OpenApiJsonSchema.JsonSchema` -> `effect/JsonSchema#JsonSchema`: Use the
  dialect-neutral open JSON Schema object model.
- `OpenApiJsonSchema.Never` -> `effect/JsonSchema#JsonSchema`: The special
  never-schema interface was consolidated into the open JSON Schema object
  model; represent it with a not constraint.
- `OpenApiJsonSchema.Number` -> `effect/JsonSchema#JsonSchema`: The narrow
  number interface was consolidated into the open, dialect-neutral JSON Schema
  object model.
- `OpenApiJsonSchema.Numeric` -> `effect/JsonSchema#JsonSchema`: The narrow
  numeric interfaces were consolidated into the general object model.
- `OpenApiJsonSchema.Object` -> `effect/JsonSchema#JsonSchema`: The narrow node
  interfaces were consolidated into the general object model.
- `OpenApiJsonSchema.Ref` -> `effect/JsonSchema#JsonSchema`: The narrow ref
  interface was consolidated; OpenAPI conversion rewrites definition references.
- `OpenApiJsonSchema.Root` -> `effect/JsonSchema#MultiDocument`: OpenAPI
  generation keeps roots in schemas and shared components in definitions; the
  inline-definitions root model is gone.
- `OpenApiJsonSchema.String` -> `effect/JsonSchema#JsonSchema`: The narrow
  string interface was consolidated into the open, dialect-neutral JSON Schema
  object model.
- `OpenApiJsonSchema.Unknown`: TODO: needs guidance
- `OpenApiJsonSchema.Void` -> `effect/JsonSchema#JsonSchema`: The special
  void-schema interface was consolidated into the open JSON Schema object model.
- `OpenApiJsonSchema.make` ->
  `effect/Schema#toJsonSchemaDocument + effect/JsonSchema#toMultiDocumentOpenApi3_1`:
  Generate Draft 2020-12, wrap the root in a multi-document, then convert
  references and definitions to OpenAPI 3.1.
- `OpenApiJsonSchema.makeWithDefs` ->
  `effect/SchemaRepresentation#toJsonSchemaMultiDocument + effect/JsonSchema#toMultiDocumentOpenApi3_1`:
  Definitions are returned separately; build a multi-document representation
  and convert it to OpenAPI 3.1.
