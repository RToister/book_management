import json
import csv
import io
from sqlalchemy.orm import Session

from book_app.repositories.book_repository import get_books


def export_books_json(db: Session):
    books = get_books(db, size=10000)

    return [
        {
            "id": b.id,
            "title": b.title,
            "published_year": b.published_year,
            "genre": b.genre.value,
            "author_id": b.author_id,
        }
        for b in books
    ]


def export_books_csv(db: Session):
    books = get_books(db, size=10000)

    output = io.StringIO()
    writer = csv.writer(output)

    # header
    writer.writerow(["id", "title", "published_year", "genre", "author_id"])

    for b in books:
        writer.writerow([
            b.id,
            b.title,
            b.published_year,
            b.genre.value,
            b.author_id
        ])

    return output.getvalue()



def import_books_from_json(db: Session, content: bytes):
    from book_app.repositories.book_repository import create_book
    from book_app.schemas.book import BookCreate

    data = json.loads(content.decode("utf-8"))

    count = 0
    for item in data:
        create_book(db, BookCreate(**item))
        count += 1

    return count


def import_books_from_csv(db: Session, content: bytes):
    from book_app.repositories.book_repository import create_book
    from book_app.schemas.book import BookCreate

    decoded = content.decode("utf-8")
    reader = csv.DictReader(io.StringIO(decoded))

    count = 0
    for row in reader:
        row["published_year"] = int(row["published_year"])
        row["author_id"] = int(row["author_id"])

        create_book(db, BookCreate(**row))
        count += 1

    return count
