from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models import Mood
from app.schemas import MoodCreate

router = APIRouter()

@router.get("/")
def read_root():
    return {"message": "Mood Tracker Api is running"}

@router.post("/moods", status_code=201)
def create_mood(
        mood_data: MoodCreate,
        db: Session = Depends(get_db)):

    db_mood = Mood(
        mood=mood_data.mood,
        energy=mood_data.energy
    )

    db.add(db_mood)
    db.commit()
    db.refresh(db_mood)

    return {
        "id": db_mood.id,
        "mood": db_mood.mood,
        "energy": db_mood.energy
    }