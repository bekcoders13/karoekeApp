from fastapi import APIRouter

from db import Base, engine
from routes.user import users_router

api = APIRouter()

Base.metadata.create_all(bind=engine)

api.include_router(users_router)
