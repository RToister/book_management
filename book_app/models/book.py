from sqlalchemy import String, Integer, ForeignKey, Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship

from book_app.models.base import Base
from book_app.models.enums import GenreEnum


class Book(Base):
    __tablename__ = "books"

    id: Mapped[int] = mapped_column(primary_key=True)

    title: Mapped[str] = mapped_column(String(255), nullable=False)

    published_year: Mapped[int] = mapped_column(Integer)

    genre: Mapped[GenreEnum] = mapped_column(
        Enum(GenreEnum),
        nullable=False
    )

    author_id: Mapped[int] = mapped_column(
        ForeignKey("authors.id")
    )

    author = relationship("Author", back_populates="books")
    