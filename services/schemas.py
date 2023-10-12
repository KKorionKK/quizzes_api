from pydantic import BaseModel, ConfigDict
from datetime import datetime


class InputDataSchema(BaseModel):
    questions_num: int


class ResponseQuestionSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    question_id: int
    question: str
    answer: str
    created_at: datetime
