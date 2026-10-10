import pytest

from myproject.models.predict import predict
from myproject.models.train import train_mean_model


def test_train_and_predict_roundtrip():
    model = train_mean_model([1.0, 2.0, 3.0])
    assert model == 2.0
    assert predict(model, 3) == [2.0, 2.0, 2.0]


def test_train_mean_model_empty_raises():
    with pytest.raises(ValueError):
        train_mean_model([])
