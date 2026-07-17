"""Panel application for interactive Gaussian Process exploration."""

from __future__ import annotations

import io
from dataclasses import asdict
from typing import Any

import panel as pn
import pandas as pd

from gaussian_explorer.data import CsvUploadError, UploadedDataset, load_uploaded_csv
from gaussian_explorer.export import build_metadata_json, build_plot_html, build_results_csv
from gaussian_explorer.inference import InferenceError, InferenceResult, inference_results_csv
from gaussian_explorer.persistence import (
    GaussianProcessArtifact,
    create_model_artifact,
    serialize_model_artifact,
)
from gaussian_explorer.model import (
    GprSettings,
    ModelFitError,
    ModelSettingsError,
    PredictionResult,
    SUPPORTED_KERNELS,
    default_gpr_settings,
    fit_gpr_bundle,
)
from gaussian_explorer.validation import (
    SelectedVariables,
    ValidationError,
    find_numeric_columns,
    validate_selected_variables,
)
from gaussian_explorer.visualization import (
    PlotSettings,
    build_prediction_figure,
    build_visualization_metadata,
    default_plot_settings,
    plot_settings_for_x_domain,
)

pn.extension("plotly", "tabulator", notifications=True, sizing_mode="stretch_width")

APP_CSS = """
:root {
  --ge-border: #e5e7eb;
  --ge-muted: #64748b;
  --ge-panel: #ffffff;
}
.bk-root { font-family: Inter, ui-sans-serif, system-ui, sans-serif; }
.ge-hero { padding: 0.2rem 0 0.8rem 0; }
.ge-hero h1 { margin: 0; color: #0f172a; font-size: 2rem; }
.ge-hero p { margin: 0.35rem 0 0; color: var(--ge-muted); }
.ge-card {
  background: var(--ge-panel);
  border: 1px solid var(--ge-border);
  border-radius: 12px;
  padding: 14px 16px;
  min-height: 92px;
  box-shadow: 0 1px 2px rgba(15, 23, 42, 0.03);
}
.ge-card-label { color: var(--ge-muted); font-size: 0.82rem; }
.ge-card-value { color: #0f172a; font-size: 1.75rem; font-weight: 700; margin-top: 0.25rem; }
.ge-status-ok { color: #15803d; font-weight: 600; }
.ge-status-muted { color: var(--ge-muted); }
"""


