import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from dotenv import load_dotenv

load_dotenv()


DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

print("DATABASE_URL", DATABASE_URL)

engine = create_engine(DATABASE_URL)
session_factory = sessionmaker(autocommit=False, autoflush=False, bind=engine)
db_session = scoped_session(session_factory)

def init_db():
    from src.models.model import Blacklist, Base # Adjusted import statement
    print("Initializing database")
    Base.metadata.create_all(bind=engine)
    print("Database initialized")
