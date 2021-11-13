import os


def configuration(parent_package="", top_path=None):
    from numpy.distutils.misc_util import Configuration

    config = Configuration("utility", parent_package, top_path)

    libraries = []
    if os.name == "posix":
        libraries.append("m")

    config.add_extension(
        "_blas_wrap", sources=["_blas_wrap.pyx"], libraries=libraries
    )

    config.add_extension(
        "_math", sources=["_math.pyx"], libraries=libraries
    )

    return config

if __name__ == "__main__":
    from numpy.distutils.core import setup
    setup(configuration=configuration)
