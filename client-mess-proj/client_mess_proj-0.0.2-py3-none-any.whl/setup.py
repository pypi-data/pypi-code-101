from setuptools import setup, find_packages

setup(name="client_mess_proj",
      version="0.0.1",
      description="client_mess_proj",
      author="Ivan Ivanov",
      author_email="volga52@bk.ru",
      packages=find_packages(),
      install_requires=['PyQt5', 'sqlalchemy', 'pycryptodome', 'pycryptodomex']
      )
