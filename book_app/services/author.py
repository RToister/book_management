from sqlalchemy.orm import Session

from book_app.repositories.author import (
    create_author,
    get_authors,
    get_author,
    update_author,
    delete_author,
)


def create_author_service(db: Session, name: str):
    return create_author(db, name)


def list_authors_service(db: Session):
    return get_authors(db)


def get_author_service(db: Session, author_id: int):
    return get_author(db, author_id)


def update_author_service(db: Session, author_id: int, name: str):
    author = get_author(db, author_id)
    if not author:
        return None
    return update_author(db, author, name)


def delete_author_service(db: Session, author_id: int):
    author = get_author(db, author_id)
    if not author:
        return False
    delete_author(db, author)
    return True
