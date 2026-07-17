"""Variable selection and numerical data validation."""

from __future__ import annotations

import math
from dataclasses import dataclass

from gaussian_explorer.data import UploadedDataset

MIN_FIT_ROWS = 3


class ValidationError(ValueError):
    """Raised when selected analysis inputs are invalid."""


@dataclass(frozen=True, slots=True)
class SelectedVariables:
    x_column: str
    y_column: str


@dataclass(frozen=True, slots=True)
class SelectedData:
    x_values: tuple[float, ...]
    y_values: tuple[float, ...]
    variables: SelectedVariables

    @property
    def x_min(self) -> float:
        return self.x_values[0]

    @property
    def x_max(self) -> float:
        return self.x_values[-1]


def _to_finite_float(value: str, *, column: str, row_number: int) -> float:
    stripped = value.strip()
    if not stripped:
        raise ValidationError(
            f"Column '{column}' contains a missing value at data row {row_number}."
        )
    try:
        number = float(stripped)
    except ValueError as exc:
        raise ValidationError(
            f"Column '{column}' contains a non-numeric value at data row {row_number}."
        ) from exc
    if not math.isfinite(number):
        raise ValidationError(
            f"Column '{column}' contains a non-finite value at data row {row_number}."
        )
    return number


def find_numeric_columns(dataset: UploadedDataset) -> tuple[str, ...]:
    """Return columns containing only finite numeric values and no blanks."""

    numeric: list[str] = []
    for column in dataset.columns:
        try:
            for row_number, value in enumerate(dataset.column_values(column), start=1):
                _to_finite_float(value, column=column, row_number=row_number)
        except ValidationError:
            continue
        numeric.append(column)
    return tuple(numeric)


def validate_selected_variables(
    dataset: UploadedDataset,
    x_column: str,
    y_column: str,
) -> SelectedVariables:
    if x_column not in dataset.columns:
        raise ValidationError(f"Unknown X column: '{x_column}'.")
    if y_column not in dataset.columns:
        raise ValidationError(f"Unknown Y column: '{y_column}'.")
    if x_column == y_column:
        raise ValidationError("X and Y must be different columns.")

    numeric = find_numeric_columns(dataset)
    if len(numeric) < 2:
        raise ValidationError("The dataset must contain at least two numeric columns.")
    if x_column not in numeric:
        raise ValidationError(f"X column '{x_column}' is not fully numeric.")
    if y_column not in numeric:
        raise ValidationError(f"Y column '{y_column}' is not fully numeric.")
    return SelectedVariables(x_column=x_column, y_column=y_column)


def validate_selected_data(
    dataset: UploadedDataset,
    variables: SelectedVariables,
) -> SelectedData:
    """Extract, validate, and sort the selected X/Y observations."""

    valid = validate_selected_variables(dataset, variables.x_column, variables.y_column)
    x_raw = dataset.column_values(valid.x_column)
    y_raw = dataset.column_values(valid.y_column)
    pairs: list[tuple[float, float]] = []
    for row_number, (x_value, y_value) in enumerate(zip(x_raw, y_raw, strict=True), start=1):
        pairs.append(
            (
                _to_finite_float(x_value, column=valid.x_column, row_number=row_number),
                _to_finite_float(y_value, column=valid.y_column, row_number=row_number),
            )
        )

    if len(pairs) < MIN_FIT_ROWS:
        raise ValidationError(f"At least {MIN_FIT_ROWS} valid rows are required.")
    x_values = [pair[0] for pair in pairs]
    if len(set(x_values)) != len(x_values):
        raise ValidationError("The selected X column contains duplicate values.")

    pairs.sort(key=lambda item: item[0])
    return SelectedData(
        x_values=tuple(item[0] for item in pairs),
        y_values=tuple(item[1] for item in pairs),
        variables=valid,
    )
