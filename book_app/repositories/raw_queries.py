from sqlalchemy import text
from sqlalchemy.orm import Session


def get_books_raw(db: Session):
    result = db.execute(text("SELECT * FROM books"))
    return result.mappings().all()
