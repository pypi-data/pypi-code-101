"""Package init module."""
import importlib.metadata
import logging
import os
import subprocess
import sys
from pathlib import Path
from typing import Union

PKG_NAME = __name__
__version__ = importlib.metadata.version(PKG_NAME)


PathLike = Union[str, os.PathLike, Path]

log = logging.getLogger(__name__)


def install_requirements(req_file):
    """Install requirements from a file programatically

    Args:
        req_file (str): Path to requirements file

    Raises:
        SystemExit: If there was an error from pip
    """
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", req_file])
    except subprocess.CalledProcessError as e:
        log.error(f"Could not install requirements, pip exit code {e.returncode}")
        sys.exit(1)


__all__ = ["install_requirements", "PKG_NAME", "__version__"]
