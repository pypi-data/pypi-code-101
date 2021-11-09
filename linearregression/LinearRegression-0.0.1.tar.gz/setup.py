import pathlib
from setuptools import setup

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()
setup(
	name = "LinearRegression",
	version = "0.0.1",
	description = "Linear Regression From Scratch",
	long_description = README,

	long_description_content_type = "text/markdown",
	author = "Karthi Prasad",
	author_email = "Teamoctaholix@gmail.com",
	license = "MIT",
	packages = ["LinearRegression"],
	zip_safe = False
	)