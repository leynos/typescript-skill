<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/platform/Worker` v3 → v4

- `Worker.BackingWorker` -> `Worker.Worker`: The low-level backing worker
  became the primary Worker interface with send and run operations.
- `Worker.PlatformWorker` -> `Worker.WorkerPlatform`: The platform service was
  renamed and is now a Context.Service class.
- `Worker.PlatformWorkerTypeId` -> `none`: The Context.Service class replaces
  the public platform-worker type-id alias.
- `Worker.SerializedWorker` -> `RpcClient with RpcClient.layerProtocolWorker`:
  The serialized worker facade was removed; v4 routes schema-defined RPCs
  through the worker protocol.
- `Worker.SerializedWorker.Options` -> `RpcWorker.layerInitialMessage`: Use
  RpcWorker.layerInitialMessage when a worker RPC protocol needs schema-encoded
  initialization.
- `Worker.SerializedWorkerPool` -> `RpcClient.makeProtocolWorker`: The
  worker-backed RPC protocol owns its worker pool in v4.
- `Worker.SerializedWorkerPool.Options` ->
  `Parameters<typeof RpcClient.makeProtocolWorker>[0]`: Pool sizing options
  moved to the worker RPC protocol; initial messages are provided separately
  with RpcWorker.layerInitialMessage.
- `Worker.Worker` -> `Worker.Worker`: The name remains in
  effect/workers/Worker, but it is now the low-level send/run abstraction
  rather than execute/executeEffect.
- `Worker.Worker.Options` -> `Worker.Worker["run"] options`: Encoding moved to
  RPC schemas; the low-level run operation only accepts an optional onSpawn
  effect.
- `Worker.Worker.Response` -> `none`: The old tagged-request wire response is
  gone; worker RPC wire messages are internal to RpcClient and RpcServer.
- `Worker.Worker.Span` -> `none`: The explicit span tuple was removed; the RPC
  worker protocol handles span propagation internally.
- `Worker.WorkerManager` -> `Worker.WorkerPlatform`: WorkerPlatform now spawns
  low-level Worker values directly, replacing WorkerManager.
- `Worker.WorkerManagerTypeId` -> `none`: The removed WorkerManager has no v4
  type-id; WorkerPlatform is a Context.Service class.
- `Worker.WorkerPool` -> `RpcClient.Protocol`: For serialized request/response
  workloads use the worker-backed RPC Protocol; for raw messages build a Pool
  around WorkerPlatform.spawn.
- `Worker.WorkerPool.Options` ->
  `Parameters<typeof RpcClient.makeProtocolWorker>[0]`: Worker RPC pool sizing
  is configured on makeProtocolWorker or layerProtocolWorker.
- `Worker.layerManager` -> `Worker.WorkerPlatform`: WorkerManager was removed;
  provide the adapter's WorkerPlatform layer directly.
- `Worker.makeManager` -> `Worker.WorkerPlatform`: WorkerManager was removed;
  obtain WorkerPlatform and call its spawn method.
- `Worker.makePool` -> `Pool + Worker.WorkerPlatform.spawn`: Generic worker
  pools are no longer built by this module; build a Pool around
  WorkerPlatform.spawn, or use RpcClient.makeProtocolWorker for RPC workers.
- `Worker.makePoolLayer` -> `RpcClient.layerProtocolWorker`: The standard v4
  worker-pool layer is the worker-backed RPC client protocol; compose it with
  the RPC client layer.
- `Worker.makePoolSerialized` -> `RpcClient.makeProtocolWorker`: Serialized
  tagged-request workers were replaced by the worker-backed RPC protocol.
- `Worker.makePoolSerializedLayer` -> `RpcClient.layerProtocolWorker`:
  Serialized tagged-request worker pools were replaced by the worker-backed RPC
  protocol layer.
- `Worker.makeSerialized` -> `RpcClient with RpcClient.layerProtocolWorker`:
  Serialized tagged-request execution moved to the v4 RPC model; define an
  RpcGroup and use the worker protocol.
