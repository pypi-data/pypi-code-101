#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Select a gitignore for the current directory"""
from pathlib import Path
from shutil import copy
import subprocess
import sys

try:
    from appdirs import user_data_dir

    GI_DIR = Path(user_data_dir("gitignore"))
except ImportError:
    from os import getenv

    GI_DIR = Path(f"{getenv('HOME')}/templates/gitignore")


def dir_yield(path: Path):
    """recursively yield from all directories in the gitignore repo"""
    for entry in path.iterdir():
        if entry.is_dir() and "git" not in entry.name:
            yield from dir_yield(entry.resolve())
        elif not entry.name.endswith(".gitignore"):
            continue
        yield entry.resolve()


def get_gitignores():
    """download the gitignore repository if it doesn't exist"""
    try:
        # HACK: this checks if the dir: doesn't exist OR exists and is empty
        if not GI_DIR.exists() or (not GI_DIR.exists() and not any(GI_DIR.iterdir())):
            GI_DIR.mkdir(parents=True)
            print("Cloning gitignore repository...")
            subprocess.run(
                ["git", "clone", "https://github.com/github/gitignore", GI_DIR],
                check=True,
            )
            print(f"gitignores cloned to '{GI_DIR}'")
        return
    except PermissionError as err:
        raise NotImplementedError from err
    except subprocess.CalledProcessError as err:
        raise NotImplementedError from err


def main():
    """select a gitignore"""
    # dict comprehension where key is the filename w/o gitignore and value is file path
    get_gitignores()
    gitignores = {
        f.name.replace(".gitignore", ""): f.resolve() for f in dir_yield(GI_DIR)
    }

    # use argument if one is provided, otherwise choose interactively
    try:
        chosen = sys.argv[1]
    except IndexError:
        raise SystemExit(1)

    try:
        # change all dict keys to lowercase
        gitignores = {name.lower(): loc for name, loc in gitignores.items()}
        copy(gitignores[chosen], f"{sys.argv[2]}/.gitignore")
    except KeyError:
        print(f"'{chosen}' is not a valid gitignore type.")
        sys.exit(1)


if __name__ == "__main__":
    main()
