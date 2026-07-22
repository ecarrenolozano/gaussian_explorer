# Persistence and Traceability

Load this file only during Step 7.

## Output Files

Update these files as one consistent change:

- `sdlc_docs/01_requirements/01_user_stories.md`
- `sdlc_docs/01_requirements/02_traceability_matrix.md`
- `sdlc_docs/01_requirements/03_decision_backlog.md`
- `sdlc_docs/01_requirements/04_requirement_coverage.md`

If a file is missing, create it from its template. If it exists, preserve its content and add only the sections or entries required by this skill.

When direct file editing is unavailable, provide the exact content, insertion locations, version, registry markers, traceability rows, and revision row. Do not claim the files were updated.

## Document Version

Use `major.minor` versions.

- Use `1.0` for the first generated content.
- For each later content change, increment the minor number by one: `1.0` to `1.1`, `1.9` to `1.10`.
- Process all batches selected in one run under one new content version.
- Approval does not increment the version.

A content change includes adding, revising, deprecating, regrouping, reprioritizing, or adding source lineage to a story.

Set the current document status to `Draft` whenever content changes. A prior approval does not apply to the new version.

## User-Story File Structure

When creating the file, use `templates/user-stories-file.md`.

When updating an existing file:

- preserve existing stories and headings;
- add missing priority, open-question, registry, or revision sections without rewriting unrelated content;
- place each active story under its priority and feature group;
- append new stories in identifier order within the relevant feature;
- do not move an existing story unless its priority or feature is explicitly revised;
- do not delete stories; use `lifecycle: deprecated` for an explicitly invalidated outcome.

Use `templates/agile-user-story-template.md` for each new story. Remove instructional placeholders and empty optional lines.

## Story Metadata

Place one machine-readable comment immediately below each story heading:

```html
<!-- story-id: US-0001 | source-batch: PRDB-001 | priority: MVP | lifecycle: active -->
```

Keep the visible **Source batch** entry aligned with the metadata. When an existing story gains another source, add the batch to both places without changing the story identifier.

## Traceability Matrix

When creating the file, use `templates/traceability-matrix.md`.

Maintain one row per `(Story ID, Source Batch)` relationship. Use these columns exactly:

- Story ID
- Source Batch
- Source Requirement or Decision
- Feature
- Priority
- Lifecycle
- Document Version

Preserve existing rows. Append only missing relationships. Update a row only when the corresponding story is explicitly revised.

For **Source Requirement or Decision**, use a concise evidence-based phrase from the clarified handoff. Do not copy an entire handoff section.

## Open Questions

Append unresolved questions that materially affect generated stories under **Open Questions**, grouped by source batch. Do not duplicate questions already present.

A story whose core behavior depends on an unresolved question must not be persisted.

## Source Batch Registry

After all story content and traceability rows for a batch are complete, add one marker under **Source Batch Registry**:

```html
<!-- story-batch: PRDB-001 | status: generated | story-ids: US-0001,US-0002 | document-version: 1.0 -->
```

List identifiers in ascending order without spaces. For a batch that only maps to existing stories, list those existing identifiers.

Do not add the marker when story content, traceability, or revision history is incomplete.

## Revision History

Append one row for the new content version:

```text
| 1.0 | YYYY-MM-DD | ChatGPT | Generated | PRDB-001 | Initial user stories; status reset to Draft. |
```

Use action `Generated` for the first content version and `Revised` for later content changes. List every source batch changed in the run. Use a supplied author name instead of `ChatGPT` when appropriate.

## Safe Update Procedure

When file editing tools permit:

1. prepare both updated files in temporary copies;
2. validate identifiers, registry markers, sections, table columns, version, and cross-file mappings;
3. replace the originals only after both copies pass validation.

If a consistent two-file update cannot be completed, leave the originals unchanged and report the failure.

## Verification

Before finishing, confirm that:

- every active story has one valid identifier and metadata comment;
- every story traces to at least one eligible batch;
- every `(Story ID, Source Batch)` relationship has one matrix row;
- every selected batch has one registry marker with the correct story IDs and version;
- no duplicate identifiers, relationships, or registry entries exist;
- the current version and Draft status are correct;
- one revision row records the content change;
- unresolved questions remain visible;
- no unsupported or implementation-specific content was added.


## Decision Backlog

Maintain stable `DI-XXXX` identifiers. Preserve resolved decisions and their rationale. A decision item may block implementation planning without blocking user-story generation.

## Requirement Coverage

Maintain one row per meaningful source statement. Use stable `RC-XXXX` identifiers. A row must identify the statement classification, disposition, linked artifact, and status. Coverage may point to a story, decision item, NFR section, open question, exclusion, or existing artifact.

Do not mark a batch complete while meaningful source statements remain unclassified or uncovered.
