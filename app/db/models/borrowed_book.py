from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, Date, ForeignKey
from app.db.models.base import Base
from typing import Optional
from app.db.models.book import Book
from app.db.models.reader import Reader


class BorrowedBook(Base):
    __tablename__ = "borrowed_books"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    book_id: Mapped[int] = mapped_column(ForeignKey("books.id"), nullable=False)
    reader_id: Mapped[int] = mapped_column(ForeignKey("readers.id"), nullable=False)
    borrow_date: Mapped[Date] = mapped_column(nullable=False)
    return_date: Mapped[Optional[Date]] = mapped_column(nullable=True)

    book: Mapped[Book] = relationship(back_populates="borrowed_books")
    reader: Mapped[Reader] = relationship(back_populates="borrowed_books")
