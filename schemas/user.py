from pydantic import BaseModel


class UserCreate(BaseModel):
    name: str
    password: str
    role: str
    country_id: int

class User(UserCreate):
    id: int 

    class Config:
        orm_mode=True