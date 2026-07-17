# User Stories — Inference and Fitted-Model Reuse

## Document Status

- Current version: `1.0`
- Status: `Draft`
- Last updated: `2026-07-17`
- Source batch: `PRDB-002`
- Extends: `PRDB-001`

## MVP

### Feature: Interactive Inference

## US-0009 - Predict a Single New Input

<!-- story-id: US-0009 | source-batch: PRDB-002 | priority: MVP | lifecycle: active -->

### **User story**

As a `researcher`,
I need `to enter a new X value after fitting a Gaussian Process model`,
so that `I can obtain a predicted Y value and quantify its uncertainty`.

### **Source and constraints**

- Source batch: `PRDB-002 (2026-07-17)`
- Source requirement or decision: Use the fitted Gaussian Process as a reusable inference machine.
- Confirmed constraints: The application shall reuse the current fitted model and shall not refit it when only the inference X value changes.
- Explicit assumptions: The inference input uses the same units and preprocessing conventions as the selected training X variable.
- Open questions: Whether future versions should expose both latent-function and future-observation uncertainty.

### **Acceptance criteria**

#### **Scenario: Predict one new value**

Given a researcher has fitted a Gaussian Process model
When the researcher enters one finite numeric X value and requests a prediction
Then the application returns the predicted mean
And returns the predictive standard deviation
And returns lower and upper bounds for the configured confidence level
And identifies the input as IID or OOD relative to the observed training X domain.

#### **Scenario: Prevent inference before fitting**

Given no Gaussian Process model has been fitted
When the researcher attempts to run inference
Then the application prevents the prediction
And explains that a model must be fitted first.

---

## US-0010 - Predict Multiple New Inputs

<!-- story-id: US-0010 | source-batch: PRDB-002 | priority: MVP | lifecycle: active -->

### **User story**

As a `researcher`,
I need `to predict multiple new X values in one operation`,
so that `I can apply the fitted model to a set of experimental conditions efficiently`.

### **Source and constraints**

- Source batch: `PRDB-002 (2026-07-17)`
- Source requirement or decision: Support batch inference without retraining.
- Confirmed constraints: The first version shall accept a list of numeric X values entered as comma-, space-, or line-separated text.
- Explicit assumptions: The same fitted model and confidence level apply to every supplied value.
- Open questions: Whether a later version should accept a separate inference CSV file with additional identifier columns.

### **Acceptance criteria**

#### **Scenario: Predict a batch of valid values**

Given a researcher has fitted a Gaussian Process model
When the researcher supplies multiple finite numeric X values
Then the application predicts each value using the existing fitted model
And displays the input, predicted mean, predictive standard deviation, uncertainty bounds, confidence level, and IID/OOD region for every result.

#### **Scenario: Reject invalid batch input**

Given a researcher has fitted a Gaussian Process model
When the supplied batch contains a missing, malformed, or non-finite value
Then the application prevents batch inference
And explains how the input must be corrected.

---

## US-0011 - Export Inference Results

<!-- story-id: US-0011 | source-batch: PRDB-002 | priority: MVP | lifecycle: active -->

### **User story**

As a `researcher`,
I need `to export predictions generated for new input values`,
so that `I can use the inferred values and uncertainty estimates outside the application`.

### **Source and constraints**

- Source batch: `PRDB-002 (2026-07-17)`
- Source requirement or decision: Inference results shall be portable and auditable.
- Confirmed constraints: The export shall be a UTF-8 CSV generated only after inference has been run.
- Explicit assumptions: The configured confidence level is common to all rows in one export.
- Open questions: None.

### **Acceptance criteria**

#### **Scenario: Export batch inference results**

Given the researcher has generated one or more inference results
When the researcher downloads the inference results
Then the application provides a CSV containing X, predicted mean, predictive standard deviation, lower bound, upper bound, confidence level, and IID/OOD region.

#### **Scenario: Prevent empty inference export**

