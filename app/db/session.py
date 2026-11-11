from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

from app.core.config import settings

DATABASE_URL = (f"postgresql+psycopg://"
                f"{settings.postgres_user}:{settings.postgres_password}"
                f"@{settings.db_host}:{settings.db_port}/{settings.postgres_db}")

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

# with engine.connect() as connection:
#     result = connection.execute(text("SELECT 1"))
#     print(result.scalar())