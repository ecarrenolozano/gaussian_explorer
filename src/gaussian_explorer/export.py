"""Prediction, plot, and reproducibility exports."""

from __future__ import annotations

import csv
import io
import json
from dataclasses import asdict

from gaussian_explorer.data import UploadedDataset
from gaussian_explorer.model import PredictionResult
from gaussian_explorer.visualization import VisualizationMetadata

RESULT_FIELDS = (
    "predicted_x",
    "predicted_mean",
    "standard_deviation",
    "lower_bound",
    "upper_bound",
    "distribution_region",
    "x_column",
    "y_column",
    "covariance_function",
    "characteristic_length_scale",
    "sigma_f",
    "signal_variance",
    "sigma_n",
    "noise_variance",
    "matern_nu",
    "rational_quadratic_alpha",
    "optimize_hyperparameters",
    "normalize_target",
    "optimizer_restarts",
    "prediction_min",
    "prediction_max",
    "prediction_points",
    "confidence_level",
    "effective_length_scale",
    "effective_sigma_f",
    "effective_rational_quadratic_alpha",
    "hyperparameter_status",
    "log_marginal_likelihood",
)


def build_results_csv(result: PredictionResult) -> bytes:
    output = io.StringIO(newline="")
    writer = csv.DictWriter(output, fieldnames=RESULT_FIELDS, lineterminator="\n")
    writer.writeheader()
    for x, mean, std, lower, upper, region in zip(
        result.x_values,
        result.mean,
        result.standard_deviation,
        result.lower_bound,
        result.upper_bound,
        result.regions,
        strict=True,
    ):
        writer.writerow(
            {
                "predicted_x": x,
                "predicted_mean": mean,
                "standard_deviation": std,
                "lower_bound": lower,
                "upper_bound": upper,
                "distribution_region": region,
                "x_column": result.selected_variables.x_column,
                "y_column": result.selected_variables.y_column,
                "covariance_function": result.settings.covariance_function,
                "characteristic_length_scale": result.settings.length_scale,
                "sigma_f": result.settings.sigma_f,
                "signal_variance": result.settings.signal_variance,
                "sigma_n": result.settings.sigma_n,
                "noise_variance": result.settings.noise_variance,
                "matern_nu": result.settings.matern_nu,
                "rational_quadratic_alpha": result.settings.rational_quadratic_alpha,
                "optimize_hyperparameters": result.settings.optimize_hyperparameters,
                "normalize_target": result.settings.normalize_target,
                "optimizer_restarts": result.settings.optimizer_restarts,
                "prediction_min": result.settings.prediction_min,
                "prediction_max": result.settings.prediction_max,
                "prediction_points": result.settings.prediction_points,
                "confidence_level": result.settings.confidence_level,
                "effective_length_scale": result.hyperparameters.effective_length_scale,
                "effective_sigma_f": result.hyperparameters.effective_sigma_f,
                "effective_rational_quadratic_alpha": (
                    result.hyperparameters.effective_rational_quadratic_alpha
                ),
                "hyperparameter_status": (
                    "optimized"
                    if result.hyperparameters.optimization_enabled
                    else "fixed_user_values"
                ),
                "log_marginal_likelihood": (
                    result.hyperparameters.log_marginal_likelihood
                ),
            }
        )
    return output.getvalue().encode("utf-8")


def build_metadata_json(
    dataset: UploadedDataset,
    result: PredictionResult,
    visualization: VisualizationMetadata,
) -> bytes:
    payload = {
        "source": {
            "filename": dataset.filename,
            "row_count": dataset.row_count,
            "sha256": dataset.content_hash,
        },
        "selected_variables": asdict(result.selected_variables),
        "settings": asdict(result.settings),
        "effective_hyperparameters": asdict(result.hyperparameters),
        "training_domain": {
            "observed_x_min": result.observed_x_min,
            "observed_x_max": result.observed_x_max,
        },
        "prediction_summary": {
            "prediction_count": len(result.x_values),
            "iid_prediction_count": result.regions.count("iid"),
            "ood_prediction_count": result.regions.count("ood"),
            "confidence_multiplier": result.confidence_multiplier,
        },
        "visualization": asdict(visualization),
    }
    return (json.dumps(payload, indent=2, sort_keys=True, allow_nan=False) + "\n").encode(
        "utf-8"
    )


def build_plot_html(figure) -> bytes:
    """Export the same Plotly figure used by the Panel application."""

    return figure.to_html(
        full_html=True,
        include_plotlyjs="cdn",
        config={"responsive": True, "displaylogo": False},
    ).encode("utf-8")
