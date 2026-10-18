<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/typeclass/Semigroup` v3 → v4

- `Semigroup.Invariant` -> `none`: The @effect/typeclass package was removed in
  v4 with no generic typeclass layer replacement. Rewrite this abstraction
  against the concrete v4 data type and its module functions.
- `Semigroup.Product` -> `none`: The @effect/typeclass package was removed in
  v4 with no generic typeclass layer replacement. Rewrite this abstraction
  against the concrete v4 data type and its module functions.
- `Semigroup.SemiProduct` -> `none`: The @effect/typeclass package was removed
  in v4 with no generic typeclass layer replacement. Rewrite this abstraction
  against the concrete v4 data type and its module functions.
- `Semigroup.Semigroup` -> `Combiner.Combiner`: Combiner replaces Semigroup in
  v4 and retains the binary combine method; combineMany was removed.
- `Semigroup.SemigroupTypeLambda` -> `none`: The @effect/typeclass package was
  removed in v4 with no generic typeclass layer replacement. Rewrite this
  abstraction against the concrete v4 data type and its module functions.
- `Semigroup.array` -> `Array.makeReducerConcat`: The v4 concatenation Reducer
  is also a Combiner and replaces the array Semigroup.
- `Semigroup.constant` -> `Combiner.constant`: Combiner replaces Semigroup in
  v4.
- `Semigroup.first` -> `Combiner.first`: Combiner replaces Semigroup in v4.
- `Semigroup.imap` -> `Combiner.make`: V4 has no generic invariant instance;
  build a Combiner that maps both inputs with from, combines them, then maps
  the result with to.
- `Semigroup.intercalate` -> `Combiner.intercalate`: Combiner replaces
  Semigroup; v4 takes the separator first and then the Combiner.
- `Semigroup.last` -> `Combiner.last`: Combiner replaces Semigroup in v4.
- `Semigroup.make` -> `Combiner.make`: Combiner replaces Semigroup. V4 accepts
  only the binary combine function and has no combineMany override.
- `Semigroup.max` -> `Combiner.max`: Combiner replaces Semigroup; pass the same
  Order to retain last-maximum tie behavior.
- `Semigroup.min` -> `Combiner.min`: Combiner replaces Semigroup; pass the same
  Order to retain last-minimum tie behavior.
- `Semigroup.reverse` -> `Combiner.flip`: Use the v4 Combiner combinator to
  reverse combine argument order.
- `Semigroup.struct` -> `Struct.makeCombiner`: Pass a record of v4 Combiners to
  derive a field-wise Combiner.
- `Semigroup.tuple` -> `Tuple.makeCombiner`: Pass one array of v4 Combiners
  instead of rest Semigroup arguments.
