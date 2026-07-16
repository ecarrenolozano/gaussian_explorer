# Implementation Planning Batch - batch-001

<!-- implementation-planning-batch | batch: batch-001 | roadmap-version: 1.0 | story-version: 1.0 | architecture-version: 1.0 | technical-review: TR-002 | repository-revision: 2fb7e5d -->

## Scope

- Batch: `batch-001`
- Source: live GitHub issues with approved `TR-002` lineage markers
- Repository issues: `#9`, `#10`, `#11`, `#12`, `#13`, `#14`, `#15`, `#16`
- Source stories or spikes: `US-0001`, `US-0002`, `US-0003`, `US-0004`, `US-0005`, `US-0006`, `US-0007`, `US-0008`
- Reconciliation batch, when applicable: none
- Registry: local registry missing; live issue bodies verified as source evidence

## Review Disposition

- Superseded by: `batch-002`
- Disposition: `changes-required`
- Reason: This batch was created before the local repository issue registry was repaired and did not plan complete vertical slices for the repository issues. Several increments omitted required H planning fields, and concrete model/export decisions were underspecified.

## Added or Updated Plans

| Issue | Story or spike | Plan path | Version | Assessment |
|---:|---|---|---|---|
| `#9` | `US-0001` | `planning_batches/batch-001/plans/issue-9-implementation-plan.md` | `1.0` | `ready` |
| `#10` | `US-0002` | `planning_batches/batch-001/plans/issue-10-implementation-plan.md` | `1.0` | `ready-with-open-items` |
| `#11` | `US-0003` | `planning_batches/batch-001/plans/issue-11-implementation-plan.md` | `1.0` | `ready-with-open-items` |
| `#12` | `US-0004` | `planning_batches/batch-001/plans/issue-12-implementation-plan.md` | `1.0` | `ready-with-open-items` |
| `#16` | `US-0005` | `planning_batches/batch-001/plans/issue-16-implementation-plan.md` | `1.0` | `ready-with-open-items` |
| `#14` | `US-0006` | `planning_batches/batch-001/plans/issue-14-implementation-plan.md` | `1.0` | `ready-with-open-items` |
| `#13` | `US-0007` | `planning_batches/batch-001/plans/issue-13-implementation-plan.md` | `1.0` | `ready-with-open-items` |
| `#15` | `US-0008` | `planning_batches/batch-001/plans/issue-15-implementation-plan.md` | `1.0` | `ready-with-open-items` |

## Dependency Changes

| Issue | Dependency | Type | Reason |
|---:|---|---|---|
| `#10` | `#9` | `hard` | Needs accepted dataset and numeric column discovery input. |
| `#11` | `#10` | `soft` | Settings can be implemented before full UI integration, but fit workflow uses selected variables. |
| `#12` | `#9`, `#10`, `#11` | `hard` | Fitting requires all upstream inputs. |
| `#16` | `#12` | `hard` | Visualization needs fitted prediction output. |
| `#14` | `#12` | `hard` | Results CSV needs fitted prediction output. |
| `#13` | `#12`, `#16` | `hard` | Plot and metadata export need fitted output and visualization metadata. |
| `#15` | `#9`, `#10`, `#12` | `split-across-waves` | Invalid-input feedback belongs in each validation gate. |

## Routes and Open Items

| Item | Route | Reason |
|---|---|---|
| Missing local issue registry | Skill G | Refresh registry for live `#9`-`#16` issue set. |
| Library choices for GPR, plotting, and plot export | Implementation review | Choices are inside approved architecture but must be declared and tested. |
| Persistence, backend, database, deployment automation | Skill E | Out of approved MVP boundaries. |

## Readiness

- Assessment: `changes-required`
- Approver, when required: pending
- Date: `2026-07-16`
