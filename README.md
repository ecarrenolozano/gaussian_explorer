# Gaussian Process Regression Explorer — Panel

## Install

```bash
uv pip install panel plotly pandas numpy scipy scikit-learn joblib
```

## Run

```bash
PYTHONPATH=src panel serve src/gaussian_explorer/app.py --show --autoreload
```

## New inference capabilities

After fitting a model, the application can:

- predict one new X value;
- predict multiple comma-, space-, or line-separated X values;
- return predicted mean, predictive standard deviation, confidence bounds, and IID/OOD status;
- export inference results as CSV;
- download the complete fitted model as a versioned joblib artifact.

## Reuse an exported model

Only load model artifacts from trusted sources. Joblib uses pickle-based serialization and may execute code during loading.

```python
from gaussian_explorer.persistence import load_model_artifact

artifact = load_model_artifact("gaussian_process_model.joblib")
result = artifact.predict_one(4.2)
print(result)
```

The artifact records the selected variables, training domain, model settings, initial and fitted kernel descriptions, source hash, and package versions used during fitting.
