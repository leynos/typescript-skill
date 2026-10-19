<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `effect/FastCheck` v3 → v4

- `FastCheck.Arbitrary` -> `FastCheck.Arbitrary`: Depend on fast-check and
  import it directly. The API is unchanged in fast-check v4.
- `FastCheck.ArrayConstraints` -> `FastCheck.ArrayConstraints`: Depend on
  fast-check and import it directly. The API is unchanged in fast-check v4.
- `FastCheck.AsyncCommand` -> `FastCheck.AsyncCommand`: Depend on fast-check
  and import it directly. The API is unchanged in fast-check v4.
- `FastCheck.AsyncPropertyHookFunction` ->
  `FastCheck.AsyncPropertyHookFunction`: Depend on fast-check and import it
  directly. The API is unchanged in fast-check v4.
- `FastCheck.BigIntArrayConstraints` -> `FastCheck.BigIntArrayConstraints`:
  Depend on fast-check and import it directly. The API is unchanged in
  fast-check v4.
- `FastCheck.BigIntConstraints` -> `FastCheck.BigIntConstraints`: Depend on
  fast-check and import it directly. The API is unchanged in fast-check v4.
- `FastCheck.BigUintConstraints` -> `FastCheck.BigIntConstraints`: Depend on
  fast-check and import it directly. Unsigned bigint constraints were
  consolidated into BigIntConstraints with min: 0n.
- `FastCheck.CloneValue` -> `FastCheck.CloneValue`: Depend on fast-check and
  import it directly. The API is unchanged in fast-check v4.
- `FastCheck.Command` -> `FastCheck.Command`: Depend on fast-check and import
  it directly. The API is unchanged in fast-check v4.
- `FastCheck.CommandsContraints` -> `FastCheck.CommandsContraints`: Depend on
  fast-check and import it directly. The API is unchanged in fast-check v4.
- `FastCheck.ContextValue` -> `FastCheck.ContextValue`: Depend on fast-check
  and import it directly. The API is unchanged in fast-check v4.
- `FastCheck.DateConstraints` -> `FastCheck.DateConstraints`: Depend on
  fast-check and import it directly. The API is unchanged in fast-check v4.
- `FastCheck.DepthContext` -> `FastCheck.DepthContext`: Depend on fast-check
  and import it directly. The API is unchanged in fast-check v4.
- `FastCheck.DepthIdentifier` -> `FastCheck.DepthIdentifier`: Depend on
  fast-check and import it directly. The API is unchanged in fast-check v4.
- `FastCheck.DepthSize` -> `FastCheck.DepthSize`: Depend on fast-check and
  import it directly. The API is unchanged in fast-check v4.
- `FastCheck.DictionaryConstraints` -> `FastCheck.DictionaryConstraints`:
  Depend on fast-check and import it directly. The API is unchanged in
  fast-check v4.
- `FastCheck.DomainConstraints` -> `FastCheck.DomainConstraints`: Depend on
  fast-check and import it directly. The API is unchanged in fast-check v4.
- `FastCheck.DoubleConstraints` -> `FastCheck.DoubleConstraints`: Depend on
  fast-check and import it directly. The API is unchanged in fast-check v4.
- `FastCheck.EmailAddressConstraints` -> `FastCheck.EmailAddressConstraints`:
  Depend on fast-check and import it directly. The API is unchanged in
  fast-check v4.
- `FastCheck.ExecutionStatus` -> `FastCheck.ExecutionStatus`: Depend on
  fast-check and import it directly. The API is unchanged in fast-check v4.
- `FastCheck.ExecutionTree` -> `FastCheck.ExecutionTree`: Depend on fast-check
  and import it directly. The API is unchanged in fast-check v4.
- `FastCheck.FalsyContraints` -> `FastCheck.FalsyContraints`: Depend on
  fast-check and import it directly. The API is unchanged in fast-check v4.
- `FastCheck.FalsyValue` -> `FastCheck.FalsyValue`: Depend on fast-check and
  import it directly. The API is unchanged in fast-check v4.
- `FastCheck.Float32ArrayConstraints` -> `FastCheck.Float32ArrayConstraints`:
  Depend on fast-check and import it directly. The API is unchanged in
  fast-check v4.
