from sqlmodel import SQLModel
from sqlmodel import Session
from db import engine
from db.model import Users as UsersModel
# from db.engine import async_create


class UsersService:
    def __init__(self) -> None:  # type: ignore
        self.session = engine

    def create(self, username: str, password: str) -> UsersModel:
        with Session(self.session) as session:
            user = UsersModel(username=username, password=password)
            session.add(user)
            session.commit()
            return user
