# Solution Assumptions and Decision Items

Load during Step 4 and whenever the source names a framework, library, architecture, storage mechanism, API, database, or deployment platform.

## Decision Audit

For each solution proposal, record:

1. the exact proposal;
2. who proposed it;
3. its status: `approved constraint`, `preference`, `assumption`, `candidate`, or `rejected`;
4. the user or project need it is intended to satisfy;
5. the alternatives that remain open, when known;
6. the criteria needed to decide;
7. whether the decision blocks story generation.

A professor, stakeholder, or requester naming a technology does not automatically make it the best or approved choice.

## When to Create a Decision Item

Create a decision item when:

- the source prescribes a solution without an approved rationale;
- multiple realistic options exist and the choice affects UX, deployment, maintenance, or extensibility;
- later requirements expose a mismatch between the assumed solution and desired behavior;
- a quality attribute cannot be accepted without selecting or validating a technical approach.

Do not create a user story such as “As a developer, I need to compare Streamlit and Panel.” That is a discovery or architecture decision, not user value.

## Decision Criteria

Use evidence-supported criteria. Typical criteria for a scientific interactive application may include:

- dynamic conditional controls;
- reactive state and explicit fit behavior;
- Plotly or visualization interoperability;
- file upload and download support;
- model persistence and inference workflows;
- deployment environment and authentication needs;
- responsiveness for expected dataset sizes;
- testing, modularity, maintainability, and extension cost;
- accessibility and usability for researchers;
- project team familiarity and operational support.

These are prompts. Include only relevant supported criteria.

## Example

```markdown
## DI-0001 - Evaluate the application framework

- Source batch: `PRDB-001`
- Trigger: The request proposes Streamlit, but the framework has not been approved through an options assessment.
- Status: `Open`
- Decision required: Select the framework for the interactive scientific application.
- Candidate options: Streamlit, Panel, or another supported Python web framework.
- Decision criteria:
  - dynamic kernel-specific controls;
  - reliable Plotly interaction and state preservation;
  - model fitting and inference state management;
  - downloadable result and model artifacts;
  - maintainability and deployment fit.
- Blocking effect: Does not block user-outcome stories, but blocks implementation planning.
- Expected output: Approved decision or ADR with rationale.
```
