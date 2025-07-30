from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from fastapi import APIRouter
import uuid

app = FastAPI()

router = APIRouter()

# In-memory storage for boards
boards = {}

@router.post("/api/v1/boards", status_code=status.HTTP_201_CREATED)
def create_board(payload: dict):
    name = payload.get("name")
    board_id = str(uuid.uuid4())
    board_data = {"id": board_id, "name": name}
    boards[board_id] = board_data  # Store the board
    return JSONResponse(status_code=201, content=board_data)

@router.get("/api/v1/boards/{board_id}")
def get_board(board_id: str):
    board_data = boards.get(board_id)
    if board_data:
        return JSONResponse(status_code=200, content=board_data)
    return JSONResponse(status_code=404, content={"detail": "Board not found"})

@router.post("/api/v1/boards/{board_id}/columns", status_code=status.HTTP_201_CREATED)
def add_column(board_id: str, payload: dict):
    name = payload.get("name")
    column_id = str(uuid.uuid4())
    return JSONResponse(status_code=201, content={"id": column_id, "name": name})

app.include_router(router)
