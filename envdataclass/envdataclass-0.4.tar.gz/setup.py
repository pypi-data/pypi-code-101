import pathlib

from setuptools import setup

HERE = pathlib.Path(__file__).parent
README = (HERE / 'readme.md').read_text()

setup(
    name='envdataclass',
    packages=['envdataclass'],
    version='0.4',
    long_description=README,
    long_description_content_type="text/markdown",
    license='MIT',
    author='briccardo',
    author_email='rbiagini02@gmail.com',
    description='Parses .env files against dataclass based schema validation',
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8",
    ],
    install_requires=[
        'python-dotenv',
    ]
)
