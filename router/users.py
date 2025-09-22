from fastapi import APIRouter, Body
from schema.users import UserInput
from operation.users import UsersService
from sqlmodel import Session
router = APIRouter()


@router.post('/register')
async def register(data: UserInput = Body()):
    user = UsersService().create(username=data.username, password=data.password)
    return user


@router.get('/users')
async def get_all():
    ...


@router.post('/create')
async def create_user():
    ...


@router.put('/update-user')
async def update_user():
    ...
