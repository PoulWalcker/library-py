from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String
from app.db.models.base import Base


class Librarian(Base):
    __tablename__ = "librarians"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    email: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    hashed_password: Mapped[str] = mapped_column(String, nullable=False)
