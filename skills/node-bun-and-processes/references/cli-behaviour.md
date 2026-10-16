# CLI behaviour

A command-line tool is a user interface with two audiences: a person at a
terminal and a script in a pipeline. Serve both.

## Contract

| Aspect        | Rule                                                                                                                   |
| ------------- | ---------------------------------------------------------------------------------------------------------------------- |
| stdout        | Results only. What a pipe would consume.                                                                               |
| stderr        | Diagnostics, progress, warnings, errors, usage.                                                                        |
| Exit code     | 0 success, 1 failure, 2 usage error; document anything else.                                                           |
| `--help`      | Always available; prints usage to stdout and exits 0.                                                                  |
| `--version`   | Prints the version to stdout and exits 0.                                                                              |
| `--json`      | Machine-readable output when the tool has structured results.                                                          |
| Colour        | Only when stdout is a TTY and `NO_COLOR` is unset; `FORCE_COLOR` overrides.                                            |
| Progress      | Only when stderr is a TTY; never interleaved with stdout results.                                                      |
| Signals       | `SIGINT` cancels the current operation and exits 130 after cleanup.                                                    |
| Configuration | Flags override environment, environment overrides a config file, file overrides defaults. State the order in `--help`. |

_Table 1: The command-line interface contract._

## Argument parsing

Use a typed parser (`node:util` `parseArgs`, or a library for subcommands).
Validate values at parse time (`--port abc` is a usage error, not a `NaN`
later), and route the resulting options object through the same configuration
parser as environment variables so there is one typed configuration. Route that
parse to `typescript-boundaries-and-validation`.

## Errors

- A user error (bad input, missing file) prints one line to stderr, with no
  stack trace, and exits 1 or 2.
- An internal error prints a short message and, when `--verbose` or a debug
  environment variable is set, the stack and cause chain.
- Never print an error to stdout; a consumer parsing results would read it as
  data.

## Interactive versus piped

Detect `process.stdout.isTTY` and `process.stdin.isTTY`. A prompt on a
non-interactive stdin should fail with a usage error naming the flag that
supplies the value, not hang.

## Testing a CLI

- Unit-test the command functions with injected stdout and stderr writers and
  an injected exit function; do not spawn the process for every case.
- One integration test per command spawns the real `bin` with `spawn`, asserts
  exit code, stdout, and stderr separately, and runs under each supported
  runtime.
- Snapshot `--help` output so a flag change is a visible diff.

## Distribution

- `bin` entries point at a file with a shebang and no `.ts` imports.
- If the CLI is a thin wrapper over a library, the wrapper is the only place
  that reads `process.argv`, `process.env`, and `process.exit`.
- A compiled single binary (Bun's `--compile`, or a packager) is a
  distribution choice, not a code structure; the code above stays the same.
