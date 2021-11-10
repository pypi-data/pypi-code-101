from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
  name = 'colordet2',
  version = 1.0,
  description = 'Detect colors from image',
  author = 'Jakub Zalewski',
  author_email = 'jakub.zetka11@gmail.com',
  long_description=long_description,  
  long_description_content_type="text/markdown",           
  packages = find_packages(),
  install_requires=[
          'numpy',
          'opencv-python',
      ],
)