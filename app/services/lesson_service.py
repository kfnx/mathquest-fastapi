from fastapi import HTTPException
from sqlmodel import Session, select

from app.models.database import Lessons, Problems, ProblemChoices
from app.schema.lessons import LessonCreate, LessonRead, ProblemRead, ProblemChoiceRead


def create_lesson(db_session: Session, lesson: LessonCreate):
    new_lesson = Lessons(**lesson.model_dump())
    db_session.add(new_lesson)
    db_session.commit()
    db_session.refresh(new_lesson)
    return new_lesson


def get_lesson(db_session: Session, lesson_id: str):
    statement = select(Lessons).where(Lessons.id == lesson_id)
    lesson = db_session.exec(statement).first()
    if not lesson:
        raise HTTPException(status_code=404, detail="Lesson not found")
    
    # Get problems for this lesson
    problems_statement = select(Problems).where(Problems.lesson_id == lesson_id).order_by(Problems.order)
    problems = db_session.exec(problems_statement).all()
    
    # Convert to response format with choices
    problem_reads = []
    for problem in problems:
        # Get choices for this problem
        choices_statement = select(ProblemChoices).where(ProblemChoices.problem_id == problem.id).order_by(ProblemChoices.order)
        choices = db_session.exec(choices_statement).all()
        
        choice_reads = [
            ProblemChoiceRead(
                id=choice.id,
                answer=choice.answer,
                order=choice.order
            ) for choice in choices
        ]
        
        problem_read = ProblemRead(
            id=problem.id,
            question=problem.question,
            type=problem.type,
            reward=problem.reward,
            order=problem.order,
            choices=choice_reads
        )
        problem_reads.append(problem_read)
    
    return LessonRead(
        id=lesson.id,
        title=lesson.title,
        description=lesson.description,
        order=lesson.order,
        problems=problem_reads
    )


def get_lessons(db_session: Session):
    return db_session.exec(select(Lessons)).all()


def submit_lesson(db_session: Session, lesson_id: str, attempt_id: str):
    pass
