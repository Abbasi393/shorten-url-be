from datetime import datetime
from sqlalchemy import (Column, Integer, Boolean, DateTime)


class AutoIdModelMixin:
    id = Column(Integer, primary_key=True, autoincrement=True)


class AuditModelMixin:
    is_enabled = Column(Boolean, default=True)

    created_on = Column(DateTime, nullable=False, default=datetime.now)
    created_by_id = Column(Integer, nullable=True)

    updated_on = Column(DateTime, nullable=True, onupdate=datetime.now)
    updated_by_id = Column(Integer, nullable=True)


class SoftDeleteMixin:
    is_deleted = Column(Boolean, nullable=False, default=False)
