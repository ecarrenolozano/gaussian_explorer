# Reconciliation

Classify tracker issues and registry rows without treating repository-originated issues as automatically implementation-ready.

## Registry and Canonical Issue Classes

- `linked`: tracker issue and registry agree.
- `missing-from-registry`: tracker issue appears valid but has no registry row.
- `missing-repository-lineage`: tracker issue lacks required source lineage.
- `candidate-match`: possible match; needs human confirmation before binding.
- `unlinked`: no approved source found.
- `duplicate`: multiple issues represent the same approved source.
- `diverged`: scope or acceptance differs from approved documentation.

## Contributor Intake Classes

- `canonical-linked`: issue already has valid lineage markers and maps to approved documentation.
- `duplicate`: same scope as an existing canonical issue or approved story; propose canonical link and closure.
- `similar-existing-scope`: related to approved scope but not an independent requirement; propose link to canonical issue or story and preserve useful notes.
- `bug`: defect against implemented approved behavior. Link to story, plan, implementation artifact, and tests when known.
- `new-requirement-candidate`: distinct product behavior not covered by approved scope; route to Skill B / raw requirements intake.
- `out-of-scope`: outside current project or approved product boundary.
- `not-actionable`: lacks enough information and no useful clarification path is available.
- `needs-human-review`: ambiguity remains after inspection; do not mutate or promote without reviewer decision.

## Clustering Rules

For large issue sets, create one reconciliation batch and cluster issues before routing. Compare:

- source and lineage markers;
- titles, bodies, labels, linked PRs, and comments when available;
- acceptance behavior and user-visible outcome;
- matching story IDs, architecture elements, and implementation-plan paths;
- known duplicates and prior reconciliation decisions.

Do not create one SDLC branch or implementation plan per raw tracker issue. Bulk intake should usually produce one reconciliation batch, a smaller set of promoted candidates, and links or closures for the rest.

## Routing Rules

Do not bind a candidate match without human confirmation. Route new product behavior to Skill B, story defects to Skills C and D, architecture changes to Skill E, technical investigations to Skill F, and planning-only tasks to Skill H.

Confirmed bugs against already implemented approved behavior may remain as tracker issues with bug labels. If a bug changes expected behavior, route it as a requirement candidate instead of planning it directly.

Operational changes such as labels, assignees, comments, or open and closed state may update the registry. Scope or acceptance changes require upstream review.

## Tracker Action Rules

Before writing to the tracker, show the exact proposed action:

- labels to add or remove;
- comments to post;
- issue bodies to update;
- issues to close or reopen;
- canonical issue, story, or plan links to add.

After approved writes, verify affected issues and record the reconciliation batch, class, canonical target, action, and last reconciled date in the registry or reconciliation index.
