"""Sphinx ReadTheDocs theme.

From https://github.com/ryan-roemer/sphinx-bootstrap-theme.

"""

__all__ = ('__version__',)

import os
from pkg_resources import get_distribution, DistributionNotFound


try:
    __version__ = get_distribution('documenteer').version
except DistributionNotFound:
    # package is not installed
    __version__ = 'unknown'


def get_html_theme_path():
    """Return list of HTML theme paths."""
    cur_dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    return cur_dir
