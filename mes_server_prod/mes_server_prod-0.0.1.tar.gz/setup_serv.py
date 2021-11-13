from setuptools import setup, find_packages

setup(name="mes_server_prod",
      version="0.0.1",
      description="mes_server_prod",
      author="Ruslan Zakirov",
      author_email="zakirovra@gmail.com",
      packages=find_packages(),
      install_requires=['PyQt5', 'sqlalchemy', 'pycryptodome', 'pycryptodomex']
      )