from sqlalchemy import Column, Integer, VARCHAR, ForeignKey, Enum
from sqlalchemy.orm import validates

from app.db.database import Base
from app.service.image_position import ImagePositionEnum


class Image(Base):
    __tablename__ = 'image'

    id = Column(Integer, nullable=False, unique=True, primary_key=True, autoincrement=True)
    category_id = Column(Integer, ForeignKey('category.id', ondelete='CASCADE'), nullable=False)
    position = Column(Enum(ImagePositionEnum), nullable=False, default='Horizontal')
    creation_year = Column(Integer, nullable=False, default=3000)
    name = Column(VARCHAR(100), nullable=False)

    @validates('creation_year')
    def validate_year(self, key, value):
        if value is not None and (value < 1000 or value > 9999):
            raise ValueError("Year must be a four-digit number between 1000 and 9999")
        return value
