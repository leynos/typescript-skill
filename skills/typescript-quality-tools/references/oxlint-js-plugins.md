# Oxlint JS plugins

Reviewed 2026-10-16 against the Oxc documentation and the March 2026 alpha
announcement. Oxlint was at 1.88.0 on npm. JS plugins are **alpha** and not
subject to semantic versioning; recheck this page before relying on an API
detail.

## Configuration

```json
{
  "jsPlugins": ["df12-lints/oxlint-plugin", "./tools/local-plugin.js"],
  "categories": { "correctness": "off" },
  "rules": {
    "complexity": ["error", { "max": 8 }],
    "max-depth": ["error", 3],
    "df12/complex-conditional": ["error", { "maxLogicalOperators": 1 }],
    "df12/require-public-jsdoc": "error"
  }
}
```

- `jsPlugins` takes relative paths (resolved from the configuration file),
  package names, or scoped packages. An object form `{ name, specifier }`
  aliases a plugin, which matters when a plugin name clashes with a native
  Oxlint plugin.
- Rules are referenced as `plugin/rule` under `rules`.
- Oxlint prefers its native rules where they exist (several `react-hooks`
  rules, for example); alias the JS plugin only for rules Oxlint lacks.

## API surface

The plugin API targets ESLint v9 and later, and differences are treated as
bugs. Supported: AST traversal with `node.parent` and
`context.sourceCode.getAncestors`, fixes, rule options with `meta.schema`,
selectors, `SourceCode` text and token APIs, scope analysis, code-path
analysis, inline `// oxlint-disable` directives, and language-server
integration. Unsupported: custom parsers and file formats (Vue, Svelte, Angular
templates), type-aware rules, and APIs removed in ESLint v9.

The shared plugin uses `{ meta, create(context) }` rule objects,
`context.sourceCode.text`, `context.sourceCode.getCommentsBefore`,
`context.report`, `context.options[0]`, `context.filename`, and `context.cwd`,
with legacy `getFilename()` and `getCwd()` fallbacks. That is a conservative
subset and the right posture while the API is alpha.

## Testing without `RuleTester`

The documentation does not mention `RuleTester`. The shared plugin tests its
rules by spawning the real Oxlint binary against temporary workspaces with a
generated `.oxlintrc.json` and snapshotting the diagnostics. That tests the
rule as consumers run it and survives API changes in the test harness; keep it
as the pattern. Pair it with fast-check properties over generated ASTs for
rules that count or classify.

## Distribution

- Pin the plugin as a Git dependency on a tag
  (`"df12-lints": "github:leynos/df12-lints#v0.1.0"`).
- Bun consumers must add it to `trustedDependencies` because its `prepare`
  script builds on install.
- Export the plugin entry as committed source under a subpath
  (`./oxlint-plugin`) so it needs no build step to load.

## When this page is stale

- Oxlint's plugin documentation drops the alpha label, or
- a `RuleTester` equivalent appears, or
- type-aware JS rules become supported.

Any of those is a reason to revise this reference and consider whether an
`oxlint-js-plugins` specialist skill has earned its place. Until then the
evergreen quality-tools skill plus this dated page is enough.
