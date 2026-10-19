<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/platform/UrlParams` v3 → v4

- `UrlParams.CoercibleRecord` -> `UrlParams.CoercibleRecord<A>`: The recursive
  interface became a generic mapped type preserving the input shape.
- `UrlParams.Input` -> `UrlParams.Input`: Retained and broadened to include
  UrlParams itself.
- `UrlParams.UrlParams` -> `UrlParams.UrlParams`: Import UrlParams from
  effect/http. It is now a branded iterable object with a params field rather
  than a ReadonlyArray; construct it with UrlParams.make or UrlParams.fromInput.
- `UrlParams.makeUrl` -> `Url.make`: Moved to Url, returns Result, and takes
  string | undefined for the hash.
- `UrlParams.schemaFromSelf` -> `Schema.UrlParams`: The declaration schema for
  the v4 wrapper moved to effect/Schema.
- `UrlParams.schemaFromString` ->
  `Schema.String.pipe(Schema.decodeTo(Schema.UrlParams, { decode: SchemaGetter.transform((s) => UrlParams.fromInput(new URLSearchParams(s))), encode: SchemaGetter.transform(UrlParams.toString) }))`:
  No prebuilt string codec remains; recreate it by transforming between a
  query string and UrlParams.
- `UrlParams.schemaJson` ->
  `Schema.JsonFromUrlParamsField(field).pipe(Schema.decodeTo(schema), Schema.decodeEffect)`:
  The field codec moved to effect/Schema. Compose it with the target schema,
  then decode it.
- `UrlParams.schemaParse` ->
  `UrlParamsFromString.pipe(Schema.decodeTo(Schema.RecordFromUrlParams.pipe(Schema.decodeTo(schema))))`:
  Recreate the removed helper by composing the string, record, and target
  codecs.
- `UrlParams.schemaRecord` ->
  `Schema.RecordFromUrlParams.pipe(Schema.decodeTo(schema))`:
  RecordFromUrlParams is a base codec in effect/Schema; compose it with the
  target schema.
- `UrlParams.schemaStruct` ->
  `Schema.RecordFromUrlParams.pipe(Schema.decodeTo(schema), Schema.decodeEffect)`:
  Compose the record codec from effect/Schema with the target schema and
  decode it.
- `UrlParams.toString` -> `UrlParams.toString`: Retained and broadened to
  accept any UrlParams.Input.
