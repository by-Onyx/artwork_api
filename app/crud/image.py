from sqlalchemy.orm import Session

from app.crud.base import CreateReadBase
from app.db.base import Image
from app.service.image_position import ImagePositionEnum


class ImageCRUD(CreateReadBase[Image]):
    def get_all_artwork_image_ids(self, db: Session, position: ImagePositionEnum) -> list[int]:
        return [id for id, in db.query(Image.id).filter(Image.position == position).all()]


image_crud = ImageCRUD(Image)
