from fastapi import FastAPI, Body
from pydantic import BaseModel
from router.users import router as user

app = FastAPI(title='Blog Project')

app.include_router(router=user, prefix='/users')


class User(BaseModel):
    username: str
    password: str
    age: int
    char_name: str | None = None


class UserOut(BaseModel):
    username: str


class UserDB(BaseModel):
    hashed_password: str


@app.get('/user')
async def root(user: User = Body()):
    return {'hello': user.username}
