<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/ai/Chat` v3 → v4

- `Chat.Chat` -> `Chat.Chat`: Use the Chat interface for implementations and
  the Context.Service value as the service key; it is no longer a class.
  Chat.empty and Chat.fromPrompt construct branded chat sessions.
- `Chat.Service` -> `Chat.Chat`: Service was renamed to Chat. Implementations
  require [Chat.TypeId]: Chat.TypeId; use Chat.empty or Chat.fromPrompt to
  create a session.
