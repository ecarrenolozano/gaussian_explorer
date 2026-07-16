# Architecture Traceability

<!-- architecture-traceability | architecture-version: 1.0 | source-story-version: 1.0 -->

| Story ID | arc42 concern | Software system | Container | Component or data model | Runtime or deployment concern | Responsibility | Implementation location | Mapping status | Related decision or issue |
|---|---|---|---|---|---|---|---|---|---|
| US-0001 | Sections 3, 5, 6, 8 | Gaussian Process Regression Web Application | Streamlit Web Application; In-memory Analysis Session | Workflow UI; CSV parsing and validation; Active analysis state | CSV upload gate | Accept supported CSV data and make the accepted dataset available for variable selection. | `src/gaussian_explorer/data.py` for current CSV parsing; Streamlit entry point proposed. | confirmed / proposed | ADR-001, ADR-002 |
| US-0002 | Sections 5, 6, 8 | Gaussian Process Regression Web Application | Streamlit Web Application; In-memory Analysis Session | Variable and GPR settings; CSV parsing and validation; Active analysis state | Variable selection gate | Derive numeric columns and record one X and one Y variable for regression. | `src/gaussian_explorer/validation.py` proposed. | proposed | ADR-001, ADR-002 |
| US-0003 | Sections 5, 6, 8 | Gaussian Process Regression Web Application | Streamlit Web Application; In-memory Analysis Session | Workflow UI; Variable and GPR settings; Active analysis state | Settings review before fitting | Provide default GPR settings and use changed settings for analysis. | `src/gaussian_explorer/app.py` and `src/gaussian_explorer/model.py` proposed. | proposed | ADR-001, ADR-002 |
| US-0004 | Sections 5, 6, 8, 10 | Gaussian Process Regression Web Application | Streamlit Web Application; In-memory Analysis Session | GPR fitting and prediction; Variable and GPR settings; Active analysis state | Model fitting gate | Fit a GPR model from validated data, selected variables, and current settings. | `src/gaussian_explorer/model.py` proposed. | proposed | ADR-001, ADR-002 |
| US-0005 | Sections 5, 6, 8, 10 | Gaussian Process Regression Web Application | Streamlit Web Application; In-memory Analysis Session | Prediction and uncertainty visualization; GPR fitting and prediction; Active analysis state | Result visualization after fitting | Display original data, predicted curve, and uncertainty estimates together. | `src/gaussian_explorer/visualization.py` proposed. | proposed | ADR-001, ADR-002 |
| US-0006 | Sections 5, 6, 8, 10 | Gaussian Process Regression Web Application | Streamlit Web Application; In-memory Analysis Session | Export generation; GPR fitting and prediction; Variable and GPR settings; Active analysis state | Export download after fitting | Provide a results CSV with prediction values, uncertainty bounds, selected variables, and model settings. | `src/gaussian_explorer/export.py` proposed. | proposed | ADR-001, ADR-002 |
| US-0007 | Sections 5, 6, 8, 10 | Gaussian Process Regression Web Application | Streamlit Web Application; In-memory Analysis Session | Prediction and uncertainty visualization; Export generation; Active analysis state | Plot and metadata export after visualization | Provide plot output and reproducibility metadata from the fitted analysis state. | `src/gaussian_explorer/export.py` and `src/gaussian_explorer/visualization.py` proposed. | proposed | ADR-001, ADR-002 |
| US-0008 | Sections 3, 5, 6, 8, 10 | Gaussian Process Regression Web Application | Streamlit Web Application; In-memory Analysis Session | Workflow UI; CSV parsing and validation; Variable and GPR settings; GPR fitting and prediction; Active analysis state | Upload, selection, and fitting validation gates | Prevent analysis from proceeding for each confirmed invalid-input case and explain the problem. | `src/gaussian_explorer/data.py` confirmed for initial CSV parsing; `src/gaussian_explorer/validation.py` proposed for remaining validation. | confirmed / proposed | ADR-001, ADR-002 |

## Coverage Notes

- Active story coverage: `US-0001` through `US-0008` are mapped.
- Source story version: `1.0`.
- Architecture version: `1.0`.
- Current confirmed implementation evidence: `src/gaussian_explorer/data.py` exists and provides in-memory CSV intake support.
- Proposed implementation locations are architecture guidance only; implementation planning may refine names while preserving responsibilities.
