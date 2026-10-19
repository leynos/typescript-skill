<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/rpc/Rpc` v3 → v4

- `Rpc.AddError` -> `effect/rpc/Rpc#AddError`: Retained; the added error must
  now be a Schema.Top and the resulting RPC also preserves its explicit service
  requirements.
- `Rpc.AddMiddleware` -> `effect/rpc/Rpc#AddMiddleware`: Retained; middleware
  is now an RpcMiddleware.AnyService and its provides/requires metadata updates
  the RPC service requirements.
- `Rpc.Any` -> `effect/rpc/Rpc#Any`: Retained as the erased RPC shape; use
  AnyWithProps when schema and middleware fields are required.
- `Rpc.AnySchema` -> `Schema.Top`: The RPC-specific erased schema alias was
  removed; use the v4 top schema constraint.
- `Rpc.AnyTaggedRequestSchema` -> `none`: RpcGroup no longer converts
  Schema.TaggedRequest classes into RPCs; declare the contract explicitly with
  Rpc.make.
- `Rpc.Context` -> `effect/rpc/Rpc#Services`: Schema Context became decoding
  and encoding services; use Services, or ServicesClient / ServicesServer at
  the corresponding boundary.
- `Rpc.ErrorEncoded` -> `Rpc.ErrorSchema<R>["Encoded"]`: The alias was removed;
  index the v4 error schema's Encoded member directly.
- `Rpc.ErrorExitEncoded` -> `Rpc.ErrorExitSchema<R>["Encoded"]`: Use the new
  exit error schema, which includes stream and middleware errors, then select
  its Encoded member.
- `Rpc.ErrorSchema` -> `effect/rpc/Rpc#ErrorSchema`: Retained; middleware
  errors now come from each service's error metadata.
- `Rpc.Handler` -> `effect/rpc/Rpc#Handler`: Retained; handler metadata now
  supplies ServerClient, RequestId, headers, and the concrete RPC.
- `Rpc.Middleware` -> `effect/rpc/Rpc#Middleware`: Retained and extracts
  Context.Service identifiers from the attached middleware services.
- `Rpc.MiddlewareClient` -> `effect/rpc/Rpc#MiddlewareClient`: Retained;
  required client middleware is derived from services configured with
  requiredForClient.
- `Rpc.Payload` -> `effect/rpc/Rpc#Payload`: Retained as the decoded payload
  type; use PayloadConstructor for the input accepted by generated clients.
- `Rpc.Success` -> `effect/rpc/Rpc#Success`: Retained as the decoded success
  type.
- `Rpc.SuccessChunkEncoded` -> `Rpc.SuccessExitSchema<R>["Encoded"]`: The alias
  was removed; for a streaming RPC the exit success schema is the stream
  element schema.
- `Rpc.SuccessEncoded` -> `effect/rpc/Rpc#SuccessEncoded`: Retained after the
  module move and now accounts for the RPC's explicit service-requirement
  parameter.
- `Rpc.SuccessExitEncoded` -> `Rpc.SuccessExitSchema<R>["Encoded"]`: Use the
  new exit success schema and select its Encoded member; streaming RPC exits
  use the element schema separately from the terminal void exit.
- `Rpc.SuccessSchema` -> `effect/rpc/Rpc#SuccessSchema`: Retained and uses the
  v4 Schema.Top constraint.
- `Rpc.Tag` -> `effect/rpc/Rpc#Tag`: Retained and also accounts for the v4 RPC
  service-requirement parameter.
- `Rpc.TypeId` -> `none`: The RPC marker is private in v4; use Rpc.isRpc for
  runtime checks and Rpc.Any for type constraints.
- `Rpc.WrapperTypeId` -> `none`: The wrapper marker is private in v4; use
  Rpc.isWrapper and the public Wrapper type.
- `Rpc.fromTaggedRequest` -> `Rpc.make`: Automatic TaggedRequest conversion was
  removed; pass the tag, payload, success, and error schemas explicitly to
  Rpc.make.
- `Rpc.make` -> `effect/rpc/Rpc#make`: Retained; schemas use v4 Schema.Top
  constraints and the defect option accepts Rpc.DefectSchema.
- `Rpc.wrap` -> `effect/rpc/Rpc#wrap`: Retained after the module move; it still
  applies fork and uninterruptible handler options, while the return type is
  now uniformly Rpc.Wrapper.
