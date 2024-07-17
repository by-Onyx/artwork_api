import datetime

from fastapi import Depends, APIRouter, HTTPException, UploadFile, Form
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.crud.image import image_crud
from app.schemas.image import Image
from app.service import image_service

router = APIRouter(prefix="/image", tags=["image"])


@router.post("/", response_model=bool)
async def create_image(file: UploadFile, category_id: int = Form(int),
                       creation_year: int = Form(int),
                       db: Session = Depends(get_db)):
    image = image_service.add_text_to_image(image=file)
    # if image is None:
    #     raise HTTPException(status_code=404, detail='Image not created')
    # artwork_image = image_crud.create(db, name=file.filename, category_id=category_id, creation_year=creation_year)
    return True
