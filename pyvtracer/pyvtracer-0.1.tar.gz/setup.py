from setuptools import find_packages, setup
from setuptools.dist import Distribution as _Distribution
from setuptools_rust import Binding, RustExtension


class BinaryDistribution(_Distribution):
    def has_ext_modules(foo):
        return True


setup(
    name="pyvtracer",
    version="0.1",
    author="Wook Song",
    author_email="wook16.song@samsung.com",
    maintainer="Wook Song",
    maintainer_email="wook16.song@samsung.com",
    rust_extensions=[RustExtension(
        "pyvtracer.pyvtracer", binding=Binding.PyO3)],
    packages=find_packages(),
    zip_safe=False,
    distclass=BinaryDistribution,
)
