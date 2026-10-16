# Narrowing and guards

Narrowing is how a value of a wide type becomes usable at a narrow one. The
compiler does most of it from control flow; hand-written guards fill the gaps
and are where lies creep in.

## Prefer control flow

```ts
type Shape =
  | { readonly kind: "circle"; readonly radius: number }
  | { readonly kind: "rect"; readonly width: number; readonly height: number };

export function area(shape: Shape): number {
  switch (shape.kind) {
    case "circle":
      return Math.PI * shape.radius ** 2;
    case "rect":
      return shape.width * shape.height;
    default:
      return assertNever(shape);
  }
}

function assertNever(value: never): never {
  throw new Error(`unhandled: ${JSON.stringify(value)}`);
}
```

The discriminant does the work. No predicate, no cast, and adding a third
`kind` fails to compile until every `switch` handles it.

`in` narrows too, but only when the property is unique to one member of the
union; a shared optional property narrows nothing.

## Type predicates must be equivalences

```ts
// Honest: the check proves the type.
function isNonEmpty<T>(items: readonly T[]): items is readonly [T, ...T[]] {
  return items.length > 0;
}

// Dishonest: a `string` with the right shape is not a validated identifier.
function isUserId(value: string): value is UserId {
  return value.length > 0; // lies about the brand
}
```

A predicate that returns `true` for values outside the narrowed type lets the
compiler trust something false for the rest of the function. When the check is
a parse rather than a test, return the parsed value, or an outcome, instead of
a boolean. That is the shape `typescript-boundaries-and-validation` uses.

## Assertion functions

`asserts value is T` is for invariants the code cannot continue without. Use it
at the start of a function, and make the thrown error say which invariant
failed. Do not use it to paper over data that should have been validated at a
boundary.

## `satisfies` versus annotation

```ts
const routes = {
  home: "/",
  profile: "/profile/:id",
} satisfies Record<string, string>;

routes.profile; // still the literal type "/profile/:id"
```

An annotation widens to the declared type; `satisfies` checks against it and
keeps the inferred type. Use `satisfies` for configuration objects and
registries whose keys the rest of the program depends on.

## Where narrowing stops

- Across an `await`, a closure, or a callback, the compiler forgets narrowing
  of mutable properties. Copy the narrowed value into a `const` first.
- Index access under `noUncheckedIndexedAccess` is `T | undefined` even after
  a length check on the array; destructure or use `.at()` and narrow the result.
- Narrowing does not cross a `JSON.parse`. The result is `any`; wrap it in
  `unknown` and validate.
