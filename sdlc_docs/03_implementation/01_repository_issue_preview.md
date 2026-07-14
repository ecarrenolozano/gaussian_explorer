# Repository Issue Preview

## Publication Summary

- Repository: `https://github.com/ecarrenolozano/gaussian_explorer`
- Platform: `GitHub`
- Publication batch: `publication-003`
- Documentation revision: `8ce0d69`
- Proposed issue count: `8`
- Proposed relationship writes: `0`
- Warnings: Existing issues `#1` through `#8` are linked and relationship state is already verified from `publication-002`. This preview updates only issue descriptions so each visible body matches the canonical user-story format from `sdlc_docs/01_requirements/01_user_stories.md`. No labels, milestones, assignees, issue relationships, or issue titles are proposed for change.

## Proposed Issues

### US-0001 - Upload Experimental CSV Data

- Source type: `user-story`
- Source identifier: `US-0001`
- Story version: `1.0`
- Architecture version: `1.0`
- Technical review: `TR-001`
- Labels: `enhancement`
- Milestone: None
- Assignees: None
- Dependencies: None

#### Proposed Body

## US-0001 - Upload Experimental CSV Data

<!-- story-id: US-0001 | source-batch: PRDB-001 | priority: MVP | lifecycle: active -->

### **User story**

As a `researcher`,
I need `to upload a CSV dataset for analysis`,
so that `I can begin Gaussian Process Regression from my experimental data`.

### **Source and constraints**

- Source batch: `PRDB-001 (2026-07-13)`
- Source requirement or decision: CSV upload for small experimental datasets
- Confirmed constraints: The uploaded dataset may contain multiple columns and shall be processed in memory for small experimental datasets.
- Explicit assumptions: "Small experimental datasets" can be processed in memory in the Streamlit application.
- Open questions: None

### **Acceptance criteria**

#### **Scenario: Upload a supported CSV dataset**

Given a researcher has a supported CSV file
When the researcher uploads the file
Then the application accepts the file for analysis
And makes the dataset available for variable selection.

<!-- workflow-link
source-type: user-story
source-identifier: US-0001
story-version: 1.0
architecture-version: 1.0
technical-review-identifier: TR-001
publication-batch-identifier: publication-003
documentation-revision: 8ce0d69
-->

### US-0002 - Select Regression Variables

- Source type: `user-story`
- Source identifier: `US-0002`
- Story version: `1.0`
- Architecture version: `1.0`
- Technical review: `TR-001`
- Labels: `enhancement`
- Milestone: None
- Assignees: None
- Dependencies: `US-0001`

#### Proposed Body

## US-0002 - Select Regression Variables

<!-- story-id: US-0002 | source-batch: PRDB-001 | priority: MVP | lifecycle: active -->

### **User story**

As a `researcher`,
I need `to choose the X and Y variables from numeric columns in my uploaded dataset`,
so that `I can analyze the relationship between the variables that matter for my experiment`.

### **Source and constraints**

- Source batch: `PRDB-001 (2026-07-13)`
- Source requirement or decision: Multi-column CSV with user-selected X/Y variables
- Confirmed constraints: The application shall analyze two selected variables from an uploaded dataset, even when the CSV contains more than two columns.
- Explicit assumptions: None
- Open questions: None

### **Acceptance criteria**

#### **Scenario: Select numeric X and Y variables**

Given a researcher has uploaded a CSV file with at least two numeric columns
When the researcher selects one numeric column as X and one numeric column as Y
Then the application records the selected variables for regression.

<!-- workflow-link
source-type: user-story
source-identifier: US-0002
story-version: 1.0
architecture-version: 1.0
technical-review-identifier: TR-001
publication-batch-identifier: publication-003
documentation-revision: 8ce0d69
-->

### US-0003 - Configure GPR Settings

- Source type: `user-story`
- Source identifier: `US-0003`
- Story version: `1.0`
- Architecture version: `1.0`
- Technical review: `TR-001`
- Labels: `enhancement`
- Milestone: None
- Assignees: None
- Dependencies: `US-0002`

#### Proposed Body

## US-0003 - Configure GPR Settings

<!-- story-id: US-0003 | source-batch: PRDB-001 | priority: MVP | lifecycle: active -->

### **User story**

As a `researcher`,
I need `to review and modify default Gaussian Process Regression settings before fitting`,
so that `I can run the model with settings appropriate for my analysis`.

### **Source and constraints**

