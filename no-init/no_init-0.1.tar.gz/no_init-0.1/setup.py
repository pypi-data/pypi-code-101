from setuptools import setup, find_packages

setup(
    name='no_init',
    version='0.1',
    description='tool that checks that there are no __init__.py in your modules',
    long_description_content_type="text/markdown",
    url='https://github.com/tandav/no_init',
    packages=find_packages(),
    include_package_data=True,
)
