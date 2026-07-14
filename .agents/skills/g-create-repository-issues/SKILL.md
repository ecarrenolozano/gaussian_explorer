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

Prepare complete issue bodies and metadata, including repository, title, body, labels, milestone, assignees, dependencies, source lineage, and warnings. Store the preview in:

`sdlc_docs/03_implementation/01_repository_issue_preview.md`

Use `templates/issue-preview.md`.

### 6. Obtain Publication Approval

Require explicit approval of the exact preview. Approval of stories, architecture, or technical readiness does not authorize repository writes.

### 7. Publish and Verify

Create or update only the approved issues. Verify issue identifiers, URLs, and applied metadata. Do not blindly retry ambiguous writes.

### 8. Update the Repository Issue Registry

Record verified mappings in:

`sdlc_docs/03_implementation/00_repository_issue_registry.md`

If issue publication succeeds but registry persistence fails, report partial completion and repair the registry without recreating the issue.

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
