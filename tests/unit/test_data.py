from io import BytesIO, StringIO

import pytest

from gaussian_explorer.data import CsvUploadError, load_uploaded_csv


def test_loads_supported_csv_from_bytes() -> None:
    dataset = load_uploaded_csv(
        b"x,y,label\n1.0,2.0,first\n3.0,4.0,second\n",
        filename="experiment.csv",
    )

    assert dataset.filename == "experiment.csv"
    assert dataset.columns == ("x", "y", "label")
    assert dataset.row_count == 2
    assert dataset.rows[0] == {"x": "1.0", "y": "2.0", "label": "first"}


def test_loads_supported_csv_from_text_file_like_object() -> None:
    dataset = load_uploaded_csv(StringIO("temperature,response\n10,5\n11,7\n"))

    assert dataset.columns == ("temperature", "response")
    assert dataset.row_count == 2


def test_loads_supported_csv_from_binary_file_like_object() -> None:
    dataset = load_uploaded_csv(BytesIO(b"time,signal\n0,1\n1,2\n"))

    assert dataset.columns == ("time", "signal")
    assert dataset.rows[1]["signal"] == "2"


def test_rejects_csv_without_data_rows() -> None:
    with pytest.raises(CsvUploadError, match="at least one data row"):
        load_uploaded_csv("x,y\n")


def test_rejects_duplicate_column_names() -> None:
    with pytest.raises(CsvUploadError, match="unique column names"):
        load_uploaded_csv("x,x\n1,2\n")
