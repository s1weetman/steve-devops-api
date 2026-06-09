from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_root_endpoint() -> None:
    response = client.get("/")

    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert "docs" in data
    assert "health" in data


def test_health_endpoint() -> None:
    response = client.get("/health")

    assert response.status_code == 200
    data = response.json()
    assert "status" in data
    assert "service" in data


def test_python_version_endpoint() -> None:
    response = client.get("/ops/python-version")

    assert response.status_code == 200
    data = response.json()
    assert "ok" in data
    assert "stdout" in data
    assert "runtime" in data
