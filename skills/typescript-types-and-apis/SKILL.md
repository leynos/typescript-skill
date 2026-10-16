---
name: typescript-types-and-apis
description: Use for TypeScript type modelling and public API shape, including narrowing, generics, overloads, variance, branded types, exhaustive unions, unknown versus any, assertions, satisfies, suppression discipline, and how strict a greenfield or brownfield tsconfig should be.
metadata:
  globs: "**/tsconfig*.json, **/*.ts, **/*.tsx, **/*.mts, **/*.cts, **/*.d.ts"
---

# TypeScript types and APIs

Use this when the real question is how much of the design should live in the
type system, and how much strictness the project can honestly carry.

## Working stance

- Make invalid states unrepresentable before adding runtime checks, and keep
  runtime checks at the boundary where untyped data arrives.
- Types are claims the compiler verifies about typed code. A type says
  nothing about data that arrived through `JSON.parse`, `postMessage`, or
  `process.env`; route that to `typescript-boundaries-and-validation`.
- Keep public APIs narrower than internal helpers: precise return types,
  permissive parameter types, no generic parameters that exist only for
  internal convenience.
- Prefer `unknown` to `any` everywhere. `any` is a hole in the proof; `unknown`
  is a value whose shape is not yet known.
- Treat every `as`, `!`, `@ts-expect-error`, and `@ts-ignore` as a claim that
  needs a comment naming the invariant the checker cannot see.
- Decide the strictness posture before writing types. Greenfield code takes the
  full switch set. Brownfield code takes a ratchet, not a wholesale flip.

## Decision surface

- **Exhaustive unions.** Discriminate on a literal `kind` or `type` field,
  `switch` over it, and end with `assertNever(value: never)`. A missing arm is
  then a compile error. Use `satisfies` to check an object against a type while
  keeping the narrower inferred type.
- **Narrowing.** Prefer control-flow narrowing, `in`, and discriminants over
  type predicates. Write a predicate (`x is Foo`) only when the check is a
  genuine equivalence; a predicate that can lie is worse than no narrowing. See
  [narrowing-and-guards.md](references/narrowing-and-guards.md).
- **Branded types.** Wrap a primitive in
  `string & { readonly __brand: "UserId" }` when two identifiers of the same
  shape must not be confused. Construct the brand in one function, at the
  boundary that validated it.
- **Generics and variance.** Reach for a type parameter when one concrete type
  flows from input to output. Mark callbacks that only read as `readonly` and
  arrays that are never mutated as `readonly T[]`, so variance works for you.
  Overloads suit a closed set of call shapes; a union parameter suits an open
  one. See [generics-and-variance.md](references/generics-and-variance.md).
- **`unknown` versus `any`.** `catch (error: unknown)` and `JSON.parse(): any`
  are the two places `any` leaks in. Convert at once: classify the error,
  validate the JSON.
- **Assertions.** `as const` and `satisfies` are safe. `as T` on a value the
  compiler already types is a downcast and needs a reason. `as unknown as T` is
  a boundary and belongs in exactly one adapter function.
- **Suppression.** `@ts-expect-error` over `@ts-ignore`, always with a reason
  on the same line, and only on the narrowest statement. A suppression without
  a tracking note is debt the compiler will never remind you of. See
  [suppression-discipline.md](references/suppression-discipline.md).

## Strictness ratchet

Greenfield projects enable `strict`, `noUncheckedIndexedAccess`,
`exactOptionalPropertyTypes`, `noImplicitOverride`,
`noPropertyAccessFromIndexSignature`, `noFallthroughCasesInSwitch`,
`useUnknownInCatchVariables`, `verbatimModuleSyntax`, and `isolatedModules`
from the first commit. The
[strictness-switches.ts](../../examples/diagnostics/strictness-switches.ts)
fixture shows what each of the sharper switches rejects.

Brownfield projects ratchet instead:

1. Keep a strict base `tsconfig` and let new directories extend it unchanged.
2. Give legacy directories their own `tsconfig` that extends the base and
   switches off only the options that currently fail, each with a comment.
3. Enable one switch at a time across one legacy directory, fix or suppress
   with reasons, and commit. Count suppressions in CI so the number only goes
   down.
4. Never relax the base to make a legacy directory pass. The gate that checks
   the whole repository must use the per-directory configurations, not a fourth
   configuration that is looser than any of them.

See [strictness-ratchet.md](references/strictness-ratchet.md) for the switch
order, what each one typically breaks, and how to measure progress.

## Red flags

- A public function parameter or return type is `any`, or an object type is
  `{}` or `object` where a named shape was meant.
- A type predicate returns `true` for values that do not satisfy the type.
- `as` appears next to a runtime check that would narrow on its own.
- A `switch` over a union has a `default` that returns a fallback instead of
  calling `assertNever`.
- Two `boolean` parameters in one signature; use an options object or a union
  of literals.
- A brand is constructed in more than one place, or bypassed with `as`.
- A repository-wide type-check configuration is looser than the base it
  extends, so the gate proves less than the editor shows.
- Enabling a switch is done by adding `@ts-expect-error` in bulk with no
  reasons and no count.

## Pairing

- Pair with `typescript-boundaries-and-validation` when the question is where
  a branded or validated type is first constructed.
- Pair with `typescript-data-and-state` when the union models runtime state
  transitions rather than API vocabulary.
- Pair with `typescript-modules-and-packaging` when declaration emit or
  `exports` conditions change the public type surface.
