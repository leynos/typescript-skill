# Consumer checks

Three checks, all on the packed artefact, all in CI.

## 1. `publint`

```sh
npm pack --pack-destination /tmp/pack
npx publint /tmp/pack/scope-pkg-1.2.3.tgz
```

Catches `package.json` mistakes: `exports` entries that point at missing files,
`types` not first, `module` field misuse, `files` omissions, `bin` without a
shebang. Run it against the tarball so `files` and `publishConfig` are applied.

## 2. `attw`

```sh
npx @arethetypeswrong/cli --pack .
```

Resolves every export under every resolution mode and reports declaration
problems (see
[declarations-and-dual-packages.md](declarations-and-dual-packages.md)).
`--pack` builds the tarball first. Build tools such as tsdown can run both
`publint` and `attw` as part of the build (`attw: true`, `publint: true`); that
is convenient, but keep an explicit CI step too so a build-tool upgrade cannot
silently drop the check.

## 3. Packed-install smoke test

```sh
tmp=$(mktemp -d)
npm pack --pack-destination "$tmp"
cd "$tmp" && npm init -y >/dev/null
npm install ./scope-pkg-1.2.3.tgz typescript
printf 'import { x } from "@scope/pkg"; console.log(typeof x);\n' > esm.mjs
printf 'const { x } = require("@scope/pkg"); console.log(typeof x);\n' > cjs.cjs
printf 'import { x } from "@scope/pkg"; const y: number = x;\n' > check.ts
node esm.mjs && node cjs.cjs && npx tsc --noEmit --module nodenext check.ts
```

This proves what no static check can: the artefact installs, the runtime loads
each entry, and a TypeScript consumer resolves the declarations. Add a `bin`
invocation if the package ships one, and run the ESM and CJS cases under Bun
too if Bun is a supported consumer.

## What the checks do not cover

- Behaviour. The smoke test imports; the package's own test suite tests.
- Peer dependency ranges. Test against the lowest and highest supported
  versions of each peer in a matrix if the range is wide.
- Bundle size. Measure with the consumer's bundler if it matters, and record
  the number in the README so a regression is visible.
- The `development` condition path. Test it separately in the monorepo,
  because the packed artefact deliberately lacks it.

## Where in the estate this already runs

The two published packages in the estate wire `attw` and `publint` through
tsdown and rely on `typesVersions` plus a top-level `types` field rather than a
`types` condition. That passes the tools but is fragile under `node16`
resolution; adding `types` to each condition block is the fix. See
[the source inventory](../../../docs/source-inventory.md) for the current state.
