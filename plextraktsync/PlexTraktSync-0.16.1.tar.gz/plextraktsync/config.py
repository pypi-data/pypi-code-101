import json
from json import JSONDecodeError
from os import getenv
from os.path import exists

from dotenv import load_dotenv

from plextraktsync.path import (cache_dir, config_file, default_config_file,
                                env_file)

"""
Platform name to identify our application
"""
PLEX_PLATFORM = "PlexTraktSync"

"""
Constant in seconds for how much to wait between Trakt POST API calls.
"""
TRAKT_POST_DELAY = 1.1


class Config(dict):
    env_keys = [
        "PLEX_BASEURL",
        "PLEX_FALLBACKURL",
        "PLEX_TOKEN",
        "PLEX_USERNAME",
        "TRAKT_USERNAME",
    ]

    initialized = False
    config_file = config_file
    env_file = env_file

    def __getitem__(self, item):
        if not self.initialized:
            self.initialize()
        return dict.__getitem__(self, item)

    def initialize(self):
        defaults = self.load_json(default_config_file)
        self.update(defaults)

        if not exists(self.config_file):
            with open(self.config_file, "w") as fp:
                fp.write(json.dumps(defaults, indent=4))

        config = self.load_json(self.config_file)
        self.update(config)

        load_dotenv(self.env_file)
        for key in self.env_keys:
            value = getenv(key)
            if value == "-" or value == "None" or value == "":
                value = None
            self[key] = value

        self.initialized = True

        self["cache"]["path"] = self["cache"]["path"].replace("$PTS_CACHE_DIR", cache_dir)

    def save(self):
        with open(self.env_file, "w") as txt:
            txt.write("# This is .env file for PlexTraktSync\n")
            for key in self.env_keys:
                if key in self and self[key] is not None:
                    txt.write("{}={}\n".format(key, self[key]))
                else:
                    txt.write("{}=\n".format(key))

    @staticmethod
    def load_json(path):
        with open(path, "r") as fp:
            try:
                config = json.load(fp)
            except JSONDecodeError as e:
                raise RuntimeError(f"Unable to parse {path}: {e}")
        return config


CONFIG = Config()
