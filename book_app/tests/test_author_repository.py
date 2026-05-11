from book_app.repositories.author_repository import (
    create_author,
    get_author_by_id,
    get_authors,
    update_author,
    delete_author
)


def test_create_author(db):
    author = create_author(db, "King")

    assert author.id is not None
    assert author.name == "King"


def test_get_author_by_id(db):
    author = create_author(db, "Rowling")

    found = get_author_by_id(db, author.id)

    assert found.id == author.id


def test_get_authors(db):
    create_author(db, "A1")
    create_author(db, "A2")

    authors = get_authors(db)

    assert len(authors) == 2


def test_update_author(db):
    author = create_author(db, "Old")

    updated = update_author(db, author, "New")

    assert updated.name == "New"


def test_delete_author(db):
    author = create_author(db, "ToDelete")

    delete_author(db, author)

    result = get_author_by_id(db, author.id)

    assert result is None
