from datetime import datetime

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    field_validator
)

from book_app.models.enums import GenreEnum


CURRENT_YEAR = datetime.now().year


class BookBase(BaseModel):
    title: str = Field(
        min_length=1,
        max_length=255
    )

    published_year: int

    genre: GenreEnum

    author_id: int


    @field_validator("published_year")
    @classmethod
    def validate_year(cls, value: int):
        if value < 1800 or value > CURRENT_YEAR:
            raise ValueError(
                f"published_year must be between 1800 and {CURRENT_YEAR}"
            )

        return value


class BookCreate(BookBase):
    pass


class BookUpdate(BookBase):
    pass


class BookResponse(BookBase):
    id: int

    model_config = ConfigDict(
        from_attributes=True
    )
