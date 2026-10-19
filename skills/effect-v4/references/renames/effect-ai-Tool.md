<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/ai/Tool` v3 → v4

- `Tool.AnyParametersSchema` -> `Schema.Constraint`: The AI-specific alias was
  removed. V4 Tool parameter schemas use the general Schema.Constraint type and
  are no longer restricted to the old struct-or-EmptyParams union.
- `Tool.AnyTaggedRequestSchema` -> `none`: The TaggedRequest-specific Tool
  adapter contract was removed. Model the operation directly with Tool.make and
  ordinary v4 Schema.Constraint values.
- `Tool.Destructive` -> `Tool.Destructive`: Moved to effect/ai/Tool. It is now
  a Context.Reference\<boolean\> value rather than a Reference subclass; its
  default remains true.
- `Tool.Failure` -> `Tool.Failure`: Moved to effect/ai/Tool and remains the
  utility type that extracts a tool's decoded failure type.
- `Tool.FromTaggedRequest` -> `Tool.Tool`: The dedicated derived alias was
  removed. Construct with Tool.make and let Tool.Tool infer the name,
  parameter, success, and failure schemas.
- `Tool.Idempotent` -> `Tool.Idempotent`: Moved to effect/ai/Tool. It is now a
  Context.Reference\<boolean\> value rather than a Reference subclass; its
  default remains false.
- `Tool.OpenWorld` -> `Tool.OpenWorld`: Moved to effect/ai/Tool. It is now a
  Context.Reference\<boolean\> value rather than a Reference subclass; its
  default remains true.
- `Tool.ProviderDefinedTypeId` -> `Tool.ProviderDefinedTypeId`: Moved to
  effect/ai/Tool and remains public. Its literal changed, so use the export
  rather than retaining the old hard-coded string.
- `Tool.Readonly` -> `Tool.Readonly`: Moved to effect/ai/Tool. It is now a
  Context.Reference\<boolean\> value rather than a Reference subclass; its
  default remains false.
- `Tool.Requirements` -> `Tool.HandlerServices`: Renamed and refined.
  HandlerServices combines parameter-decoding, result-encoding, and
  request-level dependencies required by a tool handler.
- `Tool.Result` -> `Tool.Result`: The result includes success, declared
  failure, and execution-denied or execution-interrupted values in both failure
  modes. Return mode also includes AiError; handle these variants when
  narrowing results.
- `Tool.ResultEncoded` -> `Tool.ResultEncoded`: The encoded result includes
  execution-denied and execution-interrupted variants in both failure modes,
  plus encoded AiError in return mode.
- `Tool.Success` -> `Tool.Success`: Moved to effect/ai/Tool and remains the
  utility type that extracts a tool's decoded success type.
- `Tool.Tool.ProviderDefinedProto` -> `Tool.ProviderDefined`: This
  implementation-brand interface is no longer public. Use Tool.ProviderDefined
  for the model type and Tool.isProviderDefined for runtime narrowing.
- `Tool.Tool.Variance` -> `Tool.Tool / Tool.Any`: This implementation variance
  interface is no longer public; its requirement marker is inline in Tool.Tool.
  Constrain generic code with Tool.Tool or Tool.Any.
- `Tool.Tool.VarianceStruct` -> `Tool.Tool / Tool.Any`: This implementation
  variance payload is no longer public; the requirements marker is inline in
  Tool.Tool and should not be named independently.
- `Tool.TypeId` -> `Tool.TypeId`: Moved to effect/ai/Tool and remains public.
  Its literal changed, so use the export rather than retaining the old
  hard-coded string.
- `Tool.fromTaggedRequest` -> `Tool.make`: The adapter was removed. Rebuild the
  tool explicitly with Tool.make(name, { parameters, success, failure });
  Toolkit.make no longer converts schema values automatically.
- `Tool.getDescriptionFromSchemaAst` -> `SchemaAST.resolveDescription`: Moved
  out of Tool to the general v4 AST annotation resolver. For a Tool value,
  prefer Tool.getDescription.
- `Tool.getJsonSchemaFromSchemaAst` -> `Tool.getJsonSchemaFromSchema`: Renamed
  to accept a Schema.Constraint instead of a raw AST and now emits the v4 JSON
  Schema model. Wrap a raw AST with Schema.make first.
