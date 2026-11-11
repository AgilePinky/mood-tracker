from app.db.base import Base
from app.db.session import engine
from app.models import Mood

Mood.metadata.create_all(bind=engine)
print(Mood.metadata.tables)