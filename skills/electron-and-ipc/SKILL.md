---
name: electron-and-ipc
description: Use for Electron applications in TypeScript and JavaScript, including main, renderer, and preload privilege separation, context isolation, typed and validated IPC, cancellation across processes, protocol versioning, native add-ons, renderer scheduling, and shutdown.
metadata:
  globs: "**/electron-builder.*, **/electron.vite.config.*, **/preload*.ts, **/main/**/*.ts, **/renderer/**/*.ts, **/renderer/**/*.tsx, **/shared/**/*.ts, **/*.ts, **/*.tsx"
---

# Electron and IPC

Use this when code runs in an Electron application and the question is which
process it belongs in, how the processes talk, and what happens when one of
them is compromised, slow, or shutting down.

## Working stance

- The renderer is a web page. Treat it as untrusted even when the team wrote
  it: a single injected script or a vulnerable dependency gives an attacker
  whatever the renderer can reach.
- Privilege lives in the main process. The renderer asks; the main process
  decides, validates, and acts.
- The preload script is the only bridge. It exposes a small, typed, named API
  through `contextBridge`; it never exposes `ipcRenderer` itself, Node modules,
  or a generic "invoke anything" function.
- IPC is a boundary like HTTP: every message is validated on receipt, every
  channel is in an allowlist, and every error is serialized deliberately.
- Cancellation crosses the boundary explicitly: a request identifier and a
  cancel message, not a dropped promise.
- Shutdown is coordinated: the main process stops accepting IPC, aborts
  in-flight work, closes native resources, then quits.

## Decision surface

- **Where does this code run?** Main for anything touching the file system,
  processes, native modules, or OS APIs. Renderer for everything that draws.
  Preload for the bridge and nothing else. Shared for protocol types and
  schemas, with no runtime imports from either side.
- **Privilege separation.** `contextIsolation: true`, `nodeIntegration: false`,
  `sandbox: true`, no `@electron/remote`. A brownfield application that has
  none of these migrates one window at a time; the order and the traps are in
  [privilege-separation-migration.md](references/privilege-separation-migration.md).
- **Typed IPC.** One shared protocol module defines each channel's request and
  response schema; the main side validates requests before acting, the renderer
  side validates responses before trusting them. A registry declared with
  `satisfies` keeps channel names, schemas, and handler types in step. See
  [typed-ipc-protocol.md](references/typed-ipc-protocol.md) and the
  [typed-ipc-registry.ts](../../examples/positive/typed-ipc-registry.ts)
  example.
- **Privileged commands.** A renderer asking to run a shell command, read an
  arbitrary path, or install a plugin is asking for privilege. Validate the
  arguments against an allowlist or a constrained schema, check the sender
  (`event.senderFrame`), and log the decision. Validation alone is not an
  authorization policy.
- **Protocol versioning.** Once main and renderer can be deployed or cached
  separately (auto-update, cached renderer bundles), carry a protocol version
  and reject mismatches with a clear message.
- **Native add-ons.** Load in main only, through one adapter with a clear
  failure message naming the rebuild step, pinned to the Electron ABI. See
  [native-modules-and-shutdown.md](references/native-modules-and-shutdown.md).
- **Renderer scheduling.** High-rate data from main (PTY output, logs,
  progress) is batched in main by time and size, and the renderer coalesces per
  frame. Frame-timing samplers stop when the window is hidden. The general
  material is in `browser-main-thread-performance`; the Electron specifics are
  in [renderer-scheduling.md](references/renderer-scheduling.md).
- **Shutdown.** `before-quit` aborts the root signal, stops watchers, and
  waits for children with a deadline; `window-all-closed` decides per platform;
  `will-quit` is the last chance to flush.

## Red flags

- `nodeIntegration: true` or `contextIsolation: false` on any window that
  loads remote or user-influenced content, and no migration plan where it does
  not.
- `@electron/remote` in renderer code.
- `ipcMain.handle("run", (_, command) => exec(command))` with no validation
  and no allowlist.
- A preload that exposes `ipcRenderer.invoke` generically.
- Response schemas on the renderer side but no request schemas on the main
  side.
- `instanceof` checks on errors that crossed IPC.
- A per-window channel name derived from a UUID but no check that the sender
  frame owns that window.
- Main sending every PTY chunk to the renderer as it arrives.
- A native module whose load failure crashes main with a stack trace.
- A quit path that does not kill child processes or PTYs.

## Pairing

- Pair with `typescript-boundaries-and-validation` for the schema side of
  IPC; this skill owns the privilege and process side.
- Pair with `browser-main-thread-performance` when the renderer drops frames.
- Pair with `node-bun-and-processes` for the main process's lifecycle and
  child processes.
- Pair with `typescript-errors-and-outcomes` for error serialization across
  the boundary.
