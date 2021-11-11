from pathlib import Path

from pabui.lib.utils import SimpleJsonFileHandler
from pabui.lib.strategies import StrategiesLoader
from pabui.lib.contracts import ContractsLoader

class PAB:
    def __init__(self, directory: str = None):
        self.directory = None
        self.config = None
        self.strategies = None
        self.tasks = None
        if directory:
            self.load(directory)
    
    def load(self, directory: Path):
        self.config = SimpleJsonFileHandler(directory / "config.json")
        self.tasks = SimpleJsonFileHandler(directory / "tasks.json")
        self.strategies = StrategiesLoader(directory)
        self.contracts = ContractsLoader(directory)
        self.directory = directory
        