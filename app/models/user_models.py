from sqlalchemy import Column, String

from app.models import BaseModel, AutoIdModelMixin, AuditModelMixin, SoftDeleteMixin


class User(BaseModel, AutoIdModelMixin, AuditModelMixin, SoftDeleteMixin):
    __tablename__ = 'users'

    username = Column(String(), nullable=False, unique=True)
    email = Column(String(), nullable=False, unique=True)
    password = Column(String(), nullable=False)
