# Source inventory

The catalogue was shaped against six local repositories. This document records
what each one actually does, as read from its configuration and source on
2026-10-16, so that a skill's claim about "the estate" can be checked against a
file rather than a memory. Where the design brief assumed something the tree
does not show, the discrepancy is stated.

Grep counts are approximate and exclude `node_modules`, build output, and
worktrees. "Lock" means the version resolved in `bun.lock`.

## Summary

| Repository            | Role in the catalogue                            | TypeScript                | Strictness                               | Lint owners                                        | Tests                                           |
| --------------------- | ------------------------------------------------ | ------------------------- | ---------------------------------------- | -------------------------------------------------- | ----------------------------------------------- |
| `df12-lints`          | Executable-policy home for house lint rules      | `^5.6.3` (lock 5.9.3)     | Fully strict                             | Biome 2.4, Oxlint 1.67 with its own JS plugin      | Bun test, fast-check, snapshot, `npm pack`      |
| `wildside-mockup-v2a` | Strict React browser app with maps and tokens    | `^5.6.3` (lock 5.9.3)     | Fully strict, `--skipLibCheck` in script | Biome 2.3 + 46 Grit plugins, Stylelint 16, Semgrep | Bun + happy-dom, Vitest a11y, Playwright + axe  |
| `corbusier-mockup`    | React, localization, context-sensitive rAF       | `^5.6.3` (lock 5.9.3)     | Fully strict                             | Same family as Wildside                            | Same family as Wildside                         |
| `simulacat-core`      | Published dual-module library and CLI            | `^6.0.3` (lock 6.0.3)     | Strict tsconfig, relaxed Biome           | Biome 2.5, Oxlint 1.72 with a vendored plugin copy | Bun test, Cucumber steps, fast-check            |
| `digitalpuddle`       | Deterministic simulator in design, fork of above | `^6.0.2` (lock 6.0.2)     | Strict tsconfig, relaxed Biome           | Biome 2.4, no Oxlint                               | Bun test, fast-check, one `.test-d.ts`          |
| `velocetty`           | Brownfield Electron terminal, native modules     | `^5.4.5` + native preview | Strict base, relaxed root and typecheck  | Biome 2.3, orphaned Stylelint config               | Bun test (concurrent, shuffled), Playwright e2e |

_Table 1: The six repositories at a glance._

## Six facts that reshaped the design

1. **No repository consumes `df12-lints` as a package.** `simulacat-core`
   vendors an older copy of the plugin at `tools/oxlint-plugin-df12/index.js`;
   the other four do not use Oxlint at all. The catalogue therefore treats
   adoption of the shared package as work to be routed, not as the status quo.
2. **`df12-lints` ships no presets.** It has four custom rules
   (`complex-conditional`, `require-module-jsdoc`, `require-public-jsdoc`,
   `require-private-jsdoc`) plus curated `complexity` and `max-depth` settings,
   and consumers copy a sample `.oxlintrc.json` from its users' guide. The
   "opt-in browser preset" in the design brief does not exist yet;
   `typescript-quality-tools` describes it as the proposed home for
   `prefer-css-state`, not as a shipped artefact.
3. **DigitalPuddle's deterministic worker and virtual clock exist only in
   design documents.** `docs/adr/0004-deterministic-worker.md` and the
   technical design describe a scheduler, a virtual clock, seeded identity, and
   drain-to-idle; `src/worker/` does not exist and the store still calls
   `new Date()`. The vocabulary (a logical worker that owns orchestration) is
   real; the implementation is pending.
4. **Velocetty's Electron configuration is the old style.**
   `app/ui/window.ts` sets `nodeIntegration: true` and
   `contextIsolation: false`, `@electron/remote` is enabled, and there is no
   preload script or `contextBridge`. Renderer-side IPC responses are validated
   with zod 4 (`lib/transport/ipc-schemas.ts`); main-side `ipcMain.handle`
   calls in `app/plugins.ts` validate nothing. The Electron skill is therefore
   a migration guide as much as a design guide.
5. **Velocetty's own type gate is lax.** `tsconfig.base.json` is strict, but
   `tsconfig.json` and `tsconfig.typecheck.json` switch off `strict`,
   `exactOptionalPropertyTypes`, `noUncheckedIndexedAccess`, and the rest for
   the legacy `app/` and `lib/` trees. Only `frontend/`, `backend/`, and
   `shared/` keep the strict base. This is the brownfield ratchet the types
   skill must serve.
