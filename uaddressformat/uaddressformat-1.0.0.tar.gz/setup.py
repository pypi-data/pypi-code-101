try:
    from setuptools import setup
except ImportError:
    raise ImportError(
        "setuptools module required, please go to "
        "https://pypi.python.org/pypi/setuptools and follow the instructions "
        "for installing setuptools"
    )

setup(
    name='uaddressformat',
    description='Library for uaddress package. Format types addresses',
    version='1.0.0',
    author='Evgen Kytonin',
    license='MIT',
    keywords=['module', 'parse', 'uaddress'],
    url='https://github.com/martinjack/uaddressformat',
    packages=['uaddressformat']
)