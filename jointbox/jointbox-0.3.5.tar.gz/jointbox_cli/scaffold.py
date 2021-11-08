#    JointBox CLI
#    Copyright (C) 2021 Dmitry Berezovsky
#    The MIT License (MIT)
#
#    Permission is hereby granted, free of charge, to any person obtaining
#    a copy of this software and associated documentation files
#    (the "Software"), to deal in the Software without restriction,
#    including without limitation the rights to use, copy, modify, merge,
#    publish, distribute, sublicense, and/or sell copies of the Software,
#    and to permit persons to whom the Software is furnished to do so,
#    subject to the following conditions:
#
#    The above copyright notice and this permission notice shall be
#    included in all copies or substantial portions of the Software.
#
#    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
#    EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
#    MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
#    IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
#    CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
#    TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
#    SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import abc
import argparse
import logging
import os
import shutil
import tempfile
from typing import Optional, Dict

from cli_rack import CLI
from cli_rack.ansi import Fg, Seq, Mod
from cli_rack.loader import LoadedDataMeta, DefaultLoaderRegistry
from cli_rack.modular import CliExtension
from cli_rack.utils import ensure_dir

LOGGER = logging.getLogger("scaffold")


class PreconditionsFailedError(Exception):
    pass


class BaseGenerator(CliExtension, abc.ABC):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._loader_registry = DefaultLoaderRegistry.clone()
        self._loader_registry.target_dir = tempfile.mkdtemp("jointbox-scaffold")

    def check_preconditions(self, location: str) -> None:
        pass

    @abc.abstractmethod
    def do_scaffold(self, location: str, params: argparse.Namespace):
        pass

    @classmethod
    def setup_parser(cls, parser: argparse.ArgumentParser):
        parser.add_argument(
            "--path",
            "-p",
            type=str,
            action="store",
            dest="path",
            default=".",
            help="Directory to put generated files to. If it doesn't exist generator will create it",
        )

    def handle(self, args: argparse.Namespace):
        return self.do_scaffold(os.path.abspath(args.path), args)

    def _load_repo(self, repo_locator: str) -> LoadedDataMeta:
        return self._loader_registry.load(repo_locator)

    def _copy_contents_to(self, source_dir: str, dest_dir: str, overrides: Optional[Dict[str, Optional[str]]] = None):
        if overrides is None:
            overrides = {}
        files = os.listdir(source_dir)
        for x in files:
            src = os.path.join(source_dir, x)
            dst = os.path.join(dest_dir, x)
            if x in overrides:
                if overrides[x] is None:
                    continue
                else:
                    dst = os.path.join(dest_dir, overrides[x])  # type: ignore
            if os.path.isdir(src):
                shutil.copytree(src, dst, dirs_exist_ok=True)  # type: ignore
            else:
                shutil.copy2(os.path.join(source_dir, x), dst)


class SelfGenerator(BaseGenerator):
    COMMAND_NAME = "self"
    COMMAND_DESCRIPTION = "Setups base structure to start new project from scratch"

    TEMPLATE_REPO_LOCATOR = "github://jointbox/project-template@master"
    JOINTBOX_EXECUTABLE = "jointbox"

    def check_preconditions(self, location: str) -> None:
        super().check_preconditions(location)
        if not os.path.exists(location):
            return
        if os.path.isfile(location):
            raise PreconditionsFailedError("Path must point a directory,not a file")
        if os.path.isfile(os.path.join(location, self.JOINTBOX_EXECUTABLE)):
            raise PreconditionsFailedError("Given path ({}) already contains JointBox project".format(location))

    def do_scaffold(self, location: str, params: argparse.Namespace):
        LOGGER.info("Scaffolding new project at {}".format(location))
        template_meta = self._load_repo(self.TEMPLATE_REPO_LOCATOR)
        template_path = os.path.join(template_meta.path, template_meta.target_path)
        target_path = params.path
        ensure_dir(target_path)
        self._copy_contents_to(
            template_path,
            params.path,
            overrides={"meta.json": None, "LICENSE": None, "README.md": None, "secrets.example.yaml": "secrets.yaml"},
        )
        jointbox_executable_path = os.path.join(params.path, self.JOINTBOX_EXECUTABLE)
        if os.path.exists(jointbox_executable_path):
            os.chmod(jointbox_executable_path, 0o755)
        LOGGER.info("Project is ready.")
        CLI.print_info("")
        CLI.print_info("")
        CLI.print_info("Navigate to {} and run ".format(location) + Seq.wrap(Fg.YELLOW + Mod.BOLD, '"./jointbox"'))
        CLI.print_info(
            "You may also want to edit "
            + Seq.wrap(Fg.YELLOW + Mod.BOLD, "secrets.yaml")
            + " and "
            + Seq.wrap(Fg.YELLOW + Mod.BOLD, "jointbox.env")
        )
        CLI.print_info("")
