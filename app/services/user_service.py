from sqlalchemy.orm import selectinload
from sqlmodel import Session, select

from app.models.database import Users
from app.schema.users import UserCreate


def create_user(db_session: Session, user: UserCreate):
    new_user = Users(**user.model_dump())
    db_session.add(new_user)
    db_session.commit()
    db_session.refresh(new_user)
    return new_user

def get_user_profile(db_session: Session):
    pass

def get_user(db_session: Session, user_id: str):
    statement = select(Users).options(selectinload(Users.posts)).where(Users.id == user_id)
    return db_session.exec(statement).first()


def get_users(db_session: Session):
    return db_session.exec(select(Users)).all()
