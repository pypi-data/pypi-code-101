from setuptools import find_packages, setup
setup(
    name='hw5lib',
    packages=find_packages(include=['hw5lib']),
    version='1.0.1',
    description='HW5 Library',
    author='gnlm',
    license='MIT',
    install_requires=['pandas','sklearn','numpy','matplotlib'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
)