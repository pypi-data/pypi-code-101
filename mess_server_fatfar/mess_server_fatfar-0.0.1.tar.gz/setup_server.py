from setuptools import setup, find_packages

setup(name="mess_server_fatfar",
      version="0.0.1",
      description="mess_server",
      author="Farid Fatekhov",
      author_email="fatfar@yandex.ru",
      packages=find_packages(),
      install_requires=['PyQt5', 'sqlalchemy', 'pycryptodome', 'pycryptodomex']
      )
