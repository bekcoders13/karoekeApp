from pydantic import BaseModel, validator
from db import SessionLocal
from models.user import Users

db = SessionLocal()


class CreateUser(BaseModel):
    name: str
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
        return username


class UpdateUser(BaseModel):
    name: str
    password: str

    @validator('password')
    def password_validate(cls, password):
        if len(password) < 8:
            raise ValueError('Parol 8 tadan kam bo`lmasligi kerak')
        return password
