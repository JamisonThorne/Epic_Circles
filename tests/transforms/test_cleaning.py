import pytest

from myproject.transforms.cleaning import coerce_floats, drop_missing


def test_drop_missing_filters_empty_fields():
    rows = [{"a": "1", "b": ""}, {"a": "2", "b": "3"}]
    assert drop_missing(rows, required=["a", "b"]) == [{"a": "2", "b": "3"}]


def test_coerce_floats_converts_and_raises():
    rows = [{"a": "1.5"}]
    assert coerce_floats(rows, ["a"]) == [{"a": 1.5}]
    with pytest.raises(ValueError):
        coerce_floats([{"a": "not-a-number"}], ["a"])
