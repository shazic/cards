from fastapi import FastAPI, HTTPException, status
from fastapi import APIRouter
from pydantic import BaseModel, Field
import uuid

# Pydantic models for OpenAPI specification compliance
class BoardCreate(BaseModel):
    """Request model for creating a new Kanban board."""
    name: str = Field(..., description="Name of the board", example="My Project Board")

class BoardResponse(BaseModel):
    """Response model for board operations."""
    id: str = Field(..., description="Unique identifier for the board", example="550e8400-e29b-41d4-a716-446655440000")
    name: str = Field(..., description="Name of the board", example="My Project Board")

class ColumnCreate(BaseModel):
    """Request model for creating a new column in a board."""
    name: str = Field(..., description="Name of the column", example="To Do")

class ColumnResponse(BaseModel):
    """Response model for column operations."""
    id: str = Field(..., description="Unique identifier for the column", example="550e8400-e29b-41d4-a716-446655440001")
    name: str = Field(..., description="Name of the column", example="To Do")

app = FastAPI(
    title="Kanban Board API",
    version="1.0.0",
    description="A RESTful API for managing Kanban boards built with FastAPI, following TDD, SOLID principles, and DDD.",
    contact={
        "name": "Kanban Board API Team",
        "email": "support@kanbanapi.com",
    },
    license_info={
        "name": "MIT",
    },
)

router = APIRouter()

# In-memory storage for boards
boards = {}

@router.post(
    "/api/v1/boards", 
    status_code=status.HTTP_201_CREATED, 
    response_model=BoardResponse,
    summary="Create a new Kanban board",
    description="Creates a new Kanban board with the specified name. The board will be assigned a unique UUID.",
    response_description="Successfully created board with unique ID and name",
    responses={
        201: {
            "description": "Board created successfully",
            "content": {
                "application/json": {
                    "example": {
                        "id": "550e8400-e29b-41d4-a716-446655440000",
                        "name": "My Project Board"
                    }
                }
            }
        }
    }
)
def create_board(board: BoardCreate) -> BoardResponse:
    """
    Create a new Kanban board.
    
    This endpoint creates a new Kanban board with the provided name.
    Each board gets a unique UUID that can be used to reference it in other operations.
    
    Args:
        board: Board creation data containing the name
        
    Returns:
        BoardResponse: The created board with its unique ID and name
        
    Example:
        ```python
        POST /api/v1/boards
        {
            "name": "My Project Board"
        }
        ```
    """
    board_id = str(uuid.uuid4())
    board_data = BoardResponse(id=board_id, name=board.name)
    boards[board_id] = board_data.dict()  # Store the board
    return board_data

@router.get(
    "/api/v1/boards/{board_id}", 
    response_model=BoardResponse,
    summary="Retrieve a Kanban board by ID",
    description="Retrieves a specific Kanban board using its unique identifier.",
    response_description="Successfully retrieved board information",
    responses={
        200: {
            "description": "Board retrieved successfully",
            "content": {
                "application/json": {
                    "example": {
                        "id": "550e8400-e29b-41d4-a716-446655440000",
                        "name": "My Project Board"
                    }
                }
            }
        },
        404: {
            "description": "Board not found",
            "content": {
                "application/json": {
                    "example": {
                        "detail": "Board not found"
                    }
                }
            }
        }
    }
)
def get_board(board_id: str) -> BoardResponse:
    """
    Retrieve a Kanban board by its unique identifier.
    
    This endpoint retrieves a specific Kanban board using its UUID.
    If the board doesn't exist, a 404 error is returned.
    
    Args:
        board_id: The unique identifier (UUID) of the board to retrieve
        
    Returns:
        BoardResponse: The board information including ID and name
        
    Raises:
        HTTPException: 404 error if the board is not found
        
    Example:
        ```python
        GET /api/v1/boards/550e8400-e29b-41d4-a716-446655440000
        ```
    """
    board_data = boards.get(board_id)
    if not board_data:
        raise HTTPException(status_code=404, detail="Board not found")
    return BoardResponse(**board_data)

@router.post(
    "/api/v1/boards/{board_id}/columns", 
    status_code=status.HTTP_201_CREATED, 
    response_model=ColumnResponse,
    summary="Add a new column to a Kanban board",
    description="Creates a new column in the specified Kanban board. The board must exist before adding columns.",
    response_description="Successfully created column with unique ID and name",
    responses={
        201: {
            "description": "Column created successfully",
            "content": {
                "application/json": {
                    "example": {
                        "id": "550e8400-e29b-41d4-a716-446655440001",
                        "name": "To Do"
                    }
                }
            }
        },
        404: {
            "description": "Board not found",
            "content": {
                "application/json": {
                    "example": {
                        "detail": "Board not found"
                    }
                }
            }
        }
    }
)
def add_column(board_id: str, column: ColumnCreate) -> ColumnResponse:
    """
    Add a new column to an existing Kanban board.
    
    This endpoint creates a new column in the specified board.
    The board must exist before columns can be added to it.
    Each column gets a unique UUID for identification.
    
    Args:
        board_id: The unique identifier (UUID) of the board to add the column to
        column: Column creation data containing the name
        
    Returns:
        ColumnResponse: The created column with its unique ID and name
        
    Raises:
        HTTPException: 404 error if the board is not found
        
    Example:
        ```python
        POST /api/v1/boards/550e8400-e29b-41d4-a716-446655440000/columns
        {
            "name": "To Do"
        }
        ```
    """
    # Check if board exists
    if board_id not in boards:
        raise HTTPException(status_code=404, detail="Board not found")
    
    column_id = str(uuid.uuid4())
    return ColumnResponse(id=column_id, name=column.name)

app.include_router(router)
