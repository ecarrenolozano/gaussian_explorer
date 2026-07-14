"""CSV intake support for Gaussian Explorer."""

from __future__ import annotations

import csv
from collections.abc import Sequence
from dataclasses import dataclass
from io import StringIO
from typing import BinaryIO, TextIO


class CsvUploadError(ValueError):
    """Raised when uploaded CSV content cannot be accepted for analysis."""


@dataclass(frozen=True)
class UploadedDataset:
    """Validated in-memory representation of an uploaded CSV dataset."""

    columns: tuple[str, ...]
    rows: tuple[dict[str, str], ...]
    filename: str | None = None

    @property
    def row_count(self) -> int:
        """Return the number of data rows in the dataset."""

        return len(self.rows)


CsvSource = bytes | str | BinaryIO | TextIO


def load_uploaded_csv(source: CsvSource, *, filename: str | None = None) -> UploadedDataset:
    """Load supported CSV upload content into an in-memory dataset.

    The function accepts raw bytes, decoded text, or file-like objects such as
    Streamlit uploaded files. It intentionally keeps data in memory for the
    active analysis workflow.
    """

    text = _read_text(source)
    reader = csv.DictReader(StringIO(text))

    if reader.fieldnames is None:
        msg = "CSV upload must include a header row."
        raise CsvUploadError(msg)

    columns = tuple(_normalize_header(reader.fieldnames))
    if not columns:
        msg = "CSV upload must include at least one column."
        raise CsvUploadError(msg)

    rows: list[dict[str, str]] = []
    try:
        for row in reader:
            rows.append({column: row.get(column, "") for column in columns})
    except csv.Error as exc:
        msg = "CSV upload could not be parsed."
        raise CsvUploadError(msg) from exc

    if not rows:
        msg = "CSV upload must include at least one data row."
        raise CsvUploadError(msg)

    return UploadedDataset(columns=columns, rows=tuple(rows), filename=filename)


def _read_text(source: CsvSource) -> str:
    if isinstance(source, bytes):
        return source.decode("utf-8-sig")

    if isinstance(source, str):
        return source

    data = source.read()
    if isinstance(data, bytes):
        return data.decode("utf-8-sig")

    return data


def _normalize_header(fieldnames: Sequence[str]) -> tuple[str, ...]:
    columns = tuple(fieldname.strip() for fieldname in fieldnames if fieldname.strip())
    if len(set(columns)) != len(columns):
        msg = "CSV upload must include unique column names."
        raise CsvUploadError(msg)
    return columns
