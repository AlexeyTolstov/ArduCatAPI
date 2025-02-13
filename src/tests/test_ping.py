import pytest
from fastapi.testclient import TestClient
from app import app


client = TestClient(app)

def test_ping():
    """Checks server availability at /ping endpoint."""

    response = client.get("/ping")
    assert response.status_code == 200, f"Error: {response.status_code}"