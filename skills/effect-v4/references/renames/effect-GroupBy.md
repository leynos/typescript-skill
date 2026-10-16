<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `effect/GroupBy` v3 → v4

- `GroupBy.GroupBy` -> `Stream<readonly [K, Stream<V>]>`: The GroupBy datatype
  is removed in v4; Stream.groupBy/groupByKey now return an ordinary Stream of
  readonly [key, substream] pairs, processed with regular Stream operators.
- `GroupBy.GroupBy.Variance` -> `none`: Variance plumbing for the removed
  GroupBy datatype; v4 has no GroupBy type, so there is no variance interface
  to migrate to.
- `GroupBy.GroupByTypeId` -> `none`: Brand symbol for the removed GroupBy
  datatype; v4 groupBy results are plain Streams, discriminated with
  Stream.isStream if needed.
- `GroupBy.filter` -> `Stream.filter`: Filter the groups by key with an
  ordinary Stream.filter on the pairs: Stream.filter(([key]) =\>
  predicate(key)).
- `GroupBy.first` -> `Stream.take`: Keep only the first n groups with an
  ordinary Stream.take(n) on the [key, stream] pair stream.
- `GroupBy.make` -> `none`: No wrapper to construct in v4: a grouped stream is
  just any Stream\<readonly [K, Stream\<V\>]\>, so build the pair stream
  directly (Stream.groupBy/groupByKey produce it); the v3 shape Stream\<[K,
  Dequeue\<Take\<V, E\>\>]\> is gone along with the queue-of-Take encoding.
