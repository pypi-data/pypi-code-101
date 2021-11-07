import glob
import os
import random
from typing import List

from xlsx_lib.domain.motorcycle_model.motorcycle_model import MotorcycleModel
from xlsx_lib.domain.motorcycle_model.motorcycle_model_workbook import MotorcycleModelWorkbook


def create_motorcycle_model(filename: str):
    motorcycle_model: MotorcycleModel = MotorcycleModelWorkbook(
        file=filename,
        filename=filename,
    ).motorcycle_model

    pass


def create_all_models() -> List[MotorcycleModel]:
    filenames: List[str] = glob.glob("./xlsx_lib/files/*.xlsx", recursive=True)

    models: List[MotorcycleModel] = list()
    # TODO: Create directory name

    directory_name: str = f"./xlsx_lib/json/{random.randint(0, 999)}"

    try:
        os.mkdir(directory_name)
    except OSError as error:
        print(error)

    for filename in filenames:
        create_motorcycle_model(
            filename=filename,
        )

    return models


if __name__ == "__main__":
    # create_motorcycle_model("./xlsx_lib/files/FICHA T MAX 560 2020.xlsx")
    # create_motorcycle_model("/home/tomasdarioam/projects/infomoto/vps-backup/a1/_data/gilera/sc-125-06/FICHA  SC 125  ´06 -.xlsx")
    # create_motorcycle_model("files/FICHA MONSTER 796.xlsx")
    # create_motorcycle_model("files/FICHA PEGASO 650 ´93 ´00.xlsx")
    # create_motorcycle_model("files/FICHA XVS 950 STAR ´14.xlsx")
    # create_motorcycle_model("files/FICHA FORZA 125 ´15 .xlsx")
    # create_motorcycle_model("files/FICHA ATLANTIC 125 200 ´02.xlsx")
    # create_all_models()
    pass
