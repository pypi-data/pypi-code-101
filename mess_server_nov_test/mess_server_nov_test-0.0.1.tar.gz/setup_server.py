from setuptools import setup, find_packages

setup(name="mess_server_nov_test",
      version="0.0.1",
      description="mess_server_nov",
      author="Ivan Ivanov",
      author_email="iv.iv@yandex.ru",
      packages=find_packages(),
      install_requires=['PyQt5', 'sqlalchemy', 'pycryptodome', 'pycryptodomex']
      )
