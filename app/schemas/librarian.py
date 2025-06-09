from pydantic import BaseModel, EmailStr


class LibrarianCreate(BaseModel):
    email: EmailStr
    password: str


class LibrarianRead(BaseModel):
    id: int
    email: EmailStr

    class Config:
        from_attributes = True
