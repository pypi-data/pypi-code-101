# -*- coding: utf-8 -*-
"""Automate the creation of development environments"""
from __future__ import annotations
import argparse
import os
from pathlib import Path
from shutil import copytree, rmtree
import subprocess
from typing import Dict, List, Union

from rich import print

from dvnv import SCRIPTS_DIR, VERSION
from dvnv.utils import check_dir, confirm, print_error


def copy_scripts(
    src: Path = Path(__file__).parent / "scripts",
    dest: Path = SCRIPTS_DIR,
    quiet: bool = False,
) -> bool:
    """Copies scripts from the dvnv installation to the local script directory

    Args:
        src: The directory to copy to dest.
        dest: The directory to copy to. Must be a filepath ending in "scripts"

    Returns:
        bool: True for on successful copy, False if the copy fails
    """
    try:
        copytree(src, dest)
        if not quiet:
            print(f"'{src}' copied to '{dest}'!")
    except FileExistsError:
        # ask before overwriting
        if confirm(f"'{dest}' already exists. Overwrite? [Y/n] "):
            rmtree(dest)
            return copy_scripts(src, dest)
        return False
    return True


def list_langs(script_dir: Path) -> Union[List[str], None]:
    """Returns a list of all available languages

    Args:
        script_dir: The directory to search for available languages

    Returns:
        list: A list containing any available language
    """
    available_languages: List[str] = []
    try:
        for entry in sorted(script_dir.iterdir()):
            if entry.is_dir():
                available_languages.append(entry.name)
        return available_languages
    except FileNotFoundError as err:
        print_error(err)
        return None


def run_scripts(script_dir: Path, lang: str, name: str, quiet: bool = False) -> bool:
    """Runs scripts in a given dir

    Args:
        script_dir: The directory to search for scripts
        lang: The main language of the project
        name: The name of the project

    Returns:
        bool: True for success, False otherwise
    """
    for script in sorted(script_dir.iterdir()):
        if not os.access(script, os.X_OK):
            if not quiet:
                print_error(f"'{script.name}' is not executable! Skipping.", "WARN")
            continue
        if script.is_file():
            try:
                if not quiet:
                    print(f"Running '{script.name}'...")
                subprocess.run([str(script.resolve()), lang, name], check=True)
            except subprocess.CalledProcessError as err:
                print_error(f"Error running '{script}'!")
                print_error(err)
                return False
    return True


def parse_args() -> argparse.Namespace:
    """Parse arguments

    Returns:
        argparse.Namespace: a Namespace with all collected arguments
    """
    parser: argparse.ArgumentParser = argparse.ArgumentParser(prog="dvnv")
    parser.add_argument(
        "lang", nargs="?", help="the language of the project", default=None
    )
    parser.add_argument("name", nargs="?", help="the name of the project", default=None)
    parser.add_argument(
        "--install_scripts", action="store_true", help="install the builtin scripts"
    )
    parser.add_argument(
        "-l",
        "--list",
        action="store_true",
        help="list available language directories",
    )
    parser.add_argument(
        "-q", "--quiet", action="store_true", help="supress non-fatal messages"
    )
    parser.add_argument(
        "--scripts_dir",
        help="the path to a 'scripts' directory",
        default=SCRIPTS_DIR,
        type=Path,
    )
    parser.add_argument("--version", action="version", version=f"%(prog)s {VERSION}")
    args: argparse.Namespace = parser.parse_args()

    # throw error when there are no positional args when needed
    if not args.install_scripts and not args.list:
        if not args.lang and not args.name:
            print_error("the following arguments are required: lang, name")
            parser.print_help()
            raise SystemExit(1)
        if not args.lang:
            print_error("the following arguments are required: lang")
            parser.print_help()
            raise SystemExit(1)
        if not args.name:
            print_error("the following arguments are required: name")
            parser.print_help()
            raise SystemExit(1)

    return args


def main(args: argparse.Namespace):
    """Run the program according to arguments provided

    Args:
        args: A Namespace object of arguments to provide
    """
    if args.install_scripts or args.list:
        if args.install_scripts:
            if not copy_scripts(dest=args.scripts_dir, quiet=args.quiet):
                print_error("Error copying scripts!")
        if args.list:
            if not (langs := list_langs(args.scripts_dir)):
                print_error(
                    f"Rerun with `--install_scripts` to populate `{args.scripts_dir}'."
                )
                raise SystemExit(1)
            print("Available languages are:", *langs)
        if not args.lang or args.name:
            raise SystemExit

    all_dir: Path = args.scripts_dir / "all"
    lang_dir: Path = args.scripts_dir / args.lang
    all_running: bool = check_dir(all_dir)
    lang_running: bool = check_dir(lang_dir)
    script_dirs: Dict[Path, bool] = {all_dir: all_running, lang_dir: lang_running}

    try:
        no_run: int = 0
        for directory, to_run in script_dirs.items():
            if not to_run:
                if not args.quiet:
                    print_error(
                        f"Skipping '{directory}', as there are no runnable scripts.",
                        "WARN",
                    )
                no_run += 1
                continue
            if not run_scripts(directory, args.lang, args.name, args.quiet):
                raise SystemExit(1)
        if no_run == 2:
            err = (
                f"Did not run any scripts; both '{all_dir}' and '{lang_dir}' are empty!"
            )
            raise SystemError(err)
    except PermissionError as err:
        raise PermissionError from err


if __name__ == "__main__":
    main(parse_args())
