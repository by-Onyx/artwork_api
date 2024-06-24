from typing import List

from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session

from app.crud.language import language_crud
from app.db.database import get_db
from app.schemas.language import Language

router = APIRouter(prefix='/language', tags=['language'])


@router.get('/{language_id}', response_model=Language)
async def get_language(language_id: int, db: Session = Depends(get_db)):
    language = language_crud.get(db, language_id)
    if language is None:
        raise HTTPException(status_code=404, detail='Language not found')
    return language


@router.get('/', response_model=List[Language])
async def get_all_languages(db: Session = Depends(get_db)):
    return language_crud.get_all(db)
