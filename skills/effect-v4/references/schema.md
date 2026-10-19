# Schema in Effect 4

`Schema` is now part of the core `effect` package and stable. Every schema is a
codec with a decoded `Type`, an `Encoded` form, and the services it needs while
decoding (`DecodingServices`) and encoding (`EncodingServices`). The full
upstream guide lives at `packages/effect/SCHEMA.md` in the Effect repository;
the v3→v4 mapping is in `upstream/migration/schema.md` (verbatim) and
`renames/effect-Schema.md`.

All blocks below compile against `effect@4.0.5`.

## Contents

1. Primitives, structs, optionality
2. Literals, unions, tagged unions, records, tuples
3. Classes, opaque types, brands
4. Checks (filters) and refinements
5. Transformations and defaults
6. Decoding and encoding APIs
7. Interop: JSON strings, JSON Schema, Standard Schema
8. Migration pitfalls

## 1. Primitives, structs, optionality

```ts
import { Schema } from "effect"

export const User = Schema.Struct({
  id: Schema.Int,
  name: Schema.NonEmptyString,
  email: Schema.String,
  nickname: Schema.optional(Schema.String),     // { nickname?: string | undefined }
  locale: Schema.optionalKey(Schema.String),    // exact optional key: { locale?: string }
  manager: Schema.NullOr(Schema.Int),           // number | null
  tags: Schema.Array(Schema.String),
  createdAt: Schema.DateFromString              // ISO string on the wire, Date in memory
})

export type User = typeof User.Type
export type UserEncoded = typeof User.Encoded
```

Primitive catalogue (abridged): `String`, `Number` (accepts `NaN`/`Infinity`),
`Finite`, `Int`, `Boolean`, `BigInt`, `Symbol`, `Date` (a `Date` value),
`DateFromString`, `DateFromMillis`, `DateTimeUtcFromString`, `Duration`,
`DurationFromMillis`, `NumberFromString`, `FiniteFromString`,
`BigIntFromString`, `URL`, `URLFromString`, `Uint8ArrayFromBase64`, `Trim`,
`Trimmed`, `NonEmptyString`, `Natural`, `Port`, `Json`, `Unknown`, `Never`,
`Redacted`, `Option`, `OptionFromNullOr`, `OptionFromOptionalKey`, `Result`,
`Defect`.

The `*FromSelf` suffix is gone: v3 `DateFromSelf` is v4 `Date`,
`OptionFromSelf` is `Option`, and so on. v3 `Schema.Date` (string→Date) is v4
`Schema.DateFromString`.

Struct surgery uses `mapFields` with the `Struct` helpers:

```ts
import { Schema, Struct } from "effect"

const Base = Schema.Struct({ id: Schema.Int, name: Schema.String, secret: Schema.String })

export const Public = Base.mapFields(Struct.omit(["secret"]))
export const IdOnly = Base.mapFields(Struct.pick(["id"]))
export const Patch = Base.mapFields(Struct.map(Schema.optionalKey))   // v3 partialWith({ exact: true })
export const Extended = Base.mapFields(Struct.assign({ role: Schema.String })) // v3 extend
```

## 2. Literals, unions, tagged unions, records, tuples

Variadic constructors became array-taking.

```ts
import { Schema } from "effect"

export const Role = Schema.Literals(["admin", "member", "guest"])
export const Staff = Role.pick(["admin", "member"])
export const One = Schema.Literal("one")
export const Id = Schema.Union([Schema.Int, Schema.NonEmptyString])
export const Pair = Schema.Tuple([Schema.String, Schema.Number])
export const Scores = Schema.Record(Schema.String, Schema.Number)

// Discriminated union with matching helpers built in
export const Shape = Schema.TaggedUnion({
  Circle: { radius: Schema.Finite },
  Rectangle: { width: Schema.Finite, height: Schema.Finite }
})
export type Shape = typeof Shape.Type
export const area = (s: Shape) =>
  Shape.match(s, {
    Circle: (c) => Math.PI * c.radius ** 2,
    Rectangle: (r) => r.width * r.height
  })

// Or augment an existing union of tagged structs
const A = Schema.TaggedStruct("A", { value: Schema.Number })
const B = Schema.TaggedStruct("B", { name: Schema.String })
export const AB = Schema.Union([A, B]).pipe(Schema.toTaggedUnion("_tag"))
```

