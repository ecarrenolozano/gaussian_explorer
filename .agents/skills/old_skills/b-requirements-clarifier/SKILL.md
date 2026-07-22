---
name: b-requirements-clarifier
description: clarify informal or incomplete software requirements before backlog creation. use with sdlc_docs/00_project_context/project_context.md and unprocessed dated batches in sdlc_docs/01_requirements/00_raw_ideas.md, or with requester messages, notes, transcripts, and rough requirements, to classify uncertainty, conduct focused clarification, score readiness, and produce a traceable handoff for downstream planning skills.
---

# Requirements Clarifier

## Purpose

Turn informal requirements into shared, evidence-based understanding before implementation. Preserve requester intent, expose uncertainty, conduct a focused interview, and produce a structured handoff for downstream user-story, issue, architecture, or implementation-planning skills.

Interview patiently and progressively. Do not treat clarification as approval or solution design.

## Governing Rules

Apply these rules throughout the workflow:

- Preserve the original requester input and meaning.
- Identify the source for each material finding.
- Distinguish confirmed information from inference and unresolved uncertainty.
- Do not invent requirements or silently resolve conflicts.
- Ask only questions that materially improve readiness.
- Keep unresolved items visible in the handoff.
- Do not generate user stories, issues, architecture, implementation plans, test plans, or acceptance criteria by default.

Canonical source files remain authoritative. Summaries from other skills are supporting context, not replacements for the original files.

## Workflow

1. Gather and validate sources.
2. Extract and organize findings.
3. Separate requirement states.
4. Interview to reduce uncertainty.
5. Produce the clarified requirements handoff.

### 1. Gather and Validate Sources

Read these canonical files in order:

1. `sdlc_docs/00_project_context/project_context.md`
2. `sdlc_docs/01_requirements/00_raw_ideas.md`

Use `project_context.md` for project purpose, scope, stakeholders, constraints, terminology, and approved decisions. Use `00_raw_ideas.md` for informal requirement batches that may be incomplete, ambiguous, inconsistent, or unstructured.

Treat requester messages, notes, transcripts, or requirement text supplied in the conversation as supplementary evidence unless the user explicitly designates them as replacements.

If `a-project-context-interpretation` is available, invoke it for an overview, then verify relevant details against `project_context.md`.

If either canonical file is missing:

- Continue with the available evidence.
- Record the missing file as a context gap.
- Do not infer its contents.
- Stop only when no requirement batch can be identified and no useful clarification question can be formed.

Record available and missing inputs before continuing.

### 2. Extract and Organize Findings

Analyze available evidence before asking questions. Organize findings under:

- Project or feature goal
- Target users and stakeholders
- Inputs and outputs
- Workflows or user actions
- Functional and non-functional requirements
- Constraints and preferences
- Dependencies, integrations, and external systems
- Important terminology
- Risks, edge cases, and failure modes

For each finding, record its source and whether it is directly stated or inferred. Mark unsupported categories as `Not specified`. Do not resolve uncertainty in this step.

### 3. Separate Requirement States

Classify each finding into one primary state:

- **Confirmed requirement:** Explicitly supported by a source or confirmed user response.
- **Likely assumption:** Plausible but not explicitly confirmed.
- **Ambiguity:** Supports multiple reasonable interpretations.
- **Contradiction:** Conflicts with another source or confirmed response.
- **Missing decision:** Must be decided for reliable downstream planning.
- **Out-of-scope candidate:** May exceed documented project scope.

For each item, identify its source and give a brief rationale. Keep items separate when they require different decisions.

When sources conflict, identify both statements, use approved project-context decisions as the current baseline unless the user explicitly supersedes them, and preserve the conflict for confirmation. Do not silently merge, replace, or discard either statement.

Label useful recommendations as **Suggestion**. Never treat a suggestion as a requirement until confirmed.

Use unresolved classifications as the interview backlog for Step 4. Do not ask questions in this step.

### 4. Interview to Reduce Uncertainty

When unresolved items require user input, read and follow `references/interview-guide.md`.

After each answer, update the requirement states and continue with the next highest-impact unresolved item. Stop when readiness can be determined reliably, remaining questions are deferrable preferences, or the user requests the current handoff.

Preserve unresolved essentials under **Open Questions** and lower readiness accordingly.

### 5. Produce the Clarified Requirements Handoff

When clarification is complete or the user requests the current state, read and follow these resources in order:

1. `references/handoff-rules.md`
2. `templates/handoff.md`
3. `references/readiness.md`

Append or propose the handoff for the corresponding batch in `sdlc_docs/01_requirements/00_raw_ideas.md`. Keep the original requester input unchanged.

Do not load these resources before Step 5 unless their rules are required for the current action.

The completed handoff is the authoritative clarification input for downstream planning. It does not replace the original requester input or project context.

## Boundary with Other Skills

When the user requests a downstream artifact, complete or update the handoff first, determine readiness, and pass the result to the relevant downstream skill. Do not silently expand this skill into backlog creation or solution design.
