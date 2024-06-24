from app.db.database import Base, engine
from .models.language import Language
from .models.image import Image
from .models.category import Category
from .models.description import Description

Base.metadata.create_all(bind=engine)