## 3. Classes, opaque types, brands

```ts
import { Schema } from "effect"

export class Person extends Schema.Class<Person>("myapp/Person")({
  name: Schema.NonEmptyString,
  age: Schema.Int
}) {
  get greeting() {
    return `Hello, ${this.name}`
  }
}

export class Employee extends Person.extend<Employee>("myapp/Employee")({
  team: Schema.String
}) {}

// Constructor validates; throws on invalid input
export const ada = new Person({ name: "Ada", age: 36 })

// _tag populated automatically
export class Created extends Schema.TaggedClass<Created>()("Created", { id: Schema.String }) {}

// Nominal type over a struct without class semantics
export class Point extends Schema.Opaque<Point>()(Schema.Struct({ x: Schema.Number, y: Schema.Number })) {}

// Brands are type-level only; pair with a check for runtime validation
export const UserId = Schema.String.pipe(Schema.check(Schema.isUUID()), Schema.brand("UserId"))
export type UserId = typeof UserId.Type
```

Errors are classes too: `Schema.TaggedError<Self>()(tag, fields)` and
`Schema.Error<Self>(identifier)(fields)` — see `core.md` §2.

## 4. Checks and refinements

Filters gained an `is` prefix and attach via `check`:

```ts
import { Option, Schema } from "effect"

export const Age = Schema.Int.check(Schema.isBetween({ minimum: 0, maximum: 150 }))
export const Username = Schema.String.pipe(
  Schema.check(Schema.isMinLength(3), Schema.isMaxLength(32), Schema.isPattern(/^[a-z0-9_]+$/))
)
export const Even = Schema.Int.check(Schema.makeFilter((n) => n % 2 === 0 || "expected an even number"))

// Cross-field validation, reporting at a nested path
export const Signup = Schema.Struct({ password: Schema.String, confirm: Schema.String }).check(
  Schema.makeFilter((o) =>
    o.password === o.confirm ? undefined : { path: ["confirm"], issue: "passwords must match" }
  )
)

// Type-narrowing refinement
export const SomeString = Schema.Option(Schema.String).pipe(Schema.refine(Option.isSome))
```

A `makeFilter` predicate may return `true`/`undefined` (ok), `false`, a message
string, a `SchemaIssue.Issue`, `{ path, issue }`, or an array of those. Removed
filters: `positive`, `negative`, `nonNegative`, `nonPositive` — use
`isGreaterThan(0)`, `isGreaterThanOrEqualTo(0)`, and so on.

## 5. Transformations and defaults

`transform` / `transformOrFail` / `compose` collapse into `decodeTo`:

```ts
import { Effect, Number, Option, Schema, SchemaGetter, SchemaIssue, SchemaTransformation } from "effect"

// Pure, total transformation
export const OnOff = Schema.Literals(["on", "off"]).pipe(
  Schema.decodeTo(
    Schema.Boolean,
    SchemaTransformation.transform({
      decode: (s) => s === "on",
      encode: (b) => (b ? "on" : "off")
    })
  )
)

// Fallible transformation
export const Num = Schema.String.pipe(
  Schema.decodeTo(Schema.Number, {
    decode: SchemaGetter.transformEffect((s: string) =>
      Option.match(Number.parse(s), { // Number.parse returns Option<number> in v4
        onNone: () => Effect.fail(new SchemaIssue.InvalidValue({ message: "not a number" }, s)),
        onSome: Effect.succeed
      })
    ),
    encode: SchemaGetter.String()
  })
)

// Defaults: decoding defaults fill missing input; constructor defaults fill `make`/`new`
export const Settings = Schema.Struct({
  retries: Schema.Int.pipe(Schema.withDecodingDefault(Effect.succeed(3))),
  label: Schema.String.pipe(Schema.optionalKey, Schema.withConstructorDefault(Effect.succeed("default")))
})
```

