---
name: workflow-project-development
description: guide a developer or scientist through the repository-based software development workflow by starting or resuming a project, inspecting existing sdlc_docs state, identifying completed, blocked, stale, and eligible stages, and delegating the selected stage to the existing sibling skills from a-project-context-interpretation through k-deployment-preparation. Use when the user asks to start, resume, continue, inspect, navigate, repair, or explain the project workflow, or asks what to do next.
---

# Project Development Workflow

## Purpose

Provide one guided interface over the existing specialist skills. Inspect the repository, explain the current state in plain language, select the next valid stage, and reuse the corresponding sibling skill without duplicating its workflow.

Support users with basic software-development knowledge. Explain unfamiliar terms briefly and ask focused questions only when a decision or missing input blocks progress.

## Governing Rules

- Reuse the sibling specialist skills; do not reproduce or replace their detailed instructions.
- Load only the selected specialist skill and the references it explicitly requires.
- Treat canonical repository artifacts as workflow state. Do not rely on conversational memory alone.
- Verify versions, identifiers, approvals, and artifact relationships before routing downstream work.
- Treat a file's existence as evidence of activity, not proof of completion or approval.
- Preserve each specialist skill's ownership, write boundaries, and approval gates.
- Do not silently repair, approve, or reinterpret an artifact owned by another skill.
- Run one primary specialist stage at a time unless the user explicitly requests a multi-stage diagnostic that performs no consequential writes.
- After a delegated stage completes, reassess the repository state and present the next eligible action.
- Do not cross a human approval gate automatically.
- Keep guided explanations concise and suitable for a scientist or developer who may not know the workflow terminology.

## Skill Location and Delegation

Assume this skill and the specialist skills are sibling directories under the same `skills/` directory.

Resolve a selected specialist entrypoint using:

```text
../<specialist-skill-name>/SKILL.md
```

Read that `SKILL.md` and follow it as the authoritative procedure for the selected stage. Read only the referenced files needed for the current step. Do not copy specialist instructions into this skill.

When the runtime cannot access or apply a sibling skill, stop before performing the specialist work. Report the missing skill name and expected path, then provide a concise handoff instruction the user can invoke after installing or restoring it.

## Interaction Modes

Use **guided mode** by default.

- **Guided:** explain the current stage, why it matters, required inputs, expected output, and approval decisions. Ask one focused question at a time when practical.
- **Standard:** present concise state, blockers, and the recommended action.
- **Expert:** include canonical paths, versions, identifiers, stale-state reasoning, and routing details.

Honor an explicitly requested mode. Do not reduce required validation in any mode.

## Supported User Actions

Classify the request as one of:

- **start:** initialize or enter the workflow for a new or undocumented project;
- **resume:** inspect existing artifacts and continue from the current valid state;
- **status:** report completed, active, blocked, stale, and not-started stages;
- **continue:** select and delegate the next eligible stage;
- **run-stage:** delegate a named workflow stage;
- **explain:** explain the current stage, blocker, approval, or expected artifact;
- **repair:** identify inconsistent or stale workflow state and route correction to the owning skill;
- **reconcile-issues:** delegate repository-issue publication or reconciliation to Skill G.

## Core Workflow

### 1. Locate the Project and Skills

Identify the repository root and confirm that the sibling skills required for the requested action are available. Do not require all A–K skills when only one stage is needed, but report missing downstream skills when showing the complete workflow.

Read `references/skill-routing.md` to map stages and user requests to specialist skills.

### 2. Inspect the Minimum Workflow State

Inspect `sdlc_docs/` and relevant repository artifacts. Read only enough metadata and approval evidence to determine stage state. Expand into a specialist artifact only when its state cannot be determined safely from the available metadata.

Read `references/state-detection.md` for stage evidence and state definitions.

### 3. Detect Inconsistency and Staleness

Check whether downstream artifacts still reference the current upstream versions, approvals, issues, implementation artifact, test evidence, release candidate, and target environment.

When upstream content changed after downstream approval or generation, mark the affected downstream stage as `stale`; do not present it as completed.

Read `references/invalidation-rules.md` for routing and invalidation rules.

### 4. Present the Workflow Status

Present a compact status before consequential delegation:

```text
Current stage: <stage>
Completed: <stages or none>
Blocked or stale: <items or none>
Recommended action: <one action>
Specialist: <skill name>
```

In expert mode, add artifact paths, versions, approval identifiers, and evidence for the routing decision.

Do not create a separate workflow-status document unless the user explicitly requests one.

### 5. Select the Next Eligible Stage

For `start`, choose the earliest missing prerequisite needed to establish usable project context.

For `resume` or `continue`, select the earliest stage that is:

1. required by the user's objective;
2. eligible from current upstream evidence;
3. incomplete, stale, or awaiting its owning review;
4. not blocked by an unresolved human decision.

Do not assume that every project must execute every stage immediately. Respect user-selected scope while enforcing prerequisites.

### 6. Prepare the Delegation Context

Before loading the specialist skill, summarize:

- user objective;
- selected stage and specialist skill;
- relevant canonical paths;
- selected identifiers and current versions;
- verified prerequisite approvals;
- blockers, stale relationships, or inconsistencies;
- interaction mode;
- whether writes or external actions are expected.

Do not reinterpret the artifacts during this handoff.

### 7. Reuse the Specialist Skill

Read and follow the selected sibling skill's `SKILL.md`. Allow that skill to control its own questions, files, templates, tools, external-write confirmation, approval requirements, and stop conditions.

Do not continue performing the stage from this wrapper when the specialist skill stops on a blocker.

### 8. Reassess and Close the Step

After the specialist stage completes:

1. inspect the artifacts it reports creating or updating;
2. verify that the expected stage evidence now exists;
3. update the user-facing status;
4. identify the next eligible action;
5. ask for confirmation before entering another consequential stage or approval gate.

Do not claim success solely because the specialist produced prose. Confirm the repository state when repository access is available.

## Boundary with Specialist Skills

This skill owns navigation, state assessment, delegation, and user-facing guidance.

It does not independently:

- interpret and approve project context;
- clarify requirements;
- create or revise user stories;
- approve product readiness;
- design or approve architecture;
- approve technical readiness;
- publish or reconcile repository issues;
- create implementation plans;
- implement code;
- create or execute automated testing;
- perform stakeholder acceptance;
- prepare or execute deployment.

Delegate each activity to its owner in `references/skill-routing.md`. Implementation execution and deployment execution remain outside Skills A–K unless separate execution skills are installed.

## Resources

- Read `references/skill-routing.md` when mapping a request or stage to a specialist skill.
- Read `references/state-detection.md` when starting, resuming, showing status, or deciding what is next.
- Read `references/invalidation-rules.md` when an upstream artifact changed, approvals disagree, or a downstream artifact may be stale.
- Read `references/guided-interaction.md` when interacting with a beginner or presenting choices, blockers, and approvals.
