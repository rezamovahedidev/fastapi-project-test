from sqlmodel import SQLModel
from sqlmodel import Session
from db import engine
from db.model import Users as UsersModel
# from db.engine import async_create


class UsersService():
    def __init__(self, session: Session) -> None:  # type: ignore
        self.session = session 

    def create(self, user: UserModel) -> UsersModel:

    self.session.add(user)
    self.session.commit()
    return user
    
    
