from pydantic import BaseModel, EmailStr
from typing import Optional


class ReaderCreate(BaseModel):
    name: str
    email: EmailStr


class ReaderRead(BaseModel):
    id: int
    name: str
    email: EmailStr

    class Config:
        from_attributes = True


class ReaderUpdate(BaseModel):
    name: Optional[str]
    email: Optional[EmailStr]
