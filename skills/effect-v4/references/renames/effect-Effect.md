<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `effect/Effect` v3 → v4

- `Effect.Adapter` -> `none`: The generator adapter type was removed; yield
  Effect values directly inside `Effect.gen`.
- `Effect.All.ExtractMode` -> `Effect.All.Return`: The `either` extraction
  helper was removed; use `mode: "result"` and the v4 return helper.
- `Effect.Blocked` -> `none`: The request-runtime blocked model is internal;
  use public `Request` and `RequestResolver` APIs.
- `Effect.Effect.AsEffect` -> `Effect.Effect`: Use the Effect type directly and
  extract channels with `Effect.Success`, `Effect.Error`, and `Effect.Services`.
- `Effect.Effect.Context` -> `Effect.Services`: Use the renamed type-level
  extractor for required services.
- `Effect.Effect.VarianceStruct` -> `Effect.Variance`: Use the v4 variance
  interface.
- `Effect.EffectGenerator` -> `Effect.EffectIterator`: Use the v4 iterator type
  used by generator delegation.
- `Effect.EffectTypeId` -> `Effect.TypeId`: Use the v4 type-level Effect
  identifier.
- `Effect.EffectUnifyIgnore` -> `none`: The internal unification-ignore helper
  is no longer public; rely on v4 Effect inference.
- `Effect.FunctionWithSpanOptions` -> `Tracer.SpanOptions`: Use the v4 tracing
  options type when wrapping functions with `Effect.withSpan`.
- `Effect.LatchUnify` -> `Latch.Latch`: Latch moved to the standalone
  `effect/Latch` module; rely on normal v4 inference.
- `Effect.LatchUnifyIgnore` -> `none`: The internal Latch unification helper
  was removed; use `Latch.Latch` directly.
- `Effect.Permit` -> `Semaphore.Semaphore`: Use the standalone Semaphore API
  and its `withPermit` / `withPermits` methods.
- `Effect.Service` -> `Context.Service`: Replace the `effect` constructor
  option with `make`. V4 does not generate a `Default` layer or wire
  `dependencies`; define a `Layer.effect` and provide its dependencies
  explicitly.
- `Effect.Service.AllowedType` -> `Context.Service`: Service type machinery
  moved to `Context.Service`; do not reference its internal helper types.
- `Effect.Service.Class` -> `Context.Service`: Service classes are now defined
  with `Context.Service`.
- `Effect.Service.HasArguments` -> `Context.Service`: Service constructor
  typing is handled by `Context.Service`.
- `Effect.Service.MakeAccessors` -> `Context.Service`: Use the generated `.use`
  helper instead of v3 accessor type machinery.
- `Effect.Service.MakeArguments` -> `Context.Service`: Pass a `make` Effect in
  the v4 `Context.Service` options.
- `Effect.Service.MakeContext` -> `Context.Service`: Service context typing is
  inferred by `Context.Service`.
- `Effect.Service.MakeDeps` -> `Layer.provide`: Compose service dependencies
  explicitly with Layers.
- `Effect.Service.MakeDepsE` -> `Layer.Error`: Use Layer channel extractors
  rather than Service internals.
- `Effect.Service.MakeDepsIn` -> `Layer.Services`: Use Layer channel extractors
  rather than Service internals.
- `Effect.Service.MakeDepsOut` -> `Layer.Success`: Use Layer channel extractors
  rather than Service internals.
- `Effect.Service.MakeError` -> `Layer.Error`: Use the Layer error-channel
  extractor.
- `Effect.Service.MakeService` -> `Context.Service`: The service shape is
  inferred by `Context.Service`.
- `Effect.Service.ProhibitedType` -> `Context.Service`: Do not reference the
  removed internal validation type.
- `Effect.Tag` -> `Context.Service`: Define services with `Context.Service`;
  use the generated `.use` helper for accessors.
- `Effect.Tag.AllowedType` -> `Context.Service`: Tag validation internals were
  removed; use `Context.Service` directly.
