from datetime import date
from typing import List, Optional

from sqlalchemy.orm import Session
from sqlalchemy import select

from app.db.models.book import Book, BorrowedBook
from app.schemas.borrowed_book import BorrowedBookCreate


def borrow_book(db: Session, data: BorrowedBookCreate) -> BorrowedBook:
    book = db.get(Book, data.book_id)
    if not book or book.amount < 1:
        raise ValueError("Book is not available")

    active_borrows = (
        db.execute(
            select(BorrowedBook).where(
                BorrowedBook.reader_id == data.reader_id,
                BorrowedBook.return_date.is_(None),
            )
        )
        .scalars()
        .all()
    )

    if len(active_borrows) >= 3:
        raise ValueError("Reader already borrowed 3 books")

    borrow = BorrowedBook(
        book_id=data.book_id,
        reader_id=data.reader_id,
        borrow_date=date.today(),
        return_date=None,
    )

    book.amount -= 1

    db.add(borrow)
    db.commit()
    db.refresh(borrow)

    return borrow


def get_book_by_id(db: Session, borrowed_id: int) -> Optional[BorrowedBook]:
    borrow = db.get(BorrowedBook, borrowed_id)

    if not borrow or borrow.return_date is not None:
        raise ValueError("This borrow record is invalid or already returned")

    book = db.get(Book, borrow.book_id)
    if not book:
        raise ValueError("Book record not found")

    borrow.return_date = date.today()
    book.amount += 1

    db.commit()
    db.refresh(borrow)

    return borrow


def get_all_borrowed_books(db: Session) -> List[BorrowedBook]:
    stmt = select(BorrowedBook)
    result = db.execute(stmt)
    return list(result.scalars().all())
