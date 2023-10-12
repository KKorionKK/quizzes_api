from fastapi import APIRouter, Depends
from services.schemas import InputDataSchema, ResponseQuestionSchema
from services.database import get_session
from sqlalchemy.ext.asyncio import AsyncSession
from routes.quiz.logic import get_quiz_data


quiz_router = APIRouter(prefix="/quiz")


@quiz_router.post("/get_quiz", response_model=ResponseQuestionSchema | None)
async def get_quiz(
    input_data: InputDataSchema, session: AsyncSession = Depends(get_session)
):
    """
    Запрос на получение вопросов викторины,
    на выходе получаем либо None, либо последний вопрос
    """
    return await get_quiz_data(input_data=input_data, session=session)
