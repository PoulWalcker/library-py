from pydantic import BaseModel, EmailStr
from typing import Optional


class LibrarianCreate(BaseModel):
    email: EmailStr
    password: str


class LibrarianRead(BaseModel):
    id: int
    email: EmailStr

    class Config:
        from_attributes = True


class LibrarianUpdate(BaseModel):
    email: Optional[EmailStr] = None
    password: Optional[str] = None
