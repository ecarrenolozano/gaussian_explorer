# User Stories

## Document Status

- Current version: `1.0`
- Status: `Approved`
- Last updated: `2026-07-14`

## MVP

### Feature: Dataset Intake and Variable Selection

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

### Feature: Model Configuration and Fitting

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

### Feature: Prediction Visualization

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

### Feature: Result Export and Reproducibility

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

### Feature: Input Validation and Error Handling

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

## Post-MVP

No stories generated for this version.

## Deferred

No stories generated for this version.

## Unconfirmed Priority

No stories generated for this version.

## Open Questions

PRDB-001: None.

## Source Batch Registry

<!-- story-batch: PRDB-001 | status: generated | story-ids: US-0001,US-0002,US-0003,US-0004,US-0005,US-0006,US-0007,US-0008 | document-version: 1.0 -->

## Revision History

| Version | Date | Author | Action | Source Batches | Notes |
|---|---|---|---|---|---|
| 1.0 | 2026-07-14 | ChatGPT | Generated | PRDB-001 | Initial user stories; status reset to Draft. |
| 1.0 | 2026-07-14 | Edwin Carreno | Approved | PRDB-001 | Approved for downstream planning. |
