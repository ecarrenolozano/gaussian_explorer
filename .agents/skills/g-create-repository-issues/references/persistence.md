# Persistence

Use sequential publication batch names such as `publication-001`.

Publication is complete only when:

1. the issue exists;
2. its identifier and URL are verified;
3. the issue contains correct lineage;
4. every approved issue relationship is verified or recorded with an explicit fallback reason;
5. the local registry contains the issue mapping and relationship state.

Never delete registry history. Update current state and append publication or reconciliation history.

When only part of a batch succeeds, record each successful issue and each failed item. Do not republish successful items during repair.

Relationship publication is complete only when the platform confirms the relationship, or the registry records that the relationship was intentionally skipped because the platform could not represent it or the approved graph would violate platform constraints.
