import os

import setuptools


def package_files(directory):
  paths = []
  for (path, directories, filenames) in os.walk(directory):
    for filename in filenames:
      paths.append(os.path.join('..', path, filename))
  return paths


descriptor_files = package_files('kama_telem_plugin/descriptors')
asset_files = package_files('kama_telem_plugin/assets')

with open("README.md", "r") as fh:
  long_description = fh.read()


setuptools.setup(
  name="kama-telem-plugin",
  version="0.0.7",
  author="NMachine",
  author_email="xavier@nmachine.io",
  description="Telemetry plugin for the kama-sdk-py",
  long_description=long_description,
  long_description_content_type="text/markdown",
  url="https://github.com/nmachine-io/kama-sdk-py",
  packages=setuptools.find_packages(exclude=['kama_sdk']),
  package_data={
    '': descriptor_files + asset_files
    # 'kama_telem_plugin': [
    #   'assets/*.*',
    #   'descriptors'
    # ]
  },
  include_package_data=True,
  install_requires=[
    'kama-sdk-py',
  ],
  classifiers=[
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
  ],
  python_requires='>=3.8'
)