- `FastCheck.Float64ArrayConstraints` -> `FastCheck.Float64ArrayConstraints`:
  Depend on fast-check and import it directly. The API is unchanged in
  fast-check v4.
- `FastCheck.FloatConstraints` -> `FastCheck.FloatConstraints`: Depend on
  fast-check and import it directly. The API is unchanged in fast-check v4.
- `FastCheck.GeneratorValue` -> `FastCheck.GeneratorValue`: Depend on
  fast-check and import it directly. The API is unchanged in fast-check v4.
- `FastCheck.GlobalAsyncPropertyHookFunction` ->
  `FastCheck.GlobalAsyncPropertyHookFunction`: Depend on fast-check and import
  it directly. The API is unchanged in fast-check v4.
- `FastCheck.GlobalParameters` -> `FastCheck.GlobalParameters`: Depend on
  fast-check and import it directly. The API is unchanged in fast-check v4.
- `FastCheck.GlobalPropertyHookFunction` ->
  `FastCheck.GlobalPropertyHookFunction`: Depend on fast-check and import it
  directly. The API is unchanged in fast-check v4.
- `FastCheck.IAsyncProperty` -> `FastCheck.IAsyncProperty`: Depend on
  fast-check and import it directly. The API is unchanged in fast-check v4.
- `FastCheck.IAsyncPropertyWithHooks` -> `FastCheck.IAsyncPropertyWithHooks`:
  Depend on fast-check and import it directly. The API is unchanged in
  fast-check v4.
- `FastCheck.ICommand` -> `FastCheck.ICommand`: Depend on fast-check and import
  it directly. The API is unchanged in fast-check v4.
- `FastCheck.IProperty` -> `FastCheck.IProperty`: Depend on fast-check and
  import it directly. The API is unchanged in fast-check v4.
- `FastCheck.IPropertyWithHooks` -> `FastCheck.IPropertyWithHooks`: Depend on
  fast-check and import it directly. The API is unchanged in fast-check v4.
- `FastCheck.IRawProperty` -> `FastCheck.IRawProperty`: Depend on fast-check
  and import it directly. The API is unchanged in fast-check v4.
- `FastCheck.IntArrayConstraints` -> `FastCheck.IntArrayConstraints`: Depend on
  fast-check and import it directly. The API is unchanged in fast-check v4.
- `FastCheck.IntegerConstraints` -> `FastCheck.IntegerConstraints`: Depend on
  fast-check and import it directly. The API is unchanged in fast-check v4.
- `FastCheck.JsonSharedConstraints` -> `FastCheck.JsonSharedConstraints`:
  Depend on fast-check and import it directly. The API is unchanged in
  fast-check v4.
- `FastCheck.LetrecLooselyTypedBuilder` ->
  `FastCheck.LetrecLooselyTypedBuilder`: Depend on fast-check and import it
  directly. The API is unchanged in fast-check v4.
- `FastCheck.LetrecLooselyTypedTie` -> `FastCheck.LetrecLooselyTypedTie`:
  Depend on fast-check and import it directly. The API is unchanged in
  fast-check v4.
- `FastCheck.LetrecTypedBuilder` -> `FastCheck.LetrecTypedBuilder`: Depend on
  fast-check and import it directly. The API is unchanged in fast-check v4.
- `FastCheck.LetrecTypedTie` -> `FastCheck.LetrecTypedTie`: Depend on
  fast-check and import it directly. The API is unchanged in fast-check v4.
- `FastCheck.LetrecValue` -> `FastCheck.LetrecValue`: Depend on fast-check and
  import it directly. The API is unchanged in fast-check v4.
- `FastCheck.LoremConstraints` -> `FastCheck.LoremConstraints`: Depend on
  fast-check and import it directly. The API is unchanged in fast-check v4.
- `FastCheck.MaybeWeightedArbitrary` -> `FastCheck.MaybeWeightedArbitrary`:
  Depend on fast-check and import it directly. The API is unchanged in
  fast-check v4.
- `FastCheck.Memo` -> `FastCheck.Memo`: Depend on fast-check and import it
  directly. The API is unchanged in fast-check v4.
- `FastCheck.MixedCaseConstraints` -> `FastCheck.MixedCaseConstraints`: Depend
  on fast-check and import it directly. The API is unchanged in fast-check v4.
