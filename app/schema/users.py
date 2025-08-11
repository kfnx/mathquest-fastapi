from pydantic import BaseModel


class UserCreate(BaseModel):
    full_name: str
    email: str
    password: str


class UserRead(BaseModel):
    id: str
    full_name: str
    email: str
