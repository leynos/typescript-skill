# Native modules and shutdown

## Native add-ons

- Load in the main process only. A renderer with `nodeIntegration: false`
  cannot load them, and a renderer that can is the problem the migration fixes.
- One adapter module per add-on. It `require`s the module inside a `try`,
  converts a load failure into an error whose message names the rebuild command
  (`electron-rebuild`, the project's `make rebuild-native`) and the Electron
  version, validates results, and exposes a typed interface. Nothing else
  imports the add-on.
- Pin the Electron ABI. Native modules are compiled against Electron's Node
  headers, not the system Node's; a mismatch fails at load. The rebuild step
  runs in `postinstall` and in CI for each target platform.
- Prefer N-API (`node-addon-api`) modules; they survive Electron upgrades
  without a rebuild more often than NAN or raw V8 modules.
- Optional add-ons (platform-specific registry access, for example) are
  optional dependencies with a feature flag the adapter reports, so the
  application degrades rather than crashes.
- `asarUnpack` the `.node` files; they cannot be loaded from inside an archive.

## PTYs and long-lived children

A terminal emulator's PTY is a native child that outlives any one IPC call.

- Own each PTY in a session object with a scope; the session is created by a
  validated IPC request and destroyed on window close, explicit close, or
  application quit.
- Batch output in main by time and size (16 ms or 200 KiB) before sending to
  the renderer, with a `StringDecoder` reset before each emit for re-entrancy.
- Kill the child in `destroy()`, and call `destroy()` from `before-quit` for
  every live session. An orphaned shell after quit is a defect users notice.
- A shell that exits immediately with a non-zero code is a configuration
  problem; fall back to a default shell once and report, rather than looping.

## Shutdown sequence

```ts
app.on("before-quit", (event) => {
  if (!shuttingDown) {
    shuttingDown = true;
    event.preventDefault();
    void shutdown().finally(() => app.quit());
  }
});

async function shutdown(): Promise<void> {
  root.abort(new ShutdownSignal("quit"));
  for (const session of sessions.values()) session.destroy();
  await Promise.allSettled([configWatcher.close(), pluginHost.stop()]);
  await flushLogs();
}
```

- `before-quit` runs once; the flag prevents re-entry when `app.quit()` is
  called again at the end.
- `window-all-closed` quits on Windows and Linux and stays alive on macOS by
  convention; make it a stated decision.
- `will-quit` is for the final synchronous flush; nothing async completes
  after it.
- Renderer windows get a `shutdown` event so they can stop samplers and
  persist state before `close`.

## Crash and relaunch

- `child-process-gone` and `render-process-gone` events are logged with the
  reason and, for renderers, trigger a reload with a backoff and a cap.
- A crashed GPU process disables WebGL for the session; the terminal renderer
  falls back to canvas on `onContextLoss` rather than going blank.
