from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from book_app.core.database import get_db
from book_app.schemas.user import UserCreate, UserLogin, Token
from book_app.services.auth_service import register_user, login_user

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    result = register_user(db, user.email, user.password)

    if not result:
        raise HTTPException(status_code=400, detail="User already exists")

    return {"message": "user created"}


@router.post("/login", response_model=Token)
def login(user: UserLogin, db: Session = Depends(get_db)):
    token = login_user(db, user.email, user.password)

    if not token:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    return Token(access_token=token)
