from sqlalchemy import Column, String

from app.models.base_model import BaseModel
from app.models.model_mixins import (AutoIdModelMixin, AuditModelMixin, SoftDeleteMixin)


class Url(BaseModel, AutoIdModelMixin, AuditModelMixin, SoftDeleteMixin):
    __tablename__ = 'urls'

    long_url = Column(String, nullable=False, unique=True)
    short_code = Column(String, unique=True, index=True, nullable=False)