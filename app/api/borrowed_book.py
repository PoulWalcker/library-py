from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.dependency import get_db
from app.schemas.borrowed_book import BorrowedBookCreate, BorrowedBookRead
from app.crud.borrowed_book import borrow_book, get_all_borrowed_books, get_book_by_id
from app.api.auth import get_current_librarian
from typing import List

router = APIRouter()


@router.post("/borrow", response_model=BorrowedBookRead)
def register_borrowed_book(
    borrow_data: BorrowedBookCreate,
    db: Session = Depends(get_db),
    librarian=Depends(get_current_librarian),
):
    try:
        return borrow_book(db, borrow_data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/return/{borrowed_id}", response_model=BorrowedBookRead)
def return_book(
    borrowed_id: int,
    db: Session = Depends(get_db),
    librarian=Depends(get_current_librarian),
):
    try:
        return get_book_by_id(db, borrowed_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/borrowed", response_model=List[BorrowedBookRead])
def return_all_borrowed_books(
    db: Session = Depends(get_db),
    librarian=Depends(get_current_librarian),
):
    return get_all_borrowed_books(db)
