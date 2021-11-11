import json

from typing import Optional
from pathlib import Path


class SimpleJsonFileHandler:
    def __init__(self, file: Path):
        self.file = file

    def save(self, data: dict) -> None:
        with self.file.open("w") as fp:
            json.dump(data, fp, indent=4)
            fp.flush()

    def read(self) -> Optional[dict]:
        with self.file.open("r") as fp:
            return json.load(fp)

    def _valid_file(self) -> bool:
        return self.file and self.file.is_file() 