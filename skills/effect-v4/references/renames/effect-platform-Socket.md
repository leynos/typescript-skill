<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/platform/Socket` v3 → v4

- `Socket.CloseEventTypeId` -> `Socket.CloseEvent`: The close-event marker is
  internal in v4; use the CloseEvent class or Socket.isCloseEvent.
- `Socket.SocketError` -> `Socket.SocketError`: The old union became a tagged
  wrapper around SocketReadError, SocketWriteError, SocketOpenError, or
  SocketCloseError.
- `Socket.SocketErrorTypeId` -> `Socket.SocketErrorTypeId`: The error marker
  remains in effect/socket/Socket.
- `Socket.SocketGenericError` ->
  `Socket.SocketReadError | Socket.SocketWriteError | Socket.SocketOpenError`:
  The generic reason discriminator was replaced by dedicated read, write, and
  open error classes.
- `Socket.TypeId` -> `typeof Socket.TypeId`: The socket marker remains
  exported, but the separate type alias was removed.
- `Socket.WebSocket` -> `Socket.WebSocket`: The opaque service moved to
  effect/socket/Socket and is now a Context.Service class for
  globalThis.WebSocket.
- `Socket.WebSocketConstructor` -> `Socket.WebSocketConstructor`: The service
  moved to effect/socket/Socket and is now a Context.Service class.
- `Socket.currentSendQueueCapacity` -> `none`: The send queue was removed. The
  v4 Socket is pull-based: acquire socket.reader in a scope and pull frame
  batches; writes apply the transport's native backpressure.
- `Socket.defaultCloseCodeIsError` -> `none`: Sockets no longer classify close
  codes; every close fails the reader's pull with a SocketError wrapping
  SocketCloseError. Consumers that treat a close as normal catch the error.
- `Socket.fromTransformStream` -> `Socket.fromTransformStream`: The constructor
  remains in effect/socket/Socket but drops closeCodeIsError; every close fails
  the reader's pull with a SocketError wrapping SocketCloseError.
- `Socket.layerWebSocket` -> `Socket.layerWebSocket`: The constructor remains
  in effect/socket/Socket; its URL may now also be an Effect.
- `Socket.toChannelMap` -> `none`: The v4 Socket read side is an Effect that
  never completes via Cause.Done; map frames by acquiring Socket.readerBytes or
  Socket.readerString, or Effect.map the reader from socket.reader, and use
  Socket.toChannel or Socket.toChannelString for duplex channels.
