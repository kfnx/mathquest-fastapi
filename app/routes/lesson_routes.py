from fastapi import APIRouter, Depends
from sqlmodel import Session

from app.models.engine import db_session
from app.schema.lessons import LessonCreate, LessonRead
from app.services.lesson_service import create_lesson, get_lesson, get_lessons, submit_lesson

lessons_router = APIRouter(prefix="/lessons", tags=["lessons"])
# • GET /api/lessons - Return lessons with completion/progress status
# • GET /api/lessons/:id - Get lesson + problems (don't leak correct answers to frontend)
# • POST /api/lessons/:id/submit - Submit answers with attempt_id ; return XP, streak, progress (idempotent)



@lessons_router.get("/", response_model=list[LessonRead])
def get_lessons_api(db: Session = Depends(db_session)):
    return get_lessons(db)


@lessons_router.get("/{lesson_id}", response_model=LessonRead)
def get_lesson_api(lesson_id: str, db: Session = Depends(db_session)):
    return get_lesson(db, lesson_id)


@lessons_router.post("/{lesson_id}/submit", response_model=LessonRead)
def submit_lesson_api(lesson_id: str, attempt_id: str, db: Session = Depends(db_session)):
    return submit_lesson(db, lesson_id, attempt_id)

@lessons_router.post("/", response_model=LessonRead)
def create_lesson_api(lesson: LessonCreate, db: Session = Depends(db_session)):
    return create_lesson(db, lesson)
