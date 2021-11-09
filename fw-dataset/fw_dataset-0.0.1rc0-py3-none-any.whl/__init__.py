"""fw_dataset package metadata."""
from importlib import metadata

PKG_NAME = __name__
try:
    __version__ = metadata.version(__name__)
except metadata.PackageNotFoundError:
    pass

from .dataset import Dataset