6. **Absent everywhere:** Effect, Web Workers, `worker_threads`,
   `requestIdleCallback`, `scheduler.postTask`, `scheduler.yield`, ESLint, FLIP
   animations, and `typos`. The async skill's worker guidance is therefore
   anticipatory, written against library documentation rather than estate code.

## df12-lints

- **Purpose.** Shared lint tooling for JavaScript and TypeScript projects: an
  Oxlint JS plugin plus a small metadata export. Private; consumed as a Git
  dependency pinned to a tag (`github:leynos/df12-lints#v0.1.0`) with
  `jsPlugins: ["df12-lints/oxlint-plugin"]`. Bun consumers need
  `trustedDependencies` because `prepare` builds on install.
- **tsconfig.** `strict`, `noUncheckedIndexedAccess`,
  `exactOptionalPropertyTypes`, `noImplicitOverride`,
  `noPropertyAccessFromIndexSignature`, `useUnknownInCatchVariables`,
  `isolatedModules`, `moduleDetection: force`, `module: ESNext`,
  `moduleResolution: Bundler`, `target: ES2022`, declaration emit to `dist`.
- **Lint.** Biome with `noExcessiveCognitiveComplexity` 8,
  `noExcessiveLinesPerFunction` 70, `useMaxParams` 4; Oxlint with `complexity`
  8, `max-depth` 3, and the four `df12/*` rules.
- **Tests.** Rules are tested by spawning real Oxlint against temporary
  workspaces with generated configuration and snapshotting diagnostics
  (`tests/oxlint-plugin.test.js`); fast-check drives recursive AST arbitraries
  for operator counting. `RuleTester` is not used. A packaging test installs
  the package Git-style and checks `npm pack` contents against an expected list.
- **Plugin API surface used.** ESLint-style `{ meta, create(context) }`,
  `context.sourceCode.text`, `context.sourceCode.getCommentsBefore`,
  `context.report`, `context.options[0]`, `context.filename` and `context.cwd`
  with legacy fallbacks. Option validation via `meta.schema`.
- **Publishing.** `exports` maps `.` to `{ types, default }` under `dist/` and
  `./oxlint-plugin` to committed source. No `publint` or `attw`.

## wildside-mockup-v2a

- **Purpose.** A browser mockup of the Wildside walk planner: Vite, React 19,
  TanStack Router, Tailwind 4, DaisyUI 5, MapLibre GL, Fluent and i18next
  localization, Style Dictionary tokens in `tokens/`.
- **tsconfig.** The strict family above plus `isolatedModules`, `noEmit`,
  `jsx: react-jsx`. `verbatimModuleSyntax` absent. `--skipLibCheck` is passed
  on the command line.
- **Lint.** Biome with 46 GritQL plugins under `tools/grit/` (accessibility,
  DaisyUI misuse, state slots such as `data-state` and `aria-current`, banned
  testing patterns); Stylelint with `stylelint-declaration-strict-value` forcing
  `var(--…)` for colour properties, `declaration-no-important`, and a `px` ban
  on spacing properties; Semgrep rules for raw colour classes and test IDs;
  custom class-list scripts. No animation-property rule. Oxlint and
  `df12-lints` absent.
- **Tests.** Bun test with happy-dom (about 43 files), Vitest with jest-axe
  for accessibility (`*.a11y.test.tsx`), Playwright with `@axe-core/playwright`
  on a single mobile viewport. Testing Library throughout; test IDs banned. No
  fast-check, no `.test-d.ts`.
- **Scheduling and DOM.** No `.style.X =` writes and no custom-property writes
  in TypeScript. State reaches CSS through `data-theme` and `data-direction`
  attributes and Radix `data-state`. MapLibre is lazily imported and driven
  imperatively from `useEffect` in `src/app/components/wildside-map.tsx`. One
  800 ms `setTimeout` simulates generation. The reference HTML screens live in
  `wildside-v2a-examples/*.html`, outside the TypeScript tree.
- **Validation.** None.
- **Strictness signals.** Two `@ts-expect-error` markers, both in tests; one
  `biome-ignore` for `useLiteralKeys` where
  `noPropertyAccessFromIndexSignature` forces bracket access on `process.env`.

## corbusier-mockup

- **Purpose.** A browser mockup for an agent-orchestration platform. Same
  toolchain family as Wildside, plus `scripts/check-hardcoded-strings.ts`.
