from services.schemas import InputDataSchema, ResponseQuestionSchema
from sqlalchemy.ext.asyncio import AsyncSession
from httpx import AsyncClient
from sqlalchemy import select, Sequence
from services.models import Question
import dateutil.parser

API_URL = "https://jservice.io/api/random"


async def get_quiz_data(
    input_data: InputDataSchema, session: AsyncSession
) -> ResponseQuestionSchema:
    last = await get_last_question(session=session)
    questions = await get_questions(input_data=input_data.questions_num)
    ids = [item.get("id") for item in questions]
    in_db = await check_in_db(session=session, questions_ids=ids)
    if in_db:
        for item in in_db:
            await attempt_additional_question(session=session, question_id=item)
    else:
        await attempt_to_db(session=session, questions=questions)
    return last


async def get_questions(input_data: int) -> list[dict]:
    async with AsyncClient() as client:
        response = await client.get(url=f"{API_URL}?count={input_data}")
        return response.json()


async def check_in_db(
    session: AsyncSession, questions_ids: list[int]
) -> bool | Sequence:
    is_in_db = (
        (
            await session.execute(
                select(Question.question_id).where(
                    Question.question_id.in_(questions_ids)
                )
            )
        )
        .scalars()
        .all()
    )
    if is_in_db:
        return is_in_db
    return False


async def attempt_to_db(session: AsyncSession, questions: list[dict]) -> None:
    question_instances = []
    for item in questions:
        date = dateutil.parser.parse(item.get("created_at"))
        question = Question(
            question_id=item.get("id"),
            question=item.get("question"),
            answer=item.get("answer"),
            created_at=date,
        )
        question_instances.append(question)
    session.add_all(question_instances)
    await session.flush()
    await session.commit()


async def attempt_additional_question(session: AsyncSession, question_id: str) -> None:
    additional = await get_questions(input_data=1)
    if additional[0].get("id") != question_id:
        await attempt_to_db(session=session, questions=additional)
    else:
        await attempt_additional_question(session=session, question_id=question_id)


async def get_last_question(session: AsyncSession) -> ResponseQuestionSchema | None:
    last_question = (
        await session.scalars(select(Question).order_by(Question.position.desc()))
    ).first()
    if last_question:
        return ResponseQuestionSchema.model_validate(last_question)
    else:
        return None
