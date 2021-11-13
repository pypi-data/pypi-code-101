from setuptools import setup, find_packages

setup(name="client_for_messenger",
      version="0.0.1",
      description="client_for_messenger",
      author="Tina",
      author_email="tina@yandex.ru",
      packages=find_packages(),
      install_requires=['PyQt5', 'sqlalchemy', 'pycryptodome', 'pycryptodomex']
      )