- `Effect.Tag.ProhibitedType` -> `Context.Service`: Tag validation internals
  were removed; use `Context.Service` directly.
- `Effect.Tag.Proxy` -> `Context.Service.use`: Replace proxy accessors with the
  generated `.use` helper.
- `Effect.acquireReleaseInterruptible` -> `Effect.acquireRelease`: Pass
  `{ interruptible: true }` in the options object.
- `Effect.allSuccesses` -> `Effect.all`: Run with `{ mode: "result" }`, then
  retain `Result.Success` values.
- `Effect.allWith` -> `Effect.all`: Wrap `Effect.all(values, options)` in a
  lambda when a data-last combinator is needed.
- `Effect.allowInterrupt` -> `Effect.yieldNow`: Yield to the scheduler to
  create an interruptible checkpoint.
- `Effect.ap` -> `Effect.zipWith`: Zip the function effect and value effect,
  then apply the function in the combiner.
- `Effect.asSomeError` -> `Effect.mapError`: Map errors with `Option.some`.
- `Effect.async` -> `Effect.callback`: Use the renamed callback constructor.
- `Effect.asyncEffect` -> `Effect.callback`: The callback registration may
  return an Effect cleanup action in v4.
- `Effect.bindAll` -> `Effect.bind + Effect.all`: Bind the result of
  `Effect.all` explicitly in the do-notation pipeline.
- `Effect.blocked` -> `none`: The request-runtime blocked constructor is
  internal; express work with `Effect.request` and a `RequestResolver`.
- `Effect.cacheRequestResult` -> `none`: Direct request-cache mutation was
  removed; configure request resolution through `RequestResolver`.
- `Effect.cachedFunction` -> `none`: The function memoizer was removed; use
  `Cache` for keyed effectful caching.
- `Effect.catchAll` -> `Effect.catch`: Use the shortened v4 error-handler name.
- `Effect.catchAllCause` -> `Effect.catchCause`: Use the shortened v4
  cause-handler name.
- `Effect.catchAllDefect` -> `Effect.catchDefect`: Use the shortened v4
  defect-handler name.
- `Effect.catchSome` -> `Effect.catchFilter`: Replace the Option-returning
  partial function with a `Filter` and handler.
- `Effect.catchSomeCause` -> `Effect.catchCauseFilter`: Replace the
  Option-returning partial function with a cause `Filter` and handler.
- `Effect.catchSomeDefect` -> `none`: Use `Effect.catchDefect` and branch
  explicitly, re-dying for unmatched defects.
- `Effect.cause` -> `Effect.exit`: Inspect `Exit.Failure.cause`; v4 no longer
  exposes an Effect-only cause extractor.
- `Effect.checkInterruptible` -> `none`: Interruptibility introspection was
  removed; structure the region explicitly with `Effect.interruptible` or
  `Effect.uninterruptible`.
- `Effect.clock` -> `Clock.Clock`: Services are Effects in v4; yield or compose
  `Clock.Clock` directly.
- `Effect.configProviderWith` -> `ConfigProvider.ConfigProvider.use`: Use the
  ConfigProvider reference's `.use` helper to invoke the effectful callback.
- `Effect.console` -> `Console.Console`: Services are Effects in v4; yield or
  compose `Console.Console` directly.
- `Effect.consoleWith` -> `Console.Console.use`: Use the Console reference's
  `.use` helper to invoke the effectful callback.
- `Effect.contextWithEffect` -> `Effect.contextWith`: `contextWith` accepts an
  effectful callback in v4.
- `Effect.currentPropagatedSpan` -> `Effect.currentParentSpan`: Use the current
  parent span representation.
- `Effect.custom` -> `none`: The low-level custom instruction constructor was
  removed; use public constructors such as `Effect.sync`, `Effect.suspend`, or
  `Effect.callback`.
- `Effect.daemonChildren` -> `Effect.awaitAllChildren`: Use structured
  child-fiber waiting, or fork explicitly with `Effect.forkDetach` when
  detachment is intended.
