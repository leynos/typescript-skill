<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/sql-mssql/Parameter` v3 → v4

- `Parameter.Parameter` -> `@effect/sql-mssql/Parameter#Parameter`: Retained;
  the phantom brand key was renamed from ParameterId to TypeId.
- `Parameter.ParameterId` -> `@effect/sql-mssql/Parameter#TypeId`: Renamed; use
  TypeId for direct brand-key and type references.
