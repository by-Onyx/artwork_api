from sqlalchemy import Column, Integer, VARCHAR
from app.db.database import Base


class Category(Base):
    __tablename__ = 'category'

    id = Column(Integer, nullable=False, unique=True, primary_key=True, autoincrement=True)
    name = Column(VARCHAR(100), nullable=False)
