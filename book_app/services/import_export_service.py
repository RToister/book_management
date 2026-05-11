import csv
import json

from sqlalchemy.orm import Session

from book_app.models.book import Book
from book_app.repositories.book_repository import create_book


def export_books_to_json(db: Session):
    books = db.query(Book).all()

    return [
        {
            "title": b.title,
            "published_year": b.published_year,
            "genre": b.genre,
            "author_id": b.author_id
        }
        for b in books
    ]


def export_books_to_csv(db: Session):
    books = db.query(Book).all()

    output = []

    for b in books:
        output.append([
            b.title,
            b.published_year,
            b.genre,
            b.author_id
        ])

    return output


def import_books_from_json(db: Session, data: list):
    for item in data:
        create_book(db, item)


def import_books_from_csv(db: Session, rows: list):
    for row in rows:
        create_book(
            db,
            type(
                "obj",
                (),
                {
                    "model_dump": lambda: {
                        "title": row[0],
                        "published_year": int(row[1]),
                        "genre": row[2],
                        "author_id": int(row[3])
                    }
                }
            )()
        )
