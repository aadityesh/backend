from fastapi import APIRouter, Depends, status
from fastapi.security import OAuth2PasswordRequestForm
from crud import user
from database.setup import get_db

router = APIRouter(
    prefix="/user",
    tags=["user"]
)


@router.post("/token", status_code=status.HTTP_200_OK)
def login_handler(data: OAuth2PasswordRequestForm = Depends(), db=Depends(get_db)):
    return user.login(data, db)
