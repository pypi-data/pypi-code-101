import sys

if __name__=="__main__":
  sys.argv+=["sdist"]
from setuptools import find_packages,setup
from xes import version
setup(
    name = 'pygame-buttons',
    version = version.version,
    author = 'Ruoyu Wang',
    description = 'pygame按钮控件',
    packages = find_packages(),
    install_requires = ["pygments", "xes-lib", "pygame"],
    url = 'https://code.xueersi.com'
)