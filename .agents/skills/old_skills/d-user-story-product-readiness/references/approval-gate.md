# Product Approval Gate

Load during Step 7, when approval is requested, or before architecture work.

The Decision History table in `03_user_story_product_readiness.md` is the product-approval audit trail. Approval elsewhere does not satisfy this gate.

For the current story version, use the latest `Assessed` row. The decision is `pending` unless a later row for the same version records `Approved` or `Changes Requested`. A newer assessment or story content version invalidates earlier approval.

Record approval only when:

- review mode is `full-gate`;
- the reviewed version is still current;
- the latest assessment is `product-ready`;
- the user explicitly approves the complete version for product readiness;
- the approver name is known;
- no artifact inconsistency remains.

Do not infer approval from partial agreement, review comments, "looks good," a request to continue, or silence.

Append without incrementing the story version:

```text
| 1.0 | YYYY-MM-DD | Approver Name | Approved | product-ready | PRDB-001 | Approved for architecture. |
```

For explicit changes requested, append a `Changes Requested` row and route findings through `references/review-rules.md`.

Architecture may proceed only when the exact current story version has a latest full-gate assessment of `product-ready` and a later valid `Approved` row, with no newer assessment or story version.

End with one chat badge:

- `**Status: GREEN / PRODUCT APPROVED - story version X.Y**`
- `**Status: YELLOW / DIAGNOSTIC ONLY - NO APPROVAL**`
- `**Status: YELLOW / PRODUCT READY - APPROVAL REQUIRED - story version X.Y**`
- `**Status: RED / CHANGES REQUIRED - story version X.Y**`
- `**Status: RED / CLARIFICATION REQUIRED - story version X.Y**`
- `**Status: RED / BLOCKED - <brief reason>**`

