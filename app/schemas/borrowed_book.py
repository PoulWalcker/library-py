from pydantic import BaseModel
from datetime import date
from typing import Optional


class BorrowedBookCreate(BaseModel):
    book_id: int
    reader_id: int


class BorrowedBookReturn(BaseModel):
    book_id: int


class BorrowedBookRead(BaseModel):
    id: int
    book_id: int
    reader_id: int
    borrow_date: date
    return_date: Optional[date] = None

    class Config:
        from_attributes = True
