---
name: g-create-repository-issues
description: publish approved implementation-ready user stories and approved technical spike candidates as traceable github or gitlab issues, and reconcile repository-created issues with sdlc_docs. use after technical readiness to preview external writes, detect duplicates, preserve documentation lineage, maintain the repository issue registry, and repair documentation drift without silently changing approved scope.
---

# Create Repository Issues

## Purpose

Create or reconcile repository issues without breaking traceability between approved workflow documentation and repository work tracking.

Use publication mode to create issues from approved sources. Use reconciliation mode to detect and classify issues created or changed directly in the repository.

## Governing Rules

- Treat every repository write as an external operation requiring explicit approval of the exact preview.
- Publish only work supported by an authoritative approved source.
- Do not invent scope, technical tasks, labels, milestones, assignees, or dependencies.
- Publish each approved user story as exactly one repository issue; represent story-to-story dependency or hierarchy as issue relationships, not duplicate issues.
- For user-story issues, make the issue description preserve the same human-readable format as the canonical user story block in `01_user_stories.md`; do not rewrite it into Summary/Motivation/Traceability sections.
- Keep `sdlc_docs` authoritative for approved scope and GitHub or GitLab authoritative for operational issue state.
- Never silently copy repository scope changes back into approved documentation.
- Use human-readable names and workflow identifiers; do not create implementation naming conventions.
- On uncertain write results, verify before retrying.

## Canonical Files

Read when applicable:

- `sdlc_docs/01_requirements/01_user_stories.md`
- `sdlc_docs/01_requirements/02_traceability_matrix.md`
- `sdlc_docs/01_requirements/04_user_story_technical_readiness.md`
- `sdlc_docs/02_architecture/01_story_architecture_map.md`
- `sdlc_docs/03_implementation/00_repository_issue_registry.md`
- repository-native issue forms, templates, labels, milestones, and contribution rules

Create the registry from `templates/repository-issue-registry.md` when missing.

## Core Workflow

### 1. Determine the Operating Mode

Use **publication mode** when creating approved issues. Use **reconciliation mode** when comparing repository issues with the local registry or investigating directly created issues.

### 2. Validate the Repository and Upstream State

Confirm the repository, platform, access level, and exact source artifacts. For story issues, require an `implementation-ready` story with valid human technical approval for the current story and architecture versions. For spikes, require an approved spike candidate from technical readiness.

Read `references/input-and-publication-gate.md`.

### 3. Select and Classify Work

Identify the authoritative source type and source identifier. Do not publish architecture changes, migrations, enabling work, or dependencies unless an upstream artifact explicitly defines them.

### 4. Detect Existing or Divergent Issues

Search machine-readable lineage first, then source identifiers and title similarity. Classify existing issues as linked, missing from registry, missing repository lineage, candidate match, unlinked, duplicate, or diverged.

Read `references/reconciliation.md` when reconciling or when a possible match exists.

### 5. Prepare the Exact Preview

Prepare complete issue bodies and metadata, including repository, title, body, labels, milestone, assignees, dependencies, source lineage, proposed issue relationships, minimal delivery plan, and warnings. Store the preview in:

`sdlc_docs/03_implementation/01_repository_issue_preview.md`

Use `templates/issue-preview.md`.

For user-story issue bodies:

- Copy the complete canonical story block from `01_user_stories.md`, preserving the same Markdown structure: `## US-...`, story metadata comment, `### **User story**`, `### **Source and constraints**`, and `### **Acceptance criteria**` with scenario headings and Given/When/Then lines.
- Do not replace the story block with repository-template prose such as `# Summary`, `# Motivation`, or `# Traceability`.
- Add the required `workflow-link` HTML marker after the copied story block. Keep it hidden as a comment so the visible issue description still reads like the user-story document.
- Put repository labels, milestone, assignees, relationship writes, and delivery-order guidance in preview metadata, not in the issue body.

For approved user stories, default to one issue per story. When a story depends on another approved story, include a proposed relationship plan:

- **GitHub:** after both issues exist, add the dependency issue as a sub-issue of the dependent story issue when the relationship is unambiguous and the child issue does not need multiple parents. GitHub CLI supports `gh issue create --parent` for new sub-issues and `gh issue edit PARENT --add-sub-issue CHILD` for existing issues. When a dependency edge cannot be represented as a sub-issue because it would require multiple parents, prefer GitHub's native issue dependency relationship (`gh issue edit DEPENDENT --add-blocked-by DEPENDENCY`) before falling back to body text only.
- **GitLab:** use native linked issues when available. Prefer `blocks` / `is_blocked_by` for dependency semantics; use `relates_to` only when the dependency direction is unclear or the GitLab tier/API does not support blocking links. Do not claim GitLab sub-issues unless the target GitLab instance exposes that feature.
- **Fallback:** if the platform cannot represent the relationship, keep the dependency in the issue body and record the skipped relationship with a warning.

Every proposed relationship is an external write. Preview it explicitly with parent, child, relationship type, platform command/API intent, and any fallback reason.

Also include a minimal delivery plan derived from the approved dependency graph:

- Include an explicit priority order for attending issues. Priority is based on dependency unblocking, critical-path position, integration risk, and user-visible milestone value.
- Include explicit parallelization groups. Issues in the same group can usually be started together once the listed start condition is met.
- Include a small Kanban guidance table with suggested board focus, start condition, and handoff/checkpoint. Keep it short enough for a senior developer to assign work without reading a full implementation plan.
- Do not assign named people unless the user explicitly instructs you to assign users.
- For the current Gaussian Explorer shape, the useful pattern is: upload first; variable selection and settings next; model fitting as the central integration issue; visualization and tabular export in parallel after fitting; plot/reproducibility after visualization; invalid-input feedback threaded across upload, selection, and fitting rather than deferred to the end.

### 6. Obtain Publication Approval

Require explicit approval of the exact preview. Approval of stories, architecture, or technical readiness does not authorize repository writes.

### 7. Publish and Verify

Create or update only the approved issues and approved issue relationships. Verify issue identifiers, URLs, applied metadata, and relationship state. Do not blindly retry ambiguous writes.

### 8. Update the Repository Issue Registry

Record verified mappings in:

`sdlc_docs/03_implementation/00_repository_issue_registry.md`

If issue publication succeeds but registry persistence fails, report partial completion and repair the registry without recreating the issue.

Record verified issue relationships separately from issue mappings so future reconciliation can distinguish scope publication from platform hierarchy/link state.

### 9. Reconcile Repository-Originated Issues

Classify unregistered issues and route them to the appropriate workflow owner. Require confirmation before binding an issue to existing documentation. Record reconciliation history without treating repository text as approved scope.

## Boundary with Other Skills

- Skill F determines technical readiness and spike candidates.
- Skill G owns repository publication, registry maintenance, and reconciliation.
- Skill H creates detailed implementation plans linked to published work items.
- New product behavior returns to Skill B.
- Story defects return to Skill C and Skill D.
- Architecture changes return to Skill E.
- Skill G does not implement work or create detailed code-level plans.

## Resources

- `references/input-and-publication-gate.md`
- `references/reconciliation.md`
- `references/platform-and-write-safety.md`
- `references/persistence.md`
- `templates/issue-preview.md`
- `templates/repository-issue-registry.md`
