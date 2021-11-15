import logging
from pathlib import Path

log = logging.getLogger(__name__)

WIN_ENCODING = 'ISO-8859-1'

HOME_DIR = Path.home()

PACKAGE_DIR = Path(__file__).absolute().resolve().parent
PACKAGE_NAME = PACKAGE_DIR.name
SRC_DIR = PACKAGE_DIR.parent
if SRC_DIR.name != 'src':
    SRC_DIR = PACKAGE_DIR
REPO_DIR = SRC_DIR.parent
DOCS_DIR = REPO_DIR / 'docs'
IMAGES_DIR = DOCS_DIR / 'images'

DATA_DIR_NAME = f'.{PACKAGE_NAME}-data'
DATA_DIR = PACKAGE_DIR / DATA_DIR_NAME
if not DATA_DIR.is_dir():
    DATA_DIR = REPO_DIR / DATA_DIR_NAME
# canonical data directory to share data between nlpia2 installations
HOME_DATA_DIR = HOME_DIR / DATA_DIR_NAME
if not HOME_DATA_DIR.is_dir():
    # TODO: use tempfiles.tempdir()?
    HOME_DATA_DIR.mkdir(parents=True, exist_ok=True)
if not DATA_DIR.is_dir():
    DATA_DIR = HOME_DATA_DIR


# TODO: share data between users of jupyter hub or tljh
# configurable location to share data between users on the same machine
# canonical data directory to share with other applications
# SHARED_DATA_DIR = Path('/data')
