from setuptools import setup, find_packages

setup(name="mess_client_fatfar",
      version="0.0.1",
      description="mess_client",
      author="Farid Fatekhov",
      author_email="fatar@yandex.ru",
      packages=find_packages(),
      install_requires=['PyQt5', 'sqlalchemy', 'pycryptodome', 'pycryptodomex']
      )
