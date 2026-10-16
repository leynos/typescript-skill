<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `effect/Resource` v3 → v4

- `Resource.Resource` -> `Resource.Resource`: The type remains but no longer
  extends Effect; use Resource.get(resource).
- `Resource.Resource.Variance` -> `none`: The exported variance artifact was
  removed.
- `Resource.ResourceTypeId` -> `Resource.isResource`: The marker is private;
  use the public runtime guard.
- `Resource.ResourceUnify` -> `none`: Resource no longer extends Effect; use
  Resource.get explicitly.
- `Resource.ResourceUnifyIgnore` -> `none`: The Effect-unification
  implementation detail was removed.
