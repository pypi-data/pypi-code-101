#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
import sys


def create_plugin_template():
    proj_name = sys.argv[2]
    proj_path = Path(proj_name)
    for directory in (f"autoload/{proj_name}", "doc", "plugin", "syntax", "tests"):
        (proj_path / directory).mkdir(parents=True)

    (proj_path / "doc" / f"{proj_name}.txt").touch()

    for directory in ("plugin", "syntax"):
        (proj_path / directory / f"{proj_name}.vim").touch()
