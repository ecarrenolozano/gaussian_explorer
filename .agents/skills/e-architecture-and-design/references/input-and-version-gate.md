# Architecture Input and Version Gate

Load during Step 1.

## Story Version

Determine the current user-story content version from the highest `Generated` or `Revised` row in `01_user_stories.md`. Verify that:

- `Document Status` names the same version;
- every active story has a valid user-story heading and metadata comment;
- each active story has at least one traceability relationship;
- story, registry, traceability, and version state is not malformed or duplicated.

Do not rely on an `Approved` row in `01_user_stories.md` as the product gate.

## Product Approval

In `03_user_story_product_readiness.md`, require all of the following for the exact current story version:

- review mode `full-gate`;
- latest assessment `product-ready`;
- a later `Approved` decision row for the same version;
- no newer assessment or story content version;
- no contradictory Current Gate marker or history state.

If product approval is absent or stale, stop and route to `d-user-story-product-readiness`.

## Existing Architecture State

When `00_architecture_overview.md` exists, determine the current architecture content version from the highest `Generated` or `Revised` row in its Decision History. Validate:

- Current Architecture State and its marker agree with history;
- `01_story_architecture_map.md` names the same architecture and source-story versions;
- referenced component documents have valid name and lifecycle markers, and no `last-revised-version` is newer than the current architecture version;
- referenced architecture decision records exist and their document numbers are unique;
- no newer source-story version exists than the one bound to the architecture.

Do not overwrite inconsistent architecture. Report the exact repair required.

## Run Type and Version

Use `major.minor` architecture versions.

- First architecture content: `1.0`.
- Any later content change: increment the minor value by one.
- Approval does not increment the version.
- A new source-story version always requires a new architecture content version, even when changes are limited to mapping or validation.
- A reassessment without content changes keeps the version but resets its decision to `pending`.

A content change includes adding, removing, or changing architecture elements, relationships, responsibilities, mappings, interfaces, data ownership, deployment, component documents, or architecture decision references.

Record one run type: `create`, `revise`, `reassess`, or `approve`.
