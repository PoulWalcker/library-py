from sqlalchemy.orm import Session
from sqlalchemy import select
from app.db.models.book import Book
from app.schemas.book import BookCreate, BookUpdate
from typing import Optional, List


def create_book(db: Session, new_book: BookCreate) -> Book:
    book = Book(
        title=new_book.title,
        isbn=new_book.isbn,
        author=new_book.author,
        amount=new_book.amount,
        publication_year=new_book.publication_year,
    )

    db.add(book)
    db.commit()
    db.refresh(book)

    return book


def get_book_by_id(db: Session, book_id: int) -> Optional[Book]:
    stmt = select(Book).where(Book.id == book_id)
    book = db.execute(stmt)
    return book.scalar_one_or_none()


def get_books(db: Session) -> List[Book]:
    stmt = select(Book)
    result = db.execute(stmt)
    return list(result.scalars().all())


def update_book(db: Session, book: Book, data: BookUpdate) -> Book:
    if data.title:
        book.title = data.title
    if data.author:
        book.author = data.author
    if data.publication_year:
        book.publication_year = data.publication_year
    if data.isbn:
        book.isbn = data.isbn
    if data.amount:
        book.amount = data.amount

    db.commit()
    db.refresh(book)
    return book


def delete_book(db: Session, book_id: int) -> Optional[Book]:
    book = get_book_by_id(db, book_id)

    if book:
        db.delete(book)
        db.commit()
        return book
