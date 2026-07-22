# Technical Approval Gate

Human approval applies only to named story IDs in one technical review and to the exact story and architecture versions recorded there.

Approve only when:

- each approved story is `implementation-ready`;
- product and architecture approvals remain valid;
- no newer overlapping review supersedes the result;
- the approver is known and explicitly approves the reviewed set.

A newer story version, architecture version, invalidated upstream approval, or newer overlapping review makes affected approval stale.
