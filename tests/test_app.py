import pytest
from app import create_app

@pytest.fixture
def app():
    app = create_app()
    app.testing = True
    return app

@pytest.fixture
def client(app):
    return app.test_client()

def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Hello, World!" in response.data