- `FastCheck.ModelRunAsyncSetup` -> `FastCheck.ModelRunAsyncSetup`: Depend on
  fast-check and import it directly. The API is unchanged in fast-check v4.
- `FastCheck.ModelRunSetup` -> `FastCheck.ModelRunSetup`: Depend on fast-check
  and import it directly. The API is unchanged in fast-check v4.
- `FastCheck.NatConstraints` -> `FastCheck.NatConstraints`: Depend on
  fast-check and import it directly. The API is unchanged in fast-check v4.
- `FastCheck.ObjectConstraints` -> `FastCheck.ObjectConstraints`: Depend on
  fast-check and import it directly. The API is unchanged in fast-check v4.
- `FastCheck.OneOfConstraints` -> `FastCheck.OneOfConstraints`: Depend on
  fast-check and import it directly. The API is unchanged in fast-check v4.
- `FastCheck.OneOfValue` -> `FastCheck.OneOfValue`: Depend on fast-check and
  import it directly. The API is unchanged in fast-check v4.
- `FastCheck.OptionConstraints` -> `FastCheck.OptionConstraints`: Depend on
  fast-check and import it directly. The API is unchanged in fast-check v4.
- `FastCheck.Parameters` -> `FastCheck.Parameters`: Depend on fast-check and
  import it directly. The API is unchanged in fast-check v4.
- `FastCheck.PreconditionFailure` -> `FastCheck.PreconditionFailure`: Depend on
  fast-check and import it directly. The API is unchanged in fast-check v4.
- `FastCheck.PropertyHookFunction` -> `FastCheck.PropertyHookFunction`: Depend
  on fast-check and import it directly. The API is unchanged in fast-check v4.
- `FastCheck.Random` -> `FastCheck.Random`: Depend on fast-check and import it
  directly. The API is unchanged in fast-check v4.
- `FastCheck.RandomType` -> `FastCheck.RandomType`: Depend on fast-check and
  import it directly. The API is unchanged in fast-check v4.
- `FastCheck.RecordConstraints` -> `FastCheck.RecordConstraints`: Depend on
  fast-check and import it directly. The API is unchanged in fast-check v4.
- `FastCheck.RecordValue` -> `FastCheck.RecordValue`: Depend on fast-check and
  import it directly. The API is unchanged in fast-check v4.
- `FastCheck.RunDetails` -> `FastCheck.RunDetails`: Depend on fast-check and
  import it directly. The API is unchanged in fast-check v4.
- `FastCheck.RunDetailsCommon` -> `FastCheck.RunDetailsCommon`: Depend on
  fast-check and import it directly. The API is unchanged in fast-check v4.
- `FastCheck.RunDetailsFailureInterrupted` ->
  `FastCheck.RunDetailsFailureInterrupted`: Depend on fast-check and import it
  directly. The API is unchanged in fast-check v4.
- `FastCheck.RunDetailsFailureProperty` ->
  `FastCheck.RunDetailsFailureProperty`: Depend on fast-check and import it
  directly. The API is unchanged in fast-check v4.
- `FastCheck.RunDetailsFailureTooManySkips` ->
  `FastCheck.RunDetailsFailureTooManySkips`: Depend on fast-check and import it
  directly. The API is unchanged in fast-check v4.
- `FastCheck.RunDetailsSuccess` -> `FastCheck.RunDetailsSuccess`: Depend on
  fast-check and import it directly. The API is unchanged in fast-check v4.
- `FastCheck.SchedulerAct` -> `FastCheck.SchedulerAct`: Depend on fast-check
  and import it directly. The API is unchanged in fast-check v4.
- `FastCheck.SchedulerConstraints` -> `FastCheck.SchedulerConstraints`: Depend
  on fast-check and import it directly. The API is unchanged in fast-check v4.
- `FastCheck.SchedulerReportItem` -> `FastCheck.SchedulerReportItem`: Depend on
  fast-check and import it directly. The API is unchanged in fast-check v4.
- `FastCheck.SchedulerSequenceItem` -> `FastCheck.SchedulerSequenceItem`:
  Depend on fast-check and import it directly. The API is unchanged in
  fast-check v4.
- `FastCheck.ShuffledSubarrayConstraints` ->
  `FastCheck.ShuffledSubarrayConstraints`: Depend on fast-check and import it
  directly. The API is unchanged in fast-check v4.
