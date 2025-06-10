from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.reader import ReaderRead, ReaderCreate
from app.crud.reader import get_reader_by_id, get_readers, create_reader, Reader
from app.db.dependency import get_db
from typing import List

router = APIRouter()


@router.post('/register_reader', response_model=ReaderRead)
def register_reader(
        new_reader: ReaderCreate,
        db: Session = Depends(get_db)
):
    existing_reader = db.query(Reader).filter_by(email=new_reader.email).first()
    if existing_reader:
        raise HTTPException(status_code=400, detail='Reader with this email already registered.')
    return create_reader(db, new_reader)


@router.get('/readers/{reader_id}', response_model=ReaderRead)
def get_reader(
        reader_id: int,
        db: Session = Depends(get_db)
):
    reader = get_reader_by_id(db, reader_id)
    if not reader:
        raise HTTPException(
            status_code=404,
            detail=f"Reader with id: {reader_id} does not exist.",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return reader


@router.get('/readers', response_model=List[ReaderRead])
def get_all_readers(
        db: Session = Depends(get_db)
):
    readers = get_readers(db)
    return readers



