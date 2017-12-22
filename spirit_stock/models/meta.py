from datetime import datetime
import pytz

from sqlalchemy import Column, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import MetaData

# Recommended naming convention used by Alembic, as various different database
# providers will autogenerate vastly different names making migrations more
# difficult. See: http://alembic.zzzcomputing.com/en/latest/naming.html
NAMING_CONVENTION = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}

metadata = MetaData(naming_convention=NAMING_CONVENTION)
Base = declarative_base(metadata=metadata)


def utc_aware_time_now():
    return datetime.now(tz=pytz.utc)


class BaseModel(object):
    id = Column(UUID(as_uuid=True), primary_key=True)

    created = Column(DateTime(timezone=True), default=utc_aware_time_now)
    updated = Column(DateTime(timezone=True), onupdate=utc_aware_time_now)
    deleted = Column(DateTime(timezone=True))
