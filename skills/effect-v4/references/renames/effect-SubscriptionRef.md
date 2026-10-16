<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `effect/SubscriptionRef` v3 → v4

- `SubscriptionRef.SubscriptionRef` -> `SubscriptionRef.SubscriptionRef`: The
  model remains but no longer extends SynchronizedRef or Subscribable; use
  SubscriptionRef.get and SubscriptionRef.changes explicitly.
- `SubscriptionRef.SubscriptionRef.Variance` ->
  `SubscriptionRef.SubscriptionRef.Variance`: The marker remains under
  SubscriptionRef.SubscriptionRef, but its brand uses an internal type id.
- `SubscriptionRef.SubscriptionRefTypeId` ->
  `SubscriptionRef.isSubscriptionRef`: The type id is internal in v4; use the
  public runtime guard instead.
- `SubscriptionRef.SubscriptionRefUnify` -> `none`: SubscriptionRef is no
  longer an Effect subtype, so its unification helper was removed; call
  SubscriptionRef.get explicitly.
- `SubscriptionRef.SubscriptionRefUnifyIgnore` -> `none`: SubscriptionRef is no
  longer a SynchronizedRef or Effect subtype, so its unification ignore marker
  was removed.
