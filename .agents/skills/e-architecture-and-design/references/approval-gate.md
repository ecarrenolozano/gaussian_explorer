# Architecture Approval Gate

Load during Step 8, when approval is requested, or before technical-readiness review.

The Decision History in `00_architecture_overview.md` is the architecture-approval audit trail. Approval elsewhere does not satisfy this gate.

For the current architecture version, use the latest `Generated`, `Revised`, or `Assessed` row. The decision is `pending` unless a later row for the same architecture and source-story versions records `Approved` or `Changes Requested`. A newer content version, assessment, or source-story version invalidates earlier approval.

Record approval only when:

- the current source-story version still has valid product approval;
- architecture assessment is `architecture-ready`;
- every active story is mapped and none is blocked;
- required architecture decision records are decided and can be marked `accepted`;
- no cross-file inconsistency remains;
- the user explicitly approves the complete current architecture version;
- the approver name is known.

Do not infer approval from review comments, partial agreement, "looks good," a request to continue, or silence.

On approval, update required architecture decision record statuses to `accepted`, set the Current Architecture State decision to `approved`, and append:

```text
| 1.0 | 1.0 | YYYY-MM-DD | Approver Name | Approved | architecture-ready | Approved for technical-readiness review. |
```

For explicit changes requested, append `Changes Requested`, set decision to `changes-requested`, and keep technical-readiness review blocked.

`f-user-story-technical-readiness` may proceed only when the exact current architecture version is approved and bound to the exact current product-approved story version.

End with one chat badge:

- `**Status: GREEN / ARCHITECTURE APPROVED - architecture X.Y / stories A.B**`
- `**Status: YELLOW / ARCHITECTURE READY - APPROVAL REQUIRED - architecture X.Y**`
- `**Status: RED / ARCHITECTURE CHANGES REQUIRED - architecture X.Y**`
- `**Status: RED / ARCHITECTURE BLOCKED - <brief reason>**`
- `**Status: YELLOW / DIAGNOSTIC ONLY - NO APPROVAL**`
