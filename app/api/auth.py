from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from sqlalchemy.orm import Session
from app.schemas.librarian import LibrarianCreate, LibrarianRead
from app.crud.librarian import create_librarian, get_librarian_by_email, get_librarian_by_id,  Librarian
from app.db.dependency import get_db
from app.core.security import create_access_token, verify_password, ACCESS_TOKEN_EXPIRE_MINUTES, SECRET_KEY, ALGORITHM, Token
from datetime import timedelta
from jose import jwt, JWTError
from typing import Annotated


router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


def get_current_librarian(
    token: Annotated[str, Depends(oauth2_scheme)],
    db: Session = Depends(get_db)
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        librarian_id: str = payload.get("sub")
        if librarian_id is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    librarian = get_librarian_by_id(db, int(librarian_id))
    if librarian is None:
        raise credentials_exception
    return librarian


@router.post('/register', response_model=LibrarianRead)
def register_librarian(
        new_librarian: LibrarianCreate,
        db: Session = Depends(get_db)
):
    existing_librarian = db.query(Librarian).filter_by(email=new_librarian.email).first()
    if existing_librarian:
        raise HTTPException(status_code=400, detail='Librarian with this email already registered.')
    return create_librarian(db, new_librarian)


@router.post("/login", response_model=Token)
def login(
        form_data: OAuth2PasswordRequestForm = Depends(),
        db: Session = Depends(get_db)
):
    librarian_email = form_data.username
    librarian_password = form_data.password

    librarian = get_librarian_by_email(db, librarian_email)

    if not librarian or not verify_password(librarian_password, librarian.hashed_password):
        raise HTTPException(
            status_code=401,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": str(librarian.id)},
        expires_delta=access_token_expires
    )

    return Token(access_token=access_token, token_type="bearer")


@router.get('/me', response_model=LibrarianRead)
def read_me(current_user: Librarian = Depends(get_current_librarian)):
    return current_user




