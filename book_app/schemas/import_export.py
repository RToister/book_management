from pydantic import BaseModel

from book_app.models.enums import GenreEnum


class BookImport(BaseModel):
    title: str

    published_year: int

    genre: GenreEnum

    author_id: int
