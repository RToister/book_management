from sqlalchemy.orm import Session

from book_app.models.book import Book


def recommend_books(db: Session, genre: str):
    return (
        db.query(Book)
        .filter(Book.genre == genre)
        .limit(5)
        .all()
    )
