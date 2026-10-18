<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `effect/Arbitrary` v3 → v4

- `Arbitrary.ArbitraryAnnotation` ->
  `Schema.Annotations.ToArbitrary.Declaration`: Arbitrary derivation
  annotations now live in Schema.Annotations. Attach a toCodecArbitrary
  declaration callback that returns a Schema Link.
- `Arbitrary.ArbitraryGenerationContext` ->
  `Schema.Annotations.ToArbitrary.DeclarationInput`: Native arbitrary callbacks
  receive DeclarationInput with decoded type-parameter schemas and normalized
  constraints.
- `Arbitrary.LazyArbitrary` -> `effect/Arbitrary#Arbitrary`: The
  generated-value description is now the native Arbitrary interface from
  effect/Arbitrary.
