from fastapi import Depends
from sqlmodel import select, Session
from database.setup import get_db
from database.model import User
from auth.hashing import hash_password, verify_password
from auth.token import create_token


def check_user_in_db(data, db: Session):
    query = select(User).where(User.username == data.username)
    user = db.exec(query).first()
    return user


def signup(data, db: Session):
    hash_pwd = hash_password(data.password)
    new_user = User(
        username=data.username,
        password=hash_pwd
    )
    db.add(new_user)
    db.commit()
    return create_token(data)


def signin(user, data):
    if user and verify_password(data.password, user.password):
        return create_token(data)


def login(data, db: Session):

    user = check_user_in_db(data, db)
    if user is None:
        return signup(data, db)

    return signin(user, data)
