from sqlalchemy.orm import Session
from sqlalchemy import select
from app.db.models.librarian import Librarian
from app.core.security import hash_password
from app.schemas.librarian import LibrarianCreate, LibrarianUpdate
from typing import Optional


def create_librarian(
        db: Session,
        new_librarian: LibrarianCreate,
) -> Librarian:
    hashed_password = hash_password(new_librarian.password)

    librarian = Librarian(
        email=new_librarian.email,
        hashed_password=hashed_password
    )

    db.add(librarian)
    db.commit()
    db.refresh(librarian)

    return librarian


def get_librarian_by_id(
        db: Session,
        librarian_id: int
) -> Optional[Librarian]:
    stmt = select(Librarian).where(Librarian.id == librarian_id)
    librarian = db.execute(stmt)
    return librarian.scalar_one_or_none()


def get_librarian_by_email(
        db: Session,
        librarian_email: str
) -> Optional[Librarian]:
    stmt = select(Librarian).where(Librarian.email == librarian_email)
    librarian = db.execute(stmt)
    return librarian.scalar_one_or_none()


def update_librarian(
        db: Session,
        librarian: Librarian,
        librarian_update_data: LibrarianUpdate
) -> Optional[Librarian]:
    if librarian_update_data.email is not None:
        librarian.email = librarian_update_data.email

    if librarian_update_data.password is not None:
        librarian.hashed_password = hash_password(librarian_update_data.password)

    db.commit()
    db.refresh(librarian)
    return librarian


def delete_librarian(
        db: Session,
        librarian_id: int
) -> Optional[Librarian]:
    librarian = get_librarian_by_id(db, librarian_id)

    if librarian:
        db.delete(librarian)
        db.commit()
        return librarian
