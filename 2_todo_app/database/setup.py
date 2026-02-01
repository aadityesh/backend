from sqlmodel import create_engine, SQLModel, Session

sqlite_file_name = "todoApp.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo=True, connect_args={
    "check_same_thread": False,
    "timeout": 30
})


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_db():
    with Session(engine) as session:
        yield session
