<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `effect/JSONSchema` v3 → v4

- `JSONSchema.JsonSchema7` -> `JsonSchema.JsonSchema`: The draft-07-specific
  union was replaced by the dialect-neutral JSON Schema model.
- `JSONSchema.JsonSchema7Any` -> `JsonSchema.JsonSchema`: Individual draft-07
  node interfaces were consolidated into JsonSchema.JsonSchema.
- `JSONSchema.JsonSchema7AnyOf` -> `JsonSchema.JsonSchema`: Individual draft-07
  node interfaces were consolidated into JsonSchema.JsonSchema.
- `JSONSchema.JsonSchema7Array` -> `JsonSchema.JsonSchema`: Individual draft-07
  node interfaces were consolidated into JsonSchema.JsonSchema.
- `JSONSchema.JsonSchema7Boolean` -> `JsonSchema.JsonSchema`: Individual
  draft-07 node interfaces were consolidated into JsonSchema.JsonSchema.
- `JSONSchema.JsonSchema7Enum` -> `JsonSchema.JsonSchema`: Individual draft-07
  node interfaces were consolidated into JsonSchema.JsonSchema.
- `JSONSchema.JsonSchema7Enums` -> `JsonSchema.JsonSchema`: Individual draft-07
  node interfaces were consolidated into JsonSchema.JsonSchema.
- `JSONSchema.JsonSchema7Integer` -> `JsonSchema.JsonSchema`: Individual
  draft-07 node interfaces were consolidated into JsonSchema.JsonSchema.
- `JSONSchema.JsonSchema7Never` -> `JsonSchema.JsonSchema`: Individual draft-07
  node interfaces were consolidated into JsonSchema.JsonSchema.
- `JSONSchema.JsonSchema7Null` -> `JsonSchema.JsonSchema`: Individual draft-07
  node interfaces were consolidated into JsonSchema.JsonSchema.
- `JSONSchema.JsonSchema7Number` -> `JsonSchema.JsonSchema`: Individual
  draft-07 node interfaces were consolidated into JsonSchema.JsonSchema.
- `JSONSchema.JsonSchema7Numeric` -> `JsonSchema.JsonSchema`: Individual
  draft-07 node interfaces were consolidated into JsonSchema.JsonSchema.
- `JSONSchema.JsonSchema7Object` -> `JsonSchema.JsonSchema`: Individual
  draft-07 node interfaces were consolidated into JsonSchema.JsonSchema.
- `JSONSchema.JsonSchema7Ref` -> `JsonSchema.JsonSchema`: Individual draft-07
  node interfaces were consolidated into JsonSchema.JsonSchema.
- `JSONSchema.JsonSchema7Root` -> `JsonSchema.Document<"draft-07">`: Use a
  typed JSON Schema document for a draft-07 root and definitions.
- `JSONSchema.JsonSchema7String` -> `JsonSchema.JsonSchema`: Individual
  draft-07 node interfaces were consolidated into JsonSchema.JsonSchema.
- `JSONSchema.JsonSchema7Unknown` -> `JsonSchema.JsonSchema`: Individual
  draft-07 node interfaces were consolidated into JsonSchema.JsonSchema.
- `JSONSchema.JsonSchema7Void` -> `JsonSchema.JsonSchema`: Individual draft-07
  node interfaces were consolidated into JsonSchema.JsonSchema.
- `JSONSchema.JsonSchema7empty` -> `JsonSchema.JsonSchema`: Individual draft-07
  node interfaces were consolidated into JsonSchema.JsonSchema.
- `JSONSchema.JsonSchema7object` -> `JsonSchema.JsonSchema`: Individual
  draft-07 node interfaces were consolidated into JsonSchema.JsonSchema.
- `JSONSchema.JsonSchemaAnnotations` -> `Schema.Annotations.Documentation`:
  Schema metadata now uses string-keyed Schema annotations; JSON
  Schema-specific checks use toJsonSchema annotations.