- Source batch: `PRDB-001 (2026-07-13)`
- Source requirement or decision: User-editable sensible GPR defaults
- Confirmed constraints: The first version shall expose kernel choice, length scale, noise level / alpha, prediction range, number of prediction points, and confidence interval level.
- Explicit assumptions: None
- Open questions: None

### **Acceptance criteria**

#### **Scenario: Use default model settings**

Given a researcher has selected valid X and Y variables
When the researcher reviews the model settings without changing them
Then the application provides default settings for kernel choice, length scale, noise level / alpha, prediction range, number of prediction points, and confidence interval level.

#### **Scenario: Modify model settings before fitting**

Given a researcher has selected valid X and Y variables
When the researcher changes any exposed GPR setting before fitting
Then the application uses the changed setting for the analysis.

<!-- workflow-link
source-type: user-story
source-identifier: US-0003
story-version: 1.0
architecture-version: 1.0
technical-review-identifier: TR-001
publication-batch-identifier: publication-003
documentation-revision: 8ce0d69
-->

### US-0004 - Fit the Gaussian Process Regression Model

- Source type: `user-story`
- Source identifier: `US-0004`
- Story version: `1.0`
- Architecture version: `1.0`
- Technical review: `TR-001`
- Labels: `enhancement`
- Milestone: None
- Assignees: None
- Dependencies: `US-0001`, `US-0002`, `US-0003`

#### Proposed Body

## US-0004 - Fit the Gaussian Process Regression Model

<!-- story-id: US-0004 | source-batch: PRDB-001 | priority: MVP | lifecycle: active -->

### **User story**

As a `researcher`,
I need `to fit a Gaussian Process Regression model to my selected variables`,
so that `I can estimate the underlying function represented by my data`.

### **Source and constraints**

- Source batch: `PRDB-001 (2026-07-13)`
- Source requirement or decision: Fit GPR model for selected variables
- Confirmed constraints: The application shall support Gaussian Process Regression for small experimental datasets.
- Explicit assumptions: "Small experimental datasets" can be processed in memory in the Streamlit application.
- Open questions: None

### **Acceptance criteria**

#### **Scenario: Fit a model from valid analysis inputs**

Given a researcher has uploaded a valid dataset, selected valid X and Y variables, and reviewed the GPR settings
When the researcher fits the model
Then the application produces GPR prediction results for the selected variables.

<!-- workflow-link
source-type: user-story
source-identifier: US-0004
story-version: 1.0
architecture-version: 1.0
technical-review-identifier: TR-001
publication-batch-identifier: publication-003
documentation-revision: 8ce0d69
-->

### US-0005 - View Prediction and Uncertainty

- Source type: `user-story`
- Source identifier: `US-0005`
- Story version: `1.0`
- Architecture version: `1.0`
- Technical review: `TR-001`
- Labels: `enhancement`
- Milestone: None
- Assignees: None
- Dependencies: `US-0004`

#### Proposed Body

## US-0005 - View Prediction and Uncertainty

<!-- story-id: US-0005 | source-batch: PRDB-001 | priority: MVP | lifecycle: active -->

### **User story**

As a `researcher`,
I need `to view the original data, predicted curve, and uncertainty estimates together`,
so that `I can interpret the model prediction and its confidence`.

### **Source and constraints**

- Source batch: `PRDB-001 (2026-07-13)`
- Source requirement or decision: Interactive prediction and uncertainty visualization
- Confirmed constraints: The visualization shall show original data, predicted curve, and uncertainty estimates.
- Explicit assumptions: None
- Open questions: None

### **Acceptance criteria**

#### **Scenario: Display model prediction with uncertainty**

Given a researcher has fitted a GPR model
When prediction results are available
Then the application displays an interactive visualization containing the original data, predicted curve, and uncertainty estimates.

<!-- workflow-link
source-type: user-story
source-identifier: US-0005
story-version: 1.0
architecture-version: 1.0
technical-review-identifier: TR-001
publication-batch-identifier: publication-003
documentation-revision: 8ce0d69
-->

### US-0006 - Export Tabular Prediction Results

- Source type: `user-story`
- Source identifier: `US-0006`
- Story version: `1.0`
- Architecture version: `1.0`
- Technical review: `TR-001`
- Labels: `enhancement`
- Milestone: None
- Assignees: None
- Dependencies: `US-0004`

#### Proposed Body

## US-0006 - Export Tabular Prediction Results

<!-- story-id: US-0006 | source-batch: PRDB-001 | priority: MVP | lifecycle: active -->

### **User story**

As a `researcher`,
I need `to export tabular prediction results`,
so that `I can use the model outputs outside the application`.

