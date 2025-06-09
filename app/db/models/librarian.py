from sqlalchemy import Column, String, Integer
from app.db.models.base import Base


class Librarian(Base):
    __tablename__ = 'librarians'
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)
