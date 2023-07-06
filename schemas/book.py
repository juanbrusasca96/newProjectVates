from pydantic import BaseModel


class BookCreate(BaseModel):
    name: str
    description: str

class Book(BookCreate):
    id: int 

    class Config:
        orm_mode=True