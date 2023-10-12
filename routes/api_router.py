from fastapi import APIRouter
from routes.quiz.quiz import quiz_router

api = APIRouter(prefix="/v1", tags=["V1"])
api.include_router(quiz_router)
