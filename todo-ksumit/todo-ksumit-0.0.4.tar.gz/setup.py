from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
  name='todo-ksumit',
  version='0.0.4',
  description='A perfect task manager.',
  py_modules=["todo"],
  packages=find_packages(),
  include_package_data=True,
  long_description=long_description,
  long_description_content_type='text/markdown',

  classifiers=[
    'Programming Language :: Python :: 3.10',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
  ],

  url='https://github.com/sumit-kushwah/todo-cli',
  author='Sumit kushwah',
  author_email='sumitkushwah1729@gmail.com',

  install_requires=[
    'Click',
    'tabulate'
  ],
  
  entry_points={
    'console_scripts': [
      't = src.cli:cli',
    ]
  },

  extras_require = {
    "dev": [
        'pytest >= 3.7',
        'check-manifest',
        'twine',
    ],
  },
)