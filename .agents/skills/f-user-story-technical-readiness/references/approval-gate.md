# Technical Approval Gate

Load during Step 7, when approval is requested, or before repository issue publication.

The Decision History in `04_user_story_technical_readiness.md` is the technical-approval audit trail. Approval elsewhere does not satisfy this gate.

## Valid Review

Approval requires that:

- the review's story version is still the exact current product-approved version;
- the review's architecture version is still the exact current approved architecture version bound to that story version;
- no newer assessment covering an approved story ID and the same upstream versions supersedes that story's result;
- approved story IDs remain active and unchanged within the same story version;
- each approved story has status `implementation-ready`;
- each approved story is independent of non-ready blockers or has all required dependencies also approved;
- the user explicitly approves the exact story IDs for technical readiness;
- the approver name is known;
- no report inconsistency remains.

Do not infer approval from a general request to continue, review comments, partial agreement, "looks good," or silence.

## Approval Scope

- For `technical-ready`, approval may cover all reviewed stories.
- For `partially-ready`, approval may cover only the explicitly named eligible story IDs.
- `changes-required` and `blocked` cannot be approved.
- Unreviewed stories are never covered.

Append without changing upstream versions:

```text
| TR-001 | 1.0 | 1.0 | YYYY-MM-DD | Approver Name | Approved | technical-ready | US-0001, US-0002 | Approved for repository issue publication. |
```

Set the Current Gate decision to `approved` and list approved story IDs in the report. A later story version, architecture version, or upstream approval change invalidates all affected approvals. A later technical review resets only the overlapping story IDs to pending; non-overlapping approvals remain valid.

## Downstream Gate

The Current Gate summarizes the latest review. The Decision History remains authoritative for valid approvals from earlier non-overlapping review sets.

`g-create-repository-issues` may publish only story IDs that:

1. appear as `implementation-ready` in the approved review;
2. are explicitly listed in its valid approval row;
3. still belong to the exact approved story and architecture versions;
4. have no unresolved required dependency outside the approved set.

A spike candidate also requires explicit technical approval before `g` may publish it as a spike issue.

End with one chat badge:

- `**Status: GREEN / TECHNICALLY APPROVED - <story IDs> - review TR-XXX**`
- `**Status: YELLOW / TECHNICALLY READY - APPROVAL REQUIRED - review TR-XXX**`
- `**Status: YELLOW / PARTIALLY READY - APPROVAL REQUIRED FOR <eligible IDs>**`
- `**Status: RED / TECHNICAL CHANGES REQUIRED - review TR-XXX**`
- `**Status: RED / TECHNICAL REVIEW BLOCKED - <brief reason>**`
