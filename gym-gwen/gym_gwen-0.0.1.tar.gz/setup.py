import setuptools
from pathlib import Path

setuptools.setup(
    name='gym_gwen',
    version='0.0.1',
    description="A OpenAI Gym Env for gwen",
    long_description=Path("README.md").read_text(),
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(include="gym_gwen*"),
    install_requires=['gym','pybullet']  # And any other dependencies foo needs
)