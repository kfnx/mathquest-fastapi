from datetime import date, datetime
from enum import Enum
from typing import Any, Dict

from sqlalchemy import JSON
from sqlmodel import Field, Relationship, SQLModel

from app.utils.generate_id import generate_id


class ProblemType(str, Enum):
    MULTIPLE_CHOICE = "multiple_choice"
    INPUT = "input"


class Users(SQLModel, table=True):
    id: str = Field(default_factory=generate_id, primary_key=True)
    full_name: str = Field(default="")
    email: str = Field(default="", unique=True)
    password: str | None = None
    created_at: datetime = Field(default_factory=datetime.now)

    progress: list["UserProgress"] = Relationship(back_populates="user")
    submissions: list["Submissions"] = Relationship(back_populates="user")
    stats: "UserStats" = Relationship(back_populates="user")



class Lessons(SQLModel, table=True):
    id: str = Field(default_factory=generate_id, primary_key=True)
    title: str = Field(default="")
    description: str = Field(default="")
    order: int = Field(default=0)
    created_at: datetime = Field(default_factory=datetime.now)

    problems: list["Problems"] = Relationship(back_populates="lesson")


class Problems(SQLModel, table=True):
    id: str = Field(default_factory=generate_id, primary_key=True)
    lesson_id: str = Field(foreign_key="lessons.id")
    question: str = Field(default="")
    type: ProblemType = Field(default=ProblemType.MULTIPLE_CHOICE)
    answer: str = Field(default="")
    reward: int = Field(default=0)
    order: int = Field(default=0)
    created_at: datetime = Field(default_factory=datetime.now)

    lesson: Lessons = Relationship(back_populates="problems")
    choices: list["ProblemChoices"] = Relationship(back_populates="problem")


class ProblemChoices(SQLModel, table=True):
    __tablename__ = "problem_choices"
    id: str = Field(default_factory=generate_id, primary_key=True)
    problem_id: str = Field(foreign_key="problems.id")
    answer: str = Field(default="")
    order: int = Field(default=0)

    problem: Problems = Relationship(back_populates="choices")


class Submissions(SQLModel, table=True):
    id: str = Field(default_factory=generate_id, primary_key=True) # attempt_id
    user_id: str = Field(foreign_key="users.id")
    lesson_id: str = Field(foreign_key="lessons.id")
    answers: Dict[str, Any] = Field(default={}, sa_type=JSON) # TODO: revisit later, to not use JSON?
    correct_count: int = Field(default=0)
    earned_xp: int = Field(default=0)
    created_at: datetime = Field(default_factory=datetime.now)

    user: Users = Relationship(back_populates="submissions")


class UserProgress(SQLModel, table=True):
    __tablename__ = "user_progress"
    id: str = Field(default_factory=generate_id, primary_key=True)
    user_id: str = Field(foreign_key="users.id")
    lesson_id: str = Field(foreign_key="lessons.id")
    completed_problems: int = Field(default=0)
    total_problems: int = Field(default=0)
    is_completed: bool = Field(default=False)
    last_activity_at: datetime = Field(default_factory=datetime.now)
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)

    user: Users = Relationship(back_populates="progress")


class UserStats(SQLModel, table=True):
    __tablename__ = "user_stats"
    id: str = Field(default_factory=generate_id, primary_key=True)
    user_id: str = Field(foreign_key="users.id", unique=True)
    total_xp: int = Field(default=0)
    current_streak: int = Field(default=0)
    best_streak: int = Field(default=0)
    last_activity_date: date | None = Field(default=None)
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)

    user: Users = Relationship(back_populates="stats")

