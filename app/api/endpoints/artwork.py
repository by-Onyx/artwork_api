from typing import List

from fastapi import Depends, APIRouter, HTTPException, Query
from sqlalchemy.orm import Session

from app.crud.description import description_crud
from app.crud.language import language_crud
from app.db.database import get_db
from app.crud.image import image_crud
from app.schemas.artwork import Artwork
from app.schemas.description import SimpleDescription
from app.service.image_position import ImagePositionEnum

router = APIRouter(prefix="/artwork", tags=["artwork"])


@router.get("/{artwork_id}", response_model=Artwork)
async def get_artwork(artwork_id: int, db: Session = Depends(get_db)):
    image = image_crud.get(db, artwork_id)
    if image is None:
        raise HTTPException(status_code=404, detail="Artwork not found")

    descriptions = description_crud.get_all_description_by_image_id(db, artwork_id)

    mapped_descriptions = [
        SimpleDescription(
            language=language_crud.get(db, description.language_id).name,
            description=str(description.description)
        )
        for description in descriptions
    ]

    return Artwork(
        id=image.id,
        name=image.name,
        position=image.position,
        descriptions=mapped_descriptions
    )


@router.get("/", response_model=List[Artwork])
async def get_all_artworks(position: ImagePositionEnum = Query(None, description="Filter by image position"),
                           category_id: int = Query(None, description="Filter by category id"),
                           db: Session = Depends(get_db)):
    ids = image_crud.get_all_artwork_image_ids(db=db, position=position, category_id=category_id)

    artwork_schemas = [
        await get_artwork(artwork_id=artwork_id, db=db) for artwork_id in ids
    ]

    return artwork_schemas


@router.get("/carousel/", response_model=List[Artwork])
async def get_carousel(db: Session = Depends(get_db)):
    ids = image_crud.get_all_carousel_images(db)

    artwork_schemas = [
        await get_artwork(artwork_id=artwork_id, db=db) for artwork_id in ids
    ]

    return artwork_schemas
