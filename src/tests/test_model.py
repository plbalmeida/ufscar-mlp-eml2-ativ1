import joblib
import pytest  # noqa: F401


def test_predict():
    model = joblib.load('iris_model.pkl')
    test_input = [5.9, 3.0, 5.1, 1.8]
    prediction = model.predict(test_input)
    expected_output = 2
    assert prediction == expected_output, f"""  # nosec
        Expected prediction {expected_output}, but got {prediction}
    """
