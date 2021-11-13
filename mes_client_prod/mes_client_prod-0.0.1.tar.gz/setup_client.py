from setuptools import setup, find_packages

setup(name="mes_client_prod",
      version="0.0.1",
      description="mes_client_prod",
      author="Ruslan Zakirov",
      author_email="zakirovra@gmail.com",
      packages=find_packages(),
      install_requires=['PyQt5', 'sqlalchemy', 'pycryptodome', 'pycryptodomex']
      )
