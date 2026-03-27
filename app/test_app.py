import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True # nosemgrep: python.flask.security.audit.hardcoded-config.avoid_hardcoded_config_TESTING
    with app.test_client() as client:
        yield client

def test_hello(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Hello DevOps Lab!" in response.data

def test_run_allowed_command(client):
    response = client.get('/run?cmd=ls')
    assert response.status_code == 200

def test_run_forbidden_command(client):
    response = client.get('/run?cmd=rm')
    assert response.status_code == 403