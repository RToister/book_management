from book_app.repositories.auth_repository import create_user, get_user_by_email


def test_create_user(db):
    user = create_user(
        db=db,
        email="test@test.com",
        hashed_password="hashed123"
    )

    assert user.id is not None
    assert user.email == "test@test.com"


def test_get_user_by_email(db):
    create_user(
        db=db,
        email="find@test.com",
        hashed_password="hashed123"
    )

    user = get_user_by_email(db, "find@test.com")

    assert user is not None
    assert user.email == "find@test.com"