- **Context-sensitive scheduling.** `use-command-palette-actions.ts` defers
  `router.navigate` with a one-shot `requestAnimationFrame` so the Radix Dialog
  unmounts before navigation. `slash-command-input.tsx` debounces blur with a
  `setTimeout` that is cleaned up. Neither is an animation loop; both are
  legitimate exceptions the browser skill must not flag.
- **Validation.** valibot 1.2 validates fixture data and IDs in `src/data/*.ts`
  with `v.parse` and `v.safeParse`. `localStorage` reads are not validated.
- **Tests.** Bun test with happy-dom (38 files), one Vitest a11y suite,
  eleven Playwright suites, with a Podman fallback for end-to-end runs.
- **Strictness signals.** Zero suppressions, zero `any`.

## simulacat-core

- **Purpose.** A stateful mock GitHub API engine published to npm (0.6.4),
  extending Simulacrum, with a CJS `bin/start.cjs` CLI.
- **tsconfig.** The strict family plus `verbatimModuleSyntax`,
  `allowImportingTsExtensions`, `noEmit`, `ignoreDeprecations: "6.0"`.
- **Packaging.** tsdown builds dual ESM and CJS with declaration maps, shims,
  `attw: true`, `publint: true`, and a `development` export condition pointing
  at `src/index.ts` that `publishConfig.exports` strips. The `exports` map has
  `import` and `require` conditions but no `types` condition; declarations are
  found through top-level `types` pointing at `dist/index.d.cts` and a
  `typesVersions` block. `@arethetypeswrong/core` (the library, not the CLI) is
  the dev dependency.
- **Generated code.** graphql-codegen writes
  `src/__generated__/resolvers-types.ts` from `schema/schema.docs.graphql`; the
  output is listed in `.gitignore` yet also tracked. `sync.ts` fetches the
  OpenAPI document with an `AbortController` timeout.
- **Lint.** Biome 2.5 with the Hyper-derived relaxations (`noExplicitAny` off,
  `noNonNullAssertion` off) and the same complexity limits as `df12-lints`.
  Oxlint runs a vendored, older copy of the df12 plugin with an 83-entry JSDoc
  baseline.
- **Tests.** Bun test with `--max-concurrency=1`, Cucumber steps through
  `@aboviq/bun-test-cucumber`, fast-check in four files. No `.test-d.ts`,
  contrary to the design brief.
- **Validation.** zod 3 for the initial store, entity builders, and the
  OpenAPI document.

## digitalpuddle

- **Purpose.** A local DigitalOcean API simulator for deterministic
  infrastructure tests, forked from `simulacat-core` and being reshaped.
- **Determinism model (designed).** ADR 0004 and the technical design specify:
  handlers only validate, update state, create actions, enqueue work, and
  respond; a worker owns engine side effects; jobs are keyed by virtual time
  and drained in order; the admin API advances the clock
  (`POST /_digitalpuddle/clock/tick`) and drains to idle; journals carry both
  virtual and wall timestamps; a same-seed double run must produce
  byte-identical journals. Planned files:
  `src/worker/{scheduler,clock,transitions,faults}.ts`.
- **Determinism model (implemented).** `src/openapi/capabilities.ts` carries
  the `runtimeBehaviour` vocabulary
  (`handler | worker | fixture | not-implemented`) and a refinement that
  engine-backed entries require worker orchestration. Store code still uses
  `new Date()`.
- **Type tests.** `tests/openapi-capabilities.test-d.ts` is the estate's only
  compile-time test file: one `@ts-expect-error` rejecting an invalid
  `Capability` literal and `satisfies` checks on manifest shapes. It is
  type-checked through the tsconfig `include`, not a separate runner.
- **Packaging, lint, validation.** As `simulacat-core`, minus Oxlint and minus
  the Biome complexity limits.

## velocetty

- **Purpose.** A terminal built on web standards, forked from Hyper. Electron
  40 main process in `app/` (CommonJS), React 19 renderer in `lib/` (mostly
  class components, Redux 5), new layered packages `frontend/`, `backend/`,
  `shared/`, and a CLI.
- **TypeScript.** `typescript ^5.4.5` for library consumers
  (`scripts/check-package-boundaries.mjs`, `typescript-json-schema`) and
  `@typescript/native-preview ^7.0.0-dev.20260128.1` for every type-check and
  build script (`bunx tsgo --project …`). This is the only estate repository on
  the native compiler and it is on a January development build.
