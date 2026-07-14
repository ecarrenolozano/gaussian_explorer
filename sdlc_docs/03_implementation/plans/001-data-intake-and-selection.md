# Implementation Plan

## Current State

- Plan version: `1.0`
- Status: `ready-with-open-items`
- Repository issues: `#1`, `#2`
- Source stories: `US-0001`, `US-0002`
- Story version: `1.0`
- Architecture version: `1.0`
- Technical review: `TR-001`
- Code baseline: `8ce0d69`
- Author: `ChatGPT`
- Date: `2026-07-14`

## Scope

Implement CSV upload parsing and numeric variable selection for small experimental datasets. This plan covers accepting supported CSV input, exposing validated dataset state, detecting numeric columns, and recording selected X/Y variables for later GPR fitting.

Out of scope: model fitting, visualization, exports, persistence, accounts, and batch processing.

## Architecture References

- Streamlit web application.
- Workflow UI.
- CSV parsing and validation.
- Variable and GPR settings.
- Uploaded CSV dataset.
- In-memory analysis session.
- `architecture-decision-001-single-streamlit-web-application`
- `architecture-decision-002-in-memory-session-and-export-reproducibility`

## Existing Code and Test Baseline

The repository currently has a Python package skeleton under `src/gaussian_explorer`, empty unit/integration test directories, strict `mypy`, `ruff`, and `pytest` configuration, and no runtime application dependencies in `pyproject.toml`.

## Implementation Approach

Use small application-support modules that can be tested without running Streamlit:

- Provisional `gaussian_explorer.data` for CSV parsing, dataset representation, numeric-column discovery, and selected-column extraction.
- Provisional `gaussian_explorer.app` for Streamlit workflow wiring once dependencies are declared.
- Data structures should be typed and simple, such as a validated dataset object containing the tabular data, column names, numeric column names, and original filename metadata.

## Ordered Increments

### Increment 1 - Declare Intake Dependencies

- Objective: Add the minimum dependencies needed for CSV upload and app wiring.
- Affected code: `pyproject.toml`; dependency lock file if the project uses one.
- Dependencies: None.
- Implementation change: Add Streamlit and a tabular data library, with exact package choices made by implementation.
- Developer tests: Existing quality checks should still import the package.
- Verification: `uv run pytest`, `uv run ruff check .`, `uv run mypy src`.
- Related story and issue: `US-0001` / `#1`

### Increment 2 - Parse Supported CSV Input

- Objective: Convert uploaded CSV bytes or file-like input into a validated in-memory dataset.
- Affected code: provisional `src/gaussian_explorer/data.py`; unit tests under `tests/unit/`.
- Dependencies: Increment 1.
- Implementation change: Implement CSV read behavior for supported CSV files and return dataset metadata used by later workflow steps.
- Developer tests: Unit tests for a small valid CSV, multiple-column input, and preservation of column names.
- Verification: Unit tests plus type checking.
- Related story and issue: `US-0001` / `#1`

### Increment 3 - Discover Numeric Columns

- Objective: Identify selectable numeric columns from a validated dataset.
- Affected code: provisional `src/gaussian_explorer/data.py`; unit tests.
- Dependencies: Increment 2.
- Implementation change: Provide a typed operation that returns numeric columns without mutating the dataset.
- Developer tests: Multi-column CSV with numeric and non-numeric columns; all-numeric CSV; no-numeric CSV behavior prepared for validation plan.
- Verification: Unit tests.
- Related story and issue: `US-0002` / `#2`

### Increment 4 - Record Selected X/Y Variables

- Objective: Capture selected X and Y numeric columns for downstream fitting.
- Affected code: provisional `src/gaussian_explorer/data.py` or `settings.py`; Streamlit wiring in provisional `app.py`.
- Dependencies: Increment 3.
- Implementation change: Add a typed selected-variable structure and Streamlit controls backed by discovered numeric columns.
- Developer tests: Unit tests for valid selection and extracting selected series.
- Verification: Unit tests and focused manual Streamlit check once app entry point exists.
- Related story and issue: `US-0002` / `#2`

## Data, Interface, Migration, and Configuration Changes

- Data: in-memory validated dataset and selected X/Y variable state.
- Interface: Streamlit file upload and select controls.
- Migration: none.
- Configuration: dependency additions only.

## Risks, Assumptions, and Open Questions

- Assumption: datasets remain small enough for in-memory processing.
- Risk: CSV parsing and type inference can surprise users; validation issue `#8` covers clear failure feedback.
- Open item: choose exact data library during implementation.

## Change Requests and Routes

- New file formats or persistent data storage must return to requirements and architecture review.
- Additional variable types or multi-output regression would require story changes.

## Readiness Decision

`ready-with-open-items`: implementation can begin; exact dependency choices are open but non-blocking.

## Revision History

| Version | Date | Author | Action | Upstream Versions | Notes |
|---|---|---|---|---|---|
| 1.0 | 2026-07-14 | ChatGPT | Created | story `1.0`; architecture `1.0`; technical review `TR-001`; issues `#1`, `#2`; code baseline `8ce0d69` | Initial plan for data intake and variable selection. |
