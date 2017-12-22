from sqlalchemy import (Column, Integer, Float, String, ForeignKey)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from .meta import Base, BaseModel


class Stock(Base, BaseModel):
    __tablename__ = 'stock'

    name = Column(String(255), nullable=False)
    starting_price = Column(Float, nullable=False)
    current_price = Column(Float, nullable=False)
    max_price = Column(Float, nullable=True)
    min_price = Column(Float, nullable=True)
    starting_stock = Column(Integer, nullable=True)
    current_stock = Column(Integer, nullable=True)

    stock_type_id = Column(UUID(as_uuid=True), ForeignKey('stock_type.id'))
    stock_type = relationship('StockType', back_ref='stocks')

    user_id = Column(UUID(as_uuid=True), ForeignKey('user.id'))
    user = relationship('User')

    def __json__(self, _):
        return {
            "id": self.id,
            "name": self.name,
            "starting_price": self.starting_price,
            "current_price": self.current_price,
            "max_price": self.max_price,
            "min_price": self.min_price,
            "starting_stock": self.starting_stock,
            "current_stock": self.current_stock
        }


class StockType(Base, BaseModel):
    __tablename__ = 'stock_type'

    name = Column(String(255), nullable=False)
    stocks = relationship('Stock', back_ref='stock_type')

    user_id = Column(UUID(as_uuid=True), ForeignKey('user.id'))
    user = relationship('User')

    def __json__(self, _):
        return {
            "id": self.id,
            "name": self.name
        }
