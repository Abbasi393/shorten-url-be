from fastapi import (APIRouter, Depends, HTTPException)
from sqlalchemy.orm import Session
from starlette import status

from app.core.config import get_session
from app.models import User
from app.schemas.user_schema import (UserCreateModel, UserResponseModel, UserLoginModel)
from app.services.user_service import UserService

user_router = APIRouter()


@user_router.post(
    '/register',
    tags=['auth'],
    summary='Create a new user',
    status_code=status.HTTP_201_CREATED,
    response_model=UserResponseModel
)
def register_user(
        request: UserCreateModel,
        session: Session = Depends(get_session)
):
    existing_user = session.query(User).filter_by(email=request.email).first()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f'User with email {request.email} already exists.'
        )

    return UserService.create_user(session=session, user_data=request)


@user_router.post(
    '/login',
    tags=['auth'],
    summary='User Login'
)
def login_user(
        request: UserLoginModel,
        session: Session = Depends(get_session)
):
    user = UserService.authenticate_user(
        session=session, username=request.username, password=request.password
    )
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = UserService.generate_token(user)
    return {"access_token": token, "token_type": "bearer"}
