from sqlalchemy import Column, Integer, VARCHAR, ForeignKey, Enum
from app.db.database import Base
from app.service.image_position import ImagePositionEnum


class Image(Base):
    __tablename__ = 'image'

    id = Column(Integer, nullable=False, unique=True, primary_key=True, autoincrement=True)
    category_id = Column(Integer, ForeignKey('category.id', ondelete='CASCADE'), nullable=False)
    position = Column(Enum(ImagePositionEnum), nullable=False, default='Horizontal')
    name = Column(VARCHAR(100), nullable=False)
