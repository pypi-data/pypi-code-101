import setuptools


setuptools.setup(
    name='re_env',
    version='0.0.1',
    install_requires=['gym'],  # And any other dependencies foo needs
    packages=setuptools.find_packages(include='re_env'),
)