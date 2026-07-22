---
name: g-create-repository-issues
description: Publish technically approved user stories or spike candidates as repository tracker issues, reconcile repository tracker issues with SDLC documentation, and triage direct contributor-created tracker issues at scale across platforms such as GitHub, GitLab, GitKraken, or other issue trackers. Use after f-user-story-technical-readiness when Codex must verify story, architecture, and technical-review lineage; prevent duplicates; show exact issue descriptions and metadata in chat for approval before tracker writes; create or update approved issues; verify publication; update the repository issue registry; classify unlinked tracker issues as duplicates, similar existing scope, bugs, new requirement candidates, out of scope, not actionable, or needing human review; create intake reconciliation reports; or route unlinked, duplicate, diverged, or contributor-created issues.
---

# Create Repository Issues

## Purpose

Publish approved outcome-level work to a repository issue tracker and keep tracker state mapped to canonical `sdlc_docs`.

Accept direct repository issues as raw intake signals, not implementation-ready work, until they are reconciled against approved stories, architecture, technical readiness, existing canonical issues, and implementation plans.

## Non-Negotiables

- Publish only versioned work with current product, architecture, and technical approval.
- Treat `sdlc_docs` as the source of approved scope; treat the issue tracker as the source of operational issue state.
- Show the complete approval preview in chat before any tracker write: repository, title, exact body, labels, milestone, assignees, dependencies, source lineage, architecture lineage, and warnings.
- Do not use a separate approval/proposal file unless the user asks for one, accepts that format, or the file is itself the deliverable.
- Create or update only issues explicitly approved from the chat preview.
- Link to architecture and decisions; do not duplicate long architecture text in issue bodies.
- Search for duplicates by source identifier, lineage marker, registry mapping, and tracker results before writing.
- Verify every tracker write by reading the created or updated issue before claiming success.
- Update the repository issue registry only after verification. Preserve partial-publication facts if registry persistence fails.
- Do not convert bulk contributor-created issues directly into stories or plans. Reconcile, cluster, classify, and promote only distinct new or changed scope.
- Require approval before bulk tracker mutations such as closing issues, adding labels, posting comments, or rewriting bodies.
- Do not create implementation plans or file-level tasks; route that work to Skill H.

## Canonical Files

Read the files needed for the selected scope:

- `sdlc_docs/01_requirements/01_user_stories.md`
- `sdlc_docs/01_requirements/03_user_story_product_readiness.md`
- `sdlc_docs/01_requirements/04_user_story_technical_readiness.md`
- `sdlc_docs/02_architecture/00_architecture_document.md`
- `sdlc_docs/02_architecture/01_architecture_traceability.md`
- relevant files under `sdlc_docs/02_architecture/decisions/`
- relevant detailed architecture files such as `sdlc_docs/02_architecture/containers/`, only when present and referenced
- `sdlc_docs/03_implementation/00_repository_issue_registry.md`; create it from `templates/repository-issue-registry.md` when absent
- existing reconciliation reports under `sdlc_docs/03_implementation/intake_reconciliation/`, when present

## Modes

- **Publication:** create or update approved repository issues, verify them, and register mappings.
- **Reconciliation:** compare tracker issues with the registry and documentation, classify differences, and route them.
- **Intake reconciliation:** process direct contributor-created tracker issues, cluster duplicates and similar issues, identify new requirement candidates or bugs, and produce a reconciliation batch report before any SDLC promotion.

## Publication Workflow

1. Select repository, platform, source stories or spike candidates, architecture version, and technical review.
2. Validate the gate with `references/input-and-publication-gate.md`. Stop on stale approval, missing lineage, unresolved architecture scope, or contradictory state.
3. Inspect repository issue forms, contribution rules, labels, milestones, permissions, and current issues. Read `references/platform-and-write-safety.md` before any tracker write.
4. Detect duplicates from registry, tracker search, source identifiers, and lineage markers. Use `references/reconciliation.md` for possible matches or direct repository-originated issues.
5. Prepare each issue with `templates/issue-template-repository.md`. Preserve the template sections: story heading, `Description`, `Assumptions & Details`, `Source and constraints`, and acceptance scenarios.
6. Show the complete approval preview in chat. Use one compact metadata block per issue plus the exact body. If the set is long, keep formatting scannable, but do not replace the chat preview with a file.
7. Wait for explicit approval of the exact repository, issue bodies, labels, milestones, assignees, and dependencies shown in chat. If approval covers only part of the set, publish only that part or show the missing items and ask again.
8. Create or update approved issues only. Verify issue number, URL, body, lineage, labels, milestone, assignees, and state by reading the issue after the write.
9. Update `sdlc_docs/03_implementation/00_repository_issue_registry.md` with verified mappings. Follow `references/persistence.md` if publication succeeds but registry update fails.

## Reconciliation Workflow

Compare repository issues, registry rows, and canonical SDLC documentation. Classify each difference with `references/reconciliation.md`. Require confirmation before binding any unregistered tracker issue to approved documentation.

For contributor-created or otherwise unlinked issues:

1. Collect the candidate issue set from the tracker and registry. Identify issues missing SDLC lineage markers.
2. Cluster issues by topic, source markers, titles, bodies, labels, acceptance behavior, linked PRs, and similarity to approved stories, canonical issues, and implementation plans.
3. Classify each issue as `canonical-linked`, `duplicate`, `similar-existing-scope`, `bug`, `new-requirement-candidate`, `out-of-scope`, `not-actionable`, or `needs-human-review`.
4. Prepare an intake reconciliation batch under `sdlc_docs/03_implementation/intake_reconciliation/` using the reconciliation templates. Include summary counts, clusters, proposed issue actions, and upstream routes.
5. Show proposed tracker mutations in chat before writing: labels, comments, closures, body updates, or canonical links.
6. After approval, perform only the approved tracker mutations, verify them by reading the affected issues, and update the registry and reconciliation index.
7. Route promoted new requirement candidates to Skill B by appending or preparing input for `sdlc_docs/01_requirements/00_raw_ideas.md`. Do not create stories or implementation plans from intake issues inside Skill G.

## Boundary with Other Skills

- Skill F owns technical readiness and spike candidates.
- Skill E owns architecture content and mappings.
- Skill G owns issue publication, registry maintenance, and reconciliation.
- Skill H owns implementation plans linked to published issues.
- Skill B owns clarification of promoted new requirement candidates.
- A lightweight bug path may keep confirmed implementation bugs in the tracker, but behavior-changing bugs must route upstream through requirements and architecture as needed.

## Resources

- `references/input-and-publication-gate.md`: gate checklist for publication.
- `references/platform-and-write-safety.md`: tracker write and verification rules.
- `references/reconciliation.md`: classification and routing for existing tracker issues.
- `references/persistence.md`: registry update and partial-publication recovery.
- `templates/issue-template-repository.md`: issue body template.
- `templates/repository-issue-registry.md`: registry bootstrap template.
- `templates/tracker-intake-summary.md`: reconciliation batch summary template.
- `templates/tracker-issue-clusters.md`: clustered issue analysis template.
- `templates/tracker-reconciliation-decisions.md`: proposed and verified issue-action decisions template.
