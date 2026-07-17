# Gaussian Process Regression Explorer — User Stories

## Document Status

- Current version: `2.0`
- Status: `Draft`
- Last updated: `2026-07-17`
- Purpose: Improved user-story set derived from the original informal requirement and lessons learned during implementation.

---

# Discovery and Technical Decisions

These items are not user stories, but they should be resolved before or during implementation.

## DI-0001 — Evaluate the Application Framework

### Decision

Select the most appropriate Python framework for the interactive scientific application.

### Candidate options

- Streamlit
- Panel
- Another justified Python framework

### Evaluation criteria

- Dynamic controls for covariance-function-specific parameters
- Reliable Plotly integration
- Application-state management
- Long-running model fitting
- File uploads and downloads
- Fitted-model export
- Testability
- Modularity
- Deployment requirements
- Future extensibility

### Expected output

A short architecture decision record documenting:

- selected framework;
- alternatives considered;
- evaluation criteria;
- rationale;
- known consequences.

---

## DI-0002 — Define the Meaning of Reproducibility

Determine whether “reproduce the analysis later” means:

- exporting settings and predictions;
- recreating the same figure;
- saving the fitted estimator;
- loading the estimator without retraining;
- restoring the complete UI state.

Recommended interpretation for this project:

> Export predictions, metadata, plot, and a reusable fitted-model artifact.

---

## DI-0003 — Define Supported Covariance Functions

Confirm the initial covariance functions and terminology.

Recommended initial set:

- Squared Exponential
- Matérn
- Rational Quadratic

Future candidates:

- Periodic
- Linear
- Covariance-function composition

---

# MVP User Stories

## Feature: Dataset Intake

## US-0001 — Upload Experimental CSV Data

### User story

As a researcher,  
I need to upload a CSV dataset,  
so that I can analyse my experimental observations.

### Acceptance criteria

#### Scenario: Upload a valid CSV

Given the researcher selects a supported CSV file  
When the file is uploaded  
Then the application reads the data in memory  
And displays the filename, number of rows, and number of columns  
And makes the dataset available for variable selection.

#### Scenario: Replace an uploaded dataset

Given a dataset is already loaded  
When the researcher uploads a different valid CSV file  
Then the previous analysis state is cleared  
And the new dataset becomes the active dataset.

---

## US-0002 — Preview the Uploaded Dataset

### User story

As a researcher,  
I need to preview the uploaded observations,  
so that I can verify that the file was interpreted correctly.

### Acceptance criteria

Given a valid CSV is loaded  
When the dataset preview is displayed  
Then the researcher can inspect column names and representative rows  
And the preview does not modify the uploaded data.

---

## Feature: Variable Selection

## US-0003 — Select Regression Variables

### User story

As a researcher,  
I need to select numeric X and Y variables,  
so that I can define the relationship to model.

### Acceptance criteria

Given a CSV contains at least two numeric columns  
When the researcher selects one column as X and another as Y  
Then the application records the selected variables  
And prevents the same column from being used as both X and Y.

---

## US-0004 — Validate Selected Observations

### User story

As a researcher,  
I need the selected observations to be validated before fitting,  
so that I do not rely on an invalid regression result.

### Acceptance criteria

The application must prevent fitting and explain the problem when:

- selected values contain missing or non-finite values;
- fewer than the required number of valid observations remain;
- X and Y have different lengths;
- duplicate X values are unsupported by the selected workflow;
- the file exceeds the configured size limit.

The application must not silently remove or modify observations.

---

## Feature: Covariance-Function Configuration

## US-0005 — Select a Covariance Function

### User story

As a researcher,  
I need to select a covariance function,  
so that I can express assumptions about the behaviour of the unknown function.

### Acceptance criteria

Given valid X and Y variables are selected  
When the researcher opens the covariance-function selector  
Then the application displays the supported covariance functions  
And selecting one updates the visible hyperparameter controls.

The user-facing terminology must use **covariance function**, while implementation-specific names may remain internal.

---

## US-0006 — Configure Common Hyperparameters

### User story

As a researcher,  
I need to configure the common Gaussian Process hyperparameters,  
so that the model reflects the scale and variability of my data.

### Acceptance criteria

For every supported covariance function, the application displays the controls in this order:

1. Characteristic length-scale \(\ell\)
2. Signal standard deviation \(\sigma_f\)
3. Noise standard deviation \(\sigma_n\)

The researcher enters \(\sigma_f\) and \(\sigma_n\), not their squared values.

The application internally uses:

\[
\sigma_f^2
\]

as the signal variance and:

\[
\sigma_n^2
\]

as the noise level in:

\[
K+\sigma_n^2I
\]

All values must be positive and finite.

---

## US-0007 — Configure Matérn-Specific Parameters

### User story

