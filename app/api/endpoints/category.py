from typing import List

from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session

from app.crud.category import category_crud
from app.db.database import get_db
from app.schemas.category import Category

router = APIRouter(prefix="/category", tags=["category"])


@router.get("/{category_id}", response_model=Category)
async def get_category(category_id: int, db: Session = Depends(get_db)):
    artwork_category = category_crud.get(db, category_id)
    if artwork_category is None:
        raise HTTPException(status_code=404, detail='Artwork category not found')
    return artwork_category


@router.get("/", response_model=List[Category])
async def get_all_categories(db: Session = Depends(get_db)):
    return category_crud.get_all(db)
