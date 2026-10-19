<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `effect/BigInt` v3 → v4

- `BigInt.fromNumber` -> `BigInt.fromNumber`: Unchanged; it returns Option for
  safe conversion.
- `BigInt.greaterThan` -> `BigInt.isGreaterThan`: Renamed with the v4 is-prefix.
- `BigInt.greaterThanOrEqualTo` -> `BigInt.isGreaterThanOrEqualTo`: Renamed
  with the v4 is-prefix.
- `BigInt.lessThan` -> `BigInt.isLessThan`: Renamed with the v4 is-prefix.
- `BigInt.lessThanOrEqualTo` -> `BigInt.isLessThanOrEqualTo`: Renamed with the
  v4 is-prefix.
- `BigInt.unsafeDivide` -> `BigInt.divideUnsafe`: Renamed to use the v4 Unsafe
  suffix convention.
- `BigInt.unsafeSqrt` -> `BigInt.sqrtUnsafe`: Renamed to use the v4 Unsafe
  suffix convention.
