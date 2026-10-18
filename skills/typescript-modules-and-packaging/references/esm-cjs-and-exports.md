# ESM, CJS, and the exports map

## Which format a file is

Node and Bun decide by extension first, then by the nearest `package.json`:

| File           | Format                                                             |
| -------------- | ------------------------------------------------------------------ |
| `.mjs`, `.mts` | Always ESM                                                         |
| `.cjs`, `.cts` | Always CJS                                                         |
| `.js`, `.ts`   | ESM if the nearest `package.json` has `"type": "module"`, else CJS |

_Table 1: How a file's module format is determined._

TypeScript under `module: nodenext` follows the same rules, which is why that
setting is right for anything Node runs directly. `module: esnext` with
`moduleResolution: bundler` is for code a bundler consumes; it accepts
extensionless relative imports that Node would reject.

## Compiler settings by project kind

| Project kind                         | `module`   | `moduleResolution` | Other                                                                             |
| ------------------------------------ | ---------- | ------------------ | --------------------------------------------------------------------------------- |
| Bundled application                  | `esnext`   | `bundler`          | `noEmit`, `verbatimModuleSyntax`, `isolatedModules`                               |
| Node or Bun service, run from source | `nodenext` | (implied)          | `allowImportingTsExtensions` with `noEmit`, or emit `.js`                         |
| Published library                    | `nodenext` | (implied)          | `declaration`, `declarationMap`, `isolatedDeclarations` if public API is explicit |
| Electron main                        | `nodenext` | (implied)          | Emit CJS or ESM per Electron version; record the decision                         |

_Table 2: Module settings by project kind._

## `exports` shape

```json
{
  "name": "@scope/pkg",
  "type": "module",
  "exports": {
    ".": {
      "import": {
        "types": "./dist/index.d.ts",
        "default": "./dist/index.js"
      },
      "require": {
        "types": "./dist/index.d.cts",
        "default": "./dist/index.cjs"
      }
    },
    "./schema": {
      "types": "./dist/schema.d.ts",
      "default": "./dist/schema.js"
    },
    "./package.json": "./package.json"
  },
  "files": ["dist", "README.md", "LICENSE"],
  "sideEffects": false
}
```

Rules:

- `types` first in each block; resolvers take the first matching condition.
- Every public subpath listed; everything else is private by construction.
- `./package.json` exported so tooling can read it.
- `files` lists what ships; check the packed tarball, not the list.
- `sideEffects: false` only when it is true; it lets bundlers tree-shake.

## Development and source conditions

```json
{
  "exports": {
    ".": {
      "development": "./src/index.ts",
      "types": "./dist/index.d.ts",
      "import": "./dist/index.js"
    }
  },
  "publishConfig": {
    "exports": {
      ".": {
        "types": "./dist/index.d.ts",
        "import": "./dist/index.js"
      }
    }
  }
}
```

The `development` condition lets a workspace import source directly in a
monorepo; `publishConfig.exports` replaces the map at publish time so a
consumer never resolves into `src/`. Bun, Vite, and Node all honour custom
conditions when told to (`--conditions development`, `resolve.conditions`).

## Common errors

- `ERR_REQUIRE_ESM`: a CJS file `require`s an ESM-only package. Either ship a
  CJS build, or let the consumer use `import()`. Recent Node can `require` ESM
  without top-level `await`, but do not rely on it for a published package
  without stating the floor.
- `ERR_PACKAGE_PATH_NOT_EXPORTED`: the consumer imports a subpath the map
  does not list. Add it or document that it is private.
- `Cannot find module` with a `.js` specifier in `.ts` source: that is
  correct under `nodenext`; the compiler maps `.js` to `.ts`.
- Default import of a CJS module gives `{ default: … }`: with
  `esModuleInterop` on, this is usually a declaration problem; run `attw`.
  Whether the switch can still be turned off depends on the compiler release;
  `typescript-7-transition` names the release that removed the off switch.
