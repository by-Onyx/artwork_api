from fastapi import APIRouter

from .endpoints import language, category, image, description, artwork

api_router = APIRouter()
api_router.include_router(language.router)
api_router.include_router(category.router)
api_router.include_router(image.router)
api_router.include_router(description.router)
api_router.include_router(artwork.router)
