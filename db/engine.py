from sqlmodel import SQLModel
from sqlmodel import create_engine

sqlurl = "postgresql://postgres:reza123@127.0.0.1:5432/blogdb"
# connect_args = {"check_same_thread": False}

async_create = create_engine(sqlurl, echo=True)


def create_db():
    SQLModel.metadata.create_all(async_create)
