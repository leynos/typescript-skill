# Public surface

## The entry point is a curated list

```ts
// src/index.ts
export { createEngine } from "./engine.js";
export type { Engine, EngineOptions } from "./engine.js";
export { EngineError, type EngineErrorCode } from "./errors.js";
export { CommandSchema, type Command } from "./protocol.js";
```

Every line is a decision. `export *` is an abdication: it publishes whatever
the module happens to contain, including things added for tests. The entry
point names what consumers may use; the build's `exports` map names where it
lives.

## What belongs

| Export                    | Belongs when                                           |
| ------------------------- | ------------------------------------------------------ |
| Factory or constructor    | Consumers create the thing                             |
| Options type              | Consumers configure it                                 |
| Result and model types    | Consumers read what it returns                         |
| Error class or code union | Consumers branch on failure                            |
| Schema                    | Consumers validate against the same contract           |
| Constants                 | Consumers need the exact value (channel names, limits) |
| Test helpers              | Only from a separate `./testing` subpath               |

_Table 1: What a public entry point exports and why._

Internal helpers, implementation data structures, and anything with "util" in
the name stay out.

## Subpaths for optional surface

```json
{
  "exports": {
    ".": "./dist/index.js",
    "./testing": "./dist/testing/index.js",
    "./unstable": "./dist/unstable/index.js"
  }
}
```

A `./testing` subpath keeps fakes and fixtures out of the main surface while
still shipping them. An `./unstable` subpath makes the stability promise
visible in the import statement. A deep import into `./dist/internal/…` is
blocked by the `exports` map.

## Types that cross the boundary

A type that leaves the package is a contract:

- Prefer `interface` and `type` over classes for data; a class exported for its
  type drags its constructor and prototype into the contract.
- Keep branded types and `Date` out of types that will be serialized by a
  consumer; export the transport type and the converter instead.
- Mark fields `readonly`. A consumer who mutates a result has created a
  coupling the package did not sign up for.
- Avoid exporting types derived from a dependency's types
  (`ReturnType<typeof thirdParty.create>`); a dependency bump becomes a
  breaking change.

## Checking the surface

- `isolatedDeclarations` forces every export to have an explicit type, which
  doubles as a review prompt.
- An API extractor or a snapshot of the generated `.d.ts` entry makes surface
  changes visible in review.
- A contract test imports the package through its `exports` map (never a path
  alias) and asserts the expected names exist and nothing else does.
