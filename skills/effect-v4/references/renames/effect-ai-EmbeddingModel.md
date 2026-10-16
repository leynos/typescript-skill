<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/ai/EmbeddingModel` v3 → v4

- `EmbeddingModel.EmbeddingModel` -> `EmbeddingModel.EmbeddingModel`: Use the
  EmbeddingModel interface for implementations and the Context.Service value as
  the service key; it is no longer a class. Prefer EmbeddingModel.make to
  construct the branded implementation.
- `EmbeddingModel.Result`: TODO: needs guidance
- `EmbeddingModel.Service` -> `EmbeddingModel.EmbeddingModel`: Service was
  renamed to EmbeddingModel. Implementations require [EmbeddingModel.TypeId]:
  EmbeddingModel.TypeId; EmbeddingModel.make supplies the brand.
- `EmbeddingModel.makeDataLoader` ->
  `EmbeddingModel.make + RequestResolver.setDelay + RequestResolver.batchN`:
  The dedicated data-loader constructor was removed. EmbeddingModel.make
  batches concurrent embed requests through its resolver; compose the exposed
  resolver with setDelay and optional batchN for the old window and
  maximum-batch behavior.
