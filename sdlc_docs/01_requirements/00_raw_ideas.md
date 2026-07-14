# Raw Ideas

## Date: 2026-07-13
<!-- batch-id: PRDB-001 | status: processed | date: 2026-07-13 -->


Hi Edwin,

Could you develop a Streamlit application for analysing small experimental datasets with Gaussian Process Regression?

Researchers should be able to upload data, choose the variables, fit the model, and view the prediction together with its uncertainty. They should also be able to export the results and reproduce the analysis later.

Please use sensible defaults, handle invalid inputs properly, and keep the code modular enough to extend in the future.

Best,
Professor Charles Xavier

### Clarified Requirements Handoff

#### Original Requester Intent

Professor Charles Xavier requested a Streamlit application that helps researchers analyze small experimental datasets using Gaussian Process Regression, with upload, variable selection, model fitting, uncertainty visualization, export, reproducibility, sensible defaults, invalid-input handling, and modular code.

#### Confirmed Requirements

- The application shall be built with Streamlit.
- The application shall support Gaussian Process Regression for small experimental datasets.
- Researchers shall be able to upload CSV data.
- Researchers shall be able to choose the variables used for regression.
- Researchers shall be able to fit the model.
- The application shall show the prediction together with uncertainty.
- The application shall provide sensible default model settings.
- The application shall handle invalid inputs properly.
- The code shall be modular enough to support future extension.

#### Clarified Decisions

- The application shall accept CSV files with multiple columns and allow the user to select the X and Y variables for analysis.
- The export shall include both tabular results and visual/reproducibility materials.
- The tabular export shall include predicted X values, predicted mean, uncertainty bounds, selected X/Y column names, and model settings.
- The visual/reproducibility export shall include the plot and enough metadata to reproduce the analysis later.
- Users shall be able to modify the default Gaussian Process Regression settings before fitting the model.
- The first version shall expose these configurable GPR settings: kernel choice, length scale, noise level / alpha, prediction range, number of prediction points, and confidence interval level.
- The first version shall explicitly handle these invalid-input cases: malformed CSV, no numeric columns, fewer than two selectable numeric columns, missing values in selected columns, too few rows, duplicate X values, and unsupported or very large files.

#### Open Questions

None.

#### Scope Boundaries

- In scope: Streamlit interface, CSV upload, multi-column variable selection, GPR fitting, interactive visualization, configurable basic GPR settings, result export, plot export, reproducibility metadata, and explicit invalid-input handling.
- In scope: Analysis of two selected variables from an uploaded dataset, even when the CSV contains more than two columns.
- Out of scope unless later requested: user accounts, server-side persistence of past analyses, collaborative workflows, database storage, batch processing, and deployment automation.

#### Project

Gaussian Process Regression Web Application.

#### Source Material

- `sdlc_docs/00_project_context/project_context.md`
- Original request in this 2026-07-13 raw-ideas batch.
- Clarification responses from the user: multi-column CSV with selectable X/Y variables; export includes both tabular and visual/reproducibility materials; defaults are user-editable; all listed basic GPR settings are included; all listed invalid-input cases are included.

#### Explicit Assumptions

- "Small experimental datasets" can be processed in memory in the Streamlit application.
- Reproducibility can be satisfied through exported settings, selected variables, prediction results, and plot metadata rather than server-side saved sessions.

#### Important Terminology

- CSV: Comma-Separated Values file used for tabular data.
- Gaussian Process Regression (GPR): A probabilistic regression technique that predicts a function together with an estimate of prediction uncertainty.
- Uncertainty bounds: User-visible interval estimates derived from model uncertainty for the predicted curve.

#### Inputs

- Uploaded CSV file.
- User-selected X and Y columns from numeric columns in the uploaded dataset.
- User-configurable GPR settings: kernel choice, length scale, noise level / alpha, prediction range, number of prediction points, and confidence interval level.

#### Outputs

- Interactive visualization of original data, predicted curve, and uncertainty estimates.
- Results CSV containing predicted X values, predicted mean, uncertainty bounds, selected X/Y column names, and model settings.
- Plot export.
- Reproducibility metadata sufficient to reproduce the analysis later.

#### User Workflows

- A researcher uploads a CSV file.
- The application validates the file and available columns.
- The researcher selects X and Y variables.
- The researcher reviews or modifies default GPR settings.
- The researcher fits the model.
- The application displays the prediction and uncertainty visualization.
- The researcher exports tabular results, plot, and reproducibility metadata.

#### Edge Cases and Error Handling

- Malformed CSV.
- No numeric columns.
- Fewer than two selectable numeric columns.
- Missing values in selected columns.
- Too few rows to fit the model reliably.
- Duplicate X values.
- Unsupported or very large files.

#### Non-Functional Requirements

- The application should use sensible defaults for basic GPR settings.
- The application should provide clear invalid-input handling.
- The code should be modular enough to extend in the future.

#### Readiness for User Story Generation

- [x] Ready
- [ ] Partially ready
- [ ] Not ready

| Criterion | Score | Evidence or remaining gap |
|---|---:|---|
| User or stakeholder goal | 5 | Goal is explicit: help researchers analyze small experimental datasets with GPR. |
| Target users or roles | 5 | Researchers are explicitly identified; project context also identifies scientists and end users. |
| Main input and output expectations | 5 | CSV upload, variable selection, predictions, uncertainty, result export, plot export, and reproducibility metadata are confirmed. |
| Main workflow and expected behavior | 5 | Upload, validate, choose variables, configure defaults, fit model, view visualization, and export are confirmed. |
| Scope boundaries | 4 | Core inclusions are clear; exclusions are recorded for persistence, accounts, batch processing, and deployment automation. |
| Important constraints and dependencies | 4 | Streamlit, CSV input, configurable GPR settings, and modularity are confirmed; deployment environment remains unspecified but is not blocking. |
| Major edge cases or invalid states | 5 | Required invalid-input cases are explicitly confirmed. |
| Acceptance-level expectations | 4 | Expected user-visible outcomes are clear enough for story generation; detailed acceptance criteria should be created in the next stage. |
| **Overall average** | 4.6 | Ready; no blocking contradictions remain. |

### Notes for Downstream User-Story Generation

User-story generation should proceed. The core user goal, target users, inputs, outputs, workflow, configurable GPR settings, export expectations, reproducibility expectations, and invalid-input cases are confirmed. The prior tension between "two-column CSV" and "choose variables" has been resolved: the app accepts multi-column CSV files and analyzes two user-selected variables. Remaining details such as exact UI layout, exact export file formats, and deployment choices can be refined during user-story, architecture, or implementation-planning work.
