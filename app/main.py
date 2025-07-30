from fastapi import FastAPI, HTTPException, status
from fastapi import APIRouter
from pydantic import BaseModel
import uuid

# Pydantic models for OpenAPI specification compliance
class BoardCreate(BaseModel):
    name: str

class BoardResponse(BaseModel):
    id: str
    name: str

class ColumnCreate(BaseModel):
    name: str

class ColumnResponse(BaseModel):
    id: str
    name: str

app = FastAPI(title="Kanban Board API", version="1.0.0")

router = APIRouter()

# In-memory storage for boards
boards = {}

@router.post("/api/v1/boards", status_code=status.HTTP_201_CREATED, response_model=BoardResponse)
def create_board(board: BoardCreate) -> BoardResponse:
    board_id = str(uuid.uuid4())
    board_data = BoardResponse(id=board_id, name=board.name)
    boards[board_id] = board_data.dict()  # Store the board
    return board_data

@router.get("/api/v1/boards/{board_id}", response_model=BoardResponse)
def get_board(board_id: str) -> BoardResponse:
    board_data = boards.get(board_id)
    if not board_data:
        raise HTTPException(status_code=404, detail="Board not found")
    return BoardResponse(**board_data)

@router.post("/api/v1/boards/{board_id}/columns", status_code=status.HTTP_201_CREATED, response_model=ColumnResponse)
def add_column(board_id: str, column: ColumnCreate) -> ColumnResponse:
    # Check if board exists
    if board_id not in boards:
        raise HTTPException(status_code=404, detail="Board not found")
    
    column_id = str(uuid.uuid4())
    return ColumnResponse(id=column_id, name=column.name)

app.include_router(router)
