# Clarified Handoff Rules

Load this file only during Step 5.

## 1. Select the Requirement Batch

Treat a Markdown heading whose text begins with an ISO date (`YYYY-MM-DD`) as a batch heading. The batch continues until the next dated heading of the same or higher level.

Before processing:

1. Check for a batch-status comment immediately below the heading.
2. Skip a batch marked `status: processed` unless the user explicitly requests reassessment.
3. Process the user-selected batch. If none is selected, process the earliest unprocessed batch in document order.
4. Process one batch unless the user requests multiple batches.
5. Keep unrelated batches separate.

If an identifiable requirement has no ISO-dated heading, clarify it but do not invent a date or mark it processed. Provide the proposed handoff and state that a dated heading is required before inserting a status marker.

If date boundaries, status tags, or identifiers are malformed or duplicated, report the issue and do not modify the affected batch until the ambiguity is resolved.

If an unprocessed batch already contains a partial handoff, update that handoff instead of appending a duplicate.

### Reassessment

On explicit reassessment, preserve the original requester input and existing batch identifier, replace the prior handoff, and keep one status marker. Assign a new identifier only when requester input is recorded as a new dated batch.

## 2. Assign the Batch Identifier

Use `PRDB-XXX`, where `PRDB` means Product Requirement Document Batch and `XXX` is a three-digit sequence.

Scan all existing `batch-id` tags and increment the highest numeric value. Use `PRDB-001` when none exist. Never reuse or silently renumber identifiers; preserve gaps.

Flag malformed or duplicate identifiers instead of guessing.

## 3. Write the Handoff

Append the handoff beneath the original content of the selected batch. Keep the original requester input unchanged.

Use only:

- The original batch
- The canonical project context
- Confirmed user responses
- Recorded interpretations and unresolved items from Steps 2-4

Follow `templates/handoff.md`:

- Include every required section.
- Include optional sections only when supported content exists.
- Omit empty optional sections.
- Do not add content merely to complete the template.

Map states consistently:

- Verified behavior -> **Confirmed Requirements**
- User-confirmed choices -> **Clarified Decisions**
- Necessary but unconfirmed interpretations -> **Explicit Assumptions**
- Unresolved ambiguities, contradictions, and missing decisions -> **Open Questions**
- Exclusions and possible expansion -> **Scope Boundaries**
- Unresolved impact, feasibility, or dependency concerns -> **Risks and Uncertainties**

Under **Notes for Downstream User-Story Generation**, state what is confirmed, which assumptions remain, which questions affect backlog quality, and whether generation should proceed.

## 4. Assign Readiness

Apply `references/readiness.md`. Select exactly one status and record all criterion scores, the overall average, and blocking issues in the handoff.

## 5. Mark the Batch as Processed

After the handoff and readiness assessment are complete, insert this comment immediately below the batch heading:

```html
<!-- batch-id: PRDB-001 | status: processed | date: YYYY-MM-DD -->
```

Use the assigned identifier and batch date. Add the marker only after the handoff exists, readiness is selected, and all known unresolved items are preserved.

`status: processed` means a clarification handoff exists; it does not mean the requirement is ready or approved.

Do not mark a batch as processed when the handoff could not be produced.

## 6. Update or Propose the File Change

When file editing is available and modification is part of the task, update `00_raw_ideas.md` directly. Otherwise provide:

1. The exact status comment
2. The complete handoff
3. The precise insertion location

Never claim a file was updated unless the change completed successfully.

## 7. Verify

Before finishing, confirm that:

- The original requester input is unchanged.
- The handoff belongs to the correct batch.
- The identifier is unique.
- Requirement states remain distinct.
- Unresolved questions remain visible.
- Exactly one readiness status is selected.
- Readiness scores support that status.
- No unsupported requirements or downstream artifacts were introduced.