As a researcher,  
I need to configure the Matérn smoothness parameter,  
so that I can control the assumed smoothness of the function.

### Acceptance criteria

Given the Matérn covariance function is selected  
Then the application displays the smoothness parameter \(\nu\).

Supported values initially include:

- \(1/2\)
- \(3/2\)
- \(5/2\)

When another covariance function is selected  
Then the Matérn-specific control is hidden.

---

## US-0008 — Configure Rational Quadratic Parameters

### User story

As a researcher,  
I need to configure the Rational Quadratic parameter \(\alpha\),  
so that I can control its mixture of characteristic length scales.

### Acceptance criteria

Given Rational Quadratic is selected  
Then the application displays the Rational Quadratic parameter \(\alpha\).

The interface must not confuse this parameter with:

- observation noise;
- `GaussianProcessRegressor.alpha`;
- numerical jitter.

When another covariance function is selected  
Then this control is hidden.

---

## Feature: Model Fitting

## US-0009 — Fit Using Fixed Hyperparameters

### User story

As a researcher,  
I need to fit the model using the values I entered,  
so that I can evaluate a specific Gaussian Process configuration.

### Acceptance criteria

Given hyperparameter optimization is disabled  
When the model is fitted  
Then the application uses the user-entered values without changing them  
And the plot displays predictions from that fixed configuration  
And the hyperparameter boxes continue to display the user-entered values.

---

## US-0010 — Optimize Supported Hyperparameters

### User story

As a researcher,  
I need the application to optimize supported hyperparameters,  
so that I can obtain values that better explain the observations.

### Acceptance criteria

Given optimization is enabled  
When the model is fitted  
Then scikit-learn optimizes all non-fixed kernel hyperparameters within defined finite bounds  
And selects the result with the highest log marginal likelihood among the optimization runs  
And the plot uses the fitted model.

The application must clearly identify which parameters were optimized and which remained fixed.

In the current implementation:

- \(\ell\) may be optimized;
- \(\sigma_f\) may be optimized;
- Rational Quadratic \(\alpha\) may be optimized;
- Matérn \(\nu\) remains fixed;
- \(\sigma_n\) remains fixed when implemented through `GaussianProcessRegressor.alpha`.

---

## US-0011 — Toggle Between Optimized and Manual Fits

### User story

As a researcher,  
I need to switch between optimized and manually configured fits,  
so that I can compare their effects on the prediction.

### Acceptance criteria

#### Scenario: Enable optimization

Given the researcher has entered manual hyperparameters  
When optimization is enabled  
Then the application fits an optimized model  
And updates the plot  
And displays the effective optimized values in the hyperparameter boxes.

#### Scenario: Disable optimization

Given an optimized model is displayed  
When optimization is disabled  
Then the application restores the last values explicitly entered by the researcher  
And refits the model without optimization  
And updates the plot  
And displays the manual values in the boxes.

Switching modes must not permanently overwrite the stored manual values.

---

## US-0012 — Configure Optimizer Restarts

### User story

As a researcher,  
I need to configure optimizer restarts,  
so that I can balance fitting speed and the likelihood of finding a better solution.

### Acceptance criteria

Given optimization is enabled  
When the researcher sets the restart count  
Then the application performs the initial optimization plus the selected number of additional starts  
And retains the solution with the best log marginal likelihood.

Given optimization is disabled  
Then optimizer restarts have no effect  
And the control is disabled or clearly marked as inactive.

---

## US-0013 — Normalize the Target Internally

### User story

As a researcher,  
I need the option to normalize the target before fitting,  
so that I can model variation around the observed target level.

### Acceptance criteria

Given target normalization is enabled  
When the model is fitted  
Then the target is normalized internally  
And predictions are returned in the original Y units  
And the uploaded dataset remains unchanged.

The interface must explain what normalization does.

---

## US-0014 — Display Model-Fitting Status

### User story

As a researcher,  
I need to know the current model state,  
so that I can determine whether the displayed results correspond to the current settings.

### Acceptance criteria

The application communicates these states:

- Not fitted
- Fitting or optimizing
- Fit successful
- Fit failed
- Settings changed — refit required

When live update is disabled and a fitting setting changes  
Then exports and inference based on the previous model are marked stale or disabled.

---

## Feature: Prediction Configuration

## US-0015 — Configure the Prediction Domain

### User story

As a researcher,  
I need to select the prediction range and resolution,  
so that I can inspect interpolation and extrapolation over a useful domain.

### Acceptance criteria

The researcher can configure:

- prediction minimum;
- prediction maximum;
- number of prediction points.

The application validates that:

- minimum is less than maximum;
- the number of points is within supported limits.

These settings affect prediction and visualization, but not covariance hyperparameter optimization.

---

## US-0016 — Configure the Uncertainty Level

