import pytest
from app.app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_home_page(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Automated CI/CD Deployment System" in response.data

def test_api_info(client):
    response = client.get("/api")
    assert response.status_code == 200
    assert response.json["status"] == "running"

def test_health_check(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json["status"] == "healthy"

def test_invalid_route(client):
    response = client.get("/invalid")
    assert response.status_code == 404
    assert response.json["error"] == "Resource not found"
