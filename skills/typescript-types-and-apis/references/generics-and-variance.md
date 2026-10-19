# Generics and variance

## When a type parameter earns its place

A type parameter is justified when one concrete type flows from an input to an
output and the caller must see that relationship preserved.

```ts
export function first<T>(items: readonly T[]): T | undefined {
  return items[0];
}

export function groupBy<T, K extends PropertyKey>(
  items: readonly T[],
  key: (item: T) => K,
): Partial<Record<K, T[]>> {
  const groups: Partial<Record<K, T[]>> = {};
  for (const item of items) {
    (groups[key(item)] ??= []).push(item);
  }
  return groups;
}
```

A type parameter is not justified when it appears only once in a signature; a
single-use `T` is an `unknown` that reads worse. It is also not justified when
it exists so that an internal helper can be reused; keep the helper generic and
the public signature concrete.

## Constraints and defaults

- Constrain with `extends` to the smallest shape the body needs.
- Give a default (`<T = unknown>`) only when callers genuinely omit it; a
  default that is always overridden is noise.
- Prefer `NoInfer<T>` when a second parameter should not widen the inference
  from the first.

## Variance in practice

- `readonly T[]` and `ReadonlyArray<T>` are covariant: a `readonly Dog[]`
  is a `readonly Animal[]`. Mutable arrays are not safe to treat that way, and
  TypeScript's unsound allowance is a known hole; accept `readonly` arrays in
  parameters to keep it closed.
- Callback parameters are contravariant under `strictFunctionTypes`. A handler
  typed `(event: MouseEvent) => void` is not assignable where
  `(event: Event) => void` is required. Method shorthand
  (`on(event: Event): void`) is bivariant and therefore looser; prefer property
  syntax for callbacks in public interfaces when the check matters.
- Mark variance explicitly (`in`, `out`) on type parameters of interfaces only
  when inference is slow or wrong; it is a documentation and performance aid,
  not a correctness requirement.

## Overloads versus unions

Use overloads when a closed set of call shapes each has a distinct return type
and the implementation signature would otherwise return a union the caller has
to narrow again:

```ts
export function parse(input: string): Document;
export function parse(input: string, options: { readonly lenient: true }): Document | null;
export function parse(input: string, options?: { readonly lenient?: boolean }): Document | null {
  // one implementation
}
```

Use a union parameter when the set is open or the return type does not depend
on the shape. Overloads are checked less thoroughly than ordinary signatures,
so keep the implementation signature as narrow as it can honestly be.

## Branded primitives

```ts
declare const brand: unique symbol;
export type UserId = string & { readonly [brand]: "UserId" };

export function userId(raw: string): UserId {
  if (!/^[a-z0-9]{8}$/.test(raw)) {
    throw new TypeError("invalid user id");
  }
  return raw as UserId;
}
```

The single `as` lives here and nowhere else. Every other function takes
`UserId` and can trust it. If the brand needs to cross JSON, it is a plain
string on the wire and is re-branded by the parser on the way in.
