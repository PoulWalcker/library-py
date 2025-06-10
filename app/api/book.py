from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.book import BookRead, BookCreate
from app.db.models.book import Book
from app.crud.book import get_book_by_id, get_books, create_book, update_book
from app.db.dependency import get_db
from typing import List


router = APIRouter()


@router.post('/register_book', response_model=BookRead)
def register_book(new_book: BookCreate, db: Session = Depends(get_db)):
    existing_book = db.query(Book).filter_by(title=new_book.title).first()
    if existing_book:
        raise HTTPException(status_code=400, detail='Book already exists.')
    return create_book(db, new_book)


@router.get('/books/{book_id}', response_model=BookRead)
def get_book(book_id: int, db: Session = Depends(get_db)):
    book = get_book_by_id(db, book_id)
    if not book:
        raise HTTPException(
            status_code=404,
            detail=f"Book with id: {book_id} does not exist.",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return book


@router.get('/books', response_model=List[BookRead])
def get_all_books(db: Session = Depends(get_db)):
    books = get_books(db)
    return books
