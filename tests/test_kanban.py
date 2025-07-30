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

def test_add_column_to_board():
    # First, create a board
    board_resp = client.post('/api/v1/boards', json={'name': 'Board for Columns'})
    assert board_resp.status_code == 201
    board_id = board_resp.json()['id']

    # Add a column to this board
    column_resp = client.post(f'/api/v1/boards/{board_id}/columns', json={'name': 'To Do'})
    assert column_resp.status_code == 201
    column_data = column_resp.json()
    assert column_data.get('name', '') == 'To Do'
    assert 'id' in column_data
