import sys
from typing import IO, Any

from colorama import Style, init

_isInited = False

if not _isInited:
    _isInited = True
    init()


def printColor(*values: Any, sep: str = " ", end: str = "\n", file: IO[str] = sys.stdout, flush: bool = False, color: list[Any] = []):
    '''color 数组参数 colorama.Fore / colorama.Back / colorama.Style 的常量'''
    newValues = color + list(values) + [Style.RESET_ALL]
    print(*newValues, sep=sep, end=end, file=file, flush=flush)


def setPrintColor(*colorList: Any):
    content = "".join(colorList)
    if content:
        sys.stdout.write(content)
        sys.stderr.write(content)


def resetPrintColor():
    sys.stdout.write(Style.RESET_ALL)
    sys.stderr.write(Style.RESET_ALL)
