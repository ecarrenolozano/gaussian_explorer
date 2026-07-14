# Implementation Plan

## Current State

- Plan version: `1.0`
- Status: `ready`
- Repository issues: `#8`
- Source stories: `US-0008`
- Story version: `1.0`
- Architecture version: `1.0`
- Technical review: `TR-001`
- Code baseline: `8ce0d69`
- Author: `ChatGPT`
- Date: `2026-07-14`

## Scope

Implement clear invalid-input feedback across upload, variable selection, and fitting. This plan is cross-cutting and should be threaded through plans 001 and 002 rather than implemented as a final isolated pass.

Out of scope: new validation cases beyond those approved in `US-0008`, persistent error logs, and user account behavior.

## Architecture References

- Streamlit web application.
- Workflow UI.
- CSV parsing and validation.
- Variable and GPR settings.
- Model fitting.
- Uploaded CSV dataset.
- In-memory analysis session.
- `architecture-decision-001-single-streamlit-web-application`
- `architecture-decision-002-in-memory-session-and-export-reproducibility`

## Existing Code and Test Baseline

No validation implementation exists yet. Validation should be introduced alongside intake, selection, and fitting modules so invalid states are blocked before analysis proceeds.

## Implementation Approach

Use typed validation results or exceptions that separate internal validation decisions from user-facing messages:

- Provisional `gaussian_explorer.validation` for reusable validation rules and message codes.
- Intake validation: malformed CSV, unsupported file, very large file.
- Column validation: no numeric columns, fewer than two selectable numeric columns.
- Selected-data validation: missing selected values, too few rows, duplicate X values.
- Streamlit layer maps validation failures to clear corrective feedback and disables downstream actions.

## Ordered Increments

### Increment 1 - Define Validation Result Shape

- Objective: Provide a consistent way to return validation success or user-facing failure.
- Affected code: provisional `src/gaussian_explorer/validation.py`; tests.
- Dependencies: None.
- Implementation change: Add typed validation result/message structures.
- Developer tests: Unit tests for success and failure result construction.
- Verification: Unit tests and type checking.
- Related story and issue: `US-0008` / `#8`

### Increment 2 - Validate Uploaded Files

- Objective: Reject malformed, unsupported, or very large files before analysis proceeds.
- Affected code: validation and data modules from plan 001.
- Dependencies: Plan 001 CSV parsing increment.
- Implementation change: Add upload/file validation rules and feedback messages.
- Developer tests: Malformed CSV, unsupported extension/content, large-file threshold behavior.
- Verification: Unit tests.
- Related story and issue: `US-0008` / `#8`

### Increment 3 - Validate Selectable Columns

- Objective: Reject datasets with no numeric columns or fewer than two selectable numeric columns.
- Affected code: validation and data modules from plan 001.
- Dependencies: Numeric-column discovery.
- Implementation change: Add numeric-column availability validation.
- Developer tests: No numeric columns; exactly one numeric column; two numeric columns.
- Verification: Unit tests.
- Related story and issue: `US-0008` / `#8`

### Increment 4 - Validate Selected Data for Fitting

- Objective: Reject missing selected values, too few rows, and duplicate X values before fitting.
- Affected code: validation module and modeling workflow from plan 002.
- Dependencies: Selected-variable extraction and fitting entry point.
- Implementation change: Add selected-data validation before the fit action is enabled or executed.
- Developer tests: Missing values, too few rows, duplicate X values, valid selected data.
- Verification: Unit tests and focused integration test across selection-to-fit boundary.
- Related story and issue: `US-0008` / `#8`

### Increment 5 - Surface Corrective Feedback in Streamlit

- Objective: Show clear feedback and block invalid downstream actions.
- Affected code: provisional `src/gaussian_explorer/app.py`; validation module.
- Dependencies: Increments 1-4.
- Implementation change: Map validation failures to Streamlit messages and disabled controls where appropriate.
- Developer tests: Component checks where practical; manual workflow check for all approved invalid cases.
- Verification: Manual Streamlit validation pass and unit coverage for message mapping.
- Related story and issue: `US-0008` / `#8`

## Data, Interface, Migration, and Configuration Changes

- Data: validation result/message structures.
- Interface: user-visible Streamlit feedback for invalid inputs.
- Migration: none.
- Configuration: optional file-size threshold constant if implemented.

## Risks, Assumptions, and Open Questions

- Risk: validation rules scattered across modules could drift; keep central validation behavior test-covered.
- Assumption: "very large file" threshold is an implementation decision unless product later specifies a numeric limit.
- Open item: choose initial file-size threshold and document it in app behavior or configuration.

## Change Requests and Routes

- New validation categories or changed acceptance behavior require story/product review.
- Architecture change required only if validation introduces persistence, background processing, or external services.

## Readiness Decision

`ready`: validation planning is actionable and should be implemented alongside the dependent slices.

## Revision History

| Version | Date | Author | Action | Upstream Versions | Notes |
|---|---|---|---|---|---|
| 1.0 | 2026-07-14 | ChatGPT | Created | story `1.0`; architecture `1.0`; technical review `TR-001`; issue `#8`; code baseline `8ce0d69` | Initial cross-cutting validation plan. |
