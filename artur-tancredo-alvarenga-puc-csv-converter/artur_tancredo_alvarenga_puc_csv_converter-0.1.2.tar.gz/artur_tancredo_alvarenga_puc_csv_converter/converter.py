import logging

from pathlib import Path
import click
import pandas as pd

logging.basicConfig(
    Level='DEBUG', format="'%(asctime)s - %(name)s - %(levelname)s - %(message)s'"
)
logger = logging.getLogger(__name__)

@click.command()
@click.option("--input", "-i", default="./", help="Path where to read the files for conversion.", type=str)
@click.option("--output", "-o", default="./", help="Path where to read the files will be saved.", type=str)
@click.option("--delimiter", "-d", default=",", help="Separator used to split the files.", type=str)
@click.option("--prefix","-prefix", prompt=True, prompt_required=False, default='file',  
    help=(
        "Prefix used to prepend to the name of the converted file saved on disk."
        "The suffix will be a number starting from 0. ge: file_0.json."),)
def converter(input: str = "./", output: str = "./", delimiter: str = ',', prefix: str = None):  
    """Convert single file or list of csv to json"""
    input_path = Path(input)
    output_path = Path(output)
    logger.info("Input Path: %s", input_path)
    logger.info("Output Path: %s", output_path)

    for p in [input_path,output_path]:
        if not (p.is_file() or p.is_dir()):
            raise TypeError("Not a valid path or file name.")
        
    data = read_csv_file(source=input_path, delimiter=delimiter)
    save_to_json_files(csvs=data, output_path=output_path, prefix=prefix)

def read_csv_file(source: Path, delimiter: str) -> tuple:
    """Load csv files from disk.
    Source (Path): Path of a single csv file or directory containing csvs to be parsed.
    delimiter (str): Separator for columns in csv.
    Return:
        tuple: Tuple of DataFrames."""
    if source.is_file():
        logger.info("Reading Single File %s", source)
        return (pd.read_csv(filepath_or_buffer=source, delimiter=delimiter, index_col=False),)

    logger.info("Reandign all files for given path %s", source)
    data = list()
    for name in source.iterdir():
        data.append(pd.read_csv(filepath_or_buffer=name, delimiter=delimiter, index_col=False))

    return tuple(data)

def save_to_json_files(csvs: tuple, output_path: Path, prefix: str = None):
    """Save Dataframes to Disk"""

    i = 0
    while i < len(csvs):
        file_name = output_path.joinpath(f"{prefix}_{i}")
        logger.info("Savinf file %s in folder %s", file_name, output_path)

        data = csvs[i]
        data.to_json(path_or_buf=file_name, orient="records", indent=4)
        i += 1
        