- `FastCheck.Size` -> `FastCheck.Size`: Depend on fast-check and import it
  directly. The API is unchanged in fast-check v4.
- `FastCheck.SizeForArbitrary` -> `FastCheck.SizeForArbitrary`: Depend on
  fast-check and import it directly. The API is unchanged in fast-check v4.
- `FastCheck.SparseArrayConstraints` -> `FastCheck.SparseArrayConstraints`:
  Depend on fast-check and import it directly. The API is unchanged in
  fast-check v4.
- `FastCheck.StringConstraints` -> `FastCheck.StringConstraints`: Depend on
  fast-check and import it directly. The API is unchanged in fast-check v4.
- `FastCheck.StringMatchingConstraints` ->
  `FastCheck.StringMatchingConstraints`: Depend on fast-check and import it
  directly. The API is unchanged in fast-check v4.
- `FastCheck.StringSharedConstraints` -> `FastCheck.StringSharedConstraints`:
  Depend on fast-check and import it directly. The API is unchanged in
  fast-check v4.
- `FastCheck.SubarrayConstraints` -> `FastCheck.SubarrayConstraints`: Depend on
  fast-check and import it directly. The API is unchanged in fast-check v4.
- `FastCheck.UnicodeJsonSharedConstraints` ->
  `FastCheck.JsonSharedConstraints`: Depend on fast-check and import it
  directly. Unicode JSON generation was consolidated into
  JsonSharedConstraints.stringUnit.
- `FastCheck.UniqueArrayConstraints` -> `FastCheck.UniqueArrayConstraints`:
  Depend on fast-check and import it directly. The API is unchanged in
  fast-check v4.
- `FastCheck.UniqueArrayConstraintsCustomCompare` ->
  `FastCheck.UniqueArrayConstraintsCustomCompare`: Depend on fast-check and
  import it directly. The API is unchanged in fast-check v4.
- `FastCheck.UniqueArrayConstraintsCustomCompareSelect` ->
  `FastCheck.UniqueArrayConstraintsCustomCompareSelect`: Depend on fast-check
  and import it directly. The API is unchanged in fast-check v4.
- `FastCheck.UniqueArrayConstraintsRecommended` ->
  `FastCheck.UniqueArrayConstraintsRecommended`: Depend on fast-check and
  import it directly. The API is unchanged in fast-check v4.
- `FastCheck.UniqueArraySharedConstraints` ->
  `FastCheck.UniqueArraySharedConstraints`: Depend on fast-check and import it
  directly. The API is unchanged in fast-check v4.
- `FastCheck.UuidConstraints` -> `FastCheck.UuidConstraints`: Depend on
  fast-check and import it directly. The API is unchanged in fast-check v4.
- `FastCheck.Value` -> `FastCheck.Value`: Depend on fast-check and import it
  directly. The API is unchanged in fast-check v4.
- `FastCheck.VerbosityLevel` -> `FastCheck.VerbosityLevel`: Depend on
  fast-check and import it directly. The API is unchanged in fast-check v4.
- `FastCheck.WebAuthorityConstraints` -> `FastCheck.WebAuthorityConstraints`:
  Depend on fast-check and import it directly. The API is unchanged in
  fast-check v4.
- `FastCheck.WebFragmentsConstraints` -> `FastCheck.WebFragmentsConstraints`:
  Depend on fast-check and import it directly. The API is unchanged in
  fast-check v4.
- `FastCheck.WebPathConstraints` -> `FastCheck.WebPathConstraints`: Depend on
  fast-check and import it directly. The API is unchanged in fast-check v4.
- `FastCheck.WebQueryParametersConstraints` ->
  `FastCheck.WebQueryParametersConstraints`: Depend on fast-check and import it
  directly. The API is unchanged in fast-check v4.
- `FastCheck.WebSegmentConstraints` -> `FastCheck.WebSegmentConstraints`:
  Depend on fast-check and import it directly. The API is unchanged in
  fast-check v4.
- `FastCheck.WebUrlConstraints` -> `FastCheck.WebUrlConstraints`: Depend on
  fast-check and import it directly. The API is unchanged in fast-check v4.
- `FastCheck.WeightedArbitrary` -> `FastCheck.WeightedArbitrary`: Depend on
  fast-check and import it directly. The API is unchanged in fast-check v4.