### **Source and constraints**

- Source batch: `PRDB-001 (2026-07-13)`
- Source requirement or decision: Results CSV export
- Confirmed constraints: The tabular export shall include predicted X values, predicted mean, uncertainty bounds, selected X/Y column names, and model settings.
- Explicit assumptions: Reproducibility can be satisfied through exported settings, selected variables, prediction results, and plot metadata rather than server-side saved sessions.
- Open questions: None

### **Acceptance criteria**

#### **Scenario: Export prediction results**

Given a researcher has fitted a GPR model
When the researcher exports tabular results
Then the application provides a results CSV containing predicted X values, predicted mean, uncertainty bounds, selected X/Y column names, and model settings.

<!-- workflow-link
source-type: user-story
source-identifier: US-0006
story-version: 1.0
architecture-version: 1.0
technical-review-identifier: TR-001
publication-batch-identifier: publication-003
documentation-revision: 8ce0d69
-->

### US-0007 - Export Plot and Reproducibility Metadata

- Source type: `user-story`
- Source identifier: `US-0007`
- Story version: `1.0`
- Architecture version: `1.0`
- Technical review: `TR-001`
- Labels: `enhancement`
- Milestone: None
- Assignees: None
- Dependencies: `US-0004`, `US-0005`

#### Proposed Body

## US-0007 - Export Plot and Reproducibility Metadata

<!-- story-id: US-0007 | source-batch: PRDB-001 | priority: MVP | lifecycle: active -->

### **User story**

As a `researcher`,
I need `to export the plot and reproducibility metadata`,
so that `I can document and reproduce my analysis later`.

### **Source and constraints**

- Source batch: `PRDB-001 (2026-07-13)`
- Source requirement or decision: Visual and reproducibility export
- Confirmed constraints: The visual/reproducibility export shall include the plot and enough metadata to reproduce the analysis later.
- Explicit assumptions: Reproducibility can be satisfied through exported settings, selected variables, prediction results, and plot metadata rather than server-side saved sessions.
- Open questions: None

### **Acceptance criteria**

#### **Scenario: Export visual and reproducibility materials**

Given a researcher has fitted a GPR model and viewed the visualization
When the researcher exports visual and reproducibility materials
Then the application provides the plot and metadata sufficient to reproduce the analysis later.

<!-- workflow-link
source-type: user-story
source-identifier: US-0007
story-version: 1.0
architecture-version: 1.0
technical-review-identifier: TR-001
publication-batch-identifier: publication-003
documentation-revision: 8ce0d69
-->

### US-0008 - Receive Clear Invalid-Input Feedback

- Source type: `user-story`
- Source identifier: `US-0008`
- Story version: `1.0`
- Architecture version: `1.0`
- Technical review: `TR-001`
- Labels: `enhancement`
- Milestone: None
- Assignees: None
- Dependencies: `US-0001`, `US-0002`, `US-0004`

#### Proposed Body

## US-0008 - Receive Clear Invalid-Input Feedback

<!-- story-id: US-0008 | source-batch: PRDB-001 | priority: MVP | lifecycle: active -->

### **User story**

As a `researcher`,
I need `the application to clearly handle invalid inputs`,
so that `I can correct data problems before relying on an analysis`.

### **Source and constraints**

- Source batch: `PRDB-001 (2026-07-13)`
- Source requirement or decision: Explicit invalid-input handling
- Confirmed constraints: The first version shall explicitly handle malformed CSV, no numeric columns, fewer than two selectable numeric columns, missing values in selected columns, too few rows, duplicate X values, and unsupported or very large files.
- Explicit assumptions: None
- Open questions: None

### **Acceptance criteria**

#### **Scenario: Reject an unusable uploaded file**

Given a researcher uploads a malformed CSV, unsupported file, or very large file
When the application validates the upload
Then the application prevents analysis from proceeding
And explains the invalid-input problem.

#### **Scenario: Reject a dataset without selectable regression variables**

Given a researcher uploads a CSV file with no numeric columns or fewer than two selectable numeric columns
When the application validates available columns
Then the application prevents variable selection from proceeding
And explains why the dataset cannot be used for regression.

#### **Scenario: Reject invalid selected data**

Given a researcher has selected X and Y columns with missing values, too few rows, or duplicate X values
When the application validates the selected data for fitting
Then the application prevents model fitting from proceeding
And explains the data issue that must be corrected.

