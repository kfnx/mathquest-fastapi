from pydantic import BaseModel

from app.models.database import ProblemType


class ProblemChoiceRead(BaseModel):
    id: str
    answer: str
    order: int


class ProblemRead(BaseModel):
    id: str
    question: str
    type: ProblemType
    reward: int
    order: int
    choices: list[ProblemChoiceRead] = []


class LessonRead(BaseModel):
    id: str
    title: str
    description: str
    order: int
    problems: list[ProblemRead] = []


class LessonCreate(BaseModel):
    title: str
    description: str
    order: int
