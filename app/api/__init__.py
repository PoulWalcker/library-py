from fastapi import APIRouter
from app.api import auth, reader, book

router = APIRouter()

router.include_router(auth.router, prefix="/auth", tags=["auth"])
router.include_router(reader.router, prefix="/reader", tags=["reader"])
router.include_router(book.router, prefix="/book", tags=["book"])
