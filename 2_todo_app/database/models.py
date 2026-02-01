from sqlmodel import Field, SQLModel, Session
from .setup import engine, create_db_and_tables


class Users(SQLModel, table=True):
    __tablename__ = 'users'
    id: int | None = Field(default=None, primary_key=True)
    username: str
    password: str


class Tasks(SQLModel, table=True):
    __tablename__ = 'tasks'
    user_id: int = Field(foreign_key='users.id')
    task_id: int | None = Field(default=None, primary_key=True)
    task: str
    status: str
