from fastapi import HTTPException
from pydantic import BaseModel, validator
from db import SessionLocal
from models.user import Users

db = SessionLocal()


class CreateUser(BaseModel):
    firstname: str
    lastname: str
    username: str
    password: str

    @validator('password')
    def password_validate(cls, password):
        if len(password) < 8:
            raise ValueError('Parol 8 tadan kam bo`lmasligi kerak')
        return password

    @validator('username')
    def username_validate(cls, username):
        validate_my = db.query(Users).filter(
            Users.username == username,
        ).count()
        if validate_my != 0:
            raise ValueError('Bunday login avval ro`yxatga olingan!')
        if str(username).isnumeric() is False:
            raise HTTPException(400, "raqamlardan iborat bolsin")
        return username


class UpdateUser(BaseModel):
    firstname: str
    lastname: str
    password: str

    @validator('password')
    def password_validate(cls, password):
        if len(password) < 8:
            raise ValueError('Parol 8 tadan kam bo`lmasligi kerak')
        return password


class CreateGeneralUser(BaseModel):
    firstname: str
    lastname: str
    username: str
    password: str

    @validator('password')
    def password_validate(cls, password):
        if len(password) < 8:
            raise ValueError('Parol 8 tadan kam bo`lmasligi kerak')
        return password

    @validator('username')
    def username_validate(cls, username):
        validate_my = db.query(Users).filter(
            Users.username == username,
        ).count()

        if validate_my != 0:
            raise ValueError('Bunday login avval ro`yxatga olingan!')
        if str(username).isnumeric() is False:
            raise HTTPException(400, "raqamlardan iborat bolsin")
        return username
