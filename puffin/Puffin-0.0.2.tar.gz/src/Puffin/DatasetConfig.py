from abc import ABC
from dataclasses import dataclass
from pathlib import Path
from Puffin.enums import FileType, VarType, DatasetType

class DatasetConfig(ABC):
    def __init__(self, name):
        self.name = name
    
    def get_str_path(self):
        return str(self.path)
    
@dataclass
class FileDatasetConfig(DatasetConfig):
    name: str
    path: Path
    filetype: FileType
    vartype: VarType
    type: DatasetType = DatasetType.file
