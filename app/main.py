from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from fastapi import APIRouter
import uuid

app = FastAPI()

router = APIRouter()

@router.post("/api/v1/boards", status_code=status.HTTP_201_CREATED)
def create_board(payload: dict):
    name = payload.get("name")
    board_id = str(uuid.uuid4())
    return JSONResponse(status_code=201, content={"id": board_id, "name": name})

app.include_router(router)
