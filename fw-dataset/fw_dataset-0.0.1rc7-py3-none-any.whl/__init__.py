"""fw_dataset package metadata."""
try:
    from importlib import metadata

    __version__ = metadata.version(__name__)
except ImportError:
    __version__ = "0.0.0"

from .dataset import Dataset
