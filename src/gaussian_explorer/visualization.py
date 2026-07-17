"""Plotly visualization for Gaussian Process predictions."""

from __future__ import annotations

import math
from dataclasses import dataclass

from gaussian_explorer.model import PredictionResult


@dataclass(frozen=True, slots=True)
class PlotSettings:
    """Display-only settings that do not require refitting the model."""

    x_min: float | None = None
    x_max: float | None = None
    y_min: float | None = None
    y_max: float | None = None
    show_confidence: bool = True
    show_observations: bool = True
    show_regions: bool = True


@dataclass(frozen=True, slots=True)
class VisualizationMetadata:
    """Metadata describing the displayed prediction figure."""

    x_label: str
    y_label: str
    iid_definition: str
    ood_definition: str
    confidence_level: float


def build_visualization_metadata(result: PredictionResult) -> VisualizationMetadata:
    return VisualizationMetadata(
        x_label=result.selected_variables.x_column,
        y_label=result.selected_variables.y_column,
        iid_definition=(
            f"{result.observed_x_min:g} <= x <= {result.observed_x_max:g}"
        ),
        ood_definition=(
            f"x < {result.observed_x_min:g} or x > {result.observed_x_max:g}"
        ),
        confidence_level=result.settings.confidence_level,
    )


def _validate_result(result: PredictionResult) -> None:
    collections = {
        "prediction X": result.x_values,
        "predicted mean": result.mean,
        "standard deviation": result.standard_deviation,
        "lower confidence bound": result.lower_bound,
        "upper confidence bound": result.upper_bound,
        "training X": result.training_x,
        "training Y": result.training_y,
    }
    for name, values in collections.items():
        if not values:
            raise ValueError(f"{name} contains no values.")
        for value in values:
            if not math.isfinite(float(value)):
                raise ValueError(f"{name} contains a non-finite value: {value!r}.")


def default_plot_settings(result: PredictionResult) -> PlotSettings:
    y_min = min(min(result.lower_bound), min(result.training_y))
    y_max = max(max(result.upper_bound), max(result.training_y))
    padding = max((y_max - y_min) * 0.08, 1e-9)
    return PlotSettings(
        x_min=min(result.x_values),
        x_max=max(result.x_values),
        y_min=y_min - padding,
        y_max=y_max + padding,
    )


def plot_settings_for_x_domain(
    result: PredictionResult,
    x_min: float,
    x_max: float,
) -> PlotSettings:
    if x_min >= x_max:
        raise ValueError("X minimum must be less than X maximum.")

    values: list[float] = []
    for x, lower, upper in zip(
        result.x_values,
        result.lower_bound,
        result.upper_bound,
        strict=True,
    ):
        if x_min <= x <= x_max:
            values.extend((lower, upper))
    for x, y in zip(result.training_x, result.training_y, strict=True):
        if x_min <= x <= x_max:
            values.append(y)

    if not values:
        defaults = default_plot_settings(result)
        return PlotSettings(
            x_min=x_min,
            x_max=x_max,
            y_min=defaults.y_min,
            y_max=defaults.y_max,
        )

    y_min = min(values)
    y_max = max(values)
    padding = max((y_max - y_min) * 0.10, 1e-9)
    return PlotSettings(
        x_min=x_min,
        x_max=x_max,
        y_min=y_min - padding,
        y_max=y_max + padding,
    )


