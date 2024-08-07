from typing import Optional, List
from pydantic import BaseModel

from app.schemas.description import SimpleDescription


class Artwork(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None
    descriptions: List[SimpleDescription] = []

    class Config:
        orm_mode = True

    def __init___(self, artwork_id: int, name: str, descriptions: List[SimpleDescription]) -> None:
        super(Artwork, self).__init__(id=artwork_id, name=name, description=descriptions)
        self.id = artwork_id
        self.name = name
        self.descriptions = descriptions
