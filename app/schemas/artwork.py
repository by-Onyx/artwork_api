from typing import Optional, List
from pydantic import BaseModel

from app.schemas.description import SimpleDescription
from app.service.image_position import ImagePositionEnum


class Artwork(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None
    position: Optional[ImagePositionEnum] = ImagePositionEnum.HORIZONTAL
    descriptions: List[SimpleDescription] = []

    class Config:
        orm_mode = True

    def __init___(self, artwork_id: int, name: str, descriptions: List[SimpleDescription], position: ImagePositionEnum) -> None:
        super(Artwork, self).__init__(id=artwork_id, name=name, description=descriptions, position=position)
        self.id = artwork_id
        self.name = name
        self.descriptions = descriptions