- `Effect.descriptor` -> `Effect.fiberId`: The full fiber descriptor was
  removed; retrieve the current numeric fiber id.
- `Effect.descriptorWith` -> `Effect.fiberId + Effect.flatMap`: Read the
  current fiber id and invoke the callback explicitly.
- `Effect.dieMessage` -> `Effect.die`: Construct the desired defect explicitly
  and pass it to `Effect.die`.
- `Effect.dieSync` -> `Effect.suspend + Effect.die`: Evaluate the lazy defect
  inside `Effect.suspend`.
- `Effect.diffFiberRefs` -> `none`: The public FiberRefs diff API was removed;
  model fiber-local state with context references and scoped
  `Effect.provideService`.
- `Effect.disconnect` -> `Effect.forkDetach`: Fork explicitly and decide how to
  await or interrupt the detached Fiber.
- `Effect.dropUntil` -> `none`: Use an explicit `Effect.gen` loop for an
  effectful stopping predicate.
- `Effect.dropWhile` -> `none`: Use an explicit `Effect.gen` loop, or
  `Array.dropWhile` when the predicate is pure.
- `Effect.either` -> `Effect.result`: V4 represents typed success/failure as
  `Result` instead of `Either`.
- `Effect.ensureErrorType` -> `Effect.satisfiesErrorType`: Use the renamed
  compile-time channel constraint.
- `Effect.ensureRequirementsType` -> `Effect.satisfiesServicesType`: Use the
  renamed compile-time services constraint.
- `Effect.ensureSuccessType` -> `Effect.satisfiesSuccessType`: Use the renamed
  compile-time channel constraint.
- `Effect.ensuringChild` -> `Effect.ensuring + Fiber APIs`: Track the child
  Fiber explicitly and run the finalizer with `Effect.ensuring`.
- `Effect.ensuringChildren` -> `Effect.awaitAllChildren + Effect.ensuring`: Use
  structured child waiting and an explicit finalizer.
- `Effect.every` -> `Effect.forEach`: Evaluate predicates with
  `Effect.forEach`, then test the resulting booleans with `Array.every`.
- `Effect.exists` -> `Effect.findFirst`: Find the first value satisfying the
  effectful predicate and test the returned Option.
- `Effect.fiberIdWith` -> `Effect.fiberId + Effect.flatMap`: Read the numeric
  fiber id and invoke the callback explicitly.
- `Effect.filterEffectOrElse` -> `Effect.flatMap`: Evaluate the effectful
  predicate and branch to `Effect.succeed` or the fallback.
- `Effect.filterEffectOrFail` -> `Effect.flatMap`: Evaluate the effectful
  predicate and branch to `Effect.succeed` or `Effect.fail`.
- `Effect.filterOrDie` -> `Effect.filterOrFail + Effect.orDie`: Filter with a
  typed failure, then convert it to a defect.
- `Effect.filterOrDieMessage` -> `Effect.filterOrFail + Effect.orDie`: Create
  the message-bearing error in `filterOrFail`, then convert it to a defect.
- `Effect.finalizersMask` -> `none`: Configurable finalizer execution
  strategies were removed; register ordered finalizers explicitly in a Scope.
- `Effect.flipWith` -> `Effect.flip`: Flip, apply the transformation, then flip
  the resulting Effect back.
- `Effect.fn.Gen` -> `Effect.fn.Return`: Use the v4 generator-return helper
  type.
- `Effect.fn.NonGen` -> `Effect.fn.Untraced`: Use the v4 function helper type
  for non-generator wrapping.
- `Effect.fork` -> `Effect.forkChild`: Use the renamed structured child-fiber
  combinator.
- `Effect.forkAll` -> `Effect.forEach + Effect.forkChild`: Fork each effect
  explicitly, or prefer a higher-level concurrent combinator.
- `Effect.forkDaemon` -> `Effect.forkDetach`: Use the renamed detached-fiber
  combinator.
- `Effect.forkWithErrorHandler` -> `Effect.forkChild + Fiber.await`: Fork
  explicitly and observe the Fiber result to handle errors.
