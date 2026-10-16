<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/ai/Prompt` v3 → v4

- `Prompt.FilePart` -> `Prompt.FilePart`: Moved to effect/ai/Prompt with the
  same file-part model and schema; update the module import.
- `Prompt.FromJson` -> `Schema.fromJsonString(Prompt.Prompt)`: The
  module-specific JSON schema was removed. Compose the general v4 JSON-string
  codec with the public Prompt codec.
- `Prompt.MessageContentFromString` -> `Prompt.ContentFromString`: Renamed in
  effect/ai/Prompt. It still decodes a string to a non-empty array containing
  one TextPart and encodes the first part's text.
- `Prompt.MessageTypeId` -> `Prompt.isMessage`: The message type id is private
  in v4. Use the public isMessage guard for runtime refinement instead of
  importing or inspecting the marker.
- `Prompt.Part` -> `Prompt.Part`: Moved to effect/ai/Prompt. The union now also
  includes tool-approval request and response parts.
- `Prompt.PartEncoded` -> `Prompt.PartEncoded`: Moved to effect/ai/Prompt. The
  encoded union now also includes tool-approval request and response parts.
- `Prompt.PartTypeId` -> `Prompt.isPart`: The part type id is private in v4.
  Use the public isPart guard for runtime refinement instead of importing or
  inspecting the marker.
- `Prompt.PromptFromSelf` -> `Prompt.Prompt`: The standalone declared from-self
  schema was removed. Use the public Prompt codec for prompt validation and
  encoding, or Prompt.isPrompt when only runtime refinement is needed.
- `Prompt.ReasoningPart` -> `Prompt.ReasoningPart`: Moved to effect/ai/Prompt
  with the same reasoning-part model and schema; update the module import.
- `Prompt.TextPart` -> `Prompt.TextPart`: Moved to effect/ai/Prompt with the
  same text-part model and schema; update the module import.
- `Prompt.ToolCallPart` -> `Prompt.ToolCallPart`: Moved to effect/ai/Prompt
  with the same tool-call model and schema; update the module import.
- `Prompt.ToolResultPartEncoded` -> `Prompt.ToolResultPartEncoded`: Moved to
  effect/ai/Prompt, but providerExecuted was removed from the encoded prompt
  tool-result shape.
- `Prompt.TypeId` -> `Prompt.isPrompt`: The Prompt type id is private in v4 and
  its internal literal changed. Use the public isPrompt guard instead of
  importing or inspecting the marker.
- `Prompt.makePart` -> `Prompt.makePart`: Moved to effect/ai/Prompt. The
  generic constructor also supports the new tool-approval request and response
  part variants.
- `Prompt.merge` -> `Prompt.concat`: Renamed in v4. concat preserves the old
  dual API and concatenates the messages from a Prompt with additional raw
  input.
