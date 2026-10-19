<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `effect/Trie` v3 → v4

- `Trie.TypeId` -> `none`: The Trie brand is private and there is no public
  Trie runtime guard; use Trie.Trie\<V\> in type positions.
- `Trie.unsafeGet` -> `Trie.getUnsafe`: Direct word-order rename; it still
  throws for a missing key.
