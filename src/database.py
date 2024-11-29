import os
import logging
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from dotenv import load_dotenv
from contextlib import contextmanager

load_dotenv()

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

logger.info(f"Connecting to database: {DATABASE_URL}")

engine = create_engine(
    DATABASE_URL,
    pool_size=30,       # Valor por defecto o ajustado
    max_overflow=-1,    # Conexiones adicionales ilimitadas
    pool_timeout=30,    # Tiempo máximo de espera para obtener una conexión
    connect_args={"options": "-c statement_timeout=30000"}  # 30 segundos será cancelada automáticamente
)

session_factory = sessionmaker(autocommit=False, autoflush=False, bind=engine)
db_session = scoped_session(session_factory)

@contextmanager
def session_scope():
    """Provide a transactional scope around a series of operations."""
    session = session_factory()
    try:
        yield session
        session.commit()
    except Exception as e:
        session.rollback()
        logger.error(f"Database error: {str(e)}", exc_info=True)
        raise
    finally:
        logger.info("Closing database session")
        session.close()

def init_db():
    from src.models.model import Blacklist, Base
    logger.info("Initializing database")
    Base.metadata.create_all(bind=engine)
    logger.info("Database initialized")