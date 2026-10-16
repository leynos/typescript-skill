<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/ai/Telemetry` v3 → v4

- `Telemetry.AllAttributes` -> `none`: Removed. Use
  Telemetry.GenAITelemetryAttributeOptions for the grouped options accepted by
  Telemetry.addGenAIAnnotations, or Telemetry.GenAITelemetryAttributes for the
  prefixed gen\_ai.\* span attribute keys.
- `Telemetry.BaseAttributes` -> `Telemetry.ProviderAttributes`: gen\_ai.system
  was replaced by gen\_ai.provider.name. Pass provider: { name } instead of
  system; legacy system values are not mapped.
- `Telemetry.GenAITelemetryAttributeOptions` ->
  `Telemetry.GenAITelemetryAttributeOptions`: The system and token options were
  removed. Use provider: { name } for gen\_ai.provider.name; gen\_ai.token.type
  has no span replacement. The new output option writes gen\_ai.output.type.
- `Telemetry.GenAITelemetryAttributes` -> `Telemetry.GenAITelemetryAttributes`:
  The flat span attribute keys changed: replace gen\_ai.system with
  gen\_ai.provider.name and remove gen\_ai.token.type. gen\_ai.output.type
  records text or json. Update code constructing or indexing this attribute
  type.
- `Telemetry.TokenAttributes` -> `none`: Removed with the token option.
  gen\_ai.token.type is not a span attribute in the current OpenTelemetry GenAI
  conventions.
- `Telemetry.WellKnownSystem` -> `Telemetry.WellKnownProviderName`: Values
  follow gen\_ai.provider.name: az.ai.inference, az.ai.openai, gemini,
  vertex\_ai and xai became azure.ai.inference, azure.ai.openai, gcp.gemini,
  gcp.vertex\_ai and x\_ai.
