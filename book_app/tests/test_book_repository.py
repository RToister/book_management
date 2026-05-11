from book_app.repositories.book_repository import (
    create_book,
    get_books,
    get_book_by_id,
    update_book,
    delete_book
)

from book_app.models.enums import GenreEnum


class FakeBookData:
    def __init__(self):
        self.title = "Book 1"
        self.published_year = 2020
        self.genre = GenreEnum.fiction
        self.author_id = 1

    def model_dump(self):
        return self.__dict__


def test_create_book(db):
    book = create_book(db, FakeBookData())

    assert book.id is not None
    assert book.title == "Book 1"


def test_get_books(db):
    create_book(db, FakeBookData())
    create_book(db, FakeBookData())

    books = get_books(db)

    assert len(books) == 2


def test_get_books_filter(db):
    data = FakeBookData()
    data.title = "Unique Title"

    create_book(db, data)

    result = get_books(db, title="Unique")

    assert len(result) == 1


def test_get_book_by_id(db):
    book = create_book(db, FakeBookData())

    found = get_book_by_id(db, book.id)

    assert found.id == book.id


def test_update_book(db):
    book = create_book(db, FakeBookData())

    class UpdateData:
        def model_dump(self):
            return {
                "title": "Updated",
                "published_year": 2021,
                "genre": GenreEnum.fantasy,
                "author_id": 1
            }

    updated = update_book(db, book, UpdateData())

    assert updated.title == "Updated"


def test_delete_book(db):
    book = create_book(db, FakeBookData())

    delete_book(db, book)

    result = get_book_by_id(db, book.id)

    assert result is None
