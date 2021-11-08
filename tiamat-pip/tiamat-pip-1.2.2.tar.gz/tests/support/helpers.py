import logging
import os
import pathlib
import random
import shutil
import string
import subprocess
import textwrap
from typing import List
from typing import Optional

import attr

import tiamatpip
from tiamatpip.store import Store

log = logging.getLogger(__name__)

CODE_ROOT = pathlib.Path(tiamatpip.__file__).resolve().parent.parent


def random_string(prefix, size=6, uppercase=True, lowercase=True, digits=True):
    """
    Generates a random string.

    :keyword str prefix: The prefix for the random string
    :keyword int size: The size of the random string
    :keyword bool uppercase: If true, include upper-cased ascii chars in choice sample
    :keyword bool lowercase: If true, include lower-cased ascii chars in choice sample
    :keyword bool digits: If true, include digits in choice sample
    :return str: The random string
    """
    if not any([uppercase, lowercase, digits]):
        raise RuntimeError(
            "At least one of 'uppercase', 'lowercase' or 'digits' needs to be true"
        )
    choices = []
    if uppercase:
        choices.extend(string.ascii_uppercase)
    if lowercase:
        choices.extend(string.ascii_lowercase)
    if digits:
        choices.extend(string.digits)

    return prefix + "".join(random.choice(choices) for _ in range(size))


@attr.s(frozen=True)
class ProcessResult:
    """
    This class serves the purpose of having a common result class which will hold the
    resulting data from a subprocess command.
    """

    exitcode = attr.ib()
    stdout = attr.ib()
    stderr = attr.ib()
    cmdline = attr.ib(default=None, kw_only=True)

    @exitcode.validator
    def _validate_exitcode(self, attribute, value):
        if not isinstance(value, int):
            raise ValueError(f"'exitcode' needs to be an integer, not '{type(value)}'")

    def __str__(self):
        message = self.__class__.__name__
        if self.cmdline:
            message += f"\n Command Line: {self.cmdline}"
        if self.exitcode is not None:
            message += f"\n Exitcode: {self.exitcode}"
        if self.stdout or self.stderr:
            message += "\n Process Output:"
        if self.stdout:
            message += f"\n   >>>>> STDOUT >>>>>\n{self.stdout}\n   <<<<< STDOUT <<<<<"
        if self.stderr:
            message += f"\n   >>>>> STDERR >>>>>\n{self.stderr}\n   <<<<< STDERR <<<<<"
        return message + "\n"


@attr.s(kw_only=True, slots=True)
class TiamatPipProject:
    name: str = attr.ib()
    path: pathlib.Path = attr.ib()
    pypath: Optional[pathlib.Path] = attr.ib(init=False)
    build_conf_contents: str = attr.ib()
    run_py_contents: str = attr.ib()
    requirements: List[str] = attr.ib(default=attr.Factory(list))
    requirements_txt_contents: str = attr.ib()
    build_conf: pathlib.Path = attr.ib(init=False)
    run_py: Optional[pathlib.Path] = attr.ib(init=False)
    requirements_txt: Optional[pathlib.Path] = attr.ib(init=False)

    @name.default
    def _default_name(self):
        return random_string("project-")

    @pypath.default
    def _default_pypath(self):
        pypath = self.path / "pypath"
        pypath.mkdir(parents=True, exist_ok=True, mode=0o755)
        return pypath

    @build_conf.default
    def _default_build_conf(self):
        return self.path / "build.conf"

    @build_conf_contents.default
    def _default_build_conf_contents(self):
        return textwrap.dedent(
            """\
        tiamat:
          name: {}
          dev_pyinstaller: True
        """.format(
                self.name
            )
        )

    @run_py.default
    def _default_run_py(self):
        return self.path / "run.py"

    @run_py_contents.default
    def _default_run_py_contents(self):
        return textwrap.dedent(
            """\
            #!/usr/bin/env python3

            import os
            import sys
            import traceback
            import multiprocessing
            import tiamatpip.cli
            import tiamatpip.configure

            tiamatpip.configure.set_user_base_path({!r})

            def main(argv):
                if argv[1] == "shell":
                    py_shell()
                    return
                if tiamatpip.cli.should_redirect_argv(argv):
                    tiamatpip.cli.process_pip_argv(argv)

                # If we reached this far, it means we're not handling pip stuff

                if argv[1] == "test":
                    print("Tested!")
                if argv[1] == "code":
                    try:
                        exec(sys.argv[2].strip(), globals().copy(), locals())
                    except:
                        traceback.print_exc()
                        sys.exit(1)
                else:
                    print("No command?!")

                sys.exit(0)


            def py_shell():
                import readline  # optional, will allow Up/Down/History in the console
                import code

                variables = globals().copy()
                variables.update(locals())
                shell = code.InteractiveConsole(variables)
                shell.interact()

            if __name__ == "__main__":
                if sys.platform.startswith("win"):
                    multiprocessing.freeze_support()
                main(sys.argv)
            """.format(
                str(self.pypath)
            )
        )

    @requirements_txt.default
    def _default_requirements_txt(self):
        return self.path / "requirements.txt"

    @requirements_txt_contents.default
    def _default_requirements_txt_contents(self):
        return "\n".join([str(CODE_ROOT)] + list(self.requirements))

    def __attrs_post_init__(self):
        self.build_conf.write_text(self.build_conf_contents)
        self.run_py.write_text(self.run_py_contents)
        self.requirements_txt.write_text(self.requirements_txt_contents)

    @property
    def generated_binary_path(self) -> pathlib.Path:
        return self.path / "dist" / self.name

    def copy_generated_project_to(self, path: pathlib.Path) -> None:
        dst = path / self.generated_binary_path.name
        log.info("Copying %s -> %s", self.generated_binary_path, dst)
        if self.generated_binary_path.is_dir():
            shutil.copytree(self.generated_binary_path, dst)
        else:
            shutil.copyfile(self.generated_binary_path, dst)

    def run(self, *args, cwd=None, check=None, **kwargs):
        if cwd is None:
            cwd = str(self.path)
        cmdline = [str(self.generated_binary_path.relative_to(self.path))]
        cmdline.extend(list(args))
        env = os.environ.copy()
        env["TIAMAT_PIP_DEBUG"] = "1"
        result = subprocess.run(
            cmdline,
            cwd=cwd,
            env=env,
            check=check,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True,
            **kwargs,
        )
        if check is True:
            result.check_returncode()
        ret = ProcessResult(
            result.returncode,
            result.stdout,
            result.stderr,
            cmdline=args,
        )
        log.debug(ret)
        return ret

    def run_code(self, code):
        if code.startswith("\n"):
            code = code[1:]
        code = textwrap.dedent(code)
        return self.run("code", code)

    def build(self):
        subprocess.run(
            ["tiamat", "--log-level=debug", "build", "-c", "build.conf"],
            cwd=self.path,
            check=True,
        )

    def delete_pypath(self):
        shutil.rmtree(self.pypath, ignore_errors=True)

    def get_store(self):
        return Store(pypath=self.pypath)

    def __enter__(self):
        self.build()
        return self

    def __exit__(self, *args):
        shutil.rmtree(self.path, ignore_errors=True)