v3 `optionalWith` translations:

| v3 options                 | v4                                                                                     |
| -------------------------- | -------------------------------------------------------------------------------------- |
| `{ exact: true }`          | `Schema.optionalKey(s)`                                                                |
| `{ default: () => x }`     | `s.pipe(Schema.withDecodingDefaultType(Effect.succeed(x)))`                            |
| `{ exact: true, default }` | `s.pipe(Schema.withDecodingDefaultTypeKey(Effect.succeed(x)))`                         |
| `{ nullable: true, ... }`  | `optional(NullOr(s))` + `decodeTo` filtering null — see `upstream/migration/schema.md` |
| `{ as: "Option" }`         | `Schema.OptionFromOptional(s)` / `OptionFromOptionalKey(s)`                            |

## 6. Decoding and encoding

```ts
import { Effect, Schema } from "effect"

const Payload = Schema.Struct({ id: Schema.Int, name: Schema.String })

export const viaEffect = Schema.decodeUnknownEffect(Payload)   // (u) => Effect<A, SchemaError, R>
export const viaSync = Schema.decodeUnknownSync(Payload)       // throws
export const viaExit = Schema.decodeUnknownExit(Payload)       // Exit<A, SchemaError>
export const viaOption = Schema.decodeUnknownOption(Payload)
export const viaResult = Schema.decodeUnknownResult(Payload)
export const encode = Schema.encodeEffect(Payload)
export const isPayload = Schema.is(Payload)                    // type guard on the decoded Type

export const handle = Effect.fn("handle")(function*(body: unknown) {
  const p = yield* viaEffect(body).pipe(
    Effect.mapError((e) => new Error(e.message)) // SchemaError#message is a formatted report
  )
  return p.id
})
```

Naming rule: `decode*` takes `Encoded`, `decodeUnknown*` takes `unknown`;
suffix chooses the result shape (`Effect`, `Sync`, `Exit`, `Option`, `Result`,
`Promise`). `validate*` is gone — decode with `Schema.toType(schema)` instead.
`asserts(schema, u)` is now two-argument.

## 7. Interop

```ts
import { Schema } from "effect"

const Event = Schema.Struct({ kind: Schema.Literals(["a", "b"]), at: Schema.DateFromString })

export const EventFromJson = Schema.fromJsonString(Event)        // string <-> Event (v3 parseJson(schema))
export const jsonSchema = Schema.toJsonSchemaDocument(Event)     // JSON Schema document
export const standard = Schema.toStandardSchemaV1(Event)         // for tRPC, Hono validators, etc.
export const jsonCodec = Schema.toCodecJson(Event)               // canonical JSON codec
```

`SchemaRepresentation` (in core) imports/exports JSON Schema drafts
04/07/2020-12 and OpenAPI 3.0/3.1 and generates TypeScript; AI structured
output builds on it.

## 8. Migration pitfalls

- `Schema.Date` silently changed meaning (string→Date became Date→Date). Grep
  for it.
- `Union`, `Literal(…many)`, `Tuple`, `TemplateLiteral` are array-taking; v3
  calls may still type-check in odd ways, so fix them mechanically.
- `Record({ key, value })` → `Record(key, value)`.
- `annotations({...})` → `annotate({...})`; `compose` → `decodeTo`;
  `encodedSchema`/`typeSchema` → `toEncoded`/`toType`; `asSchema` →
  `revealCodec`.
- `ParseResult` is gone: issues are `SchemaIssue.*`, the failure type is
  `Schema.SchemaError`, formatters live in `SchemaIssue`.
- `Schema.Data(...)` is removed — structural equality is the default in v4.
- Arbitraries come from `effect/Arbitrary` (native), not the fast-check bridge.
