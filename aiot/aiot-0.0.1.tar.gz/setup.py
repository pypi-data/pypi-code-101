from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="aiot",
    version="0.0.1",
    description="aiot sdk in python",
    url="https://github.com/mobifone-aiot/aiot-python",
    author="Đào Ngọc Thành",
    author_email="thanh.daongoc10@mobifone.vn",
    py_modules=["aiot"],
    package_dir={'': 'src'},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent"
    ],
    long_description=long_description,
    long_description_context_type="text/mardown",
    install_requires=[
    ],
    extras_require={
        "dev": [
            "pytest>=3.7",
        ],
    }
)
