import enum


class GenreEnum(str, enum.Enum):
    fiction = "fiction"

    non_fiction = "non_fiction"

    science = "science"

    history = "history"

    fantasy = "fantasy"

    horror = "horror"

    romance = "romance"