- **tsconfig ratchet.** `tsconfig.base.json` is strict with
  `verbatimModuleSyntax`, `composite`, `allowJs`, `checkJs: false`.
  `tsconfig.json` and `tsconfig.typecheck.json` turn off `strict`,
  `noImplicitAny`, `exactOptionalPropertyTypes`, `noUncheckedIndexedAccess`,
  `noPropertyAccessFromIndexSignature`, `noImplicitOverride`,
  `useUnknownInCatchVariables`, and `verbatimModuleSyntax` for `app/`, `lib/`,
  `cli/`, and `typings/`. `app/tsconfig.json` uses `module: commonjs` and
  `moduleResolution: node`, both of which TypeScript 6 deprecates.
- **Electron.** `nodeIntegration: true`, `contextIsolation: false`,
  `@electron/remote` enabled, no preload, no `contextBridge`. IPC contracts are
  typed in `shared/src/types/common.ts` (`IpcCommands`, `MainEvents`,
  `RendererEvents`) and `shared/src/types/transport.ts`. The renderer validates
  every `invoke` result with zod 4 (`lib/transport/ipc-schemas.ts`,
  `satisfies Record<keyof IpcCommands, ZodType>`, `.passthrough()` objects).
  `ipcMain.handle` in `app/plugins.ts` passes arguments such as a shell
  `command` through unvalidated. `app/rpc.ts` uses a per-window UUID channel
  and guards destroyed windows before `send`.
- **Native modules.** `node-pty` 1.1.0 with a load-failure message and a
  rebuild script, `native-process-working-directory`, optional `native-reg`,
  patched `leveldown` and `node-gyp-build`.
- **Batching and frame timing.** `app/session.ts` `DataBatcher` flushes PTY
  output every 16 ms or at 200 KiB, whichever first, with a `StringDecoder`
  reset before emit for re-entrancy. `lib/components/term.tsx` runs a
  self-rescheduling `requestAnimationFrame` loop that records frame durations
  while the document is visible (long frame threshold 16 ms) and a coalesced
  one-per-frame visibility sync; both are cancelled on unmount.
  `scripts/run-pty-frame-timing-benchmark.mjs` asserts a long-frame ratio below
  0.05 and p95 input latency below 24 ms.
- **Imperative DOM.** `term.tsx` writes `term.element.style.padding`;
  `split-pane.tsx` writes `left` or `top` through `style.setProperty` during a
  drag and removes it afterwards (a geometry adapter, not a custom property);
  `notification.tsx` writes `background-color` with `!important`. xterm 5.3
  renders through WebGL with an `onContextLoss` fallback to the canvas addon,
  and a WebGL context pool (`lib/utils/webgl-context-pool.ts`) bounds contexts.
- **Cancellation and shutdown.** `AbortSignal` in `cli/api.ts` (validated with
  `z.instanceof(AbortSignal)`) and `app/plugins/install.ts`; `Session.destroy`
  kills the PTY; `before-quit` closes the config watcher; `window-all-closed`
  quits on non-macOS. No `SIGTERM` or `uncaughtException` handlers in `app/`.
- **Strictness signals.** 5 `@ts-expect-error` (one in source for react-redux
  `connect`), 14 `as any`, 65 `: any` concentrated in `lib/utils/plugins.ts` and
  `typings/hyper.d.ts`. Biome `noExplicitAny` is off. Stylelint configuration
  exists but is not installed or run.

## How the inventory feeds the catalogue

- `typescript-types-and-apis` carries a brownfield ratchet because Velocetty's
  layered tsconfigs are the real shape of a partial migration.
- `typescript-modules-and-packaging` and `arch-typescript-package-design`
  take their consumer-check material from Simulacat's tsdown configuration,
  including the missing `types` condition and the `development` condition
  stripped at publish time.
- `electron-and-ipc` is a privilege-separation migration first and a design
  guide second, because Velocetty has not yet separated privilege.
- `browser-main-thread-performance` keeps Corbusier's one-shot
  `requestAnimationFrame` and Velocetty's split-pane geometry write as named
  exceptions, so the skill cannot be read as "ban every imperative write".
- `typescript-quality-tools` describes the Wildside and Corbusier three-tool
  arrangement (Biome with Grit, Stylelint, Semgrep) and proposes
  `prefer-css-state` and `stylelint-high-performance-animation` as additions
  rather than describing them as present.
- `typescript-7-transition` treats Velocetty's January native-preview build
  and the simulators' `ignoreDeprecations: "6.0"` as the two live transition
  states in the estate.
- `typescript-verification` and `typescript-testing` take the compile-time
  test shape from DigitalPuddle's single `.test-d.ts` file and the
  property-test shape from the simulators' fast-check suites.
