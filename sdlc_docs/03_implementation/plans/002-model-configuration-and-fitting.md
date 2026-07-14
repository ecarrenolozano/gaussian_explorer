# Implementation Plan

## Current State

- Plan version: `1.0`
- Status: `ready-with-open-items`
- Repository issues: `#3`, `#4`
- Source stories: `US-0003`, `US-0004`
- Story version: `1.0`
- Architecture version: `1.0`
- Technical review: `TR-001`
- Code baseline: `8ce0d69`
- Author: `ChatGPT`
- Date: `2026-07-14`

## Scope

Implement default and editable GPR settings and fit a Gaussian Process Regression model from validated selected variables. This plan produces fitted prediction results for downstream visualization and export.

Out of scope: CSV upload, variable selection, visualization rendering, export generation, persistence, and batch execution.

## Architecture References

- Streamlit web application.
- Workflow UI.
- Variable and GPR settings.
- GPR fitting and prediction.
- Model fitting.
- In-memory analysis session.
- `architecture-decision-001-single-streamlit-web-application`
- `architecture-decision-002-in-memory-session-and-export-reproducibility`

## Existing Code and Test Baseline

No model, settings, or Streamlit implementation exists yet. The package has strict typing and no runtime dependencies. Intake and selection contracts are expected from plan `001-data-intake-and-selection`.

## Implementation Approach

Use a small typed settings/result boundary that downstream components can consume:

- Provisional `gaussian_explorer.settings` for model settings defaults and validation.
- Provisional `gaussian_explorer.modeling` for GPR fitting and prediction.
- A fitted result object should include predicted X values, predicted mean, uncertainty bounds, selected variable names, and settings used.

## Ordered Increments

### Increment 1 - Declare Modeling Dependencies

- Objective: Add a Python-compatible GPR dependency and any required numerical dependency.
- Affected code: `pyproject.toml`; dependency lock file if used.
- Dependencies: Data intake dependency decisions.
- Implementation change: Add the selected GPR/numerical packages.
- Developer tests: Package import smoke test.
- Verification: `uv run pytest`, `uv run mypy src`.
- Related story and issue: `US-0004` / `#4`

### Increment 2 - Define GPR Settings Defaults

- Objective: Provide defaults for kernel choice, length scale, noise level / alpha, prediction range, prediction point count, and confidence interval level.
- Affected code: provisional `src/gaussian_explorer/settings.py`; unit tests.
- Dependencies: None.
- Implementation change: Add a typed settings structure and default factory.
- Developer tests: Unit tests proving all approved settings are present with defaults.
- Verification: Unit tests.
- Related story and issue: `US-0003` / `#3`

### Increment 3 - Wire Editable Settings Controls

- Objective: Let the Streamlit workflow show and capture editable model settings.
- Affected code: provisional `src/gaussian_explorer/app.py`; settings module.
- Dependencies: Increment 2 and selected-variable contract from plan 001.
- Implementation change: Add Streamlit controls that produce the typed settings object.
- Developer tests: Unit tests for settings validation; focused component/integration check for changed settings flowing to fit call.
- Verification: Unit tests and manual Streamlit check.
- Related story and issue: `US-0003` / `#3`

### Increment 4 - Fit GPR and Produce Prediction Results

- Objective: Fit a model from valid selected variables and current settings.
- Affected code: provisional `src/gaussian_explorer/modeling.py`; unit tests.
- Dependencies: Increments 1-3 and validated selected data.
- Implementation change: Implement fitting and prediction over the configured prediction range and number of prediction points.
- Developer tests: Unit tests with a small deterministic dataset proving prediction arrays and uncertainty bounds are produced.
- Verification: Unit tests with numerical tolerance and type checking.
- Related story and issue: `US-0004` / `#4`

### Increment 5 - Store Fitted Result in Session State

- Objective: Make fitted results available to visualization and export components.
- Affected code: provisional `src/gaussian_explorer/app.py`; optional state helpers.
- Dependencies: Increment 4.
- Implementation change: Store fitted result in the active in-memory session after successful fitting.
- Developer tests: Focused integration test or component test for state transition after fit.
- Verification: Integration/component test and manual Streamlit check.
- Related story and issue: `US-0004` / `#4`

## Data, Interface, Migration, and Configuration Changes

- Data: settings object and fitted prediction result object in memory.
- Interface: Streamlit controls for settings and fit action.
- Migration: none.
- Configuration: modeling dependencies.

## Risks, Assumptions, and Open Questions

- Risk: selected GPR library API may shape result structures; keep the internal result object stable for downstream use.
- Risk: invalid selected data can produce misleading or failed model fits; validation plan `004-invalid-input-feedback` covers this.
- Open item: choose exact GPR dependency during implementation.

## Change Requests and Routes

- Additional kernels or fitting algorithms beyond approved settings require story review if user-visible.
- Persistent model storage requires architecture change.

## Readiness Decision

`ready-with-open-items`: implementation can begin; exact dependency choice is open but bounded by approved architecture.

## Revision History

| Version | Date | Author | Action | Upstream Versions | Notes |
|---|---|---|---|---|---|
| 1.0 | 2026-07-14 | ChatGPT | Created | story `1.0`; architecture `1.0`; technical review `TR-001`; issues `#3`, `#4`; code baseline `8ce0d69` | Initial plan for GPR settings and fitting. |
