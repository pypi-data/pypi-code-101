"""fw_dataset package metadata."""

try:
    from importlib import metadata

    from fw_core_client import CoreClient

    PY38_ENABLED = True
    try:
        __version__ = metadata.version(__name__)
    except metadata.PackageNotFoundError:
        pass
except ImportError:
    PKG_NAME = __name__
    PY38_ENABLED = False


from .dataset import Dataset
