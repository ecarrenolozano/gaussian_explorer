# Report Persistence

Load during Step 6.

Create or update `sdlc_docs/01_requirements/03_user_story_product_readiness.md` using `templates/product-readiness-report.md`. Preserve prior version reviews and all decision-history rows. When direct editing is unavailable, provide exact content and insertion location.

## Current Gate

Keep Current Gate aligned with the current story version and latest event for that version. Use:

```html
<!-- product-readiness | story-version: 1.0 | review-mode: full-gate | assessment: product-ready | decision: pending -->
```

Allowed review modes: `full-gate`, `diagnostic`. Allowed assessments: `product-ready`, `changes-required`, `clarification-required`, `blocked`, `diagnostic-only`. Allowed decisions: `pending`, `approved`, `changes-requested`.

## Review Sections

Maintain one latest detailed review section per story version.

- Add a section for a newly reviewed version.
- Before approval, reassessment may replace the same version's section.
- Reassessing an approved version requires explicit user intent and resets its decision to `pending`.
- Never alter an older version's section because a newer version exists.

Record scope, overlays, story results, coverage, findings, questions, routing, technical signals, and recommendation. Put blocking and major findings first.

## Decision History

Use columns: `Story Version`, `Date`, `Actor`, `Action`, `Assessment`, `Source Batches`, `Notes`.

Allowed actions: `Assessed`, `Approved`, `Changes Requested`.

Every review appends an `Assessed` row and resets the decision for that version to `pending`. Approval and changes requests append separate rows without changing the story version.

Validate the marker, detailed section, and history row before writing. On failure, leave the existing report unchanged and explain the inconsistency.
