from typing import Optional
from pydantic import BaseModel

from app.service.image_position import ImagePositionEnum


class ImageCreate(BaseModel):
    category_id: Optional[int] = None
    position: Optional[ImagePositionEnum] = ImagePositionEnum.HORIZONTAL

    class Config:
        orm_mode = True


class Image(BaseModel):
    id: Optional[int] = None
    category_id: Optional[int] = None
    position: Optional[ImagePositionEnum] = None
    name: Optional[str] = None

    class Config:
        orm_mode = True