### User story

As a researcher,  
I need to select the uncertainty level,  
so that I can view lower and upper bounds appropriate for my analysis.

### Acceptance criteria

Given a confidence or predictive interval probability is selected  
When predictions are calculated  
Then the application computes corresponding lower and upper bounds  
And updates the plot and exported results.

The application must consistently use one term, such as:

> Predictive interval probability

or clearly document what “confidence level” means in the implementation.

---

## Feature: Visualization

## US-0017 — View Observations, Prediction, and Uncertainty

### User story

As a researcher,  
I need to view observations, the predictive mean, and uncertainty together,  
so that I can interpret the fitted model.

### Acceptance criteria

Given a successful fit  
Then the plot displays:

- observed data;
- predictive mean;
- lower uncertainty bound;
- upper uncertainty bound;
- shaded uncertainty region.

The user can show or hide observations and uncertainty.

---

## US-0018 — Distinguish IID and OOD Regions

### User story

As a researcher,  
I need interpolation and extrapolation regions to be identified,  
so that I can interpret predictions outside the observed input domain cautiously.

### Acceptance criteria

The application defines:

\[
\min(X_{\text{observed}})
\le x \le
\max(X_{\text{observed}})
\]

as the IID or interpolation region.

Predictions outside that range are marked as OOD or extrapolation.

The plot shows:

- visually distinct IID and OOD backgrounds;
- boundaries at observed X minimum and maximum;
- IID/OOD status in relevant tooltips and exports.

---

## US-0019 — Inspect Prediction Values in a Tooltip

### User story

As a researcher,  
I need to inspect numerical prediction values directly on the plot,  
so that I can interpret individual locations without exporting the data.

### Acceptance criteria

Hovering over the predictive mean displays:

- X value;
- predictive mean Y;
- lower Y bound for the selected interval;
- upper Y bound for the selected interval;
- IID or OOD status.

The tooltip labels must use the selected column names where appropriate.

---

## US-0020 — Preserve Interactive Plot State

### User story

As a researcher,  
I need zoom and axis selections to remain stable during display-only updates,  
so that I do not lose the region I am inspecting.

### Acceptance criteria

Changing display-only settings should not unnecessarily reset:

- zoom;
- pan;
- selected axis limits.

A model refit may update the data while preserving the current view when technically safe.

---

## Feature: Effective Hyperparameters

## US-0021 — Display Effective Hyperparameters

### User story

As a researcher,  
I need to know which hyperparameters the displayed model actually uses,  
so that I can interpret and reproduce the result.

### Acceptance criteria

When optimization is enabled, the application records:

- initial value;
- effective fitted value;
- optimization status.

When optimization is disabled, the effective value equals the entered value.

The application also displays:

- covariance function;
- fixed parameters;
- log marginal likelihood;
- whether target normalization was used;
- optimizer restart count.

---

## US-0022 — Keep Manual and Optimized Values Separate

### User story

As a researcher,  
I need the application to preserve the values I entered while displaying fitted values,  
so that I can switch between optimized and manual models without losing my configuration.

### Acceptance criteria

The application maintains separate internal state for:

- last user-entered values;
- current effective values.

Showing optimized values in the controls must not erase the user-entered configuration.

---

## Feature: Inference

## US-0023 — Predict One New X Value

### User story

As a researcher,  
I need to submit a new X value to the fitted model,  
so that I can obtain a prediction and its uncertainty.

### Acceptance criteria

Given a valid fitted model  
When the researcher enters a valid X value  
Then the application returns:

- predictive mean;
- predictive standard deviation;
- lower interval bound;
- upper interval bound;
- IID or OOD status.

Changing the query value must not refit the model.

---

## US-0024 — Predict Multiple New X Values

### User story

As a researcher,  
I need to predict multiple X values in one operation,  
so that I can use the fitted model for batch inference.

### Acceptance criteria

The application accepts multiple valid X values through:

- a delimited input;
- an editable table;
- or a CSV upload.

The result contains one row per query value with:

- X;
- predictive mean;
- predictive standard deviation;
- lower bound;
- upper bound;
- IID/OOD status.

Invalid values are reported clearly.

---

## US-0025 — Export Inference Results

### User story

As a researcher,  
I need to export batch inference results,  
so that I can use the predictions in another workflow.

### Acceptance criteria

Given batch predictions exist  
When the researcher selects download  
Then the application provides a CSV containing the complete inference result.

---

## Feature: Export and Reproducibility

## US-0026 — Export Prediction-Grid Results

### User story

As a researcher,  
I need to export the prediction curve numerically,  
so that I can analyse or plot it outside the application.

### Acceptance criteria

The CSV contains:

