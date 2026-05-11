from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from book_app.core.database import get_db
from book_app.schemas.book import BookCreate
from book_app.services.book_service import create_book_service, list_books_service

router = APIRouter(prefix="/books", tags=["Books"])


@router.post("/")
def create_book(book: BookCreate, db: Session = Depends(get_db)):
    return create_book_service(db, book)


@router.get("/")
def get_books(db: Session = Depends(get_db)):
    return list_books_service(db)
