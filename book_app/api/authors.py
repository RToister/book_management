from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from book_app.core.database import get_db
from book_app.schemas.author import AuthorCreate, AuthorUpdate, AuthorResponse
from book_app.services.author_service import (
    create_author_service,
    list_authors_service,
    get_author_service,
    update_author_service,
    delete_author_service,
)

router = APIRouter(prefix="/authors", tags=["Authors"])


@router.post("/", response_model=AuthorResponse)
def create_author(author: AuthorCreate, db: Session = Depends(get_db)):
    return create_author_service(db, author.name)


@router.get("/", response_model=list[AuthorResponse])
def get_authors(db: Session = Depends(get_db)):
    return list_authors_service(db)


@router.get("/{author_id}", response_model=AuthorResponse)
def get_author(author_id: int, db: Session = Depends(get_db)):
    author = get_author_service(db, author_id)
    if not author:
        raise HTTPException(status_code=404, detail="Author not found")
    return author


@router.put("/{author_id}", response_model=AuthorResponse)
def update_author(author_id: int, author: AuthorUpdate, db: Session = Depends(get_db)):
    updated = update_author_service(db, author_id, author.name)
    if not updated:
        raise HTTPException(status_code=404, detail="Author not found")
    return updated


@router.delete("/{author_id}")
def delete_author(author_id: int, db: Session = Depends(get_db)):
    success = delete_author_service(db, author_id)
    if not success:
        raise HTTPException(status_code=404, detail="Author not found")
    return {"message": "deleted"}