- prediction X;
- predictive mean;
- predictive standard deviation;
- lower bound;
- upper bound;
- IID/OOD classification;
- selected X and Y variable names;
- covariance function;
- initial and effective hyperparameters;
- confidence or interval probability.

---

## US-0027 — Export an Interactive Plot

### User story

As a researcher,  
I need to export the interactive prediction plot,  
so that I can inspect or share the visualization outside the running application.

### Acceptance criteria

Given a successful fit  
When the researcher exports the plot  
Then an HTML visualization is generated using the current model result and plot settings.

---

## US-0028 — Export Reproducibility Metadata

### User story

As a researcher,  
I need to export analysis metadata,  
so that I can understand how a result was produced.

### Acceptance criteria

The metadata export contains:

- source filename;
- source-data hash;
- selected variables;
- observation count;
- observed X domain;
- prediction domain;
- covariance function;
- initial hyperparameters;
- effective hyperparameters;
- fixed versus optimized status;
- normalization setting;
- optimizer restarts;
- log marginal likelihood;
- interval probability;
- fitting timestamp;
- relevant software versions;
- application artifact-format version.

---

## US-0029 — Export the Fitted Model

### User story

As a researcher,  
I need to download the fitted Gaussian Process model,  
so that I can make predictions later without retraining.

### Acceptance criteria

The exported artifact contains:

- fitted estimator;
- required preprocessing;
- selected X and Y metadata;
- observed X domain;
- covariance-function information;
- effective hyperparameters;
- interval configuration;
- dependency versions;
- artifact-format version.

The application warns that pickle-based artifacts must only be loaded from trusted sources.

---

## US-0030 — Load and Reuse a Fitted Model

### User story

As a researcher,  
I need to load a previously exported trusted model,  
so that I can perform inference without repeating the original fit.

### Acceptance criteria

Given a compatible trusted artifact  
When it is loaded  
Then the application validates its format and compatibility  
And enables single and batch inference.

If the artifact is incompatible, malformed, or untrusted  
Then the application rejects it with a clear explanation.

---

## Feature: Error Handling

## US-0031 — Recover From Fitting Errors

### User story

As a researcher,  
I need fitting failures to be explained without crashing the application,  
so that I can correct the configuration.

### Acceptance criteria

The application handles errors such as:

- covariance matrix not positive definite;
- invalid hyperparameter values;
- optimizer failure;
- unsupported covariance function;
- invalid prediction domain;
- numerical overflow or non-finite output.

The previous successful result must not be silently presented as the result of the failed configuration.

---

## US-0032 — Handle Invalid Export and Inference State

### User story

As a researcher,  
I need exports and inference to be available only for a current fitted model,  
so that I do not use stale results.

### Acceptance criteria

Exports and inference are disabled when:

- no model has been fitted;
- fitting failed;
- model settings changed and live update is disabled;
- a new dataset was uploaded;
- selected variables changed.

---

# Quality Requirements

These are not user stories, but they should be retained alongside them.

## NFR-0001 — Modular Architecture

The implementation must separate:

- CSV intake;
- validation;
- covariance-function construction;
- model fitting;
- inference;
- visualization;
- export;
- model persistence;
- user interface.

The model and inference layers must not depend on Panel or Streamlit.

---

## NFR-0002 — Extensible Covariance Functions

Adding a new covariance function should require:

- registering its name;
- defining its parameters;
- implementing its kernel construction;
- defining its dynamic controls.

It should not require rewriting the complete application.

---

## NFR-0003 — Deterministic Verification

Given a fixed dataset, random seed, software environment, and configuration, the application should produce repeatable effective hyperparameters and predictions within defined numerical tolerances.

---

## NFR-0004 — Performance Scope

The MVP is intended for small, one-dimensional experimental datasets processed in memory.

The project must define explicit limits for:

- maximum file size;
- maximum number of rows;
- maximum prediction points;
- maximum optimizer restarts.

---

## NFR-0005 — Terminology Consistency

The interface must consistently use the terminology selected for the project:

- covariance function;
- characteristic length-scale \(\ell\);
- signal standard deviation \(\sigma_f\);
- noise standard deviation \(\sigma_n\);
- Matérn smoothness parameter \(\nu\);
- Rational Quadratic parameter \(\alpha\);
- predictive mean;
- lower and upper predictive bounds;
- IID and OOD regions.

Implementation-specific names should not leak into the interface unless explained.

---

# Suggested Delivery Order

1. `DI-0001` to `DI-0003`
2. `US-0001` to `US-0004`
3. `US-0005` to `US-0009`
4. `US-0015` to `US-0019`
5. `US-0010` to `US-0014`
6. `US-0021` and `US-0022`
7. `US-0026` to `US-0028`
8. `US-0023` to `US-0025`
9. `US-0029` and `US-0030`
10. `US-0031` and `US-0032`
