import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

@pytest.fixture
def created_board():
    """Fixture that creates a board and returns its data"""
    response = client.post('/api/v1/boards', json={'name': 'Test Board'})
    return response.json()

def test_create_board():
    response = client.post('/api/v1/boards', json={'name': 'My First Board'})
    assert response.status_code == 201
    data = response.json()
    assert data.get('name', '') == 'My First Board'
    assert "id" in data

def test_add_column_to_board(created_board):
    board_id = created_board['id']
    
    # Add a column to this board
    column_resp = client.post(f'/api/v1/boards/{board_id}/columns', json={'name': 'To Do'})
    assert column_resp.status_code == 201
    column_data = column_resp.json()
    assert column_data.get('name', '') == 'To Do'
    assert 'id' in column_data

def test_get_board_by_id(created_board):
    board_id = created_board['id']
    
    # Retrieve the board by ID
    response = client.get(f'/api/v1/boards/{board_id}')
    assert response.status_code == 200
    board_data = response.json()
    assert board_data.get('id') == board_id
    assert board_data.get('name') == 'Test Board'
    assert 'id' in board_data
    assert 'name' in board_data

def test_get_nonexistent_board():
    # Try to retrieve a board that doesn't exist
    nonexistent_id = 'nonexistent-board-id'
    response = client.get(f'/api/v1/boards/{nonexistent_id}')
    assert response.status_code == 404
    error_data = response.json()
    assert 'detail' in error_data
