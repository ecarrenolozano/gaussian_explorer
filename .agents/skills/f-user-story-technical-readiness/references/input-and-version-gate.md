# Technical-Readiness Input and Version Gate

Load during Step 1.

## Current Story Version

Determine the current story content version from the highest `Generated` or `Revised` row in `01_user_stories.md`. Verify active story IDs, metadata, registry markers, traceability, Document Status, and revision history are consistent.

## Product Approval

For the exact current story version, require in `03_user_story_product_readiness.md`:

- review mode `full-gate`;
- latest assessment `product-ready`;
- a later `Approved` row for the same version;
- no newer assessment or content version;
- Current Gate and history agreement.

Approval recorded only in `01_user_stories.md` does not satisfy this gate.

## Architecture Approval

Determine the current architecture content version from the highest `Generated` or `Revised` row in `00_architecture_overview.md`. Require:

- source-story version equal to the exact current story version;
- latest architecture assessment `architecture-ready`;
- a later `Approved` row for the same architecture and story versions;
- no newer architecture content, assessment, or story version;
- Current Architecture State and Decision History agreement;
- `01_story_architecture_map.md` bound to the same versions;
- every reviewed active story mapped with status `mapped` or `mapped-with-assumption`;
- referenced component documents and ADRs present and identifiers unique.

Stop and route to `e-architecture-and-design` when architecture approval or mapping is absent, stale, or contradictory.

## Repository and Environment Evidence

Use only relevant, available evidence such as existing code boundaries, interface definitions, schemas, deployment configuration, supported environments, coding standards, test infrastructure, or team conventions.

Label evidence source and freshness. Do not assume planned architecture has already been implemented. When current code conflicts with approved architecture, record the mismatch and route according to impact.

## State Failures

Use `blocked-state` when exact upstream versions, approvals, active stories, mappings, or identifiers cannot be established. Do not modify inconsistent upstream files.

A blocked-state report may be written only when a unique story version and review scope can still be identified. Otherwise report the blockage in chat without creating ambiguous approval metadata.
