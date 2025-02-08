from sqlalchemy import (Column, String, DateTime)

from app.models.model_mixins import AuditModelMixin, SoftDeleteMixin
from model_base import BaseModel
from model_mixins import AutoIdModelMixin


class Url(BaseModel, AutoIdModelMixin, AuditModelMixin, SoftDeleteMixin):
    __tablename__ = "urls"

    long_url = Column(String, nullable=False, unique=True)
    short_code = Column(String, unique=True, index=True, nullable=False)
    expiry_date = Column(DateTime, nullable=True)
