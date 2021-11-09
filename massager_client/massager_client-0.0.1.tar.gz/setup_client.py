from setuptools import setup, find_packages

setup(name="massager_client",
      version="0.0.1",
      description="client_part",
      author="Buryan_Ilya",
      author_email="forwow21@mail.ru",
      packages=find_packages(),
      install_requires=['PyQt5', 'sqlalchemy', 'pycryptodome', 'pycryptodomex']
      )
