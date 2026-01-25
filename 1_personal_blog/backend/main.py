from fastapi import FastAPI, Depends
from database.db import init_db
from crud.users import create_user
from crud.posts import *
from models.users import User
from api_models.models import *

app = FastAPI()


@app.on_event("startup")
def start_up():
    init_db()


@app.post("/users")
def create_user_handler(data: UserCreate):
    return create_user(data)


@app.post("/create_post")
def create_post_handler(data: PostCreate):
    return create_post(data)


@app.delete("/delete_post")
def delete_post_handler(data: PostID):
    return delete_post(data)


@app.put("/update_post")
def update_post_handler(data: PostUpdate):
    return update_post(data)


@app.get("/fetch")
def fetch_all_posts_handler():
    return fetch_all_posts()


@app.get("/fetch/{username}")
def fetch_post_by_user_handler(username: str):
    return fetch_post_by_user(username)
