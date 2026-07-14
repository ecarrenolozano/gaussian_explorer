# Story-to-Architecture Map

## Current Mapping

- Architecture version: `1.0`
- Source story version: `1.0`
- Last updated: `2026-07-14`

<!-- architecture-map | architecture-version: 1.0 | source-story-version: 1.0 -->

| Story ID | Source Batches | Architecture Responsibilities | Major Applications or Services | Components | Interfaces | Data | Architecture Decisions | Mapping Status | Notes |
|---|---|---|---|---|---|---|---|---|---|
| US-0001 | PRDB-001 | Accept CSV uploads and make validated dataset state available for variable selection. | Streamlit web application | Workflow UI; CSV parsing and validation | CSV upload | Uploaded CSV dataset; In-memory analysis session | architecture-decision-001; architecture-decision-002 | mapped | File validation blocks unsupported, malformed, or very large files. |
| US-0002 | PRDB-001 | Present numeric column choices and capture selected X/Y variables for analysis. | Streamlit web application | CSV parsing and validation; Variable and GPR settings | Variable selection | Uploaded CSV dataset; In-memory analysis session | architecture-decision-001; architecture-decision-002 | mapped | Multi-column CSV input is supported; two selected numeric variables are analyzed. |
| US-0003 | PRDB-001 | Provide default and editable GPR settings before model fitting. | Streamlit web application | Workflow UI; Variable and GPR settings | GPR settings | In-memory analysis session | architecture-decision-001; architecture-decision-002 | mapped | Settings include kernel choice, length scale, noise level / alpha, prediction range, number of prediction points, and confidence interval level. |
| US-0004 | PRDB-001 | Fit GPR using validated selected variables and current settings. | Streamlit web application | Variable and GPR settings; GPR fitting and prediction | Model fitting | Uploaded CSV dataset; In-memory analysis session | architecture-decision-001; architecture-decision-002 | mapped | Fitting only proceeds after validation. |
| US-0005 | PRDB-001 | Display original data, predicted curve, and uncertainty estimates together. | Streamlit web application | GPR fitting and prediction; Prediction and uncertainty visualization | Results visualization | In-memory analysis session | architecture-decision-001; architecture-decision-002 | mapped | Visualization consumes fitted result state. |
| US-0006 | PRDB-001 | Generate tabular prediction results with predicted X values, predicted mean, uncertainty bounds, selected column names, and model settings. | Streamlit web application | GPR fitting and prediction; Variable and GPR settings; Export generation | Export download | In-memory analysis session; Export artifacts | architecture-decision-001; architecture-decision-002 | mapped | Export unavailable until fitted prediction results exist. |
| US-0007 | PRDB-001 | Generate plot export and reproducibility metadata from fitted analysis state. | Streamlit web application | Prediction and uncertainty visualization; GPR fitting and prediction; Export generation | Export download | In-memory analysis session; Export artifacts | architecture-decision-001; architecture-decision-002 | mapped | Metadata preserves selected variables, settings, prediction results, and plot metadata. |
| US-0008 | PRDB-001 | Reject invalid uploads or selected data with user-visible corrective feedback. | Streamlit web application | Workflow UI; CSV parsing and validation; Variable and GPR settings | CSV upload; Variable selection; Model fitting | Uploaded CSV dataset; In-memory analysis session | architecture-decision-001; architecture-decision-002 | mapped | Covers all invalid-input cases confirmed in `PRDB-001`. |
