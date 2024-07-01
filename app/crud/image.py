from typing import Optional

from sqlalchemy.orm import Session

from app.crud.base import CreateReadBase
from app.db.base import Image
from app.service.image_position import ImagePositionEnum


class ImageCRUD(CreateReadBase[Image]):
    def get_all_artwork_image_ids(self, db: Session, position: Optional[ImagePositionEnum],
                                  category_id: Optional[int]) -> list[int]:
        query = db.query(Image.id).order_by(Image.creation_year)

        if position is not None:
            query = query.filter(Image.position == position)
        if category_id is not None:
            query = query.filter(Image.category_id == category_id)

        return [id for id, in query.all()]


image_crud = ImageCRUD(Image)
