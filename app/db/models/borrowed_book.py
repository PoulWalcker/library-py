from sqlalchemy import Column, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.db.models.base import Base


class BorrowedBook(Base):
    __tablename__ = "borrowed_books"

    id = Column(Integer, primary_key=True, index=True)
    book_id = Column(Integer, ForeignKey("books.id"), nullable=False)
    reader_id = Column(Integer, ForeignKey("readers.id"), nullable=False)
    borrow_date = Column(Date, nullable=False)
    return_date = Column(Date, nullable=True)

    book = relationship("Book", backref="borrowed_books")
    reader = relationship("Reader", backref="borrowed_books")
