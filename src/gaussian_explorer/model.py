"""Gaussian Process Regression configuration, fitting, and prediction."""

from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Any

from gaussian_explorer.data import UploadedDataset
from gaussian_explorer.validation import (
    SelectedVariables,
    ValidationError,
    validate_selected_data,
)

SQUARED_EXPONENTIAL = "Squared Exponential"
MATERN = "Matérn"
RATIONAL_QUADRATIC = "Rational Quadratic"
SUPPORTED_KERNELS = (SQUARED_EXPONENTIAL, MATERN, RATIONAL_QUADRATIC)
IID_REGION = "iid"
OOD_REGION = "ood"


class ModelSettingsError(ValueError):
    """Raised when model settings are invalid."""


class ModelFitError(RuntimeError):
    """Raised when a valid analysis cannot be fitted safely."""


@dataclass(frozen=True, slots=True)
class GprSettings:
    """User-facing GPR settings using GPML book terminology."""

    covariance_function: str = SQUARED_EXPONENTIAL
    length_scale: float = 1.0
    sigma_f: float = 1.0
    sigma_n: float = 1e-3
    matern_nu: float = 1.5
    rational_quadratic_alpha: float = 1.0
    optimize_hyperparameters: bool = True
    normalize_target: bool = True
    optimizer_restarts: int = 0
    prediction_min: float = 0.0
    prediction_max: float = 1.0
    prediction_points: int = 300
    confidence_level: float = 0.95

    @property
    def kernel(self) -> str:
        """Compatibility alias for older exports and callers."""

        return self.covariance_function

    @property
    def signal_variance(self) -> float:
        """Derived signal variance sigma_f squared."""

        return self.sigma_f**2

    @property
    def noise_variance(self) -> float:
        """Derived noise variance sigma_n squared."""

        return self.sigma_n**2

    @property
    def noise_level(self) -> float:
        """Compatibility alias for the derived noise variance."""

        return self.noise_variance


@dataclass(frozen=True, slots=True)
class HyperparameterSummary:
    """Initial and effective hyperparameters for one fitted model."""

    optimization_enabled: bool
    initial_length_scale: float
    effective_length_scale: float
    initial_sigma_f: float
    effective_sigma_f: float
    sigma_n: float
    matern_nu: float | None = None
    initial_rational_quadratic_alpha: float | None = None
    effective_rational_quadratic_alpha: float | None = None
    log_marginal_likelihood: float | None = None


@dataclass(frozen=True, slots=True)
class PredictionResult:
    x_values: tuple[float, ...]
    mean: tuple[float, ...]
    standard_deviation: tuple[float, ...]
    lower_bound: tuple[float, ...]
    upper_bound: tuple[float, ...]
    regions: tuple[str, ...]
    training_x: tuple[float, ...]
    training_y: tuple[float, ...]
    observed_x_min: float
    observed_x_max: float
    selected_variables: SelectedVariables
    settings: GprSettings
    confidence_multiplier: float
    hyperparameters: HyperparameterSummary

    def __post_init__(self) -> None:
        prediction_lengths = {
            len(self.x_values),
            len(self.mean),
            len(self.standard_deviation),
            len(self.lower_bound),
            len(self.upper_bound),
            len(self.regions),
        }
        if len(prediction_lengths) != 1:
            raise ValueError("All prediction arrays must have equal lengths.")
        if len(self.training_x) != len(self.training_y):
            raise ValueError("Training X and Y arrays must have equal lengths.")


@dataclass(frozen=True, slots=True)
class ModelFitBundle:
    """One fitted estimator, its plotted prediction result, and covariance details."""

    model: Any
    prediction: PredictionResult
    initial_kernel: str
    fitted_kernel: str


def default_gpr_settings(
    dataset: UploadedDataset,
    variables: SelectedVariables,
) -> GprSettings:
    """Create defaults with a visible OOD margin on each side of training data."""

    selected = validate_selected_data(dataset, variables)
    span = selected.x_max - selected.x_min
    margin = span * 0.20
    signal_variance = max(
        sum((value - sum(selected.y_values) / len(selected.y_values)) ** 2 for value in selected.y_values)
        / max(len(selected.y_values), 1),
        1e-12,
    )
    sigma_f = math.sqrt(signal_variance)
    return GprSettings(
        covariance_function=SQUARED_EXPONENTIAL,
        length_scale=max(span / 5.0, 1e-12),
        sigma_f=sigma_f,
        sigma_n=1e-3,
        matern_nu=1.5,
        rational_quadratic_alpha=1.0,
        optimize_hyperparameters=True,
        normalize_target=True,
        optimizer_restarts=0,
        prediction_min=selected.x_min - margin,
        prediction_max=selected.x_max + margin,
        prediction_points=300,
        confidence_level=0.95,
    )


