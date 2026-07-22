# Version-Specific Approval Gate

Load this file during Step 8, when approval is requested, or before any downstream planning task.

## Source of Truth

The **Revision History** table in `01_user_stories.md` is the approval audit trail. Do not store approval in YAML frontmatter.

Use these columns exactly:

- Version
- Date
- Author
- Action
- Source Batches
- Notes

Allowed actions are `Generated`, `Revised`, and `Approved`.

## Current Status

The current version is the highest content version recorded by a `Generated` or `Revised` row.

That version is approved only when:

1. a later row explicitly records `Approved` for the same version; and
2. no higher content version exists.

Any generated or revised content creates a new Draft version. Approval of an earlier version never applies to later content.

Keep the **Document Status** section aligned with the revision history:

- `Status: Draft` after generation or revision;
- `Status: Approved` after valid approval of the current version.

## Recording Approval

Record approval only when all conditions are met:

- the user explicitly approves the complete current user-story version;
- the version is identified or unambiguously current;
- the approver name is known;
- no inconsistent story, registry, traceability, or revision state remains.

Do not interpret review comments, approval of one story, "looks good", requests to continue, or silence as formal approval.

If the approver name is unknown, request it before recording approval.

Approval adds a row for the same version and does not increment it:

```text
| 1.0 | YYYY-MM-DD | Approver Name | Approved | PRDB-001 | Approved for downstream planning. |
```

Update **Document Status** to `Approved` only after the row is added successfully.

## Downstream Gate

Before generating repository issues, architecture, implementation plans, test plans, or code:

1. identify the current user-story version;
2. verify that version-specific approval exists;
3. block the downstream task when approval is absent, stale, or inconsistent.

Do not treat story generation itself as approval.

## Chat Status

End generation, revision, approval, or downstream-gate checks with one prominent chat badge:

- `**Status: GREEN / APPROVED - version X.Y**`
- `**Status: YELLOW / DRAFT - APPROVAL REQUIRED - version X.Y**`
- `**Status: RED / BLOCKED - <brief reason>**`

The badge summarizes file state; it does not replace the Revision History entry.