- `Effect.fromFiber` -> `Fiber.join`: Join the Fiber to obtain an Effect of its
  result.
- `Effect.fromFiberEffect` -> `Effect.flatMap + Fiber.join`: FlatMap the
  effectful Fiber and join it.
- `Effect.fromNullable` -> `Effect.fromOption + Option.fromNullable`: Convert
  the nullable value to Option, then lift it into Effect.
- `Effect.functionWithSpan` -> `Effect.withSpan`: Wrap the function body with a
  span whose name/options are derived from its arguments.
- `Effect.getFiberRefs` -> `none`: The FiberRefs collection is no longer
  public; access individual context references through Effect services.
- `Effect.getRuntimeFlags` -> `none`: RuntimeFlags are no longer a public
  Effect service; use supported high-level runtime options.
- `Effect.if` -> `Effect.suspend`: Select the branch lazily with a JavaScript
  conditional inside `Effect.suspend`.
- `Effect.ignoreLogged` -> `Effect.ignore`: Pass `{ log: true }` to the
  consolidated ignore combinator.
- `Effect.inheritFiberRefs` -> `none`: Bulk FiberRef inheritance was removed;
  propagate required context references explicitly.
- `Effect.interruptWith` -> `Effect.interrupt`: V4 interruption uses the
  current fiber identity; remove the explicit FiberId argument.
- `Effect.intoDeferred` -> `Deferred.into`: Use the Deferred module combinator.
- `Effect.iterate` -> `none`: Use an explicit stateful `Effect.gen` loop; v4
  removed the Effect-specific loop helper.
- `Effect.labelMetrics` -> `Metric.withAttributes`: Convert labels to metric
  attributes and scope them around the Effect.
- `Effect.labelMetricsScoped` -> `Metric.withAttributes`: Apply metric
  attributes to the scoped Effect rather than mutating scoped labels.
- `Effect.liftPredicate` -> `Effect.filterOrFail`: Lift the input with
  `Effect.succeed` and apply `filterOrFail`.
- `Effect.linkSpanCurrent` -> `Effect.linkSpans`: Use the v4 span-link
  combinator.
- `Effect.locally` -> `Effect.provideService`: FiberRef values are context
  references in v4; provide the reference for the Effect lifetime.
- `Effect.locallyScoped` -> `Effect.provideService`: Provide the context
  reference around the scoped Effect.
- `Effect.locallyScopedWith` -> `Effect.updateServiceScoped`: Context
  references replace FiberRefs in v4; update the reference for the current
  scope.
- `Effect.locallyWith` -> `Effect.updateService`: Context references replace
  FiberRefs in v4; update the reference around the target Effect.
- `Effect.logAnnotations` -> `References.CurrentLogAnnotations`: Context
  references are Effects in v4; yield or compose
  `References.CurrentLogAnnotations` directly.
- `Effect.loop` -> `none`: Use an explicit `Effect.gen` loop and collect
  results when needed.
- `Effect.makeLatch` -> `Latch.make`: Latch constructors moved to
  `effect/Latch`.
- `Effect.makeSemaphore` -> `Semaphore.make`: Semaphore constructors moved to
  `effect/Semaphore`.
- `Effect.mapAccum` -> `Effect.reduce`: Carry `[state, output]` through an
  effectful reduction.
- `Effect.mapErrorCause` -> `Effect.catchCause + Effect.failCause`: Transform
  the Cause in a cause handler and fail with the mapped Cause.
- `Effect.mapInputContext` -> `Effect.contextWith + Effect.provide`: Build the
  required context from the incoming context and provide it explicitly.
- `Effect.merge` -> `Effect.catch`: Recover each typed error with
  `Effect.succeed` so both channels become success values.
- `Effect.mergeAll` -> `Effect.reduce`: Reduce the input effects with an
  effectful accumulator.
- `Effect.metricLabels` -> `Metric.CurrentMetricAttributes`: Context references
  are Effects in v4; yield or compose `Metric.CurrentMetricAttributes` directly.
