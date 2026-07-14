# Technical-Readiness Report Persistence

Load during Step 6.

Create or update `sdlc_docs/01_requirements/04_user_story_technical_readiness.md` using `templates/technical-readiness-report.md`. Preserve every prior review and decision-history row. When direct editing is unavailable, provide exact content and insertion location.

## Review Identifier

Use sequential identifiers `TR-XXX`.

- Scan existing review IDs and increment the highest number.
- Start at `TR-001`.
- Never reuse or renumber an identifier.
- Every new assessment receives a new review ID, including reassessment of the same versions and story set.

## Current Gate Marker

Maintain:

```html
<!-- technical-readiness | review-id: TR-001 | story-version: 1.0 | architecture-version: 1.0 | review-mode: full-gate | assessment: technical-ready | decision: pending -->
```

Allowed review modes: `full-gate`, `selected`.
Allowed assessments: `technical-ready`, `partially-ready`, `changes-required`, `blocked`.
Allowed decisions: `pending`, `approved`, `changes-requested`.

## Review Sections

Append one immutable detailed section per review ID. Record:

- exact story and architecture versions;
- review mode and reviewed story IDs;
- available technical evidence;
- per-story status, confidence, severity, architecture references, dependencies, findings, verification needs, route, and publication eligibility;
- cross-story dependencies and sequencing;
- architecture, story, requirement, external, and artifact-state findings;
- spike candidates;
- eligible story IDs;
- recommendation.

Put blocking and major findings first. Do not overwrite an earlier review; a new assessment uses a new review ID.

## Decision History

Use columns:

`Review ID`, `Story Version`, `Architecture Version`, `Date`, `Actor`, `Action`, `Assessment`, `Story IDs`, `Notes`.

Allowed actions: `Assessed`, `Approved`, `Changes Requested`.

Every review appends `Assessed` and sets the reviewed story IDs to `pending`. Approval and changes requests append separate rows using the same review ID. For an approval row, `Story IDs` must list the exact approved implementation-ready stories. A later review supersedes prior technical decisions only for overlapping story IDs; non-overlapping approvals remain valid while upstream versions remain unchanged.

## Validation

Before writing, confirm that:

- the review ID is unique;
- upstream versions and approvals are valid;
- every reviewed story has exactly one primary status;
- every architecture reference exists;
- every eligible story is `implementation-ready` and independent of non-ready blockers;
- routes name the correct owning stage;
- spike candidates satisfy `references/spike-rules.md`;
- the Current Gate marker, latest section, and history agree;
- no upstream artifact was modified.

On failure, leave the existing report unchanged and explain the inconsistency.
