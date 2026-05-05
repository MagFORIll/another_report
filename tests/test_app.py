import os
import csv
import pytest

from handler import Handler
from input_file import InputFile
from output_file import OutputFile


def test_start_up_creates_correct_path(monkeypatch):
    fake_cwd = "C:\\test_dir"
    monkeypatch.setattr(os, "getcwd", lambda: fake_cwd)

    files, path = Handler.start_up()

    assert path == f"{fake_cwd}\\docs"
    assert isinstance(files, list)


class Args:
    def __init__(self, files):
        self.files = files


def test_find_files_to_work_with(tmp_path):
    docs = tmp_path / "docs"
    docs.mkdir()

    # создаем файлы
    file1 = docs / "a.csv"
    file1.write_text("test")

    file2 = docs / "b.csv"
    file2.write_text("test")

    args = Args(files=["a.csv", "b.csv", "c.csv"])

    result = Handler.find_files_to_work_with(args, str(docs))

    assert sorted(result) == ["a.csv", "b.csv"]


def test_calculating_average_filters_correctly():
    data = [
        {"title": "A", "ctr": "20", "retention_rate": "30"},  # OK
        {"title": "B", "ctr": "10", "retention_rate": "30"},  # ctr low
        {"title": "C", "ctr": "25", "retention_rate": "50"},  # retention high
    ]

    storage = {}

    result = Handler.calculating_average(data, storage)

    assert "A" in result
    assert "B" not in result
    assert "C" not in result


def test_get_data_from_csv(tmp_path):
    file = tmp_path / "test.csv"

    with open(file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["title", "ctr", "retention_rate"])
        writer.writerow(["A", "20", "30"])

    data = InputFile.get_data_from_csv(str(file))
    data = list(data)

    assert data[0]["title"] == "A"


def test_get_data_from_csv_error():
    result = InputFile.get_data_from_csv("non_existent.csv")

    assert isinstance(result, list)
    assert result[0]["status"] == "Error"


def test_upload_data_to_csv(tmp_path):
    output_file = tmp_path / "out.csv"

    data = {
        "A": [20.0, 30.0],
        "B": [25.0, 20.0],
    }

    OutputFile.upload_data_to_csv(str(output_file), data)

    with open(output_file, "r") as f:
        rows = list(csv.reader(f))

    assert rows[0] == ["title", "ctr", "retention_rate"]
    assert ["A", "20.0", "30.0"] in rows
    assert ["B", "25.0", "20.0"] in rows