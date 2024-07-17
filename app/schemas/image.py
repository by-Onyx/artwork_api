from typing import Optional
from pydantic import BaseModel


class ImageCreate(BaseModel):
    category_id: Optional[int] = None

    class Config:
        orm_mode = True


class Image(BaseModel):
    id: Optional[int] = None
    category_id: Optional[int] = None
    name: Optional[str] = None

    class Config:
        orm_mode = True
