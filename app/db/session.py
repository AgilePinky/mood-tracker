from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

from app.core.config import settings

DATABASE_URL = (f"postgresql+psycopg://"
                f"{settings.postgres_user}:{settings.postgres_password}"
                f"@{settings.db_host}:{settings.db_port}/{settings.postgres_db}")

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()