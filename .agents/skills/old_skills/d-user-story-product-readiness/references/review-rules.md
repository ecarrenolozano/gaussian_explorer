# Product-Readiness Review Rules

Load this file during Steps 3 and 5.

## Integrity and Lineage

For every active story, confirm that:

- the heading and metadata use the same valid `US-XXXX` ID;
- lifecycle is `active` or `deprecated`;
- metadata and the visible source entry identify the same PRDB batch or batches;
- each `(Story ID, Source Batch)` relationship has exactly one traceability row;
- each referenced batch has one registry marker and one clarified handoff marked `status: processed`;
- identifiers, registry entries, relationships, and versions are not malformed or duplicated.

Determine the current story version from the highest `Generated` or `Revised` Revision History row and confirm that Document Status agrees. Approval in `01_user_stories.md` does not satisfy this gate.

Stop with `blocked` when integrity or lineage cannot be established. Route story, registry, traceability, and version defects to `c-create-user-stories`.

## Source Coverage

Read only the clarified PRDB sections referenced by active stories. Stop if a batch is missing, unprocessed, lacks a handoff, or is `Not ready`.

Classify each confirmed source outcome as:

- **represented** by active stories;
- **intentionally deferred** by documented scope or a deferred story;
- **duplicated** without distinct actor, value, or behavior;
- **contradicted** by story content;
- **missing** from the active set;
- **not story-level** and correctly retained as project context or a cross-cutting constraint.

Do not require one story per source statement. Judge whether the complete user outcome is preserved.

## Story Criteria

Use criterion statuses `satisfied`, `partial`, `missing`, `conflicting`, `unknown`, or `not applicable`.

For each story, assess:

1. **Source fidelity:** actor, capability, value, behavior, constraints, assumptions, and open questions are supported; no product rule or threshold is invented.
2. **Outcome and scope:** the user outcome is bounded, independently useful, and not split only by technical layer; exclusions and deferred behavior remain visible.
3. **Workflow behavior:** triggers, actions, end states, roles, permissions, inputs, outputs, validations, business states, and material failure outcomes are understandable where supported.
4. **Acceptance criteria:** observable Given/When/Then scenarios cover the primary outcome and supported alternatives; static constraints are measurable; criteria avoid implementation prescriptions.
5. **Uncertainty:** only handoff-recorded assumptions are carried forward; essential open questions and contradictions remain visible.
6. **Set coherence:** stories collectively cover confirmed outcomes, avoid unjustified duplication, use consistent terminology and states, and preserve evidence-based feature grouping and priority.
7. **Product qualities:** required user-visible accessibility, privacy, security, safety, compatibility, localization, reliability, support, or specialist-review outcomes are represented without demanding technical mechanisms.

## Severity

- **blocking:** prevents reliable assessment or approval.
- **major:** materially changes user behavior, scope, coverage, or acceptance.
- **moderate:** important nonblocking correction.
- **minor:** low-risk clarity, consistency, or editorial issue.

## Assessment

Assign each active story one result:

- **product-ready:** no blocking or major product finding remains;
- **changes-required:** source evidence is sufficient, but story content or traceability must change;
- **clarification-required:** a blocking or major product question is unresolved in the source handoff;
- **blocked:** artifact state prevents reliable assessment.

For a full-gate review, select the least-ready overall result in this order: `blocked`, `clarification-required`, `changes-required`, `product-ready`. Label a subset review `diagnostic-only`; it cannot be approved.

## Routing

- `changes-required` -> `c-create-user-stories`
- `clarification-required` -> `b-requirements-clarifier`, then `c-create-user-stories`
- story, registry, traceability, or version blockage -> `c-create-user-stories`
- missing or conflicting project context -> its artifact owner, then `b-requirements-clarifier` when requirements are affected
- architecture or feasibility concern without a product defect -> **Broader Technical Signals** for downstream review

Ask only the smallest decision-oriented questions needed for blocking or major findings. Identify the source batch and affected story IDs; do not conduct an extended interview.
