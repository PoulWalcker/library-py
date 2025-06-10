from sqlalchemy.orm import Session
from sqlalchemy import select
from app.db.models.reader import Reader
from app.schemas.reader import ReaderCreate, ReaderUpdate
from typing import Optional, List


def create_reader(db: Session, new_reader: ReaderCreate) -> Reader:
    reader = Reader(
        email=new_reader.email,
        name=new_reader.name
    )

    db.add(reader)
    db.commit()
    db.refresh(reader)

    return reader


def get_reader_by_id(db: Session, reader_id) -> Optional[Reader]:
    stmt = select(Reader).where(Reader.id == reader_id)
    reader = db.execute(stmt)
    return reader.scalar_one_or_none()


def get_readers(db: Session) -> List[Reader]:
    stmt = select(Reader)
    result = db.execute(stmt)
    return list(result.scalars().all())


def update_reader(
        db: Session,
        reader: Reader,
        reader_update_data: ReaderUpdate
) -> Optional[Reader]:
    if reader_update_data.name is not None:
        reader.name = reader_update_data.name

    if reader_update_data.email is not None:
        reader.email = reader_update_data.email

    db.commit()
    db.refresh(reader)
    return reader


def delete_librarian(
        db: Session,
        reader_id: int
) -> Optional[Reader]:
    reader = get_reader_by_id(db, reader_id)

    if reader:
        db.delete(reader)
        db.commit()
        return reader


