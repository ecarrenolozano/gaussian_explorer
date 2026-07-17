"""Inference helpers for fitted Gaussian Process models."""

from __future__ import annotations

import csv
import io
import math
from dataclasses import asdict, dataclass
from typing import Iterable, Protocol


class PredictiveModel(Protocol):
    """Minimal interface required from a fitted regression estimator."""

    def predict(self, values, *, return_std: bool = False): ...


@dataclass(frozen=True, slots=True)
class InferenceResult:
    """Prediction and uncertainty for one input value."""

    x: float
    predicted_mean: float
    predictive_standard_deviation: float
    lower_bound: float
    upper_bound: float
    confidence_level: float
    region: str


class InferenceError(ValueError):
    """Raised when inference inputs or model outputs are invalid."""


def _confidence_multiplier(confidence_level: float) -> float:
    if not 0.50 < confidence_level < 0.999:
        raise InferenceError("Confidence level must be between 0.50 and 0.999.")
    try:
        from scipy.stats import norm
    except ImportError as exc:  # pragma: no cover
        raise RuntimeError("SciPy is required to calculate confidence intervals.") from exc
    return float(norm.ppf((1.0 + confidence_level) / 2.0))


def classify_distribution_region(
    x: float,
    training_x_min: float,
    training_x_max: float,
) -> str:
    """Classify an input as interpolation (IID) or extrapolation (OOD)."""

    if training_x_min > training_x_max:
        raise InferenceError("Training X minimum cannot exceed its maximum.")
    return "iid" if training_x_min <= x <= training_x_max else "ood"


def predict_many(
    model: PredictiveModel,
    x_values: Iterable[float],
    *,
    training_x_min: float,
    training_x_max: float,
    confidence_level: float = 0.95,
) -> tuple[InferenceResult, ...]:
    """Predict one or more new X values with uncertainty and IID/OOD labels."""

    try:
        import numpy as np
    except ImportError as exc:  # pragma: no cover
        raise RuntimeError("NumPy is required for Gaussian Process inference.") from exc

    values = tuple(float(value) for value in x_values)
    if not values:
        raise InferenceError("Provide at least one X value for inference.")
    if not all(math.isfinite(value) for value in values):
        raise InferenceError("All inference X values must be finite numbers.")

    multiplier = _confidence_multiplier(confidence_level)
    query = np.asarray(values, dtype=float).reshape(-1, 1)

    try:
        means, standard_deviations = model.predict(query, return_std=True)
    except Exception as exc:
        raise InferenceError(f"The fitted model could not predict the supplied values: {exc}") from exc

    if len(means) != len(values) or len(standard_deviations) != len(values):
        raise InferenceError("The fitted model returned an unexpected number of predictions.")

    results: list[InferenceResult] = []
    for x, mean, standard_deviation in zip(
        values,
        means,
        standard_deviations,
        strict=True,
    ):
        mean_value = float(mean)
        std_value = float(standard_deviation)
        if not math.isfinite(mean_value) or not math.isfinite(std_value):
            raise InferenceError("The fitted model returned a non-finite prediction.")
        if std_value < 0:
            raise InferenceError("Predictive standard deviation cannot be negative.")
        results.append(
            InferenceResult(
                x=x,
                predicted_mean=mean_value,
                predictive_standard_deviation=std_value,
                lower_bound=mean_value - multiplier * std_value,
                upper_bound=mean_value + multiplier * std_value,
                confidence_level=confidence_level,
                region=classify_distribution_region(
                    x,
                    training_x_min,
                    training_x_max,
                ),
            )
        )
    return tuple(results)


def predict_one(
    model: PredictiveModel,
    x: float,
    *,
    training_x_min: float,
    training_x_max: float,
    confidence_level: float = 0.95,
) -> InferenceResult:
    """Predict one X value."""

    return predict_many(
        model,
        [x],
        training_x_min=training_x_min,
        training_x_max=training_x_max,
        confidence_level=confidence_level,
    )[0]


def inference_results_csv(results: Iterable[InferenceResult]) -> bytes:
    """Serialize inference results as a deterministic UTF-8 CSV file."""

    rows = tuple(results)
    if not rows:
        raise InferenceError("There are no inference results to export.")

    fieldnames = tuple(asdict(rows[0]).keys())
    output = io.StringIO(newline="")
    writer = csv.DictWriter(output, fieldnames=fieldnames, lineterminator="\n")
    writer.writeheader()
    for result in rows:
        writer.writerow(asdict(result))
    return output.getvalue().encode("utf-8")
