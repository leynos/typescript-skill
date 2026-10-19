<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `effect/Brand` v3 → v4

- `Brand.Brand` -> `Brand.Brand`: Still exported, but v4 brand keys are strings
  rather than symbols.
- `Brand.Brand.BrandErrors` -> `Brand.BrandError`: Validation now returns one
  BrandError wrapping a SchemaIssue.Issue instead of an error array.
- `Brand.Brand.RefinementError` -> `Schema.FilterIssue`: Brand.make validators
  use Schema filter output instead of the old message and meta record.
- `Brand.BrandTypeId` -> `none`: The public marker was removed; the v4 brand
  type id is private.
- `Brand.Branded` -> `Brand.Branded`: Still exported, with the brand key
  restricted to string.
- `Brand.RefinedConstructorsTypeId` -> `none`: The public refined-constructor
  marker was removed.
- `Brand.all` -> `Brand.all`: Still exported; combines multiple brand
  constructors and checks.
- `Brand.error` -> `Brand.make`: Return a string or Schema filter issue
  directly from a Brand.make validator.
- `Brand.nominal` -> `Brand.nominal`: Still exported; the constructor's either
  method is now result.
- `Brand.refined` -> `Brand.make`: Use Brand.make for custom validation or
  Brand.check for Schema checks.
- `Brand.unbranded` -> `Function.cast`: Brands are runtime-identical to their
  base value; cast explicitly when an unbranded type is required.
