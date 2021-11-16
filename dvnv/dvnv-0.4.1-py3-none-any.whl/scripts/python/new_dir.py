#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pathlib import Path
import sys


def new_dir():
    """Creates a new Python project directory with a source dir and a tests dir"""
    proj_name = sys.argv[2]
    proj_path = Path(proj_name)
    # make the project directory
    if not proj_path.exists():
        proj_path.mkdir(parents=True)
    # create tests and src dirs
    for direc in (proj_name.replace("-", "_"), "tests"):
        sub_dir = proj_path / direc
        sub_dir.mkdir()
        (sub_dir / "__init__.py").touch()


if __name__ == "__main__":
    new_dir()
