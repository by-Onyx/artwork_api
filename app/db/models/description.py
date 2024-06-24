from sqlalchemy import Column, Integer, VARCHAR, ForeignKey
from app.db.database import Base


class Description(Base):
    __tablename__ = 'description'

    id = Column(Integer, nullable=False, unique=True, primary_key=True, autoincrement=True)
    image_id = Column(Integer, ForeignKey('image.id', ondelete='CASCADE'), nullable=False)
    language_id = Column(Integer, ForeignKey('language.id', ondelete='CASCADE'), nullable=False)
    description = Column(VARCHAR(1024), nullable=False)
