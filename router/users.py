from fastapi import APIRouter

router = APIRouter()


@router.get('/users')
async def get_all():
    ...


@router.post('/create')
async def create_user():
    ...


@router.put('/update-user')
async def update_user():
    ...