- `FastCheck.WithAsyncToStringMethod` -> `FastCheck.WithAsyncToStringMethod`:
  Depend on fast-check and import it directly. The API is unchanged in
  fast-check v4.
- `FastCheck.WithCloneMethod` -> `FastCheck.WithCloneMethod`: Depend on
  fast-check and import it directly. The API is unchanged in fast-check v4.
- `FastCheck.WithToStringMethod` -> `FastCheck.WithToStringMethod`: Depend on
  fast-check and import it directly. The API is unchanged in fast-check v4.
- `FastCheck.__commitHash` -> `FastCheck.__commitHash`: Depend on fast-check
  and import it directly. The API is unchanged in fast-check v4.
- `FastCheck.__type` -> `FastCheck.__type`: Depend on fast-check and import it
  directly. The API is unchanged in fast-check v4.
- `FastCheck.__version` -> `FastCheck.__version`: Depend on fast-check and
  import it directly. The API is unchanged in fast-check v4.
- `FastCheck.anything` -> `FastCheck.anything`: Depend on fast-check and import
  it directly. The API is unchanged in fast-check v4.
- `FastCheck.array` -> `FastCheck.array`: Depend on fast-check and import it
  directly. The API is unchanged in fast-check v4.
- `FastCheck.assert` -> `FastCheck.assert`: Depend on fast-check and import it
  directly. The API is unchanged in fast-check v4.
- `FastCheck.asyncDefaultReportMessage` ->
  `FastCheck.asyncDefaultReportMessage`: Depend on fast-check and import it
  directly. The API is unchanged in fast-check v4.
- `FastCheck.asyncModelRun` -> `FastCheck.asyncModelRun`: Depend on fast-check
  and import it directly. The API is unchanged in fast-check v4.
- `FastCheck.asyncProperty` -> `FastCheck.asyncProperty`: Depend on fast-check
  and import it directly. The API is unchanged in fast-check v4.
- `FastCheck.asyncStringify` -> `FastCheck.asyncStringify`: Depend on
  fast-check and import it directly. The API is unchanged in fast-check v4.
- `FastCheck.asyncToStringMethod` -> `FastCheck.asyncToStringMethod`: Depend on
  fast-check and import it directly. The API is unchanged in fast-check v4.
- `FastCheck.base64String` -> `FastCheck.base64String`: Depend on fast-check
  and import it directly. The API is unchanged in fast-check v4.
- `FastCheck.bigInt` -> `FastCheck.bigInt`: Depend on fast-check and import it
  directly. The API is unchanged in fast-check v4.
- `FastCheck.bigInt64Array` -> `FastCheck.bigInt64Array`: Depend on fast-check
  and import it directly. The API is unchanged in fast-check v4.
- `FastCheck.bigIntN` -> `FastCheck.bigInt`: Depend on fast-check and import it
  directly. Express the signed bit range with min and max constraints.
- `FastCheck.bigUint64Array` -> `FastCheck.bigUint64Array`: Depend on
  fast-check and import it directly. The API is unchanged in fast-check v4.
- `FastCheck.boolean` -> `FastCheck.boolean`: Depend on fast-check and import
  it directly. The API is unchanged in fast-check v4.
- `FastCheck.check` -> `FastCheck.check`: Depend on fast-check and import it
  directly. The runner remains, but RunDetails.error was replaced by
  errorInstance in fast-check v4.
- `FastCheck.clone` -> `FastCheck.clone`: Depend on fast-check and import it
  directly. The API is unchanged in fast-check v4.
- `FastCheck.cloneIfNeeded` -> `FastCheck.cloneIfNeeded`: Depend on fast-check
  and import it directly. The API is unchanged in fast-check v4.
- `FastCheck.cloneMethod` -> `FastCheck.cloneMethod`: Depend on fast-check and
  import it directly. The API is unchanged in fast-check v4.
- `FastCheck.commands` -> `FastCheck.commands`: Depend on fast-check and import
  it directly. The API is unchanged in fast-check v4.
- `FastCheck.compareBooleanFunc` -> `FastCheck.compareBooleanFunc`: Depend on
  fast-check and import it directly. The API is unchanged in fast-check v4.
- `FastCheck.compareFunc` -> `FastCheck.compareFunc`: Depend on fast-check and
  import it directly. The API is unchanged in fast-check v4.
