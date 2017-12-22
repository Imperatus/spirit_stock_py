from sqlalchemy import (Column, Boolean, String)

from .meta import Base, BaseModel


class User(Base, BaseModel):
    __tablename__ = 'stock'

    name = Column(String(255), nullable=False)
    surname = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)
    password = Column(String(255), nullable=True)
    active = Column(Boolean(), nullable=False, default=False)

    @property
    def full_name(self):
        return (self.name + ' ' + self.surname).replace('  ', ' ')

    def __json__(self, _):
        return {
            "id": self.id,
            "name": self.name,
            "surname": self.surname,
            "full_name": self.full_name,
            "email": self.email,
        }
