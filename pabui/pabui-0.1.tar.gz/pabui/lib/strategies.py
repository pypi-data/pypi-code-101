import json
import subprocess

from pathlib import Path


class StrategyLoadError(Exception):
    pass 


class StrategiesLoader:
    RELATIVE_PAB_PATH = Path("venv/bin/pab")  # TODO: Try to dinamically find virtualenv

    def __init__(self, directory: Path) -> None:
        self.directory = directory

    def get_strategies_data(self):
        self.check_valid_pab()
        proc = subprocess.run(
            (self.RELATIVE_PAB_PATH, "list-strategies", "-j"), 
            cwd=self.directory, 
            stdout=subprocess.PIPE
        )
        if proc.returncode != 0:
            raise StrategyLoadError("Error loading strategies.")
        return json.loads(proc.stdout.decode())
    
    def check_valid_pab(self):
        pab_path = self.directory / self.RELATIVE_PAB_PATH
        if not pab_path.is_file():
            raise StrategyLoadError("PAB executable not found in project venv")
