# Input and Version Gate

Verify:

- selected repository issue exists in the registry or in an approved publication/reconciliation record;
- selected issue is canonical, not raw repository tracker intake;
- issue body or registry row contains approved lineage markers: source story or spike, story version when applicable, architecture version, technical review, and implementation-plan path or planned output location;
- source story and technical review are current and approved;
- architecture version matches the technical review;
- architecture traceability identifies relevant arc42 concerns, software system, container, component or data model, runtime or deployment concern, decisions, and mapping status;
- referenced container, component, data, and decision documents exist;
- repository revision is identified;
- no newer upstream version makes the issue or plan stale.

Stop when the issue is unlinked, approval is stale, architecture scope is contradictory, or reconciliation status is `duplicate`, `similar-existing-scope`, `new-requirement-candidate`, `out-of-scope`, `not-actionable`, `needs-human-review`, or otherwise not implementation-ready.

Route direct contributor-created tracker issues without canonical lineage to Skill G. Do not create implementation plans for raw intake, even when the issue looks actionable.
