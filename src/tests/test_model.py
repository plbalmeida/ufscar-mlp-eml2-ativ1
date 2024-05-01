import joblib
import numpy as np 
import pytest  # noqa: F401


def test_predict():
    model = joblib.load('iris_model.pkl')
    test_input = np.array([[5.9, 3.0, 5.1, 1.8]])
    prediction = model.predict(test_input)
    assert prediction is not None