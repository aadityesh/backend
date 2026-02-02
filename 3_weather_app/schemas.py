from pydantic import BaseModel


class UserLogin(BaseModel):
    username: str
    password: str


class Location(BaseModel):
    location: str
