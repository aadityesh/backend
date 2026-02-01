from fastapi import status
from database.models import Users
from auth.hashing import hash_password, verify_password
from auth.token import create_token
from sqlmodel import select, Session
from utils import schemas


def check_user_in_db(data, db: Session):
    query = select(Users).where(Users.username == data.username)
    user = db.exec(query).first()
    return user


def signup(data, db: Session):

    hashed_password = hash_password(data.password)
    print(f"hash - {hashed_password}")

    new_user = Users(
        username=data.username,
        password=hashed_password
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return create_token(data={"sub": data.username})


def signin(data, user):
    try:
        if user and verify_password(data.password, user.password):
            return create_token(data={"sub": data.username})
    except Exception as e:
        print(f"Error in signin: {e}")


def login(data, db: Session):
    """
        1. Check if the user exists
            - if yes then return token
            - if not then add in db and then return token
    """
    try:
        user = check_user_in_db(data, db)
        if user is None:
            return signup(data, db)
        return signin(data, user)

    except Exception as e:
        return {
            "detail": f"Error while logging in: {e}"
        }
