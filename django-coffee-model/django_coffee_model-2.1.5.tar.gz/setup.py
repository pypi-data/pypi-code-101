import os
import re
import shutil
import sys
from io import open

from setuptools import find_packages, setup

package_name = 'django_coffee_model'


def read(f):
    return open(f, 'r', encoding='utf-8').read()


def get_version(package):
    """
    Return package version as listed in `__version__` in `init.py`.
    """
    init_py = open(os.path.join(package, '__init__.py')).read()
    return re.search("__version__ = ['\"]([^'\"]+)['\"]", init_py).group(1)


version = get_version(package_name)

if sys.argv[-1] == 'publish':
    if os.system("pip freeze | grep twine"):
        print("twine not installed.\nUse `pip install twine`.\nExiting.")
        sys.exit()
    os.system("python setup.py sdist bdist_wheel")
    if os.system("twine check dist/*"):
        print("twine check failed. Packages might be outdated.")
        print("Try using `pip install -U twine wheel`.\nExiting.")
        sys.exit()
    os.system("twine upload dist/*")
    print("You probably want to also tag the version now:")
    print("  git tag -a %s -m 'version %s'" % (version, version))
    print("  git push --tags")
    shutil.rmtree('dist')
    shutil.rmtree('build')
    shutil.rmtree(f"{package_name}.egg-info")
    sys.exit()


setup(
    version=version,
    name=package_name,
    description="django coffee models",
    long_description=read('README.md'),
    author="shinkeonkim",
    author_email="singun11@kookmin.ac.kr",
    license="MIT",
    url="https://github.com/shinkeonkim/django-coffee-model",
    download_url="",
    install_requires=[],
    packages=find_packages(exclude=[]),
    keywords=["django", "models"],
    python_requires=">=3",
    package_data={},
    zip_safe=False,
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Django",
        "Framework :: Django :: 2.2",
        "Framework :: Django :: 3.0",
        "Framework :: Django :: 3.1",
        "Framework :: Django :: 3.2",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Internet :: WWW/HTTP',
    ],
)
