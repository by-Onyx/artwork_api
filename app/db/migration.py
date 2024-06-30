import json
import os
import shutil

from sqlalchemy import Table
from sqlalchemy.exc import SQLAlchemyError

from app.db.database import engine, metadata

__data_dir = 'db_data'
__source_dir = '../../../artwork_image'
__destination_dir = 'db_data/artwork_image'


def copy_artwork_dir(source_dir, destination_dir, reverse=False):
    try:
        if reverse:
            source_dir, destination_dir = destination_dir, source_dir

        # Создаем целевую директорию, если она не существует
        os.makedirs(destination_dir, exist_ok=True)

        # Копируем содержимое исходной директории в целевую
        for item in os.listdir(source_dir):
            source_item = os.path.join(source_dir, item)
            destination_item = os.path.join(destination_dir, item)

            if os.path.isdir(source_item):
                # Если текущий элемент является директорией, рекурсивно копируем её
                shutil.copytree(source_item, destination_item, symlinks=True)
            else:
                # Если текущий элемент является файлом, копируем его
                shutil.copy2(source_item, destination_item)

        print(f"Директория {source_dir} успешно скопирована в {destination_dir}")
    except OSError as e:
        print(f"Ошибка при копировании директории {source_dir} в {destination_dir}: {e}")


def extract_and_save_data():
    os.makedirs(__data_dir, exist_ok=True)
    copy_artwork_dir(__source_dir, __destination_dir)
    with engine.connect() as connection:
        metadata.reflect(bind=engine)
        for table_name in metadata.tables:
            table = Table(table_name, metadata, autoload_with=engine)
            result = connection.execute(table.select()).fetchall()
            columns = table.columns.keys()
            data = [dict(zip(columns, row)) for row in result]

            with open(f'db_data/{table_name}.json', 'w') as f:
                json.dump(data, f, indent=4)
            print(f"Data from table {table_name} saved to db_data/{table_name}.json")


def load_data():
    copy_artwork_dir(__source_dir, __destination_dir, reverse=True)
    with engine.connect() as connection:
        metadata.reflect(bind=engine)
        files = [f for f in os.listdir(__data_dir) if f.endswith('.json')]

        for file in files:
            table_name = file.split('.')[0]
            table = Table(table_name, metadata, autoload_with=engine)

            with open(os.path.join(__data_dir, file), 'r') as f:
                data = json.load(f)

            if data:
                try:
                    connection.execute(table.insert(), data)
                    connection.commit()
                    print(f"Data inserted into table {table_name} from {file}")
                except SQLAlchemyError as e:
                    print(f"Error inserting data into table {table_name}: {e}")

extract_and_save_data()