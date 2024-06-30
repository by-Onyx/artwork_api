import os
from io import BytesIO

from PIL import Image, ImageDraw, ImageFont
from fastapi import UploadFile, HTTPException


def add_text_to_image(image: UploadFile, text='K.Dorokhova', font_path='../../font/STIXTwoText-VariableFont_wght.ttf',
                      color='white', text_proportion=0.3, margin_proportion=0.02,
                      scale_factor=2) -> bytes:
    # Проверка расширения файла
    __validate_image_extension(image)

    # Чтение и обработка изображения
    img = __process_image(image, scale_factor)

    # Добавление текста на изображение
    img_with_text = __draw_text_on_image(img, text, font_path, color, text_proportion, margin_proportion)

    # Сохранение изображения в память и получение данных
    return __save_image_to_bytes(img_with_text, image.filename)


def __resize_image(image, scale_factor):
    width, height = image.size
    new_size = (width // scale_factor, height // scale_factor)
    return image.resize(new_size, Image.Resampling.LANCZOS)


def __validate_image_extension(image: UploadFile):
    allowed_extensions = {'jpg', 'jpeg', 'png', 'gif'}
    ext = image.filename.split('.')[-1]
    if ext.lower() not in allowed_extensions:
        raise HTTPException(status_code=415,
                            detail=f'Unsupported file extension: {ext}. Allowed extensions: '
                                   f'{", ".join(allowed_extensions)}')


def __process_image(image: UploadFile, scale_factor):
    # Чтение загруженного изображения
    img = Image.open(image.file)


    # Сжать изображение
    img = __resize_image(img, scale_factor)

    return img


def __draw_text_on_image(img, text, font_path, color, text_proportion, margin_proportion):
    # Создать объект для рисования
    draw = ImageDraw.Draw(img)

    # Получить размеры изображения
    image_width, image_height = img.size

    # Рассчитать начальный размер шрифта
    font_size = 10  # Начальный размер шрифта
    font = ImageFont.truetype(font_path, font_size)

    # Увеличивать размер шрифта, пока текст не займёт нужный процент от ширины изображения
    text_width = 0
    while text_width < image_width * text_proportion:
        font = ImageFont.truetype(font_path, font_size)
        text_bbox = draw.textbbox((0, 0), text, font=font)
        text_width = text_bbox[2] - text_bbox[0]
        font_size += 1

    # Получить окончательный размер текста
    text_height = text_bbox[3] - text_bbox[1]

    # Рассчитать отступы
    margin = int(image_width * margin_proportion)

    # Определить позицию текста (правый нижний угол с отступом)
    x = image_width - text_width - margin
    y = image_height - text_height - margin

    # Добавить текст на изображение
    draw.text((x, y), text, font=font, fill=color)

    return img


def __save_image_to_bytes(image, output_filename):
    try:
        # Составляем полный путь к файлу для сохранения
        output_path = os.path.join('../../artwork_image/', output_filename)

        # Создаем временный буфер для сохранения изображения в память
        output_buffer = BytesIO()

        # Сохраняем изображение в буфер output_buffer с указанным форматом
        image.save(output_buffer, format='jpeg')

        # Сохраняем изображение на диск в указанное место
        with open(output_path, 'wb') as f:
            f.write(output_buffer.getvalue())

        print(f'Изображение успешно сохранено как {output_path}')
        return output_path

    except Exception as e:
        print(f'Ошибка при сохранении изображения: {e}')
        return None
