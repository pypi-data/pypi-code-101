from configparser import ConfigParser
from importlib import resources

# Version of sochainer package
__version__ = "1.0.0"

# Read URL of feed from config file
cfg = ConfigParser()
with resources.path("sochainer", "config.cfg") as path:
    cfg.read(str(path))

URL = cfg.get("feed", "url")