from pydantic import BaseModel


class BookCreate(BaseModel):
    name: str
    description: str
    user_id: int
    state_id:int


class Book(BookCreate):
    id: int

    class Config:
        orm_mode = True
