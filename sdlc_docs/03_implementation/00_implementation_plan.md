# Implementation Plan Index

## Current State

- Plan set version: `1.0`
- Status: `ready-with-open-items`
- Repository issues: `#1`, `#2`, `#3`, `#4`, `#5`, `#6`, `#7`, `#8`
- Source stories: `US-0001`, `US-0002`, `US-0003`, `US-0004`, `US-0005`, `US-0006`, `US-0007`, `US-0008`
- Story version: `1.0`
- Architecture version: `1.0`
- Technical review: `TR-001`
- Repository issue publication: `publication-003`
- Code baseline: `8ce0d69`
- Author: `ChatGPT`
- Date: `2026-07-14`

## Delivery Order

| Priority | Plan | Issues | Parallelization |
|---|---|---|---|
| 1 | [001-data-intake-and-selection.md](plans/001-data-intake-and-selection.md) | `#1`, `#2` | Starts first. |
| 2 | [002-model-configuration-and-fitting.md](plans/002-model-configuration-and-fitting.md) | `#3`, `#4` | Settings design can begin after intake contracts are clear; fitting integrates after intake and settings. |
| 3 | [003-results-visualization-and-export.md](plans/003-results-visualization-and-export.md) | `#5`, `#6`, `#7` | Visualization and tabular export can run in parallel after fitted results exist; plot/metadata follows visualization. |
| 4 | [004-invalid-input-feedback.md](plans/004-invalid-input-feedback.md) | `#8` | Thread through intake, selection, and fitting rather than defer to the end. |

## Kanban Guidance

| Board Focus | Issues | Handoff or Checkpoint |
|---|---|---|
| Data intake path | `US-0001`, `US-0002` | Dataset state and selected variable contract are ready for fitting. |
| Model integration path | `US-0003`, `US-0004` | Settings and fitted prediction result contract are ready for consumers. |
| Results path | `US-0005`, `US-0006`, `US-0007` | Visualization/export outputs are ready for validation. |
| Cross-cutting validation | `US-0008` | Invalid upload, selection, and fitting cases are covered before release. |

## Open Items

- Application dependencies are not declared yet. The first implementation slice should add the chosen runtime dependencies within the approved architecture: Streamlit, CSV/data handling, GPR fitting, plotting, and export support.
- Plans use provisional module names grounded in the current empty package. Implementation may adjust names while preserving the approved responsibilities and interfaces.

## Readiness Decision

`ready-with-open-items`: implementation can begin, with dependency declaration and exact module naming resolved during the first implementation increments.

## Revision History

| Version | Date | Author | Action | Upstream Versions | Notes |
|---|---|---|---|---|---|
| 1.0 | 2026-07-14 | ChatGPT | Created implementation plan set | story `1.0`; architecture `1.0`; technical review `TR-001`; issues `publication-003`; code baseline `8ce0d69` | Initial implementation planning for issues `#1` through `#8`. |
