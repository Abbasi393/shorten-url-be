from sqlalchemy import or_
from sqlalchemy.orm import Session

from app.models import User
from app.schemas.user_schema import UserCreateModel
from app.core.authentication import (hash_password, verify_password, create_access_token)


class UserService:

    @staticmethod
    def create_user(session: Session, user_data: UserCreateModel) -> User:
        password = hash_password(user_data.password)
        user = User(
            username=user_data.username,
            email=str(user_data.email),
            password=password,
        )
        session.add(user)
        session.commit()
        session.refresh(user)
        return user

    @staticmethod
    def authenticate_user(session: Session, username: str, password: str):
        user = session.query(User).filter(
            or_(User.username == username, User.email == username)
        ).first()
        if user and verify_password(password, user.password):
            return user
        return None

    @staticmethod
    def generate_token(user):
        return create_access_token(data={"user": user.username})
