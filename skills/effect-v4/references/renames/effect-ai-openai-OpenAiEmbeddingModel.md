<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/ai-openai/OpenAiEmbeddingModel` v3 → v4

- `OpenAiEmbeddingModel.Config.Batched` ->
  `OpenAiEmbeddingModel.Config.Service`: Batch-mode configuration was removed;
  use the unified embedding config and constructor.
- `OpenAiEmbeddingModel.Config.DataLoader` ->
  `OpenAiEmbeddingModel.Config.Service`: Data-loader configuration was removed;
  use the unified embedding config and constructor.
- `OpenAiEmbeddingModel.layerBatched` -> `OpenAiEmbeddingModel.layer`: The
  batched and data-loader layers were replaced by one embedding layer; pass the
  model and request config explicitly.
- `OpenAiEmbeddingModel.layerDataLoader` -> `OpenAiEmbeddingModel.layer`: The
  batched and data-loader layers were replaced by one embedding layer; pass the
  model and request config explicitly.
- `OpenAiEmbeddingModel.makeDataLoader` -> `OpenAiEmbeddingModel.make`: The
  dedicated data-loader constructor was removed; use the unified v4 embedding
  service constructor.
