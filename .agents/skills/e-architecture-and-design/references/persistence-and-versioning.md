# Architecture Persistence and Versioning

Load during Step 7.

## Current State Marker

Maintain this marker in `00_architecture_overview.md`:

```html
<!-- architecture-state | architecture-version: 1.0 | source-story-version: 1.0 | assessment: architecture-ready | decision: pending -->
```

Allowed assessments: `architecture-ready`, `changes-required`, `blocked`, `diagnostic-only`.
Allowed decisions: `pending`, `approved`, `changes-requested`.

- `architecture-ready`: the package is coherent, every active story is mapped, and no consequential architecture decision blocks technical review.
- `changes-required`: authoritative inputs are sufficient, but the current architecture package needs correction and was not fully repaired in this run.
- `blocked`: missing, stale, conflicting, or undecided evidence prevents a responsible architecture.
- `diagnostic-only`: the review covered less than the complete current architecture package.

A normal create or revise run sets decision to `pending`. A diagnostic assessment cannot be approved.

## Architecture Package

Use one architecture version across all files changed in a run. Create files from these templates when absent:

- `templates/architecture-overview.md`
- `templates/story-architecture-map.md`
- `templates/component-architecture.md`
- `templates/architecture-decision.md`

Preserve unchanged files and prior history. Do not create empty component or architecture-decision directories.

For every component document, include a marker naming the clear component name, introduced version, last-revised version, last-revised source-story version, and lifecycle. Update that marker only when the component content changes; preserve unchanged component documents. Keep the story map marker aligned with the overview marker.

## Story Mapping

Map every active story in the approved source version. Use one row per story with status:

- `mapped`: responsibilities and architecture path are clear;
- `mapped-with-assumption`: a bounded, explicit technical assumption remains;
- `blocked`: no responsible architecture path can be established without an upstream or consequential technical decision.

Architecture cannot be assessed `architecture-ready` while any active story is `blocked`.

## Decision History

Use columns:

`Architecture Version`, `Source Story Version`, `Date`, `Actor`, `Action`, `Assessment`, `Notes`.

Allowed actions: `Generated`, `Revised`, `Assessed`, `Approved`, `Changes Requested`.

- Content creation appends `Generated`.
- Content change appends `Revised`.
- Review without content change appends `Assessed` and resets decision to `pending`.
- Approval and changes requests append separate rows without incrementing the version.

The current architecture version is the highest `Generated` or `Revised` version. For that version, use the latest `Generated`, `Revised`, or `Assessed` row as the current assessment. A later valid `Approved` row establishes approval.

## Safe Update Procedure

When direct editing is available:

1. prepare all affected files in temporary copies;
2. validate markers, versions, names, mappings, architecture decision references, links, and history;
3. verify every active story is mapped exactly once;
4. replace originals only after the full package passes validation.

If a consistent update cannot be completed, leave existing architecture unchanged and report the failure. When direct editing is unavailable, provide exact files or insertions and do not claim persistence.

## Final Validation

Confirm that:

- product approval is valid for the source-story version;
- every active story has one mapping row;
- every referenced architecture area, component document, and architecture decision record exists;
- overview and story map use the same current version binding, and referenced component revisions are not newer than it;
- important interfaces identify provider, consumer, purpose, and material failure behavior;
- important data has an owner and lifecycle;
- selected quality attributes have architectural support;
- every required selected view is present as editable Mermaid in a canonical Markdown file;
- every referenced supplementary modeling artifact has a documented role, path, and validation status and does not conflict with the canonical package;
- no product behavior or unsupported threshold was invented;
- no class, method, module, task, or issue design was added;
- the assessment and decision marker agrees with history.
