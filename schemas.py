from pydantic import BaseModel, validator, Field

from datetime import date
from typing import List

class Genre(BaseModel):
    name: str

class Author(BaseModel):
    first_name: str = Field(..., max_length=25)
    last_name: str
    age: int = Field(..., gt=15, lt=90, description='15 90')

    # @validator('age')
    # def check_age(cls, v):
    #     if v < 15:
    #         raise ValueError('age < 15')

class Book(BaseModel):

    title: str
    writer: str
    duration: str
    date: date
    summary: str
    genres: List[Genre] = []
    pages: int

class BookOut(Book):
    id: int = 2