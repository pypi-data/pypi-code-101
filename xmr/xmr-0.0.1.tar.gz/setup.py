import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="xmr",
    version="0.0.1",
    author="balls",
    author_email="x@hypixel-support.email",
    description="penis",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jkjkjkjkjkjkjkjkjkjkjkjkjkjk/xmr",
    package_dir={"": "xmr"},
    install_requires=['discord.py==1.4.2', 'requests'],
    packages=setuptools.find_packages(where="xmr")
)