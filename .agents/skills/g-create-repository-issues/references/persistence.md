# Persistence

Use sequential publication batch names such as `publication-001`.

Publication is complete only when:

1. the issue exists;
2. its identifier and URL are verified;
3. the issue contains correct lineage;
4. the local registry contains the mapping.

Never delete registry history. Update current state and append publication or reconciliation history.

When only part of a batch succeeds, record each successful issue and each failed item. Do not republish successful items during repair.