- `FastCheck.configureGlobal` -> `FastCheck.configureGlobal`: Depend on
  fast-check and import it directly. The API is unchanged in fast-check v4.
- `FastCheck.constant` -> `FastCheck.constant`: Depend on fast-check and import
  it directly. The API remains; v4 infers literal types by default.
- `FastCheck.constantFrom` -> `FastCheck.constantFrom`: Depend on fast-check
  and import it directly. The API is unchanged in fast-check v4.
- `FastCheck.context` -> `FastCheck.context`: Depend on fast-check and import
  it directly. The API is otherwise unchanged.
- `FastCheck.createDepthIdentifier` -> `FastCheck.createDepthIdentifier`:
  Depend on fast-check and import it directly. The API is unchanged in
  fast-check v4.
- `FastCheck.date` -> `FastCheck.date`: Depend on fast-check and import it
  directly. The API is unchanged in fast-check v4.
- `FastCheck.defaultReportMessage` -> `FastCheck.defaultReportMessage`: Depend
  on fast-check and import it directly. The API is unchanged in fast-check v4.
- `FastCheck.dictionary` -> `FastCheck.dictionary`: Depend on fast-check and
  import it directly. The API is unchanged in fast-check v4.
- `FastCheck.domain` -> `FastCheck.domain`: Depend on fast-check and import it
  directly. The API is unchanged in fast-check v4.
- `FastCheck.double` -> `FastCheck.double`: Depend on fast-check and import it
  directly. The API is unchanged in fast-check v4.
- `FastCheck.emailAddress` -> `FastCheck.emailAddress`: Depend on fast-check
  and import it directly. The API is unchanged in fast-check v4.
- `FastCheck.falsy` -> `FastCheck.falsy`: Depend on fast-check and import it
  directly. The API is unchanged in fast-check v4.
- `FastCheck.float` -> `FastCheck.float`: Depend on fast-check and import it
  directly. The API is unchanged in fast-check v4.
- `FastCheck.float32Array` -> `FastCheck.float32Array`: Depend on fast-check
  and import it directly. The API is unchanged in fast-check v4.
- `FastCheck.float64Array` -> `FastCheck.float64Array`: Depend on fast-check
  and import it directly. The API is unchanged in fast-check v4.
- `FastCheck.func` -> `FastCheck.func`: Depend on fast-check and import it
  directly. The API is unchanged in fast-check v4.
- `FastCheck.gen` -> `FastCheck.gen`: Depend on fast-check and import it
  directly. The API is unchanged in fast-check v4.
- `FastCheck.getDepthContextFor` -> `FastCheck.getDepthContextFor`: Depend on
  fast-check and import it directly. The API is unchanged in fast-check v4.
- `FastCheck.hasAsyncToStringMethod` -> `FastCheck.hasAsyncToStringMethod`:
  Depend on fast-check and import it directly. The API is unchanged in
  fast-check v4.
- `FastCheck.hasCloneMethod` -> `FastCheck.hasCloneMethod`: Depend on
  fast-check and import it directly. The API is unchanged in fast-check v4.
- `FastCheck.hasToStringMethod` -> `FastCheck.hasToStringMethod`: Depend on
  fast-check and import it directly. The API is unchanged in fast-check v4.
- `FastCheck.hash` -> `FastCheck.hash`: Depend on fast-check and import it
  directly. The API is unchanged in fast-check v4.
- `FastCheck.hexa` -> `FastCheck.integer`: Depend on fast-check and import it
  directly. Map an integer from 0 through 15 to a hexadecimal character.
- `FastCheck.hexaString` -> `FastCheck.string`: Depend on fast-check and import
  it directly. Pass a hexadecimal-character arbitrary as the string unit.
- `FastCheck.infiniteStream` -> `FastCheck.infiniteStream`: Depend on
  fast-check and import it directly. The API is unchanged in fast-check v4.
- `FastCheck.int16Array` -> `FastCheck.int16Array`: Depend on fast-check and
  import it directly. The API is unchanged in fast-check v4.
- `FastCheck.int32Array` -> `FastCheck.int32Array`: Depend on fast-check and
  import it directly. The API is unchanged in fast-check v4.
- `FastCheck.int8Array` -> `FastCheck.int8Array`: Depend on fast-check and
  import it directly. The API is unchanged in fast-check v4.
