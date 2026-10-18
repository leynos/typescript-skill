<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/ai/Response` v3 → v4

- `Response.Part` -> `Response.Part`: Moved to effect/ai/Response. The
  non-streaming union now also includes ToolApprovalRequestPart.
- `Response.PartTypeId` -> `Response.isPart`: The public PartTypeId was removed
  and the marker is internal in v4. Use Response.isPart for runtime refinement.
- `Response.ToolCallPartEncoded` -> `Response.ToolCallPartEncoded`: Moved to
  effect/ai/Response; providerName was removed while providerExecuted remains
  optional when encoded.
- `Response.ToolResultPart` -> `Response.ToolResultPart`: The schema selects
  success or failure using isFailure rather than trying both result schemas. It
  returns Schema.Codec; supply decoding services when decoding and encoding
  services when encoding.
- `Response.ToolResultPartEncoded` -> `Response.ToolResultPartEncoded`: Moved
  to effect/ai/Response; providerName was removed and optional preliminary was
  added to the encoded shape.
- `Response.documentSourcePart` ->
  `Response.makePart("source", { ...params, sourceType: "document" })`: The
  lowercase convenience constructor was removed. The DocumentSourcePart model
  remains, and the generic constructor now requires the document source
  discriminator.
- `Response.errorPart` -> `Response.makePart("error", params)`: The lowercase
  convenience constructor was removed; construct the retained error part
  through Response.makePart.
- `Response.finishPart` -> `Response.makePart("finish", params)`: The lowercase
  convenience constructor was removed. V4 Usage has nested inputTokens and
  outputTokens objects, and FinishPart adds optional HTTP response details.
- `Response.reasoningDeltaPart` ->
  `Response.makePart("reasoning-delta", params)`: The lowercase convenience
  constructor was removed; construct the retained ReasoningDeltaPart through
  Response.makePart.
- `Response.reasoningEndPart` -> `Response.makePart("reasoning-end", params)`:
  The lowercase convenience constructor was removed; construct the retained
  ReasoningEndPart through Response.makePart.
- `Response.reasoningStartPart` ->
  `Response.makePart("reasoning-start", params)`: The lowercase convenience
  constructor was removed; construct the retained ReasoningStartPart through
  Response.makePart.
- `Response.responseMetadataPart` ->
  `Response.makePart("response-metadata", params)`: The lowercase convenience
  constructor was removed. V4 id, modelId, and timestamp are optional raw
  values rather than Option values, and optional HTTP request details were
  added.
- `Response.textDeltaPart` -> `Response.makePart("text-delta", params)`: The
  lowercase convenience constructor was removed; construct the retained
  TextDeltaPart through Response.makePart.
- `Response.textEndPart` -> `Response.makePart("text-end", params)`: The
  lowercase convenience constructor was removed; construct the retained
  TextEndPart through Response.makePart.
- `Response.textStartPart` -> `Response.makePart("text-start", params)`: The
  lowercase convenience constructor was removed; construct the retained
  TextStartPart through Response.makePart.
- `Response.toolParamsDeltaPart` ->
  `Response.makePart("tool-params-delta", params)`: The lowercase convenience
  constructor was removed; construct the retained ToolParamsDeltaPart through
  Response.makePart.
- `Response.toolParamsEndPart` ->
  `Response.makePart("tool-params-end", params)`: The lowercase convenience
  constructor was removed; construct the retained ToolParamsEndPart through
  Response.makePart.
- `Response.toolParamsStartPart` ->
  `Response.makePart("tool-params-start", params)`: The lowercase convenience
  constructor was removed; providerName was also removed from
  ToolParamsStartPart in v4.
- `Response.toolResultPart` -> `Response.toolResultPart`: Moved to
  effect/ai/Response; providerName was removed and decoded tool results now
  require preliminary, normally false.
- `Response.urlSourcePart` ->
  `Response.makePart("source", { ...params, sourceType: "url" })`: The
  lowercase convenience constructor was removed. The UrlSourcePart model
  remains, and the generic constructor now requires the URL source
  discriminator.
