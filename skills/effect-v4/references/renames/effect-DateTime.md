<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `effect/DateTime` v3 → v4

- `DateTime.DateTime` -> `DateTime.DateTime`: The Utc | Zoned model remains;
  epochMillis fields are now epochMilliseconds and unit/part names use
  millisecond terminology.
- `DateTime.DateTime.Input` -> `DateTime.DateTime.Input`: The input type
  remains and additionally accepts Instant and InstantWithZone objects.
- `DateTime.DateTime.Parts` -> `DateTime.DateTime.Parts`: Rename millis,
  seconds, minutes, and hours fields to millisecond, second, minute, and hour.
- `DateTime.DateTime.PartsForMath` -> `DateTime.DateTime.PartsForMath`: Rename
  the millis field to milliseconds; the other plural arithmetic fields remain.
- `DateTime.DateTime.PartsWithWeekday` -> `DateTime.DateTime.PartsWithWeekday`:
  Rename millis, seconds, minutes, and hours fields to millisecond, second,
  minute, and hour.
- `DateTime.DateTime.Proto` -> `DateTime.DateTime.Proto`: The protocol remains,
  but its marker uses the private v4 TypeId value.
- `DateTime.DateTime.UnitPlural` -> `DateTime.DateTime.UnitPlural`: Use
  milliseconds instead of millis; the other plural unit strings remain.
- `DateTime.DateTime.UnitSingular` -> `DateTime.DateTime.UnitSingular`: Use
  millisecond instead of milli; the other singular unit strings remain.
- `DateTime.TimeZone` -> `DateTime.TimeZone`: The Offset | Named model remains;
  its public type-id marker type was removed.
- `DateTime.TimeZone.Proto` -> `DateTime.TimeZone.Proto`: The protocol remains,
  but its marker uses the private v4 TimeZoneTypeId value.
- `DateTime.TimeZoneTypeId` -> `none`: The time-zone type id is private in v4.
  Use DateTime.isTimeZone, isTimeZoneOffset, or isTimeZoneNamed.
- `DateTime.TypeId` -> `none`: The DateTime type id is private in v4. Use
  DateTime.isDateTime, isUtc, or isZoned.
- `DateTime.Utc` -> `DateTime.Utc`: The model remains; rename epochMillis to
  epochMilliseconds.
- `DateTime.Zoned` -> `DateTime.Zoned`: The model remains; rename epochMillis
  and adjustedEpochMillis to epochMilliseconds and adjustedEpochMilliseconds.
- `DateTime.distance` -> `Duration.toMillis(DateTime.distance(self, other))`:
  V3 returns signed milliseconds; v4 returns a signed Duration (other minus
  self). Convert it with Duration.toMillis when a numeric millisecond result is
  required.
- `DateTime.distanceDuration` ->
  `Duration.abs(DateTime.distance(self, other))`: V4 DateTime.distance already
  returns a signed Duration. Use Duration.abs to preserve the non-negative
  distance returned by v3; Math.abs and Duration.millis expect numbers, not
  Durations.
- `DateTime.distanceDurationEither` -> `DateTime.distance + Result`: Let diff =
  DateTime.distance(self, other), a signed Duration. Use
  Duration.isPositive(diff) ? Result.succeed(Duration.abs(diff)) :
  Result.fail(Duration.abs(diff)) to preserve v3 behavior, including equal
  dates producing a failure with Duration.zero. V4 uses Result instead of
  Either.
- `DateTime.greaterThan` -> `DateTime.isGreaterThan`: The comparison was
  renamed with the is prefix.
- `DateTime.greaterThanOrEqualTo` -> `DateTime.isGreaterThanOrEqualTo`: The
  comparison was renamed with the is prefix.
- `DateTime.lessThan` -> `DateTime.isLessThan`: The comparison was renamed with
  the is prefix.
- `DateTime.lessThanOrEqualTo` -> `DateTime.isLessThanOrEqualTo`: The
  comparison was renamed with the is prefix.
- `DateTime.unsafeFromDate` -> `DateTime.fromDateUnsafe`: The unsafe suffix
  moved to the end of the constructor name.
- `DateTime.unsafeIsFuture` -> `DateTime.isFutureUnsafe`: The unsafe suffix
  moved to the end of the predicate name.
- `DateTime.unsafeIsPast` -> `DateTime.isPastUnsafe`: The unsafe suffix moved
  to the end of the predicate name.
- `DateTime.unsafeMake` -> `DateTime.makeUnsafe`: The unsafe suffix moved to
  the end of the constructor name.
- `DateTime.unsafeMakeZoned` -> `DateTime.makeZonedUnsafe`: The unsafe suffix
  moved to the end of the constructor name.
- `DateTime.unsafeNow` -> `DateTime.nowUnsafe`: The unsafe suffix moved to the
  end of the accessor name.
- `DateTime.unsafeSetZoneNamed` -> `DateTime.setZoneNamedUnsafe`: The unsafe
  suffix moved to the end of the zone setter name.
- `DateTime.zoneUnsafeMakeNamed` -> `DateTime.zoneMakeNamedUnsafe`: The unsafe
  suffix moved to the end of the named-zone constructor.
