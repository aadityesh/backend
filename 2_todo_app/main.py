from fastapi import FastAPI
from database.setup import create_db_and_tables
from router import tasks, user

app = FastAPI()

create_db_and_tables()  # Create Tables

app.include_router(router=user.router)
app.include_router(router=tasks.router)
