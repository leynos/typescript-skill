<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/experimental/VariantSchema` v3 → v4

- `VariantSchema.Extract` -> `effect/schema/VariantSchema#Extract`: Import the
  retained helper from the v4 module; its erased schema constraint is
  Schema.Top.
- `VariantSchema.Field.Any` -> `effect/schema/VariantSchema#Field.Any`: Import
  the retained Field.Any helper type from the v4 unstable VariantSchema module.
- `VariantSchema.Field.Config` -> `effect/schema/VariantSchema#Field.Config`:
  Import the retained Field.Config helper type from the v4 unstable
  VariantSchema module.
- `VariantSchema.Field.Fields` -> `effect/schema/VariantSchema#Field.Fields`:
  Import the retained Field.Fields helper type from the v4 unstable
  VariantSchema module.
- `VariantSchema.Field.ValueAny` -> `effect/Schema#Top`: Use the core
  Schema.Top constraint for an arbitrary field value schema.
- `VariantSchema.FieldTypeId` -> `none`: The Field brand is private in v4; use
  VariantSchema.isField for narrowing.
- `VariantSchema.Struct.Fields` -> `effect/schema/VariantSchema#Struct.Fields`:
  Import the retained Struct.Fields helper type from the v4 unstable
  VariantSchema module.
- `VariantSchema.TypeId` -> `effect/schema/VariantSchema#TypeId`: Use the
  retained runtime value; in type position use typeof VariantSchema.TypeId.
- `VariantSchema.fromKey` -> `none`: Field-level fromKey was not ported; for
  whole-struct encoded-key renaming consider Schema.encodeKeys.
- `VariantSchema.fromKey.Rename` -> `none`: The fromKey rename helper was not
  ported; for whole-struct encoded-key renaming consider Schema.encodeKeys.
- `VariantSchema.make` -> `effect/schema/VariantSchema#make`: Import make from
  the v4 module; FieldOnly and FieldExcept take one key array and Union takes
  one member array.
