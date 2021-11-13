import os.path
from pathlib import Path
import shutil
from distutils.command.clean import clean as Clean


def configuration(parent_package="", top_path=None):
    from numpy.distutils.misc_util import Configuration

    config = Configuration(None, parent_package, top_path)
    config.set_options(
        ignore_setup_xxx_py=True,
        assume_default_configuration=True,
        delegate_options_to_subpackages=True,
        quiet=False,
    )

    config.add_subpackage("pymyfit")

    return config


class CleanCommand(Clean):
    description = "Remove build artifacts from the source tree"

    def run(self):
        Clean.run(self)

        cwd = Path(__file__).resolve().parent
        remove_c_files = not os.path.exists(os.path.join(cwd, "PKG-INFO"))
        if remove_c_files:
            print("Will remove generated .c files")
        if os.path.exists("build"):
            shutil.rmtree("build")
        for dirpath, dirnames, filenames in os.walk("pymyfit"):
            for filename in filenames:
                if any(
                    filename.endswith(suffix)
                    for suffix in (".so", ".pyd", ".dll", ".pyc")
                ):
                    os.unlink(os.path.join(dirpath, filename))
                    continue
                extension = os.path.splitext(filename)[1]
                if remove_c_files and extension in [".c", ".cpp"]:
                    pyx_file = str.replace(filename, extension, ".pyx")
                    if os.path.exists(os.path.join(dirpath, pyx_file)):
                        os.unlink(os.path.join(dirpath, filename))
            for dirname in dirnames:
                if dirname == "__pycache__":
                    shutil.rmtree(os.path.join(dirpath, dirname))


def setup_package():
    metadata = dict(
        name="pymyfit",
        maintainer="Yelyzaveta Velizhanina",
        maintainer_email="velizhaninae@gmail.com",
        author="Yelyzaveta Velizhanina",
        platforms=["Mac OS-X"],
        test_suite="pytest",
        python_requires=">=3.8",
        cmdclass={"clean": CleanCommand},
    )

    metadata["configuration"] = configuration

    from numpy.distutils.core import setup

    setup(**metadata)


if __name__ == "__main__":
    setup_package()
