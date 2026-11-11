from pydantic import BaseModel, Field

class MoodCreate(BaseModel):
    mood: int = Field(ge=1, le=10)
    energy: int = Field(ge=1, le=10)