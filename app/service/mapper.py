from app.db.base import Image, Description
from app.schemas.description import ArtworkDescriptionSchema
from app.service.image_position import ImagePositionEnum


def to_artwork_image_model(name: str, category_id: int, position: ImagePositionEnum):
    return Image(name=name, category_id=category_id, position=position)


# def to_artwork_description_model(artwork_description: ArtworkDescriptionSchema):
#     return Description(
#         artwork_id=artwork_description.artwork_id,
#         language_id=artwork_description.language_id,
#         description=artwork_description.description,
#     )
