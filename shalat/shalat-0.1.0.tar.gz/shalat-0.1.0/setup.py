from distutils.core import setup
import os
from setuptools import find_packages

def read_file(path):
	content = ""
	with open(path, encoding='utf-8') as f:
		content = f.read()
	return content

# User-friendly description from README.md
current_directory = os.path.dirname(os.path.abspath(__file__))
try:
    long_description = read_file(os.path.join(current_directory, 'README.md'))
except Exception:
    long_description = ''

setup(
	# Name of the package
	name='shalat',
	# Packages to include into the distribution
	packages=find_packages('.'),
	# Start with a small number and increase it with
	# every change you make https://semver.org
	version='0.1.0',
	# Short description of your library
	description='Shalat time calculation',
	# Long description of your library
	long_description=long_description,
	long_description_content_type='text/markdown',
	# Your name
	author='Haxors',
	# Your email
	author_email='hanzhaxors@gmail.com',
	# Either the link to your github or to your website
	url='https://github.com/HanzHaxors/shalat',
	# List of keywords
	keywords=[],
	# List of packages to install with this one
	install_requires=[],
	# https://pypi.org/classifiers/
	classifiers=[
		"License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
		"Development Status :: 1 - Planning",
		"Intended Audience :: Developers",
		"Intended Audience :: Religion",
		"Intended Audience :: Science/Research",
		"Programming Language :: Python :: 3 :: Only",
		"Topic :: Scientific/Engineering :: Astronomy",
		"Topic :: Software Development :: Libraries"
	]
)
