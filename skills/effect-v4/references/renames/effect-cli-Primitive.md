<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/cli/Primitive` v3 → v4

- `Primitive.Primitive.PathExists` -> `mustExist?: boolean`: Use true for yes
  and omit for either; no cannot be represented exactly because false permits
  existing paths.
- `Primitive.Primitive.ValueType` ->
  `P extends Primitive.Primitive<infer A> ? A : never`: The named helper was
  removed; infer the value with a local conditional type.
- `Primitive.Primitive.Variance` -> `Primitive.Primitive.Variance`: The
  variance interface remains, but its brand key is internal; prefer
  Primitive\<A\> in user APIs.
- `Primitive.PrimitiveTypeId` -> `none`: The public Primitive type-id symbol
  was removed.
- `Primitive.boolean` -> `Primitive.Boolean`: Boolean is now a singleton value;
  defaults belong on Flag.Boolean or withDefault.
- `Primitive.choice` -> `Primitive.Choice`: Use the moved constructor.
- `Primitive.date` -> `Primitive.Date`: Date is now a singleton Primitive value.
- `Primitive.float` -> `Primitive.Finite`: Finite is now a singleton Primitive
  value and rejects non-finite numbers.
- `Primitive.getChoices` -> `none`: Choice introspection is internal in v4;
  retain alternatives in application code when needed.
- `Primitive.getHelp` -> `none`: Primitive-level help generation was removed
  from the public API.
- `Primitive.integer` -> `Primitive.Int`: Int is now a singleton Primitive
  value.
- `Primitive.isBool` -> `none`: The boolean Primitive predicate is internal in
  v4.
- `Primitive.text` -> `Primitive.String`: Renamed from text to String.
- `Primitive.validate` -> `primitive.parse(value)`: Parsing is now the
  Primitive.parse method over a string; defaults and case normalization moved
  out of this layer.
