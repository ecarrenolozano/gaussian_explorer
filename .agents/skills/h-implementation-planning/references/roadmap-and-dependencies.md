# Roadmap and Dependencies

Create or refresh `sdlc_docs/03_implementation/01_implementation_roadmap.md` before issue-specific plans when planning a set of published repository issues.

The roadmap is a living coordination artifact for organizing canonical issues and assigning developers safely. It does not replace issue implementation plans.

Maintain it incrementally. When new informal requests later become approved stories and canonical issues, append a planning batch entry and update the current roadmap rather than replacing history.

## Evidence Sources

Use only project evidence:

- user-story priority from `sdlc_docs/01_requirements/01_user_stories.md`;
- issue mappings from `sdlc_docs/03_implementation/00_repository_issue_registry.md`;
- dependencies from `sdlc_docs/01_requirements/04_user_story_technical_readiness.md`;
- runtime flow, component ownership, data ownership, and decisions from architecture docs;
- current codebase, tests, dependencies, and configuration.
- intake reconciliation reports and indexes when issues originated from direct repository tracker intake.

Do not invent product priority, change story scope, or create calendar commitments.

## Dependency Types

- `none`: no upstream issue is required before work can start.
- `hard`: downstream work cannot be completed safely until the upstream issue is complete.
- `soft`: work can start in parallel, but final integration or review depends on upstream work.
- `split-across-waves`: cross-cutting work should be coordinated with multiple related issues instead of treated as one isolated final issue.

## Roadmap Contents

Record only:

- roadmap metadata and current upstream versions;
- planning batch history, including source batch, issue set, story version, architecture version, technical review, repository revision, and reconciliation batch when applicable;
- issue-to-story table with priority, issue ID, title, and current state;
- dependency table with type and evidence-based reason;
- implementation waves showing which issues can run in parallel;
- ready, blocked, needs-reconciliation, and ready-in-wave queues;
- developer assignment guidance, including safe parallel assignments and coordination notes;
- sequencing risks and open questions.

Do not include sprint estimates, sprint count, sprint plans, sprint capacity, dates, or calendar commitments.

## Routing

Route back to the owning upstream skill when dependency analysis exposes:

- untriaged or contributor-created issues without approved lineage;
- product priority or scope conflicts;
- missing or contradictory technical-readiness dependencies;
- architecture path, component ownership, data ownership, or runtime-flow conflicts;
- a reusable design decision that should govern multiple issues.

## Scale Rules

For small issue sets, issue plans may live directly under `sdlc_docs/03_implementation/plans/` if that convention already exists. For new incremental work or large sets, use:

```text
sdlc_docs/03_implementation/
├── 01_implementation_roadmap.md
├── planning_batches/
│   └── batch-<nnn>/
│       ├── batch-summary.md
│       └── plans/
└── indexes/
    ├── issue-plan-index.md
    ├── story-to-plan-index.md
    └── tracker-reconciliation-index.md
```

Do not create hundreds of flat plan files without indexes or batch grouping.