<!-- workflow-link
source-type: user-story
source-identifier: US-0008
story-version: 1.0
architecture-version: 1.0
technical-review-identifier: TR-001
publication-batch-identifier: publication-003
documentation-revision: 8ce0d69
-->

## Proposed Issue Relationships

No relationship writes are proposed. Current `publication-002` relationships remain verified:

| Parent Issue | Child Issue | Relationship Type | Platform Representation | Planned Write | Fallback or Warning |
|---|---|---|---|---|---|
| `#4` / `US-0004` | `#1` / `US-0001` | sub-issue | GitHub sub-issue | None | Already verified in `publication-002`. |
| `#4` / `US-0004` | `#2` / `US-0002` | sub-issue | GitHub sub-issue | None | Already verified in `publication-002`. |
| `#4` / `US-0004` | `#3` / `US-0003` | sub-issue | GitHub sub-issue | None | Already verified in `publication-002`. |
| `#5` / `US-0005` | `#4` / `US-0004` | sub-issue | GitHub sub-issue | None | Already verified in `publication-002`. |
| `#7` / `US-0007` | `#5` / `US-0005` | sub-issue | GitHub sub-issue | None | Already verified in `publication-002`. |
| `#2` / `US-0002` | `#1` / `US-0001` | dependency | GitHub blocked-by | None | Already verified in `publication-002`. |
| `#3` / `US-0003` | `#2` / `US-0002` | dependency | GitHub blocked-by | None | Already verified in `publication-002`. |
| `#6` / `US-0006` | `#4` / `US-0004` | dependency | GitHub blocked-by | None | Already verified in `publication-002`. |
| `#7` / `US-0007` | `#4` / `US-0004` | dependency | GitHub blocked-by | None | Already verified in `publication-002`. |
| `#8` / `US-0008` | `#1`, `#2`, `#4` / `US-0001`, `US-0002`, `US-0004` | dependency | GitHub blocked-by | None | Already verified in `publication-002`. |

## Delivery Plan

### Priority Order

| Priority | Issue | Why This Priority | Unblocks |
|---|---|---|---|
| 1 | `#1` / `US-0001` | Establishes uploaded dataset state and validation entry point. | `US-0002`, `US-0004`, `US-0008` |
| 2 | `#2` / `US-0002` | Captures selected X/Y variables needed for fitting. | `US-0003`, `US-0004`, `US-0008` |
| 3 | `#3` / `US-0003` | Defines model settings contract before fitting. | `US-0004` |
| 4 | `#4` / `US-0004` | Central integration issue for upload, variables, settings, and prediction results. | `US-0005`, `US-0006`, `US-0007`, `US-0008` |
| 5 | `#5` / `US-0005` | Creates visualization state needed by plot/reproducibility export. | `US-0007` |
| 6 | `#6` / `US-0006` | Independent tabular export once fitted results exist. | External result use |
| 7 | `#8` / `US-0008` | Cross-cutting validation should be threaded through upload, selection, and fitting. | Release confidence across intake and fitting |
| 8 | `#7` / `US-0007` | Final reproducibility export depends on fitted results and visualization state. | MVP completion |

### Parallelization Groups

| Group | Issues | Start Condition | Notes |
|---|---|---|---|
| 1 | `US-0001` | Start immediately. | Foundation for the rest of the workflow. |
| 2 | `US-0002`, `US-0003` | `US-0001` interface is stable enough for selection/settings integration. | `US-0003` can begin control design early, then bind to selected variables. |
| 3 | `US-0004` | `US-0001`, `US-0002`, and `US-0003` contracts are available. | Treat as integration-critical. |
| 4 | `US-0005`, `US-0006`, `US-0008` | `US-0004` produces fitted prediction results and validation hooks. | Visualization, tabular export, and validation can progress in parallel. |
| 5 | `US-0007` | `US-0004` and `US-0005` outputs are available. | Final export/reproducibility work. |

### Kanban Guidance

| Board Focus | Issues | Handoff or Checkpoint |
|---|---|---|
| Data intake path | `US-0001`, `US-0002` | Dataset state and selected variable contract are ready for fitting. |
| Model integration path | `US-0003`, `US-0004` | Settings and fitted prediction result contract are ready for consumers. |
| Results path | `US-0005`, `US-0006`, `US-0007` | Visualization/export outputs are ready for validation. |
| Cross-cutting validation | `US-0008` | Invalid upload, selection, and fitting cases are covered before release. |

## Approval

- [x] Exact preview approved for publication

Approved by: `Edwin Carreno`
Approval date: `2026-07-14`
Approval scope: `publication-003` body updates for issues `#1` through `#8`
