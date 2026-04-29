from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

DATABASE_URL = "sqlite:///./app.db"

engine = create_engine(DATABASE_URL)
Base = declarative_base()
session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency
def get_db() -> Session:
    db = session_local()
    try:
        yield db
    finally:
        db.close()