- `Effect.negate` -> `Effect.map`: Map the boolean result with logical negation.
- `Effect.none` -> `Effect.flatMap + Option.match`: Fail for `Some` and succeed
  with void for `None`.
- `Effect.once` -> `Effect.cached`: Create the cached Effect once, then execute
  the returned Effect repeatedly.
- `Effect.optionFromOptional` -> `Effect.catchTag`: Map success to
  `Option.some` and recover `NoSuchElementError` with `Option.none`.
- `Effect.orDieWith` -> `Effect.mapError + Effect.orDie`: Map the typed error
  to the desired defect, then convert failures to defects.
- `Effect.orElse` -> `Effect.catch`: Ignore the caught error and evaluate the
  fallback Effect.
- `Effect.orElseFail` -> `Effect.mapError`: Replace every typed error with the
  lazily produced failure value.
- `Effect.parallelErrors` -> `Effect.all`: Use
  `{ mode: "result", concurrency: "unbounded" }` and collect failures
  explicitly.
- `Effect.parallelFinalizers` -> `none`: Parallel finalizer strategy mutation
  was removed; fork independent cleanup explicitly when ordering is irrelevant.
- `Effect.partition` -> `Effect.partition`: The tuple is now [passes, fails],
  the reverse of v3 [failures, successes]. Every effect still runs, and the
  outer effect does not fail.
- `Effect.patchFiberRefs` -> `none`: Bulk FiberRefs patching was removed;
  update individual context references with `Effect.updateService`.
- `Effect.patchRuntimeFlags` -> `none`: RuntimeFlags patching was removed from
  the public API; use supported high-level runtime options.
- `Effect.raceWith` -> `Effect.raceFirst + Fiber APIs`: Use `raceFirst` for
  first completion, or fork both effects and inspect their Exits for custom
  finishers.
- `Effect.random` -> `Random.Random`: Services are Effects in v4; yield or
  compose `Random.Random` directly.
- `Effect.randomWith` -> `Random.Random.use`: Use the Random reference's `.use`
  helper to invoke the effectful callback. Prefer module-level Random
  operations when possible.
- `Effect.reduceEffect` -> `Effect.flatMap + Effect.reduce`: Evaluate the
  initial Effect, then reduce the remaining effects.
- `Effect.reduceRight` -> `Effect.reduce`: Reverse the input first, then
  perform the effectful reduction.
- `Effect.reduceWhile` -> `none`: Use an explicit `Effect.gen` loop that checks
  the accumulator before each step.
- `Effect.repeatN` -> `Effect.repeat`: Pass `{ times: n }` to the consolidated
  repeat combinator.
- `Effect.runRequestBlock` -> `none`: The request-runtime block runner is
  internal; submit requests with `Effect.request`.
- `Effect.runtime` -> `Effect.context + Effect.runForkWith`: Capture services
  as a Context and use the corresponding `run*With` function.
- `Effect.scheduleForked` -> `Effect.schedule + Effect.forkScoped`: Schedule
  the Effect, then fork it in the current Scope.
- `Effect.scopeWith` -> `Effect.scopedWith`: Use the renamed scoped callback
  combinator.
- `Effect.sequentialFinalizers` -> `none`: Sequential reverse-order
  finalization is the normal Scope behavior; remove this wrapper.
- `Effect.serviceConstants` -> `Context.Service.use`: Expose constants from the
  service explicitly or through the generated `use` helper.
- `Effect.serviceFunction` -> `Context.Service.use`: Use the service class
  `.use` helper to build an accessor function.
- `Effect.serviceFunctionEffect` -> `Context.Service.use`: Use the service class
  `.use` helper for effect-returning methods.
- `Effect.serviceFunctions` -> `Context.Service.use`: Define explicit service
  accessors with the generated `.use` helper.
- `Effect.serviceMembers` -> `Context.Service.use`: Define explicit service
  accessors with the generated `.use` helper.
- `Effect.serviceOptional` -> `service`: Services are Effects in v4; yield or
  compose the service key directly. Use `Effect.serviceOption` only when
  absence is expected.
