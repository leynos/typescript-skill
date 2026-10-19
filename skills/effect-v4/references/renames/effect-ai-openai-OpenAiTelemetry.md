<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/ai-openai/OpenAiTelemetry` v3 → v4

- `OpenAiTelemetry.AllAttributes` -> `none`: Removed. Use
  OpenAiTelemetry.OpenAiTelemetryAttributeOptions for the grouped options
  accepted by OpenAiTelemetry.addGenAIAnnotations, or
  OpenAiTelemetry.OpenAiTelemetryAttributes for the prefixed span attribute
  keys.
- `OpenAiTelemetry.OpenAiTelemetryAttributes` ->
  `OpenAiTelemetry.OpenAiTelemetryAttributes`: Use openai.request.\* for
  request keys and openai.response.\* for response keys instead of
  gen\_ai.openai.\*. The response-format attribute was removed; use
  gen\_ai.output.type from LanguageModel instead.
- `OpenAiTelemetry.RequestAttributes` -> `OpenAiTelemetry.RequestAttributes`:
  Attributes are written under openai.request.\* instead of
  gen\_ai.openai.request.\*. responseFormat was removed; LanguageModel records
  gen\_ai.output.type for every provider.
- `OpenAiTelemetry.WellKnownResponseFormat` -> `Telemetry.WellKnownOutputType`:
  The response format is no longer a telemetry option. LanguageModel records
  gen\_ai.output.type as text or json from the requested response format.
