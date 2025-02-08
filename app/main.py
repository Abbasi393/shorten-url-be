from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import settings

app = FastAPI()

engine = create_engine(settings.database_url)
db_session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_session():
    db = db_session()
    try:
        yield db
    finally:
        db.close()

