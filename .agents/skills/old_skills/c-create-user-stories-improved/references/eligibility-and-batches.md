# Eligibility and Batch Selection

Load this file only during Step 2.

## Batch Boundaries

Treat a Markdown heading whose text begins with an ISO date (`YYYY-MM-DD`) as a requirement-batch heading. The batch continues until the next dated heading of the same or higher level.

A valid clarified batch has one unique marker immediately below its heading:

```html
<!-- batch-id: PRDB-001 | status: processed | date: YYYY-MM-DD -->
```

It must also contain one **Clarified Requirements Handoff** and exactly one selected readiness status.

## Eligibility

A batch is eligible only when all applicable conditions hold:

1. The batch marker is well formed and has `status: processed`.
2. The `PRDB-XXX` identifier is unique.
3. A clarified handoff is present.
4. Readiness is not `Not ready`.
5. A `Ready` batch may proceed normally.
6. A `Partially ready` batch may proceed only when its downstream notes state that user-story generation may proceed, or the user explicitly requests generation from that batch.
7. The source-batch registry in `01_user_stories.md` does not already mark it as generated.

`status: processed` means clarification exists; it does not mean the batch is approved or automatically eligible.

## Readiness Behavior

- **Ready:** Generate all supported candidate outcomes.
- **Partially ready:** Generate only outcomes whose actor, core behavior, value, and scope are supported. Carry explicit non-blocking assumptions as labeled details. Preserve open questions. Defer outcomes whose core behavior or acceptance boundary depends on unresolved information.
- **Not ready:** Do not generate stories. Report the blocking gaps and route the batch to `b-requirements-clarifier`.

## Detect Prior Generation

Use this registry marker in `01_user_stories.md`:

```html
<!-- story-batch: PRDB-001 | status: generated | story-ids: US-0001,US-0002 | document-version: 1.0 -->
```

For legacy files without a registry, treat a batch as previously generated only when its identifier appears consistently in story metadata and the traceability matrix. If those sources disagree, stop and report the inconsistency.

Skip previously generated batches unless the user explicitly requests an update.

## Selection

1. Process a batch explicitly selected by the user.
2. Otherwise process the earliest eligible batch in document order.
3. Process one batch by default.
4. Keep unrelated batches separate.

If no eligible batch exists, report why each candidate was skipped. Do not generate from raw or unclarified content.

## Explicit Update Mode

When the user explicitly requests updates for a previously generated batch:

- compare the revised handoff with stories already mapped to that batch;
- preserve identifiers for materially unchanged outcomes;
- assign new identifiers only to new outcomes;
- mark invalidated stories as `deprecated`; never delete or reuse their identifiers;
- update story metadata, registry, traceability, version, and approval status together.

Do not enter update mode implicitly.

## Invalid State

Stop on missing handoffs, duplicate or malformed batch markers, multiple readiness selections, partial duplicate registries, missing registered stories, missing traceability rows, or conflicting canonical evidence. Identify the exact batch and correction required.