def build_prediction_figure(
    result: PredictionResult,
    plot_settings: PlotSettings | None = None,
):
    """Build one stable Plotly figure shared by the UI and HTML export."""

    try:
        import plotly.graph_objects as go
    except ImportError as exc:  # pragma: no cover
        raise RuntimeError("Plotly is required to build the prediction figure.") from exc

    _validate_result(result)
    view = plot_settings or default_plot_settings(result)
    metadata = build_visualization_metadata(result)

    x = list(result.x_values)
    mean = list(result.mean)
    lower = list(result.lower_bound)
    upper = list(result.upper_bound)
    regions = list(result.regions)

    confidence_percent = metadata.confidence_level * 100.0

    customdata = [
        [lower_value, upper_value, region]
        for lower_value, upper_value, region in zip(
            lower,
            upper,
            regions,
            strict=True,
        )
    ]

    figure = go.Figure()

    if view.show_regions:
        prediction_min = min(x)
        prediction_max = max(x)
        if prediction_min < result.observed_x_min:
            figure.add_vrect(
                x0=prediction_min,
                x1=result.observed_x_min,
                fillcolor="rgba(249, 115, 22, 0.10)",
                line_width=0,
                layer="below",
            )
        figure.add_vrect(
            x0=max(prediction_min, result.observed_x_min),
            x1=min(prediction_max, result.observed_x_max),
            fillcolor="rgba(59, 130, 246, 0.07)",
            line_width=0,
            layer="below",
        )
        if prediction_max > result.observed_x_max:
            figure.add_vrect(
                x0=result.observed_x_max,
                x1=prediction_max,
                fillcolor="rgba(249, 115, 22, 0.10)",
                line_width=0,
                layer="below",
            )

    if view.show_confidence:
        figure.add_trace(
            go.Scatter(
                x=x,
                y=upper,
                mode="lines",
                line={"width": 0},
                hoverinfo="skip",
                showlegend=False,
                name="Upper confidence bound",
            )
        )
        figure.add_trace(
            go.Scatter(
                x=x,
                y=lower,
                mode="lines",
                line={"width": 0},
                fill="tonexty",
                fillcolor="rgba(59, 130, 246, 0.24)",
                name=f"{metadata.confidence_level:.0%} confidence",
                hoverinfo="skip",
            )
        )

    figure.add_trace(
        go.Scatter(
            x=x,
            y=mean,
            mode="lines",
            line={"width": 3, "color": "#dc2626"},
            name="Mean prediction",
            customdata=customdata,
            hovertemplate=(
                "<b>Gaussian Process prediction</b><br>"
                f"{metadata.x_label}: %{{x:.6g}}<br>"
                f"Mean {metadata.y_label}: %{{y:.6g}}<br>"
                f"Lower {metadata.y_label} ({confidence_percent:.0f}%): "
                "%{customdata[0]:.6g}<br>"
                f"Upper {metadata.y_label} ({confidence_percent:.0f}%): "
                "%{customdata[1]:.6g}<br>"
                "Region: %{customdata[2]}"
                "<extra></extra>"
            ),
        )
    )

    if view.show_observations:
        figure.add_trace(
            go.Scatter(
                x=list(result.training_x),
                y=list(result.training_y),
                mode="markers",
                marker={
                    "size": 9,
                    "color": "#111827",
                    "line": {"width": 1, "color": "white"},
                },
                name="Observed data",
                hovertemplate=(
                    f"Observed {metadata.x_label}: %{{x:.6g}}<br>"
                    f"Observed {metadata.y_label}: %{{y:.6g}}"
                    "<extra></extra>"
                ),
            )
        )

    figure.add_vline(
        x=result.observed_x_min,
        line_width=1,
        line_dash="dash",
        line_color="#6b7280",
    )
    figure.add_vline(
        x=result.observed_x_max,
        line_width=1,
        line_dash="dash",
        line_color="#6b7280",
    )

    x_range = None
    if view.x_min is not None and view.x_max is not None:
        if view.x_min >= view.x_max:
            raise ValueError("X minimum must be less than X maximum.")
        x_range = [view.x_min, view.x_max]

    y_range = None
    if view.y_min is not None and view.y_max is not None:
        if view.y_min >= view.y_max:
            raise ValueError("Y minimum must be less than Y maximum.")
        y_range = [view.y_min, view.y_max]

    figure.update_layout(
        title={"text": "Gaussian Process prediction and uncertainty", "x": 0.01},
        template="plotly_white",
        height=610,
        margin={"l": 70, "r": 30, "t": 75, "b": 60},
        hovermode="x unified",
        dragmode="zoom",
        uirevision="gaussian-explorer-view",
        legend={"orientation": "h", "y": 1.08, "x": 0},
        xaxis={
            "title": metadata.x_label,
            "range": x_range,
            "autorange": x_range is None,
            "showgrid": True,
            "gridcolor": "#e5e7eb",
            "zeroline": False,
        },
        yaxis={
            "title": metadata.y_label,
            "range": y_range,
            "autorange": y_range is None,
            "showgrid": True,
            "gridcolor": "#e5e7eb",
            "zeroline": True,
            "zerolinecolor": "#d1d5db",
        },
    )
    return figure
