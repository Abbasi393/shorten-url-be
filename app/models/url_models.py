from sqlalchemy import (MetaData, Column, String, DateTime)
from sqlalchemy.ext.declarative import declarative_base

from app.models.model_mixins import (AutoIdModelMixin, AuditModelMixin, SoftDeleteMixin)

convention = {
    'ix': 'ix_%(column_0_label)s',
    'uq': 'uq_%(table_name)s_%(column_0_name)s',
    'ck': 'ck_%(table_name)s_%(constraint_name)s',
    'fk': 'fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s',
    'pk': 'pk_%(table_name)s'
}

sa_metadata = MetaData(naming_convention=convention)
BaseModel = declarative_base(metadata=sa_metadata)


class Url(BaseModel, AutoIdModelMixin, AuditModelMixin, SoftDeleteMixin):
    __tablename__ = 'urls'

    long_url = Column(String, nullable=False, unique=True)
    short_code = Column(String, unique=True, index=True, nullable=False)
    expiry_date = Column(DateTime, nullable=True)
