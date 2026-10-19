# JSON Schema conversion options

## Zod → JSON Schema (`z.toJSONSchema()`)

```ts
z.toJSONSchema(schema, options?)
```

### Options

| Option            | Type                                                                         | Description                                                              |
| ----------------- | ---------------------------------------------------------------------------- | ------------------------------------------------------------------------ |
| `target`          | `"draft-2020-12"` (default) \| `"draft-7"` \| `"draft-4"` \| `"openapi-3.0"` | Which dialect's `$schema` and keywords to emit                           |
| `metadata`        | `$ZodRegistry`                                                               | Registry whose entries supply `title`, `description`, `examples`, `id`   |
| `unrepresentable` | `"throw"` (default) \| `"any"`                                               | What to do with `z.date()`, `z.bigint()`, transforms: throw or emit `{}` |
| `cycles`          | `"ref"` (default) \| `"throw"`                                               | Recursive schemas become `$ref`s, or conversion fails                    |
| `reused`          | `"inline"` (default) \| `"ref"`                                              | Whether a schema used twice is inlined or hoisted into `$defs`           |
| `io`              | `"output"` (default) \| `"input"`                                            | Which side of transforms and pipes to represent                          |
| `override`        | `(ctx) => void`                                                              | Post-process each generated node                                         |

Checked against `zod@4.6.7` on 2026-10-18. Unknown option names are ignored
silently, so a misspelled option changes nothing and reports nothing.

### Metadata propagation

Any metadata stored in `z.globalRegistry` (via `.meta()` or `.describe()`) is
automatically included in the JSON Schema output.

```ts
const schema = z.object({
  name: z.string().meta({ title: "User name", examples: ["alice"] }),
  age: z.int().meta({ description: "Age in years" }),
});

z.toJSONSchema(schema);
// {
//   type: "object",
//   properties: {
//     name: { type: "string", title: "User name", examples: ["alice"] },
//     age: { type: "integer", description: "Age in years", minimum: ..., maximum: ... },
//   },
//   required: ["name", "age"],
//   additionalProperties: false,
// }
```

### Named definitions via `id` metadata

Give a schema an `id` in the global registry and every use of it becomes a
`$ref` into `$defs` under that name:

```ts
const Address = z.object({ street: z.string(), city: z.string() }).meta({ id: "Address" });
const User = z.object({ name: z.string(), address: Address, home: Address });

z.toJSONSchema(User);
// properties.address → { "$ref": "#/$defs/Address" }, $defs.Address → the object
```

Without an `id`, a schema used twice is inlined; `{ reused: "ref" }` hoists it
into `$defs` under a generated name. To emit a set of named schemas at once,
pass a registry: `z.toJSONSchema(myRegistry)` returns
`{ schemas: { <id>: … } }`.

### Input or output side

`io` controls how transforms and pipes appear in the generated schema:

- `"output"` (default): the output side; a transform is unrepresentable and
  throws unless `unrepresentable: "any"` is set
- `"input"`: the input side, which is what a request validator should emit

### Schema type mapping

Zod 4 maps schemas to JSON Schema as follows (non-exhaustive):

| Zod schema               | JSON Schema                           |
| ------------------------ | ------------------------------------- |
| `z.string()`             | `{ type: "string" }`                  |
| `z.email()`              | `{ type: "string", format: "email" }` |
| `z.int()`                | `{ type: "integer", ... }`            |
| `z.number()`             | `{ type: "number" }`                  |
| `z.boolean()`            | `{ type: "boolean" }`                 |
| `z.null()`               | `{ type: "null" }`                    |
| `z.array()`              | `{ type: "array", items: ... }`       |
| `z.object()`             | `{ type: "object", ... }`             |
| `z.union()`              | `{ anyOf: [...] }`                    |
| `z.xor()`                | `{ oneOf: [...] }`                    |
| `z.discriminatedUnion()` | `{ anyOf: [...] }` with discriminator |
| `z.literal()`            | `{ const: ... }` or `{ enum: [...] }` |
| `z.optional()`           | removes from `required`               |
| `z.nullable()`           | adds `null` to type                   |

### `additionalProperties`

By default, `z.object()` produces `additionalProperties: false`.
`z.looseObject()` produces `additionalProperties: true`. `z.strictObject()`
produces `additionalProperties: false`.

## JSON Schema → Zod (`z.fromJSONSchema()`)

**Experimental** (4.3+). May change in minor releases. No guarantee of
round-trip fidelity.

```ts
const zodSchema = z.fromJSONSchema(jsonSchema, options?);
```

### Supported drafts

- JSON Schema draft-2020-12
- JSON Schema draft-7
- JSON Schema draft-4
- OpenAPI 3.0

### Options

| Option     | Type          | Description                     |
| ---------- | ------------- | ------------------------------- |
| `errorMap` | `ZodErrorMap` | Custom error map for the schema |

### Limitations

- No 1:1 round-trip soundness: `schema → toJSONSchema → fromJSONSchema` may not
  produce an equivalent schema, because some Zod features (refinements,
  transforms, codecs) have no JSON Schema representation, and vice versa.
- Complex JSON Schema features like `$dynamicRef`, `if/then/else`, and certain
  `patternProperties` combinations may not convert faithfully.
- The returned schema is loosely typed (`ZodTypeAny`) — you lose the
  compile-time type information that hand-authored Zod schemas provide.

### Practical use case

Useful for consuming external JSON Schema definitions (e.g. from a schema
registry or OpenAPI spec) and applying Zod's runtime validation:

```ts
const externalSchema = await fetch("/api/schema/user").then(r => r.json());
const validator = z.fromJSONSchema(externalSchema);

const result = validator.safeParse(untrustedData);
```
