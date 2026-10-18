<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/sql/Model` v3 → v4

- `Model.Any` -> `effect/schema/Model#Any`: Moved; v4 schemas track
  DecodingServices and EncodingServices separately instead of one Context type.
- `Model.AnyNoContext` -> `effect/schema/Model#Any`: The distinct no-context
  alias was removed; Model.Any propagates decoding and encoding services.
  Constrain both service types to never when required.
- `Model.BooleanFromNumber` -> `effect/Schema#BooleanFromBit`: Use the core 0 |
  1 to boolean schema; Model.BooleanSqlite is the ready-made model field.
- `Model.Class` -> `effect/schema/Model#Class`: Moved; model variants remain
  select, insert, update, json, jsonCreate, and jsonUpdate.
- `Model.Date` -> `effect/schema/Model#Date`: Moved; still serializes
  DateTime.Utc as a YYYY-MM-DD string.
- `Model.DateTimeFromDate` -> `effect/Schema#DateTimeUtcFromDate`: Moved to
  core Schema and retains Date to DateTime.Utc conversion.
- `Model.Generated` -> `effect/schema/Model#GeneratedByDb`: Renamed and now
  read-only, with select and json variants only. Use Model.Field with select,
  update, and json to preserve writable v3 behavior.
- `Model.extract` -> `effect/schema/Model#extract`: Retained after moving the
  model variant helpers into core Effect's unstable schema package.
- `Model.fieldFromKey` -> `effect/Schema#encodeKeys`: The field helper was
  removed; apply encodeKeys to each concrete struct or model-variant schema
  that crosses the naming boundary.
- `Model.fields` -> `effect/schema/Model#fields`: Moved with the variant-model
  helpers into core Effect's unstable schema package.
- `Model.makeDataLoaders` -> `effect/sql/SqlModel#makeResolvers`: Returns
  RequestResolvers instead of callable loaders; execute with
  SqlResolver.request and use RequestResolver delay/batch combinators for
  batching controls. The insert resolver requires model decoding services as
  well as insert-schema encoding services.
