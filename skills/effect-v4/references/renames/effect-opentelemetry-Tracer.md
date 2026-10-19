<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/opentelemetry/Tracer` v3 → v4

- `Tracer.OtelTraceFlags` -> `OtelTracer.OtelTraceFlags`: The service moved
  with the module and is now declared as a Context.Service class.
- `Tracer.OtelTraceState` -> `OtelTracer.OtelTraceState`: The service moved
  with the module and is now declared as a Context.Service class.
- `Tracer.OtelTracer` -> `OtelTracer.OtelTracer`: The service moved with the
  renamed module and is now declared as a Context.Service class.
- `Tracer.OtelTracerProvider` -> `OtelTracer.OtelTracerProvider`: The service
  moved with the renamed module and is now declared as a Context.Service class.
- `Tracer.layer` -> `OtelTracer.layer`: The Tracer module was renamed to
  OtelTracer; this still creates an OpenTelemetry tracer and installs it as
  Effect's tracer.
- `Tracer.layerTracer` -> `OtelTracer.layerTracer`: The Tracer module was
  renamed to OtelTracer; this layer still creates only the OpenTelemetry tracer
  service.
- `Tracer.make` -> `OtelTracer.make`: The constructor remains in the renamed
  OtelTracer module.
