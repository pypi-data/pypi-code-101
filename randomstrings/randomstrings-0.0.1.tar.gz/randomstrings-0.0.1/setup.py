import os
import pathlib
import shutil
import sys

from setuptools import Command, setup

here = pathlib.Path(__file__).parent.resolve()

long_description = (here / 'README.md').read_text(encoding='utf-8')

URL = "https://pypi.org/project/random-strings/"
VERSION = '0.0.1'


class PublishCommand(Command):
    """Support setup.py publish."""

    description = "Build and publish the package."
    user_options = []

    @staticmethod
    def status(s):
        """Print things in bold."""
        print("\033[1m{0}\033[0m".format(s))

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        try:
            self.status("Removing older builds")
            shutil.rmtree(os.path.join(here, "dist"))
        except FileNotFoundError:
            print("No older builds exist, Do nothing")

        self.status("Building Source and Wheel")
        os.system("{0} setup.py sdist bdist_wheel".format(sys.executable))

        self.status("Uploading to PyPi using Twine")
        os.system("twine upload dist/*")

        sys.exit()


setup(
    name='randomstrings',
    version=VERSION,
    description='strings that are ✨ random ✨',
    url=URL,
    install_requires=['random-strings'],
    python_requires='>=3.6, <4',
    long_description=long_description,
    long_description_content_type='text/markdown',

    # setup.py publish
    cmdclass={
        "publish": PublishCommand,
    },
)
