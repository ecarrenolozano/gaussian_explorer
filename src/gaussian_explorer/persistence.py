"""Versioned persistence for fitted Gaussian Process inference artifacts."""

from __future__ import annotations

import io
import platform
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable

from gaussian_explorer.inference import InferenceResult, predict_many, predict_one
from gaussian_explorer.model import GprSettings
from gaussian_explorer.validation import SelectedVariables

MODEL_ARTIFACT_FORMAT_VERSION = "1.0"


class ModelPersistenceError(RuntimeError):
    """Raised when a fitted model cannot be serialized or loaded safely."""


@dataclass(slots=True)
class GaussianProcessArtifact:
    """Reusable fitted model plus the metadata required for inference."""

    format_version: str
    created_at_utc: str
    model: Any
    selected_variables: SelectedVariables
    training_x_min: float
    training_x_max: float
    confidence_level: float
    settings: GprSettings
    initial_kernel: str
    fitted_kernel: str
    source_filename: str
    source_sha256: str
    python_version: str
    numpy_version: str
    scipy_version: str
    scikit_learn_version: str

    def predict_one(
        self,
        x: float,
        *,
        confidence_level: float | None = None,
    ) -> InferenceResult:
        return predict_one(
            self.model,
            x,
            training_x_min=self.training_x_min,
            training_x_max=self.training_x_max,
            confidence_level=(
                self.confidence_level
                if confidence_level is None
                else confidence_level
            ),
        )

    def predict_many(
        self,
        x_values: Iterable[float],
        *,
        confidence_level: float | None = None,
    ) -> tuple[InferenceResult, ...]:
        return predict_many(
            self.model,
            x_values,
            training_x_min=self.training_x_min,
            training_x_max=self.training_x_max,
            confidence_level=(
                self.confidence_level
                if confidence_level is None
                else confidence_level
            ),
        )


def create_model_artifact(
    *,
    model: Any,
    selected_variables: SelectedVariables,
    training_x_min: float,
    training_x_max: float,
    confidence_level: float,
    settings: GprSettings,
    initial_kernel: str,
    fitted_kernel: str,
    source_filename: str,
    source_sha256: str,
) -> GaussianProcessArtifact:
    """Create a versioned inference artifact from one successfully fitted model."""

    try:
        import numpy
        import scipy
        import sklearn
    except ImportError as exc:  # pragma: no cover
        raise ModelPersistenceError(
            "NumPy, SciPy, and scikit-learn must be installed to create an artifact."
        ) from exc

    return GaussianProcessArtifact(
        format_version=MODEL_ARTIFACT_FORMAT_VERSION,
        created_at_utc=datetime.now(timezone.utc).isoformat(),
        model=model,
        selected_variables=selected_variables,
        training_x_min=float(training_x_min),
        training_x_max=float(training_x_max),
        confidence_level=float(confidence_level),
        settings=settings,
        initial_kernel=initial_kernel,
        fitted_kernel=fitted_kernel,
        source_filename=source_filename,
        source_sha256=source_sha256,
        python_version=platform.python_version(),
        numpy_version=numpy.__version__,
        scipy_version=scipy.__version__,
        scikit_learn_version=sklearn.__version__,
    )


def serialize_model_artifact(artifact: GaussianProcessArtifact) -> bytes:
    """Serialize an artifact to joblib bytes suitable for browser download."""

    try:
        import joblib
    except ImportError as exc:  # pragma: no cover
        raise ModelPersistenceError("joblib is required to export fitted models.") from exc

    buffer = io.BytesIO()
    try:
        joblib.dump(artifact, buffer)
    except Exception as exc:
        raise ModelPersistenceError(f"The fitted model could not be serialized: {exc}") from exc
    return buffer.getvalue()


def save_model_artifact(
    artifact: GaussianProcessArtifact,
    destination: str | Path,
) -> Path:
    """Persist an artifact to a local path."""

    path = Path(destination)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(serialize_model_artifact(artifact))
    return path


def load_model_artifact(source: str | Path | bytes | bytearray) -> GaussianProcessArtifact:
    """Load a trusted artifact and validate its format version.

    Never load joblib files received from an untrusted source because pickle-based
    formats may execute arbitrary code during deserialization.
    """

    try:
        import joblib
    except ImportError as exc:  # pragma: no cover
        raise ModelPersistenceError("joblib is required to load fitted models.") from exc

    try:
        if isinstance(source, (bytes, bytearray)):
            artifact = joblib.load(io.BytesIO(source))
        else:
            artifact = joblib.load(Path(source))
    except Exception as exc:
        raise ModelPersistenceError(f"The model artifact could not be loaded: {exc}") from exc

    if not isinstance(artifact, GaussianProcessArtifact):
        raise ModelPersistenceError("The file is not a Gaussian Process artifact.")
    if artifact.format_version != MODEL_ARTIFACT_FORMAT_VERSION:
        raise ModelPersistenceError(
            "Unsupported model artifact format version: "
            f"{artifact.format_version!r}."
        )
    return artifact
