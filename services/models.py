from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, DateTime

Base = declarative_base()


class Question(Base):
    __tablename__ = "questions"
    question_id = Column(Integer, unique=True)
    question = Column(String, nullable=False)
    answer = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), nullable=False)
    position = Column(
        Integer,
        autoincrement=True,
        primary_key=True,
    )