def validate_gpr_settings(settings: GprSettings) -> GprSettings:
    numeric_values = {
        "characteristic length-scale": settings.length_scale,
        "signal standard deviation": settings.sigma_f,
        "noise standard deviation": settings.sigma_n,
        "Matérn smoothness parameter": settings.matern_nu,
        "Rational Quadratic parameter alpha": settings.rational_quadratic_alpha,
        "prediction minimum": settings.prediction_min,
        "prediction maximum": settings.prediction_max,
        "confidence level": settings.confidence_level,
    }
    for name, value in numeric_values.items():
        if not math.isfinite(value):
            raise ModelSettingsError(f"{name.capitalize()} must be finite.")
    if settings.covariance_function not in SUPPORTED_KERNELS:
        raise ModelSettingsError(
            "Unsupported covariance function "
            f"'{settings.covariance_function}'. Use: {', '.join(SUPPORTED_KERNELS)}."
        )
    if settings.length_scale <= 0:
        raise ModelSettingsError("Characteristic length-scale must be greater than zero.")
    if settings.sigma_f <= 0:
        raise ModelSettingsError("Sigma f must be greater than zero.")
    if settings.sigma_n <= 0:
        raise ModelSettingsError("Sigma n must be greater than zero.")
    if settings.matern_nu not in (0.5, 1.5, 2.5):
        raise ModelSettingsError("Matérn nu must be one of: 1/2, 3/2, or 5/2.")
    if settings.rational_quadratic_alpha <= 0:
        raise ModelSettingsError("Rational Quadratic alpha must be greater than zero.")
    if settings.optimizer_restarts < 0 or settings.optimizer_restarts > 20:
        raise ModelSettingsError("Optimizer restarts must be between 0 and 20.")
    if settings.prediction_min >= settings.prediction_max:
        raise ModelSettingsError("Prediction minimum must be less than prediction maximum.")
    if not 20 <= settings.prediction_points <= 5_000:
        raise ModelSettingsError("Prediction points must be between 20 and 5,000.")
    if not 0.50 < settings.confidence_level < 0.999:
        raise ModelSettingsError("Confidence level must be between 0.50 and 0.999.")
    return settings


def _build_kernel(settings: GprSettings):
    try:
        from sklearn.gaussian_process.kernels import (
            ConstantKernel,
            Matern,
            RBF,
            RationalQuadratic,
        )
    except ImportError as exc:  # pragma: no cover
        raise ModelFitError("scikit-learn is required for model fitting.") from exc

    # Keep optimization inside a scientifically meaningful neighborhood of
    # the values entered by the user. Extremely broad bounds such as
    # (1e-12, 1e12) can make the optimizer collapse the length-scale to an
    # almost-zero value, producing a flat prior-mean curve between samples.
    signal_variance = settings.sigma_f**2
    signal = ConstantKernel(
        constant_value=signal_variance,
        constant_value_bounds=(
            max(signal_variance / 100.0, 1e-12),
            max(signal_variance * 100.0, 1e-10),
        ),
    )

    length_scale_bounds = (
        max(settings.length_scale / 100.0, 1e-8),
        max(settings.length_scale * 100.0, 1e-6),
    )

    if settings.covariance_function == SQUARED_EXPONENTIAL:
        base = RBF(
            length_scale=settings.length_scale,
            length_scale_bounds=length_scale_bounds,
        )
    elif settings.covariance_function == MATERN:
        base = Matern(
            length_scale=settings.length_scale,
            length_scale_bounds=length_scale_bounds,
            nu=settings.matern_nu,
        )
    elif settings.covariance_function == RATIONAL_QUADRATIC:
        base = RationalQuadratic(
            length_scale=settings.length_scale,
            alpha=settings.rational_quadratic_alpha,
            length_scale_bounds=length_scale_bounds,
            alpha_bounds=(
                max(settings.rational_quadratic_alpha / 100.0, 1e-8),
                max(settings.rational_quadratic_alpha * 100.0, 1e-6),
            ),
        )
    else:  # pragma: no cover - validated before this point
        raise ModelSettingsError(
            f"Unsupported covariance function '{settings.covariance_function}'."
        )

    return signal * base


