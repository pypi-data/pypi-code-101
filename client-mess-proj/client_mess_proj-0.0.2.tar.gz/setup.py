from setuptools import setup, find_packages

setup(name="client_mess_proj",
      version="0.0.2",
      description="client_mess_proj",
      author="Esin Evgenii",
      author_email="volga52@bk.ru",
      packages=find_packages(),
      install_requires=['PyQt5', 'sqlalchemy', 'pycryptodome', 'pycryptodomex']
      )
