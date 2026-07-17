"""CSV intake for the Gaussian Process Regression Explorer."""

from __future__ import annotations

import csv
import hashlib
import io
from dataclasses import dataclass
from pathlib import Path
from typing import BinaryIO, TextIO

MAX_UPLOAD_BYTES = 5_000_000
SUPPORTED_SUFFIXES = {".csv"}


class CsvUploadError(ValueError):
    """Raised when an uploaded CSV cannot be accepted."""


@dataclass(frozen=True, slots=True)
class UploadedDataset:
    """Immutable, serializable representation of an uploaded CSV dataset."""

    columns: tuple[str, ...]
    rows: tuple[tuple[str, ...], ...]
    filename: str | None
    content_hash: str

    @property
    def row_count(self) -> int:
        return len(self.rows)

    def column_values(self, column: str) -> tuple[str, ...]:
        try:
            index = self.columns.index(column)
        except ValueError as exc:
            raise KeyError(column) from exc
        return tuple(row[index] for row in self.rows)


def _read_bytes(source: bytes | bytearray | BinaryIO | TextIO | str) -> bytes:
    if isinstance(source, bytes):
        return source
    if isinstance(source, bytearray):
        return bytes(source)
    if isinstance(source, str):
        return source.encode("utf-8")
    if not hasattr(source, "read"):
        raise CsvUploadError("The uploaded file could not be read.")

    position: int | None = None
    try:
        if hasattr(source, "tell"):
            position = source.tell()
        content = source.read()
    except (OSError, TypeError, ValueError) as exc:
        raise CsvUploadError("The uploaded file could not be read.") from exc
    finally:
        if position is not None and hasattr(source, "seek"):
            try:
                source.seek(position)
            except (OSError, ValueError):
                pass

    if isinstance(content, str):
        return content.encode("utf-8")
    if isinstance(content, (bytes, bytearray)):
        return bytes(content)
    raise CsvUploadError("The uploaded file must contain text or bytes.")


def load_uploaded_csv(
    source: bytes | bytearray | BinaryIO | TextIO | str,
    *,
    filename: str | None = None,
) -> UploadedDataset:
    """Validate and parse a small UTF-8 CSV file entirely in memory."""

    inferred_name = filename or getattr(source, "name", None)
    if inferred_name and Path(inferred_name).suffix.lower() not in SUPPORTED_SUFFIXES:
        raise CsvUploadError("Unsupported file type. Upload a .csv file.")

    payload = _read_bytes(source)
    if not payload:
        raise CsvUploadError("The uploaded file is empty.")
    if len(payload) > MAX_UPLOAD_BYTES:
        raise CsvUploadError(
            f"The uploaded file exceeds the {MAX_UPLOAD_BYTES:,}-byte size limit."
        )

    try:
        text = payload.decode("utf-8-sig")
    except UnicodeDecodeError as exc:
        raise CsvUploadError("The CSV file must be UTF-8 encoded.") from exc

    try:
        reader = csv.reader(io.StringIO(text, newline=""), strict=True)
        raw_header = next(reader, None)
        if not raw_header:
            raise CsvUploadError("The CSV file must contain a header row.")

        columns = tuple(value.strip() for value in raw_header)
        if any(not value for value in columns):
            raise CsvUploadError("Every CSV column must have a non-empty header.")
        if len(set(columns)) != len(columns):
            raise CsvUploadError("The CSV file contains duplicate column headers.")

        rows: list[tuple[str, ...]] = []
        for row_number, values in enumerate(reader, start=2):
            if not values or all(value.strip() == "" for value in values):
                continue
            if len(values) != len(columns):
                raise CsvUploadError(
                    f"CSV row {row_number} has {len(values)} values; "
                    f"expected {len(columns)}."
                )
            rows.append(tuple(values))
    except csv.Error as exc:
        raise CsvUploadError("The uploaded file is not a valid CSV document.") from exc

    if not rows:
        raise CsvUploadError("The CSV file must contain at least one data row.")

    return UploadedDataset(
        columns=columns,
        rows=tuple(rows),
        filename=inferred_name,
        content_hash=hashlib.sha256(payload).hexdigest(),
    )
