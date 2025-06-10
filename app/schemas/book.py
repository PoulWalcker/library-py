from pydantic import BaseModel
from typing import Optional


class BookCreate(BaseModel):
    title: str
    author: str
    publication_year: Optional[int] = None
    isbn: Optional[str] = None
    amount: int = 1


class BookRead(BaseModel):
    id: int
    title: str
    author: str
    publication_year: Optional[int]
    isbn: Optional[str]
    amount: int

    class Config:
        from_attributes = True


class BookUpdate(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    publication_year: Optional[int] = None
    isbn: Optional[str] = None
    amount: Optional[int] = None
