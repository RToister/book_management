from sqlalchemy.orm import Session

from book_app.repositories.auth_repository import (
    get_user_by_email,
    create_user
)

from book_app.core.security import (
    hash_password,
    verify_password,
    create_access_token
)


def register_user(db: Session, email: str, password: str):
    existing_user = get_user_by_email(db, email)

    if existing_user:
        raise ValueError("User already exists")

    hashed_password = hash_password(password)

    return create_user(
        db=db,
        email=email,
        hashed_password=hashed_password
    )


def login_user(db: Session, email: str, password: str):
    user = get_user_by_email(db, email)

    if not user:
        return None

    if not verify_password(password, user.hashed_password):
        return None

    token = create_access_token(data={"sub": user.email})

    return token

