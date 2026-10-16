# Boundary catalogue

Each row names a boundary, its trust level, the usual failure when it is
unguarded, and the shape of the guard.

| Boundary                         | Trust                            | Unguarded failure                                  | Guard                                                              |
| -------------------------------- | -------------------------------- | -------------------------------------------------- | ------------------------------------------------------------------ |
| HTTP response body               | Remote, versioned apart          | `undefined` field read three layers later          | Schema parse per endpoint; status code checked first               |
| HTTP request body                | Hostile                          | Injection, prototype pollution, oversize payload   | Strict schema, size limit, reject unknown keys                     |
| Query and path parameters        | Hostile                          | Type confusion (`?id=1&id=2` is an array)          | Schema with explicit cardinality                                   |
| JSON or YAML configuration file  | Operator                         | Typo silently ignored                              | Schema, reject unknown keys, report every error at once            |
| `process.env`                    | Operator                         | Missing variable discovered at first use           | One parse at startup into a typed object                           |
| CLI arguments                    | Operator                         | `--port abc` passed through as `NaN`               | Parser with typed options; exit with usage                         |
| `localStorage`, `sessionStorage` | Same origin, older code          | Stale shape from a previous release                | Versioned schema; discard and reset on failure                     |
| IndexedDB, SQLite rows           | Same app, older code             | Migration missed a field                           | Versioned schema per store; migration chain tested                 |
| `postMessage` (worker, iframe)   | Same repository, separate deploy | Message from a stale worker after a reload         | Schema per message type; version field; validate on receipt        |
| Electron IPC                     | Renderer may be compromised      | Privilege escalation through an unchecked argument | Schema on main; allowlist of channels; route to `electron-and-ipc` |
| Plugin return value              | Third party                      | Host crashes on a malformed result                 | Adapter that validates and converts errors                         |
| Native binding result            | Third party, no types            | Wrong shape from a version mismatch                | One adapter per binding; validate; convert errors                  |
| Generated API client             | Remote, drifting                 | Server removed a field; client type still has it   | Validate against the generating schema, or accept drift            |
| WebSocket frame                  | Remote                           | Partial or out-of-order message                    | Framing, then schema, then sequence check                          |
| File upload                      | Hostile                          | Path traversal, wrong MIME, oversize               | Name sanitized, size bounded, type sniffed not trusted             |

_Table 1: Boundaries, trust levels, unguarded failures, and guards._

## Reject-by-default details

- Unknown keys on inbound bodies are rejected unless the API is documented as
  forward-compatible, in which case they are stripped and the stripping is
  tested.
- Numbers from JSON are IEEE doubles; integers above `2^53` and identifiers
  that look numeric are strings on the wire.
- Strings have a maximum length at every boundary, even internal ones; the
  default is "whatever the schema says", and the schema should say.
- Dates arrive as strings. Parse to a `Date` or a temporal type at the
  boundary and reject invalid ones; `new Date("garbage")` is `Invalid Date`,
  not an exception.
- `__proto__`, `constructor`, and `prototype` keys are rejected on any object
  that will be merged into another.

## One parse per boundary

```ts
export function parseConfig(raw: unknown): Config {
  const result = ConfigSchema.safeParse(raw);
  if (!result.success) {
    throw new ConfigError(formatIssues(result.error));
  }
  return toConfig(result.data);
}
```

The function has one job: turn `unknown` into `Config` or fail with every
problem listed. It runs once, at startup or at receipt, and nothing downstream
checks the shape again.
