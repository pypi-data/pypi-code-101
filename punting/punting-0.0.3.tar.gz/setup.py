import pathlib
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

setup(
    name="punting",
    version="0.0.3",
    description="Basic racing related utilities",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/microprediction/punting",
    author="microprediction",
    author_email="peter.cotton@microprediction.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.9",
    ],
    packages=["punting","punting.onedim","punting.twodim"],
    test_suite='pytest',
    tests_require=['pytest'],
    include_package_data=True,
    install_requires=["numpy","pytest","pathlib","wheel"],
    entry_points={
        "console_scripts": [
            "punting=punting.__main__:main",
        ]
    },
)
