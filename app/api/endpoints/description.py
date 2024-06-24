from typing import List

from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.crud.description import description_crud
from app.schemas.description import Description, CreateDescription

router = APIRouter(prefix='/artwork_description', tags=['artwork_description'])


@router.get('/{description_id}', response_model=Description)
async def get_description(description_id: int, db: Session = Depends(get_db)):
    artwork_description = description_crud.get(db, description_id)
    if artwork_description is None:
        raise HTTPException(status_code=404, detail='Artwork description not found')
    return artwork_description


@router.get('/', response_model=List[Description])
async def get_descriptions(db: Session = Depends(get_db)):
    return description_crud.get_all(db)


@router.post('/', response_model=Description)
async def create_description(description: CreateDescription, db: Session = Depends(get_db)):
    return description_crud.create(db, image_id=description.image_id, language_id=description.language_id,
                                   description=description.description)
