<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/workflow/Workflow` v3 → v4

- `Workflow.Any` -> `effect/workflow/Workflow#Any`: Moved into core Effect.
  Workflow identity changed from name to \_tag and definitions are now
  class-compatible constructors.
- `Workflow.AnyTaggedRequestSchema` -> `none`: The TaggedRequest adapter
  constraint was removed. Define the workflow explicitly with Workflow.make and
  the request payload, success, error, and PrimaryKey schemas.
- `Workflow.CaptureDefects` -> `effect/workflow/Workflow#CaptureDefects`: Moved
  into core Effect and changed from a Context.Tag subclass to a
  Context.Reference value with the same true default.
- `Workflow.Execution` -> `effect/workflow/Workflow#Execution`: Moved into core
  Effect; its workflow discriminator changed from name to \_tag.
- `Workflow.Requirements` ->
  `Workflow.RequirementsClient / Workflow.RequirementsHandler`: The schema
  Context union split by direction: client payload encoding and result decoding
  versus handler payload decoding and result encoding.
- `Workflow.Result` -> `effect/workflow/Workflow#Result`: Moved into core
  Effect and remains the Complete or Suspended result type and schema
  constructor.
- `Workflow.ResultEncoded` -> `effect/workflow/Workflow#ResultEncoded`: Moved
  into core Effect and remains both the encoded result type and generic
  encoded-result codec.
- `Workflow.ResultTypeId` -> `none`: The result marker is private in v4. Use
  Workflow.isResult for narrowing.
- `Workflow.SuspendOnFailure` -> `effect/workflow/Workflow#SuspendOnFailure`:
  Moved into core Effect and changed from a Context.Tag subclass to a
  Context.Reference value with the same false default.
- `Workflow.TypeId` -> `none`: The workflow marker is private in v4. Use
  Workflow.Any or Workflow.Workflow constraints.
- `Workflow.Workflow` -> `effect/workflow/Workflow#Workflow`: Name and name
  became Tag and \_tag, schemas use directional services, definitions are
  constructable, and poll returns Option.
- `Workflow.Workflow.Error` -> `W["errorSchema"]["Type"]`: The namespace alias
  was removed. Extract the decoded error type from the public errorSchema
  property.
- `Workflow.Workflow.Payload` ->
  `Schema.Schema.Type<Workflow.PayloadSchema<W>>`: The namespace alias was
  removed. Extract the decoded payload from the exported PayloadSchema helper.
- `Workflow.Workflow.Success` -> `W["successSchema"]["Type"]`: The namespace
  alias was removed. Extract the decoded success type from the public
  successSchema property.
- `Workflow.fromTaggedRequest` -> `none`: Removed. Expand to
  Workflow.make(schema.\_tag, { payload: schema, success: schema.success,
  error: schema.failure, idempotencyKey: PrimaryKey.value }).
- `Workflow.make` -> `effect/workflow/Workflow#make`: The signature changed
  from make({ name, … }) to make(tag, { … }); definitions expose \_tag and are
  class-compatible constructors.
