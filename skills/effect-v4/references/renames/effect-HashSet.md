<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `effect/HashSet` v3 → v4

- `HashSet.HashSet` -> `HashSet.HashSet`: The immutable model remains, but the
  brand is private and transient mutation helpers were removed.
- `HashSet.TypeId` -> `HashSet.isHashSet`: The brand is private; use
  HashSet.isHashSet for runtime refinement and HashSet.HashSet\<A\> in type
  positions.
- `HashSet.beginMutation` -> `none`: Transient mutation mode was removed;
  reassign immutable add/remove results or build a batch with
  HashSet.fromIterable.
- `HashSet.endMutation` -> `none`: There is no mutation window to finalize;
  remove this call and use the latest immutable HashSet value.
- `HashSet.flatMap` -> `HashSet.fromIterable + Iterable.flatMap`: Preserve set
  deduplication with HashSet.fromIterable(Iterable.flatMap(self, f)); no direct
  flatMap remains.
- `HashSet.forEach` -> `Iterable.forEach`: HashSet remains Iterable, so
  Iterable.forEach(self, f) preserves eager side-effecting traversal.
- `HashSet.mutate` -> `none`: Transient mutation was removed; reassign
  immutable HashSet.add/remove results or build a complete replacement with
  HashSet.fromIterable.
- `HashSet.partition` -> `HashSet.filter`: Build [excluded, satisfying] with
  complementary HashSet.filter calls, or use one reduction when the predicate
  is expensive.
- `HashSet.toValues` -> `Array.from`: HashSet remains iterable;
  Array.from(self) produces the former Array result.
- `HashSet.toggle` -> `HashSet.has + HashSet.remove / HashSet.add`: Use
  HashSet.has(self, value) ? HashSet.remove(self, value) : HashSet.add(self,
  value).
- `HashSet.values` -> `none`: The HashSet itself is iterable; iterate it
  directly or call self[Symbol.iterator]() when an iterator object is required.
