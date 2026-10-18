<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `effect/Secret` v3 → v4

- `Secret.Secret` -> `Redacted.Redacted<string>`: Secret was deprecated in v3
  and removed in v4; use the generic Redacted wrapper.
- `Secret.Secret.Proto` -> `none`: The Secret-specific prototype was removed
  with the module; use Redacted.Redacted\<string\>.
- `Secret.SecretTypeId` -> `Redacted.isRedacted`: The Secret marker was
  removed; use the Redacted runtime guard.
- `Secret.fromIterable` -> `Redacted.make(Array.from(iterable).join(""))`:
  Secret was removed; join the character iterable and wrap the resulting string
  in Redacted.
- `Secret.fromString`: TODO: needs guidance
- `Secret.isSecret` -> `Redacted.isRedacted`: Secret was removed in favor of
  Redacted.
- `Secret.make` ->
  `Redacted.make(bytes.map((byte) => String.fromCharCode(byte)).join(""))`:
  Secret was removed; preserve the v3 byte-to-code-unit conversion explicitly,
  then wrap the string in Redacted.
- `Secret.unsafeWipe` -> `Redacted.wipeUnsafe`: Redacted.wipeUnsafe removes the
  registry entry but, unlike v3 Secret, cannot zero a retained mutable byte
  array; zero external buffers separately when required.
