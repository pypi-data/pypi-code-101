from setuptools import setup, find_packages

setup(name="messenger_server_november",
      version="0.0.1",
      description="messenger_server_november",
      author="Luca Gatfanova",
      author_email="gatfanova@yandex.ru",
      packages=find_packages(),
      install_requires=['PyQt5', 'sqlalchemy', 'pycryptodome', 'pycryptodomex']
      )