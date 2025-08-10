from pydantic import BaseModel


class LessonRead(BaseModel):
    id: str
    title: str
    content: str
