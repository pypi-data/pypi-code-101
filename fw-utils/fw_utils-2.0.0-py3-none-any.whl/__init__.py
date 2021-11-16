"""Flywheel utilities and common helpers."""
# pylint: disable=unused-import
try:
    from importlib.metadata import version
except ImportError:  # pragma: no cover
    from importlib_metadata import version  # type: ignore

__version__ = version(__name__)

from .dicts import AttrDict, attrify, flatten_dotdict, get_field, inflate_dotdict
from .files import AnyFile, BinFile, TempDir, TempFile, fileglob, open_any
from .filters import (
    BaseFilter,
    ExpressionFilter,
    IncludeExcludeFilter,
    NumberFilter,
    SetFilter,
    SizeFilter,
    StringFilter,
    TimeFilter,
)
from .formatters import (
    Template,
    Timer,
    format_datetime,
    format_template,
    hrsize,
    hrtime,
    pluralize,
    quantify,
)
from .parsers import (
    Pattern,
    get_datetime,
    parse_field_name,
    parse_hrsize,
    parse_hrtime,
    parse_pattern,
    parse_url,
)
from .state import Cached
from .testing import assert_like
