# Side by side and npm aliases

Reviewed 2026-10-16. The release notes recommend npm aliases for running
TypeScript 6 and 7 together; Bun honours the same `npm:` alias syntax.

## Option A: `tsc` is 7, library consumers get 6

```json
{
  "devDependencies": {
    "typescript": "7.0.2",
    "@typescript/typescript6": "6.0.3"
  }
}
```

Tools that `import "typescript"` resolve 7.0.2 and fail, because 7.0 has no
API. Point them at 6 explicitly where they allow it (`typescript-eslint` reads
its peer; a schema generator may take a path), or use option B.

## Option B: `typescript` is 6, `tsc` from an alias

```json
{
  "devDependencies": {
    "typescript": "npm:@typescript/typescript6@6.0.3",
    "@typescript/native": "npm:typescript@7.0.2"
  },
  "scripts": {
    "check:types": "tsc -p tsconfig.json",
    "check:types:6": "tsc6 -p tsconfig.json"
  }
}
```

With this layout every library consumer sees the 6.0 API through the
`typescript` name, `tsc6` is the 6.0 compiler, and the `@typescript/native`
alias provides the 7.0 `tsc` on `PATH` through its `bin`. The release notes
show this arrangement; check which binary `npx tsc` resolves to in the project
and write it in the script name.

## The compare script

```sh
#!/usr/bin/env bash
set -euo pipefail
out6=$(mktemp -d); out7=$(mktemp -d)
npx tsc6 -p tsconfig.json --noEmit --pretty false > "$out6/diagnostics.txt" || true
npx tsc  -p tsconfig.json --noEmit --pretty false > "$out7/diagnostics.txt" || true
diff <(sort "$out6/diagnostics.txt") <(sort "$out7/diagnostics.txt") && echo "diagnostics agree"
```

For emit comparison, point both at a scratch `outDir` and diff the trees,
ignoring source maps. Run with `stableTypeOrdering` on in 6.0 so declaration
output orders unions the same way.

Expected differences to explain rather than fix:

- union ordering if 6.0 ran without `stableTypeOrdering`;
- template literal inference over astral characters;
- JavaScript-file diagnostics under `checkJs`.

Anything else is either a removed option that 6.0 should already have reported,
or a bug worth reporting with the minimal repro the diff gives you.

## Editors

- VS Code: the `TypeScriptTeam.native-preview` extension enables 7 by default
  and has commands to toggle it. Projects with embedded languages (Vue, Svelte,
  Astro, MDX) should keep the editor on 6.0 until their language services ship
  against the 7.1 API, while running 7.0 `tsc` in the gate.
- Visual Studio enables 7 automatically by workspace.
- Other LSP editors connect to the 7.0 language server, which is LSP-native
  and multithreaded.

## Nightlies

`typescript@next` carries nightlies again. `@typescript/native-preview` is
retired; a project pinned to a dated preview build (`7.0.0-dev.2026…`) should
move to `typescript@7.0.x` and delete the preview dependency.

## Bun

`bun install` honours `npm:` aliases. `bunx tsc` resolves the `typescript`
package's `bin`; with option B, that is `tsc6`, so scripts must call the
alias's binary explicitly or use option A. Pin exact versions in both
`package.json` and `bun.lock`, and run the compare script in CI during the
transition.