Given no inference results are available
When the researcher attempts to export inference results
Then the application prevents the export
And explains that inference must be run first.

### Feature: Fitted-Model Persistence

## US-0012 - Export the Fitted Gaussian Process Model

<!-- story-id: US-0012 | source-batch: PRDB-002 | priority: MVP | lifecycle: active -->

### **User story**

As a `researcher`,
I need `to download the fitted Gaussian Process as a reusable model artifact`,
so that `I can make predictions later without repeating model fitting`.

### **Source and constraints**

- Source batch: `PRDB-002 (2026-07-17)`
- Source requirement or decision: Persist the complete inference machine rather than only its plotted prediction table.
- Confirmed constraints: The artifact shall contain the fitted scikit-learn estimator and the metadata needed to interpret new predictions.
- Explicit assumptions: The artifact is intended for trusted Python environments with compatible package versions.
- Open questions: Whether a non-pickle interchange format will be required in a future release.

### **Acceptance criteria**

#### **Scenario: Download a fitted model artifact**

Given a researcher has successfully fitted a Gaussian Process model
When the researcher downloads the fitted model
Then the application provides a versioned `.joblib` artifact
And the artifact contains the fitted estimator
And the selected X and Y variables
And the observed training X domain
And the configured confidence level
And the initial and fitted kernel descriptions
And the source dataset hash
And the relevant Python and scientific-library versions.

#### **Scenario: Prevent model export before fitting**

Given no Gaussian Process model has been fitted
When the researcher attempts to download a fitted model
Then the application prevents the download
And explains that a model must be fitted first.

---

## US-0013 - Reuse a Trusted Fitted Model Artifact

<!-- story-id: US-0013 | source-batch: PRDB-002 | priority: MVP | lifecycle: active -->

### **User story**

As a `research software developer`,
I need `to load a previously exported Gaussian Process artifact in Python`,
so that `the fitted model can be reused as an inference machine in another trusted workflow`.

### **Source and constraints**

- Source batch: `PRDB-002 (2026-07-17)`
- Source requirement or decision: Provide a package-level persistence API in addition to the application download control.
- Confirmed constraints: The loader shall validate the artifact type and format version before returning it.
- Explicit assumptions: Only trusted artifacts may be loaded because joblib uses pickle-based serialization.
- Open questions: Whether loading artifacts directly through the graphical application belongs in MVP or a later release.

### **Acceptance criteria**

#### **Scenario: Load and use a compatible artifact**

Given a trusted artifact was created by a compatible version of the package
When a developer loads the artifact through the package persistence API
Then the package returns a Gaussian Process artifact
And the artifact can predict one or multiple new X values
And the returned results contain predictive uncertainty and IID/OOD classification.

#### **Scenario: Reject an incompatible artifact**

Given a file is not a Gaussian Process artifact or uses an unsupported format version
When a developer attempts to load it
Then the package rejects the file
And reports that the artifact is invalid or incompatible.

## Post-MVP

- Graphical upload of a previously exported fitted model.
- Batch inference from a dedicated CSV file with preserved identifier columns.
- Separate latent-function and future-observation uncertainty outputs.
- A non-pickle model interchange option when deployment requirements justify it.

## Deferred

No stories deferred for this batch.

## Unconfirmed Priority

No stories with unconfirmed priority for this batch.

## Open Questions

- Should the graphical application support loading model artifacts in the MVP?
- Should predictive uncertainty represent the latent function, a future noisy observation, or both?
- Is a portable non-pickle interchange format required for external deployment?

## Source Batch Registry

<!-- story-batch: PRDB-002 | status: generated | story-ids: US-0009,US-0010,US-0011,US-0012,US-0013 | document-version: 1.0 -->

## Revision History

| Version | Date | Author | Action | Source Batches | Notes |
|---|---|---|---|---|---|
| 1.0 | 2026-07-17 | ChatGPT | Generated | PRDB-002 | Adds single and batch inference, inference export, fitted-model export, and trusted model reuse. |
