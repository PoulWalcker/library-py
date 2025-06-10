from __future__ import annotations
from typing import List, Optional
from datetime import date

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, ForeignKey
from app.db.models.base import Base


class Book(Base):
    __tablename__ = "books"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title: Mapped[str] = mapped_column(nullable=False)
    author: Mapped[str] = mapped_column(nullable=False)
    publication_year: Mapped[Optional[int]] = mapped_column(nullable=True)
    isbn: Mapped[Optional[str]] = mapped_column(unique=True, nullable=True)
    amount: Mapped[int] = mapped_column(default=1)

    borrowed_books: Mapped[List["BorrowedBook"]] = relationship(
        back_populates="book", cascade="all, delete-orphan"
    )


class BorrowedBook(Base):
    __tablename__ = "borrowed_books"

    id: Mapped[int] = mapped_column(primary_key=True)
    book_id: Mapped[int] = mapped_column(ForeignKey("books.id"))
    reader_id: Mapped[int] = mapped_column(ForeignKey("readers.id"))
    borrow_date: Mapped[date]
    return_date: Mapped[Optional[date]] = mapped_column(nullable=True)

    book: Mapped["Book"] = relationship(back_populates="borrowed_books")
    reader: Mapped["Reader"] = relationship(back_populates="borrowed_books")
