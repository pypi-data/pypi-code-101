from setuptools import setup, find_packages

setup(name="massager_server",
      version="0.8.7",
      description="server_part",
      author="Buryan Ilya",
      author_email="forwow21@mail.ru",
      packages=find_packages(),
      install_requires=['PyQt5', 'sqlalchemy', 'pycryptodome', 'pycryptodomex']
      )
