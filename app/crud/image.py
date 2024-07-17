from typing import Optional

from sqlalchemy import case
from sqlalchemy.orm import Session

from app.crud.base import CreateReadBase
from app.db.base import Image


class ImageCRUD(CreateReadBase[Image]):
    def get_all_artwork_image_ids(self, db: Session, category_id: Optional[int]) -> list[int]:
        query = db.query(Image.id).order_by(Image.creation_year)

        if category_id is not None:
            query = query.filter(Image.category_id == category_id)

        return [id for id, in query.all()]

    def get_all_carousel_images(self, db: Session) -> list[int]:
        ids_to_filter = [176, 178, 196, 107, 182, 190, 202]

        ordering = case(
            {id: index for index, id in enumerate(ids_to_filter)},
            value=Image.id
        )

        query = db.query(Image.id).filter(Image.id.in_(ids_to_filter)).order_by(ordering)
        return [id for id, in query.all()]


image_crud = ImageCRUD(Image)
