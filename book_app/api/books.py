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
    delete_book_service,
)

router = APIRouter(prefix="/books", tags=["Books"])


@router.post("/", response_model=BookResponse)
def create_book(
    book: BookCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    return create_book_service(db, book)


@router.get("/", response_model=list[BookResponse])
def get_books(
    db: Session = Depends(get_db),
    title: str | None = None,
    genre: str | None = None,
    year_from: int | None = None,
    year_to: int | None = None,
    sort_by: str | None = None,
    page: int = 1,
    size: int = 10
):
    return list_books_service(
        db=db,
        title=title,
        genre=genre,
        year_from=year_from,
        year_to=year_to,
        sort_by=sort_by,
        page=page,
        size=size
    )


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


@router.put("/{book_id}", response_model=BookResponse)
def update_book(
    book_id: int,
    data: BookUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    updated_book = update_book_service(
        db,
        book_id,
        data
    )

    if not updated_book:
        raise HTTPException(
            status_code=404,
            detail="Book not found"
        )

    return updated_book


@router.delete("/{book_id}")
def delete_book(
    book_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    deleted = delete_book_service(
        db,
        book_id
    )

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Book not found"
        )

    return {"message": "Book deleted"}
