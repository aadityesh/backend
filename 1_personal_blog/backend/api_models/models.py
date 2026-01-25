from pydantic import BaseModel


class UserCreate(BaseModel):
    name: str
    email: str
    password: str
    username: str


class PostCreate(BaseModel):
    username: str
    post_content: str


class PostID(BaseModel):
    id: str


class PostUpdate(BaseModel):
    id: str
    post_content: str
