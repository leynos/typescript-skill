# Generated code

## One owner, one of two states

| State          | Tracked | Hand-edited | Build step                         | CI check                                |
| -------------- | ------- | ----------- | ---------------------------------- | --------------------------------------- |
| Tracked output | Yes     | Never       | Regenerate on schema change        | Regenerate, then `git diff --exit-code` |
| Ignored output | No      | Never       | Regenerate in `prepare` or `build` | Build must succeed from a clean tree    |

_Table 1: The two valid states for generated code._

A file that is listed in `.gitignore` and also present in the index is in
neither state: Git tracks it, so edits show in diffs, but `git add .` will not
pick up regeneration, so the tracked copy rots. Pick a state and fix the index
(`git rm --cached` or remove the ignore rule).

Tracked output is the better default for types consumed by many files: a
reviewer sees the API change in the diff, and editors work without a build
step. Ignored output is better for large or binary artefacts.

## The generation script

```json
{
  "scripts": {
    "generate": "graphql-codegen --config codegen.ts && openapi-typescript schema/api.json -o src/__generated__/api.ts",
    "generate:check": "npm run generate && git diff --exit-code -- src/__generated__"
  }
}
```

`generate:check` runs in CI on every pull request. The generator's own version
is pinned in `package.json`, because a generator upgrade changes the output and
should be its own commit.

## Exclusions

Generated directories are excluded from:

- lint (`.oxlintrc.json` `ignorePatterns`, Biome `files.ignore`);
- the strictness ratchet (a `tsconfig` that extends the base with only the
  relaxations the generator needs, and a comment naming the generator);
- mutation testing and coverage thresholds;
- formatting, so a formatter upgrade does not produce a diff the generator
  will undo.

They are not excluded from type-checking: generated types that do not compile
are a generator bug worth seeing.

## Schema as the reviewed artefact

The input schema (`openapi.json`, `schema.graphql`, `*.proto`) is the thing to
review. A fetched upstream schema is updated by a script with its own commit,
so a server-side change arrives as a visible diff to the schema and the
regenerated types together.

## Typed access to generated types

Generated types are transport types. Wrap them:

```ts
import type { components } from "./__generated__/api.js";

export type UserDto = components["schemas"]["User"];
export function toUser(dto: UserDto): User { /* ... */ }
```

Nothing outside the boundary module imports from `__generated__`. Route the
validation question to `typescript-boundaries-and-validation`.
