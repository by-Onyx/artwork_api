# from typing import Type, List, Optional
# from sqlalchemy.orm import Session
# from app.db.base import ArtworkDescription
#
#
# def get_all_artwork_descriptions(db: Session) -> List[Type[ArtworkDescription]]:
#     return db.query(ArtworkDescription).all()
#
#
# def get_artwork_description_by_id(db: Session, artwork_description_id: int) -> Optional[ArtworkDescription]:
#     return db.query(ArtworkDescription).filter(ArtworkDescription.id == artwork_description_id).first()
#
#
# def get_all_description_by_image_id(db: Session, artwork_image_id: int) -> List[Type[ArtworkDescription]]:
#     return db.query(ArtworkDescription).filter(ArtworkDescription.artwork_id == artwork_image_id).all()
#
#
# def create_artwork_description(db: Session, artwork_description: ArtworkDescription) -> \
#         Optional[ArtworkDescription]:
#     db.add(artwork_description)
#     db.commit()
#     db.refresh(artwork_description)
#     return artwork_description
from typing import List, Type

from sqlalchemy.orm import Session

from app.crud.base import CreateReadBase
from app.db.base import Description


class DescriptionCRUD(CreateReadBase[Description]):
    def get_all_description_by_image_id(self, db: Session, artwork_image_id: int) -> List[Type[Description]]:
        return db.query(Description).filter(Description.image_id == artwork_image_id).all()


description_crud = DescriptionCRUD(Description)
