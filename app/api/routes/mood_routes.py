from fastapi import APIRouter

from app.schemas.mood_schema import MoodCreate

router = APIRouter()

@router.get("/")
def read_root():
    return {"message": "Mood Tracker Api is running"}

@router.post("/moods", status_code=201)
def create_mood(mood_data: MoodCreate):
    return 'hello'