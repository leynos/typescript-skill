<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/platform-browser/BrowserWorkerRunner` v3 → v4

- `BrowserWorkerRunner.launch` ->
  `Layer.launch + RpcServer.layerProtocolWorkerRunner`: The close-latch
  launcher was removed. Compose BrowserWorkerRunner.layer with the worker RPC
  server protocol layer and launch the resulting handler layer.
