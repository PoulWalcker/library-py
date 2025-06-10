from fastapi import APIRouter
from app.api import auth
from app.api import reader

router = APIRouter()

router.include_router(auth.router, prefix="/auth", tags=["auth"])
router.include_router(reader.router, prefix="/reader", tags=["reader"])
