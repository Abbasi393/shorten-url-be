import pytest
from pydantic import EmailStr
from sqlalchemy.orm import Session
from tests.config import client
from app.core.config import get_session
from app.schemas.user_schema import UserCreateModel
from app.services.user_service import UserService


@pytest.fixture(scope="function")
def session():
    db_generator = get_session()
    db = next(db_generator)
    try:
        yield db
    finally:
        next(db_generator, None)


@pytest.fixture(scope="function")
def test_user(session: Session):
    from app.models.user_models import User

    existing_user = session.query(User).filter(User.email == "test@example.com").first()
    if existing_user:
        return existing_user

    user_data = UserCreateModel(
        username="testuser",
        email="test@example.com",
        password="password123"
    )
    user = UserService.create_user(session, user_data)
    session.commit()
    return user


def test_register_user(session: Session):
    response = client.post("/register", json={
        "username": "newuser1",
        "email": "newuser1@example.com",
        "password": "testsecurepassword"
    })
    assert response.status_code == 201
    assert response.json()["email"] == "newuser1@example.com"


def test_register_existing_user(session: Session, test_user):
    response = client.post("/register", json={
        "username": test_user.username,
        "email": test_user.email,
        "password": "password123"
    })
    assert response.status_code == 409


def test_login_user(session: Session, test_user):
    response = client.post("/login", json={
        "username": test_user.username,
        "password": "password123"
    })
    assert response.status_code == 200
    assert "access_token" in response.json()


def test_login_invalid_credentials():
    response = client.post("/login", json={
        "username": "invaliduser",
        "password": "wrongpassword"
    })
    assert response.status_code == 401