- `Effect.setFiberRefs` -> `none`: Bulk FiberRefs replacement was removed;
  provide individual context references.
- `Effect.step` -> `none`: The low-level Effect stepping API was removed from
  the public surface.
- `Effect.summarized` -> `Effect.gen`: Run the summary Effect before and after
  the target Effect and combine the two measurements explicitly.
- `Effect.supervised` -> `FiberSet`: Track explicitly forked Fibers in a scoped
  `FiberSet` instead of installing a runtime Supervisor.
- `Effect.tagMetrics` -> `Metric.withAttributes`: Convert key/value tags to
  metric attributes.
- `Effect.tagMetricsScoped` -> `Metric.withAttributes`: Apply attributes around
  the scoped Effect.
- `Effect.takeUntil` -> `none`: Use an explicit `Effect.gen` loop for an
  effectful stopping predicate.
- `Effect.takeWhile` -> `none`: Use an explicit `Effect.gen` loop, or
  `Array.takeWhile` when the predicate is pure.
- `Effect.tapBoth` -> `Effect.tapError + Effect.tap`: Tap the failure path
  first, then tap successful values.
- `Effect.tapErrorCause` -> `Effect.tapCause`: Use the shortened v4 cause-tap
  name.
- `Effect.timedWith` -> `Effect.gen`: Read the supplied clock Effect before and
  after the target and compute the Duration explicitly.
- `Effect.timeoutFail` -> `Effect.timeoutOrElse`: Use
  `Effect.fail(onTimeout())` as the timeout fallback.
- `Effect.timeoutFailCause` -> `Effect.timeoutOrElse`: Use
  `Effect.failCause(onTimeout())` as the timeout fallback.
- `Effect.timeoutTo` -> `Effect.timeoutOrElse + Effect.map`: Map successful
  values first and use the timeout fallback for `onTimeout`.
- `Effect.tracerWith` -> `Tracer.Tracer.use`: Use the Tracer reference's `.use`
  helper to invoke the effectful callback.
- `Effect.transplant` -> `none`: Fiber scope grafting was removed; use
  structured concurrency with `forkChild`, `forkScoped`, or `forkIn`.
- `Effect.transposeMapOption` -> `Option.match`: Return `Effect.succeedNone`
  for None and map the Effect result to Some.
- `Effect.try` -> `Effect.try`: Use the callback overload for
  Cause.UnknownError, or the object overload with try and catch to map failures
  to a custom error. The callback-only overload does not accept a custom error
  type parameter.
- `Effect.tryMap` -> `Effect.flatMap + Effect.try`: FlatMap the source value
  into the v4 synchronous try constructor.
- `Effect.tryMapPromise` -> `Effect.flatMap + Effect.tryPromise`: FlatMap the
  source value into the v4 Promise try constructor.
- `Effect.unless` -> `Effect.suspend`: Select `Effect.void` or the target
  Effect with a negated lazy condition.
- `Effect.unlessEffect` -> `Effect.when`: Negate the effectful boolean
  condition, then use the consolidated `when`.
- `Effect.unsafeMakeLatch` -> `Latch.makeUnsafe`: The unsafe constructor moved
  to `effect/Latch`.
- `Effect.unsafeMakeSemaphore` -> `Semaphore.makeUnsafe`: The unsafe
  constructor moved to `effect/Semaphore`.
- `Effect.unsandbox` -> `Effect.catch + Effect.failCause`: Treat the sandboxed
  Cause as an error and fail with that Cause.
- `Effect.updateFiberRefs` -> `none`: Bulk FiberRefs updates were removed;
  update individual context references with `Effect.updateService`.
- `Effect.using` -> `Effect.scoped + Effect.flatMap`: Acquire inside a fresh
  Scope, run the use Effect, and close the Scope afterward.
- `Effect.validateAll` -> `Effect.validate`: Use the consolidated collection
  validation combinator.
- `Effect.validateFirst` -> `Effect.firstSuccessOf`: Map inputs to validation
  effects and select the first success; handle accumulated diagnostics
  explicitly if required.
