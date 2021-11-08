# PYTHON_ARGCOMPLETE_OK
"""pyland: launch auto test framework with Pytest."""
from _pyland.api.run import run_server
from _pyland.thirdparty import CaseManage
from _pyland.thirdparty import GroupManage
from _pyland.thirdparty import ProjectManage
from _pyland.thirdparty import ResultManage
from _pyland.utils import injson
from _pyland.utils import support
from _pyland.utils import client
from _pyland.utils import assertion
from _pyland.utils import error
from _pyland.cases_collect import list_case
from _pyland.cases_collect import update_case
from _pyland.cases_execute import run_case
from _pyland.config import Config
from _pyland.config import YamlParam
from _pyland.config import com_params
from _pyland.config import com_params_obj
from _pyland.extractor import extract
from _pyland.log import Logger
from _pyland.log import logger
from _pyland.pre_request import PRequest
from _pyland.pytest_run import run_by
from _pyland.sql import Sql
from _pyland.cmd import console_main
from _pyland.cmd import main
from _pyland import exceptions
from _pyland import commands
from _pyland import config
from _pyland import utils
from _pyland.scaffold import main_scaffold


__all__ = [
    "injson",
    "client",
    "assertion",
    "extract",
    "Config",
    "logger",
    "Logger",
    "run_by",
    "list_case",
    "update_case",
    "run_case",
    "console_main",
    "main",
    "exceptions",
    "run_server",
    "commands",
    "utils",
    "config",
    "error",
    "com_params",
    "com_params_obj",
    "support"
]

import importlib_metadata

metadata = importlib_metadata.metadata("pyland")

__title__ = metadata["name"]
__summary__ = metadata["summary"]
__uri__ = metadata["home-page"]
__version__ = metadata["version"]
__author__ = metadata["author"]
__email__ = metadata["author-email"]
__license__ = metadata["license"]

if __name__ == "__main__":
    import pyland
    raise SystemExit(pyland.console_main())
