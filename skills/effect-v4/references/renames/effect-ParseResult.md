<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `effect/ParseResult` v3 → v4

- `ParseResult.ArrayFormatterIssue` ->
  `StandardSchemaV1.FailureResult["issues"][number]`: Use the Standard Schema
  issue shape returned by makeFormatterStandardSchemaV1.
- `ParseResult.Composite` -> `SchemaIssue.Composite`: Composite parse failures
  moved to SchemaIssue. The v4 constructor takes the failing AST and an array
  of nested issues; input is retained only when reportInput is enabled.
- `ParseResult.DeclarationDecodeUnknown` -> `SchemaGetter.Getter`: Custom
  declaration decoding now uses SchemaGetter values and Schema.declare
  annotations. Getter is a tagged union, not a constructor; use
  transformOptionalEffect for an Option-to-Effect decoder. Use standalone
  SchemaGetter.run, map, and compose instead of instance methods.
- `ParseResult.DecodeUnknown` -> `Schema.decodeUnknownEffect`: Use the function
  type returned by Schema.decodeUnknownEffect.
- `ParseResult.Forbidden` -> `SchemaIssue.Forbidden`: Forbidden failures use
  the v4 SchemaIssue class; its constructor takes issue annotations plus
  optional input and parse options, retaining input only when reportInput is
  true.
- `ParseResult.Missing` -> `SchemaIssue.MissingKey`: Missing-key failures use
  the v4 SchemaIssue class.
- `ParseResult.ParseError` -> `Schema.SchemaError`: The parse error moved onto
  Schema; use Schema.isSchemaError for runtime narrowing.
- `ParseResult.ParseErrorTypeId` -> `none`: The public symbol was removed; use
  Schema.isSchemaError for runtime narrowing.
- `ParseResult.ParseIssue` -> `SchemaIssue.Issue`: The structured parse issue
  union moved to SchemaIssue.
- `ParseResult.ParseResultFormatter` -> `SchemaIssue.Formatter`: Issue
  formatter types moved to SchemaIssue.
- `ParseResult.Pointer` -> `SchemaIssue.Pointer`: Path-qualified failures moved
  to SchemaIssue. Construct them with the property path and nested issue;
  rejected input belongs to the nested issue when reportInput is enabled.
- `ParseResult.Refinement` -> `SchemaIssue.Filter`: Refinement failures are
  represented as filter issues in v4.
- `ParseResult.SingleOrNonEmpty` -> `ReadonlyArray`: This ParseResult helper
  type was removed; use an explicit value-or-non-empty-array type when still
  needed.
- `ParseResult.Transformation` -> `SchemaIssue.Encoding`: Transformation-stage
  failures are Encoding issues in v4. They retain the failing AST and nested
  issue; the old Encoded, Transformation, and Type kind discriminator was
  removed.
- `ParseResult.Type` -> `SchemaIssue.InvalidType`: Type mismatches use the v4
  SchemaIssue class.
- `ParseResult.Unexpected` -> `SchemaIssue.UnexpectedKey`: Unexpected object
  keys use the v4 SchemaIssue class.
- `ParseResult.decode` -> `Schema.decodeEffect`: Parsing helpers moved onto
  Schema; the effectful decoder fails with SchemaError.
- `ParseResult.decodeEither` -> `Schema.decodeExit`: Either parsing was
  replaced by Exit parsing.
- `ParseResult.decodePromise` -> `Schema.decodePromise`: Parsing helpers moved
  onto Schema and now fail with SchemaError.
- `ParseResult.decodeSync` -> `Schema.decodeSync`: Parsing helpers moved onto
  Schema and now throw SchemaError.
- `ParseResult.decodeUnknownEither` -> `Schema.decodeUnknownExit`: Either
  parsing was replaced by Exit parsing.
- `ParseResult.decodeUnknownPromise` -> `Schema.decodeUnknownPromise`: Parsing
  helpers moved onto Schema and now reject with SchemaError.
- `ParseResult.decodeUnknownSync` -> `Schema.decodeUnknownSync`: Parsing
  helpers moved onto Schema and now throw SchemaError.
- `ParseResult.eitherOrUndefined` -> `none`: This ParseResult internal
  optimization was removed; use Effect, Exit, Option, or Result combinators
  directly.
- `ParseResult.encode` -> `Schema.encodeEffect`: Encoding helpers moved onto
  Schema; the effectful encoder fails with SchemaError.
- `ParseResult.encodeEither` -> `Schema.encodeExit`: Either encoding was
  replaced by Exit encoding.
- `ParseResult.encodeSync` -> `Schema.encodeSync`: Encoding helpers moved onto
  Schema and now throw SchemaError.
- `ParseResult.encodeUnknownEither` -> `Schema.encodeUnknownExit`: Either
  encoding was replaced by Exit encoding.
- `ParseResult.encodeUnknownSync` -> `Schema.encodeUnknownSync`: Encoding
  helpers moved onto Schema and now throw SchemaError.
- `ParseResult.fail` -> `Effect.fail`: Schema transformations now use Effect
  and fail with SchemaIssue.Issue.
- `ParseResult.flatMap` -> `Effect.flatMap`: Schema transformations now use
  Effect combinators.
- `ParseResult.isComposite` -> `SchemaIssue.Composite`: Narrow with instanceof
  SchemaIssue.Composite or inspect the issue \_tag.
- `ParseResult.isParseError` -> `Schema.isSchemaError`: ParseError was replaced
  by SchemaError.
- `ParseResult.map` -> `Effect.map`: Schema transformations now use Effect
  combinators.
- `ParseResult.orElse` -> `Effect.orElse`: Schema transformations now use
  Effect combinators.
- `ParseResult.succeed` -> `Effect.succeed`: Schema transformations now use
  Effect.
- `ParseResult.try` -> `Effect.try`: Schema transformations now use Effect and
  map thrown errors to SchemaIssue values.
