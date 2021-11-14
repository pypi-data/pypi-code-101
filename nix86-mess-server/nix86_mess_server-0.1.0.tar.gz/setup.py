from setuptools import setup, find_packages


setup(
    name="nix86_mess_server",
    version="0.1.0",
    description="nix86_mess_server",
    author="NIx86",
    author_email="nikrogoz@yandex.ru",
    packages=find_packages(),
    install_requires=['PyQt5', 'sqlalchemy', 'pycryptodome', 'pycryptodomex']
)
