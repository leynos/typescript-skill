<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/ai-openai/OpenAiClient` v3 → v4

- `OpenAiClient.LogProbs` -> `Generated.LogProb`: The client-local
  log-probability schema moved to the regenerated v4 OpenAI schema surface and
  changed shape.
- `OpenAiClient.ResponseCodeInterpreterCallCodeDeltaEvent` ->
  `Generated.ResponseCodeInterpreterCallCodeDeltaEvent`: The event schema moved
  out of OpenAiClient into the regenerated OpenAI schema surface; re-check its
  v4 Type/Encoded shape.
- `OpenAiClient.ResponseCodeInterpreterCallCodeDoneEvent` ->
  `Generated.ResponseCodeInterpreterCallCodeDoneEvent`: The event schema moved
  out of OpenAiClient into the regenerated OpenAI schema surface; re-check its
  v4 Type/Encoded shape.
- `OpenAiClient.ResponseCodeInterpreterCallCompletedEvent` ->
  `Generated.ResponseCodeInterpreterCallCompletedEvent`: The event schema moved
  out of OpenAiClient into the regenerated OpenAI schema surface; re-check its
  v4 Type/Encoded shape.
- `OpenAiClient.ResponseCodeInterpreterCallInProgressEvent` ->
  `Generated.ResponseCodeInterpreterCallInProgressEvent`: The event schema
  moved out of OpenAiClient into the regenerated OpenAI schema surface;
  re-check its v4 Type/Encoded shape.
- `OpenAiClient.ResponseCodeInterpreterCallInterpretingEvent` ->
  `Generated.ResponseCodeInterpreterCallInterpretingEvent`: The event schema
  moved out of OpenAiClient into the regenerated OpenAI schema surface;
  re-check its v4 Type/Encoded shape.
- `OpenAiClient.ResponseCompletedEvent` -> `Generated.ResponseCompletedEvent`:
  The event schema moved out of OpenAiClient into the regenerated OpenAI schema
  surface; re-check its v4 Type/Encoded shape.
- `OpenAiClient.ResponseContentPartAddedEvent` ->
  `Generated.ResponseContentPartAddedEvent`: The event schema moved out of
  OpenAiClient into the regenerated OpenAI schema surface; re-check its v4
  Type/Encoded shape.
- `OpenAiClient.ResponseContentPartDoneEvent` ->
  `Generated.ResponseContentPartDoneEvent`: The event schema moved out of
  OpenAiClient into the regenerated OpenAI schema surface; re-check its v4
  Type/Encoded shape.
- `OpenAiClient.ResponseCreatedEvent` -> `Generated.ResponseCreatedEvent`: The
  event schema moved out of OpenAiClient into the regenerated OpenAI schema
  surface; re-check its v4 Type/Encoded shape.
- `OpenAiClient.ResponseCustomToolCallInputDeltaEvent` ->
  `Generated.ResponseCustomToolCallInputDeltaEvent`: The event schema moved out
  of OpenAiClient into the regenerated OpenAI schema surface; re-check its v4
  Type/Encoded shape.
- `OpenAiClient.ResponseCustomToolCallInputDoneEvent` ->
  `Generated.ResponseCustomToolCallInputDoneEvent`: The event schema moved out
  of OpenAiClient into the regenerated OpenAI schema surface; re-check its v4
  Type/Encoded shape.
- `OpenAiClient.ResponseErrorEvent` -> `Generated.ResponseErrorEvent`: The
  event schema moved out of OpenAiClient into the regenerated OpenAI schema
  surface; re-check its v4 Type/Encoded shape.
- `OpenAiClient.ResponseFailedEvent` -> `Generated.ResponseFailedEvent`: The
  event schema moved out of OpenAiClient into the regenerated OpenAI schema
  surface; re-check its v4 Type/Encoded shape.
- `OpenAiClient.ResponseFileSearchCallCompletedEvent` ->
  `Generated.ResponseFileSearchCallCompletedEvent`: The event schema moved out
  of OpenAiClient into the regenerated OpenAI schema surface; re-check its v4
  Type/Encoded shape.
- `OpenAiClient.ResponseFileSearchCallInProgressEvent` ->
  `Generated.ResponseFileSearchCallInProgressEvent`: The event schema moved out
  of OpenAiClient into the regenerated OpenAI schema surface; re-check its v4
  Type/Encoded shape.
- `OpenAiClient.ResponseFileSearchCallSearchingEvent` ->
  `Generated.ResponseFileSearchCallSearchingEvent`: The event schema moved out
  of OpenAiClient into the regenerated OpenAI schema surface; re-check its v4
  Type/Encoded shape.
- `OpenAiClient.ResponseFunctionCallArgumentsDeltaEvent` ->
  `Generated.ResponseFunctionCallArgumentsDeltaEvent`: The event schema moved
  out of OpenAiClient into the regenerated OpenAI schema surface; re-check its
  v4 Type/Encoded shape.
- `OpenAiClient.ResponseFunctionCallArgumentsDoneEvent` ->
  `Generated.ResponseFunctionCallArgumentsDoneEvent`: The event schema moved
  out of OpenAiClient into the regenerated OpenAI schema surface; re-check its
  v4 Type/Encoded shape.
- `OpenAiClient.ResponseImageGenerationCallCompletedEvent` ->
  `OpenAiClient.ResponseStreamEvent`: The standalone event helper was removed
  from OpenAiClient; narrow the v4 ResponseStreamEvent union by its `type`
  discriminator.
- `OpenAiClient.ResponseImageGenerationCallGeneratingEvent` ->
  `OpenAiClient.ResponseStreamEvent`: The standalone event helper was removed
  from OpenAiClient; narrow the v4 ResponseStreamEvent union by its `type`
  discriminator.
- `OpenAiClient.ResponseImageGenerationCallInProgressEvent` ->
  `OpenAiClient.ResponseStreamEvent`: The standalone event helper was removed
  from OpenAiClient; narrow the v4 ResponseStreamEvent union by its `type`
  discriminator.
- `OpenAiClient.ResponseImageGenerationCallPartialImageEvent` ->
  `OpenAiClient.ResponseStreamEvent`: The standalone event helper was removed
  from OpenAiClient; narrow the v4 ResponseStreamEvent union by its `type`
  discriminator.
- `OpenAiClient.ResponseInProgressEvent` ->
  `Generated.ResponseInProgressEvent`: The event schema moved out of
  OpenAiClient into the regenerated OpenAI schema surface; re-check its v4
  Type/Encoded shape.
- `OpenAiClient.ResponseIncompleteEvent` ->
  `Generated.ResponseIncompleteEvent`: The event schema moved out of
  OpenAiClient into the regenerated OpenAI schema surface; re-check its v4
  Type/Encoded shape.
- `OpenAiClient.ResponseMcpCallArgumentsDeltaEvent` ->
  `OpenAiClient.ResponseStreamEvent`: The standalone event helper was removed
  from OpenAiClient; narrow the v4 ResponseStreamEvent union by its `type`
  discriminator.
- `OpenAiClient.ResponseMcpCallArgumentsDoneEvent` ->
  `OpenAiClient.ResponseStreamEvent`: The standalone event helper was removed
  from OpenAiClient; narrow the v4 ResponseStreamEvent union by its `type`
  discriminator.
- `OpenAiClient.ResponseMcpCallCompletedEvent` ->
  `OpenAiClient.ResponseStreamEvent`: The standalone event helper was removed
  from OpenAiClient; narrow the v4 ResponseStreamEvent union by its `type`
  discriminator.
- `OpenAiClient.ResponseMcpCallFailedEvent` ->
  `OpenAiClient.ResponseStreamEvent`: The standalone event helper was removed
  from OpenAiClient; narrow the v4 ResponseStreamEvent union by its `type`
  discriminator.
- `OpenAiClient.ResponseMcpCallInProgressEvent` ->
  `OpenAiClient.ResponseStreamEvent`: The standalone event helper was removed
  from OpenAiClient; narrow the v4 ResponseStreamEvent union by its `type`
  discriminator.
- `OpenAiClient.ResponseMcpListToolsCompletedEvent` ->
  `OpenAiClient.ResponseStreamEvent`: The standalone event helper was removed
  from OpenAiClient; narrow the v4 ResponseStreamEvent union by its `type`
  discriminator.
- `OpenAiClient.ResponseMcpListToolsFailedEvent` ->
  `OpenAiClient.ResponseStreamEvent`: The standalone event helper was removed
  from OpenAiClient; narrow the v4 ResponseStreamEvent union by its `type`
  discriminator.
- `OpenAiClient.ResponseMcpListToolsInProgressEvent` ->
  `OpenAiClient.ResponseStreamEvent`: The standalone event helper was removed
  from OpenAiClient; narrow the v4 ResponseStreamEvent union by its `type`
  discriminator.
- `OpenAiClient.ResponseOutputItemAddedEvent` ->
  `Generated.ResponseOutputItemAddedEvent`: The event schema moved out of
  OpenAiClient into the regenerated OpenAI schema surface; re-check its v4
  Type/Encoded shape.
- `OpenAiClient.ResponseOutputItemDoneEvent` ->
  `Generated.ResponseOutputItemDoneEvent`: The event schema moved out of
  OpenAiClient into the regenerated OpenAI schema surface; re-check its v4
  Type/Encoded shape.
- `OpenAiClient.ResponseOutputTextAnnotationAddedEvent` ->
  `Generated.ResponseOutputTextAnnotationAddedEvent`: The event schema moved
  out of OpenAiClient into the regenerated OpenAI schema surface; re-check its
  v4 Type/Encoded shape.
- `OpenAiClient.ResponseOutputTextDeltaEvent` ->
  `OpenAiClient.ResponseStreamEvent`: The standalone event helper was removed
  from OpenAiClient; narrow the v4 ResponseStreamEvent union by its `type`
  discriminator.
- `OpenAiClient.ResponseOutputTextDoneEvent` ->
  `OpenAiClient.ResponseStreamEvent`: The standalone event helper was removed
  from OpenAiClient; narrow the v4 ResponseStreamEvent union by its `type`
  discriminator.
- `OpenAiClient.ResponseQueuedEvent` -> `Generated.ResponseQueuedEvent`: The
  event schema moved out of OpenAiClient into the regenerated OpenAI schema
  surface; re-check its v4 Type/Encoded shape.
- `OpenAiClient.ResponseReasoningSummaryPartAddedEvent` ->
  `Generated.ResponseReasoningSummaryPartAddedEvent`: The event schema moved
  out of OpenAiClient into the regenerated OpenAI schema surface; re-check its
  v4 Type/Encoded shape.
- `OpenAiClient.ResponseReasoningSummaryPartDoneEvent` ->
  `Generated.ResponseReasoningSummaryPartDoneEvent`: The event schema moved out
  of OpenAiClient into the regenerated OpenAI schema surface; re-check its v4
  Type/Encoded shape.
- `OpenAiClient.ResponseReasoningSummaryTextDeltaEvent` ->
  `Generated.ResponseReasoningSummaryTextDeltaEvent`: The event schema moved
  out of OpenAiClient into the regenerated OpenAI schema surface; re-check its
  v4 Type/Encoded shape.
- `OpenAiClient.ResponseReasoningSummaryTextDoneEvent` ->
  `Generated.ResponseReasoningSummaryTextDoneEvent`: The event schema moved out
  of OpenAiClient into the regenerated OpenAI schema surface; re-check its v4
  Type/Encoded shape.
- `OpenAiClient.ResponseReasoningTextDeltaEvent` ->
  `Generated.ResponseReasoningTextDeltaEvent`: The event schema moved out of
  OpenAiClient into the regenerated OpenAI schema surface; re-check its v4
  Type/Encoded shape.
- `OpenAiClient.ResponseReasoningTextDoneEvent` ->
  `Generated.ResponseReasoningTextDoneEvent`: The event schema moved out of
  OpenAiClient into the regenerated OpenAI schema surface; re-check its v4
  Type/Encoded shape.
- `OpenAiClient.ResponseRefusalDeltaEvent` ->
  `Generated.ResponseRefusalDeltaEvent`: The event schema moved out of
  OpenAiClient into the regenerated OpenAI schema surface; re-check its v4
  Type/Encoded shape.
- `OpenAiClient.ResponseRefusalDoneEvent` ->
  `Generated.ResponseRefusalDoneEvent`: The event schema moved out of
  OpenAiClient into the regenerated OpenAI schema surface; re-check its v4
  Type/Encoded shape.
- `OpenAiClient.ResponseWebSearchCallCompletedEvent` ->
  `Generated.ResponseWebSearchCallCompletedEvent`: The event schema moved out
  of OpenAiClient into the regenerated OpenAI schema surface; re-check its v4
  Type/Encoded shape.
- `OpenAiClient.ResponseWebSearchCallInProgressEvent` ->
  `Generated.ResponseWebSearchCallInProgressEvent`: The event schema moved out
  of OpenAiClient into the regenerated OpenAI schema surface; re-check its v4
  Type/Encoded shape.
- `OpenAiClient.ResponseWebSearchCallSearchingEvent` ->
  `Generated.ResponseWebSearchCallSearchingEvent`: The event schema moved out
  of OpenAiClient into the regenerated OpenAI schema surface; re-check its v4
  Type/Encoded shape.
- `OpenAiClient.StreamCompletionRequest` ->
  `OpenAiSchema.CreateResponse.Encoded`: The chat-completions request alias was
  removed; the v4 client uses the Responses API, with streaming inferred by
  OpenAiClient.createResponseStream.
- `OpenAiClient.SummaryPart` -> `OpenAiSchema.SummaryTextContent`: The
  client-local reasoning summary schema moved to the focused v4 OpenAiSchema
  module.
