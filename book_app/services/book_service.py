from book_app.repositories.book_repository import (
    create_book,
    get_books,
    get_book_by_id,
    update_book,
    delete_book
)


def create_book_service(db, book):
    return create_book(db, book)


def list_books_service(
    db,
    title=None,
    genre=None,
    year_from=None,
    year_to=None,
    sort_by=None,
    page=1,
    size=10
):
    return get_books(
        db,
        title,
        genre,
        year_from,
        year_to,
        sort_by,
        page,
        size
    )


def get_book_service(db, book_id: int):
    return get_book_by_id(db, book_id)


def update_book_service(db, book_id: int, data):
    book = get_book_by_id(db, book_id)

    if not book:
        return None

    return update_book(db, book, data)


def delete_book_service(db, book_id: int):
    book = get_book_by_id(db, book_id)

    if not book:
        return False

    delete_book(db, book)
    return True