- `FastCheck.integer` -> `FastCheck.integer`: Depend on fast-check and import
  it directly. The API is unchanged in fast-check v4.
- `FastCheck.ipV4` -> `FastCheck.ipV4`: Depend on fast-check and import it
  directly. The API is unchanged in fast-check v4.
- `FastCheck.ipV4Extended` -> `FastCheck.ipV4Extended`: Depend on fast-check
  and import it directly. The API is unchanged in fast-check v4.
- `FastCheck.ipV6` -> `FastCheck.ipV6`: Depend on fast-check and import it
  directly. The API is unchanged in fast-check v4.
- `FastCheck.json` -> `FastCheck.json`: Depend on fast-check and import it
  directly. The API is unchanged in fast-check v4.
- `FastCheck.jsonValue` -> `FastCheck.jsonValue`: Depend on fast-check and
  import it directly. The API is unchanged in fast-check v4.
- `FastCheck.letrec` -> `FastCheck.letrec`: Depend on fast-check and import it
  directly. The API is unchanged in fast-check v4.
- `FastCheck.limitShrink` -> `FastCheck.limitShrink`: Depend on fast-check and
  import it directly. The API is unchanged in fast-check v4.
- `FastCheck.lorem` -> `FastCheck.lorem`: Depend on fast-check and import it
  directly. The API is unchanged in fast-check v4.
- `FastCheck.mapToConstant` -> `FastCheck.mapToConstant`: Depend on fast-check
  and import it directly. The API is unchanged in fast-check v4.
- `FastCheck.maxSafeInteger` -> `FastCheck.maxSafeInteger`: Depend on
  fast-check and import it directly. The API is unchanged in fast-check v4.
- `FastCheck.maxSafeNat` -> `FastCheck.maxSafeNat`: Depend on fast-check and
  import it directly. The API is unchanged in fast-check v4.
- `FastCheck.memo` -> `FastCheck.memo`: Depend on fast-check and import it
  directly. The API is unchanged in fast-check v4.
- `FastCheck.mixedCase` -> `FastCheck.mixedCase`: Depend on fast-check and
  import it directly. The API is unchanged in fast-check v4.
- `FastCheck.modelRun` -> `FastCheck.modelRun`: Depend on fast-check and import
  it directly. The API is unchanged in fast-check v4.
- `FastCheck.nat` -> `FastCheck.nat`: Depend on fast-check and import it
  directly. The API is unchanged in fast-check v4.
- `FastCheck.noBias` -> `FastCheck.noBias`: Depend on fast-check and import it
  directly. The API is unchanged in fast-check v4.
- `FastCheck.noShrink` -> `FastCheck.noShrink`: Depend on fast-check and import
  it directly. The API is unchanged in fast-check v4.
- `FastCheck.object` -> `FastCheck.object`: Depend on fast-check and import it
  directly. The API is unchanged in fast-check v4.
- `FastCheck.oneof` -> `FastCheck.oneof`: Depend on fast-check and import it
  directly. The API is unchanged in fast-check v4.
- `FastCheck.option` -> `FastCheck.option`: Depend on fast-check and import it
  directly. The API is unchanged in fast-check v4.
- `FastCheck.pre` -> `FastCheck.pre`: Depend on fast-check and import it
  directly. The API is unchanged in fast-check v4.
- `FastCheck.property` -> `FastCheck.property`: Depend on fast-check and import
  it directly. The API is unchanged in fast-check v4.
- `FastCheck.readConfigureGlobal` -> `FastCheck.readConfigureGlobal`: Depend on
  fast-check and import it directly. The API is unchanged in fast-check v4.
- `FastCheck.record` -> `FastCheck.record`: Depend on fast-check and import it
  directly. The API is unchanged in fast-check v4.
- `FastCheck.resetConfigureGlobal` -> `FastCheck.resetConfigureGlobal`: Depend
  on fast-check and import it directly. The API is unchanged in fast-check v4.
- `FastCheck.sample` -> `FastCheck.sample`: Depend on fast-check and import it
  directly. The API is unchanged in fast-check v4.
- `FastCheck.scheduledModelRun` -> `FastCheck.scheduledModelRun`: Depend on
  fast-check and import it directly. The API is unchanged in fast-check v4.
