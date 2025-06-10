from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String
from typing import List
from app.db.models.base import Base
from app.db.models.borrowed_book import BorrowedBook


class Reader(Base):
    __tablename__ = "readers"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(unique=True, nullable=False)

    borrowed_books: Mapped[List["BorrowedBook"]] = relationship(back_populates="reader")
