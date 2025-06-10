from sqlalchemy.orm import Mapped, mapped_column
from app.db.models.base import Base


class Book(Base):
    __tablename__ = "books"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title: Mapped[str] = mapped_column(nullable=False)
    author: Mapped[str] = mapped_column(nullable=False)
    publication_year: Mapped[int | None] = mapped_column(nullable=True)
    isbn: Mapped[str | None] = mapped_column(unique=True, nullable=True)
    amount: Mapped[int] = mapped_column(default=1)
