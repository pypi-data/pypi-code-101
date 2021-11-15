# core
from geopandas import read_file
from sqlalchemy import create_engine
import os


def _create_engine(db_config):
    engine = create_engine(
        f"postgresql://{db_config['DB_USER']}:{db_config['DB_PASSWORD']}@{db_config['DB_HOST']}:{db_config['DB_PORT']}/{db_config['DB_NAME']}")

    return engine


def _write_to_postgis(sql_engine, target_file, file_name, if_exists):
    gbf = read_file(target_file)

    try:
        gbf.to_postgis(
            name=file_name, con=sql_engine, if_exists=if_exists)
        print(f'写入 {file_name} 成功')
    except:
        raise ConnectionError("写入 geojson 失败")


def exec_import_data(db_config, relative_path, if_exists):

    sql_engine = _create_engine(db_config=db_config)

    abs_path = os.path.abspath(relative_path)

    dir_list = os.listdir(abs_path)

    for file_name in dir_list:
        target_file = abs_path + '/' + file_name

        _write_to_postgis(sql_engine, target_file, file_name, if_exists)
