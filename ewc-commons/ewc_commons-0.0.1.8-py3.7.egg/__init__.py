from typing import Optional

"""Import the current library version number."""
from .__version__ import __version__


def app_version(name: Optional[str] = None, version: Optional[str] = None) -> str:
    """
    Generate an App name - Version - x string.

    :param name: An optional app name, defaults to 'EWC Commons Library'.
    :param version: An optional app version, defaults to current library version.
    :return: An App name - Version - x multiline string.
    """
    if name is None:
        name = "EWC Commons Library"
    if version is None:
        version = __version__
    return "\n".join([name, f"Version - {version}"])
