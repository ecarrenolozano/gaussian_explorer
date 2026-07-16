# Implementation Roadmap - Gaussian Explorer MVP

<!-- implementation-roadmap | version: 2.0 | story-version: 1.0 | architecture-version: 1.0 | technical-review: TR-002 | repository-revision: 2fb7e5d -->

## Roadmap State

- Current roadmap version: `2.0`
- Current planning batch: `batch-002`
- Current story version: `1.0`
- Current architecture version: `1.0`
- Current technical review: `TR-002`
- Repository revision: `2fb7e5d`
- Registry: `sdlc_docs/03_implementation/00_repository_issue_registry.md`
- Reconciliation batches: `registry-repair-001`

## Planning Batch History

| Batch | Source | Issues | Story version | Architecture version | Technical review | Reconciliation batch | Repository revision | Result |
|---|---|---|---|---|---|---|---|---|
| `batch-001` | Live GitHub issues with approved `TR-002` lineage markers | `#9`, `#10`, `#11`, `#12`, `#13`, `#14`, `#15`, `#16` | `1.0` | `1.0` | `TR-002` | None | `2fb7e5d` | `changes-required`; superseded by `batch-002` |
| `batch-002` | Registry repair plus corrected vertical implementation planning | `#9`, `#10`, `#11`, `#12`, `#13`, `#14`, `#15`, `#16` | `1.0` | `1.0` | `TR-002` | `registry-repair-001` | `2fb7e5d` | `ready` |

## Current Issue Priority and Status

| Wave | Issue | Story | Priority | Title | Kanban status |
|---|---:|---|---|---|---|
| 1 | `#9` | `US-0001` | MVP | Upload Experimental CSV Data | Ready |
| 2 | `#10` | `US-0002` | MVP | Select Regression Variables | Ready after `#9` |
| 2 | `#11` | `US-0003` | MVP | Configure GPR Settings | Ready with soft dependency on `#10` |
| 3 | `#12` | `US-0004` | MVP | Fit the Gaussian Process Regression Model | Ready after `#9`, `#10`, `#11` |
| 4 | `#16` | `US-0005` | MVP | View Prediction and Uncertainty | Ready after `#12` |
| 4 | `#14` | `US-0006` | MVP | Export Tabular Prediction Results | Ready after `#12` |
| 5 | `#13` | `US-0007` | MVP | Export Plot and Reproducibility Metadata | Ready after `#12`, `#16` |
| split | `#15` | `US-0008` | MVP | Receive Clear Invalid-Input Feedback | Ready; coordinate across upload, selection, settings, and fitting gates |

## Dependency Table

| Issue | Depends on | Type | Reason |
|---:|---|---|---|
| `#9` | None | `none` | CSV upload is the first data availability gate. |
| `#10` | `#9` | `hard` | Variable selection requires an accepted uploaded dataset and numeric-column contract. |
| `#11` | `#10` | `soft` | Settings controls can be developed with fixtures, but workflow integration depends on selected variables. |
| `#12` | `#9`, `#10`, `#11` | `hard` | Fitting requires uploaded data, selected variables, and current GPR settings. |
| `#16` | `#12` | `hard` | Visualization consumes fitted prediction results. |
| `#14` | `#12` | `hard` | Tabular export consumes fitted prediction results and settings. |
| `#13` | `#12`, `#16` | `hard` | Plot and metadata export depends on fitted results and visualization output/metadata. |
| `#15` | `#9`, `#10`, `#12` | `split-across-waves` | Invalid-input behavior must be built into upload, selection, and fitting gates rather than deferred. |

## Implementation Waves

1. Wave 1 establishes CSV intake, upload UI, session-state storage, and upload validation through `#9` plus the upload slice of `#15`.
2. Wave 2 adds selectable numeric columns and editable GPR settings through `#10` and `#11`. These can run in parallel after agreeing on `SelectedVariables`.
3. Wave 3 adds dependencies, GPR fitting, confidence-bound calculation, fit UI, result state, and fitting validation through `#12` plus the fitting slice of `#15`.
4. Wave 4 adds fitted-result consumers through `#16` and `#14`; visualization and tabular export can run in parallel from `PredictionResult`.
5. Wave 5 adds Plotly HTML plot export and deterministic reproducibility metadata through `#13`.

## Ready and Blocked Queues

| Queue | Issues | Reason |
|---|---|---|
| Ready | `#9`, `#15` upload slice | Existing CSV intake module and tests provide a confirmed starting point. |
| Ready in wave 2 | `#10`, `#11` | Start after or alongside the dataset contract from `#9`. |
| Ready in wave 3 | `#12`, `#15` fitting slice | Start after upload, selection, and settings contracts are stable. |
| Ready in wave 4 | `#16`, `#14` | Start after `PredictionResult` is available. |
| Ready in wave 5 | `#13` | Start after visualization metadata is available. |
| Needs reconciliation | None | Registry repaired in `registry-repair-001`. |

## Developer Assignment Guidance

- Assign `#9` and the upload-validation portion of `#15` together or to tightly coordinated developers.
- Assign `#10` and `#11` in parallel only after agreeing on the selected-variable and settings dataclasses.
- Assign `#16` and `#14` in parallel after `#12` exposes a tested prediction-result structure.
- Keep `#13` separate from `#14`; it depends on visualization metadata, not only tabular prediction rows.
- Avoid changing Streamlit/database/deployment boundaries; all plans stay inside the single Streamlit Web Application and In-memory Analysis Session.

## Sequencing Risks

- `#11` and `#10` can run in parallel only if developers agree on `SelectedVariables` before wiring Streamlit state.
- `#12` should not merge until confidence-bound calculation with `scipy.stats.norm.ppf` is tested.
- `#13` intentionally exports Plotly HTML; a future mandatory static image format would require product clarification.

## Open Upstream Routes

| Item | Route | Reason |
|---|---|---|
| Any change requiring persistence, backend API, database, or deployment automation | Skill E | Would change approved container/deployment boundaries. |
| Product-level changes to supported file types, data limits, or exported artifact promises | Skills B/C/D | Would alter approved acceptance behavior. |

## Readiness

- Assessment: `ready`
- Approver, when required: pending
- Date: `2026-07-16`
