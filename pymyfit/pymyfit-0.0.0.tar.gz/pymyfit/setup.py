from tools.cythonize import cythonize_ext

def configuration(parent_package="", top_path=None):
    from numpy.distutils.misc_util import Configuration

    config = Configuration("pymyfit", parent_package, top_path)

    config.add_subpackage("algorithms")
    config.add_subpackage("utility")

    cythonize_ext(config)

    return config

if __name__ == "__main__":
    from numpy.distutils.core import setup
    setup(configuration=configuration)
