# Schema library selection

Choose by what the boundary needs. Every library below parses `unknown` into a
typed value and reports issues; they differ in inference style, transforms,
bundle size, and ecosystem.

| Need                                             | Reach for                                             | Note                                                              |
| ------------------------------------------------ | ----------------------------------------------------- | ----------------------------------------------------------------- |
| One or two small shapes, no dependency wanted    | Hand-written parse function                           | Return the typed value or throw a typed error; no boolean guards  |
| Rich inference, transforms, wide ecosystem       | Zod 4 (`zod`)                                         | Classic API for applications; `zod/mini` when bundle size matters |
| Smallest browser bundle, tree-shakeable          | valibot                                               | Function-style API; shapes built from pipes                       |
| Schema-first codebase with services and layers   | Effect `Schema`                                       | Only when the codebase already uses Effect                        |
| Runtime types written like TypeScript            | ArkType                                               | Fast; different error vocabulary                                  |
| JSON Schema is the contract (OpenAPI, Ajv users) | Ajv with generated types, or Zod's JSON Schema output | Keep one source of truth; generate the other                      |

_Table 1: Boundary needs and the library that fits._

## Selection questions

1. Is there already a schema library in the repository? Use it. Two libraries
   at different boundaries is a maintenance cost with no upside.
2. Does the boundary need transforms (string to `Date`, snake to camel)? Zod
   and valibot both carry them; a hand-written parser does them in the
   converter instead.
3. Does the schema need to be exported as JSON Schema or OpenAPI? Zod 4
   generates it; otherwise the JSON Schema is the source and types are
   generated from it.
4. Is bundle size a constraint on this boundary (browser, worker, Electron
   renderer)? valibot or `zod/mini`; measure rather than assume.
5. Will the same schema validate on both sides of a channel? Put it in a
   shared package and import it from both; never copy it.

## Zod 4 deep dive

Zod 4 is the catalogue's default for application boundaries. Its deep dive owns
migration from Zod 3, the classic versus mini split, codecs, and JSON Schema
output: [`zod4-typescript`](../../zod4-typescript/SKILL.md). Load it when the
question is about Zod itself rather than where a boundary belongs.

## Hand-written parse

```ts
interface Point {
  readonly x: number;
  readonly y: number;
}

export function parsePoint(raw: unknown): Point {
  if (typeof raw !== "object" || raw === null) {
    throw new ParseError("point", "expected an object");
  }
  const { x, y } = raw as { x?: unknown; y?: unknown };
  if (typeof x !== "number" || typeof y !== "number") {
    throw new ParseError("point", "x and y must be numbers");
  }
  return { x, y };
}
```

The single `as` narrows `object` to a shape with optional unknown fields so the
destructuring is typed; it is not a claim about the data. At the third shape
like this, switch to a library.
