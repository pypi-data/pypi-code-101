from setuptools import setup

setup(
    name='myfds_package',  # package name
    version='0.5',  # version
    description='My first package',  # short description
    url='https://github.com/Ditmarscehen/myfds_package',  # package URL
    install_requires=['pandas==1.3.4',
                      'numpy<1.20.1'],  # list of packages this package depends
    # on.
    packages=['myfds_package'],  # List of module names that installing
    # this package will provide.
)

#pip install -i https://test.pypi.org/simple/ myfds-package==0.2