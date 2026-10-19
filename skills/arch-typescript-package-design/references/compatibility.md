# Compatibility

## Stability tags

| Tag      | Promise                                                 | Signal to consumers                           |
| -------- | ------------------------------------------------------- | --------------------------------------------- |
| Stable   | Breaking changes only in a major, with a migration note | Default; exported from `.`                    |
| Unstable | May break in a minor; the changelog says so             | `./unstable` subpath or `@experimental` JSDoc |
| Internal | No promise; may vanish                                  | Not exported; or `@internal` and stripped     |

_Table 1: Stability tags and the promise each carries._

Mark every export. An unmarked export is stable by default, which is usually
more than the author meant.

## What counts as breaking

- Removing or renaming an export.
- Narrowing a parameter type or widening a return type.
- Adding a required field to an input type, or removing a field from an
  output type.
- Changing a default.
- Changing the runtime floor (`engines`), the module format, or dropping a
  condition from `exports`.
- Changing a `.d.ts` in a way that fails a consumer's type check, even if the
  runtime is unchanged. Type-level changes are API changes.

Adding an optional field to an input, adding a field to an output, and adding a
new export are not breaking.

## Deprecation

```ts
/** @deprecated Use {@link createEngine} with `mode: "strict"`. Removed in 4.0. */
export function createStrictEngine(options: EngineOptions): Engine { /* … */ }
```

- `@deprecated` with the replacement and the removal version.
- Keep the deprecated path working for at least one minor.
- A lint rule in consumers (`deprecation`) surfaces the usage.

## Checking compatibility in CI

- A type-level API snapshot: generate the entry point's `.d.ts` and diff it
  against the committed snapshot; a change requires an explicit update and a
  changelog entry.
- A compile-time test suite in a `consumer/` fixture that imports the package
  as a consumer would and asserts the shapes it relies on with `satisfies` and
  `@ts-expect-error`.
- The packed-install smoke test from `typescript-modules-and-packaging`, so a
  packaging change is caught as a compatibility change.

## Protocol compatibility

For a protocol shared across processes or services, compatibility is about the
two ends diverging in time:

- Receivers ignore unknown fields and unknown event types (with a debug log).
- Senders never remove a field without a major protocol bump.
- Both ends exchange a protocol version at handshake and refuse mismatches
  they cannot serve.
- Schemas are the source of truth and live in the shared package; a generated
  changelog of schema diffs is the review artefact.

## Runtime floor

Declare `engines.node` (and Bun where supported), and treat raising it as a
breaking change. Test on the floor version in CI, not only on the latest.
