from app.crud.base import ReadBase
from app.db.base import Category


class CategoryCRUD(ReadBase[Category]):
    pass


category_crud = CategoryCRUD(Category)
