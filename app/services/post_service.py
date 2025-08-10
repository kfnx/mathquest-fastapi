from sqlalchemy.orm import selectinload
from sqlmodel import Session, select

from app.models.database import Posts
from app.schema.posts import PostCreate


def create_post(db_session: Session, post: PostCreate):
    new_post = Posts(**post.model_dump())
    db_session.add(new_post)
    db_session.commit()
    db_session.refresh(new_post)
    return new_post


def get_post(db_session: Session, post_id: str):
    statement = select(Posts).options(selectinload(Posts.user)).where(Posts.id == post_id)
    return db_session.exec(statement).first()


def get_posts(db_session: Session):
    return db_session.exec(select(Posts)).all()