- `Effect.validateWith` -> `Effect.zipWith`: Zip and combine the Effects; use
  `mode: "result"` when both failures must be retained.
- `Effect.whenEffect` -> `Effect.when`: The v4 `when` combinator accepts an
  effectful boolean condition directly.
- `Effect.whenFiberRef` -> `reference.use + Effect.when`: Use the
  Context.Reference `.use` helper to inspect the value, test it, and branch
  explicitly.
- `Effect.whenLogLevel` -> `none`: Log-level conditional execution was removed;
  configure Logger filtering and guard optional work explicitly.
- `Effect.whenRef` -> `Ref.get + Effect.flatMap`: Read the Ref, test it, and
  branch explicitly.
- `Effect.withClock` -> `Effect.provideService`: Provide `Clock.Clock` for the
  target Effect.
- `Effect.withClockScoped` -> `Effect.provideService`: Provide `Clock.Clock`
  around the scoped Effect.
- `Effect.withConcurrency` -> `none`: Ambient concurrency was removed; pass
  `concurrency` directly to `Effect.all`, `Effect.forEach`, and related
  combinators.
- `Effect.withConfigProvider` -> `Effect.provideService`: Provide
  `ConfigProvider.ConfigProvider` for the target Effect.
- `Effect.withConfigProviderScoped` -> `Effect.provideService`: Provide the
  ConfigProvider around the scoped Effect.
- `Effect.withConsole` -> `Effect.provideService`: Provide `Console.Console`
  for the target Effect.
- `Effect.withConsoleScoped` -> `Effect.provideService`: Provide the Console
  service around the scoped Effect.
- `Effect.withEarlyRelease` -> `Scope.make + Scope.close`: Create a Scope
  explicitly, provide it to acquisition, and retain a close action.
- `Effect.withFiberRuntime` -> `none`: Direct FiberRuntime access was removed;
  use public Effect, Fiber, and Context operations.
- `Effect.withMaxOpsBeforeYield` -> `none`: The scheduler operation budget is
  no longer configurable through Effect.
- `Effect.withMetric` -> `Effect.tap + Metric.update`: Update the Metric
  explicitly from the Effect success value.
- `Effect.withRandom` -> `Effect.provideService`: Provide `Random.Random` for
  the target Effect.
- `Effect.withRandomFixed` -> `Effect.provideService`: Provide a custom
  deterministic `Random.Random` implementation.
- `Effect.withRandomScoped` -> `Effect.provideService`: Provide the Random
  service around the scoped Effect.
- `Effect.withRequestBatching` -> `none`: Ambient request batching
  configuration was removed; configure batching in the `RequestResolver`.
- `Effect.withRequestCache` -> `none`: Ambient request-cache replacement was
  removed; model keyed caching explicitly with `Cache`.
- `Effect.withRequestCaching` -> `none`: Ambient request caching was removed;
  configure resolution or use `Cache` explicitly.
- `Effect.withRuntimeFlagsPatch` -> `none`: RuntimeFlags patching was removed
  from the public API.
- `Effect.withRuntimeFlagsPatchScoped` -> `none`: Scoped RuntimeFlags patching
  was removed from the public API.
- `Effect.withScheduler` -> `none`: Ambient scheduler replacement was removed;
  use supported runtime run options or explicit scheduling combinators.
- `Effect.withSchedulingPriority` -> `none`: Ambient fiber scheduling priority
  was removed from the public API.
- `Effect.withTracerScoped` -> `Effect.provideService`: Provide the Tracer
  service around the scoped Effect.
- `Effect.withUnhandledErrorLogLevel` -> `Effect.ignore`: Handle or explicitly
  ignore child-fiber failures, selecting the desired log behavior at the
  boundary.
- `Effect.zipLeft` -> `Effect.zip + Effect.map`: Zip the Effects and select the
  first tuple element.
- `Effect.zipRight` -> `Effect.andThen`: Sequence the Effects and retain the
  second result.
