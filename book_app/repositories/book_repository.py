from sqlalchemy.orm import Session

from book_app.models.book import Book


def create_book(
    db: Session,
    data
):
    book = Book(**data.model_dump())

    db.add(book)

    db.commit()

    db.refresh(book)

    return book


def get_books(
    db: Session,
    title: str = None,
    genre: str = None,
    year_from: int = None,
    year_to: int = None,
    sort_by: str = None,
    page: int = 1,
    size: int = 10
):
    query = db.query(Book)

    if title:
        query = query.filter(
            Book.title.ilike(f"%{title}%")
        )

    if genre:
        query = query.filter(
            Book.genre == genre
        )

    if year_from:
        query = query.filter(
            Book.published_year >= year_from
        )

    if year_to:
        query = query.filter(
            Book.published_year <= year_to
        )

    if sort_by == "title":
        query = query.order_by(Book.title)

    elif sort_by == "published_year":
        query = query.order_by(Book.published_year)

    elif sort_by == "author":
        query = query.order_by(Book.author_id)

    offset = (page - 1) * size

    return (
        query
        .offset(offset)
        .limit(size)
        .all()
    )


def get_book_by_id(
    db: Session,
    book_id: int
):
    return (
        db.query(Book)
        .filter(Book.id == book_id)
        .first()
    )


def update_book(
    db: Session,
    book: Book,
    data
):
    for key, value in data.model_dump().items():
        setattr(book, key, value)

    db.commit()

    db.refresh(book)

    return book


def delete_book(
    db: Session,
    book: Book
):
    db.delete(book)

    db.commit()
