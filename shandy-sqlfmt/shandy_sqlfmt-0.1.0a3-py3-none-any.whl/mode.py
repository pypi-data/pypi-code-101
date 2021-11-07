import os
from dataclasses import dataclass, field
from typing import List

from sqlfmt.dialect import Dialect, Postgres


@dataclass
class Mode:

    SQL_EXTENSIONS: List[str] = field(default_factory=lambda: [".sql", ".sql.jinja"])
    dialect: Dialect = field(default_factory=lambda: Postgres())
    line_length: int = 88
    check: bool = False
    diff: bool = False
    verbose: bool = False
    _no_color: bool = False
    _force_color: bool = False

    @property
    def color(self) -> bool:
        """
        There are 4 considerations for setting color:
        1. The --force-color option
        2. The --no-color option
        3. The NO_COLOR environment variable
        4. The default behavior, which is to colorize output

        This property checks these flags, in descending order of priority,
        and sets the authoritative flag accordingly

        See no-color.org for details.
        """
        if self._force_color:
            return True
        elif self._no_color:
            return False
        elif os.environ.get("NO_COLOR", False):
            return False
        else:
            return True
