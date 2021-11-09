from setuptools import setup, find_packages


setup(
    name="pynuctran",
    version="1.55.1021",
    author="M. R. Omar",
    author_email="rabieomar@live.com",
    description="Python library for nuclear transmutation simulations.",
    url='https://github.com/rabieomar92/pynuctran',
    license='MIT',
    install_requires=['numpy','scipy'],
    packages=find_packages(include=['pynuctran']),
)