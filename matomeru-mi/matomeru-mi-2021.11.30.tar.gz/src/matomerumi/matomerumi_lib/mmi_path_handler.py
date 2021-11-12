# MMI v2.0
# Codename: Fir
# Copyright 2021 Fe-Ti
"""!
Path handler class module.
"""
from pathlib import Path

class PathHandler:
    """!
    Path handler class.
    
    This handles relative and absolute paths.
    """
    def __init__(self, some_path, target_file=''):
        """!
        Init function guesses if the path is absolute and if it is not
        then the path is transformed to an absolute one.
        """
        self.path = Path(str(some_path))
        if not self.path.is_absolute():
            self.path = self.path.cwd() / Path(str(target_file)).parent / self.path
    def __str__(self):
        return str(self.path)
    def str(self):
        return str(self.path)

