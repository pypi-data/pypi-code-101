from setuptools import setup, find_packages

setup(
    name='no_init',
    version='v0.1.2',
    description='tool that checks that there are no __init__.py in your modules',
    long_description_content_type="text/markdown",
    url='https://github.com/tandav/no_init',
    # packages=find_packages(),
    py_modules=['no_init'],
    include_package_data=True,
)
