from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    Enum
)

from sqlalchemy.orm import relationship

from book_app.core.database import Base
from book_app.models.enums import GenreEnum


class Book(Base):
    __tablename__ = "books"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    title = Column(
        String,
        nullable=False,
        index=True
    )

    published_year = Column(
        Integer,
        nullable=False
    )

    genre = Column(
        Enum(GenreEnum),
        nullable=False
    )

    author_id = Column(
        Integer,
        ForeignKey("authors.id"),
        nullable=False
    )

    author = relationship(
        "Author",
        back_populates="books"
    )
