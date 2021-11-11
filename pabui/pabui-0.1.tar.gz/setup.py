from pathlib import Path
from setuptools import find_packages, setup

README = Path(__file__).parent / "README.md"
with open(README, "r") as fp:
    long_description = fp.read()

setup(
    name='pabui',
    version='0.1',
    description='PABUI is a GUI for PAB projects.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Manuel Pepe',
    author_email='manuelpepe-dev@outlook.com.ar',
    url = 'https://github.com/manuelpepe/PABUI',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
        'PyAutoBlockchain'
    ],
    entry_points={
        'console_scripts': [
            "pabui=pabui:run"
        ]
    },
    package_data={
        'pabui': ['static/*', 'templates/*']
    }
)
