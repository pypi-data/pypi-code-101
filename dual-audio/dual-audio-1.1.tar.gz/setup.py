# https://stackoverflow.com/q/64225196
from setuptools import setup, find_packages

with open("README.md", "r") as f:
  long_description = f.read()

setup(
  name = 'dual-audio',
  version = '1.1',
  description = 'Make videos with double audio',
  long_description = long_description,
  long_description_content_type = 'text/markdown',
  url = 'https://github.com/istudyatuni/dual-audio',
  author = 'Ilia',
  author_email = 'istudyatuni@gmail.com',
  packages = find_packages(),
  entry_points = {
    'console_scripts': [
      'dual-audio = dual_audio.main:main'
    ]
  },
  classifiers = [
    "Programming Language :: Python :: 3",
    "Environment :: Console",
  ],
  python_requires = '>=3',
  keywords = 'video movie audio dual-audio',
)
