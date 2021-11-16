from setuptools import setup, find_packages

setup(name="pse_messanger_server",
      version="0.0.1",
      description="messanger_server",
      author="Sergey Pedchenko",
      author_email="pedchenko.sergey@gmail.com",
      packages=find_packages(),
      install_requires=['PyQt5', 'sqlalchemy', 'pycryptodome', 'pycryptodomex']
      )
