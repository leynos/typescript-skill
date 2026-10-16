<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/platform/WorkerRunner` v3 → v4

- `WorkerRunner.BackingRunner` -> `WorkerRunner.WorkerRunner`: The low-level
  backing runner became the primary WorkerRunner interface.
- `WorkerRunner.BackingRunner.Message` -> `WorkerRunner.PlatformMessage`: The
  request/close wire tuple moved to the top-level PlatformMessage type.
- `WorkerRunner.CloseLatch` -> `none`: The public close-latch service was
  removed; WorkerRunner implementations manage lifetime through their run
  effect and adapter scope.
- `WorkerRunner.PlatformRunner` -> `WorkerRunner.WorkerRunnerPlatform`: The
  platform service was renamed and is now a Context.Service class.
- `WorkerRunner.PlatformRunnerTypeId` -> `none`: The Context.Service class
  replaces the public platform-runner type-id alias.
- `WorkerRunner.Runner` -> `WorkerRunner.WorkerRunner`: The namespace-only
  runner API was replaced by the low-level WorkerRunner interface.
- `WorkerRunner.Runner.Options` -> `none`: The custom decode/encode callbacks
  were removed; use raw low-level messages or define schemas in the v4 RPC
  model.
- `WorkerRunner.SerializedRunner` -> `RpcServer with RpcGroup handlers`: The
  serialized runner namespace was removed in favor of typed Rpc definitions and
  RpcServer.
- `WorkerRunner.SerializedRunner.Handlers` -> `RpcGroup.HandlersFrom`: Define
  an RpcGroup and derive its server handler object type with HandlersFrom.
- `WorkerRunner.SerializedRunner.HandlersContext` ->
  `RpcGroup.HandlersServices`: Derive services required by an RpcGroup handler
  object with HandlersServices.
- `WorkerRunner.SerializedRunner.InitialContext` -> `none`: Initial-message
  layer outputs are no longer inferred by this helper; model initialization as
  normal RpcGroup handler layers and services.
- `WorkerRunner.SerializedRunner.InitialEnv` -> `none`: Initial-message layer
  inputs are no longer inferred by this helper; model initialization as normal
  RpcGroup handler layers and services.
- `WorkerRunner.launch` -> `RpcServer.layerProtocolWorkerRunner`: For
  schema-defined workers, provide the worker-runner RPC protocol and launch the
  normal RpcServer layer.
- `WorkerRunner.layer` ->
  `WorkerRunner.WorkerRunnerPlatform.start + WorkerRunner.WorkerRunner.run`:
  The generic processing layer was removed; use the low-level runner directly
  or the RpcServer worker protocol.
- `WorkerRunner.layerCloseLatch` -> `none`: The public close-latch layer was
  removed; adapter runner lifetime is managed internally.
- `WorkerRunner.layerSerialized` -> `RpcServer.layerProtocolWorkerRunner`:
  Serialized tagged-request handlers moved to RpcGroup handlers served through
  the worker-runner RPC protocol.
- `WorkerRunner.make` ->
  `WorkerRunner.WorkerRunnerPlatform.start + WorkerRunner.WorkerRunner.run`:
  Start the platform runner and register the low-level message handler directly.
- `WorkerRunner.makeSerialized` -> `RpcServer.makeProtocolWorkerRunner`:
  Serialized tagged-request execution moved to RpcServer with an RpcGroup
  handler layer.
