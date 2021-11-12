from setuptools import setup, find_packages

setup(name="morerandoms",
    version="0.3",
    url="https://github.com/Wolframoviy/morerandom-py",
    license="MIT",
    author="WolframoviyI",
    author_email="arseniysstrim@gmail.com",
    description="More Random for God of Random!",
    long_description=open("README.md").read(),
    requires=["random"],
    packages=["morerandom"]
    )