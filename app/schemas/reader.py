from pydantic import BaseModel, EmailStr


class ReaderCreate(BaseModel):
    name: str
    email: EmailStr


class ReaderRead(BaseModel):
    id: int
    name: str
    email: EmailStr

    class Config:
        from_attributes = True
