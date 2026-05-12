from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from book_app.core.database import get_db
from book_app.core.deps import get_current_user

from book_app.schemas.book import (
    BookCreate,
    BookUpdate,
    BookResponse
)

from book_app.services.book_service import (
    create_book_service,
    list_books_service,
    get_book_service,
    update_book_service,
    delete_book_service
)

router = APIRouter(prefix="/books", tags=["Books"])


# CREATE BOOK
@router.post("/", response_model=BookResponse)
def create_book(
    book: BookCreate,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    return create_book_service(db, book)


# GET ALL BOOKS
@router.get("/", response_model=list[BookResponse])
def get_books(
    db: Session = Depends(get_db)
):
    return list_books_service(db)


# GET BOOK BY ID
@router.get("/{book_id}", response_model=BookResponse)
def get_book(
    book_id: int,
    db: Session = Depends(get_db)
):
    book = get_book_service(db, book_id)

    if not book:
        raise HTTPException(
            status_code=404,
            detail="Book not found"
        )

    return book


# UPDATE BOOK
@router.put("/{book_id}", response_model=BookResponse)
def update_book(
    book_id: int,
    book: BookUpdate,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    updated = update_book_service(
        db,
        book_id,
        book
    )

    if not updated:
        raise HTTPException(
            status_code=404,
            detail="Book not found"
        )

    return updated


# DELETE BOOK
@router.delete("/{book_id}")
def delete_book(
    book_id: int,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    success = delete_book_service(
        db,
        book_id
    )

    if not success:
        raise HTTPException(
            status_code=404,
            detail="Book not found"
        )

    return {"message": "deleted"}