- `FastCheck.scheduler` -> `FastCheck.scheduler`: Depend on fast-check and
  import it directly. The API is unchanged in fast-check v4.
- `FastCheck.schedulerFor` -> `FastCheck.schedulerFor`: Depend on fast-check
  and import it directly. The API is unchanged in fast-check v4.
- `FastCheck.shuffledSubarray` -> `FastCheck.shuffledSubarray`: Depend on
  fast-check and import it directly. The API is unchanged in fast-check v4.
- `FastCheck.sparseArray` -> `FastCheck.sparseArray`: Depend on fast-check and
  import it directly. The API is unchanged in fast-check v4.
- `FastCheck.statistics` -> `FastCheck.statistics`: Depend on fast-check and
  import it directly. The API is unchanged in fast-check v4.
- `FastCheck.stream` -> `FastCheck.stream`: Depend on fast-check and import it
  directly. The API remains; update custom generator and Random implementations
  for fast-check v4 typings.
- `FastCheck.string` -> `FastCheck.string`: Depend on fast-check and import it
  directly. The API is unchanged in fast-check v4.
- `FastCheck.string16bits` -> `FastCheck.string`: Depend on fast-check and
  import it directly. Pass a char16bits-compatible arbitrary as the string unit.
- `FastCheck.stringMatching` -> `FastCheck.stringMatching`: Depend on
  fast-check and import it directly. The API is unchanged in fast-check v4.
- `FastCheck.subarray` -> `FastCheck.subarray`: Depend on fast-check and import
  it directly. The API is unchanged in fast-check v4.
- `FastCheck.toStringMethod` -> `FastCheck.toStringMethod`: Depend on
  fast-check and import it directly. The API is unchanged in fast-check v4.
- `FastCheck.tuple` -> `FastCheck.tuple`: Depend on fast-check and import it
  directly. The API is unchanged in fast-check v4.
- `FastCheck.uint16Array` -> `FastCheck.uint16Array`: Depend on fast-check and
  import it directly. The API is unchanged in fast-check v4.
- `FastCheck.uint32Array` -> `FastCheck.uint32Array`: Depend on fast-check and
  import it directly. The API is unchanged in fast-check v4.
- `FastCheck.uint8Array` -> `FastCheck.uint8Array`: Depend on fast-check and
  import it directly. The API is unchanged in fast-check v4.
- `FastCheck.uint8ClampedArray` -> `FastCheck.uint8ClampedArray`: Depend on
  fast-check and import it directly. The API is unchanged in fast-check v4.
- `FastCheck.ulid` -> `FastCheck.ulid`: Depend on fast-check and import it
  directly. The API is unchanged in fast-check v4.
- `FastCheck.unicode` -> `FastCheck.integer`: Depend on fast-check and import
  it directly. Map BMP code points while excluding surrogate code points;
  prefer the binary string unit for full Unicode.
- `FastCheck.unicodeString` -> `FastCheck.string`: Depend on fast-check and
  import it directly. Pass a BMP-code-point arbitrary as the unit constraint;
  prefer unit: binary for full Unicode.
- `FastCheck.uniqueArray` -> `FastCheck.uniqueArray`: Depend on fast-check and
  import it directly. The API is unchanged in fast-check v4.
- `FastCheck.uuid` -> `FastCheck.uuid`: Depend on fast-check and import it
  directly. The API is unchanged in fast-check v4.
- `FastCheck.webAuthority` -> `FastCheck.webAuthority`: Depend on fast-check
  and import it directly. The API is unchanged in fast-check v4.
- `FastCheck.webFragments` -> `FastCheck.webFragments`: Depend on fast-check
  and import it directly. The API is unchanged in fast-check v4.
- `FastCheck.webPath` -> `FastCheck.webPath`: Depend on fast-check and import
  it directly. The API is unchanged in fast-check v4.
- `FastCheck.webQueryParameters` -> `FastCheck.webQueryParameters`: Depend on
  fast-check and import it directly. The API is unchanged in fast-check v4.
- `FastCheck.webSegment` -> `FastCheck.webSegment`: Depend on fast-check and
  import it directly. The API is unchanged in fast-check v4.
- `FastCheck.webUrl` -> `FastCheck.webUrl`: Depend on fast-check and import it
  directly. The API is unchanged in fast-check v4.
