from fastapi import FastAPI
from router.users import router as user
from db.engine import create_db
app = FastAPI(title='Blog Project')

app.include_router(router=user, prefix='/users')


@app.on_event('startup')
async def startup():
    create_db()
