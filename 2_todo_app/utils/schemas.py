from pydantic import BaseModel

# Input


class CreateTask(BaseModel):
    user_id: int
    task: str
    status: str


class ReadTask(BaseModel):
    user_id: int


class DeleteTask(ReadTask):
    task_id: int


class UpdateTask(DeleteTask):
    task: str
    status: str


class UserModel(BaseModel):
    username: str
    password: str


class CreateToken(BaseModel):
    sub: str
