from fastapi import FastAPI

from app.api.routes import mood_routes

app = FastAPI()
# python -m uvicorn main:app --reload

app.include_router(mood_routes.router)