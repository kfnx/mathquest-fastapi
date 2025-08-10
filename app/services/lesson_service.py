from sqlmodel import Session, select

from app.models.database import Lessons


def get_lesson(db_session: Session, lesson_id: str):
    statement = select(Lessons).where(Lessons.id == lesson_id)
    return db_session.exec(statement).first()


def get_lessons(db_session: Session):
    return db_session.exec(select(Lessons)).all()

def submit_lesson(db_session: Session, lesson_id: str, attempt_id: str):
    pass
