from sqlalchemy import create_engine
import pymysql
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+pymysql://root:root@localhost:3306/kareoke')
SessionLocal = sessionmaker(bind=engine)


Base = declarative_base()


def database():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
