import pytest  # noqa: F401
from ..app import app as flask_app


@pytest.fixture
def app():
    yield flask_app


@pytest.fixture
def client(app):
    return app.test_client()


def test_predict(client):
    response = client.post('/predict', json={'features': [5.1, 3.5, 1.4, 0.2]})
    if response.status_code != 200:
        raise ValueError('Unexpected status code')
    if 'prediction' not in response.get_json():
        raise ValueError('Missing prediction in response')
