from enum import Enum, auto

class DatasetType(Enum):
    db = auto()
    file = auto()

class FileType(Enum):
    csv = auto()
    parquet = auto()

class VarType(Enum):
    df = auto()
