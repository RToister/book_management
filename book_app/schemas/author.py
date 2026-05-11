from pydantic import BaseModel, ConfigDict, Field


class AuthorBase(BaseModel):
    name: str = Field(
        min_length=1,
        max_length=255
    )


class AuthorCreate(AuthorBase):
    pass


class AuthorUpdate(AuthorBase):
    pass


class AuthorResponse(AuthorBase):
    id: int

    model_config = ConfigDict(
        from_attributes=True
    )