def _extract_hyperparameter_summary(settings: GprSettings, model: Any) -> HyperparameterSummary:
    """Extract the values actually used by the fitted scikit-learn estimator."""

    fitted_kernel = model.kernel_
    signal_variance = float(fitted_kernel.k1.constant_value)
    effective_sigma_f = math.sqrt(signal_variance)
    base_kernel = fitted_kernel.k2
    effective_length_scale = float(base_kernel.length_scale)

    initial_rq_alpha: float | None = None
    effective_rq_alpha: float | None = None
    matern_nu: float | None = None

    if settings.covariance_function == MATERN:
        matern_nu = float(base_kernel.nu)
    elif settings.covariance_function == RATIONAL_QUADRATIC:
        initial_rq_alpha = settings.rational_quadratic_alpha
        effective_rq_alpha = float(base_kernel.alpha)

    likelihood = getattr(model, "log_marginal_likelihood_value_", None)

    return HyperparameterSummary(
        optimization_enabled=settings.optimize_hyperparameters,
        initial_length_scale=settings.length_scale,
        effective_length_scale=effective_length_scale,
        initial_sigma_f=settings.sigma_f,
        effective_sigma_f=effective_sigma_f,
        sigma_n=settings.sigma_n,
        matern_nu=matern_nu,
        initial_rational_quadratic_alpha=initial_rq_alpha,
        effective_rational_quadratic_alpha=effective_rq_alpha,
        log_marginal_likelihood=(
            float(likelihood) if likelihood is not None and math.isfinite(float(likelihood)) else None
        ),
    )


def fit_gpr_bundle(
    dataset: UploadedDataset,
    variables: SelectedVariables,
    settings: GprSettings,
) -> ModelFitBundle:
    """Fit GPR and retain the estimator for later inference and export.

    Users enter sigma_n directly. The book's K + sigma_n^2 I convention is
    implemented by squaring it before passing it to GaussianProcessRegressor.
    """

    try:
        import numpy as np
        from scipy.stats import norm
        from sklearn.gaussian_process import GaussianProcessRegressor
    except ImportError as exc:  # pragma: no cover
        raise ModelFitError("NumPy, SciPy, and scikit-learn are required for fitting.") from exc

    valid_settings = validate_gpr_settings(settings)
    selected = validate_selected_data(dataset, variables)

    try:
        x_train = np.asarray(selected.x_values, dtype=float).reshape(-1, 1)
        y_train = np.asarray(selected.y_values, dtype=float)
        x_grid = np.linspace(
            valid_settings.prediction_min,
            valid_settings.prediction_max,
            valid_settings.prediction_points,
            dtype=float,
        )
        kernel = _build_kernel(valid_settings)
        initial_kernel = str(kernel)
        model = GaussianProcessRegressor(
            kernel=kernel,
            alpha=valid_settings.sigma_n**2,
            normalize_y=valid_settings.normalize_target,
            optimizer="fmin_l_bfgs_b" if valid_settings.optimize_hyperparameters else None,
            n_restarts_optimizer=(
                valid_settings.optimizer_restarts
                if valid_settings.optimize_hyperparameters
                else 0
            ),
            random_state=0,
        )
        model.fit(x_train, y_train)
        mean, std = model.predict(x_grid.reshape(-1, 1), return_std=True)
        multiplier = float(norm.ppf((1.0 + valid_settings.confidence_level) / 2.0))
        lower = mean - multiplier * std
        upper = mean + multiplier * std

        arrays = (x_grid, mean, std, lower, upper)
        if not all(np.all(np.isfinite(values)) for values in arrays):
            raise ModelFitError("The model produced non-finite prediction values.")

        regions = np.where(
            (x_grid >= selected.x_min) & (x_grid <= selected.x_max),
            IID_REGION,
            OOD_REGION,
        )
        prediction = PredictionResult(
            x_values=tuple(float(value) for value in x_grid),
            mean=tuple(float(value) for value in mean),
            standard_deviation=tuple(float(value) for value in std),
            lower_bound=tuple(float(value) for value in lower),
            upper_bound=tuple(float(value) for value in upper),
            regions=tuple(str(value) for value in regions),
            training_x=selected.x_values,
            training_y=selected.y_values,
            observed_x_min=selected.x_min,
            observed_x_max=selected.x_max,
            selected_variables=selected.variables,
            settings=valid_settings,
            confidence_multiplier=multiplier,
            hyperparameters=_extract_hyperparameter_summary(valid_settings, model),
        )
        return ModelFitBundle(
            model=model,
            prediction=prediction,
            initial_kernel=initial_kernel,
            fitted_kernel=str(model.kernel_),
        )
    except (ValidationError, ModelSettingsError, ModelFitError):
        raise
    except Exception as exc:
        raise ModelFitError(f"The Gaussian Process model could not be fitted: {exc}") from exc


def fit_gpr(
    dataset: UploadedDataset,
    variables: SelectedVariables,
    settings: GprSettings,
) -> PredictionResult:
    """Fit GPR and return predictions for plotting and tabular export."""

    return fit_gpr_bundle(dataset, variables, settings).prediction
