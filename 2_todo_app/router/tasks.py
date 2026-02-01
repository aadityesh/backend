from fastapi import APIRouter, Depends, status, HTTPException
from sqlmodel import Session
from database.setup import get_db
from crud import tasks, user
from utils import schemas
from auth.token import oauth2_scheme, verify_token

router = APIRouter(
    prefix="/task",
    tags=["task"],
    dependencies=[Depends(verify_token)]
)


@router.post("/create", status_code=status.HTTP_201_CREATED)
def create_task_handler(data: schemas.CreateTask, db: Session = Depends(get_db)):
    return tasks.create(data, db)


@router.get("/read/{user_id}", status_code=status.HTTP_200_OK)
def read_task_handler(user_id: int, db: Session = Depends(get_db)):
    return tasks.read(user_id, db)


@router.put("/update", status_code=status.HTTP_200_OK)
def update_task_handler(data: schemas.UpdateTask, db: Session = Depends(get_db)):
    return tasks.update(data, db)


@router.delete("/delete/{task_id}", status_code=status.HTTP_200_OK)
def delete_task_handler(task_id: int, db: Session = Depends(get_db)):
    return tasks.delete(task_id, db)