class GaussianExplorerApp:
    """One Panel session containing data, controls, model state, and exports."""

    def __init__(self) -> None:
        self.dataset: UploadedDataset | None = None
        self.selection: SelectedVariables | None = None
        self.result: PredictionResult | None = None
        self.artifact: GaussianProcessArtifact | None = None
        self.inference_results: tuple[InferenceResult, ...] = ()
        self._analysis_signature: tuple[Any, ...] | None = None
        self._updating = False
        self._manual_hyperparameters: dict[str, float] = {}
        self._showing_effective_hyperparameters = False

        self._build_widgets()
        self._build_layout()
        self._connect_callbacks()
        self._set_ready_state(False)

    def _build_widgets(self) -> None:
        self.file_input = pn.widgets.FileInput(
            name="Upload CSV file",
            accept=".csv,text/csv",
            multiple=False,
        )
        self.dataset_status = pn.pane.HTML(
            "<span class='ge-status-muted'>Upload a CSV file to begin.</span>",
            margin=(4, 0, 8, 0),
        )

        self.x_select = pn.widgets.Select(name="X variable", options=[])
        self.y_select = pn.widgets.Select(name="Y variable", options=[])

        self.live_update = pn.widgets.Checkbox(name="Live update", value=True)
        self.fit_button = pn.widgets.Button(name="Fit model", button_type="primary")
        self.kernel = pn.widgets.Select(name="Covariance function", options=list(SUPPORTED_KERNELS))
        self.length_scale = pn.widgets.FloatInput(
            name="Characteristic length-scale ℓ", value=1.0, start=1e-12, step=0.1
        )
        self.sigma_f = pn.widgets.FloatInput(
            name="Signal standard deviation σ_f", value=1.0, start=1e-12, step=0.1
        )
        self.sigma_n = pn.widgets.FloatInput(
            name="Noise standard deviation σ_n", value=1e-3, start=1e-12, step=1e-3
        )
        self.matern_nu = pn.widgets.Select(
            name="Smoothness parameter ν",
            options={"1/2": 0.5, "3/2": 1.5, "5/2": 2.5},
            value=1.5,
        )
        self.rq_alpha = pn.widgets.FloatInput(
            name="Rational Quadratic parameter α", value=1.0, start=1e-12, step=0.1
        )
        self.kernel_parameters = pn.Column()
        self.optimize_hyperparameters = pn.widgets.Checkbox(
            name="Optimize hyperparameters", value=True
        )
        self.normalize_target = pn.widgets.Checkbox(name="Normalize target", value=True)
        self.optimizer_restarts = pn.widgets.IntInput(
            name="Optimizer restarts", value=0, start=0, end=20
        )
        self.prediction_min = pn.widgets.FloatInput(name="Prediction minimum")
        self.prediction_max = pn.widgets.FloatInput(name="Prediction maximum")
        self.prediction_points = pn.widgets.IntSlider(
            name="Prediction points", start=50, end=1500, step=50, value=300
        )
        self.confidence_level = pn.widgets.FloatSlider(
            name="Confidence level", start=0.80, end=0.99, step=0.01, value=0.95
        )

        self.show_confidence = pn.widgets.Checkbox(name="Show confidence region", value=True)
        self.show_observations = pn.widgets.Checkbox(name="Show observations", value=True)
        self.show_regions = pn.widgets.Checkbox(name="Show IID / OOD regions", value=True)
        self.x_min = pn.widgets.FloatInput(name="X minimum", value=None)
        self.x_max = pn.widgets.FloatInput(name="X maximum", value=None)
        self.y_min = pn.widgets.FloatInput(name="Y minimum", value=None)
        self.y_max = pn.widgets.FloatInput(name="Y maximum", value=None)
        self.full_range_button = pn.widgets.Button(name="Full range", button_type="light")
        self.focus_iid_button = pn.widgets.Button(name="Focus IID", button_type="primary")

        self.plot_pane = pn.pane.Plotly(
            None,
            config={
                "responsive": True,
                "displaylogo": False,
                "scrollZoom": True,
                "modeBarButtonsToRemove": ["lasso2d", "select2d"],
            },
            sizing_mode="stretch_both",
            min_height=610,
        )
        self.message = pn.pane.Alert(
            "Upload a CSV file to begin.",
            alert_type="info",
            visible=True,
        )

        self.metric_observed = pn.pane.HTML(self._metric_html("Observed points", "—"))
        self.metric_iid = pn.pane.HTML(self._metric_html("IID prediction points", "—"))
        self.metric_ood = pn.pane.HTML(self._metric_html("OOD prediction points", "—"))
        self.metric_confidence = pn.pane.HTML(self._metric_html("Confidence level", "—"))

        self.details = pn.pane.Markdown("No fitted model.")
        self.preview = pn.widgets.Tabulator(
            pd.DataFrame(),
            pagination="local",
            page_size=12,
            disabled=True,
            show_index=False,
            height=320,
        )

        self.download_csv = pn.widgets.FileDownload(
            name="Prediction CSV",
            filename="prediction_results.csv",
            callback=self._download_csv,
            button_type="primary",
            disabled=True,
        )
        self.download_html = pn.widgets.FileDownload(
            name="Interactive plot HTML",
            filename="prediction_chart.html",
            callback=self._download_html,
            button_type="primary",
            disabled=True,
        )
        self.inference_x = pn.widgets.FloatInput(name="New X value", value=0.0)
        self.predict_one_button = pn.widgets.Button(
            name="Predict value", button_type="primary", disabled=True
        )
        self.inference_summary = pn.pane.HTML(
            "<span class='ge-status-muted'>Fit a model before running inference.</span>"
        )
        self.batch_values = pn.widgets.TextAreaInput(
            name="Multiple X values",
            placeholder="Enter values separated by commas or new lines, for example: 1.5, 2.0, 4.2",
            height=100,
        )
        self.predict_many_button = pn.widgets.Button(
            name="Predict values", button_type="primary", disabled=True
        )
        self.inference_table = pn.widgets.Tabulator(
            pd.DataFrame(),
            disabled=True,
            show_index=False,
            pagination="local",
            page_size=10,
            height=280,
        )
        self.download_inference_csv = pn.widgets.FileDownload(
            name="Inference CSV",
            filename="inference_results.csv",
            callback=self._download_inference_csv,
            button_type="primary",
            disabled=True,
        )
        self.download_model = pn.widgets.FileDownload(
            name="Fitted model",
            filename="gaussian_process_model.joblib",
            callback=self._download_model,
            button_type="primary",
            disabled=True,
        )

        self.download_json = pn.widgets.FileDownload(
            name="Metadata JSON",
            filename="reproducibility_metadata.json",
            callback=self._download_json,
            button_type="primary",
            disabled=True,
        )

    def _build_layout(self) -> None:
        data_card = pn.Card(
            self.file_input,
            self.dataset_status,
            title="Data",
            collapsed=False,
            margin=0,
        )
        variables_card = pn.Card(
            self.x_select,
            self.y_select,
            title="Variables",
            collapsed=False,
            margin=0,
        )
        model_card = pn.Card(
            self.kernel,
            self.kernel_parameters,
            pn.Row(self.optimize_hyperparameters, self.normalize_target),
            self.optimizer_restarts,
            pn.Row(self.prediction_min, self.prediction_max),
            self.prediction_points,
            self.confidence_level,
            pn.Row(self.live_update, self.fit_button),
            title="Model and prediction",
            collapsed=False,
            margin=0,
        )
        plot_card = pn.Card(
            self.show_confidence,
            self.show_observations,
            self.show_regions,
            pn.Row(self.x_min, self.x_max),
            pn.Row(self.y_min, self.y_max),
            pn.Row(self.full_range_button, self.focus_iid_button),
            title="Plot view",
            collapsed=False,
            margin=0,
        )

        metrics = pn.Row(
            self.metric_observed,
            self.metric_iid,
            self.metric_ood,
            self.metric_confidence,
            sizing_mode="stretch_width",
        )
        model_and_exports = pn.Row(
            pn.Card(self.details, title="Model details", collapsed=False),
            pn.Card(
                pn.pane.Markdown(
                    "Exports are built only when you click a download button."
                ),
                pn.Row(self.download_csv, self.download_html, self.download_json, self.download_model),
                title="Exports",
                collapsed=False,
            ),
        )
        inference_card = pn.Card(
            pn.pane.Markdown(
                "Use the fitted Gaussian Process as an inference machine. "
                "Predictions include uncertainty and an IID/OOD classification."
            ),
            pn.Row(self.inference_x, self.predict_one_button),
            self.inference_summary,
            pn.layout.Divider(),
            self.batch_values,
            pn.Row(self.predict_many_button, self.download_inference_csv),
            self.inference_table,
            title="Predict new values",
            collapsed=False,
        )

        preview_card = pn.Card(
            self.preview,
            title="Dataset preview",
            collapsed=True,
        )

        hero = pn.pane.HTML(
            """
            <div class="ge-hero">
              <h1>Gaussian Process Regression Explorer</h1>
              <p>Fit one-dimensional Gaussian Processes, compare IID interpolation with OOD extrapolation, and inspect predictive uncertainty.</p>
            </div>
            """
        )

        self.template = pn.template.FastListTemplate(
            title="Gaussian Process Explorer",
            site="Scientific modelling",
            accent_base_color="#2563eb",
            header_background="#ffffff",
            header_color="#0f172a",
            sidebar_width=330,
            main_max_width="1550px",
            theme_toggle=False,
            raw_css=[APP_CSS],
            sidebar=[data_card, variables_card, model_card, plot_card],
            main=[
                hero,
                self.message,
                metrics,
                pn.Card(
                    self.plot_pane,
                    title="Prediction and uncertainty",
                    collapsed=False,
                    min_height=670,
                ),
                inference_card,
                model_and_exports,
                preview_card,
            ],
        )

    def _connect_callbacks(self) -> None:
        self._update_kernel_parameter_controls()
        self.kernel.param.watch(self._on_kernel_changed, "value")
        self.file_input.param.watch(self._on_file_uploaded, "value")
        self.x_select.param.watch(self._on_variables_changed, "value")
        self.y_select.param.watch(self._on_variables_changed, "value")
        self.live_update.param.watch(self._on_live_update_changed, "value")
        self.fit_button.on_click(lambda _: self._fit(force=True))

        for widget in (
            self.length_scale,
            self.sigma_f,
            self.sigma_n,
            self.matern_nu,
            self.rq_alpha,
        ):
            parameter = "value_throttled" if "value_throttled" in widget.param else "value"
            widget.param.watch(self._on_hyperparameter_input_changed, parameter)

        self.optimize_hyperparameters.param.watch(
            self._on_optimization_toggled,
            "value",
        )

        for widget in (
            self.normalize_target,
            self.optimizer_restarts,
            self.prediction_min,
            self.prediction_max,
            self.prediction_points,
            self.confidence_level,
        ):
            parameter = "value_throttled" if "value_throttled" in widget.param else "value"
            widget.param.watch(self._on_model_setting_changed, parameter)

        for widget in (
            self.show_confidence,
            self.show_observations,
            self.show_regions,
            self.x_min,
            self.x_max,
            self.y_min,
            self.y_max,
        ):
            parameter = "value_throttled" if "value_throttled" in widget.param else "value"
            widget.param.watch(self._on_plot_setting_changed, parameter)

        self.full_range_button.on_click(lambda _: self._use_full_range())
        self.focus_iid_button.on_click(lambda _: self._focus_iid())
        self.predict_one_button.on_click(lambda _: self._predict_one())
        self.predict_many_button.on_click(lambda _: self._predict_many())

    @staticmethod
    def _metric_html(label: str, value: str) -> str:
        return (
            "<div class='ge-card'>"
            f"<div class='ge-card-label'>{label}</div>"
            f"<div class='ge-card-value'>{value}</div>"
            "</div>"
        )

    def _set_ready_state(self, ready: bool) -> None:
        for widget in (
            self.x_select,
            self.y_select,
            self.kernel,
            self.length_scale,
            self.sigma_f,
            self.sigma_n,
            self.matern_nu,
            self.rq_alpha,
            self.optimize_hyperparameters,
            self.normalize_target,
            self.optimizer_restarts,
            self.prediction_min,
            self.prediction_max,
            self.prediction_points,
            self.confidence_level,
            self.live_update,
            self.fit_button,
            self.show_confidence,
            self.show_observations,
            self.show_regions,
            self.x_min,
            self.x_max,
            self.y_min,
            self.y_max,
            self.full_range_button,
            self.focus_iid_button,
        ):
            widget.disabled = not ready

    def _reset_inference_state(self) -> None:
        self.artifact = None
        self.inference_results = ()
        self.predict_one_button.disabled = True
        self.predict_many_button.disabled = True
        self.download_inference_csv.disabled = True
        self.download_model.disabled = True
        self.inference_summary.object = (
            "<span class='ge-status-muted'>Fit a model before running inference.</span>"
        )
        self.inference_table.value = pd.DataFrame()

    def _on_file_uploaded(self, event: Any) -> None:
        if not event.new:
            self.dataset = None
            self.selection = None
            self.result = None
            self._reset_inference_state()
            self.plot_pane.object = None
            self.dataset_status.object = (
                "<span class='ge-status-muted'>Upload a CSV file to begin.</span>"
            )
            self._set_ready_state(False)
            return

        try:
            dataset = load_uploaded_csv(
                event.new,
                filename=self.file_input.filename,
            )
            numeric_columns = find_numeric_columns(dataset)
            if len(numeric_columns) < 2:
                raise ValidationError(
                    "The dataset must contain at least two fully numeric columns."
                )
        except (CsvUploadError, ValidationError) as exc:
            self._show_error(str(exc))
            return

        self._updating = True
        try:
            self.dataset = dataset
            self.result = None
            self._reset_inference_state()
            self._analysis_signature = None
            self.x_select.options = list(numeric_columns)
            self.y_select.options = list(numeric_columns)
            self.x_select.value = numeric_columns[0]
            self.y_select.value = numeric_columns[1]
            self.preview.value = pd.DataFrame(
                dataset.rows, columns=dataset.columns
            )
            self.dataset_status.object = (
                f"<span class='ge-status-ok'>Loaded {dataset.row_count} rows and "
                f"{len(dataset.columns)} columns.</span>"
            )
            self._set_ready_state(True)
            self.fit_button.disabled = self.live_update.value
            self._update_selection_and_defaults()
        finally:
            self._updating = False

        self._fit(force=True)

    def _on_variables_changed(self, _event: Any) -> None:
        if self._updating or self.dataset is None:
            return
        self._updating = True
        try:
            self._update_selection_and_defaults()
        finally:
            self._updating = False
        self._fit(force=True)

    def _update_selection_and_defaults(self) -> None:
        if self.dataset is None or not self.x_select.value or not self.y_select.value:
            return
        try:
            selection = validate_selected_variables(
                self.dataset,
                self.x_select.value,
                self.y_select.value,
            )
            defaults = default_gpr_settings(self.dataset, selection)
        except ValidationError as exc:
            self._show_error(str(exc))
            return

        self.selection = selection
        self.kernel.value = defaults.covariance_function
        self.sigma_f.value = defaults.sigma_f
        self.length_scale.value = defaults.length_scale
        self.sigma_n.value = defaults.sigma_n
        self.matern_nu.value = defaults.matern_nu
        self.rq_alpha.value = defaults.rational_quadratic_alpha
        self._manual_hyperparameters = {
            "length_scale": float(defaults.length_scale),
            "sigma_f": float(defaults.sigma_f),
            "sigma_n": float(defaults.sigma_n),
            "matern_nu": float(defaults.matern_nu),
            "rational_quadratic_alpha": float(defaults.rational_quadratic_alpha),
        }
        self._showing_effective_hyperparameters = False
        self._set_hyperparameter_labels(optimized=False)
        self.optimize_hyperparameters.value = defaults.optimize_hyperparameters
        self.normalize_target.value = defaults.normalize_target
        self.optimizer_restarts.value = defaults.optimizer_restarts
        self._update_kernel_parameter_controls()
        self.prediction_min.value = defaults.prediction_min
        self.prediction_max.value = defaults.prediction_max
        self.prediction_points.value = defaults.prediction_points
        self.confidence_level.value = defaults.confidence_level
        self._analysis_signature = None

    def _update_kernel_parameter_controls(self) -> None:
        controls = [
            self.length_scale,
            self.sigma_f,
            self.sigma_n,
        ]
        if self.kernel.value == "Matérn":
            controls.append(self.matern_nu)
        elif self.kernel.value == "Rational Quadratic":
            controls.append(self.rq_alpha)
        self.kernel_parameters.objects = controls

    def _on_kernel_changed(self, _event: Any) -> None:
        self._update_kernel_parameter_controls()
        if self._updating or not self.live_update.value:
            return
        self._fit(force=False)

    def _on_live_update_changed(self, event: Any) -> None:
        self.fit_button.disabled = bool(event.new) or self.dataset is None
        if event.new:
            self._fit(force=False)

    def _set_hyperparameter_labels(self, *, optimized: bool) -> None:
        prefix = "Optimized " if optimized else ""
        self.length_scale.name = f"{prefix}characteristic length-scale ℓ"
        self.sigma_f.name = f"{prefix}signal standard deviation σ_f"
        self.sigma_n.name = "Noise standard deviation σ_n"
        self.matern_nu.name = "Smoothness parameter ν"
        self.rq_alpha.name = f"{prefix}Rational Quadratic parameter α"

    def _remember_manual_hyperparameter(self, widget: Any, value: float) -> None:
        mapping = {
            self.length_scale: "length_scale",
            self.sigma_f: "sigma_f",
            self.sigma_n: "sigma_n",
            self.matern_nu: "matern_nu",
            self.rq_alpha: "rational_quadratic_alpha",
        }
        key = mapping.get(widget)
        if key is not None:
            self._manual_hyperparameters[key] = float(value)

    def _restore_manual_hyperparameters(self) -> None:
        if not self._manual_hyperparameters:
            return
        self._updating = True
        try:
            self.length_scale.value = self._manual_hyperparameters["length_scale"]
            self.sigma_f.value = self._manual_hyperparameters["sigma_f"]
            self.sigma_n.value = self._manual_hyperparameters["sigma_n"]
            self.matern_nu.value = self._manual_hyperparameters["matern_nu"]
            self.rq_alpha.value = self._manual_hyperparameters[
                "rational_quadratic_alpha"
            ]
            self._showing_effective_hyperparameters = False
            self._set_hyperparameter_labels(optimized=False)
        finally:
            self._updating = False

    def _display_effective_hyperparameters(self, result: PredictionResult) -> None:
        summary = result.hyperparameters
        if not summary.optimization_enabled:
            self._showing_effective_hyperparameters = False
            self._set_hyperparameter_labels(optimized=False)
            return

        self._updating = True
        try:
            self.length_scale.value = float(summary.effective_length_scale)
            self.sigma_f.value = float(summary.effective_sigma_f)
            self.sigma_n.value = float(summary.sigma_n)
            if summary.matern_nu is not None:
                self.matern_nu.value = float(summary.matern_nu)
            if summary.effective_rational_quadratic_alpha is not None:
                self.rq_alpha.value = float(
                    summary.effective_rational_quadratic_alpha
                )
            self._showing_effective_hyperparameters = True
            self._set_hyperparameter_labels(optimized=True)
        finally:
            self._updating = False

    def _on_hyperparameter_input_changed(self, event: Any) -> None:
        if self._updating:
            return
        self._remember_manual_hyperparameter(event.obj, float(event.new))
        self._showing_effective_hyperparameters = False
        self._set_hyperparameter_labels(optimized=False)
        self._on_model_setting_changed(event)

    def _on_optimization_toggled(self, event: Any) -> None:
        if self._updating or self.dataset is None:
            return

        # Switching optimization off restores the user's last explicit values.
        # Switching it on starts optimization from those same values.
        self._restore_manual_hyperparameters()
        self._fit(force=True)

    def _on_model_setting_changed(self, _event: Any) -> None:
        if self._updating:
            return
        if self.live_update.value:
            self._fit(force=False)
            return
        if self.result is not None:
            self.details.object = (
                "### Effective hyperparameters\n\n"
                "**Model settings changed — select Fit model to refresh the effective values.**"
            )
            self.download_csv.disabled = True
            self.download_html.disabled = True
            self.download_json.disabled = True
            self.download_model.disabled = True
            self.predict_one_button.disabled = True
            self.predict_many_button.disabled = True

    def _settings(self) -> GprSettings:
        use_manual = bool(self.optimize_hyperparameters.value) and bool(
            self._manual_hyperparameters
        )
        length_scale = (
            self._manual_hyperparameters["length_scale"]
            if use_manual
            else float(self.length_scale.value)
        )
        sigma_f = (
            self._manual_hyperparameters["sigma_f"]
            if use_manual
            else float(self.sigma_f.value)
        )
        sigma_n = (
            self._manual_hyperparameters["sigma_n"]
            if use_manual
            else float(self.sigma_n.value)
        )
        matern_nu = (
            self._manual_hyperparameters["matern_nu"]
            if use_manual
            else float(self.matern_nu.value)
        )
        rq_alpha = (
            self._manual_hyperparameters["rational_quadratic_alpha"]
            if use_manual
            else float(self.rq_alpha.value)
        )

        return GprSettings(
            covariance_function=str(self.kernel.value),
            length_scale=float(length_scale),
            sigma_f=float(sigma_f),
            sigma_n=float(sigma_n),
            matern_nu=float(matern_nu),
            rational_quadratic_alpha=float(rq_alpha),
            optimize_hyperparameters=bool(self.optimize_hyperparameters.value),
            normalize_target=bool(self.normalize_target.value),
            optimizer_restarts=int(self.optimizer_restarts.value),
            prediction_min=float(self.prediction_min.value),
            prediction_max=float(self.prediction_max.value),
            prediction_points=int(self.prediction_points.value),
            confidence_level=float(self.confidence_level.value),
        )

    def _signature(self, settings: GprSettings) -> tuple[Any, ...]:
        assert self.dataset is not None
        assert self.selection is not None
        return (
            self.dataset.content_hash,
            self.selection.x_column,
            self.selection.y_column,
            *asdict(settings).values(),
        )

    def _fit(self, *, force: bool) -> None:
        if self.dataset is None or self.selection is None:
            return
        try:
            settings = self._settings()
            signature = self._signature(settings)
            if not force and signature == self._analysis_signature:
                return
            self.message.object = "Fitting Gaussian Process…"
            self.message.alert_type = "info"
            self.message.visible = True
            bundle = fit_gpr_bundle(self.dataset, self.selection, settings)
            result = bundle.prediction
            artifact = create_model_artifact(
                model=bundle.model,
                selected_variables=result.selected_variables,
                training_x_min=result.observed_x_min,
                training_x_max=result.observed_x_max,
                confidence_level=result.settings.confidence_level,
                settings=result.settings,
                initial_kernel=bundle.initial_kernel,
                fitted_kernel=bundle.fitted_kernel,
                source_filename=self.dataset.filename or "",
                source_sha256=self.dataset.content_hash,
            )
        except (ValidationError, ModelSettingsError, ModelFitError, ValueError) as exc:
            self._show_error(str(exc))
            return

        self.result = result
        self.artifact = artifact
        self.inference_results = ()
        self._analysis_signature = signature
        self._display_effective_hyperparameters(result)
        self._set_default_view(result)
        self._update_plot()
        self._update_summary()
        self.download_csv.disabled = False
        self.download_html.disabled = False
        self.download_json.disabled = False
        self.download_model.disabled = False
        self.predict_one_button.disabled = False
        self.predict_many_button.disabled = False
        self.download_inference_csv.disabled = True
        self.inference_x.value = float((result.observed_x_min + result.observed_x_max) / 2.0)
        self.inference_summary.object = (
            "<span class='ge-status-muted'>Enter a new X value and select Predict value.</span>"
        )
        self.inference_table.value = pd.DataFrame()
        self.message.object = "Gaussian Process model fitted successfully."
        self.message.alert_type = "success"

    def _set_default_view(self, result: PredictionResult) -> None:
        defaults = default_plot_settings(result)
        self._updating = True
        try:
            self.x_min.value = defaults.x_min
            self.x_max.value = defaults.x_max
            self.y_min.value = defaults.y_min
            self.y_max.value = defaults.y_max
        finally:
            self._updating = False

    def _plot_settings(self) -> PlotSettings:
        return PlotSettings(
            x_min=self.x_min.value,
            x_max=self.x_max.value,
            y_min=self.y_min.value,
            y_max=self.y_max.value,
            show_confidence=self.show_confidence.value,
            show_observations=self.show_observations.value,
            show_regions=self.show_regions.value,
        )

    def _on_plot_setting_changed(self, _event: Any) -> None:
        if self._updating:
            return
        self._update_plot()

    def _update_plot(self) -> None:
        if self.result is None:
            return
        try:
            figure = build_prediction_figure(self.result, self._plot_settings())
        except (TypeError, ValueError, RuntimeError) as exc:
            self._show_error(str(exc))
            return
        self.plot_pane.object = figure

    def _use_full_range(self) -> None:
        if self.result is None:
            return
        self._apply_view(default_plot_settings(self.result))

    def _focus_iid(self) -> None:
        if self.result is None:
            return
        focused = plot_settings_for_x_domain(
            self.result,
            self.result.observed_x_min,
            self.result.observed_x_max,
        )
        self._apply_view(focused)

    def _apply_view(self, settings: PlotSettings) -> None:
        self._updating = True
        try:
            self.x_min.value = settings.x_min
            self.x_max.value = settings.x_max
            self.y_min.value = settings.y_min
            self.y_max.value = settings.y_max
        finally:
            self._updating = False
        self._update_plot()

    def _update_summary(self) -> None:
        if self.result is None:
            return
        result = self.result
        summary = result.hyperparameters
        self.metric_observed.object = self._metric_html(
            "Observed points", str(len(result.training_x))
        )
        self.metric_iid.object = self._metric_html(
            "IID prediction points", str(result.regions.count("iid"))
        )
        self.metric_ood.object = self._metric_html(
            "OOD prediction points", str(result.regions.count("ood"))
        )
        self.metric_confidence.object = self._metric_html(
            "Confidence level", f"{result.settings.confidence_level:.0%}"
        )

        if summary.optimization_enabled:
            rows = [
                (
                    "Characteristic length-scale ℓ",
                    summary.initial_length_scale,
                    summary.effective_length_scale,
                    "Optimized",
                ),
                (
                    "Signal standard deviation σ_f",
                    summary.initial_sigma_f,
                    summary.effective_sigma_f,
                    "Optimized",
                ),
                (
                    "Noise standard deviation σ_n",
                    summary.sigma_n,
                    summary.sigma_n,
                    "Fixed",
                ),
            ]
            if summary.matern_nu is not None:
                rows.append(("Smoothness parameter ν", summary.matern_nu, summary.matern_nu, "Fixed"))
            if summary.initial_rational_quadratic_alpha is not None:
                rows.append(
                    (
                        "Rational Quadratic parameter α",
                        summary.initial_rational_quadratic_alpha,
                        summary.effective_rational_quadratic_alpha,
                        "Optimized",
                    )
                )

            table_rows = "\n".join(
                f"| {name} | {initial:.6g} | {effective:.6g} | {status} |"
                for name, initial, effective, status in rows
            )
            likelihood = (
                f"{summary.log_marginal_likelihood:.6g}"
                if summary.log_marginal_likelihood is not None
                else "Not available"
            )
            hyperparameter_block = (
                "### Effective hyperparameters\n\n"
                "**Status:** Optimized by scikit-learn  \n\n"
                "| Hyperparameter | Initial | Effective | Status |\n"
                "|---|---:|---:|---|\n"
                f"{table_rows}\n\n"
                f"**Log marginal likelihood:** `{likelihood}`"
            )
        else:
            rows = [
                ("Characteristic length-scale ℓ", summary.initial_length_scale),
                ("Signal standard deviation σ_f", summary.initial_sigma_f),
                ("Noise standard deviation σ_n", summary.sigma_n),
            ]
            if summary.matern_nu is not None:
                rows.append(("Smoothness parameter ν", summary.matern_nu))
            if summary.initial_rational_quadratic_alpha is not None:
                rows.append(
                    (
                        "Rational Quadratic parameter α",
                        summary.initial_rational_quadratic_alpha,
                    )
                )
            table_rows = "\n".join(
                f"| {name} | {value:.6g} |" for name, value in rows
            )
            hyperparameter_block = (
                "### Effective hyperparameters\n\n"
                "**Status:** Fixed user values  \n\n"
                "| Hyperparameter | Value |\n"
                "|---|---:|\n"
                f"{table_rows}\n\n"
                "Optimization was disabled; the entered values were used without modification."
            )

        fitted_kernel = self.artifact.fitted_kernel if self.artifact else "—"
        initial_kernel = self.artifact.initial_kernel if self.artifact else "—"
        self.details.object = (
            f"{hyperparameter_block}\n\n"
            "### Fit configuration\n\n"
            f"**Covariance function:** {result.settings.covariance_function}  \n"
            f"**Initial covariance:** `{initial_kernel}`  \n"
            f"**Fitted covariance:** `{fitted_kernel}`  \n"
            f"**Normalize target:** {result.settings.normalize_target}  \n"
            f"**Optimizer restarts:** {result.settings.optimizer_restarts}  \n"
            f"**Observed X domain:** [{result.observed_x_min:.6g}, {result.observed_x_max:.6g}]  \n"
            f"**Prediction domain:** [{result.settings.prediction_min:.6g}, {result.settings.prediction_max:.6g}]  \n"
            f"**Prediction points:** {result.settings.prediction_points}"
        )

    @staticmethod
    def _parse_batch_values(text: str) -> tuple[float, ...]:
        tokens = text.replace(",", " ").split()
        if not tokens:
            raise InferenceError("Enter at least one X value.")
        try:
            return tuple(float(token) for token in tokens)
        except ValueError as exc:
            raise InferenceError(
                "Batch values must be numbers separated by commas, spaces, or new lines."
            ) from exc

    def _predict_one(self) -> None:
        if self.artifact is None:
            self._show_error("Fit a model before running inference.")
            return
        try:
            result = self.artifact.predict_one(float(self.inference_x.value))
        except (InferenceError, ValueError) as exc:
            self._show_error(str(exc))
            return
        self.inference_results = (result,)
        self.inference_summary.object = (
            "<div class='ge-card'>"
            f"<div><strong>X:</strong> {result.x:.6g}</div>"
            f"<div><strong>Predicted mean:</strong> {result.predicted_mean:.6g}</div>"
            f"<div><strong>Predictive standard deviation:</strong> "
            f"{result.predictive_standard_deviation:.6g}</div>"
            f"<div><strong>{result.confidence_level:.0%} interval:</strong> "
            f"[{result.lower_bound:.6g}, {result.upper_bound:.6g}]</div>"
            f"<div><strong>Region:</strong> {result.region.upper()}</div>"
            "</div>"
        )
        self.inference_table.value = pd.DataFrame([asdict(result)])
        self.download_inference_csv.disabled = False

    def _predict_many(self) -> None:
        if self.artifact is None:
            self._show_error("Fit a model before running inference.")
            return
        try:
            values = self._parse_batch_values(self.batch_values.value)
            results = self.artifact.predict_many(values)
        except (InferenceError, ValueError) as exc:
            self._show_error(str(exc))
            return
        self.inference_results = results
        self.inference_table.value = pd.DataFrame(asdict(item) for item in results)
        self.inference_summary.object = (
            f"<span class='ge-status-ok'>Predicted {len(results)} new values.</span>"
        )
        self.download_inference_csv.disabled = False

    def _show_error(self, message: str) -> None:
        self.message.object = message
        self.message.alert_type = "danger"
        self.message.visible = True
        if pn.state.notifications:
            pn.state.notifications.error(message, duration=5000)

    def _require_exports(self) -> tuple[UploadedDataset, PredictionResult]:
        if self.dataset is None or self.result is None:
            raise RuntimeError("Fit a model before exporting results.")
        return self.dataset, self.result

    def _download_csv(self) -> io.BytesIO:
        _, result = self._require_exports()
        return io.BytesIO(build_results_csv(result))

    def _download_html(self) -> io.BytesIO:
        _, result = self._require_exports()
        figure = build_prediction_figure(result, self._plot_settings())
        return io.BytesIO(build_plot_html(figure))

    def _download_inference_csv(self) -> io.BytesIO:
        if not self.inference_results:
            raise RuntimeError("Run inference before downloading inference results.")
        return io.BytesIO(inference_results_csv(self.inference_results))

    def _download_model(self) -> io.BytesIO:
        if self.artifact is None:
            raise RuntimeError("Fit a model before downloading it.")
        return io.BytesIO(serialize_model_artifact(self.artifact))

    def _download_json(self) -> io.BytesIO:
        dataset, result = self._require_exports()
        metadata = build_visualization_metadata(result)
        return io.BytesIO(build_metadata_json(dataset, result, metadata))

    def view(self):
        return self.template


def create_app():
    """Create one application instance for the current Panel session."""

    return GaussianExplorerApp().view()


create_app().servable()
