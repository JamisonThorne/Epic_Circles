import pytest

from myproject.io.loaders import load_csv


def test_load_csv_missing_file_raises(tmp_path):
    with pytest.raises(FileNotFoundError):
        load_csv(tmp_path / "nope.csv")


def test_load_csv_reads_rows(tmp_path):
    p = tmp_path / "data.csv"
    p.write_text("a,b\n1,2\n3,4\n")
    rows = load_csv(p)
    assert rows == [{"a": "1", "b": "2"}, {"a": "3", "b": "4"}]
