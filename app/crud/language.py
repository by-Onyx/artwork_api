from app.crud.base import ReadBase
from app.db.base import Language


class LanguageCRUD(ReadBase[Language]):
    pass


language_crud = LanguageCRUD(Language)
