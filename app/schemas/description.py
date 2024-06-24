from typing import Optional
from pydantic import BaseModel


class Description(BaseModel):
    id: Optional[int] = None
    image_id: Optional[int] = None
    language_id: Optional[int] = None
    description: Optional[str] = None

    class Config:
        orm_mode = True


class CreateDescription(BaseModel):
    image_id: Optional[int] = None
    language_id: Optional[int] = None
    description: Optional[str] = None

    class Config:
        orm_mode = True


class SimpleDescription(BaseModel):
    language: Optional[str] = None
    description: Optional[str] = None

    class Config:
        orm_mode = True
