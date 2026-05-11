from sqlalchemy.orm import Session

from book_app.models.author import Author


def create_author(
    db: Session,
    name: str
):
    author = Author(name=name)

    db.add(author)

    db.commit()

    db.refresh(author)

    return author


def get_authors(
    db: Session
):
    return db.query(Author).all()


def get_author_by_id(
    db: Session,
    author_id: int
):
    return (
        db.query(Author)
        .filter(Author.id == author_id)
        .first()
    )


def update_author(
    db: Session,
    author: Author,
    name: str
):
    author.name = name

    db.commit()

    db.refresh(author)

    return author


def delete_author(
    db: Session,
    author: Author
):
    db.delete(author)

    db.commit()
