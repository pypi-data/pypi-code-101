"""
configuration management
"""

import json
import pathlib

config_locations = [ "~/.worktree/config.json"]
default_config = {"clone.path": "~/.worktree/repos", "projects.path": "~/projects"}

def load_config():
    """Load configuration file"""

    for location in config_locations:
        path = pathlib.Path(location)

        if path.exists():
            with open(location, "r") as config:
                return json.load(config)

    return default_config
