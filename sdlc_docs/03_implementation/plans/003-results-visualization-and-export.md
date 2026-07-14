# Implementation Plan

## Current State

- Plan version: `1.0`
- Status: `ready-with-open-items`
- Repository issues: `#5`, `#6`, `#7`
- Source stories: `US-0005`, `US-0006`, `US-0007`
- Story version: `1.0`
- Architecture version: `1.0`
- Technical review: `TR-001`
- Code baseline: `8ce0d69`
- Author: `ChatGPT`
- Date: `2026-07-14`

## Scope

Implement prediction visualization, tabular prediction export, plot export, and reproducibility metadata from fitted analysis state.

Out of scope: model fitting, upload, variable selection, server-side saved sessions, and deployment automation.

## Architecture References

- Streamlit web application.
- GPR fitting and prediction.
- Prediction and uncertainty visualization.
- Export generation.
- Export download.
- In-memory analysis session.
- Export artifacts.
- `architecture-decision-001-single-streamlit-web-application`
- `architecture-decision-002-in-memory-session-and-export-reproducibility`

## Existing Code and Test Baseline

No visualization or export code exists yet. This plan depends on the fitted result contract from plan `002-model-configuration-and-fitting`.

## Implementation Approach

Use fitted result state as the single source for visualization and export:

- Provisional `gaussian_explorer.visualization` to construct the interactive plot.
- Provisional `gaussian_explorer.exports` to generate tabular CSV, plot output, and reproducibility metadata.
- Keep export metadata tied to selected variables, settings, prediction results, and plot metadata.

## Ordered Increments

### Increment 1 - Choose Visualization and Export Dependencies

- Objective: Add plotting/export dependencies compatible with Streamlit and the result contract.
- Affected code: `pyproject.toml`; dependency lock file if used.
- Dependencies: Modeling result shape from plan 002.
- Implementation change: Add selected plotting dependency and any export helper dependencies.
- Developer tests: Import smoke tests for export/visualization helpers.
- Verification: `uv run pytest`, `uv run mypy src`.
- Related story and issue: `US-0005`, `US-0007` / `#5`, `#7`

### Increment 2 - Build Prediction Visualization

- Objective: Display original data, predicted curve, and uncertainty estimates together.
- Affected code: provisional `src/gaussian_explorer/visualization.py`; Streamlit app wiring.
- Dependencies: Fitted result object from plan 002.
- Implementation change: Create a plot object/renderable representation from original selected data and fitted prediction results.
- Developer tests: Unit or component tests that plot data includes original points, predicted mean, and uncertainty bounds.
- Verification: Component tests and manual Streamlit check.
- Related story and issue: `US-0005` / `#5`

### Increment 3 - Generate Results CSV

- Objective: Export tabular prediction results.
- Affected code: provisional `src/gaussian_explorer/exports.py`; unit tests.
- Dependencies: Fitted result object from plan 002.
- Implementation change: Generate CSV bytes or text containing predicted X values, predicted mean, uncertainty bounds, selected X/Y names, and model settings.
- Developer tests: Unit test for expected columns and settings metadata.
- Verification: Unit tests.
- Related story and issue: `US-0006` / `#6`

### Increment 4 - Wire Results Download

- Objective: Let researchers download tabular results after fitting.
- Affected code: provisional `src/gaussian_explorer/app.py`; exports module.
- Dependencies: Increment 3.
- Implementation change: Add Streamlit download control enabled only when fitted results exist.
- Developer tests: Component/integration check for export availability after fit state.
- Verification: Manual Streamlit check and focused test where practical.
- Related story and issue: `US-0006` / `#6`

### Increment 5 - Generate Plot Export and Metadata

- Objective: Provide plot output and reproducibility metadata sufficient to reproduce the analysis later.
- Affected code: provisional `src/gaussian_explorer/exports.py`; visualization module; tests.
- Dependencies: Increments 2 and 3.
- Implementation change: Generate plot artifact and metadata including selected variables, settings, prediction result summary, and plot metadata.
- Developer tests: Unit tests for metadata fields and plot export availability.
- Verification: Unit tests and manual download check.
- Related story and issue: `US-0007` / `#7`

## Data, Interface, Migration, and Configuration Changes

- Data: export artifacts generated from fitted in-memory state.
- Interface: visualization display and Streamlit download controls.
- Migration: none.
- Configuration: plotting/export dependencies.

## Risks, Assumptions, and Open Questions

- Risk: reproducibility metadata can drift if not generated from the same fitted state as visualization.
- Risk: plot image export support depends on chosen plotting library and runtime dependencies.
- Open item: choose exact plot export format during implementation, within approved "plot output" scope.

## Change Requests and Routes

- Server-side saved sessions or persistent export history require product and architecture review.
- Additional export formats beyond approved outputs require story review if user-visible.

## Readiness Decision

`ready-with-open-items`: implementation can begin after the fitted result contract is available.

## Revision History

| Version | Date | Author | Action | Upstream Versions | Notes |
|---|---|---|---|---|---|
| 1.0 | 2026-07-14 | ChatGPT | Created | story `1.0`; architecture `1.0`; technical review `TR-001`; issues `#5`, `#6`, `#7`; code baseline `8ce0d69` | Initial plan for visualization and exports. |
