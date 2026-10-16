# Absence and identity

## Three kinds of absent

| Form                    | Meaning                             | Survives JSON    | Notes                                                         |
| ----------------------- | ----------------------------------- | ---------------- | ------------------------------------------------------------- |
| Missing key (`field?:`) | Not provided; defaults may apply    | Yes (key absent) | Under `exactOptionalPropertyTypes` it cannot hold `undefined` |
| `undefined`             | Provided, but empty                 | No (key dropped) | Indistinguishable from missing after `JSON.stringify`         |
| `null`                  | Producer explicitly said "no value" | Yes              | Only form that survives JSON as a deliberate marker           |

_Table 1: The three forms of absence and how each behaves on the wire._

Pick per boundary:

- Internal model types use missing keys for "not applicable" and a variant for
  "not yet known" when the distinction matters. Avoid `null` inside the model
  unless an external schema forces it.
- Transport types mirror the wire. If the API sends `null`, the transport type
  says `null`; the converter maps it to the model's convention.
- Never let both `undefined` and `null` mean the same thing in one type; a
  consumer will check one and miss the other.

```ts
// Model: absence is structural.
type Profile =
  | { readonly kind: "anonymous" }
  | { readonly kind: "known"; readonly displayName: string; readonly avatarUrl?: string };

// Transport: mirrors the wire exactly.
interface ProfileDto {
  readonly display_name: string | null;
  readonly avatar_url: string | null;
}

function toProfile(dto: ProfileDto): Profile {
  if (dto.display_name === null) return { kind: "anonymous" };
  return dto.avatar_url === null
    ? { kind: "known", displayName: dto.display_name }
    : { kind: "known", displayName: dto.display_name, avatarUrl: dto.avatar_url };
}
```

The converter is the one place that knows both conventions.

## Identity

- **Entities** have an identity that outlives their fields. Give them a
  branded identifier and compare by identifier. Two `User` values with the same
  `id` and different `name` are the same user at different times.
- **Values** are their fields. Compare structurally with a small helper or a
  library; never rely on `===` between two objects that came from different
  places.
- **Reference identity** is a runtime accident. It breaks across
  `structuredClone`, `postMessage`, JSON, React re-renders, and store updates.
  Code that uses an object as a `Map` key or a `WeakSet` member must own both
  ends of that object's lifetime.

## Equality traps

- `NaN !== NaN`; use `Object.is` or `Number.isNaN` where it matters.
- `new Date(x) === new Date(x)` is `false`; compare `getTime()`.
- `[] === []` is `false`; compare length and elements.
- `Set` and `Map` compare by reference; convert to sorted arrays to compare.
- `-0 === 0` is `true` but `Object.is(-0, 0)` is `false`; JSON drops the sign.

## Clones

`structuredClone` preserves `Date`, `Map`, `Set`, `ArrayBuffer`, and cycles,
and throws on functions and DOM nodes. `JSON.parse(JSON.stringify(x))` drops
`undefined`, functions, and symbols, turns `Date` into a string, and turns
`Map` and `Set` into `{}`. Use `structuredClone` for an in-process deep copy
and a converter for anything that crosses a boundary.
