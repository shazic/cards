import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_board():
    response = client.post('/api/v1/boards', json={'name': 'My First Board'})
    assert response.status_code == 201
    data = response.json()
    assert data.get('name', '') == 'My First Board'
    assert "id" in data
