from datetime import datetime

from pydantic import BaseModel, Field

from book_app.models.enums import GenreEnum


class BookBase(BaseModel):
    title: str = Field(
        min_length=1
    )

    genre: GenreEnum

    published_year: int = Field(
        ge=1800,
        le=datetime.now().year
    )

    author_id: int


class BookCreate(BookBase):
    pass


class BookUpdate(BookBase):
    pass


class BookResponse(BookBase):
    id: int

    class Config:
        from_attributes = True
