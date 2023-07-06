from pydantic import BaseModel


class CountryCreate(BaseModel):
    name: str

class Country(CountryCreate):
    id: int 

    class Config:
        orm_mode=True